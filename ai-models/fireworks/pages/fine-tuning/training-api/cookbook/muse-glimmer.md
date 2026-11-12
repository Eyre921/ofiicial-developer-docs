---
title: "Cookbook: Muse Glimmer First Fine-Tune"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/muse-glimmer
path: fine-tuning/training-api/cookbook/muse-glimmer
---

Run a free first LoRA fine-tune of Muse Glimmer 30B on Serverless Training with a public Hugging Face example, then measure base versus tuned.

This guide runs a first fine-tune of Muse Glimmer 30B end to end with the
cookbook's [Muse Glimmer starter](https://github.com/fw-ai-external/cookbook/tree/main/training/examples/muse_glimmer).
Download a public Hugging Face example at runtime, or bring your own chat JSONL. **[Serverless Training](/fine-tuning/training-api/serverless)** runs the loop on the shared trainer pool, then samples the base and tuned adapters in the same session to compare them on held-out rows.

> [!NOTE]
>
> Muse Glimmer 30B SFT is free via UI and Serverless Training API until 11/30.
> No credit card required. See [Models](/fine-tuning/models). The starter applies
> the promotion to LoRA SFT jobs started before `2026-12-01T00:00:00-08:00` and
> refuses to launch after that unless you pass `--allow-paid`. RL, DPO,
> full-parameter training, deployments, and inference outside the training run
> are not covered.

| Setting | Value |
| - | - |
| Base model | `accounts/fireworks/models/muse-glimmer-30b` |
| Tokenizer | `meta-models/Muse-Glimmer-30B` |
| Renderer | `muse_glimmer` |
| Example datasets | [Prompt routing](https://huggingface.co/datasets/SupraLabs/Prompt-Routing-Dataset) (600 rows) and [receipt extraction](https://huggingface.co/datasets/naver-clova-ix/cord-v2) (300 rows), downloaded from Hugging Face at runtime |
| Default LoRA rank | 8 |

## Quickstart

### Step 1: Install and authenticate

You need Git, Python 3.11 or newer, and a Fireworks API key from the
[dashboard](https://app.fireworks.ai/settings/users/api-keys).

```bash theme={null}
git clone --depth 1 https://github.com/fw-ai-external/cookbook.git
cd cookbook/training
python3 -m venv .venv && source .venv/bin/activate   # check python3 --version is 3.11+
pip install -e .
export FIREWORKS_API_KEY="fw_..."
```

Run the remaining commands from `cookbook/training`. You can instead put
`FIREWORKS_API_KEY` in a gitignored `.env` file in that directory.

### Step 2: Check the plan

Run the cookbook downloader before planning. It converts the public Hugging Face data into local chat JSONL without creating a Fireworks dataset:

```bash theme={null}
python -m examples.sft.example_datasets --example prompt-router --upload prompt-router-v1
```

First download the example with the cookbook helper. This creates a local file, not a Fireworks dataset:

```bash theme={null}
python -m examples.sft.example_datasets --example prompt-router
```

`plan` is read-only. It confirms the account, the local dataset, whether the
promotion is active, and every training parameter before anything is created:

```bash theme={null}
python -m examples.sft.muse_glimmer_starter plan --surface serverless --file prompt-router.jsonl
```

Pass `--surface serverless` to see the Serverless Training plan, including
batch size, sequence length, LoRA alpha, and optimizer settings.

## Train and evaluate

This workflow trains on the downloaded example or any local chat JSONL file in the format shown in
[Your own data](#your-own-data).

### Step 3: Prepare the data

`prepare` runs locally and creates nothing on Fireworks. It validates every row,
refuses the file if any row is malformed and lists those rows, holds out 40 rows
(`--n-eval`), and renders one example with the Muse Glimmer tokenizer:

```bash theme={null}
RUN=tickets-$(date +%Y%m%d-%H%M%S)
python -m examples.sft.muse_glimmer_starter prepare --file prompt-router.jsonl --run-id $RUN
```

Read the rendered example before you launch: check the token count against
`--max-seq-len` (2,048 by default) and that the trained-token count covers only
the assistant's reply.

### Step 4: Train and evaluate

```bash theme={null}
python -m examples.sft.muse_glimmer_starter launch --surface serverless --file prompt-router.jsonl --run-id $RUN
```

The script:

1. Opens a Serverless Training session and samples the base adapter on the
   holdout.
2. Runs one epoch of cross-entropy training at batch size 16, logging loss and
   gradient norm every step. It refuses rows longer than `--max-seq-len`
   rather than truncating them.
3. Samples the tuned adapter on the same holdout with the same decoding
   settings.
4. Promotes the tuned checkpoint to a LoRA model,
   `accounts/<account>/models/muse-starter-sl-$RUN`, before the session closes.
   Pass `--no-promote` to keep it session-only.

It writes these files to `muse_starter_logs/$RUN/`:

| File | Contents |
| - | - |
| `train.jsonl`, `holdout.jsonl` | The prepared splits |
| `metrics.jsonl` | The base evaluation, loss and gradient norm per step, then the tuned evaluation |
| `predictions_base.jsonl`, `predictions_tuned.jsonl` | Per-row answers and scores |
| `summary.json` | Exact match for base and tuned (with per-key accuracy when the answers are JSON), an `unterminated` count (answers that did not stop cleanly), an exact paired McNemar test, and the evaluation sampling token counts |

> [!WARNING]
>
> The promotion covers training. In-session evaluation sampling is priced
> separately at the published per-token rates; the default run samples 80
> answers. `launch` prints a cost line with the sampled token counts.

## Your own data

The starter takes chat JSONL, one example per line:

```json theme={null}
{"messages": [
  {"role": "system", "content": "Classify the ticket. Reply with JSON."},
  {"role": "user", "content": "My invoice is wrong."},
  {"role": "assistant", "content": "{\"category\": \"billing\", \"priority\": \"medium\"}"}
]}
```

Use the `prepare` step to hold out rows so you can compare base and tuned on data the model has not seen. A few hundred clean rows are enough for a first signal.
the model has not seen (the Serverless `prepare` step does this split for you). A few hundred clean rows are enough for a first signal.

## Clean up

```bash theme={null}
python -m examples.sft.muse_glimmer_starter cleanup --run-id $RUN
```

Run it once for each run ID you created. `cleanup` deletes the promoted
Serverless Training model for that run ID if it exists. A Serverless Training
session closes when the script exits.

None of these steps leaves anything running. Serving a tuned model requires an
[on-demand deployment](/fine-tuning/deploying-loras), which bills per GPU-hour
while replicas run; trained LoRAs cannot be served on serverless inference.

## With a coding agent

The [Fireworks training skills](https://github.com/fw-ai-external/cookbook/tree/main/skills)
drive this starter for you. Install them, then ask *"Is there something free I can
run right now to see how training works?"*. The agent checks your account, shows
one plan with its cost, launches after you approve, monitors the run, and
reports the results.

## Related guides

* [Serverless Training](/fine-tuning/training-api/serverless): the shared trainer pool and its lifecycle
* [Cookbook: Supervised Fine-Tuning](/fine-tuning/training-api/cookbook/sft): the general `sft_loop` recipe
* [Deploying Trained Models](/fine-tuning/deploying-loras): live merge and multi-LoRA serving
* [Models](/fine-tuning/models): surfaces and methods each model supports
