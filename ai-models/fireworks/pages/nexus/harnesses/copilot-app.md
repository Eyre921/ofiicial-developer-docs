---
title: "Copilot App"
source: https://docs.fireworks.ai/nexus/harnesses/copilot-app
path: nexus/harnesses/copilot-app
---

Add Fireworks models and Nexus Auto to the GitHub Copilot desktop app with the Nexus CLI or manual setup.

The GitHub Copilot **desktop app** keeps its built-in models and adds Fireworks alongside them. For the `copilot` command, see [Copilot CLI](/nexus/harnesses/copilot-cli).

PreviewOpenAI Chat CompletionsNexus Auto with Provider Keys

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

**2. Quit the app**

**Quit the app before you connect or run `off`.** A running app overwrites the change from memory. If it's open, Nexus CLI waits until you quit. `--force` writes anyway, which isn't recommended.

**3. Connect the Copilot App**

```bash wrap theme={null}
nexus copilot-app
nexus copilot-app status
```

**4. Reopen and pick a model**

Reopen the app and pick a model under **Fireworks** in the model picker. The default is `auto`. To change the default, run `nexus copilot-app --model glm-latest`.

> [!TIP]
>
> `nexus copilot-app status` shows the provider, where the key comes from, and the configured model.

The app's bring-your-own-key path does not support image input, the hover-card Context row, or AI-credits pricing.

## Use Nexus Auto

Nexus CLI registers `auto` in the app.

* **Anthropic and OpenAI model turns:** connect a [Provider Key](/nexus/provider-keys). Nexus CLI doesn't send keys saved with `nexus auto` from the app, and the app can't send extra headers, so manual setup needs Provider Keys too. Without a Provider Key, Nexus Auto serves every turn with open models.

See [Which harnesses can send provider keys](/nexus/auto#nexus-cli).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in the app as usual.

Nexus CLI does not add web search to the Copilot App. See [Web Search](/nexus/web-search).

## Microsoft Foundry

Nexus CLI doesn't connect the Copilot App to Microsoft Foundry. For other options, see [Nexus for Microsoft Foundry](/nexus/microsoft-foundry).

## Troubleshooting

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness.

## Manual setup (advanced)

In **Settings → Model providers**, add a provider with the values Nexus CLI uses:

| Field | Value |
| - | - |
| Base URL | `https://api.fireworks.ai/inference/v1` |
| API key | Your Fireworks key |
| Models | Fireworks IDs, such as `glm-latest` or `kimi-latest` |

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> Nexus CLI writes to `~/.copilot/data.db` (SQLite, movable with `COPILOT_HOME`):
>
> | Table | What Nexus CLI adds |
> | - | - |
> | `model_providers` | One `Fireworks` provider of type `openai`, with base URL `https://api.fireworks.ai/inference/v1` and your key as an `Authorization: Bearer` header |
> | `provider_models` | One row per model, with token limits and reasoning efforts (`low`, `medium`, `high`, `max`) |
>
> The file is saved with mode `0600`. `off` deletes the provider and its models and leaves providers you added yourself. Use `--db-path` for a non-default database.
