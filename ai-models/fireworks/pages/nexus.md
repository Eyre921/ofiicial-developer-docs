---
title: "Overview"
source: https://docs.fireworks.ai/nexus
path: nexus
---

Use Fireworks open models and Nexus Auto in Claude Code, ChatGPT, and your other AI tools, with Provider Keys and Spend Limits for admins.

> **[Connect your tool in a few minutes](/nexus/quickstart)**
>
> Pick Claude Code, ChatGPT, Cursor IDE, or another harness, then follow its setup.

## Who Nexus is for

> **Developers**
>
> Keep Claude Code, ChatGPT, Codex, Cursor IDE, or VS Code. Run one command, and Fireworks open models appear in your model picker next to the models you use today. Run one more command to get your original settings back.

> **Team admins**
>
> Connect your Anthropic, OpenAI, or Amazon Bedrock account once for the whole team. Cap each person's spend on Fireworks models, and see usage by model and by user.

## What you get

> **[Nexus CLI](/nexus/cli)**
>
> One command connects a coding harness to Fireworks. Another restores your settings when you're done.

> **[Nexus Auto](/nexus/auto)**
>
> One model ID: `auto`. Easy turns run on open models. Harder turns go to an Anthropic or OpenAI model on your own account.

> **[Open models](/nexus/open-models)**
>
> GLM, Kimi, DeepSeek, and other open models on Fireworks serverless, billed per token.

> **[Harness support](/nexus/harnesses)**
>
> Setup steps and answers for Claude Code, ChatGPT, Codex, Claude Desktop, Cursor IDE, VS Code, OpenCode, Pi, Copilot, and DeepSeek Harness.

> **[Model providers](/nexus/provider-keys)**
>
> Store Anthropic, OpenAI, or Amazon Bedrock credentials once, so developers only need a Fireworks key.

> **[Spend limits](/nexus/usage-limits)**
>
> Set an account default, group limits, and per-user caps on Fireworks serverless spend.

## How Nexus fits together

Your tool connects through Nexus CLI, an SDK, or an LLM gateway. Each request then goes to the Fireworks model you chose, or to Nexus Auto, which picks a model for each turn.

```mermaid theme={null}
flowchart LR
  H[Coding harnesses] --> CLI[Nexus CLI]
  A[Apps and agents] --> API[Fireworks API]
  G[LLM gateways] --> API
  CLI --> API
  API --> OM[Open models]
  API --> NA[Nexus Auto]
  NA --> OM
  NA --> CM[Anthropic and OpenAI models<br/>on your provider account]
```

Building your own agent or running a gateway? See [APIs and SDKs](/nexus/apis-and-sdks) or [LLM Gateways](/nexus/llm-gateways).
