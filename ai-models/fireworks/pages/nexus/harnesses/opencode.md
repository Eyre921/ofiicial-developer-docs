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

Requires Node.js 18 or later, `git`, and `bash`. On Windows, run it from Git Bash; PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks key.

Already set up? Skip to step 2.

**2. Connect OpenCode**

```bash wrap theme={null}
nexus opencode
nexus opencode status
```

**3. Restart and pick a model**

Restart OpenCode. The default model is `auto`, stored as `fireworks-ai/auto`. `auto` and `-latest` aliases such as `glm-latest` stay short IDs. Other catalog models, such as `glm-5p3`, are stored as full Fireworks paths.

![OpenCode model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and other models](https://mintcdn.com/fireworksai/qp-9FYlGs5qTS-0n/images/nexus/opencode-model-picker.png?fit=max\&auto=format\&n=qp-9FYlGs5qTS-0n\&q=85\&s=6fb5e62060857be919ec1c20dd2b6009)

> [!TIP]
>
> `nexus opencode status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** connect an Anthropic or OpenAI [Provider Key](/nexus/provider-keys). Nexus CLI doesn't send local keys on `auto`.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Your servers stay in the `mcp` block of `opencode.json`.

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

## Troubleshooting

Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

**Fastest:** in OpenCode, run `/connect`, search **fireworks.ai**, paste your key, and pick a model with `/models`.

**Or edit the config** to add routers and pin a default:

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
>       "options": { "apiKey": "fw_..." },
>       "models": {
>         "auto": { "name": "Auto", "limit": { "context": 1048575, "output": 131072 } },
>         "glm-latest": { "name": "GLM (Latest)" }
>       }
>     }
>   },
>   "model": "fireworks-ai/auto"
> }
> ```
>
> If your `opencode.json` uses OpenCode v2's `providers` map, Nexus CLI writes the Fireworks provider there too, so the models appear in `/models`.
>
> The file is saved with mode `0600`. Nexus CLI never changes `auth.json`. Use `--config-path` for a config stored elsewhere.
