---
title: "RFT parameters reference"
source: https://docs.fireworks.ai/fine-tuning/rft-parameters-reference
path: fine-tuning/rft-parameters-reference
---

Checkpoint, resume, and GRPO metrics fields for reinforcement fine-tuning recipes.

Use this page for training **checkpoint and resume** knobs and **GRPO metric interpretation** that are easy to miss when running reinforcement fine-tuning (RFT) and cookbook-driven training. For sampling and optimization hyperparameters (learning rate, epochs, temperature, KL targets, etc.), see [Parameter tuning](/fine-tuning/reinforcement-fine-tuning-models#parameter-tuning).

The canonical cookbook reference for save, resume, and promote is [Checkpoints and Resume](/fine-tuning/training-api/cookbook/reference#checkpoints). Low-level SDK APIs are documented in [Saving and loading](/fine-tuning/training-api/dedicated#saving-and-loading).

## `dcp_save_interval`

Controls how often full training state (weights **and** optimizer) is checkpointed using DCP (Distributed Checkpoint) format.

| Property                                      | Value                                                                                                                                                                                                  |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                                      | `integer`                                                                                                                                                                                              |
| **Default**                                   | `0` (disabled)                                                                                                                                                                                         |
| **Typical config — SFT / RL / DPO cookbooks** | `WeightSyncConfig(dcp_save_interval=N)` on the recipe `Config` (see [Cookbook: RL](/fine-tuning/training-api/cookbook/rl) and [Checkpoints](/fine-tuning/training-api/cookbook/reference#checkpoints)) |

When set to `0` (the default), no periodic DCP checkpoints are written for resume. Only sampler and HuggingFace-format weight snapshots may be produced — these preserve model weights but **not optimizer state**.

When set to a positive integer `N`, a full DCP checkpoint is written every `N` steps.

**Why this matters:** If a training job is interrupted, optimizer state is lost unless `dcp_save_interval` is set. The model resumes from the last checkpoint, but the optimizer re-initializes from scratch — which can affect training stability and effective learning rate.

### Example (cookbook `Config`)

```python theme={null}
from training.recipes.rl_loop import Config, main
from training.utils import WeightSyncConfig

cfg = Config(
    log_path="./grpo_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    # ... other fields ...
    weight_sync=WeightSyncConfig(dcp_save_interval=50),  # full checkpoint every 50 steps
    # ...
)
main(cfg)
```

Some internal or forked recipes may expose the same interval on a nested config type (for example a weight sync block). The field name is always `dcp_save_interval`; see your recipe’s `Config` dataclass for the exact attribute path.

### Job recovery and preemption

For transient control-plane or worker interruptions, the trainer job manager exposes [`reconnect_and_wait`](/fine-tuning/training-api/reference/trainer-job-manager) so your driver can wait for a resumable state and resume cleanly.

<Note>
  `load_state_with_optimizer()` only restores optimizer state from DCP-format checkpoints. If you point it at an HF or sampler snapshot, optimizer state silently won't be restored. Always load from the path returned by `save_state()` when you need full optimizer restore. See [Saving and loading](/fine-tuning/training-api/dedicated#saving-and-loading).
</Note>

***

## Metrics reference

### `ppo_kl` vs `ref_kld`

GRPO training logs two KL divergence metrics that measure different things:

| Metric    | What it measures                                                                                                        | Expected behavior                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `ppo_kl`  | KL between the **current policy** and the **previous policy** (importance-sampling ratio inside the PPO clip objective) | Stays near `0` with one minibatch per rollout — this is correct, not a bug            |
| `ref_kld` | KL between the **current policy** and the **reference (base) model**                                                    | Starts near `0`, increases gradually as the policy diverges from base during training |

**Which one to monitor:** `ref_kld` is the metric to watch for policy drift. A sudden large jump in `ref_kld` may indicate reward hacking or that the KL penalty coefficient needs tuning.

The cookbook does not always surface `ref_kld` by default. To add it, you can use the `k3` unbiased estimator:

```python theme={null}
ref_kld = (ref_logp - policy_logp).exp() - (ref_logp - policy_logp) - 1
```
