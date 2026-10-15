---
title: "Training cookbook reference: configs and utilities"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/reference
path: fine-tuning/training-api/cookbook/reference
---

Reference for Training API cookbook configuration classes, TrainerConfig options, checkpoint helpers, and advanced recipe knobs used across SFT, DPO, and RL.

## TrainerConfig

Training-client launch settings: which training shape to use, the optional reference trainer, region, and run-level knobs. Recipes take it as `Config.trainer`:

```python theme={null}
from training.utils import TrainerConfig

trainer = TrainerConfig(
    training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k",
)
```

Use `training_shape_id` for explicit shape selection — this is the primary shape-specific value you set. Pass the full shared path `accounts/fireworks/trainingShapes/<shape>` (the `fireworks` account is the public shared shape catalog). If you leave it unset, supported recipes auto-select a validated shape from the control plane based on `base_model`, `lora_rank`, and `max_seq_len`.

| Field | Type | Default | Description |
| - | - | - | - |
| `training_shape_id` | `str \| None` | `None` | Optional full training-shape ID for the policy trainer, typically `accounts/fireworks/trainingShapes/<shape>`. When unset, supported recipes auto-select a validated shape. |
| `reference_training_shape_id` | `str \| None` | `None` | Optional full training-shape ID for a separate reference trainer. For full-parameter runs that need a reference, leave unset to auto-select the model's validated LoRA shape; for LoRA runs, leave unset to use the shared-session reference on the policy trainer. |
| `job_id` | `str \| None` | `None` | Attach to an existing trainer job (resume / reattach) instead of creating a new one. |
| `reference_job_id` | `str \| None` | `None` | Attach to an existing reference trainer job. |
| `cleanup_reference_on_close` | `bool` | `True` | Delete the SDK-managed reference trainer when the service closes. |
| `region` | `str \| None` | `None` | Region override (drives trainer + deployment colocation). |
| `timeout_s` | `float` | `3600` | Timeout for trainer provisioning / readiness waits. |
| `replica_count` | `int \| None` | `None` | Data-parallel HSDP replica count for policy trainer launches. This is a run-level knob, not part of the validated training shape; reference trainers are launched without it. |
| `use_reservation` | `bool` | `True` | Try reservation capacity first. Set to `False` for shared capacity only. |

To request replicated HSDP for a run:

```python theme={null}
trainer = TrainerConfig(
    training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    replica_count=2,
)
```

<Note>
  Trainer hardware comes from the validated training shape. Cookbook clients do not set trainer accelerator type or count.
</Note>

