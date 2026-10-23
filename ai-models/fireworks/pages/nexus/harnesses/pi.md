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

You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks API key (`fw_...`).

Already set up? Skip to step 2.

**2. Connect Pi**

```bash wrap theme={null}
nexus pi
nexus pi status
```

**3. Restart and pick a model**

Restart Pi if it was running. The default is `auto`. To change the default, run `nexus pi --model glm-latest`.

Pi stores other models under their full ID, such as `accounts/fireworks/routers/glm-latest`, so they line up with Pi's built-in `fireworks` rows.

> [!TIP]
>
> `nexus pi status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** save a key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key), then run `nexus pi` again. Nexus CLI adds the saved key to the provider headers in `models.json`. Or connect a [Provider Key](/nexus/provider-keys), which needs nothing saved locally.
* **Environment keys:** Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in Pi as usual.

Nexus CLI does not add web search to Pi. See [Web Search](/nexus/web-search).

## Microsoft Foundry

Nexus CLI can connect Pi to Fireworks models deployed in your Azure subscription. See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry). Nexus Auto is not available on Foundry.

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
> `models.json` gets a `providers.fireworks` entry with rows for models Pi's built-in `fireworks` catalog lacks, such as `auto`. Its `headers` carry any keys you saved with `nexus auto`.
>
> `auth.json` and `models.json` are saved with mode `0600`. `off` restores all three files byte-for-byte from the snapshots under `~/.nexus/pi/`. If you or Pi changed a file while connected, `off` reverts only the entries Nexus CLI owns and keeps everything else. Use `--settings-path` for a settings file stored elsewhere.
