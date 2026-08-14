---
title: "Fine-tuning"
source: https://docs.together.ai/reference/cli/finetune
path: reference/cli/finetune
---

Create, monitor, and manage fine-tuning jobs from your terminal.

## Create

To start a new fine-tuning job:

```bash theme={null}
tg fine-tuning create --training-file [FILE_ID | PATH] --model [MODEL]

# Shorthand
tg ft -c --training-file [FILE_ID | PATH] --model [MODEL]
```

You must provide either `--model` (to start from a base model) or `--from-checkpoint` (to resume from a previous job). Before the job is submitted, the CLI prints an estimated price and asks for confirmation. Pass `--confirm` (or `-y`) to skip the prompt in scripts and CI.

<Note>
  If `--training-file` (or `--validation-file`) is a local path, the CLI uploads the file to the Files API automatically before kicking off the job.
</Note>

### Parameters

| Flag                                        | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--training-file/-t [string \| Path]`       | **required**<br />Training file ID from the Files API or a local path to upload. The maximum allowed file size is 25 GB.                                                                                                                                                                                                                                                                             |
| `--model [string]`                          | Base model to fine-tune. See [supported models](/docs/fine-tuning/supported-models). Required unless `--from-checkpoint` is set.                                                                                                                                                                                                                                                                     |
| `--from-checkpoint [string]`                | Continue training from a previous fine-tuning job. Format: `JOB_ID/OUTPUT_MODEL_NAME:STEP`. The step is optional. The final checkpoint is used when omitted. Mutually exclusive with `--model`.                                                                                                                                                                                                      |
| `--validation-file/-v [string]`             | Validation file ID from the Files API or a local path to upload. Required when `--n-evals > 0`. The maximum allowed file size is 25 GB.                                                                                                                                                                                                                                                              |
| `--suffix [string]`                         | Up to 40 characters appended to the fine-tuned model name. Recommended to differentiate fine-tuned models.                                                                                                                                                                                                                                                                                           |
| `--packing/--no-packing`                    | Whether to use sequence packing for training. Default: enabled.                                                                                                                                                                                                                                                                                                                                      |
| `--max-seq-length [integer]`                | Maximum sequence length to use for training. Required when `--no-packing` is set. Defaults to the maximum allowed for the model and training type.                                                                                                                                                                                                                                                   |
| `--n-epochs/-ne [integer]`                  | Number of epochs to fine-tune on the dataset. Default: 1. Min: 1. Max: 20.                                                                                                                                                                                                                                                                                                                           |
| `--n-evals [integer]`                       | Number of evaluation loops to run on the validation set. Default: 0. Min: 0. Max: 100.                                                                                                                                                                                                                                                                                                               |
| `--n-checkpoints/-c [integer]`              | The number of checkpoints to save during training. Default: 1. One checkpoint is always saved on the last epoch. Must be 1 ≤ n-checkpoints ≤ n-epochs.                                                                                                                                                                                                                                               |
| `--batch-size/-b [integer \| max]`          | Batch size for each training iteration. See [supported models](/docs/fine-tuning/supported-models) for min and max batch sizes per model. Default: `max`.                                                                                                                                                                                                                                            |
| `--learning-rate/-lr [float]`               | Learning rate multiplier. Default: 0.00001. Min: 0.00000001. Max: 0.01.                                                                                                                                                                                                                                                                                                                              |
| `--lr-scheduler-type [linear \| cosine]`    | Learning rate scheduler type. Default: `cosine`.                                                                                                                                                                                                                                                                                                                                                     |
| `--min-lr-ratio [float]`                    | Ratio of the final learning rate to the peak learning rate. Default: 0.0. Min: 0.0. Max: 1.0.                                                                                                                                                                                                                                                                                                        |
| `--scheduler-num-cycles [float]`            | Number or fraction of cycles for the cosine learning rate scheduler. Must be non-negative. Default: 0.5.                                                                                                                                                                                                                                                                                             |
| `--warmup-ratio [float]`                    | Fraction of steps at the start of training to linearly warm up the learning rate. Default: 0.0. Min: 0.0. Max: 1.0.                                                                                                                                                                                                                                                                                  |
| `--max-grad-norm [float]`                   | Max gradient norm for gradient clipping. Set to 0 to disable. Default: 1.0. Min: 0.0.                                                                                                                                                                                                                                                                                                                |
| `--weight-decay [float]`                    | Weight decay for the optimizer. Default: 0.0. Min: 0.0.                                                                                                                                                                                                                                                                                                                                              |
| `--random-seed [integer]`                   | Random seed for reproducible training. Uses the server default if unset.                                                                                                                                                                                                                                                                                                                             |
| `--confirm/-y`                              | Skip the price-confirmation prompt. Useful in scripts and CI.                                                                                                                                                                                                                                                                                                                                        |
| `--train-on-inputs [true \| false \| auto]` | Whether to mask user messages in conversational data or prompts in instruction data.<br /><br />`auto` infers from the data format:<ul><li>Datasets with the `"text"` field (general format): inputs are not masked.</li><li>Datasets with the `"messages"` field (conversational format) or `"prompt"` and `"completion"` fields (instruction format): inputs are masked.</li></ul>Default: `auto`. |
| `--train-vision/--no-train-vision`          | Update the vision encoder parameters. Default: `false`. *Only available for vision-language models.*                                                                                                                                                                                                                                                                                                 |
| `--from-hf-model [string]`                  | Hugging Face Hub repository to start training from. Should match the base model's architecture and size. When `--lora` is set with `--lora-trainable-modules all-linear`, the modules `k_proj, o_proj, q_proj, v_proj` are targeted for adapter training.                                                                                                                                            |
| `--hf-model-revision [string]`              | Revision (branch name or commit hash) of the Hugging Face Hub model.                                                                                                                                                                                                                                                                                                                                 |
| `--hf-api-token [string]`                   | Hugging Face API token for downloading from a private repo or uploading the output model.                                                                                                                                                                                                                                                                                                            |
| `--hf-output-repo-name [string]`            | Hugging Face repo to upload the fine-tuned model to.                                                                                                                                                                                                                                                                                                                                                 |

#### Weights & Biases

| Flag                            | Description                                                                                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `--wandb-api-key [string]`      | Your Weights & Biases API key. Falls back to the `WANDB_API_KEY` environment variable.                      |
| `--wandb-base-url [string]`     | Base URL of a dedicated Weights & Biases instance. Leave empty if you are not using a self-hosted instance. |
| `--wandb-project-name [string]` | Weights & Biases project for your run. Defaults to `together`.                                              |
| `--wandb-name [string]`         | Weights & Biases run name.                                                                                  |
| `--wandb-entity [string]`       | Weights & Biases entity (team or user).                                                                     |

#### LoRA

| Flag                                | Description                                                                                                                                                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--lora/--no-lora`                  | Force LoRA fine-tuning (`--lora`) or full fine-tuning (`--no-lora`). When omitted, the API auto-detects: it defaults to LoRA on most base models, and inherits the parent job's training type when `--from-checkpoint` is set. |
| `--lora-r [integer]`                | Rank for LoRA adapter weights. Default: 8. Min: 1. Max: 64.                                                                                                                                                                    |
| `--lora-alpha [integer]`            | Alpha for LoRA adapter training. Default: 8. Min: 1.                                                                                                                                                                           |
| `--lora-dropout [float]`            | Dropout probability for LoRA layers. Default: 0.0. Min: 0.0. Max: 1.0.                                                                                                                                                         |
| `--lora-trainable-modules [string]` | Comma-separated list of LoRA trainable modules. Default: `all-linear`. See [supported modules for LoRA training](/docs/fine-tuning/lora-vs-full#default-target-modules).                                                       |

#### Preference fine-tuning (DPO, RPO, SimPO)

| Flag                                  | Description                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--training-method [sft \| dpo]`      | Training method. `sft` is supervised fine-tuning. `dpo` is Direct Preference Optimization. Default: `sft`. The DPO method also accepts the RPO and SimPO loss modifiers below. |
| `--dpo-beta [float]`                  | Beta parameter for DPO training. Only used when `--training-method dpo`.                                                                                                       |
| `--dpo-normalize-logratios-by-length` | Normalize logratios by sample length. Only used when `--training-method dpo`. Default: `false`.                                                                                |
| `--rpo-alpha [float]`                 | RPO alpha parameter (adds NLL term to the DPO loss). Only used when `--training-method dpo`.                                                                                   |
| `--simpo-gamma [float]`               | SimPO gamma parameter. Only used when `--training-method dpo`.                                                                                                                 |

<Tip>
  The `id` field in the JSON response contains the fine-tune job ID (`ft-…`) that you use to retrieve status, list events, cancel the job, and download weights.
</Tip>

## List

To list past and running fine-tune jobs:

```bash theme={null}
tg fine-tuning list

# Shorthand
tg ft ls
```

Jobs are listed newest first.

## Retrieve

To retrieve metadata for a job, including its current status:

```bash theme={null}
tg fine-tuning retrieve [FT_ID]
```

Completed jobs also include Together model registry IDs and human-readable object names for the final weights:

| Field                        | Description                                                                                                                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_object_id`            | Registry object ID for the final model weights (for example, `ml_...`).                                                                                                                                                    |
| `model_object_revision_id`   | Registry revision ID for the final model weights (for example, `rv_...`).                                                                                                                                                  |
| `model_object_name`          | Qualified registry name in `<project_slug>/<model_name>` form (for example, `acme-corp/my-model-abc123`). Resolved on retrieve. Omitted on list. Falls back to `model_object_id` when the project slug cannot be resolved. |
| `adapter_object_id`          | Registry object ID for the final LoRA adapter weights on LoRA jobs.                                                                                                                                                        |
| `adapter_object_revision_id` | Registry revision ID for the final LoRA adapter weights on LoRA jobs.                                                                                                                                                      |
| `adapter_object_name`        | Qualified adapter name in `<project_slug>/<model_name>-adapter` form on LoRA jobs. Falls back to `adapter_object_id` when the project slug cannot be resolved.                                                             |

## List events

To list events of a past or running job:

```bash theme={null}
tg fine-tuning list-events [FT_ID]
```

## Cancel

To cancel a running job:

```bash theme={null}
tg fine-tuning cancel [FT_ID]
```

## Preview

To preview how a training file will be tokenized before you start a job:

```bash theme={null}
tg fine-tuning preview --model [MODEL] --training-file [FILE_ID]

# Shorthand
tg ft preview -M [MODEL] -t [FILE_ID]
```

The command samples rows from your uploaded JSONL training file and shows how the base model's tokenizer and chat template tokenize them, including which tokens contribute to training loss.

<CodeGroup>
  ```bash Basic theme={null}
  tg fine-tuning preview \
    --model Qwen/Qwen2-1.5B \
    --training-file <file_id>
  ```

  ```bash More rows theme={null}
  tg fine-tuning preview \
    --model Qwen/Qwen2-1.5B \
    --training-file <file_id> \
    --top-k 10
  ```

  ```bash Tokenized output if prompt tokens are included in loss theme={null}
  tg fine-tuning preview \
    --model Qwen/Qwen2-1.5B \
    --training-file <file_id> \
    --train-on-inputs
  ```

  ```bash JSON output theme={null}
  tg fine-tuning preview \
    --model Qwen/Qwen2-1.5B \
    --training-file <file_id> \
    --json > preview.json
  ```
</CodeGroup>

The default table output prints the detected **Dataset format**, **Max sequence**, and **Train inputs** settings, then a **Preview Rows** table with these columns:

| Column            | Description                                                                         |
| ----------------- | ----------------------------------------------------------------------------------- |
| **Row**           | 1-based index of the sampled training file row.                                     |
| **Tokens**        | Total token count after truncation.                                                 |
| **Trained**       | Number of tokens that contribute to training loss.                                  |
| **Truncated**     | `yes` when the row was truncated to the model maximum sequence length.              |
| **Trained Spans** | Half-open token index ranges that contribute to training loss (for example, `1-3`). |
| **Token Preview** | First 32 token strings. Masked tokens (excluded from loss) appear dimmed.           |

Pass `--json` to print the full API response instead of the table.

### Parameters

| Flag                                     | Description                                                                                                |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `--training-file/-t [string]`            | **required**<br />Training file ID from the Files API to sample for preview.                               |
| `--model/-M [string]`                    | **required**<br />Base model whose tokenizer and chat template are used for the preview.                   |
| `--top-k [integer]`                      | Maximum number of rows from the start of the training file to tokenize. Default: `5`. Min: 1. Max: 50.     |
| `--train-on-inputs/--no-train-on-inputs` | Whether prompt or user-message tokens contribute to training loss. When omitted, the API default applies.  |
| `--training-method [sft]`                | Fine-tuning method to preview. Only supervised fine-tuning (`sft`) is currently supported. Default: `sft`. |

## Model limits

To check a model's fine-tuning limits before you configure a job:

```bash theme={null}
tg fine-tuning model-limits [MODEL]

# Shorthand
tg ft model-limits -M [MODEL]
```

The command prints the model's fine-tuning constraints, including learning-rate bounds, epoch and checkpoint maximums, the maximum sequence lengths for SFT and DPO, and the per-method limits for LoRA and full training (batch-size bounds, maximum LoRA rank, and available LoRA target modules). Models that only support LoRA report `Supports Full Training: False`. Pass `--json` for the raw response.

See [Supported models](/docs/fine-tuning/supported-models) for the list of models available for fine-tuning.

## List checkpoints

To list saved checkpoints of a job:

```bash theme={null}
tg fine-tuning list-checkpoints [FT_ID]
```

The default output is a table with **Download ID**, **Timestamp**, **Registry Artifact**, and **Type** columns. Use the Download ID with `tg fine-tuning download`: intermediate checkpoints use `FT_ID:STEP`, and the final checkpoint uses the job ID alone.

When the job uploaded the artifact to the Together model registry, the **Registry Artifact** column shows `object_name` when available (for example, `acme-corp/my-model-abc123-100`). It falls back to `object_id@object_revision_id` (for example, `ml_…@rv_…`) when the name is unavailable. The CLI also prints a copyable **Registry artifacts** block below the table.

Pass `--json` to get the full response body instead. Each checkpoint includes `step`, `path`, `created_at`, `checkpoint_type`, and `checkpoint` (the download selector: `model` or `adapter`). When the job uploaded the artifact to the Together model registry, the entry also includes `object_id`, `object_revision_id` (for example, `ml_…` and `rv_…`), and `object_name` (the qualified `<project_slug>/<model_name>` name for that checkpoint, with `-<step>` or `-adapter` suffixes as appropriate). See [Model registry object IDs](/docs/fine-tuning/deployment#model-registry-object-ids) for how these relate to the job-level `model_object_id` / `adapter_object_id` fields.

## Download model weights

To download the weights of a fine-tuned model, run:

<CodeGroup>
  ```bash Basic theme={null}
  # Download the model to the current working directory.
  tg fine-tuning download [FT_ID]
  ```

  ```bash Specify directory theme={null}
  tg fine-tuning download [FT_ID] \
    --output-dir ./models
  ```

  ```bash Download checkpoint theme={null}
  # Use `tg fine-tuning list-checkpoints` to find the checkpoint index.
  tg fine-tuning download [FT_ID] \
    --checkpoint-step 0
  ```

  ```bash Download LoRA adapter theme={null}
  tg fine-tuning download [FT_ID] \
    --checkpoint-type adapter
  ```
</CodeGroup>

The command downloads Zstandard-compressed (`.zst`) weights. To extract them, run `tar -xf filename`.

### Parameters

| Flag                                                  | Description                                                                                                                                                               |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir/-o [Path]`                              | Output directory.                                                                                                                                                         |
| `--checkpoint-step/-s [integer]`                      | Download a specific checkpoint's weights. Defaults to the latest checkpoint.                                                                                              |
| `--checkpoint-type/-c [merged \| adapter \| default]` | Checkpoint type. `merged` and `adapter` apply to LoRA jobs only. `default` resolves to `merged` for LoRA jobs and to the full model for non-LoRA jobs. Default: `merged`. |

## Download tokenized dataset

To download the tokenized dataset a job trained on:

```bash theme={null}
tg fine-tuning download-tokenized-dataset [FT_ID] \
  --output-dir ./datasets
```

The command saves a Zstandard-compressed archive named `[FT_ID]_tokenized_datasets.tar.zst` to the output directory (default: the current working directory). To extract it, run `tar -xf filename`. Use it to audit exactly what the model was trained on, for example to inspect the tokenization and loss masking of a finished job.

### Parameters

| Flag                     | Description                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| `--output-dir/-o [Path]` | Directory to save the tokenized dataset archive. Default: the current working directory. |

## Delete

To delete a fine-tuning job:

```bash theme={null}
tg fine-tuning delete [FT_ID]

# Shorthand
tg ft -d [FT_ID]
```

### Parameters

| Flag      | Description                 |
| --------- | --------------------------- |
| `--force` | Bypass confirmation prompt. |
