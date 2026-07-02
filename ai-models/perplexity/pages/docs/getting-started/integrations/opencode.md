---
title: "Perplexity with OpenCode"
source: https://docs.perplexity.ai/docs/getting-started/integrations/opencode
path: docs/getting-started/integrations/opencode
---

Use the Perplexity Agent API inside the OpenCode AI coding agent — one endpoint, every frontier model, with built-in web search and tool orchestration.

## Overview

[OpenCode](https://opencode.ai) is an open-source AI coding agent for your terminal, IDE, or desktop. The Perplexity **Agent API** is OpenAI-compatible and exposes frontier models from OpenAI, Anthropic, Google, xAI, and Perplexity through a single endpoint, with optional `web_search` and `fetch_url` tools and Perplexity's research presets.

Wiring OpenCode to the Agent API means you can swap any frontier model into your coding agent or research subagent — without juggling separate provider accounts.

<Info>
  **OpenCode** ships with multi-agent orchestration: you can configure a `primary` agent for coding and `subagent` agents for specialized tasks. Learn more at [opencode.ai](https://opencode.ai).
</Info>

## Setup

The Agent API is OpenAI-compatible, so you configure it in OpenCode as a custom provider using `@ai-sdk/openai-compatible`.

<Steps>
  <Step title="Install OpenCode">
    Follow the [OpenCode install guide](https://opencode.ai/docs) for your platform (macOS, Linux, Windows).
  </Step>

  <Step title="Get a Perplexity API key">
    <Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
      Generate your Perplexity API key from the API portal.
    </Card>

    Export it in your shell:

    ```bash theme={null}
    export PERPLEXITY_API_KEY="pplx-..."
    ```
  </Step>

  <Step title="Configure OpenCode">
    Add the Perplexity Agent API as a provider in your `opencode.json` (or `~/.config/opencode/config.json`). See the configuration below.
  </Step>

  <Step title="Verify">
    Run `/models` to confirm the Perplexity Agent models appear in the selector.
  </Step>
</Steps>

## Provider Configuration

OpenCode supports OpenAI-compatible providers out of the box. Point it at `https://api.perplexity.ai/v1` and declare the models you want available in the model picker:

```json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "perplexity-agent": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Perplexity Agent API",
      "options": {
        "baseURL": "https://api.perplexity.ai/v1",
        "apiKey": "{env:PERPLEXITY_API_KEY}",
        "headers": {
          "X-Pplx-Integration": "opencode/1.0"
        }
      },
      "models": {
        "openai/gpt-5.2": { "name": "GPT-5.2" },
        "openai/gpt-5.1": { "name": "GPT-5.1" },
        "openai/gpt-5-mini": { "name": "GPT-5 Mini" },
        "anthropic/claude-opus-4-7": { "name": "Claude Opus 4.7" },
        "anthropic/claude-sonnet-4-6": { "name": "Claude Sonnet 4.6" },
        "anthropic/claude-haiku-4-5": { "name": "Claude Haiku 4.5" },
        "google/gemini-3.1-pro-preview": { "name": "Gemini 3.1 Pro" },
        "google/gemini-3-flash-preview": { "name": "Gemini 3 Flash" },
        "xai/grok-4.20-non-reasoning": { "name": "Grok 4.20" }
      }
    }
  }
}
```

That's it — one API key, one endpoint, every frontier model.

## Available Models

The Agent API routes to models from multiple providers. The full canonical list lives on the [models page](/docs/agent-api/models); the most useful identifiers for coding work:

| Model ID                        | Best for                                     |
| ------------------------------- | -------------------------------------------- |
| `openai/gpt-5.2`                | Deep reasoning, long-horizon coding tasks    |
| `openai/gpt-5.1`                | General-purpose coding agent                 |
| `openai/gpt-5-mini`             | Fast, cheap coding completions               |
| `anthropic/claude-opus-4-7`     | Highest-quality code review and architecture |
| `anthropic/claude-sonnet-4-6`   | Balanced coding + tool use                   |
| `google/gemini-3.1-pro-preview` | Long-context refactors                       |
| `xai/grok-4.20-non-reasoning`   | Low-latency edits                            |

You can also use Perplexity's [research presets](/docs/agent-api/presets) (`fast-search`, `pro-search`, `deep-research`, `advanced-deep-research`) as model IDs to get pre-tuned web-search behavior.

## Use as a Primary Coding Model

Set any Agent API model as your default in `opencode.json`:

```json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "model": "perplexity-agent/anthropic/claude-opus-4-7"
}
```

OpenCode addresses each model as `<providerId>/<modelId>`, so the full identifier is `perplexity-agent/anthropic/claude-opus-4-7`.

## Multi-Agent Setup: Research Subagent with Web Tools

The Agent API's `web_search` and `fetch_url` tools make it a strong fit for a dedicated research subagent. The coder owns the filesystem; the researcher owns the open web.

```json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "model": "perplexity-agent/anthropic/claude-opus-4-7",
  "agent": {
    "coder": {
      "description": "Primary coding agent",
      "mode": "primary",
      "model": "perplexity-agent/anthropic/claude-opus-4-7",
      "temperature": 0.2,
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    },
    "researcher": {
      "description": "Research agent using Perplexity's deep-research preset with live web access",
      "mode": "subagent",
      "model": "perplexity-agent/deep-research",
      "temperature": 0.4,
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    }
  }
}
```

Because the researcher uses Perplexity's `deep-research` preset, every web lookup includes citations, multi-step retrieval, and the `fetch_url` tool for reading specific docs pages. The coder calls into it whenever it needs current documentation or API references.

Verify the wiring:

```
/agents   # Should show coder and researcher
/models   # Should include Perplexity Agent models
```

## Why the Agent API

The Agent API is purpose-built for agent loops:

* **One key, every model** — switch between OpenAI, Anthropic, Google, and xAI without managing separate accounts.
* **OpenAI-compatible** — drop-in for any OpenCode provider slot that speaks `/v1/responses` or `/v1/chat/completions`.
* **Built-in web tools** — opt into `web_search` and `fetch_url` per request, no MCP setup required.
* **Research presets** — `pro-search`, `deep-research`, `advanced-deep-research` give your subagents tuned retrieval behavior out of the box.

## Links & Resources

<CardGroup>
  <Card title="Agent API Quickstart" icon="bolt" href="/docs/agent-api/quickstart">
    Send your first Agent API request.
  </Card>

  <Card title="Agent API Models" icon="sparkles" href="/docs/agent-api/models">
    Full model catalog with pricing.
  </Card>

  <Card title="Research Presets" icon="layer-group" href="/docs/agent-api/presets">
    Pre-tuned model + tool configurations.
  </Card>

  <Card title="OpenAI Compatibility" icon="plug" href="/docs/agent-api/openai-compatibility">
    Use Agent API with any OpenAI SDK.
  </Card>

  <Card title="OpenCode Providers" icon="book" href="https://opencode.ai/docs/providers/">
    OpenCode custom provider reference.
  </Card>

  <Card title="OpenCode Docs" icon="book-open" href="https://opencode.ai/docs">
    Official OpenCode documentation.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [OpenCode documentation](https://opencode.ai/docs)
* Review our [FAQ](/docs/resources/faq)
