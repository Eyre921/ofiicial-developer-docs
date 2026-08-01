---
title: "FireworksClient"
source: https://docs.fireworks.ai/fine-tuning/training-api/reference/fireworks-client
path: fine-tuning/training-api/reference/fireworks-client
---

Account-level operations that don't require a running trainer job.

## Overview

`FireworksClient` provides Fireworks platform operations that are independent of any running trainer job: checkpoint promotion, training shape resolution, and model validation. It is also the base class for the legacy [`TrainerJobManager`](/fine-tuning/training-api/reference/trainer-job-manager), which adds direct trainer job lifecycle methods.

Use `FireworksClient` directly when you don't need to create or manage trainer jobs -- for example, promoting a checkpoint after the trainer has already been deleted, or resolving training shape configuration before deciding whether to launch a job.

```python theme={null}
from fireworks.training.sdk import FireworksClient
```

## Constructor

```python theme={null}
client = FireworksClient(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai",  # optional
)
```

| Parameter            | Type           | Default                      | Description               |
| -------------------- | -------------- | ---------------------------- | ------------------------- |
| `api_key`            | `str`          | --                           | Fireworks API key         |
| `base_url`           | `str`          | `"https://api.fireworks.ai"` | Control-plane URL         |
| `additional_headers` | `dict \| None` | `None`                       | Extra HTTP headers        |
| `verify_ssl`         | `bool \| None` | `None`                       | SSL verification override |

## Methods

### `promote_checkpoint(*, name, output_model_id, base_model)`

Promote a sampler checkpoint to a deployable Fireworks model. The trainer job does not need to be running -- the checkpoint resource name is enough to resolve the GCS bucket where the files reside.

```python theme={null}
from datetime import datetime

def latest_promotable(rows):
    return max(
        (row for row in rows if row.get("promotable")),
        key=lambda row: datetime.fromisoformat(
            row["createTime"].replace("Z", "+00:00")
        ),
    )

entry = latest_promotable(client.list_checkpoints("<job-id>"))
model = client.promote_checkpoint(
    name=entry["name"],          # accounts/<a>/rlorTrainerJobs/<j>/checkpoints/<c>
    output_model_id="my-fine-tuned-model",
    base_model="accounts/fireworks/models/qwen3-8b",
)
print(f"Model state: {model['state']}, kind: {model['kind']}")
```

| Parameter         | Type  | Description                                                                                                                     |
| ----------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------- |
| `name`            | `str` | Full 4-segment checkpoint resource name (`accounts/<a>/rlorTrainerJobs/<j>/checkpoints/<c>`), as returned by `list_checkpoints` |
| `output_model_id` | `str` | Desired model ID (1-63 chars, lowercase a-z, 0-9, hyphen only)                                                                  |
| `base_model`      | `str` | Base model resource name for metadata inheritance (e.g. `accounts/fireworks/models/qwen3-8b`)                                   |

