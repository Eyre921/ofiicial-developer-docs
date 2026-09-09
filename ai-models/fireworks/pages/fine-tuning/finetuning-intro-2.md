---
title: "Training Overview"
source: https://docs.fireworks.ai/fine-tuning/finetuning-intro
path: fine-tuning/finetuning-intro
---

Training adapts a base model to your task by training it on your own data, so it learns your formats, tone, tools, and edge cases instead of relying on prompt instructions alone. Fireworks runs the training for you, without the burden of building and maintaining your own GPU or training infrastructure.

Training is worth it when you want:

* **Higher task quality** - beat a general-purpose model on your specific workload, and often match or exceed a larger closed model.
* **Lower latency and cost** - a smaller specialized model can replace a bigger one at a fraction of the per-token cost.
* **Consistent behavior** - bake in formats, style, and tool-use so you stop paying for long prompts and few-shot examples on every request.
* **Ownership and no infra** - you keep the resulting weights, and Fireworks handles the GPUs, scheduling, and checkpointing.

<Info>
  **Coming from OpenAI?** Fireworks uses the same **OpenAI-compatible chat completion format** for training data — the same `messages` array with `role`, `content`, `tool_calls`, and `weight` fields. You can use your existing SFT datasets with no conversion required. See the [SFT dataset format](/fine-tuning/fine-tuning-models#fine-tuning-a-model-using-sft) for the full schema and examples.
</Info>

## Choose a method

Pick a method based on the data or signal you have. All three run as standard jobs on [Managed Training](/fine-tuning/managed-finetuning-intro), or as custom loops you write yourself on the [Training API](/fine-tuning/training-api/introduction).

|                              | SFT                                                                                                                                                      | DPO                                                                                                         | RL                                                                                                                                                     |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Good for**                 | Classification, extraction, format and tone adherence, distillation                                                                                      | Steering the model toward a goal you cannot measure objectively, such as style, helpfulness, or safety      | Tasks where you have no verified outputs to learn from, but you can tell whether an outcome was good or bad. Pushing the model beyond state-of-the-art |
| **Data you supply**          | Verified input/output pairs, or successful trajectories                                                                                                  | Preference pairs, single-turn only: one prompt, a chosen and a rejected response                            | Prompts, plus an evaluator that can tell a good outcome from a bad one                                                                                 |
| **Dataset size**             | Hundreds of examples, or roughly 10M+ tokens                                                                                                             | Hundreds to thousands of pairs                                                                              | Dozens to thousands of prompts, sometimes more. Often fewer than 100 is enough                                                                         |
| **Consider alternatives if** | You have very few examples, or no high-quality verified outputs to learn from                                                                            | Outputs can be judged objectively, or you already have high-quality verified pairs. Both point to SFT or RL | You have no way at all to judge an outcome, including an LLM judge. Simpler methods are untried, or you want a quick training experiment               |
| **Guides**                   | [Text](/fine-tuning/fine-tuning-models) · [Vision](/fine-tuning/fine-tuning-models#vision-training) · [Cookbook](/fine-tuning/training-api/cookbook/sft) | [Managed DPO / ORPO](/fine-tuning/dpo-fine-tuning) · [Cookbook](/fine-tuning/training-api/cookbook/dpo)     | [Managed RFT](/fine-tuning/reinforcement-fine-tuning-models) · [Cookbook](/fine-tuning/training-api/cookbook/rl)                                       |

<Tip>
  **Verifiable** means you can reliably judge whether a model output is good (rules, unit tests, programmatic checks). RL fits reasoning and agentic tasks where full ground-truth labels are hard to write.
</Tip>

The Training API also supports custom methods (GRPO, distillation, and others) via the Python SDK. See [Cookbook recipes](/fine-tuning/training-api/cookbook/overview) and [Managed Training](/fine-tuning/managed-finetuning-intro) for model support and pricing.

## Choose a surface

Pick a **surface** (managed or Training API, serverless or dedicated). The surface decides how much of the model you update and which **interfaces** are available to you.

Answer the question below and the flow takes you to your surface, which links to its guide. Click any answered question to change it, or show every path at once.

<TrainingDecisionFlow />

Compare the last branch in detail on [serverless versus dedicated](/fine-tuning/training-api/introduction#infrastructure), and check per-model support on [Models](/fine-tuning/models).

### Managed Training vs Training API

Fireworks offers two ways to train: **Managed Training** (Fireworks runs the loop) and the **Training API** (you write the loop in Python).

| Choose Managed Training when                                      | Choose the Training API when                                                               |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| You need a standard SFT, DPO, ORPO, or RFT job                    | You need a custom loss, reward, rollout, trajectory, or optimizer-step loop                |
| You want Fireworks to own scheduling, training, and checkpointing | You want to fork or write Python training logic                                            |
| A supported model and managed configuration cover the task        | You need inference in the loop, distillation, per-step diagnostics, or research algorithms |

<CardGroup>
  <Card title="Managed Training" icon="wand-magic-sparkles" href="/fine-tuning/managed-finetuning-intro">
    Standard jobs with a platform-managed loop.
  </Card>

  <Card title="Training API" icon="code" href="/fine-tuning/training-api/introduction">
    Programmable loops built from cookbook recipes or the SDK.
  </Card>
</CardGroup>

### Serverless vs Dedicated infrastructure

Infrastructure applies to the **Training API** only. Managed Training uses platform-managed compute.

| Choose Serverless Training when                                                   | Choose Dedicated Training when                                                     |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Supported LoRA SFT or RL covers the workload                                      | You need full-parameter, DPO, ORPO, distillation, or broader model support         |
| You want shared pooled compute with no trainer or sampler deployment provisioning | You need explicit trainer, deployment, checkpoint, reconnect, or promotion control |
| Per-token billing fits a small or bursty experiment                               | A sustained, highly utilized time-based run fits the workload                      |
| In-session sampling is sufficient                                                 | You need provisioned rollout or evaluation deployments                             |

<CardGroup>
  <Card title="Serverless Training" icon="bolt" href="/fine-tuning/training-api/serverless">
    Shared pooled trainer, no provisioning, per-token billing.
  </Card>

  <Card title="Dedicated Training" icon="server" href="/fine-tuning/training-api/dedicated">
    Provisioned trainer and deployment resources with explicit lifecycle control.
  </Card>
</CardGroup>

See the detailed [serverless versus dedicated comparison](/fine-tuning/training-api/introduction#infrastructure).

## Choose how to interact

* **Skill** — the only interface that drives both surfaces. Your coding agent configures, runs, and troubleshoots training through the [Fireworks training skill](/fine-tuning/agent/use-with-coding-agents).
* **Fireworks UI, `firectl`, or the REST API** — managed jobs only. Guided creation and monitoring in the UI, reproducible job and resource automation from the CLI or API.
* **Python SDK** — Training API loops only, on serverless or dedicated. Start from a [cookbook recipe](/fine-tuning/training-api/cookbook/overview).

<Note>
  **CLI or API vs Python SDK:** `firectl` and the REST API manage **managed** jobs and platform resources. The **Python SDK** runs **Training API** loops you author yourself (loss, rollouts, optimizer steps).
</Note>

### GPU quota prerequisite

Managed jobs and dedicated Training API runs need training GPU quota, granted automatically by [spending tier](/guides/quotas_usage/account-quotas#training-gpu-quota). [Serverless Training](/fine-tuning/training-api/serverless) uses a shared pool with its own model, concurrency, and rate limits instead of dedicated training GPU quota.

<Accordion title="Training GPU quota by spending tier">
  | Tier              | How to reach it                          | B200 / B300 (Blackwell) | H200 | H100 / A100 |
  | ----------------- | ---------------------------------------- | :---------------------: | :--: | :---------: |
  | No payment method | —                                        |            0            |   0  |      0      |
  | Tier 1            | Valid payment method and billing profile |            0            |  16  |      8      |
  | Tier 2            | Spend or add \$50 in credits             |            16           |  16  |      16     |
  | Tier 3            | Spend or add \$500 in credits            |            24           |  24  |      24     |
  | Tier 4            | Spend or add \$5,000 in credits          |            32           |  32  |      32     |

  Check your quota with the Fireworks CLI (`firectl quota list`). A job rejected with HTTP 429 `quota_exceeded` (sometimes a `403` on the job poll) is a tier issue, not a dataset/config problem.
</Accordion>

<Note>
  Need more training quota than your tier allows? [Reach out for enterprise support](https://fireworks.ai/contact-training) and we'll help size the right allocation for your workload.
</Note>

## Models

Model availability is decided per model and per surface — managed jobs by method (SFT, DPO, RFT), Training API jobs by parameter mode (LoRA or full-parameter). Check the live catalog before you launch.

<Card title="Models" icon="microchip" href="/fine-tuning/models">
  Browse the base model catalog with per-model surface, method, and training-shape support.
</Card>

## Training security

Across every training surface, one principle holds: **your training data is never used to train Fireworks-owned or shared models**. Inference follows [Zero Data Retention](/guides/security_compliance/data_handling) by default. This section summarizes the training surfaces; step-by-step BYOB IAM setup, CMEK KMS setup, and secure RFT are in [Secure Training](/guides/security_compliance/secure_training) and [CMEK](/guides/security_compliance/secure_training/cmek).

### Choose a surface by data-privacy needs

| Surface              | Where your training data lives                                  | What Fireworks retains       | Your deletion controls                                            |
| -------------------- | --------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------- |
| **Managed Training** | Fireworks-managed storage (GCS); reference link in our database | Dataset, checkpoints, traces | Delete dataset after job; request checkpoint/trace deletion       |
| **Managed + BYOB**   | Your cloud bucket; read in-place during training only           | Checkpoints and traces only  | Revoke bucket access after job; request checkpoint/trace deletion |
| **Training API**     | No dataset file on Fireworks — transient tokenized batches only | Checkpoints and traces only  | Request checkpoint/trace deletion                                 |

Checkpoints and traces are retained \~30 days by default (deletable on request). Strictest governance: [BYOB](#dataset-storage-byob) (dataset never copied to Fireworks) or the [Training API](/fine-tuning/training-api/introduction) (no stored dataset file).

### Bring your own bucket (BYOB)

Register an external URL so Fireworks reads your dataset during the job without persisting a copy, then revoke access after the job:

```bash theme={null}
firectl dataset create my-dataset --external-url gs://your-bucket/path/train.jsonl
```

Supported: GCS, AWS S3, and Azure Blob, with least-privilege IAM to Fireworks service accounts provided at onboarding. For AWS S3, lock the IAM trust policy with both `accounts.google.com:sub` and `accounts.google.com:oaud` (your Fireworks account ID) so tokens for other accounts are rejected. Full IAM trust policies, OIDC audience, and rotation are in [Secure Training](/guides/security_compliance/secure_training/byob).

### Customer-managed encryption keys (CMEK)

CMEK encrypts datasets and checkpoints on Fireworks-managed storage with **your** cloud KMS key — revoke the key and Fireworks cannot decrypt. Supported on AWS KMS, Google Cloud KMS, and Azure Key Vault. It does not cover in-memory training compute or inference request/response. Setup, IAM, and rotation detail: [CMEK](/guides/security_compliance/secure_training/cmek) · [Data Security Overview](/guides/security_compliance/data_security).

### Secure RFT and customer controls

For RFT under strict governance, combine a [BYOB](#dataset-storage-byob) dataset with evaluators and rollout servers kept in your own environment (see [Remote Environment Setup](/fine-tuning/connect-environments)). To delete checkpoints, traces, or rollout data, contact your Fireworks account team; datasets are deletable from the console or API after a job completes.

## Before launch

Verify current model support, shapes, access status, pricing, limits, and quota in the linked live pages. A coding agent asks for confirmation before upload, registration, paid inference, job creation, promotion, deployment, or another mutation. Material changes require approval again; promotion and deployment are confirmed separately.