<Tip>
  Migrating from `InfraConfig`? See [Deprecated managed infra (InfraConfig)](#deprecated-managed-infra-infraconfig) for the field-rename table.
</Tip>

## DeployConfig

Deployment settings for sampling and weight sync. Wraps `DeploymentConfig` fields:

```python theme={null}
from training.utils import DeployConfig

deploy_cfg = DeployConfig(
    deployment_id="grpo-serving",
    tokenizer_model="Qwen/Qwen3-8B",
)
```

When `deployment_shape` is set (the recommended path), the shape owns deployment hardware and serving configuration.

| Field | Type | Default | Description |
| - | - | - | - |
| `weight_sync_scope` | `WeightSyncScope` | `WeightSyncScope.PER_TRAINER` | Controls whether the trainer bucket or deployment bucket owns weight sync state. See [Weight sync](/fine-tuning/training-api/cookbook/reference#weight-sync). |
| `deployment_id` | `str \| None` | `None` | Deployment identifier. If unset, the cookbook auto-derives one from the base model name. |
| `tokenizer_model` | `str \| None` | `None` | HuggingFace model name for client-side tokenization. Required for RL sampling. |
| `tokenizer_revision` | `str \| None` | `None` | Optional HuggingFace tokenizer revision. |
| `deployment_shape` | `str \| None` | `None` | Deployment shape resource name. When set, the shape owns GPU type and serving config. |
| `hot_load_bucket_type` | `str` | `"FW_HOSTED"` | Weight-sync storage backend |
| `hot_load_trainer_job` | `str \| None` | `None` | Trainer job name whose weight-sync bucket this deployment should use. Format: `accounts/{account}/rlorTrainerJobs/{job_id}`. |
| `deployment_timeout_s` | `float` | `5400` | Timeout for deployment provisioning / readiness waits |
| `reattach_settle_timeout_s` | `int` | `600` | Timeout for the serving pod to settle after re-attaching a deployment to a new trainer bucket. |
| `sample_timeout` | `int` | `600` | HTTP read timeout for sampling completions |
| `disable_speculative_decoding` | `bool` | `True` | Disable speculative decoding for weight-sync compatibility |
| `replica_count` | `int \| None` | `None` | If set, pin the deployment to a fixed replica count (sets both min and max). |

<Note>
  Deployment hardware and serving configuration come from the deployment shape resolved for the selected training shape.
</Note>

## ConcurrencyConfig

Adaptive inference-request settings used by sampling utilities. Async trajectory admission is configured directly on the recipe `Config`; see [RL scheduling](/fine-tuning/training-api/cookbook/rl#scheduling-controls).

| Field | Type | Default | Description |
| - | - | - | - |
| `initial_window` | `int \| None` | `None` | Starting adaptive concurrency window. When unset, recipes derive it from deployment capacity. |
| `min_window` | `int` | `1` | Minimum adaptive concurrency window. |
| `max_window` | `int` | `256` | Maximum adaptive concurrency window. |
| `prefill_queue_target` | `float` | `0.5` | Target prefill queue duration in seconds for AIMD adjustment. |
| `rollout_adjustment_interval` | `int` | `32` | Adjust adaptive concurrency every N completed rollout requests. Remaining requests adjust at the step boundary; set to `0` for step-boundary-only adjustment. |

## Checkpoint & weight-sync fields

Weight-sync and checkpoint cadence are **top-level fields on the recipe `Config`** (no nested config object). Both RL loops sync before training and after each optimizer batch. The SFT, DPO, and RL recipes expose `dcp_save_interval`; SDFT uses its own `save_every` cadence:

```python theme={null}
cfg = Config(
    # ... base_model, dataset, trainer, deployment ...
    weight_sync_timeout=600,              # RL: per weight-sync timeout (seconds)
    dcp_save_interval=10,                  # periodic resumable checkpoint interval
)
```

<Warning>
  `dcp_save_interval=0` disables periodic saves, not the final checkpoint. Successful runs save final training state by default. Set a positive interval (e.g. `50`) for recovery from an interrupted run.
</Warning>

| Field | Recipes | Type | Default | Description |
| - | - | - | - | - |
| `dcp_save_interval` | SFT, DPO, RL | `int` | `0` | Save resumable DCP checkpoints every N steps. `0` disables periodic saves. Set a positive interval for recovery during a run. |
| `weight_sync_timeout` | RL family | `int` | `600` | Timeout for each weight sync (seconds). |

<Note>
  The old nested `WeightSyncConfig` recipe field is gone. Recipe `Config` objects set the fields above directly, and the SDK-managed service owns the underlying save and weight-sync state.
</Note>

## WandBConfig

Weights & Biases logging settings:

```python theme={null}
from training.utils import WandBConfig

wandb = WandBConfig(
    entity="my-team",
    project="grpo-experiment",
    run_name="qwen3-8b-v1",
)
```

| Field | Type | Default | Description |
| - | - | - | - |
| `entity` | `str \| None` | `None` | W\&B team or user name |
| `project` | `str \| None` | `None` | W\&B project name |
| `run_name` | `str \| None` | `None` | Run name (auto-generated if omitted) |

## ReconnectableClient

Blocking convenience wrapper around `FiretitanTrainingClient`. Most recipe calls block until the result is ready or the timeout expires. Async RL uses its native-future submission helpers to overlap pending backward requests. Failures propagate to the caller so the training loop can crash cleanly and resume from the last DCP checkpoint.

<Note>
  This is a recipe-internal wrapper. User code should not construct it with trainer managers. Recipes build it from the `FiretitanTrainingClient` returned by the SDK-managed service client.
</Note>

```python theme={null}
from training.utils import ReconnectableClient

client = ReconnectableClient.from_training_client(
    training_client,
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,
    job_id=service.trainer_job_id,
    service=service,
)

result = client.forward_backward_custom(datums, loss_fn)
client.optim_step(tinker.AdamParams(...))
```

| Parameter | Type | Default | Description |
| - | - | - | - |
| `client` | `FiretitanTrainingClient` | — | Training client returned by `service.create_training_client(...)` |
| `job_id` | `str` | — | RLOR trainer job ID |
| `base_model` | `str` | — | Base model name |
| `lora_rank` | `int` | `0` | LoRA rank (`0` for full-parameter) |
| `service` | `FiretitanServiceClient \| None` | `None` | Managed service that owns the trainer lifecycle |
| `default_timeout` | `int` | `3600` | Timeout in seconds for forward/backward/optim calls |

**Properties:**

| Property | Type | Description |
| - | - | - |
| `job_id` | `str` | The trainer job ID |

**Methods:**

| Method | Description |
| - | - |
| `forward(data, loss_fn)` | Forward pass, blocks until complete |
| `forward_backward(data, loss_fn, loss_fn_config)` | Forward + backward pass |
| `forward_backward_custom(data, loss_fn)` | Forward + backward with custom loss function |
| `optim_step(params, grad_accumulation_normalization=None)` | Optimizer step |
| `save_state(name, timeout)` | Save DCP checkpoint (default timeout: 2700s) |
| `load_state_with_optimizer(path, timeout)` | Load DCP checkpoint (default timeout: 2700s) |
| `save_weights_for_sampler_ext(name, checkpoint_type, timeout)` | Save sampler checkpoint for promotion |
| `resolve_checkpoint_path(name, source_job_id)` | Resolve cross-job checkpoint path |
| `list_checkpoints()` | List available DCP checkpoints |

## Checkpoint utilities

For checkpointing, resume, and promote — see the dedicated [Checkpoints and Resume](/fine-tuning/training-api/cookbook/reference#checkpoints) page.

## Skills reference

Agent-facing operational guidance for gradient accumulation normalization lives in the [cookbook skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-gradient-accumulation.md).

## Deprecated managed infra (InfraConfig)

Earlier cookbook releases provisioned trainers and deployments from the recipe layer using `InfraConfig`, `WeightSyncConfig`, and the standalone helpers `setup_infra` / `ResourceCleanup` / `make_reference_client` / `create_base_reference`. Provisioning now lives entirely behind the **SDK-managed service client** (`build_service_client(...)` → `service.create_*`), and recipes take `trainer=TrainerConfig(...)` plus `deployment=DeployConfig(...)`.

<Warning>
  This is a **breaking change to the recipe-facing interface**. The recipe `Config` no longer accepts `infra=` or `weight_sync=`, and `setup_infra` / `ResourceCleanup` have been removed. If you are **not ready to migrate, simply do not upgrade the SDK + cookbook** — pin your current versions and existing code keeps working. **Upgrading is recommended** (cleaner config, one provisioning path, SDK-owned lifecycle), but it is opt-in: the old and new surfaces do not coexist in one install.
</Warning>

### What to change

| Before (deprecated) | After (current) |
| - | - |
| `Config(infra=InfraConfig(...))` | `Config(trainer=TrainerConfig(...))` |
| `InfraConfig.ref_training_shape_id` | `TrainerConfig.reference_training_shape_id` |
| `InfraConfig.trainer_timeout_s` | `TrainerConfig.timeout_s` |
| `InfraConfig.trainer_replica_count` | `TrainerConfig.replica_count` |
| Nested weight-sync cadence | RL publishes weights after every optimizer batch; no interval field is exposed. |
| `weight_sync.dcp_save_interval=N` | `Config(dcp_save_interval=N)` (top-level, all recipes) |
| top-level `policy_job_id=...` | `TrainerConfig(job_id=...)` |
| `setup_infra(rlor_mgr, deploy_mgr, ...)` | `build_service_client(...)` (see the [SDK migration skill](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-migrate.md)) |
| `create_base_reference()` / `make_reference_client()` | `service.create_reference_client(...)` |
| `with ResourceCleanup(...)` | `cleanup_trainer_on_close=True` + `service.close()` (see [Cleanup](/fine-tuning/training-api/reference/cleanup#automatic-cleanup-via-the-sdk-managed-service)) |

The `InfraConfig` dataclass is still importable for backward compatibility and now emits a `DeprecationWarning` when constructed; it is no longer accepted by recipe `Config` objects.

### Get help migrating

The cookbook ships one [Fireworks training skill](https://github.com/fw-ai/cookbook/tree/main/skills/fireworks-training) that routes managed and Training API work. Its progressive SDK migration reference walks an agent through porting old `InfraConfig` / `setup_infra` scripts to the new `TrainerConfig` + `build_service_client` surface, alongside weight-sync and checkpoint guidance.

## Weight sync

During RL training the inference deployment needs updated weights after each optimizer step. Cookbook recipes wire this through a shared bucket (trainer writes, deployment hot-loads).

For `WeightSyncScope`, error strings, and recovery: [rl-hotload skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-hotload.md).

See also: [RL cookbook](/fine-tuning/training-api/cookbook/rl).

## Checkpoints and resume

Recipe users: set `dcp_save_interval` and `output_model_id` on the recipe `Config`. For continuation, attach to the same trainer with `TrainerConfig(job_id=...)` and keep the same `log_path`. Follow the [checkpoint skill](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-checkpoints.md) for serverless identity and explicit initialization.

```python theme={null}
cfg = Config(
    log_path="./my_training",
    dcp_save_interval=10,
    output_model_id="my-model",
    # ... other recipe fields ...
)
```

For DCP vs sampler checkpoints, promote/resume edge cases, and cross-job warm start: [sdk-checkpoints](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-checkpoints.md) and [training-api-losses](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/training-api-losses.md).
