---
title: "FiretitanServiceClient & TrainingClient"
source: https://docs.fireworks.ai/fine-tuning/training-api/reference/service-client
path: fine-tuning/training-api/reference/service-client
---

Connect to a trainer endpoint and use the training client for forward/backward passes, optimizer steps, and checkpointing.

## Overview

`FiretitanServiceClient` is the recommended direct SDK entry point. In the managed path, it creates or reattaches the FireTitan trainer, optional reference trainer, and optional inference deployment, then returns Tinker-compatible training and sampling clients.

For most direct SDK code, create it with `FiretitanServiceClient.from_firetitan_config(...)`. The bare constructor is still useful when you already have a trainer endpoint URL, but that is a lower-level compatibility path.

```python theme={null}
from fireworks.training.sdk import FiretitanServiceClient, GradAccNormalization
```

## FiretitanServiceClient

### `from_firetitan_config(...)`

Create a lazy SDK-managed service. The trainer and deployment are provisioned on the first client call, usually `create_training_client(...)`:

```python theme={null}
service = FiretitanServiceClient.from_firetitan_config(
    api_key="<FIREWORKS_API_KEY>",
    base_url="https://api.fireworks.ai",
    base_model="accounts/fireworks/models/qwen3-8b",
    tokenizer_model="Qwen/Qwen3-8B",
    lora_rank=0,
    training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    deployment_id="research-serving",   # set create_deployment=False for trainer-only flows
    learning_rate=1e-5,
    replica_count=1,                     # deployment replicas
    cleanup_trainer_on_close=True,
    cleanup_deployment_on_close="scale_to_zero",
)

training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,
)
```

Core managed config fields:

| Field                                | Type                                  | Default                    | Description                                                                                              |
| ------------------------------------ | ------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------- |
| `api_key`                            | `str \| None`                         | `FIREWORKS_API_KEY`        | Fireworks API key.                                                                                       |
| `base_url`                           | `str \| None`                         | `https://api.fireworks.ai` | Control-plane URL.                                                                                       |
| `inference_url`                      | `str \| None`                         | `None`                     | Optional inference gateway URL.                                                                          |
| `base_model`                         | `str`                                 | —                          | Fireworks base model resource name.                                                                      |
| `tokenizer_model`                    | `str \| None`                         | `None`                     | HuggingFace tokenizer name used by `get_tokenizer()` and sampler setup.                                  |
| `lora_rank`                          | `int`                                 | `0`                        | `0` for full-parameter training; positive value for LoRA.                                                |
| `training_shape_id`                  | `str \| None`                         | `None`                     | User-facing training shape ID. The SDK resolves the pinned version.                                      |
| `reference_training_shape_id`        | `str \| None`                         | `None`                     | Optional separate forward-only reference trainer shape.                                                  |
| `trainer_job_id`                     | `str \| None`                         | `None`                     | Reattach to an existing trainer instead of creating one.                                                 |
| `reference_trainer_job_id`           | `str \| None`                         | `None`                     | Reattach to an existing reference trainer.                                                               |
| `create_deployment`                  | `bool`                                | `True`                     | Whether to create or reattach an inference deployment. Set `False` for trainer-only SFT/DPO-style loops. |
| `deployment_id`                      | `str \| None`                         | `None`                     | Create or reattach an inference deployment for sampling and weight sync.                                 |
| `deployment_shape`                   | `str \| None`                         | Linked shape               | Optional deployment shape override. Usually inherited from the training shape.                           |
| `trainer_replica_count`              | `int \| None`                         | `None`                     | Data-parallel HSDP replicas for the trainer.                                                             |
| `replica_count`                      | `int`                                 | `1`                        | Inference deployment replicas.                                                                           |
| `cleanup_trainer_on_close`           | `bool`                                | `False`                    | Delete the SDK-managed policy trainer when `service.close()` runs.                                       |
| `cleanup_reference_trainer_on_close` | `bool`                                | `True`                     | Delete SDK-managed separate reference trainers when released/closed.                                     |
| `cleanup_deployment_on_close`        | `"scale_to_zero" \| "delete" \| None` | `None`                     | Optional deployment cleanup action on close.                                                             |

