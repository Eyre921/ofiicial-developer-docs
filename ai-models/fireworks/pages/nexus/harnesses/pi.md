---
title: "Pi"
source: https://docs.fireworks.ai/nexus/harnesses/pi
path: nexus/harnesses/pi
---

Connect Pi to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

Support summary:

* API the harness speaks to Fireworks: OpenAI Chat Completions
* Nexus Auto: Supported
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

**2. Connect Pi**

```bash wrap theme={null}
nexus pi
```

Nexus Auto is the default model. To pick another one, run `nexus pi --model <id>`, such as `--model glm-latest`.

`nexus pi status` shows the provider, where the key comes from, and the configured model.

**3. Restart Pi**

Restart Pi if it was running.

Pi stores models other than `auto` under their full ID, such as `accounts/fireworks/routers/glm-latest`, so they line up with Pi's built-in `fireworks` rows.

To restore your original settings, run `nexus pi off`.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin.

- Instead of a Provider Key, a developer can save their own key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key) and run `nexus pi` again. Nexus CLI adds the saved key to the provider headers in `models.json`. A Provider Key needs nothing saved locally.
- Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
- Nexus Auto (`auto`) is supported on the Chat Completions API.
- Manual setup sends `x-anthropic-api-key` and `x-openai-api-key` headers itself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* Nexus CLI doesn't add [web search](/nexus/auto#web-search) to Pi.

## Troubleshooting

Fixes for issues that affect every harness are in [Nexus Auto troubleshooting](/nexus/auto#troubleshooting).

## Manual setup (advanced)

Pi has a built-in `fireworks` provider that reads `FIREWORKS_API_KEY`. Set it as the default:

```json ~/.pi/agent/settings.json theme={null}
{
  "defaultProvider": "fireworks",
  "defaultModel": "accounts/fireworks/routers/glm-latest"
}
```

Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

Check: `pi -p "hello"` answers from GLM.

## What the Nexus CLI writes

Files in `~/.pi/agent/`: `settings.json`, `auth.json`, and `models.json`.

```json ~/.pi/agent/settings.json theme={null}
{
  "defaultProvider": "fireworks",
  "defaultModel": "auto"
}
```

```json ~/.pi/agent/auth.json theme={null}
{ "fireworks": { "type": "api_key", "key": "fw_..." } }
```

* If your `settings.json` already has an `enabledModels` list, Nexus CLI appends `fireworks/**` to it. Otherwise it leaves `enabledModels` out.
* `models.json` gets a `providers.fireworks` entry with rows for models Pi's built-in `fireworks` catalog lacks, such as `auto`. Its `headers` carry any keys you saved with `nexus auto`.
* `auth.json` and `models.json` are saved with mode `0600`.
* `off` restores all three files byte-for-byte from the snapshots under `~/.nexus/pi/`. If you or Pi changed a file while connected, `off` reverts only the entries Nexus CLI owns and keeps everything else.
* Use `--settings-path` for a settings file stored elsewhere.
