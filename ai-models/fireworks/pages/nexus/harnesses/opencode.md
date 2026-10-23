---
title: "OpenCode"
source: https://docs.fireworks.ai/nexus/harnesses/opencode
path: nexus/harnesses/opencode
---

Connect OpenCode to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

Connect OpenCode to Fireworks models and Nexus Auto.

Generally availableOpenAI Chat CompletionsNexus Auto

## Quick start

**1. Install and sign in**

```bash wrap theme={null}
curl -fsSL https://nexus.fireworks.ai/install.sh | bash
```

You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks API key (`fw_...`).

Already set up? Skip to step 2.

**2. Connect OpenCode**

```bash wrap theme={null}
nexus opencode
nexus opencode status
```

**3. Restart and pick a model**

Restart OpenCode and pick a model with `/models`. The default is `auto`, stored as `fireworks-ai/auto`. To change the default, run `nexus opencode --model glm-latest`.

Models that OpenCode already lists from models.dev keep their full ID, such as `fireworks-ai/accounts/fireworks/routers/glm-latest`, so nothing shows twice. Nexus CLI adds the rest, such as `auto`, under short IDs.

![OpenCode model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and other models](https://mintcdn.com/fireworksai/qp-9FYlGs5qTS-0n/images/nexus/opencode-model-picker.png?fit=max\&auto=format\&n=qp-9FYlGs5qTS-0n\&q=85\&s=6fb5e62060857be919ec1c20dd2b6009)

OpenCode model picker after Nexus CLI, with Auto selected

> [!TIP]
>
> `nexus opencode status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** save a key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key), then run `nexus opencode` again. Nexus CLI adds the saved key to the provider headers in `opencode.json`. Or connect a [Provider Key](/nexus/provider-keys), which needs nothing saved locally.
* **Environment keys:** Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Nexus CLI doesn't touch MCP. Your servers stay in the `mcp` block of `opencode.json`:

```json theme={null}
// ~/.config/opencode/opencode.json
{
  "mcp": {
    "docs": {
      "type": "local",
      "command": ["npx", "-y", "your-mcp-server"],
      "enabled": true
    }
  }
}
```

Nexus CLI does not add web search to OpenCode. See [Web Search](/nexus/web-search).

## Microsoft Foundry

Nexus CLI can connect OpenCode to Fireworks models deployed in your Azure subscription. See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry). Nexus Auto is not available on Foundry.

## Troubleshooting

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness. Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

**Fastest:** in OpenCode, run `/connect`, search **fireworks.ai**, paste your key, and pick a model with `/models`.

**Or edit the config** to add models and set a default:

```json ~/.config/opencode/opencode.json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "fireworks-ai": {
      "options": { "apiKey": "{env:FIREWORKS_API_KEY}" },
      "models": {
        "glm-latest": { "name": "GLM (Latest)" },
        "auto": { "name": "Nexus Auto" }
      }
    }
  },
  "model": "fireworks-ai/glm-latest"
}
```

> [!TIP]
>
> `opencode run -m fireworks-ai/auto "hello"` answers through Nexus Auto.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> ```json ~/.config/opencode/opencode.json theme={null}
> {
>   "provider": {
>     "fireworks-ai": {
>       "options": {
>         "apiKey": "fw_...",
>         "headers": { "x-anthropic-api-key": "sk-ant-..." }
>       },
>       "models": {
>         "auto": {
>           "name": "Auto",
>           "limit": { "context": 1048575, "output": 131072 },
>           "modalities": { "input": ["text", "image"] }
>         }
>       }
>     }
>   },
>   "model": "fireworks-ai/auto"
> }
> ```
>
> The `x-anthropic-api-key` and `x-openai-api-key` headers appear only for keys you saved with `nexus auto`. Nexus CLI also adds its own attribution headers. If your `opencode.json` uses OpenCode v2's `providers` map, Nexus CLI writes the Fireworks provider there too, so the models appear in `/models`.
>
> The file is saved with mode `0600`. Nexus CLI never changes `auth.json`. `off` restores `opencode.json` byte-for-byte from the snapshot under `~/.nexus/opencode/`. Use `--config-path` for a config stored elsewhere.
