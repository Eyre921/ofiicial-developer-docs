---
title: "RL parameters reference"
source: https://docs.fireworks.ai/fine-tuning/rft-parameters-reference
path: fine-tuning/rft-parameters-reference
---

Checkpoint, resume, and GRPO metrics fields for reinforcement learning recipes.

Use this page for training **checkpoint and resume** knobs and **GRPO metric interpretation** that are easy to miss when running cookbook-driven reinforcement learning. For sampling and scheduling configuration (completions per prompt, staleness budget, concurrency, loss behavior), see [Cookbook: Reinforcement Learning](/fine-tuning/training-api/cookbook/rl#scheduling-controls).

The canonical cookbook reference for save, resume, and promote is [Checkpoints and Resume](/fine-tuning/training-api/cookbook/reference#checkpoints). Low-level SDK APIs are documented in [Saving and loading](/fine-tuning/training-api/dedicated#saving-and-loading).

## `dcp_save_interval`

Controls how often full training state (weights **and** optimizer) is checkpointed using DCP (Distributed Checkpoint) format.

| Property | Value |
| - | - |
| **Type** | `integer` |
| **Default** | `0` (disabled) |
| **Typical config — SFT / RL / DPO cookbooks** | `Config(dcp_save_interval=N)` (see [Cookbook: RL](/fine-tuning/training-api/cookbook/rl) and [Checkpoints](/fine-tuning/training-api/cookbook/reference#checkpoints)) |

When set to `0` (the default), no periodic DCP checkpoints are written for resume. A successful run still saves final resumable training state by default. Sampler snapshots alone preserve weights but not optimizer state.

When set to a positive integer `N`, a full DCP checkpoint is written every `N` steps.

**Why this matters:** An interrupted run can resume only from saved training state. Enable periodic saves to bound lost progress; weights-only initialization starts a fresh optimizer.

### Example (cookbook `Config`)

```python theme={null}
from training.recipes.rl_loop import Config, main

cfg = Config(
    log_path="./grpo_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    # ... other fields ...
    dcp_save_interval=50,  # full checkpoint every 50 steps
    # ...
)
main(cfg)
```

See the recipe’s `Config` dataclass for its checkpoint fields.

### Job recovery and preemption

For transient control-plane or worker interruptions, the trainer job manager exposes [`reconnect_and_wait`](/fine-tuning/training-api/reference/trainer-job-manager) so your driver can wait for a resumable state and resume cleanly.

<Note>
  `load_state_with_optimizer()` only restores optimizer state from DCP-format checkpoints. HF or sampler snapshots are not resumable optimizer checkpoints. Always load from the path returned by `save_state()` when you need full optimizer restore. See [Saving and loading](/fine-tuning/training-api/dedicated#saving-and-loading).
</Note>

***

## Metrics reference

### Policy and inference diagnostics

| Metric | What it measures |
| - | - |
| `train/ppo_kl` | Policy-ratio diagnostic against the rollout logprobs used as the clipping anchor. |
| `train/inference_k3` | Train-versus-inference logprob discrepancy on trained tokens. |

The default GRPO recipe has no reference model or reference-KL penalty. A small
policy-ratio diagnostic on an on-policy batch is expected; it does not measure
divergence from a frozen base model. Client request timings include transport
and queueing and can overlap, so compare the full optimizer window separately
from trainer execution time. Metric definitions and reductions live in the
[step-metrics skill](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/step-metrics.md).
