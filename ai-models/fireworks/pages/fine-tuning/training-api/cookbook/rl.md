---
title: "Async GRPO reinforcement learning cookbook recipe"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/rl
path: fine-tuning/training-api/cookbook/rl
---

Run the experimental async GRPO cookbook recipe with a custom rollout function while Fireworks handles scheduling, training, checkpoints, and weight sync.

The cookbook's primary RL recipe is [`async_rl_loop`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/async_rl_loop.py). You provide dataset rows and a rollout function; the recipe overlaps rollout production with training submission. When a rollout finishes, the producer immediately tries to refill available capacity—even while forward/backward or optimizer work is running.

<Warning>
  `async_rl_loop` is experimental. Its configuration and rollout protocol may
  change without backward-compatibility shims. This page describes the current
  Cookbook and its declared SDK dependencies; pin the Cookbook commit and SDK
  version for reproducible workloads.
</Warning>

For the shared serverless pool, use the experimental
[`async_rl_loop_serverless` adapter](https://github.com/fw-ai/cookbook/blob/main/training/recipes/experiment/async_rl_loop_serverless.py).
It keeps this recipe's rollout and scheduling contract but replaces dedicated
resource lifecycle and hotloading with session-scoped snapshots. The two paths
remain separate until they share one weight-publication contract. See
[Serverless Training](/fine-tuning/training-api/serverless) for lifecycle and
limits.

## Responsibilities

| You provide | The recipe owns |
| - | - |
| Dataset rows through `Config.dataset` or `rows=` | Trainer and deployment setup, cleanup, and initial weight sync |
| `rollout_fn_factory(setup) -> rollout_fn` | Rollout fan-out, admission, grouping, and advantages |
| Environment interaction, scoring, and aligned rollout data | Built-in GRPO loss and one optimizer update per batch |
| Scheduling and algorithm configuration | Ready-group submission, sampler hotload, structured metrics, and checkpoints |
| Optional `dynamic_filter_fn` and `evaluation_fn` | Bounded failure handling, evaluation scheduling, and final-step deduplication |

## Minimal setup

```python theme={null}
from training.examples.rl.deepmath.train_deepmath import make_rollout_fn
from training.recipes.async_rl_loop import Config, main
from training.utils import DeployConfig, TrainerConfig

cfg = Config(
    log_path="./async-rl-logs",
    base_model="accounts/<account>/models/<model>",
    completions_per_prompt=8,
    prompt_groups_per_step=8,
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

The [DeepMath example](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/deepmath)
expects rows with chat `messages` and `ground_truth` answers. Fork its adapter
to supply another task and reward. For multi-turn harnesses, tools, sandboxes, and exact
token ancestry, read
[Cookbook: Agentic Reinforcement Learning](/fine-tuning/training-api/cookbook/agentic-rl).
Agentic RL changes the rollout adapter, not this async scheduling and training
contract.

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

These fields define the rollout/training pipeline:

| Field | Default | Meaning |
| - | -: | - |
| `completions_per_prompt` | `4` | Trajectories per dataset row. Must be at least `2`. |
| `prompt_groups_per_step` | `1` | Dataset rows grouped into one optimizer batch. |
| `max_head_offpolicy_versions` | `0` | Number of published policy versions that rollout admission may run ahead. `0` is fully on-policy. |
| `max_concurrency_rollout_sample` | `None` | Optional cap on in-flight rollout calls. It must fit at least one complete row. |
| `min_group_size` | `1` | Minimum surviving rollout runs required to train a row. |
| `max_incomplete_group_retries` | `0` | Number of times to rebuild a row that finishes below `min_group_size`. |

Admission is row-atomic: the scheduler submits a row only when both the
staleness budget and concurrency budget can fit all of its completions.
`max_concurrency_rollout_sample` counts active `rollout_fn` calls, not the
individual inference requests that a multi-turn agent makes. The shared
`DeploymentSampler` owns inference-request concurrency separately.
`max_head_offpolicy_versions=0` is fully on-policy: every optimizer batch
trains groups from its current published policy version. Training submission can
still overlap remaining rollouts from the same optimizer batch. The synchronous
[`rl_loop`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/rl_loop.py)
collects the full batch before training it.

## Runtime behavior

1. The recipe syncs initial policy weights to the sampler.
2. The producer submits complete rows while both admission budgets allow it.
3. Every completed rollout retries refill. As soon as a complete group is ready, training submission can begin while rollouts continue. Each submission combines all groups currently ready in that batch, with no collection timer.
4. Requests can remain pending together. One optimizer step follows only after every backward in the batch succeeds.
5. The recipe waits for evaluation on the current sampler version before replacing that version, hotloads the updated weights, and publishes the next policy version. Publication reopens staleness capacity.

There is one sampler hotload per optimizer batch; `async_rl_loop` does not
expose a weight-sync interval. The final partial optimizer batch is trained
rather than discarded. Known transient rollout failures are dropped behind a
bounded circuit breaker. Invalid rollout data, unexpected cancellation, and
unknown errors remain fatal. A row may still train after recoverable failures
when at least `min_group_size` runs survive.

## Loss behavior

The reference loops use the trainer's built-in clipped GRPO loss against the
logprobs captured during rollout, with no reference-model KL penalty. Advantages
are normalized within each prompt group. All backward requests accumulate into
one optimizer update; gradients are normalized by the batch's trainable-token
count once. SFT, DPO, and ORPO retain controlled dataset batches.

Fork the recipe to change the objective, anchor, or correction. See the
[custom-loss skill](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-custom-loss.md).

## Evaluation

Pass `evaluation_fn(step, rollout_fn)` and `evaluation_interval=N` to `main()`.
Evaluation runs at the initial or resumed step, at each interval, and once at
the actual final step without duplicating a periodic evaluation at that step.
It uses the same rollout object, sampler, `max_completion_tokens`, and resolved
`max_seq_len` as training, but it does not enter training groups or mutate the
optimizer. Evaluation is fail-open. It can overlap the next batch's rollout and
trainer work, but it must finish before that sampler version is replaced, so a
slow evaluation can delay weight publication.

## Interruptions and cleanup

The dedicated sync and async recipes and the serverless async adapter handle
`SIGINT` and `SIGTERM` throughout setup, training, final saves, and cleanup.
The first signal stops new work, waits for native calls already in progress,
and unwinds cleanup according to the recipe's resource settings. Rollout
cleanup runs before sampler and service closure. A second
signal exits immediately and may leave remote resources running. The recipes
restore the caller's signal handlers when they return.

Interrupting a run does not guarantee a new final checkpoint. Set a positive
`dcp_save_interval` to preserve resumable state during training; see
[Checkpointing](/fine-tuning/training-api/cookbook/reference#checkpoints).

## Detailed reference

Keep implementation and tuning detail out of the recipe page:

* [Async RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-async.md) — admission math, metrics, tuning, failure policy, and resume semantics
* [Agentic RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-agentic.md) — multi-turn token ancestry, session/cache architectures, mismatch policies, and trace failures
* [Custom RL loss reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-custom-loss.md) — fork the recipe deliberately when you need a trainer built-in or another research objective
* [Checkpointing](/fine-tuning/training-api/cookbook/reference#checkpoints) — resumable checkpoints and final model promotion
* [Weight sync](/fine-tuning/training-api/cookbook/reference#weight-sync) — how updated policy weights reach the sampler
* [`rl_loop`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/rl_loop.py) — simpler synchronous GRPO when rollout/training overlap is unnecessary

## IGPO (Information Gain Policy Optimization)

IGPO prepares turn-level advantages through
`rl_loop.main(..., prepare_batch_fn=igpo.prepare_batch(gamma=...))`. Answer
scoring runs across the complete batch while advantage normalization remains
group-local. Start with the [multi-hop QA example](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/multihop_qa).
