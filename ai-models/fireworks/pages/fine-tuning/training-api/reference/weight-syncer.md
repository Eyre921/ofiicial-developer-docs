---
title: "WeightSyncer (Legacy)"
source: https://docs.fireworks.ai/fine-tuning/training-api/reference/weight-syncer
path: fine-tuning/training-api/reference/weight-syncer
---

Backward-compatibility reference for the old standalone checkpoint-then-sync helper.

## Overview

<Warning>
  `WeightSyncer` is a legacy low-level helper kept only for backward compatibility in SDK API reference. Do not use it in new cookbook recipes or direct user loops. Use the SDK-managed service flow instead: `training_client.save_weights_for_sampler(...).result()` followed by `service.create_sampling_client(model_path=saved.path)` or `service.create_deployment_sampler(model_path=saved.path)`.
</Warning>

`WeightSyncer` coordinates saving sampler checkpoints and syncing them to a deployment, including automatic base/delta chain state tracking, session-scoped snapshot naming, and post-sync warmup. The managed service client now owns this logic internally.

```python theme={null}
from fireworks.training.sdk import WeightSyncer
```

<Note>
  For full-parameter training, only the first checkpoint (saved as `base`) is promotable; subsequent `delta` checkpoints are not. LoRA checkpoints are always promotable (delta chain is disabled via `lora_rank > 0`). See [Checkpoint kinds](/fine-tuning/training-api/cookbook/checkpoints#checkpoint-kinds) for the full promotability matrix.
</Note>

## Constructor

```python theme={null}
tracker = WeightSyncer(
    policy_client=training_client,
    deploy_mgr=deploy_mgr,
    deployment_id="my-deployment",
    base_model="accounts/fireworks/models/qwen3-8b",
    hotload_timeout=600,
    first_checkpoint_type="base",
    warmup_after_hotload=True,
    reset_prompt_cache=True,
    lora_rank=0,  # >0 for LoRA adapters (disables delta chain)
)
```

| Field                   | Type                        | Default    | Description                                                                                                                                                                                                                 |
| ----------------------- | --------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `policy_client`         | `FiretitanTrainingClient`   | —          | Training client for save operations                                                                                                                                                                                         |
| `deploy_mgr`            | `DeploymentManager \| None` | `None`     | Deployment manager for weight sync (`None` = no weight sync)                                                                                                                                                                |
| `deployment_id`         | `str \| None`               | `None`     | Target deployment for weight sync                                                                                                                                                                                           |
| `base_model`            | `str`                       | `""`       | Model name for weight sync API calls                                                                                                                                                                                        |
| `hotload_timeout`       | `int`                       | `600`      | Timeout in seconds for `hotload_and_wait`                                                                                                                                                                                   |
| `first_checkpoint_type` | `str`                       | `"base"`   | Type for the first checkpoint (`"base"` or `"delta"`)                                                                                                                                                                       |
| `compression_format`    | `str`                       | `"arc_v2"` | Delta compression format                                                                                                                                                                                                    |
| `warmup_after_hotload`  | `bool`                      | `True`     | Send a warmup request after each successful weight sync                                                                                                                                                                     |
| `warmup_max_retries`    | `int`                       | `10`       | Max retries for post-weight-sync warmup                                                                                                                                                                                     |
| `reset_prompt_cache`    | `bool`                      | `True`     | Reset the deployment's prompt cache after each weight sync. See [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts) for active stream, session ID, and reset-option semantics. |
| `lora_rank`             | `int`                       | `0`        | When > 0, forces all checkpoints to `base` type (no delta chain). LoRA adapter exports are standalone PEFT artifacts that cannot use incremental delta compression.                                                         |

## Methods

### `save_and_hotload(name, checkpoint_type=None)`

Save sampler weights and sync to deployment. Automatically handles base (first) vs delta (subsequent) checkpoint types.

Returns the `snapshot_name` (`str | None`) on success or raises on failure:

```python theme={null}
tracker.save_and_hotload(f"step-{step:05d}")
```

### `save_only(name, checkpoint_type=None)`

Save sampler weights without syncing to deployment:

```python theme={null}
snapshot = tracker.save_only("checkpoint-name", checkpoint_type="base")
```

Returns `snapshot_name` or `None`.

### `hotload(snapshot_name, checkpoint_type)`

Sync a previously saved snapshot to the deployment:

```python theme={null}
tracker.hotload(snapshot, checkpoint_type="base")
```

Returns `True` on success, `False` on failure.

### `check_deployment_state()`

Query the deployment's current weight sync state:

```python theme={null}
current = tracker.check_deployment_state()
print(current)  # current_snapshot_identity or None
```

### `wait_for_hotload_ready(timeout_s=300, poll_interval_s=5)`

Block until the deployment's weight sync manager is initialized.

### `reset_delta_chain()`

Force the next save to be treated as `base`. Call when the deployment's bucket or trainer session changes — for example, after attaching an existing deployment to a new trainer job — otherwise the next `delta` could reference a base checkpoint the deployment never loaded.

## Usage patterns

These patterns are for maintaining older integrations. New code should use the service-client sampler refresh pattern documented in [Training and Sampling](/fine-tuning/training-api/training-and-sampling).

### Sync weights every step

To minimize sampler staleness in a synchronous loop, sync a new sampler snapshot after every optimizer step before submitting the next rollout batch. This makes new rollout requests target the latest synced checkpoint, but the loop still owns draining or rejecting any stale in-flight requests before training on them:

```python theme={null}
import asyncio

for step in range(total_steps):
    # ... training step ...
    tracker.save_and_hotload(f"step-{step:05d}")
    completions = asyncio.run(
        sampler.sample_with_tokens(messages=input_messages, n=4)
    )
```

### Interval weight sync

For throughput-oriented loops that tolerate stale sampler weights, sync a new sampler snapshot every N steps. This only controls when new sampler snapshots are saved and synced; it does not prove that already-submitted or in-flight requests were generated by the latest policy:

```python theme={null}
for step in range(total_steps):
    # ... training step ...
    if step % weight_sync_interval == 0:
        tracker.save_and_hotload(f"step-{step:05d}")
```

### Split save and sync

Separate save from weight sync when you need intermediate steps (e.g. warmup):

```python theme={null}
snapshot = tracker.save_only("resume-step-0", checkpoint_type="base")
deploy_mgr.warmup(model)
tracker.hotload(snapshot, checkpoint_type="base")
```

### DCP checkpoints for resume

Save DCP checkpoints at intervals using the training client directly:

```python theme={null}
for step in range(total_steps):
    # ... training step ...
    tracker.save_and_hotload(f"step-{step:05d}")
    if step % dcp_interval == 0:
        training_client.save_state(f"step-{step}")
```

## Related guides

* [DeploymentManager](/fine-tuning/training-api/reference/deployment-manager) — deployment lifecycle and weight-sync API
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) — checkpoint concepts
* [Training and Sampling](/fine-tuning/training-api/training-and-sampling) — end-to-end workflow
