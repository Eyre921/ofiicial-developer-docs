---
title: "TrainerJobManager (Compatibility)"
source: https://docs.fireworks.ai/fine-tuning/training-api/reference/trainer-job-manager
path: fine-tuning/training-api/reference/trainer-job-manager
---

Legacy SDK reference for service-mode trainer job lifecycle management.

## Overview

<Warning>
  `TrainerJobManager` is a low-level compatibility API. New user code should not create trainer managers directly; use [`FiretitanServiceClient.from_firetitan_config(...)`](/fine-tuning/training-api/reference/service-client#from_firetitan_config) or cookbook recipes instead. This page remains for existing integrations, migration support, and advanced lifecycle debugging.
</Warning>

`TrainerJobManager` manages the lifecycle of service-mode trainer jobs — GPU-backed trainer endpoints that your Python loop connects to with a training client.

`TrainerJobManager` extends [`FireworksClient`](/fine-tuning/training-api/reference/fireworks-client), so all trainer-free operations (checkpoint promotion, training shape resolution) are also available here.

```python theme={null}
from fireworks.training.sdk import TrainerJobManager, TrainerJobConfig
```

## Constructor

```python theme={null}
rlor_mgr = TrainerJobManager(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai",  # optional, defaults to https://api.fireworks.ai
)
```

| Parameter            | Type           | Default                      | Description               |
| -------------------- | -------------- | ---------------------------- | ------------------------- |
| `api_key`            | `str`          | —                            | Fireworks API key         |
| `base_url`           | `str`          | `"https://api.fireworks.ai"` | Control-plane URL         |
| `additional_headers` | `dict \| None` | `None`                       | Extra HTTP headers        |
| `verify_ssl`         | `bool \| None` | `None`                       | SSL verification override |

## Methods

### `create(config)`

Create a service-mode trainer job and return immediately (without waiting). Returns a `CreatedTrainerJob`:

```python theme={null}
created = rlor_mgr.create(TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_ref="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    lora_rank=0,
    learning_rate=1e-5,
))

print(created.job_id)    # <JOB_ID>
print(created.job_name)  # accounts/<ACCOUNT_ID>/rlorTrainerJobs/<JOB_ID>
```

### `wait_for_ready(job_id, job_name=None, poll_interval_s=5.0, timeout_s=900)`

Poll until a trainer job reaches `RUNNING` state and is healthy. Returns a `TrainerServiceEndpoint`:

```python theme={null}
endpoint = rlor_mgr.wait_for_ready(created.job_id)
```

### `create_and_wait(config, poll_interval_s=5.0, timeout_s=900)`

Create a service-mode trainer and poll until the endpoint is healthy. Combines `create()` + `wait_for_ready()`. Returns a `TrainerServiceEndpoint`.

```python theme={null}
endpoint = rlor_mgr.create_and_wait(TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_ref="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    lora_rank=0,
    learning_rate=1e-5,
    display_name="grpo-policy-trainer",
))

print(endpoint.base_url)  # https://<trainer-endpoint>
print(endpoint.job_id)    # <JOB_ID>
print(endpoint.job_name)  # accounts/<ACCOUNT_ID>/rlorTrainerJobs/<JOB_ID>
```

### `wait_for_existing(job_id, poll_interval_s=5.0, timeout_s=900)`

Wait for an already-existing trainer job to reach `RUNNING` state:

```python theme={null}
existing = rlor_mgr.wait_for_existing(job_id="<existing-job-id>")
print(existing.base_url)
```

### `resume_and_wait(job_id, poll_interval_s=5.0, timeout_s=900)`

Resume a failed/cancelled/paused job and wait until healthy:

```python theme={null}
endpoint = rlor_mgr.resume_and_wait(job_id="<job-id>")
```

### `reconnect_and_wait(job_id, ...)`

Handle pod preemption and transient failures. Waits for the job to reach a resumable state, resumes it, then polls until healthy:

```python theme={null}
endpoint = rlor_mgr.reconnect_and_wait(
    job_id="<job-id>",
    timeout_s=600,
    max_wait_for_resumable_s=120,
)
```

More robust than `resume_and_wait()` — retries when the job is in a transitional state (e.g. the control plane is still processing a pod death).

| Parameter                  | Type    | Default | Description                                   |
| -------------------------- | ------- | ------- | --------------------------------------------- |
| `job_id`                   | `str`   | —       | The RLOR job ID to reconnect                  |
| `poll_interval_s`          | `float` | `5.0`   | Seconds between health checks after resume    |
| `timeout_s`                | `float` | `600`   | Overall timeout for the job to become RUNNING |
| `max_wait_for_resumable_s` | `float` | `120`   | Max seconds to wait for a resumable state     |

### `get(job_id)`

Inspect job status:

```python theme={null}
status = rlor_mgr.get(job_id=endpoint.job_id)
print(status["state"])  # JOB_STATE_RUNNING
```

### `delete(job_id)`

Delete a trainer job and release GPU resources:

```python theme={null}
rlor_mgr.delete(job_id="<job-id>")
```

### `promote_checkpoint(*, name, output_model_id, base_model)`

*Inherited from [`FireworksClient`](/fine-tuning/training-api/reference/fireworks-client).* Promote a sampler checkpoint to a deployable Fireworks model. The trainer job does not need to be running -- the checkpoint resource name resolves the storage location.

```python theme={null}
from datetime import datetime

entry = max(
    (
        row
        for row in rlor_mgr.list_checkpoints(endpoint.job_id)
        if row.get("promotable")
    ),
    key=lambda row: datetime.fromisoformat(
        row["createTime"].replace("Z", "+00:00")
    ),
)
model = rlor_mgr.promote_checkpoint(
    name=entry["name"],
    output_model_id="my-fine-tuned-model",
    base_model="accounts/fireworks/models/qwen3-8b",
)
```

See [`FireworksClient.promote_checkpoint`](/fine-tuning/training-api/reference/fireworks-client#promote_checkpoint-name-output_model_id-base_model) for full parameter docs.

### `resolve_training_profile(shape_id)`

*Inherited from [`FireworksClient`](/fine-tuning/training-api/reference/fireworks-client).* Resolve a training shape ID into a full configuration profile.

```python theme={null}
shape_id = "accounts/fireworks/trainingShapes/ts-qwen3-8b-policy"
profile = rlor_mgr.resolve_training_profile(shape_id)
```

See [`FireworksClient.resolve_training_profile`](/fine-tuning/training-api/reference/fireworks-client#resolve_training_profileshape_id) for full parameter docs.

## TrainerJobConfig

`TrainerJobManager.create_and_wait(...)` accepts a `TrainerJobConfig` dataclass:

Launching through a training shape is the recommended path. In normal user code, you should not hand-author `training_shape_ref`; pass a training shape ID to `resolve_training_profile(...)` and use the returned versioned ref. Advanced manual launches can omit `training_shape_ref` and provide infra fields directly.

When `training_shape_ref` is set (the recommended **shape path**), the training shape owns the trainer's hardware and image configuration. The fields below are what you set as a user:

| Field                        | Type                                | Default | Description                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------- | ----------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_model`                 | `str`                               | —       | Base model name (e.g. `"accounts/fireworks/models/qwen3-8b"`)                                                                                                                                                                                                                                                                                                   |
| `training_shape_ref`         | `str \| None`                       | `None`  | Full training-shape resource name (e.g. `accounts/fireworks/trainingShapes/<shape>` or `.../versions/<ver>`). Use `mgr.resolve_training_profile(...)` to get the pinned versioned ref. See [Training shapes](/fine-tuning/training-api/training-shapes).                                                                                                        |
| `lora_rank`                  | `int`                               | `0`     | LoRA rank. `0` for full-parameter tuning, or a positive integer (e.g. `16`, `64`) for LoRA                                                                                                                                                                                                                                                                      |
| `max_context_length`         | `int \| None`                       | `None`  | Maximum sequence length. Usually inherited from the training shape on the shape path.                                                                                                                                                                                                                                                                           |
| `learning_rate`              | `float`                             | `1e-5`  | Learning rate for the optimizer                                                                                                                                                                                                                                                                                                                                 |
| `display_name`               | `str \| None`                       | `None`  | Human-readable trainer name                                                                                                                                                                                                                                                                                                                                     |
| `region`                     | `str \| None`                       | `None`  | Region for the job                                                                                                                                                                                                                                                                                                                                              |
| `extra_args`                 | `list[str] \| None`                 | `None`  | Extra trainer arguments                                                                                                                                                                                                                                                                                                                                         |
| `forward_only`               | `bool`                              | `False` | Deprecated. Created a forward-only reference trainer. Use the model's LoRA shape with the adapter disabled instead.                                                                                                                                                                                                                                             |
| `inactivity_timeout`         | `datetime.timedelta \| str \| None` | `None`  | Trainer inactivity timeout. The trainer reports tracked activity, including trainer API operations and active-session heartbeats. If no tracked activity is observed for this duration, the trainer is automatically stopped. When unset or `0`, Fireworks uses the 10-minute default. String values must use protobuf JSON duration format, such as `"1800s"`. |
| `disable_inactivity_cleanup` | `bool`                              | `False` | Disable trainer inactivity cleanup. GPU usage continues to accrue while the trainer is running.                                                                                                                                                                                                                                                                 |

<Warning>
  `gradient_accumulation_steps` is deprecated in `TrainerJobConfig`. Do not use it to request server-side accumulation. Accumulate gradients in client code by calling `forward_backward...` multiple times before one `optim_step(...)`; see [Loss Functions](/fine-tuning/training-api/loss-functions#applying-the-optimizer-step).
</Warning>

<Note>
  On the recommended shape path, `accelerator_type`, `accelerator_count`, `node_count`, and `custom_image_tag` are automatically configured by the training shape and cannot be overridden. Advanced manual launches can omit `training_shape_ref` and set those fields directly.
</Note>

## CreatedTrainerJob

Returned by `create()`:

| Field      | Type  | Description                                               |
| ---------- | ----- | --------------------------------------------------------- |
| `job_name` | `str` | Full resource name (`accounts/<id>/rlorTrainerJobs/<id>`) |
| `job_id`   | `str` | RLOR trainer job ID                                       |

## TrainerServiceEndpoint

Returned by `create_and_wait`, `wait_for_ready`, `wait_for_existing`, `resume_and_wait`, and `reconnect_and_wait`:

| Field      | Type  | Description                                               |
| ---------- | ----- | --------------------------------------------------------- |
| `base_url` | `str` | Trainer endpoint URL for connecting a training client     |
| `job_id`   | `str` | RLOR trainer job ID                                       |
| `job_name` | `str` | Full resource name (`accounts/<id>/rlorTrainerJobs/<id>`) |

## TrainingShapeProfile

See [`FireworksClient` > TrainingShapeProfile](/fine-tuning/training-api/reference/fireworks-client#trainingshapeprofile) for the full field reference.

## Job states

| State                 | Meaning                                              |
| --------------------- | ---------------------------------------------------- |
| `JOB_STATE_CREATING`  | Resources being provisioned                          |
| `JOB_STATE_PENDING`   | Queued, waiting for GPU availability                 |
| `JOB_STATE_RUNNING`   | Trainer is ready — you can connect a training client |
| `JOB_STATE_IDLE`      | Service-mode job is idle                             |
| `JOB_STATE_COMPLETED` | Job finished successfully                            |
| `JOB_STATE_FAILED`    | Job failed                                           |
| `JOB_STATE_CANCELLED` | Job was cancelled                                    |

## Related guides

* [FiretitanServiceClient](/fine-tuning/training-api/reference/service-client) — create a `FiretitanTrainingClient` for a live trainer endpoint
* [Training shapes](/fine-tuning/training-api/training-shapes) — what a shape pins, and its deployment linkage
* [Cleanup](/fine-tuning/training-api/reference/cleanup) — resource cleanup
