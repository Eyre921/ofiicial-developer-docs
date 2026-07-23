---
title: "Choose a Training Path"
source: https://docs.fireworks.ai/fine-tuning/choose-training-path
path: fine-tuning/choose-training-path
---

Choose the Fireworks workflow, infrastructure, and interaction surface for your training task.

Make three choices independently:

1. **Workflow:** Managed Fine-Tuning or Training API.
2. **Infrastructure:** Serverless or dedicated, only when you choose Training API.
3. **Interface:** Your agent, the Fireworks UI, CLI or API, or Python SDK.

## Step 1: Choose the workflow

| Choose Managed Fine-Tuning when                                      | Choose the Training API when                                                               |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| You need a standard SFT, DPO, ORPO, or RFT job                       | You need a custom loss, reward, rollout, trajectory, or optimizer-step loop                |
| You want Fireworks to own the training loop and checkpoint lifecycle | You want to fork or write Python training logic                                            |
| A supported model and managed configuration cover the task           | You need inference in the loop, distillation, per-step diagnostics, or research algorithms |
| You want to launch through the UI, CLI or API, or your agent         | You want to launch through the Python SDK or your agent                                    |

<CardGroup>
  <Card title="Managed Fine-Tuning" icon="wand-magic-sparkles" href="/fine-tuning/managed-finetuning-intro">
    Standard jobs with a platform-managed loop.
  </Card>

  <Card title="Training API" icon="code" href="/fine-tuning/training-api/introduction">
    Programmable loops built from cookbook recipes or the SDK.
  </Card>
</CardGroup>

## Step 2: If Training API, choose infrastructure

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

See the detailed [serverless versus dedicated comparison](/fine-tuning/training-api/choose-infrastructure).

## Step 3: Choose how to interact

The interface does not determine the workflow or infrastructure:

| Interface        | What it does                                                                   |
| ---------------- | ------------------------------------------------------------------------------ |
| **Your agent**   | Uses the Fireworks training skill to configure, run, and troubleshoot training |
| **Fireworks UI** | Guided creation and monitoring for managed jobs                                |
| **CLI or API**   | Reproducible managed job and resource automation                               |
| **Python SDK**   | Custom Training API loops on serverless or dedicated infrastructure            |

The Fireworks CLI is called `firectl`. [Cookbook recipes](/fine-tuning/training-api/cookbook/overview) are recommended starting points for the Python SDK and can also be used by your agent.

[Install the Fireworks training skill](/fine-tuning/agent/use-with-coding-agents) to use your agent.

## Examples

### Standard SFT from labeled JSONL

* **Workflow:** Managed Fine-Tuning
* **Infrastructure:** Managed by the platform; no Training API infrastructure choice
* **Interface:** Your agent, UI, CLI, or API

### First custom GRPO experiment

* **Workflow:** Training API
* **Infrastructure:** Serverless when the model and LoRA workload are supported
* **Interface:** Python SDK with a Cookbook recipe, or your agent

### Sustained full-parameter RL

* **Workflow:** Training API
* **Infrastructure:** Dedicated
* **Interface:** Python SDK with a Cookbook recipe, optionally orchestrated by your agent

## Before launch

Verify current model support, shapes, access status, pricing, limits, and quota in the linked live pages. A coding agent asks for confirmation before upload, registration, paid inference, job creation, promotion, deployment, or another mutation. Material changes require approval again; promotion and deployment are confirmed separately.
