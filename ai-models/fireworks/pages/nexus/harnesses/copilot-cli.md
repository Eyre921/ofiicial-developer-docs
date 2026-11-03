---
title: "Copilot CLI"
source: https://docs.fireworks.ai/nexus/harnesses/copilot-cli
path: nexus/harnesses/copilot-cli
---

Connect the GitHub Copilot CLI to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

The desktop app is set up separately in [Copilot App](/nexus/harnesses/copilot-app).

Support summary:

* API the harness speaks to Fireworks: OpenAI Chat Completions
* Nexus Auto: Supported
* Native web search: Not added by Nexus. See [Web search](/nexus/auto#web-search).

The `copilot` command (`@github/copilot`) reads plain JSON under `~/.copilot`. It shares the folder with the desktop app but no settings, so you can connect either one, both, or neither.

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

**2. Connect Copilot CLI**

```bash wrap theme={null}
nexus copilot-cli
```

Nexus Auto is the default model. To pick another one, run `nexus copilot-cli --model <id>`, such as `--model glm-latest`.

`nexus copilot-cli status` shows the provider, where the key comes from, and the configured model.

**3. Start a session and pick a model**

Start a new `copilot` session. Switch models with `/model` or `copilot --model fireworks/<name>`.

The default is stored as `fireworks/auto`.

To restore your original settings, run `nexus copilot-cli off`.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin.
* Image input works on models that support it.
* Copilot CLI doesn't show context, reasoning, or pricing details for bring-your-own-key models.

- Instead of a Provider Key, a developer can save their own key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key) and run `nexus copilot-cli` again. Nexus CLI adds the saved key to the `fireworks` provider headers in `providers.json`. A Provider Key needs nothing saved locally.
- Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
- Nexus Auto (`auto`) is supported on the Chat Completions API.
- Manual setup sends `x-anthropic-api-key` and `x-openai-api-key` headers itself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* Nexus CLI doesn't add [web search](/nexus/auto#web-search) to Copilot CLI.

## Troubleshooting

* **A model switch doesn't take effect:** use provider-prefixed model IDs such as `fireworks/glm-latest`. Copilot CLI rejects a bare `glm-latest` and silently falls back to its configured model.

Fixes for issues that affect every harness are in [Nexus Auto troubleshooting](/nexus/auto#troubleshooting).

## Manual setup (advanced)

Add a `fireworks` provider and a model to `~/.copilot/providers.json`:

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

Copilot CLI won't start without a default model, so select it in `settings.json`:

```json ~/.copilot/settings.json theme={null}
{ "model": "fireworks/glm-latest" }
```

Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

* A bring-your-own-key provider has no default model, which is why `settings.json` must select one.
* To use Nexus Auto with Anthropic or OpenAI model turns, add a `headers` map to the provider, such as `"headers": { "x-anthropic-api-key": "sk-ant-..." }`, and use `auto` as the model `id` and `wireModel`. The [harness setup](/nexus/auto#nexus-cli) generates the full file.
* Running `nexus copilot-cli` again rewrites the `fireworks` provider entry. It keeps `x-anthropic-api-key` and `x-openai-api-key` headers you added by hand, but removes any other headers you added. Add those again after you reconnect.

## What the Nexus CLI writes

| File | What Nexus CLI writes |
| - | - |
| `~/.copilot/providers.json` | A `fireworks` provider with your key, plus one row per model, in the format shown in [Manual setup (advanced)](#manual-setup-advanced). Models that accept images get `vision` capabilities. |
| `~/.copilot/settings.json` | `"model": "fireworks/auto"`, or the model you chose with `--model` |

* Providers and models you added yourself stay in place.
* `providers.json` is saved with mode `0600`.
* The `x-anthropic-api-key` and `x-openai-api-key` headers appear only for keys you saved with `nexus auto`.
* `off` restores both files byte-for-byte from the snapshots under `~/.nexus/copilot-cli/`, or deletes them if Nexus CLI created them.
* `COPILOT_HOME` moves both files. Use `--providers-path` for a non-default `providers.json`.
