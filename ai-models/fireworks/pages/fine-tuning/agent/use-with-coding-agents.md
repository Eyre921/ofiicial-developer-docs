---
title: "Train from Your Coding Agent"
source: https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents
path: fine-tuning/agent/use-with-coding-agents
---

Install one Fireworks training skill and run managed or Training API workflows from Claude Code, Cursor, Codex, or another compatible agent.

The Fireworks training skill teaches your coding agent to run training end to end: choose managed or Training API, choose serverless or dedicated infrastructure when needed, prepare and validate data, launch and monitor the run, evaluate, deploy, and troubleshoot.

## Install

### Claude Code

Install the auto-updating cookbook plugin:

```bash theme={null}
claude plugin marketplace add fw-ai/cookbook
claude plugin install fireworks-training@fw-ai-cookbook
```

### Cursor

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training -a cursor -y
```

### Codex

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training -a codex -y
```

### Other compatible agents

Install to every detected Agent Skills-compatible harness:

```bash theme={null}
npx --yes skills add fw-ai/cookbook -g \
  -s fireworks-training -a '*' -y
```

<Note>
  Skills installed with `npx skills` do not update automatically. Refresh them with `npx --yes skills update -g -y`.
</Note>

## Prerequisites

* [`firectl`](/tools-sdks/firectl/firectl) installed. Authenticate with either `firectl signin` or `FIREWORKS_API_KEY`.
* Export `FIREWORKS_API_KEY` for Training API Python workflows.

## What it does

Ask in plain language, for example *"Fine-tune qwen3-4b on my `train.jsonl` and deploy it."* The skill uses current Fireworks docs and cookbook recipes to choose the right path, validate inputs, run and monitor training, evaluate the result, deploy it, and troubleshoot failures.

Before any upload, registration, paid inference, job creation, promotion, or deployment, it shows the resolved parameters, defaults, cost ceiling, evaluation, and teardown for approval. Material changes require approval again; promotion and deployment each have separate confirmation.

<Note>
  `firectl` may block mutating commands inside any AI-agent environment. When that happens, the skill gives you the exact command to run manually in your terminal, then resumes read-only monitoring and reporting. It does not bypass the guard.
</Note>

Use [managed fine-tuning](/fine-tuning/managed-finetuning-intro) for standard jobs, or the [Training API](/fine-tuning/training-api/introduction) for custom loops on [serverless or dedicated infrastructure](/fine-tuning/training-api/choose-infrastructure).

## See also

<CardGroup>
  <Card title="Managed Fine-Tuning" icon="sliders" href="/fine-tuning/managed-finetuning-intro">
    Drive the same training infra directly when you know your config.
  </Card>

  <Card title="Training API" icon="code" href="/fine-tuning/training-api/introduction">
    Write your own Python training loop on Fireworks GPUs.
  </Card>

  <Card title="Choose infrastructure" icon="server" href="/fine-tuning/training-api/choose-infrastructure">
    Compare serverless and dedicated training.
  </Card>

  <Card title="firectl" icon="terminal" href="/tools-sdks/firectl/firectl">
    The CLI the skill drives.
  </Card>

  <Card title="Cookbook" icon="book" href="/fine-tuning/training-api/cookbook/overview">
    Ready-to-run recipes, including the inline-reward RL loop.
  </Card>
</CardGroup>
