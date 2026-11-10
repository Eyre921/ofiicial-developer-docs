---
title: "Migrate from Managed Training to the Training API"
source: https://docs.fireworks.ai/fine-tuning/migrate-from-managed-training
path: fine-tuning/migrate-from-managed-training
---

Move managed SFT and DPO jobs to the Training API: clone an existing job with its settings, or start a new job with the settings you choose.

Managed supervised fine-tuning (SFT) and DPO no longer accept new jobs. Train on the [Training API](/fine-tuning/training-api/introduction) instead. Models and LoRA adapters from managed jobs stay in your account and stay deployable.

> [card] [Clone an existing job](#clone-an-existing-job)
>
> Rerun a managed job on the Training API with the same settings.

> [card] [Start a new job](#start-a-new-job)
>
> Pick the model, data and settings yourself, and get a price estimate first.

> [!NOTE]
>
> **Bring your own copy of the training data.** The Training API reads your training file directly: a local JSONL file, a directory of `.jsonl` shards, or a Google Cloud Storage path (`gs://<BUCKET>/train.jsonl`). It can't read datasets stored in Fireworks (`accounts/<ACCOUNT_ID>/datasets/<DATASET_ID>`). Use the same file you uploaded for the managed job, and its evaluation file if it had one. The row format doesn't change. For data in Amazon S3 or Azure Blob Storage, copy it to a local file or to Cloud Storage first.

## Clone an existing job

> [!NOTE]
>
> **Migration tool: [`migrate_managed_job.py`](https://github.com/fw-ai-external/cookbook/blob/main/training/examples/tools/migrate_managed_job.py)** in the Fireworks cookbook. It reads your old job's settings, maps them onto the matching training recipe, runs it, and promotes the result to a new model. See the [tool README](https://github.com/fw-ai-external/cookbook/tree/main/training/examples/tools#migrating-a-managed-fine-tuning-job) for how each setting maps.

Paste this into Claude Code, Cursor, Codex or another coding agent, from the folder that holds your training data. Fill in the values in square brackets; the [FAQ](#faq) shows where to find your job name and account ID.

> [!WARNING]
>
> Set `FIREWORKS_API_KEY` in your shell before you start the agent, and never paste the key into the agent chat. See [FAQ](#faq): "How do I keep my API key safe with a coding agent?"

```text wrap theme={null}
Set up Fireworks training for me: fetch https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents.md and follow it. Then clone my managed fine-tuning job to the Training API with the same settings, following https://docs.fireworks.ai/fine-tuning/migrate-from-managed-training.md.

- Job: [accounts/ACCOUNT_ID/supervisedFineTuningJobs/JOB_ID, or for DPO: accounts/ACCOUNT_ID/dpoJobs/JOB_ID]
- Training data: [./train.jsonl]
- New model ID: [NEW_MODEL_ID]

My API key is already set as FIREWORKS_API_KEY in this shell. Never ask me to paste it, and never print it.

Do a dry run first. Show me the plan and a price estimate, and wait for my approval before you start training.
```

> [accordion] Run it with the Python API instead
>
> **Set up once.**
>
> * Create an API key in the account that owns the job, in the [dashboard](https://app.fireworks.ai/settings/users/api-keys) or with `firectl api-key create`. The Training API rejects keys that can reach more than one account. If you belong to several Fireworks accounts, use a [service account](/accounts/service-accounts) key created in the job's account.
> * Install Python 3.11 or newer and [uv](https://docs.astral.sh/uv/getting-started/installation/).
>
> ```bash theme={null}
> read -s FIREWORKS_API_KEY && export FIREWORKS_API_KEY
> git clone https://github.com/fw-ai-external/cookbook.git
> cd cookbook/training
> uv venv --python 3.12 && source .venv/bin/activate
> uv pip install -e .
> ```
>
> Call the migration tool from Python, and review the plan before you train:
>
> ```python theme={null}
> import logging
> import os
>
> from training.examples.tools.migrate_managed_job import (
>     FireworksReader,
>     MigrationInputs,
>     describe_plan,
>     read_plan,
>     run_plan,
> )
>
> logging.basicConfig(level=logging.INFO)
>
> plan = read_plan(
>     FireworksReader(os.environ["FIREWORKS_API_KEY"]),
>     MigrationInputs(
>         dataset_path="./train.jsonl",
>         output_model_id="<NEW_MODEL_ID>",
>         log_path="./migrated_runs/<JOB_ID>",
>     ),
>     "accounts/<ACCOUNT_ID>/supervisedFineTuningJobs/<JOB_ID>",
> )
> print(describe_plan(plan))  # the recipe, serverless or dedicated, and the full config
> run_plan(plan)
> ```
>
> * For a DPO or ORPO job, pass `accounts/<ACCOUNT_ID>/dpoJobs/<JOB_ID>`.
> * `MigrationInputs` also takes `eval_dataset_path`, `mode` (`"auto"`, `"serverless"` or `"dedicated"`), `tokenizer_model` and `max_seq_len`.
> * `plan.config` is the recipe `Config` the run uses. The tool saves a resumable checkpoint every 20 steps, as managed training did.
>
> **Run, watch and resume**
>
> * The training loop runs in your Python process for the whole job, not on Fireworks. If the process stops, training stops. For long runs, use a machine that stays on, such as a cloud VM, and keep the output in a log file: `nohup python train.py > train.log 2>&1 &`.
> * Watch the loss in the log, in Weights & Biases, or on the [training dashboard](https://app.fireworks.ai/dashboard/fine-tuning).
> * If the run stops early, the tool prints how to continue it from its newest checkpoint, with the same `log_path`. Lost the output? See "My run stopped. How do I resume it?" in the [FAQ](#faq).
> * A dedicated trainer [stops after 60 minutes](/fine-tuning/training-api/reference/cleanup) without activity. If your process dies, the trainer keeps billing until then.

## Start a new job

> [!NOTE]
>
> **Training recipes: [`sft_loop.py`](https://github.com/fw-ai-external/cookbook/blob/main/training/recipes/sft_loop.py) and [`dpo_loop.py`](https://github.com/fw-ai-external/cookbook/blob/main/training/recipes/dpo_loop.py)** in the Fireworks cookbook. Each one runs the whole job from your data to a deployable model. For step-by-step guides, see [Cookbook: SFT](/fine-tuning/training-api/cookbook/sft) and [Cookbook: DPO](/fine-tuning/training-api/cookbook/dpo).

Use this path if you have no managed job to clone, for example because you only used the dashboard, or if you want different settings. Paste this into your coding agent, from the folder that holds your training data. Fill in the values in square brackets. Leave a setting as `[default]` to let the agent choose it and show you its choice in the plan.

```text wrap theme={null}
Set up Fireworks training for me: fetch https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents.md and follow it. Then start a new training job on the Fireworks Training API, following https://docs.fireworks.ai/fine-tuning/migrate-from-managed-training.md.

- Method: [SFT or DPO]
- Base model: [BASE_MODEL, for example Qwen3 8B]
- Training data: [./train.jsonl]
- Evaluation data: [none, or ./eval.jsonl]
- New model ID: [NEW_MODEL_ID]
- Epochs: [default] (whole number, usually 1–3)
- Learning rate: [default] (usually 5e-5 to 1.5e-4 for SFT, about 1e-5 for DPO)
- LoRA rank: [default] (usually 8–32; up to 64 on most serverless models)
- Batch size: [default] (rows per step for SFT, preference pairs per step for DPO)
- Max context length: [default] (tokens; your longest example, up to the model's maximum)
- Weights & Biases entity: [none] (or your W&B username or team; set WANDB_API_KEY first)

My API key is already set as FIREWORKS_API_KEY in this shell. Never ask me to paste it, and never print it.

Check my data first. Then show me the full configuration and a price estimate, and wait for my approval before you start training.
```

> [accordion] Run it with the Python API instead
>
> Set up as in [Clone an existing job](#clone-an-existing-job), then build the recipe `Config` and run it. These examples train a LoRA adapter on [serverless training](/fine-tuning/training-api/serverless), which needs no provisioning and bills per token. Every setting is a field on the recipe's `Config`.
>
> ```python SFT theme={null}
> import logging
>
> import training.recipes.sft_loop as sft_loop
>
> logging.basicConfig(level=logging.INFO)
>
> sft_loop.main(
>     sft_loop.Config(
>         serverless=True,
>         log_path="./runs/<NEW_MODEL_ID>",
>         base_model="accounts/fireworks/models/<BASE_MODEL>",
>         tokenizer_model="<HF_ORG>/<HF_REPO>",
>         dataset="./train.jsonl",
>         evaluation_dataset="./eval.jsonl",  # optional
>         output_model_id="<NEW_MODEL_ID>",
>         epochs=1,
>         learning_rate=1e-4,
>         warmup_steps=10,
>         lora_rank=16,
>         lora_alpha=32,
>         weight_decay=0.01,
>         batch_size=32,
>         max_seq_len=32768,
>         dcp_save_interval=20,  # resumable checkpoint every 20 steps
>     )
> )
> ```
>
> ```python DPO theme={null}
> import logging
>
> import training.recipes.dpo_loop as dpo_loop
> from training.utils import RunnerConfig
>
> logging.basicConfig(level=logging.INFO)
>
> dpo_loop.main(
>     dpo_loop.Config(
>         serverless=True,
>         log_path="./runs/<NEW_MODEL_ID>",
>         base_model="accounts/fireworks/models/<BASE_MODEL>",
>         tokenizer_model="<HF_ORG>/<HF_REPO>",
>         dataset="./preferences.jsonl",
>         evaluation_dataset="./eval.jsonl",  # optional
>         output_model_id="<NEW_MODEL_ID>",
>         epochs=1,
>         learning_rate=1e-5,
>         lora_rank=8,
>         batch_size=4,
>         max_seq_len=32768,
>         dcp_save_interval=20,  # resumable checkpoint every 20 steps
>         # A resumed run must score against the same reference model.
>         runner=RunnerConfig(
>             reference_checkpoint_file="./runs/<NEW_MODEL_ID>/reference_checkpoint.json",
>         ),
>     )
> )
> ```
>
> * `serverless=True` works only on the [serverless models](#faq). For any other base model, remove it to train on a dedicated trainer; see "Should I use Serverless or Dedicated Training?" in the [FAQ](#faq).
> * Always set `lora_rank`. The recipe default of `0` means full-parameter training, which needs a dedicated trainer.
> * `tokenizer_model` is the Hugging Face repo of the base model, such as `Qwen/Qwen3-8B`. A mismatch corrupts training.
> * For a `gs://` dataset, also set `dataset_loading_mode="stream"`, install `google-cloud-storage`, and sign in with `gcloud auth application-default login`.
> * For Weights & Biases charts, pass `wandb=WandBConfig(entity="<WANDB_ENTITY>")` (from `training.utils`) and set `WANDB_API_KEY`.
>
> **Run, watch and resume**
>
> * The training loop runs in your Python process for the whole job, not on Fireworks. If the process stops, training stops. For long runs, use a machine that stays on, such as a cloud VM, and keep the output in a log file: `nohup python train.py > train.log 2>&1 &`.
> * Watch the loss in the log, in Weights & Biases, or on the [training dashboard](https://app.fireworks.ai/dashboard/fine-tuning). For SFT the loss should fall over the first epoch. For DPO, `dpo_loss` starts near 0.69 and should fall while `accuracy` rises.
> * If a serverless run stops, rerun it with the same `log_path` and `init_from_checkpoint="<ACCOUNT_ID>/<RUN_ID>/<CHECKPOINT>"`. "My run stopped. How do I resume it?" in the [FAQ](#faq) shows where to find each value.
> * On a dedicated trainer, reattach with `trainer=TrainerConfig(job_id="<TRAINER_JOB_ID>")` while the trainer is still running, or start a new trainer from the checkpoint. A dedicated trainer [stops after 60 minutes](/fine-tuning/training-api/reference/cleanup) without activity, and keeps billing until then if your process dies.
>
> See [Checkpoints and resume](/fine-tuning/training-api/cookbook/reference#checkpoints) for details.

## Deploy the new model

The run promotes its final checkpoint to `accounts/<ACCOUNT_ID>/models/<NEW_MODEL_ID>`. Deploy it from **Models** in the [Fireworks app](https://app.fireworks.ai), or run:

```bash theme={null}
firectl deployment create accounts/<ACCOUNT_ID>/models/<NEW_MODEL_ID>
```

See [Deploying trained models](/fine-tuning/deploying-loras) for multi-LoRA deployments.

## What keeps working

For managed SFT, DPO and ORPO jobs created before November 9, 2026:

* Jobs that are queued or running finish normally.
* You can get, list, cancel and delete them in the dashboard, with `firectl`, and through the API.
* You can export DPO job metrics (`firectl dpo-job export-metrics`) and promote the checkpoints of existing jobs.
* The models they produced stay in your account and deploy as before.

## Troubleshooting

| Error | Fix |
| - | - |
| `no eligible shared trainer found for base model` | The model has no serverless pool. Train on a dedicated trainer: remove `serverless=True`, or use the migration tool, which falls back to dedicated. See "Should I use Serverless or Dedicated Training?" in the [FAQ](#faq). |
| `create_session: account not found` | Your API key reaches more than one account. Create a key in a single account. |
| HTTP 403 `tier_required` | Dedicated training needs a payment method or credits on the account. |
| HTTP 403 `quota_exceeded` | Request more [GPU quota](/guides/quotas_usage/account-quotas#training-gpu-quota), or use serverless training. |

## FAQ

> [accordion] Where do I find my job name and account ID?
>
> The agent prompt and the migration tool need the full job name, such as `accounts/<ACCOUNT_ID>/supervisedFineTuningJobs/<JOB_ID>`.
>
> * **Account ID:** run `firectl whoami`, which prints `Account ID: <ACCOUNT_ID>`.
> * **SFT job names:** run `firectl sftj list`.
> * **DPO and ORPO job names:** run `firectl dpoj list`.
>
> You can also find your jobs in the [training dashboard](https://app.fireworks.ai/dashboard/fine-tuning). To see a job's settings, run `firectl sftj get <JOB_ID>` or `firectl dpoj get <JOB_ID>`.

> [accordion] How do I keep my API key safe with a coding agent?
>
> Set the key in your shell, then start the agent from that same shell so it inherits the variable:
>
> ```bash theme={null}
> read -s FIREWORKS_API_KEY && export FIREWORKS_API_KEY
> ```
>
> * Never paste the key into the agent chat. Chat messages can be logged and sent to the agent's model provider.
> * The agent prompts on this page tell the agent the key is already set, and not to ask for it or print it.
> * If you pasted a key into a chat by mistake, delete it in the [dashboard](https://app.fireworks.ai/settings/users/api-keys) and create a new one.



\> \[accordion] Should I use Serverless or Dedicated Training?
\>
\> |                | Serverless Training                                                            | Dedicated Training                                                                          |
\> | -------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
\> | Models         | The \[serverless models]\(/fine-tuning/training-api/serverless#supported-models) | Any model with a Training API shape in \[Models]\(/fine-tuning/models)                        |
\> | Parameter mode | LoRA only                                                                      | LoRA or full-parameter                                                                      |
\> | Methods        | SFT and DPO                                                                    | SFT, DPO and ORPO                                                                           |
\> | Billing        | Per token                                                                      | Per GPU hour while the trainer runs                                                         |
\> | Limits         | 8 concurrent runs per account by default                                       | Your account's \[training GPU quota]\(/guides/quotas\_usage/account-quotas#training-gpu-quota) |Pick by what your managed job used:| Your managed job                     | Train it on                                                                                                                                              |
\> | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
\> | LoRA on a serverless model           | Serverless Training                                                                                                                                      |
\> | LoRA on any other model              | Dedicated Training, LoRA                                                                                                                                 |
\> | Full-parameter (LoRA rank \`0\`)       | Dedicated Training, full-parameter, when \[Models]\(/fine-tuning/models) lists a full-parameter shape for the base model. Otherwise, train a LoRA adapter. |
\> | ORPO                                 | Dedicated Training                                                                                                                                       |
\> | A warm start from an earlier adapter | Dedicated Training                                                                                                                                       |
\> | A reservation                        | Dedicated Training, on the same reservation                                                                                                              |\*\*Serverless models.\*\* \`serverless=True\` works only on these base models. On any other model it fails with \`no eligible shared trainer found for base model\`:
\>
\> \\\<table>\<thead>\<tr>\<th>Base model\</th>
\>               \\\<th>Model ID\</th>
\>               \\\<th>Max context\</th>\</tr>\</thead>
\>           \\\<tbody />\</table>
\>
\> \*\*Train on a dedicated trainer instead.\*\* Remove \`serverless=True\` from the \`Config\`. The recipe then provisions a dedicated trainer on a validated training shape for the base model. Everything else in the examples stays the same:\`\`\`python theme=\{null}
\> sft\_loop.Config(
\>     log\_path="./runs/\<NEW\_MODEL\_ID>",
\>     base\_model="accounts/fireworks/models/\<BASE\_MODEL>",
\>     tokenizer\_model="\<HF\_ORG>/\<HF\_REPO>",
\>     dataset="./train.jsonl",
\>     output\_model\_id="\<NEW\_MODEL\_ID>",
\>     epochs=1,
\>     learning\_rate=1e-4,
\>     lora\_rank=16,  # 0 for full-parameter, if Models lists a full-parameter shape
\>     batch\_size=32,
\>     dcp\_save\_interval=20,
\> )
\> \`\`\`A dedicated trainer uses your \[training GPU quota]\(/guides/quotas\_usage/account-quotas#training-gpu-quota) and bills per GPU hour while it runs. Without a reservation, it can wait in a queue for capacity, for up to 48 hours by default. The migration tool chooses serverless or dedicated for you.



> [accordion] My managed job's base model isn't available. What should I train instead?
>
> These base models have no Training API shape. Train a suggested replacement instead:
>
> | Your managed job's base model | Suggested replacement |
> | - | - |
> | Kimi K2.6 (`kimi-k2p6`) | Kimi K3 (`kimi-k3`) or GLM 5.3 (`glm-5p3`) |
> | Kimi K2.7 Code (`kimi-k2p7-code`) | Kimi K3 (`kimi-k3`) or GLM 5.3 (`glm-5p3`) |
> | GLM 5.1 (`glm-5p1`) | GLM 5.3 (`glm-5p3`) |
> | MiniMax M3 (`minimax-m3`) | DeepSeek V4.1 Flash 1017 (`deepseek-v4p1-flash-1017`) |
> | DeepSeek V4 Flash (`deepseek-v4-flash`) | DeepSeek V4.1 Flash 1017 (`deepseek-v4p1-flash-1017`) |
> | Qwen 2.5 32B Instruct (`qwen2p5-32b-instruct`) | Qwen 3 32B (`qwen3-32b`) |
>
> [Models](/fine-tuning/models) shows whether each replacement trains on Serverless Training, Dedicated Training, or both. A replacement is a different model, so evaluate it against your managed model before you move traffic.
>
> For any other base model with no Training API shape, including a base model you uploaded, contact your account team or [support@fireworks.ai](mailto:support@fireworks.ai).

> [accordion] My run stopped. How do I resume it?
>
> The training loop runs on your machine. If the laptop sleeps, the terminal closes or the connection drops, the run stops.
>
> **Prevent it**
>
> * For runs longer than a few minutes, use a machine that stays on, such as a cloud VM. Run under `tmux`, or with `nohup` and a log file, so the output survives a closed terminal:
>
>   ```bash theme={null}
>   nohup python train.py > train.log 2>&1 &
>   ```
>
> * Save checkpoints regularly: set `dcp_save_interval=20`, and `checkpoint_interval_minutes=30` for LoRA SFT and DPO. The migration tool sets both. Without them, a stopped run has nothing to resume from.
>
> **Find the checkpoint**
>
> Every resumable checkpoint is listed in `dataloader.json` inside the run's `log_path`. The checkpoint names are its keys, newest last:
>
> ```bash theme={null}
> python -c "import json; d = json.load(open('<LOG_PATH>/dataloader.json')); print([k for k in d.get('checkpoints', d) if k != 'schema_version'][-1])"
> ```
>
> **Resume**
>
> * **Serverless:** find the run ID in the log line `Serverless training session <SESSION_ID>, run <RUN_ID>` (for example, `grep "Serverless training session" train.log`). Rerun with the same `log_path` and `init_from_checkpoint="<ACCOUNT_ID>/<RUN_ID>/<CHECKPOINT>"`.
> * **Dedicated, trainer still running:** find the trainer job ID in the log (`Created trainer job: <TRAINER_JOB_ID>`). Rerun with the same `log_path` and `trainer=TrainerConfig(job_id="<TRAINER_JOB_ID>")` (from `training.utils`). The trainer stops after 60 minutes without activity.
> * **Dedicated, trainer gone:** rerun with the same `log_path` and `init_from_checkpoint="<TRAINER_JOB_ID>:<CHECKPOINT>"`. This starts a new trainer from that checkpoint's weights, and the dataset starts again from its first row.
> * **Migration tool:** pass the same `log_path`, plus `init_from_checkpoint` or `trainer_job_id`, to `MigrationInputs`.

> [accordion] What happens to my evaluation settings?
>
> * **Evaluation dataset.** Pass your own copy: `evaluation_dataset` on the recipe `Config`, or `eval_dataset_path` in the migration tool. The run reports evaluation loss on it.
> * **Automatic carve-out.** `eval_auto_carveout=True` holds out part of the training data for evaluation: by default 10% of the rows, at most 20 examples. Change the size with `eval_carve_ratio` and `max_eval_seqs`. The migration tool turns it on for jobs that used it.
> * **ORPO** has no held-out evaluation in the cookbook, so its evaluation settings are ignored.
>
> Evaluation loss is a training signal, not a quality check. When the run finishes, it promotes the final checkpoint to `accounts/<ACCOUNT_ID>/models/<NEW_MODEL_ID>`. Evaluate that model on your own prompts before you move traffic, and compare it with your managed model. [Evaluating Trained Models](/fine-tuning/evaluating-fine-tuned-models) covers sampling serverless checkpoints, loading a promoted LoRA onto serverless, and preemptible deployments.

> [accordion] The migration tool refused my job or warned me. What do I do?
>
> | Message | Do this instead |
> | - | - |
> | The job belongs to a CMEK (customer-managed encryption key) account | The Training API can't write CMEK-encrypted models yet. Your existing models keep working. Contact your Fireworks account team about training. |
> | The API key reaches more than one account, or belongs to a different account than the job | Create a key in the job's account only, such as a [service account](/accounts/service-accounts) key, and set `FIREWORKS_API_KEY` to it. |
> | No training data given | Pass your own copy of the job's training data as a local file or directory, or a `gs://` path. |
> | The dataset is a Fireworks dataset name (`accounts/.../datasets/...`) | Pass a local file or a `gs://` path instead. The Training API can't read Fireworks datasets. |
> | The output model ID is the managed job's output model | Choose a new model ID. |
> | ORPO with `gs://` data | Copy the data to a local file. |
> | The job can't run on serverless training (with `mode="serverless"`) | Use `mode="auto"` or `mode="dedicated"`. |
> | The tool can't tell which tokenizer the base model uses | Pass `tokenizer_model`, the Hugging Face repo of the base model. For a model you uploaded, use the repo it came from. |
> | The job has no max context length | Pass `max_seq_len`. |
> | LoRA rank above 64 (a warning) | Training runs, but the adapter can't be hosted as a serverless LoRA. Deploy it on an on-demand deployment, or train with a rank of 64 or less to serve it on serverless. |
> | `lora_rank N exceeds the maximum supported LoRA rank of M` (from training) | Lower `lora_rank` to `M` or less. |

> [accordion] Which managed job settings carry over?
>
> | Managed job field | Recipe `Config` field | Notes |
> | - | - | - |
> | `base_model` | `base_model` | For a job that only set `warm_start_from`, the adapter's base model. |
> | `warm_start_from` | `warm_start_from_adapter` | Dedicated Training only. Needs `lora_rank > 0`. |
> | `dataset`, `evaluation_dataset` | `dataset`, `evaluation_dataset` | Your own copy: a local file or directory, or a `gs://` path with `dataset_loading_mode="stream"`. |
> | `eval_auto_carveout` | `eval_auto_carveout` | See "What happens to my evaluation settings?" |
> | `epochs` | `epochs` | Set it: the recipe defaults are 3 for SFT, 1 for DPO and ORPO. |
> | `learning_rate` | `learning_rate` | |
> | `lr_scheduler`, `learning_rate_warmup_steps` | `lr_scheduler` | `ConstantSchedule`, `LinearSchedule` or `CosineSchedule`, with `warmup_steps`, `min_lr_ratio` and `decay_ratio`. |
> | `batch_size_samples` | `batch_size` | Same units: rows per step for SFT, preference pairs per step for DPO and ORPO. |
> | `optimizer_weight_decay` | `weight_decay` | `0` in a managed job meant the default, `0.01`. |
> | `lora_rank`, `lora_alpha` | `lora_rank`, `lora_alpha` | Always set `lora_rank`: `0` means full-parameter on both. |
> | `max_context_length` | `max_seq_len` | Required on Serverless Training. |
> | `output_model` | `output_model_id` | A new ID. The managed job's output model already exists. |
> | `thinking_trace_history_mode` | `thinking_trace_history_mode` | `interleaved` or `preserved`. |
> | `renderer_hugging_face_repo_id` | `tokenizer_model` | Or the base model's Hugging Face repo. |
> | `sampler_checkpoint_save_interval_steps` | `sampler_save_interval` | |
> | `wandb_config` | `wandb=WandBConfig(...)` | Export `WANDB_API_KEY` to sync. |
> | `use_reservation`, `reservation_target` | `trainer.use_reservation`, `trainer.reservation_target` | Set `use_reservation` explicitly: the recipe default is `True`. |
> | DPO `beta`, `ref_cache_concurrency`, `ref_cache_batch_size` | Same names | |
> | ORPO `orpo.lambda` | `orpo_lambda` | ORPO runs on Dedicated Training only. |
>
> Managed jobs saved a resumable checkpoint every 20 steps, and LoRA SFT and DPO jobs also saved one every 30 minutes. To keep that, set `dcp_save_interval=20`, and `checkpoint_interval_minutes=30` for LoRA SFT and DPO.

> [accordion] Which managed job settings have no equivalent?
>
> * A token-based `batch_size` from older jobs. Recipes batch by rows; use `batch_size_samples` → `batch_size`.
> * `lora_target_modules`, `lora_dropout` and `tune_vision_encoder`.
> * Datasets in Amazon S3 or Azure Blob Storage. Copy the data to a local file or to Cloud Storage first.
> * Region, accelerator and training shape. You don't set these; the recipe picks a validated training shape.
