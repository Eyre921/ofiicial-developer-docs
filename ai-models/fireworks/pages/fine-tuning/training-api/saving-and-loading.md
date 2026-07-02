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

| `checkpoint_type` | What it saves               | Size                   |
| ----------------- | --------------------------- | ---------------------- |
| `"base"`          | Full model weights          | Large (\~16 GB for 8B) |
| `"delta"`         | XOR diff from previous base | \~10× smaller          |

Delta is much faster for per-step weight sync (`current_weights = base XOR delta` on the deployment). LoRA sampler checkpoints always contain the full adapter regardless of `checkpoint_type`.

<Warning>
  On full-parameter training, `checkpoint_type="delta"` produces a blob that cannot be promoted — only `"base"` can. Use the SDK-managed service path (`save_weights_for_sampler` -> `create_sampling_client(model_path=...)`) or the cookbook recipe weight-sync path for the safe base-then-delta pattern. The cookbook's `TrainingCheckpoints.save(promotable=True)` always saves `base`.
</Warning>

### Saving checkpoints

```python theme={null}
# First checkpoint — must be base (full weights)
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

# With TTL (auto-delete after N seconds)
saved = training_client.save_weights_for_sampler(
    "temp-checkpoint",
    checkpoint_type="delta",
    ttl_seconds=3600,
).result()
```

`save_weights_for_sampler_ext(...)` is the Fireworks-specific low-level variant that returns `SaveSamplerResult` directly. Use it when you need a concrete return value immediately; use `save_weights_for_sampler(...).result()` for the Tinker-shaped API.

## Promoting a checkpoint to a model

Promote a sampler checkpoint to a deployable Fireworks model. Available on [`FireworksClient`](/fine-tuning/training-api/reference/fireworks-client) and on the SDK-managed [`FiretitanServiceClient`](/fine-tuning/training-api/reference/service-client) after provisioning. The trainer job does not need to be running — its row only needs to exist; promotion is a metadata + file-copy operation. See [Checkpoint kinds](/fine-tuning/training-api/cookbook/checkpoints#checkpoint-kinds) for which checkpoints are promotable.

### Preferred: pass the 4-segment `name=` from `list_checkpoints`

`list_checkpoints` returns each checkpoint's full resource name (`accounts/<account>/rlorTrainerJobs/<job>/checkpoints/<id>`). Hand that string straight to `promote_checkpoint` — no manual disassembly into `(job_id, checkpoint_id)`:

```python theme={null}
from fireworks.training.sdk import FireworksClient

client = FireworksClient(api_key=api_key)

# Pick a row from the trainer's checkpoints — usually newest promotable.
rows = client.list_checkpoints(job_id)
target = next(r for r in rows if r.get("promotable"))

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
entry = client.list_checkpoints(endpoint.job_id)[0]
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

`save_state` accepts optional `ttl_seconds` and `timeout` parameters. When `timeout` is set, the SDK blocks until the save completes or the timeout expires.

<Note>
  For the raw `FiretitanTrainingClient`, `save_state()`, `load_state()`, and `load_state_with_optimizer()` return futures — call `.result()` to block. The cookbook's `ReconnectableClient` wrapper blocks for you.
</Note>

### Cross-job checkpoint resolution

```python theme={null}
checkpoint_ref = training_client.resolve_checkpoint_path(
    "step-4",
    source_job_id="previous-job-id",
)
training_client.load_state_with_optimizer(checkpoint_ref).result()
```

### List available checkpoints

```python theme={null}
checkpoint_names = training_client.list_checkpoints()
print(checkpoint_names)  # e.g. ["step-2", "step-4"]
```

## Related guides

* [Checkpoints and Resume (cookbook)](/fine-tuning/training-api/cookbook/checkpoints) — recipe-driven save / resume / promote (start here for most users)
* [FiretitanServiceClient reference](/fine-tuning/training-api/reference/service-client) — managed trainer/deployment clients and sampler refresh
* [DeploymentManager reference](/fine-tuning/training-api/reference/deployment-manager) — compatibility weight-sync API for existing low-level integrations
