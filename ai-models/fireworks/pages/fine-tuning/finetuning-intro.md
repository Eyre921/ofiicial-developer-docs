---
title: "Training overview"
source: https://docs.fireworks.ai/fine-tuning/finetuning-intro
path: fine-tuning/finetuning-intro
---

Train an open model on your own data with Fireworks, serverless or on dedicated GPUs. Start with agent skills.

Training adapts an open model to your task with your own data. A trained model can beat a larger general-purpose model on quality while costing less and responding faster. Read [when to train your own model](https://fireworks.ai/blog/specialized-intelligence-train-your-own-model).

**Muse Glimmer 30B SFT is free to train until November 30, 2026.**\
[Start here](#quickstart)

## Quickstart

Train your first model with a coding agent such as Cursor, Claude Code, or Codex. You need a [Fireworks account](https://app.fireworks.ai/signup), an [API key](https://app.fireworks.ai/settings/users/api-keys), and Python 3.11 or newer.

**Step 1: Install the training skills.** Paste this into your agent:

```text wrap theme={null}
Set up Fireworks training for me. Fetch https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents.md and follow it.
```

**Step 2: Run your first job.** Ask the agent:

```text wrap theme={null}
Fine-tune Muse Glimmer 30B with Serverless Training on the SupraLabs/Prompt-Routing-Dataset example. Download and convert it at runtime with the cookbook helper `python -m examples.sft.example_datasets --example prompt-router`.
```

The agent shows you the parameters and cost, then waits for your approval before it starts anything.

**That's it! Now try your own use case.** In the same agent, ask:

```text wrap theme={null}
Train a model to [describe your task] using [your data file].
```

The skills suggest a method, data format, and evaluation, then plan the job for your approval.

## Ways to train

From self-serve to building with our team:

> [card] [Serverless Training](/fine-tuning/training-api/serverless)
>
> Write your own training loop on a shared trainer pool. Nothing to provision, billed per token.

> [card] [Dedicated Training](/fine-tuning/training-api/dedicated)
>
> Your own loop on GPUs reserved for your run, with full-parameter training and more models. Billed per GPU hour.

> [card] [Fireworks Lab](https://fireworks.ai/contact-training)
>
> Our researchers and engineers build the model with your team, from co-design to a custom build.

Not sure? Start with Serverless Training if your model is on the [serverless list](/fine-tuning/training-api/serverless#supported-models). Choose Dedicated Training for other models or full-parameter training ([compare serverless and dedicated](/fine-tuning/training-api/introduction#infrastructure)). Choose Fireworks Lab when you want our team to help design and build the model.

Used Managed Training? See [Migrate from Managed Training](/fine-tuning/migrate-from-managed-training) to move your jobs to the Training API.

## Choose a method

| | Supervised Fine-Tuning (SFT) | Preference Optimization (DPO) | Reinforcement Learning (RL) |
| - | - | - | - |
| **Use it for** | Classification, extraction, format and tone, distillation | Style, helpfulness, or safety, where there is no single right answer | Reasoning and agent tasks where you can score an outcome but can't write the answer |
| **You supply** | Hundreds of good input/output examples | Hundreds to thousands of chosen and rejected responses | Prompts, often fewer than 100, and a way to score outputs |
| **Runs on** | Serverless or Dedicated Training | Serverless or Dedicated Training | Serverless or Dedicated Training |
| **Guides** | [Cookbook](/fine-tuning/training-api/cookbook/sft) · [Vision](/fine-tuning/training-api/cookbook/sft#vision-datasets) | [Cookbook](/fine-tuning/training-api/cookbook/dpo) | [Agentic RL](/fine-tuning/training-api/cookbook/agentic-rl) · [Cookbook](/fine-tuning/training-api/cookbook/rl) |

The Training API also runs custom methods such as GRPO and distillation. See [Cookbook recipes](/fine-tuning/training-api/cookbook/overview).

## Other ways to run jobs

The agent is the fastest path, and you can also work directly:

* **Python SDK:** run a [cookbook recipe](/fine-tuning/training-api/cookbook/overview) or write your own loop.
* **`firectl` or the REST API:** manage and deploy the models your runs produce.

## Next steps

* [Evaluating Trained Models](/fine-tuning/evaluating-fine-tuned-models) and [Deploying Trained Models](/fine-tuning/deploying-loras) — test your trained model, then serve it
* [Models](/fine-tuning/models) — which models each method and surface supports
* [Training cost estimator](/fine-tuning/cost-estimator) — estimate a job before you launch it
* [Training GPU quota](/guides/quotas_usage/account-quotas#training-gpu-quota) — what your account gets and how to raise it
* [Secure Training](/guides/security_compliance/secure_training) — where your data lives, bring your own bucket, and customer-managed keys
