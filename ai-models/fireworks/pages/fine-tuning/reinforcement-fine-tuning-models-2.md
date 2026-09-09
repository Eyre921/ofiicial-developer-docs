---
title: "Reinforcement Fine-Tuning"
source: https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models
path: fine-tuning/reinforcement-fine-tuning-models
---

Train models using reinforcement learning in minutes

Fireworks RFT helps you train frontier models like DeepSeek V3 and Kimi K2 to **outperform closed models for your product use case, using reinforcement learning.** Fireworks RFT is powerful and easy to use for developers and enterprises:

* **No infrastructure:** Train frontier models without managing GPUs or RL infra
* **Production-ready:** Built-in tracing, monitoring, security & one-click deploy
* **Fast iteration:** From evaluator setup to deployed model in hours, not weeks

<Tip>
  See how [Genspark](https://fireworks.ai/blog/genspark) and [Vercel](https://fireworks.ai/blog/vercel) used Fireworks RFT to train open models for agentic use cases, outperforming leading closed models.
</Tip>

## Quickstart: pick your training approach

<CardGroup>
  <Card title="Single-Turn Training" icon="laptop-code" href="/fine-tuning/quickstart-math">
    **15 minutes** — test locally with a simple evaluator and small model.
  </Card>

  <Card title="Remote Agents" icon="server" href="/fine-tuning/quickstart-svg-agent">
    **1–2 hours** — multi-turn rollouts in your environment with HTTP tracing.
  </Card>

  <Card title="Training security (BYOB)" icon="shield-check" href="/guides/security_compliance/secure_training">
    **2–4 hours** — datasets stay in your GCS/S3 bucket.
  </Card>
</CardGroup>

## How RFT works

In supervised fine-tuning you provide labeled examples of good outputs. In RFT you provide **prompts** and an **evaluator** (reward function) that scores model outputs from 0 to 1. Training iteratively improves outputs that maximize that score.

<Steps>
  <Step title="Design an evaluator">
    Define how to score outputs (rules, tests, LLM-as-judge, or hybrid).
  </Step>

  <Step title="Prepare a dataset">
    JSONL with prompts (`messages` array). Ground-truth completions are optional.
  </Step>

  <Step title="Connect your agent (optional)">
    Local evaluators for simple tasks, or [remote environments](/fine-tuning/connect-environments) for agents.
  </Step>

  <Step title="Launch training">
    Fireworks UI, `firectl rftj`, or [eval-protocol CLI](https://evalprotocol.io/introduction).
  </Step>

  <Step title="Deploy">
    Promote the checkpoint and deploy LoRA on [on-demand hardware](/fine-tuning/deploying-loras).
  </Step>
</Steps>

RFT fits when the task is **verifiable** (you can judge output quality), you lack golden completions, or the task needs multi-step reasoning.

## Launch and operate

Use the docs for path choice and quickstarts. Use the **[Fireworks training skill](https://github.com/fw-ai/cookbook/tree/main/skills/fireworks-training)** for launch flags, validation, monitoring, and troubleshooting.

| Topic                                                | Skill reference                                                                                                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prerequisites, validation, job states, CLI/UI launch | [managed-rft-operations](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/managed-rft-operations.md)                 |
| Evaluator design and preference data                 | [preference-data-and-evaluators](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/preference-data-and-evaluators.md) |
| Remote agent tracing                                 | [rft-agent-tracing](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rft-agent-tracing.md)                           |
| Parameter tuning and method choice                   | [choose-method](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/choose-method.md)                                   |
| Failures and stuck jobs                              | [error-reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/error-reference.md)                               |
| Deploy and prove serving                             | [deploy-and-troubleshoot](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/deploy-and-troubleshoot.md)               |

### Prerequisites

Confirm account access and quota, an RFT-compatible base model, valid prompt JSONL, and a reviewed evaluator that produces non-flat scores on a small probe.

### Evaluators

Evaluators turn a rollout into a reward. Test full-credit, partial-credit, zero, malformed-output, and edge cases locally before registration. Keep evaluator and preference-data guidance in the [evaluator skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/preference-data-and-evaluators.md).

### Parameter tuning

Resolve the current defaults from `firectl rftj create --help` and the live RFT parameter reference. Start with a small run, change one optimization or rollout variable at a time, and compare reward and held-out quality.

#### Weighted training

Use per-example or per-token weighting only when the selected managed contract supports it. Inspect the rendered samples and effective loss mask before launch.

### Launch from the CLI

Use `firectl rftj create` for a reproducible managed job. Prepare the full base-model, dataset, evaluator, and output-model resource names, run the documented preflight, and confirm the resolved plan before creation.

### Launch from the dashboard

Use the dashboard for a guided first run: choose the model, dataset, evaluator, rollout settings, and optional W\&B project, then review the summary before launch.

### Warm start

Warm-start from a compatible promoted LoRA when continuing SFT into RFT. Do not also supply a conflicting base-model field; verify the current CLI contract before creation.

### Evaluator secrets

Store credentials in the Fireworks secret-management surface and reference them by environment-variable name. Never embed secret values in evaluator code, datasets, or run reports.

### Cost planning

Estimate rollout inference, training runtime or tokens, candidate count, response length, and any deployment uptime. Use the live pricing page and [Price vs Tinker](/fine-tuning/multi-turn-cost-comparison); do not assume a free tier.

### Monitor training

Track state plus actual progress: optimizer steps, rollout throughput, reward distribution, validation results, logs, and W\&B metrics when enabled. Inspect representative rollouts for reward hacking and stop when quality regresses or the evaluator saturates.

<Note>
  Using Cursor, Claude Code, or Codex? [Install Agent Skills](/fine-tuning/agent/use-with-coding-agents) to drive managed RFT with the `fireworks-training` skill.
</Note>

Parameter field reference: [RFT parameters](/fine-tuning/rft-parameters-reference) (API tab).

## Related

<CardGroup>
  <Card title="Remote Environment Setup" icon="server" href="/fine-tuning/connect-environments">
    HTTP `/init` contract for remote rollouts
  </Card>

  <Card title="Price vs Tinker" icon="scale-balanced" href="/fine-tuning/multi-turn-cost-comparison">
    Multi-turn RL cost comparison
  </Card>

  <Card title="Training API RL" icon="code" href="/fine-tuning/training-api/cookbook/rl">
    Custom RL loops on dedicated or serverless infrastructure
  </Card>

  <Card title="Models" icon="table" href="/fine-tuning/models">
    Which models support managed RFT
  </Card>
</CardGroup>
