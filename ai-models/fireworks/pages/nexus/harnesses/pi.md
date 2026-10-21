---
title: "Pi"
source: https://docs.fireworks.ai/nexus/harnesses/pi
path: nexus/harnesses/pi
---

Connect Pi to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

Connect Pi to Fireworks models and Nexus Auto.

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

**2. Connect Pi**

```bash wrap theme={null}
nexus pi
nexus pi status
```

**3. Restart Pi**

Restart Pi if it was running. The default model is `auto`.

> [!TIP]
>
> `nexus pi status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** connect an Anthropic or OpenAI [Provider Key](/nexus/provider-keys). Nexus CLI doesn't send local keys on `auto`.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in Pi as usual.

Nexus CLI does not add web search to Pi. See [Web Search](/nexus/web-search).

## Troubleshooting

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness.

## Manual setup (advanced)

Pi has a built-in `fireworks` provider that reads `FIREWORKS_API_KEY`. Set it as the default:

```json ~/.pi/agent/settings.json theme={null}
{
  "defaultProvider": "fireworks",
  "defaultModel": "accounts/fireworks/routers/glm-latest"
}
```

> [!TIP]
>
> `pi -p "hello"` answers from GLM.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

**\~/.pi/agent**

**settings.json**

**auth.json**

**models.json**

> **See what Nexus CLI writes**
>
> ```json ~/.pi/agent/settings.json theme={null}
> {
>   "defaultProvider": "fireworks",
>   "defaultModel": "auto"
> }
> ```
>
> ```json ~/.pi/agent/auth.json theme={null}
> { "fireworks": { "type": "api_key", "key": "fw_..." } }
> ```
>
> If your `settings.json` already has an `enabledModels` list, Nexus CLI appends `fireworks/**` to it. Otherwise it leaves `enabledModels` out.
>
> `models.json` adds a `providers.fireworks` entry with rows for models Pi's built-in `fireworks` catalog lacks, such as `auto`. `off` restores the whole `providers.fireworks` entry to what it was before you connected. Use `--settings-path` for a settings file stored elsewhere.
