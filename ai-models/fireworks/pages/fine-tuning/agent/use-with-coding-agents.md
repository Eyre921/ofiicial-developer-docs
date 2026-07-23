---
title: "Agent Skills"
source: https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents
path: fine-tuning/agent/use-with-coding-agents
---

Install the Fireworks training skill for your coding agent.

The `fireworks-training` skill helps coding agents configure, run, and troubleshoot training jobs using current Fireworks best practices.

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

* [Fireworks CLI (`firectl`)](/tools-sdks/firectl/firectl) installed. Authenticate with either `firectl signin` or `FIREWORKS_API_KEY`.
* Export `FIREWORKS_API_KEY` for Training API Python workflows.

## What it does

Ask in plain language, for example *"Fine-tune qwen3-4b on my `train.jsonl` and deploy it."* The skill configures the job, validates inputs, runs it, and helps troubleshoot failures.

Before creating cost or resources, it shows the resolved parameters and estimated cost for confirmation.

<Note>
  The Fireworks CLI (`firectl`) may block mutating commands inside an AI-agent environment. When that happens, the skill gives you the exact command to run manually, then resumes monitoring and reporting.
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

  <Card title="CLI reference" icon="terminal" href="/tools-sdks/firectl/firectl">
    Automate managed training with `firectl`.
  </Card>

  <Card title="API reference" icon="brackets-curly" href="/api-reference/introduction">
    Automate managed training through REST APIs.
  </Card>

  <Card title="Cookbook" icon="book" href="/fine-tuning/training-api/cookbook/overview">
    Ready-to-run recipes, including the inline-reward RL loop.
  </Card>
</CardGroup>
