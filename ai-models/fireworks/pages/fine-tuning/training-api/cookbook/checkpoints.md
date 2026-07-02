---
title: "Checkpoints and Resume"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/checkpoints
path: fine-tuning/training-api/cookbook/checkpoints
---

Save training progress, resume from failures, and promote checkpoints to deployable models — driven by the recipe.

## TL;DR

If you launch training through a cookbook recipe (`rl_loop`, `sft_loop`, `dpo_loop`, `orpo_loop`, `igpo_loop`), you don't have to call any checkpoint APIs yourself. Set two config fields and the recipe handles save, resume, and promote:

* `dcp_save_interval=N` (top-level `Config` field on every recipe) — save resumable checkpoints every N steps
* `output_model_id="my-model"` — promote the final checkpoint to a deployable Fireworks model

Rerunning with the same `log_path` resumes from the last saved checkpoint automatically.

```python theme={null}
from training.recipes.sft_loop import Config, main
from training.utils import TrainerConfig

cfg = Config(
    log_path="./my_training",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    output_model_id="qwen3-8b-finetuned",
    dcp_save_interval=10,
    trainer=TrainerConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
)
main(cfg)

# Interrupted? Run again with the same config — it picks up automatically.
main(cfg)
```

That's the full surface most users need. The rest of this page covers config knobs, manual promotion via the CLI, and (under [Advanced internals](#advanced-internals)) what the recipe is doing under the hood.

<Warning>
  `dcp_save_interval` defaults to `0` (off). Without setting it to a positive value, training cannot be resumed from intermediate steps.
</Warning>

## Config fields

| Field                  | Applies to  | Type          | Default    | Description                                                                                                                                |
| ---------------------- | ----------- | ------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `log_path`             | All recipes | `str`         | (required) | Directory for the recipe's local bookkeeping (`dataloader.json`) and logs                                                                  |
| `dcp_save_interval`    | All recipes | `int`         | `0`        | Save a resumable (DCP) checkpoint every N steps. `0` = off. Top-level `Config` field on every recipe (RL, IGPO, async RL, SFT, DPO, ORPO). |
| `output_model_id`      | All recipes | `str \| None` | `None`     | If set, promote the final checkpoint to this Fireworks model ID at the end of training                                                     |
| `init_from_checkpoint` | All recipes | `str \| None` | `None`     | Load weights from another job (`"job-id:checkpoint-name"`). Step counter resets to 0.                                                      |

## Resume

### Automatic (same log\_path)

Just rerun with the same `log_path` and the recipe resumes. It queries the control plane for the newest resumable checkpoint on the trainer job and reloads weights and optimizer state. The step counter and the cookbook's `data_consumed` counter are restored from `dataloader.json` in `log_path`.

### From another job

```python theme={null}
config = Config(
    log_path="./new_run",
    init_from_checkpoint="i44pvd4syzg8hjfk:step-4",  # job_id:checkpoint_name
    ...
)
```

Loads weights from the specified job, resets step to 0. Mutually exclusive with automatic resume.

## Promoting a checkpoint manually

If you want to promote an arbitrary checkpoint after training (not just the final one), use the cookbook's promote script:

```bash theme={null}
export FIREWORKS_API_KEY=...

python promote_checkpoint.py \
    --job-id <trainer-job-id> \
    --output-model-id my-fine-tuned-model \
    --base-model accounts/fireworks/models/qwen3-8b
```

By default the script promotes the newest promotable checkpoint on the job. Pass `--checkpoint-name <name>` to promote a specific one.

