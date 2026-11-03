---
title: "Copilot App"
source: https://docs.fireworks.ai/nexus/harnesses/copilot-app
path: nexus/harnesses/copilot-app
---

Add Fireworks models and Nexus Auto to the GitHub Copilot desktop app with the Nexus CLI or manual setup.

The `copilot` command is set up separately in [Copilot CLI](/nexus/harnesses/copilot-cli).

Support summary:

* API the harness speaks to Fireworks: OpenAI Chat Completions
* Nexus Auto: Supported. Anthropic and OpenAI model turns need Provider Keys
* Native web search: Not added by Nexus. See [Web search](/nexus/auto#web-search).

Plan access: Pro and Team don't include general access to open models. They use Nexus Auto (`auto`) along with their own Claude or ChatGPT models, and Nexus Auto still sends turns to open models. Enterprise accounts also get general access to open models on Fireworks serverless. See [Plans and Accounts](/nexus/plans).

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

If the Nexus CLI is already installed and signed in, skip to step 2.

**2. Quit the app**

**Quit the app before you connect or run `off`.** A running app overwrites the change from memory. If it's open, Nexus CLI waits until you quit.

`--force` writes anyway, which isn't recommended.

**3. Connect the Copilot App**

```bash wrap theme={null}
nexus copilot-app
```

Nexus Auto is the default model. To pick another one, run `nexus copilot-app --model <id>`, such as `--model glm-latest`.

`nexus copilot-app status` shows the provider, where the key comes from, and the configured model.

**4. Reopen and pick a model**

Reopen the app and pick a model under **Fireworks** in the model picker.

To restore your original settings, quit the app and run `nexus copilot-app off`.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin. Without one, Nexus Auto serves every turn with open models.
* Image input, the hover-card Context row, and AI-credits pricing don't work with the app's bring-your-own-key path.

- Nexus CLI registers `auto` in the app.
- Nexus CLI doesn't send keys saved with `nexus auto` from the app, and the app can't send extra headers, so manual setup needs Provider Keys too.
- See [Which harnesses can send provider keys](/nexus/auto#nexus-cli).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* Nexus CLI doesn't add [web search](/nexus/auto#web-search) to the Copilot App.

## Troubleshooting

Fixes for issues that affect every harness are in [Nexus Auto troubleshooting](/nexus/auto#troubleshooting).

## Manual setup (advanced)

In **Settings → Model providers**, add a provider with the values Nexus CLI uses:

| Field | Value |
| - | - |
| Base URL | `https://api.fireworks.ai/inference/v1` |
| API key | Your Fireworks key |
| Models | Fireworks IDs, such as `glm-latest` or `kimi-latest` |

Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

## What the Nexus CLI writes

Nexus CLI writes to `~/.copilot/data.db` (SQLite, movable with `COPILOT_HOME`):

| Table | What Nexus CLI adds |
| - | - |
| `model_providers` | One `Fireworks` provider of type `openai`, with base URL `https://api.fireworks.ai/inference/v1` and your key as an `Authorization: Bearer` header |
| `provider_models` | One row per model, with token limits and reasoning efforts (`low`, `medium`, `high`, `max`) |

* The file is saved with mode `0600`.
* `off` deletes the provider and its models and leaves providers you added yourself.
* Use `--db-path` for a non-default database.
