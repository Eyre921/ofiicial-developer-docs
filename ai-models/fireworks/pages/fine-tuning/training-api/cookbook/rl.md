---
title: "Cookbook: Reinforcement Learning"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/rl
path: fine-tuning/training-api/cookbook/rl
---

Run experimental async GRPO with a custom rollout function while the recipe owns scheduling, training, and weight publication.

The cookbook's primary RL recipe is [`async_rl_loop`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/async_rl_loop.py). You provide dataset rows and a rollout function; the recipe runs rollout production independently from serialized training. When a rollout finishes, the producer immediately tries to refill available capacity—even while forward/backward or optimizer work is running.

<Warning>
  `async_rl_loop` is experimental. Its configuration and rollout protocol may
  change without backward-compatibility shims. Pin the cookbook version for
  production workloads.
</Warning>

## Responsibilities

| You provide                                                | The recipe owns                                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Dataset rows through `Config.dataset` or `rows=`           | Trainer and deployment setup, cleanup, and initial weight sync                     |
| `rollout_fn_factory(setup) -> rollout_fn`                  | Rollout fan-out, admission, grouping, and advantages                               |
| Environment interaction, scoring, and aligned rollout data | Reference and old-policy forwards, GRPO/TIS/KL, and optimizer steps                |
| Scheduling and algorithm configuration                     | Training chunks, sampler hotload and version publication, metrics, and checkpoints |
| Optional `dynamic_filter_fn`                               | Bounded handling of transient rollout failures                                     |

## Minimal setup

```python theme={null}
from training.examples.rl.single_turn_token_in.rollout import make_rollout_fn
from training.recipes.async_rl_loop import Config, main
from training.utils import DeployConfig, TrainerConfig

cfg = Config(
    log_path="./async-rl-logs",
    base_model="accounts/<account>/models/<model>",
    completions_per_prompt=8,
    prompt_groups_per_step=8,
    pipeline_chunks_per_step=4,
    max_head_offpolicy_versions=2,
    max_concurrency_rollout_sample=128,
    trainer=TrainerConfig(
        training_shape_id="accounts/<account>/trainingShapes/<shape>",
    ),
    deployment=DeployConfig(tokenizer_model="<tokenizer>"),
)

rows = [...]  # Each row is passed to rollout_fn as sample_prompt.
main(cfg, rollout_fn_factory=make_rollout_fn, rows=rows)
```

The example rollout above expects rows with `prompt_token_ids`. Fork the [single-turn example](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/single_turn_token_in) or [multi-turn example](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/multi_turn_message_in) for your environment.

For multi-turn agents, tools, sandboxes, token ancestry, and session design, read
[Cookbook: Agentic Reinforcement Learning](/fine-tuning/training-api/cookbook/agentic-rl).
Agentic RL is a rollout integration concern; it does not change the async
loop's scheduling contract.

## Rollout contract

The factory receives `RolloutSetup` once and returns an async function:

```python theme={null}
from training.recipes.async_rl_loop import RolloutFn, RolloutSetup
from training.utils.rl.rollout import RolloutRun


def make_rollout_fn(setup: RolloutSetup) -> RolloutFn:
    async def rollout_fn(sample_prompt: dict) -> RolloutRun | None:
        ...

    return rollout_fn
```

The recipe calls `rollout_fn` `completions_per_prompt` times for each dataset row. One call represents one trajectory and returns:

* `RolloutRun(segments=[...])` on success. A run contains one or more `RolloutSample` segments from the same trajectory.
* `None` to drop that trajectory draw.

Each segment carries aligned `tokens`, `logprobs`, and `loss_mask` lists plus a scalar `reward`. Set the mask to `1` only for tokens that should contribute to training. All segments in one run must have the same reward.

## Scheduling controls

These five fields define the rollout/training pipeline:

| Field                            | Default | Meaning                                                                                           |
| -------------------------------- | ------: | ------------------------------------------------------------------------------------------------- |
| `completions_per_prompt`         |     `4` | Trajectories per dataset row. Must be at least `2`.                                               |
| `prompt_groups_per_step`         |     `1` | Dataset rows grouped into one optimizer batch.                                                    |
| `pipeline_chunks_per_step`       |     `1` | Balanced forward/backward chunks prepared for each optimizer batch.                               |
| `max_head_offpolicy_versions`    |     `0` | Number of published policy versions that rollout admission may run ahead. `0` is fully on-policy. |
| `max_concurrency_rollout_sample` |  `None` | Optional cap on in-flight rollout calls. It must fit at least one complete row.                   |

Admission is row-atomic: the scheduler submits a row only when both the staleness budget and concurrency budget can fit all of its completions. `max_head_offpolicy_versions=0` is fully on-policy: every optimizer batch trains groups from its current published policy version. Chunk training can still overlap remaining rollouts from the same optimizer batch.

## Runtime behavior

1. The recipe syncs initial policy weights to the sampler.
2. The producer submits complete rows while both admission budgets allow it.
3. Every completed rollout retries refill. As soon as the first training chunk is ready, serialized trainer work can begin while rollout production continues.
4. Later chunks queue and run in order. One optimizer step follows the final chunk.
5. The recipe hotloads the updated weights and publishes the next policy version. Publication reopens staleness capacity.

There is one sampler hotload per optimizer batch; `async_rl_loop` does not expose a weight-sync interval. Known transient rollout failures are dropped behind a bounded circuit breaker. Invalid rollout data, unexpected cancellation, and unknown errors remain fatal.

## Loss behavior

The stock recipe has one direct client-side GRPO path and no `policy_loss` or `loss_path` selector. `anchor_logp="old_policy"` (the default) snapshots trainer logprobs and applies TIS against rollout behavior logprobs; `anchor_logp="rollout"` reuses aligned rollout logprobs and makes the TIS ratio identity. Set `kl_beta=0` to disable reference-policy KL and reference provisioning.

## Detailed reference

Keep implementation and tuning detail out of the recipe page:

* [Async RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-async.md) — admission math, metrics, tuning, failure policy, and resume semantics
* [Agentic RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-agentic.md) — multi-turn token ancestry, session/cache architectures, mismatch policies, and trace failures
* [Custom RL loss reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-custom-loss.md) — fork the recipe deliberately when you need a trainer built-in or another research objective
* [Checkpointing](/fine-tuning/training-api/cookbook/checkpoints) — resumable checkpoints and final model promotion
* [Weight sync](/fine-tuning/training-api/cookbook/weight-sync) — how updated policy weights reach the sampler
* [`rl_loop`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/rl_loop.py) — simpler synchronous GRPO when rollout/training overlap is unnecessary