You can also call the API directly — see [Saving and Loading — Promoting](/fine-tuning/training-api/saving-and-loading#promoting-a-checkpoint-to-a-model).

## Advanced internals

<Note>
  Most users can stop reading here. The sections below cover what the recipe does internally — useful only if you're forking a recipe, calling the SDK directly, or debugging a checkpoint that doesn't promote. The full SDK-level reference lives in [Saving and Loading](/fine-tuning/training-api/saving-and-loading).
</Note>

### What gets saved, where

The recipe interacts with two surfaces:

| Surface                                                    | Owns                                          | Source of truth for                                                                        |
| ---------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Control plane (`FireworksClient.list_checkpoints(job_id)`) | All remote checkpoint blobs (DCP and sampler) | What checkpoints exist, their type, and whether each is promotable                         |
| `{log_path}/dataloader.json`                               | Local file                                    | The cookbook's `data_consumed` counter per checkpoint name (no server-side representation) |

There is no `checkpoints.jsonl` registry — the control plane is queried at resume / promote time.

### Two axes: resumable and promotable

When the recipe saves a checkpoint, it picks two independent capabilities:

| Axis              | What it writes              | Resumes? | Promotes to a model? |
| ----------------- | --------------------------- | -------- | -------------------- |
| `resumable=True`  | DCP (weights + optimizer)   | Yes      | No                   |
| `promotable=True` | Sampler weights (HF format) | No       | Yes                  |
| Both              | DCP + sampler               | Yes      | Yes                  |

Periodic saves use `resumable=True` only. The final save uses both. RL weight sync saves sampler checkpoints and syncs their snapshot identities separately from DCP resume saves.

### Forking a recipe

If you fork `rl_loop.py` (or another ported recipe) and need to drive checkpointing yourself, instantiate `TrainingCheckpoints`:

```python theme={null}
from training.utils.checkpoints import TrainingCheckpoints

ckpt = TrainingCheckpoints(
    policy,           # ReconnectableClient
    service,          # FiretitanServiceClient (control-plane checkpoint client)
    trainer_id=service.trainer_job_id,
    log_path=cfg.log_path,
    lora_rank=cfg.lora_rank,
)

# Resume on startup
resume_info = ckpt.resume(
    init_from_checkpoint=cfg.init_from_checkpoint,
    warm_start_from_adapter=cfg.warm_start_from_adapter,
)
step_offset = resume_info.step if resume_info else 0

# Periodic save
ckpt.save(f"step-{step}", resumable=True, promotable=False, data_consumed=count)

# Final save + promote
ckpt.save(f"step-{step}", resumable=True, promotable=True, data_consumed=count)
if cfg.output_model_id:
    ckpt.promote_latest(cfg.output_model_id, cfg.base_model)
```

The class is intentionally thin — it forwards `save_state` / `save_weights_for_sampler_ext` / `promote_checkpoint` to the SDK and uses the control plane as the source of truth for resume and promotion. Recipes pass the SDK-managed service client as the control-plane checkpoint client. The full API surface those calls expose is documented in [Saving and Loading](/fine-tuning/training-api/saving-and-loading).

### Checkpoint kinds

This subsection is the canonical reference for checkpoint kinds and promotability across the stack — other pages link here.

Three separate layers of the stack each have their own "type", and confusing them is the usual reason a promotion fails. They are not synonyms:

| Layer        | Where                                               | Values                                                                              | What it controls                                                                                                                                                 |
| ------------ | --------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cookbook** | `TrainingCheckpoints.save(resumable=, promotable=)` | two booleans                                                                        | Which of DCP / sampler blob (or both) gets saved                                                                                                                 |
| **SDK**      | `save_weights_for_sampler_ext(checkpoint_type=...)` | `"base"`, `"delta"`                                                                 | Whether the sampler blob is full weights or an `arc_v2` delta over the previous base (LoRA ignores this — full adapter is always saved)                          |
| **Server**   | `checkpointType` on each control-plane row          | `TRAINING`, `TRAINING_LORA`, `INFERENCE_BASE`, `INFERENCE_LORA`, `INFERENCE_ARC_V2` | Detected from blob contents. The first two are resumable; `INFERENCE_BASE` and `INFERENCE_LORA` are promotable; `INFERENCE_ARC_V2` (delta on full-param) is not. |

When the cookbook saves with `promotable=True`, it always calls the SDK with `checkpoint_type="base"`, which the server detects as `INFERENCE_BASE` (full-param) or `INFERENCE_LORA` (LoRA). Both are promotable. The non-promotable `INFERENCE_ARC_V2` only happens if you bypass the cookbook and call `save_weights_for_sampler_ext("delta")` on a full-parameter run.

#### Promotability cheat sheet

"Promotable" means the server will accept the blob for promotion — i.e. the checkpoint shows `promotable=True` in `list_checkpoints`. To actually promote, you need the checkpoint name plus `source_job_id` and `base_model`.

| How it was saved                                             | LoRA promotable                         | Full-param promotable |
| ------------------------------------------------------------ | --------------------------------------- | --------------------- |
| `TrainingCheckpoints.save(resumable=True, promotable=False)` | No (DCP only)                           | No (DCP only)         |
| `TrainingCheckpoints.save(promotable=True)`                  | Yes                                     | Yes                   |
| `save_weights_for_sampler_ext(checkpoint_type="base")`       | Yes                                     | Yes                   |
| `save_weights_for_sampler_ext(checkpoint_type="delta")`      | Yes (server always stores full adapter) | No                    |
| Recipe weight sync — first save                              | Yes                                     | Yes                   |
| Recipe weight sync — later saves                             | Yes                                     | No                    |

For SDK-level details on each row (full method signatures, base-vs-delta semantics, weight-sync lifecycle), see [Saving and Loading](/fine-tuning/training-api/saving-and-loading).

## Related guides

* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) — SDK-level reference for save / load / promote
* [Training and Sampling](/fine-tuning/training-api/training-and-sampling) — SDK-managed sampler refresh lifecycle
* [Cookbook RL](/fine-tuning/training-api/cookbook/rl) — full GRPO walkthrough
