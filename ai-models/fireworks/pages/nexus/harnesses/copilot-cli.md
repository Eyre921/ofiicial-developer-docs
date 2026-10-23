---
title: "Copilot CLI"
source: https://docs.fireworks.ai/nexus/harnesses/copilot-cli
path: nexus/harnesses/copilot-cli
---

Connect the GitHub Copilot CLI to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

The `copilot` command (`@github/copilot`) reads plain JSON under `~/.copilot`. It shares the folder with the desktop app but no settings, so you can connect either one, both, or neither. For the desktop app, see [Copilot App](/nexus/harnesses/copilot-app).

PreviewOpenAI Chat CompletionsNexus Auto

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

**2. Connect Copilot CLI**

```bash wrap theme={null}
nexus copilot-cli
nexus copilot-cli status
```

**3. Start a session and pick a model**

Start a new `copilot` session. The default is `fireworks/auto`. Switch models with `copilot --model fireworks/<name>` or `/model`. To change the default, run `nexus copilot-cli --model glm-latest`.

![Copilot CLI model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and MiniMax models](https://mintcdn.com/fireworksai/DBOQdoU3Q63xUkRQ/images/nexus/copilot-cli-model-picker.png?fit=max\&auto=format\&n=DBOQdoU3Q63xUkRQ\&q=85\&s=b5fcee9192d79e7e0e2796f945673c87)

Copilot CLI model picker after Nexus CLI, with Auto selected

> [!TIP]
>
> `nexus copilot-cli status` shows the provider, where the key comes from, and the configured model.

Image input works on models that support it. Copilot CLI doesn't show context, reasoning, or pricing details for bring-your-own-key models.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** save a key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key), then run `nexus copilot-cli` again. Nexus CLI adds the saved key to the `fireworks` provider headers in `providers.json`. Or connect a [Provider Key](/nexus/provider-keys), which needs nothing saved locally.
* **Environment keys:** Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in Copilot CLI as usual.

Nexus CLI does not add web search to Copilot CLI. See [Web Search](/nexus/web-search).

## Microsoft Foundry

Nexus CLI doesn't connect Copilot CLI to Microsoft Foundry. For other options, see [Nexus for Microsoft Foundry](/nexus/microsoft-foundry).

## Troubleshooting

* **A model switch doesn't take effect:** use provider-prefixed model IDs such as `fireworks/glm-latest`. Copilot CLI rejects a bare `glm-latest` and silently falls back to its configured model.

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness.

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

A bring-your-own-key provider has no default model, and Copilot CLI won't start without one. Select it in `settings.json`:

```json ~/.copilot/settings.json theme={null}
{ "model": "fireworks/glm-latest" }
```

To use Nexus Auto with Anthropic or OpenAI model turns, add a `headers` map to the provider, such as `"headers": { "x-anthropic-api-key": "sk-ant-..." }`, and use `auto` as the model `id` and `wireModel`. The [harness setup](/nexus/auto#nexus-cli) generates the full file.

> [!WARNING]
>
> Running `nexus copilot-cli` again rewrites the `fireworks` provider entry. It keeps `x-anthropic-api-key` and `x-openai-api-key` headers you added by hand, but removes any other headers you added. Add those again after you reconnect.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> | File | What Nexus CLI writes |
> | - | - |
> | `~/.copilot/providers.json` | A `fireworks` provider with your key, plus one row per model, in the format shown in [Manual setup (advanced)](#manual-setup-advanced). Models that accept images get `vision` capabilities. |
> | `~/.copilot/settings.json` | `"model": "fireworks/auto"`, or the model you chose with `--model` |
>
> Providers and models you added yourself stay in place. `providers.json` is saved with mode `0600`. The `x-anthropic-api-key` and `x-openai-api-key` headers appear only for keys you saved with `nexus auto`.
>
> `off` restores both files byte-for-byte from the snapshots under `~/.nexus/copilot-cli/`, or deletes them if Nexus CLI created them. `COPILOT_HOME` moves both files. Use `--providers-path` for a non-default `providers.json`.
