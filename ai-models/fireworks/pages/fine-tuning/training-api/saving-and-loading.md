---
title: "Saving and Loading"
source: https://docs.fireworks.ai/fine-tuning/training-api/saving-and-loading
path: fine-tuning/training-api/saving-and-loading
---

SDK-level reference for checkpoint save, load, weight sync, and promotion.

<Note>
  **Most users don't need this page.** If you're launching training through a cookbook recipe (`rl_loop`, `sft_loop`, etc.), the recipe handles save, resume, and promote for you — set `dcp_save_interval` and `output_model_id` on your config and you're done. See [Checkpoints and Resume (cookbook)](/fine-tuning/training-api/cookbook/checkpoints) for the recipe-driven flow.

  This page is the SDK-level reference for advanced users who are forking a recipe, calling the SDK directly, or debugging a checkpoint that doesn't promote.
</Note>

## What this is

During training, you save checkpoints for three purposes:

1. **Sampler refresh / weight sync** (`save_weights_for_sampler` + `create_sampling_client(model_path=...)`): Save updated sampler weights, then sync the returned snapshot identity onto a running inference deployment without restarting it.
2. **Resuming** (`save_state` / `load_state_with_optimizer`): Persist full training state (weights + optimizer) so you can continue training from where you left off.
3. **Promotion** (`promote_checkpoint`): Turn a saved sampler checkpoint into a deployable Fireworks model.

## Sampler checkpoints

