---
title: "Copilot CLI"
source: https://docs.fireworks.ai/nexus/harnesses/copilot-cli
path: nexus/harnesses/copilot-cli
---

Connect the GitHub Copilot CLI to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

The `copilot` command (`@github/copilot`) reads plain JSON under `~/.copilot`, separate from the desktop app.

PreviewOpenAI Chat CompletionsNexus Auto with manual setup

## Quick start

**1. Install and sign in**

```bash wrap theme={null}
curl -fsSL https://nexus.fireworks.ai/install.sh | bash
```

Requires Node.js 18 or later, `git`, and `bash`. On Windows, run it from Git Bash; PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks key.

Already set up? Skip to step 2.

**2. Connect Copilot CLI**

```bash wrap theme={null}
nexus copilot-cli
nexus copilot-cli status
```

**3. Start a session and pick a model**

Start a new `copilot` session. Switch models with `copilot --model fireworks/<name>` or `/model`.

![Copilot CLI model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and MiniMax models](https://mintcdn.com/fireworksai/DBOQdoU3Q63xUkRQ/images/nexus/copilot-cli-model-picker.png?fit=max\&auto=format\&n=DBOQdoU3Q63xUkRQ\&q=85\&s=b5fcee9192d79e7e0e2796f945673c87)

> [!TIP]
>
> `nexus copilot-cli status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus CLI can add `auto`, but it does not send provider keys from `copilot`. For turns on Anthropic or OpenAI models, connect a [Provider Key](/nexus/provider-keys) or use [manual setup](#manual-setup-advanced) to send `x-anthropic-api-key` and `x-openai-api-key` headers.

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in Copilot CLI as usual.

Nexus CLI does not add web search to Copilot CLI. See [Web Search](/nexus/web-search).

## Troubleshooting

> [!NOTE]
>
> Use provider-prefixed model IDs such as `fireworks/glm-latest`. The CLI rejects a bare `glm-latest` and silently falls back to its configured model.

## Manual setup (advanced)

```json ~/.copilot/providers.json theme={null}
{
  "providers": [
    {
      "name": "fireworks",
      "type": "openai",
      "wireApi": "completions",
      "baseUrl": "https://api.fireworks.ai/inference/v1",
      "apiKey": "fw_YOUR_FIREWORKS_API_KEY"
    }
  ],
  "models": [
    {
      "id": "glm-latest",
      "provider": "fireworks",
      "wireModel": "glm-latest",
      "name": "GLM (Latest)",
      "maxPromptTokens": 1048576,
      "maxContextWindowTokens": 1048576,
      "maxOutputTokens": 131072,
      "capabilities": { "supports": { "reasoningEffort": true } }
    }
  ]
}
```

```json ~/.copilot/settings.json theme={null}
{ "model": "fireworks/glm-latest" }
```

To use Nexus Auto with Anthropic or OpenAI model turns, add a `headers` map to the provider, such as `"headers": { "x-anthropic-api-key": "sk-ant-..." }`, and use `auto` as the model `id` and `wireModel`. Nexus CLI adds `auto` but does not send your provider keys, so use manual setup to send them yourself. The [harness setup](/nexus/auto#nexus-cli) generates the full file.

> [!WARNING]
>
> Running `nexus copilot-cli` again rewrites the `fireworks` provider entry and removes headers you added to it by hand. Add them again after you reconnect.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> `off` restores `providers.json` from its snapshot, or deletes it if Nexus CLI created it. Use `--providers-path` for a non-default location.
