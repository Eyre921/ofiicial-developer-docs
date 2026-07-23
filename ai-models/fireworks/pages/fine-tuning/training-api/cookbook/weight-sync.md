---
title: "Weight sync"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/weight-sync
path: fine-tuning/training-api/cookbook/weight-sync
---

How a trainer's updated weights reach the serving deployment during RL training.

During RL training the policy updates step by step, and the inference deployment needs those updated weights to generate the next batch of rollouts. The cookbook wires this as a **shared GCS bucket**:

* The **trainer** writes a fresh checkpoint to the bucket after each optimizer step (or on a configurable cadence).
* The **deployment** watches the same bucket and swaps in new weights without a pod restart.

<Tip>
  **Terminology.** The internal Fireworks name for this mechanism is *hotload*. You'll see that name in SDK field names (`hot_load_trainer_job`, `hot_load_deployment_id`, `hot_load_bucket_url`) and server error messages. "Weight sync" and "hotload" refer to the same thing.
</Tip>

## Normal flow

The RL recipe provisions the trainer and deployment for you — set `deployment=DeployConfig(...)` on the recipe `Config` and the SDK-managed service client wires the bucket correctly. With the default `DeployConfig(weight_sync_scope=WeightSyncScope.PER_TRAINER)`, the trainer is requested first and the deployment is linked to the trainer-owned bucket. `WeightSyncScope.PER_DEPLOYMENT` reverses that order: the deployment is created first, then trainers write to the deployment-owned bucket. If you misconfigure the pairing, the server rejects the `CreateDeployment` or `CreateRlorTrainerJob` call up front with an error that links back here.

## `WeightSyncScope`: who owns the bucket

`DeployConfig.weight_sync_scope` controls which resource must be created first:

| Scope                       | Bucket owner                                   | Use when                                                                                         |
| --------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **`PER_TRAINER`** (default) | Trainer — one bucket per run                   | Single run, or one trainer feeding multiple deployments (sampler + held-out eval)                |
| **`PER_DEPLOYMENT`**        | Deployment — stable bucket across trainer runs | Long-lived deployment, many sequential trainers, can't tolerate deployment restarts between runs |

The recipe dispatches on this single field and wires the rest correctly. The two scopes are mutually exclusive for the same trainer ↔ deployment pair — don't mix them.

## Diagnosing errors

The control plane catches scope-mix mistakes at create time and returns an error that names both resources and suggests the fix. For the full list of server error strings and per-error recovery steps, see the **[Fireworks training skill hotload reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-hotload.md)**. It also covers trainer retention, the unified promote API, and runtime bucket-mismatch warnings.

## See also

* [RL cookbook](/fine-tuning/training-api/cookbook/rl) — end-to-end RL flow, including weight-sync cadence knobs
* [Checkpoints](/fine-tuning/training-api/cookbook/checkpoints) — base/delta, promote