The managed service exposes resolved metadata after provisioning:

```python theme={null}
print(service.trainer_job_id)
print(service.deployment_id)
print(service.max_context_length)
print(service.reference_trainer_job_id)  # None when the reference is shared
```

### Bare constructor

```python theme={null}
service = FiretitanServiceClient(
    base_url=endpoint.base_url,  # From TrainerJobManager.create_and_wait(...)
    api_key="<FIREWORKS_API_KEY>",
)
```

`base_url` is the trainer endpoint URL from `TrainerServiceEndpoint.base_url`. Use this only when you intentionally manage trainer lifecycle yourself. New user code should use `from_firetitan_config(...)`.

### `create_training_client(base_model, lora_rank, user_metadata)`

Creates a `FiretitanTrainingClient` for training operations:

```python theme={null}
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,  # Must match lora_rank from job creation
)
```

| Parameter       | Type                     | Default | Description                                                 |
| --------------- | ------------------------ | ------- | ----------------------------------------------------------- |
| `base_model`    | `str`                    | —       | Must match the trainer job's `base_model`                   |
| `lora_rank`     | `int`                    | `0`     | Must match trainer creation config (`0` for full-parameter) |
| `user_metadata` | `dict[str, str] \| None` | `None`  | Optional run metadata                                       |

<Warning>
  A `ValueError` is raised if you attempt to create a second training client with the same `(base_model, lora_rank)` on the same `FiretitanServiceClient` instance. Create a new `FiretitanServiceClient` for a separate trainer.
</Warning>

### Connecting to an existing trainer

If you already have a running trainer (e.g. from a previous session), connect directly by URL:

```python theme={null}
service = FiretitanServiceClient(
    base_url="https://<existing-trainer-url>",
    api_key="<FIREWORKS_API_KEY>",
)
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,
)
```

### `create_base_training_client(base_model, user_metadata=None)`

Creates a base-only client on the same trainer session. Use this as a frozen reference for LoRA KL/reference logprobs without launching a separate forward-only trainer:

```python theme={null}
reference_client = service.create_base_training_client(base_model=base_model)
ref = reference_client.forward(datums, "cross_entropy").result()
```

Do not call `forward_backward`, `forward_backward_custom`, or `optim_step` on this client; it is for reference forward passes only.

### `create_reference_client(base_model, lora_rank=0, user_metadata=None)`

Create a frozen reference client for KL/DPO baseline logprobs:

```python theme={null}
reference_client = service.create_reference_client(base_model, lora_rank=0)
ref = reference_client.forward(datums, "cross_entropy").result()
```

The SDK chooses the backing automatically. LoRA policies without an explicit reference shape reuse the policy trainer with the adapter disabled. Full-parameter policies, explicit `reference_training_shape_id`, or explicit `reference_trainer_job_id` use a separate forward-only reference trainer owned by the service.

### `create_sampling_client(model_path=None, ...)`

Return a Tinker-shaped sampling client backed by the SDK-managed deployment. When `model_path` is provided, the SDK first syncs that sampler snapshot to the deployment:

```python theme={null}
saved = training_client.save_weights_for_sampler("step-100").result()
sampler = service.create_sampling_client(model_path=saved.path)
```

This is the replacement for calling a standalone weight-sync helper in user code. The SDK tracks the base/delta chain and builds the weight-sync metadata internally.

### `create_deployment_sampler(model_path=None, tokenizer=None, concurrency_controller=None)`

Return the FireTitan-native `DeploymentSampler` directly. Use this when you need tokenized completions, inference logprobs, routing matrices, or adaptive concurrency:

```python theme={null}
sampler = service.create_deployment_sampler(
    model_path=saved.path,
    tokenizer=tokenizer,
    concurrency_controller=controller,
)
```

### `hotload_sampler_snapshot(model_path)`

Low-level method for syncing a previously saved sampler snapshot into the SDK-managed deployment without constructing a sampler:

```python theme={null}
service.hotload_sampler_snapshot(saved.path)
```

## FiretitanTrainingClient

