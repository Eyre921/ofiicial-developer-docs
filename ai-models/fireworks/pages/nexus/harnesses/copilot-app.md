---
title: "Copilot App"
source: https://docs.fireworks.ai/nexus/harnesses/copilot-app
path: nexus/harnesses/copilot-app
---

Add Fireworks models and Nexus Auto to the GitHub Copilot desktop app with the Nexus CLI or manual setup.

The GitHub Copilot **desktop app** keeps its built-in models and adds Fireworks alongside them.

PreviewOpenAI Chat CompletionsNexus Auto with Provider Keys

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

**2. Quit the app**

**Quit the app before connecting or running `off`.**

**3. Connect the Copilot App**

```bash wrap theme={null}
nexus copilot-app
nexus copilot-app status
```

**4. Reopen and pick a model**

Reopen the app and pick a Fireworks model in **Settings → Model providers**.

> [!TIP]
>
> `nexus copilot-app status` shows the provider, where the key comes from, and the configured model.

The app's bring-your-own-key path does not support image input, the hover-card Context row, or AI-credits pricing.

## Use Nexus Auto

Nexus CLI can add `auto`, but the app cannot send a local Anthropic or OpenAI key. Without a matching [Provider Key](/nexus/provider-keys), Nexus Auto serves every turn with open models. The app can't send extra headers, so manual setup needs Provider Keys too. See [Which harnesses can send provider keys](/nexus/auto#nexus-cli).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in the app as usual.

Nexus CLI does not add web search to the Copilot App. See [Web Search](/nexus/web-search).

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
> `off` deletes the provider and its models. Use `--db-path` for a non-default database.
