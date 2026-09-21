---
title: "Cookbook: Fireworks x HUD RL Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/hud-rl-training
path: fine-tuning/training-api/cookbook/hud-rl-training
---

Train a LoRA adapter with reinforcement learning using HUD environments and Fireworks Serverless Training.

This guide shows how to train a LoRA adapter with reinforcement learning using
a [HUD environment](https://docs.hud.ai/v6/guides/creating-an-environment?utm_source=fireworks\&utm_medium=partner\&utm_content=cookbook)
and the [Fireworks Serverless Training API](/fine-tuning/training-api/serverless).
You define the task and grader in HUD; the
[HUD Fireworks cookbook](https://github.com/hud-evals/hud-python/tree/main/cookbooks/fireworks-rl-training)
handles the training loop and connection to Fireworks.

Each rollout produces a reward from the HUD grader and a trace containing the
exact token IDs sampled by the model. The cookbook converts those results into
Fireworks training datums and uses them to update the model.

The example trains a Qwen 3.8 27B LoRA adapter on four-digit multiplication in
a local environment, with one model response per rollout. Multiplication is a
stand-in for any one-turn capability that can be expressed as tasks with a
programmatic grader: answers are easy to check automatically, and the base
model makes enough mistakes to provide useful training signal.

## The environment

HUD runs the rollouts, and Fireworks provides the training infrastructure that
turns them into model updates. You write a
[HUD environment](https://docs.hud.ai/v6/guides/creating-an-environment?utm_source=fireworks\&utm_medium=partner\&utm_content=cookbook)
containing the task template, its parameters, and the grader. The same task
definition can serve both training and held-out evaluation.

A HUD environment is a small Python module with an `Environment` and one or
more task templates. A template yields a prompt, receives the model response,
and yields a grade:

```python theme={null}
@env.template()
async def multiply(a: int, b: int):
    answer = yield (
        f"What is {a} * {b}? Work it out, then put the final integer on its "
        "own line at the end of your answer."
    )
    yield grade_final_integer(answer, a * b)
```

The parameters `a` and `b` define the task, the first `yield` emits the prompt,
and the second emits the reward.

## Quickstart

### Step 1: Install and authenticate

You need Git, Python 3.11 or 3.12,
[`uv`](https://docs.astral.sh/uv/getting-started/installation/), and a Fireworks
API key from the [Fireworks dashboard](https://app.fireworks.ai/).

```bash theme={null}
git clone https://github.com/hud-evals/hud-python.git
cd hud-python/cookbooks/fireworks-rl-training
uv sync
export FIREWORKS_API_KEY="fw_..."
```

Run the remaining commands from this directory. You can instead put
`FIREWORKS_API_KEY` in a local `.env` file. The bundled environment runs
locally and does not require a HUD API key.

The cookbook installs `fireworks-ai[training]>=1.2.11` and
`tinker-cookbook>=0.5.7`. Its model defaults are:

| Setting             | Value                                   |
| ------------------- | --------------------------------------- |
| `--base-model`      | `accounts/fireworks/models/qwen3p8-27b` |
| `--tokenizer-model` | `Qwen/Qwen3.8-27B`                      |
| `--renderer`        | `qwen3_8_disable_thinking`              |

Prompt rendering happens on the client. If you change the model, pass a
matching tokenizer and renderer with these flags. The default renderer
disables thinking mode. `--max-tokens` still limits the entire generated
response.

### Step 2: Calibrate the task

Sample repeated attempts before taking an optimizer step:

```bash theme={null}
uv run train.py \
  --calibrate \
  --tasks-per-step 6 \
  --group-size 4 \
  --max-tokens 2048 \
  --debug-samples 4
```

This collects 24 runs from the initial adapter and reports:

| Metric                    | Meaning                                                         |
| ------------------------- | --------------------------------------------------------------- |
| `reward_mean`             | Fraction of correct answers for this binary-reward task         |
| `within_group_reward_std` | Mean reward standard deviation across attempts at the same task |

The cookbook only sends an update when attempts at the same task have reward
variation. If every run in a group has the same reward, that group contributes
no gradient. This is also why `--group-size` must be at least `2`.

Inspect the full responses printed by `--debug-samples` and confirm that their
rewards match answer quality:

* If every answer is correct, widen the operand range with `--min-a`,
  `--max-a`, `--min-b`, and `--max-b`.
* If every answer is incorrect, narrow the range or increase `--max-tokens`.
* Check output-token counts. A response cut off at the token limit might never
  reach its final answer.

Training samples at temperature `1.0` by default so groups can vary.
Evaluation always samples at temperature `0`.

### Step 3: Run one training step

After calibration shows reward variation, verify the complete path with one
training step:

```bash theme={null}
uv run train.py \
  --steps 1 \
  --tasks-per-step 2 \
  --group-size 4 \
  --max-tokens 2048 \
  --eval-tasks 4 \
  --require-update
```

This requests eight training runs and four held-out evaluation runs.
`--require-update` fails if the step has no groups with reward variation. A
successful step applies an optimizer update, saves sampler and training
checkpoints, and prints the held-out reward.

The step log reports `kept_groups`, `datums`, and `updated`. Detailed metrics,
including `reward_std_within_group`, are written to
`runs/fireworks-serverless/metrics.jsonl`. If any rollout fails to complete or
grade, the script stops and reports how many attempts failed rather than
treating them as zero-reward examples.

### Step 4: Run a longer experiment

```bash theme={null}
uv run train.py
```

The defaults repeat eight task pairs for 30 steps with eight runs per task per
step: 1,920 training runs followed by 16 held-out evaluation runs. Each
response has a 2,048-token generation limit. Training checkpoints are saved
every five steps and at the end. Steps whose groups all have identical rewards
skip the optimizer.

<Warning>
  Calibration and training both incur Fireworks usage. Review
  [Serverless Training pricing](/fine-tuning/training-api/serverless#pricing)
  before running a large experiment. `--max-concurrent` controls how many
  rollouts run simultaneously and defaults to `4`.
</Warning>

## Compare before and after training

Use `--eval-before` to evaluate the initial and final adapters on the same
held-out task set:

```bash theme={null}
uv run train.py --eval-before \
  --steps 8 --tasks-per-step 16 --group-size 4 \
  --eval-tasks 128 --seed 42 --max-tokens 2048 \
  --max-concurrent 8 --output-dir runs/before-after
```

This requests 512 training runs and 256 evaluation runs. In one run, eight RL
updates improved Qwen 3.8 27B accuracy on the 128 held-out multiplication
tasks:

| Held-out metric              |          Before |           After |
| ---------------------------- | --------------: | --------------: |
| Correct answers              | 100/128 (78.1%) | 126/128 (98.4%) |
| Invalid final line           |              19 |               0 |
| Wrong valid integer          |               9 |               2 |
| Responses at the token limit |              20 |               0 |
| Mean output tokens           |           1,085 |             704 |

Most of the gain came from the model learning to finish within the token
budget. Of the 27 improved tasks, 20 had baseline responses that reached the
token limit before producing an answer. Seven improvements were arithmetic
corrections.

<Note>
  This is one run on a narrow arithmetic distribution. It does not establish
  broader capability gains or run-to-run reproducibility.
</Note>

The output directory contains `config.json`, `eval-before.json`, and
`eval-after.json`. Each evaluation records prompts, full responses, rewards,
grader information, output-token counts, and whether responses reached the
token limit.

## Define the task and reward

The bundled `env.py` grades the integer on the last nonempty line:

```python theme={null}
import re

from hud import Environment
from hud.graders import EvaluationResult

env = Environment(name="fireworks-arithmetic")


def grade_final_integer(answer: object, expected: int) -> EvaluationResult:
    text = (answer if isinstance(answer, str) else str(answer)).strip()
    final = text.splitlines()[-1].strip() if text else ""
    got = (
        int(final.replace(",", ""))
        if re.fullmatch(r"[+-]?(?:\d+|\d{1,3}(?:,\d{3})+)", final)
        else None
    )
    return EvaluationResult(
        reward=1.0 if got == expected else 0.0,
        content=text,
        info={"expected": expected, "got": got},
    )
```

A wrong integer, a missing final line, or a response cut off before its answer
all score `0`. Replace the prompt and grader to define your own objective. HUD
uses the same grader during training and held-out evaluation.

## How rollouts become updates

For each task, the cookbook saves the current adapter and opens a Fireworks
sampler bound to that snapshot. `FireworksAgent` renders the task prompt,
samples one assistant turn, and records the exact prompt tokens, output tokens,
and sampling log probabilities on the HUD run. The HUD environment grades the
response and returns a reward.

HUD repeats each task with `taskset.run(..., group=group_size)`. The cookbook
turns the rewards and token IDs into Fireworks training datums. Prompt tokens
are masked from the loss. Sampled output tokens carry the rollout log
probabilities and each rollout's advantage, normalized within its task group.

The optimizer portion of `train.py` follows this pattern:

```python theme={null}
datums, kept_groups = make_training_batch(runs)
if datums:
    training_client.forward_backward(datums, "importance_sampling").result()
    training_client.optim_step(adam).result()
```

The default loss is Fireworks `importance_sampling`. Use `--loss-fn` to select
`ppo` or `cispo`. The next step samples from a newly saved snapshot of the
updated adapter.

## Checkpoint and resume

The script creates two checkpoint types:

| Checkpoint                          | Contents                            | Use                                    |
| ----------------------------------- | ----------------------------------- | -------------------------------------- |
| Sampler (`policy-*`, `final`)       | Adapter weights                     | Sample responses or promote to a model |
| Training (`state-*`, `final-state`) | Adapter weights and optimizer state | Resume training                        |

Each training checkpoint's full path is printed when it is saved. Periodic
`state-NNNN` checkpoints are saved every five steps by default, followed by
`final-state`. Pass a printed path to resume:

```bash theme={null}
uv run train.py --resume-from "<account>/<run-id>/final-state"
```

Resume restores the checkpoint's base model and optimizer state in a new run.
For models other than Qwen 3.8 27B, pass matching `--tokenizer-model` and
`--renderer` values. To change base models, start a new run.

Sampler checkpoints are session-scoped. To retain an adapter for serving,
[promote the checkpoint](/fine-tuning/training-api/serverless#promote-a-sampler-checkpoint-to-a-model)
while the session and trainer are still available.

## Use another one-turn task

For another local one-turn text task, pass the task file and environment
source:

```bash theme={null}
uv run train.py \
  --tasks-file "../my-environment/tasks.py" \
  --env-path "../my-environment/env.py" \
  --calibrate \
  --tasks-per-step 6 \
  --group-size 4
```

For an environment already deployed to HUD with a synced task set, set
`HUD_API_KEY` and select its name or ID:

```bash theme={null}
export HUD_API_KEY="sk-hud-..."
uv run train.py \
  --taskset "my-taskset" \
  --calibrate \
  --tasks-per-step 6 \
  --group-size 4
```

On the hosted path, HUD still owns the episode and grade, while the Fireworks
sampler is called from your training process. Calibration requires at least
`--tasks-per-step` tasks. Training requires `--tasks-per-step + --eval-tasks`.
The script shuffles the task set with a fixed seed and selects disjoint
training and evaluation subsets.

The bundled adapter supports one generated assistant turn per run. Multi-turn
or tool-using tasks require a custom adapter that executes those calls and
retains tokens, log probabilities, and loss masks for every assistant turn.
See [Cookbook: Agentic Reinforcement Learning](/fine-tuning/training-api/cookbook/agentic-rl)
for the Fireworks requirements.

## Next steps

* [Explore Serverless Training](/fine-tuning/training-api/serverless) for
  supported models, lifecycle, pricing, and checkpoint operations.
* Review the complete
  [HUD Fireworks cookbook](https://github.com/hud-evals/hud-python/tree/main/cookbooks/fireworks-rl-training)
  source, CLI options, and tests.
* [Build a HUD environment](https://docs.hud.ai/v6/guides/creating-an-environment?utm_source=fireworks\&utm_medium=partner\&utm_content=cookbook)
  with your own tasks, capabilities, and graders.
* Read HUD's guidance on
  [designing tasks for training signal](https://docs.hud.ai/v6/reference/advice?utm_source=fireworks\&utm_medium=partner\&utm_content=cookbook).