The training client returned by `create_training_client()`. Core training RPCs like `forward(...)`, `forward_backward_custom(...)`, `optim_step(...)`, `save_state(...)`, and `load_state_with_optimizer(...)` return **futures**. Fireworks convenience helpers like `save_weights_for_sampler_ext(...)`, `list_checkpoints()`, and `resolve_checkpoint_path(...)` return concrete values directly.

### `forward(datums, loss_type)`

Forward-only pass (no gradient computation). Useful for computing reference logprobs in GRPO/DPO:

```python theme={null}
result = training_client.forward(datums, "cross_entropy").result()
logprobs = result.loss_fn_outputs[0]["logprobs"].data
```

<Note>
  Built-in loss types like `"cross_entropy"` require datums with `target_tokens` in `loss_fn_inputs`. Datums built with `datum_from_model_input_weights` will fail. Use the target-token `tinker.Datum` example in [Loss Functions](/fine-tuning/training-api/loss-functions#using-tinkerdatum-directly-target-token-based) for built-in losses, or use `forward_backward_custom` with the weight-based format in [Building datums](/fine-tuning/training-api/loss-functions#building-datums) and the custom-loss pattern in [Example: simple cross-entropy](/fine-tuning/training-api/loss-functions#example-simple-cross-entropy).
</Note>

### `forward_backward_custom(datums, loss_fn)`

Forward + backward with your custom loss function. See [Loss Functions](/fine-tuning/training-api/loss-functions) for details:

```python theme={null}
def my_loss(data, logprobs_list):
    loss = compute_loss(data, logprobs_list)
    return loss, {"loss": float(loss.item())}

result = training_client.forward_backward_custom(datums, my_loss).result()
print(result.metrics)  # {"loss": 0.42}
```

For embedding-space objectives, pass `output="embedding"` and choose `pooling="mean"` or `"last"`; your loss function then receives pooled embedding tensors instead of logprobs:

```python theme={null}
result = training_client.forward_backward_custom(
    datums,
    embedding_loss,
    output="embedding",
    pooling="mean",
).result()
```

### `optim_step(adam_params, grad_accumulation_normalization=None)`

Apply optimizer update after accumulating gradients:

```python theme={null}
import tinker

training_client.optim_step(
    tinker.AdamParams(
        learning_rate=1e-5,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8,
        weight_decay=0.01,
    )
).result()
```

Advanced callers may pass `grad_accumulation_normalization` to control how accumulated gradients are normalized. The default `None` leaves gradients unchanged. Pass `GradAccNormalization.NUM_LOSS_TOKENS`, `GradAccNormalization.NUM_SEQUENCES`, or `GradAccNormalization.NONE` rather than raw strings. See the [cookbook skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/dev/references/rl/gradient-accumulation.md) for operational guidance.

### `save_weights_for_sampler(name, ttl_seconds=None, checkpoint_type=None)`

Save serving-compatible sampler weights and return a future. This is the normal Tinker-shaped API:

```python theme={null}
saved = training_client.save_weights_for_sampler(
    "step-100",
    checkpoint_type="base",  # optional: "base" or "delta"
).result()
print(saved.path)  # Snapshot identity for create_sampling_client(model_path=...)
```

Full-parameter training saves a base checkpoint first and deltas after that by default. LoRA training always saves base checkpoints. The returned `path` is a public snapshot identity, not a raw storage URI.

### `save_weights_for_sampler_ext(name, checkpoint_type, ttl_seconds)`

Fireworks-specific extension that returns a concrete `SaveSamplerResult` instead of a future:

```python theme={null}
result = training_client.save_weights_for_sampler_ext(
    "step-100",
    checkpoint_type="base",  # "base" for full weights, "delta" for incremental
)
print(result.snapshot_name)  # Session-qualified name for weight sync
```

| Parameter         | Type          | Default | Description                                          |
| ----------------- | ------------- | ------- | ---------------------------------------------------- |
| `name`            | `str`         | —       | Checkpoint name (auto-suffixed with session ID)      |
| `checkpoint_type` | `str \| None` | `None`  | `"base"` for full weights, `"delta"` for incremental |
| `ttl_seconds`     | `int \| None` | `None`  | Auto-delete checkpoint after this many seconds       |

<Note>
  On full-parameter training, only `checkpoint_type="base"` produces a promotable blob; `"delta"` cannot be promoted. LoRA is always promotable. See [Checkpoint kinds](/fine-tuning/training-api/cookbook/checkpoints#checkpoint-kinds) for the full promotability matrix.
</Note>

`save_weights_for_sampler_ext` saves the snapshot only; it does not mutate a deployment. To serve the snapshot, pass `result.snapshot_name` to the managed service weight-sync path, or use `create_sampling_client(model_path=...)` / `create_deployment_sampler(model_path=...)`, which sync and return a sampler.

### `save_state(name, ttl_seconds=None, timeout=None)`

Save full train state (weights + optimizer) for resume:

```python theme={null}
training_client.save_state("train_state_step_100").result()
```

| Parameter     | Type            | Default | Description                                                   |
| ------------- | --------------- | ------- | ------------------------------------------------------------- |
| `name`        | `str`           | —       | Checkpoint name                                               |
| `ttl_seconds` | `int \| None`   | `None`  | Auto-delete checkpoint after this many seconds                |
| `timeout`     | `float \| None` | `None`  | If set, block until the save completes or the timeout expires |

### `load_state_with_optimizer(name)`

Restore full train state (weights + optimizer) from a checkpoint:

```python theme={null}
training_client.load_state_with_optimizer("train_state_step_100").result()
```

### `load_state(name)`

Load model weights from a checkpoint without restoring optimizer state. The optimizer is reset so the next `optim_step` starts fresh:

```python theme={null}
training_client.load_state("train_state_step_100").result()
```

### `load_adapter(adapter_ref)`

Load a Hugging Face PEFT adapter model into the current LoRA session. Pass a Fireworks model resource name for a promoted adapter, such as `accounts/<ACCOUNT_ID>/models/<ADAPTER_MODEL_ID>`. This is a weights-only warm start; it does not restore optimizer state, scheduler state, or data cursor.

```python theme={null}
training_client.load_adapter("accounts/<ACCOUNT_ID>/models/<ADAPTER_MODEL_ID>").result()
```

### `list_checkpoints()`

List available DCP checkpoints from the trainer. Returns a `list[str]`:

```python theme={null}
checkpoint_names = training_client.list_checkpoints()
print(checkpoint_names)  # e.g. ["step-2", "step-4"]
```

### `resolve_checkpoint_path(checkpoint_name, source_job_id)`

Resolve a checkpoint path for cross-job resume:

```python theme={null}
checkpoint_ref = training_client.resolve_checkpoint_path(
    "step-4",
    source_job_id="previous-job-id",
)
training_client.load_state_with_optimizer(checkpoint_ref).result()
```

## SaveSamplerResult

Returned by `save_weights_for_sampler_ext`:

| Field           | Type  | Description                                       |
| --------------- | ----- | ------------------------------------------------- |
| `path`          | `str` | Snapshot name from trainer                        |
| `snapshot_name` | `str` | Session-qualified name for weight sync operations |

## GradAccNormalization

Enum for the advanced `optim_step` `grad_accumulation_normalization` parameter:

| Enum                                   | Wire value          | Description                                                     |
| -------------------------------------- | ------------------- | --------------------------------------------------------------- |
| `GradAccNormalization.NUM_LOSS_TOKENS` | `"num_loss_tokens"` | Normalize by total loss tokens across accumulated micro-batches |
| `GradAccNormalization.NUM_SEQUENCES`   | `"num_sequences"`   | Normalize by total sequences across accumulated micro-batches   |
| `GradAccNormalization.NONE`            | `"none"`            | Explicit no normalization (raw gradient sum)                    |

## Related guides

* [Training and Sampling](/fine-tuning/training-api/training-and-sampling) — managed service training + sampler refresh walkthrough
* [Loss Functions](/fine-tuning/training-api/loss-functions) — built-in and custom loss functions
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) — checkpoint details