Returns the model dict from the API (includes `state`, `kind`, `peftDetails`). See [Saving and Loading](/fine-tuning/training-api/saving-and-loading#promoting-a-checkpoint-to-a-model) for details, and [Checkpoint kinds](/fine-tuning/training-api/cookbook/checkpoints#checkpoint-kinds) for which checkpoints are promotable.

<Note>
  The trainer job can be in any state (running, failed, cancelled, or deleted) as long as the checkpoint files still exist in GCS. Promotion is a file copy -- it does not interact with the trainer process.
</Note>

Validate `output_model_id` with [`validate_output_model_id`](#validate-output-model-id-output-model-id) before calling — a rejected ID (>63 chars or bad charset) orphans the staged sampler blob.

### `list_checkpoints(job_id, *, page_size=200)`

Server-side list of a trainer's checkpoints (sampler + DCP, with promotability metadata). Works on any trainer state — including deleted — while the DB record + GCS blobs survive. Auto-paginates. Distinct from [`FiretitanTrainingClient.list_checkpoints()`](/fine-tuning/training-api/reference/service-client) (live-pod, DCP names only).

```python theme={null}
rows = client.list_checkpoints(job_id)
latest = latest_promotable(rows)
```

Each row has `name`, `createTime` / `updateTime` (RFC3339), `checkpointType` (opaque server enum — filter on `promotable` rather than matching values), and `promotable` (bool, authoritative). Server returns rows **oldest-first** — re-sort client-side for newest-first. Requires `fireworks-ai[training] >= 1.0.0a62`.

### `resolve_training_profile(shape_id)`

Resolve a training shape ID into a full configuration profile:

```python theme={null}
shape_id = "accounts/fireworks/trainingShapes/ts-qwen3-8b-policy"
profile = client.resolve_training_profile(shape_id)
print(profile.accelerator_type)      # e.g. "NVIDIA_B200_192GB"
print(profile.trainer_image_tag)      # e.g. "0.0.0-dev-..."
print(profile.node_count)             # e.g. 1
print(profile.pipeline_parallelism)   # e.g. 1
```

See [Training shapes](/fine-tuning/training-api/training-shapes) for the user-facing shape workflow.

### `validate_output_model_id(output_model_id)`

Client-side validation helper for `promote_checkpoint(..., output_model_id=...)`:

```python theme={null}
from fireworks.training.sdk import validate_output_model_id

errors = validate_output_model_id("my-fine-tuned-model")
if errors:
    raise ValueError("\n".join(errors))
```

Returns a list of formatted error strings. An empty list means the model ID is valid.

## Relationship to managed service clients

Normal training code should use [`FiretitanServiceClient.from_firetitan_config(...)`](/fine-tuning/training-api/reference/service-client#from_firetitan_config), which creates the trainer/deployment and delegates checkpoint listing/promotion through its managed control-plane client.

Use `FireworksClient` directly when you only need platform-level operations outside a live training service, such as promoting a checkpoint from a completed experiment. Use `TrainerJobManager` only for legacy integrations or advanced lifecycle debugging.

```python theme={null}
from fireworks.training.sdk import FireworksClient, TrainerJobManager

# Trainer-free: promote a checkpoint from a completed experiment
client = FireworksClient(api_key=api_key)
entry = latest_promotable(client.list_checkpoints(job_id))
client.promote_checkpoint(name=entry["name"], output_model_id="my-model", base_model=base_model)

# Compatibility lifecycle: create trainer manually, train, promote
mgr = TrainerJobManager(api_key=api_key)
endpoint = mgr.create_and_wait(config)
# ... train ...
entry = latest_promotable(mgr.list_checkpoints(endpoint.job_id))
mgr.promote_checkpoint(name=entry["name"], output_model_id="my-model", base_model=base_model)
mgr.delete(endpoint.job_id)
```

## TrainingShapeProfile

Returned by `resolve_training_profile`:

| Field                          | Type          | Description                                                                                                  |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------ |
| `training_shape_version`       | `str`         | Resolved shape version                                                                                       |
| `trainer_image_tag`            | `str`         | Docker image tag for the trainer                                                                             |
| `max_supported_context_length` | `int`         | Maximum supported context length                                                                             |
| `node_count`                   | `int`         | Number of trainer nodes                                                                                      |
| `deployment_shape_version`     | `str`         | Linked deployment shape                                                                                      |
| `deployment_image_tag`         | `str`         | Docker image tag for the linked deployment                                                                   |
| `accelerator_type`             | `str`         | GPU type                                                                                                     |
| `accelerator_count`            | `int`         | Number of GPUs per node                                                                                      |
| `base_model_weight_precision`  | `str`         | Model weight precision                                                                                       |
| `pipeline_parallelism`         | `int`         | Pipeline parallelism degree                                                                                  |
| `trainer_mode`                 | `str`         | Shape mode, such as `POLICY_TRAINER`, `FORWARD_ONLY`, or `LORA_TRAINER`                                      |
| `training_shape`               | `str`         | Training shape name (without `/versions/...` suffix)                                                         |
| `deployment_shape`             | `str \| None` | Full versioned deployment shape resource name; pass as-is to `DeploymentConfig.deployment_shape` for pinning |
| `supports_lora`                | `bool`        | Whether the shape is LoRA-capable (`trainer_mode == "LORA_TRAINER"`)                                         |

## Related guides

* [TrainerJobManager](/fine-tuning/training-api/reference/trainer-job-manager) -- trainer job lifecycle (extends FireworksClient)
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) -- checkpoint save, load, and promote workflows
* [Training shapes](/fine-tuning/training-api/training-shapes) -- what a shape pins, and its deployment linkage