Sampler checkpoints are weight-only snapshots used for weight sync and promotion. For promotability rules, see [Checkpoint kinds](/fine-tuning/training-api/cookbook/checkpoints#checkpoint-kinds) — the cookbook page is the source of truth.

The raw SDK exposes two `checkpoint_type` modes that affect size and weight-sync speed:

| `checkpoint_type` | What it saves                                                                                       | Size                                |
| ----------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `"base"`          | Complete chain anchor: full-model weights for full-parameter training, or the full adapter for LoRA | Depends on parameter mode and model |
| `"delta"`         | Full-parameter XOR diff from the previous base                                                      | Depends on changed weights          |

Delta is much faster for per-step weight sync (`current_weights = base XOR delta` on the deployment). LoRA sampler checkpoints always contain the full adapter regardless of `checkpoint_type`.

<Warning>
  On full-parameter training, `checkpoint_type="delta"` produces a blob that cannot be promoted — only `"base"` can. Use the SDK-managed service path (`save_weights_for_sampler` -> `create_sampling_client(model_path=...)`) or the cookbook recipe weight-sync path for the safe base-then-delta pattern. The cookbook's `TrainingCheckpoints.save(promotable=True)` always saves `base`.
</Warning>

### Saving checkpoints

```python theme={null}
# First checkpoint — base chain anchor
saved = training_client.save_weights_for_sampler(
    "step-0001",
    checkpoint_type="base",
).result()
# saved.path is the sampler snapshot identity (e.g. "step-0001-a1b2c3d4")

# Subsequent checkpoints — delta is faster
saved = training_client.save_weights_for_sampler(
    "step-0010",
    checkpoint_type="delta",
).result()
```

`save_weights_for_sampler_ext(...)` is the Fireworks-specific low-level variant that returns `SaveSamplerResult` directly. Use it when you need a concrete return value immediately; use `save_weights_for_sampler(...).result()` for the Tinker-shaped API.

## Promoting a checkpoint to a model

Promote a sampler checkpoint to a deployable Fireworks model. Available on [`FireworksClient`](/fine-tuning/training-api/reference/fireworks-client) and on the SDK-managed [`FiretitanServiceClient`](/fine-tuning/training-api/reference/service-client) after provisioning. The trainer job does not need to be running — its row only needs to exist; promotion is a metadata + file-copy operation. See [Checkpoint kinds](/fine-tuning/training-api/cookbook/checkpoints#checkpoint-kinds) for which checkpoints are promotable.

### Preferred: pass the 4-segment `name=` from `list_checkpoints`

`list_checkpoints` returns each checkpoint's full resource name (`accounts/<account>/rlorTrainerJobs/<job>/checkpoints/<id>`). Hand that string straight to `promote_checkpoint` — no manual disassembly into `(job_id, checkpoint_id)`:

```python theme={null}
from datetime import datetime
from fireworks.training.sdk import FireworksClient

client = FireworksClient(api_key=api_key)

# Select the newest promotable row by parsed timestamp.
rows = client.list_checkpoints(job_id)
target = max(
    (row for row in rows if row.get("promotable")),
    key=lambda row: datetime.fromisoformat(
        row["createTime"].replace("Z", "+00:00")
    ),
)

model = client.promote_checkpoint(
    name=target["name"],                          # 4-segment resource path
    output_model_id="my-fine-tuned-qwen3-8b",
    base_model="accounts/fireworks/models/qwen3-8b",
)
```

| Parameter         | Type  | Description                                                                                                                                                              |
| ----------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`            | `str` | Full 4-segment checkpoint resource name from `list_checkpoints` output                                                                                                   |
| `output_model_id` | `str` | Desired model ID (1-63 chars, lowercase a-z, 0-9, hyphen only). Validate with `validate_output_model_id` before calling — a rejected ID orphans the staged sampler blob. |
| `base_model`      | `str` | Base model resource name for metadata inheritance (e.g. `accounts/fireworks/models/qwen3-8b`)                                                                            |

### Legacy: positional `(job_id, checkpoint_id)` form

The previous `(job_id, checkpoint_id)` shape still works for callers that haven't migrated. It fires a `DeprecationWarning` whenever `name=` is omitted, regardless of whether `job_id` and `checkpoint_id` are passed positionally or as keywords:

```python theme={null}
model = client.promote_checkpoint(
    job_id=endpoint.job_id,
    checkpoint_id=result.snapshot_name,
    output_model_id="my-fine-tuned-qwen3-8b",
    base_model="accounts/fireworks/models/qwen3-8b",
)
# DeprecationWarning: promote_checkpoint(job_id, checkpoint_id, ...) positional
# form is deprecated. Pass the 4-segment resource name instead:
# promote_checkpoint(name=entry['name'], output_model_id=..., base_model=...).
# The 'name' field comes straight from list_checkpoints output.
```

To migrate, look the row up via `list_checkpoints` and pass its `name` field straight through:

```python theme={null}
from datetime import datetime

entry = max(
    (
        row
        for row in client.list_checkpoints(endpoint.job_id)
        if row.get("promotable")
    ),
    key=lambda row: datetime.fromisoformat(
        row["createTime"].replace("Z", "+00:00")
    ),
)
model = client.promote_checkpoint(
    name=entry["name"],
    output_model_id="my-fine-tuned-qwen3-8b",
    base_model="accounts/fireworks/models/qwen3-8b",
)
```

The `hot_load_deployment_id` parameter has its own `DeprecationWarning` and is only needed for deployments that predate the stored-bucket-URL migration:

```
DeprecationWarning: promote_checkpoint(hot_load_deployment_id=...) is
deprecated. The gateway resolves the bucket URL from the trainer's
stored metadata for any run on cookbook >= 0.3.0 (both PER_TRAINER
and PER_DEPLOYMENT bucket scopes). Omit this argument unless you are
promoting a checkpoint from a deployment that predates the
stored-bucket-URL migration.
```

For modern runs (cookbook ≥ 0.3.0, either bucket scope), omit the argument.

### Listing checkpoints on a trainer

```bash theme={null}
curl "https://api.fireworks.ai/v1/accounts/<account-id>/rlorTrainerJobs/<job-id>/checkpoints?pageSize=200" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

Each entry includes `name`, `createTime`, `updateTime`, `checkpointType`, and `promotable`.

### Serverless training sessions

[Serverless Training](/fine-tuning/training-api/serverless) runs have no trainer job, so checkpoint list and promote are scoped to the owning **training session** instead of an `rlorTrainerJobs` resource. Use the session-scoped analogs on `FireworksClient`, addressing the session by its resource name (`service.training_session_name` on the serverless `FiretitanServiceClient`):

```python theme={null}
import os
from datetime import datetime
from fireworks.training.sdk import FireworksClient

client = FireworksClient(api_key=os.environ["FIREWORKS_API_KEY"])

# From the serverless FiretitanServiceClient, e.g. "accounts/<a>/trainingSessions/<s>"
session_name = service.training_session_name

rows = client.list_training_session_checkpoints(session_name)
target = max(
    (row for row in rows if row.get("promotable")),
    key=lambda row: datetime.fromisoformat(
        row["createTime"].replace("Z", "+00:00")
    ),
)

model = client.promote_session_checkpoint(
    name=target["name"],  # accounts/<a>/trainingSessions/<s>/checkpoints/<c>
    output_model_id="my-serverless-lora",
    base_model="accounts/fireworks/models/qwen3p6-27b",
)
```

Session rows carry `name`, `checkpointName`, `checkpointType`, `promotable`, and `createTime`. `checkpointName` is the server-side checkpoint id — prefixed with the source run id and, for sampler snapshots, suffixed with an 8-hex-char session id — not the bare name you saved. `checkpointType` values are full server enum strings (`CHECKPOINT_TYPE_TRAINING_LORA` for train-state, `CHECKPOINT_TYPE_INFERENCE_LORA` for sampler snapshots); treat the field as opaque and filter on `promotable`. As with job-scoped promotion, only sampler (`INFERENCE_*`) snapshots are promotable; train-state (`TRAINING_*`) checkpoints are resume-only. List and promote require the session and its bound trainer to still exist — promote before tearing the session down. See [Saving and loading checkpoints (serverless)](/fine-tuning/training-api/serverless#saving-and-loading-checkpoints) for the serverless save / resume flow.

## Sampler refresh / weight sync

Weight sync pushes a checkpoint onto a running inference deployment without restarting it. With the SDK-managed service client, you do this by saving sampler weights and then creating a sampler for that snapshot:

```python theme={null}
saved = training_client.save_weights_for_sampler(f"step-{step:05d}").result()

# Tinker-shaped sampler wrapper.
sampler = service.create_sampling_client(model_path=saved.path)

# Or, for tokenized rollout/eval features:
deployment_sampler = service.create_deployment_sampler(
    model_path=saved.path,
    tokenizer=tokenizer,
    concurrency_controller=controller,
)
```

<Note>
  The service client owns the base/delta chain, incremental weight-sync metadata, deployment weight-sync call, and sampler construction. Existing low-level code that manually uses `DeploymentManager` or `WeightSyncer` should be treated as compatibility code; new user loops should use the service-client pattern above.
</Note>

## Train-state checkpoints

Use `save_state` to persist full training state, and one of two load methods to restore it:

| Method                            | Weights  | Optimizer state |
| --------------------------------- | -------- | --------------- |
| `load_state_with_optimizer(path)` | Restored | Restored        |
| `load_state(path)`                | Restored | Reset to zero   |

```python theme={null}
# Save full train state for resume
training_client.save_state("train_state_step_100").result()

# Resume training (weights + optimizer restored)
training_client.load_state_with_optimizer("train_state_step_100").result()
```

`save_state` accepts an optional `timeout` parameter. When set, the SDK blocks until the save completes or the timeout expires.

<Note>
  For the raw `FiretitanTrainingClient`, `save_state()`, `load_state()`, and `load_state_with_optimizer()` return futures — call `.result()` to block. The cookbook's `ReconnectableClient` wrapper blocks for you.
</Note>

### Cross-job checkpoint resolution

```python theme={null}
checkpoint_ref = training_client.resolve_checkpoint_path(
    "step-4",
    source_job_id="<source-job-id>",
)
training_client.load_state_with_optimizer(checkpoint_ref).result()
```

### Resuming and then exporting weights

`save_weights_for_sampler` / `save_weights_for_sampler_ext` export the trainer session's **currently active** weights (for LoRA, the active adapter). During normal training this is unambiguous: an `optim_step` runs just before the export, so "active weights" means "the weights you just updated." Right after a **resume**, there is no intervening `optim_step`, so be deliberate about the order:

```python theme={null}
# 1. Load the train-state checkpoint you want to continue from.
training_client.load_state_with_optimizer(checkpoint_ref).result()

# 2. Export exactly those loaded weights to a sampler snapshot.
saved = training_client.save_weights_for_sampler_ext(
    "warmstart-step-N",
    checkpoint_type="base",
)

# 3. Serve / sync that snapshot (promote or hot-load `saved.path`).
```

<Warning>
  Do not let anything change the active weights between the load in step 1 and the export in step 2: no stale adapter from a prior state, no other concurrent training step, and no second `load_*` call. If a sampler export immediately after `load_state_with_optimizer` produces a snapshot whose weights differ from the DCP step you requested, the state being exported is not the state you loaded. Capture the source job ID, the requested checkpoint name, and the exported snapshot identity, and contact Fireworks support. A storage-backend change can cause the loader to resolve the latest checkpoint rather than the requested one on a cross-job resume, which produces this symptom. See [Troubleshooting a failed resume](/fine-tuning/training-api/cookbook/checkpoints#troubleshooting).
</Warning>

### List available checkpoints

```python theme={null}
checkpoint_names = training_client.list_checkpoints()
print(checkpoint_names)  # e.g. ["step-2", "step-4"]
```

## Related guides

* [Checkpoints and Resume (cookbook)](/fine-tuning/training-api/cookbook/checkpoints) — recipe-driven save / resume / promote (start here for most users)
* [FiretitanServiceClient reference](/fine-tuning/training-api/reference/service-client) — managed trainer/deployment clients and sampler refresh
* [DeploymentManager reference](/fine-tuning/training-api/reference/deployment-manager) — compatibility weight-sync API for existing low-level integrations
