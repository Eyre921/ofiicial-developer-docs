---
title: "OpenCode"
source: https://docs.fireworks.ai/nexus/harnesses/opencode
path: nexus/harnesses/opencode
---

Connect OpenCode to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

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

**2. Connect OpenCode**

```bash wrap theme={null}
nexus opencode
```

Nexus Auto is the default model. To pick another one, run `nexus opencode --model <id>`, such as `--model glm-latest`.

`nexus opencode status` shows the provider, where the key comes from, and the configured model.

**3. Restart and pick a model**

Restart OpenCode and pick a model with `/models`.

* The default is stored as `fireworks-ai/auto`.
* Models that OpenCode already lists from models.dev keep their full ID, such as `fireworks-ai/accounts/fireworks/routers/glm-latest`, so nothing shows twice. Nexus CLI adds the rest, such as `auto`, under short IDs.

To restore your original settings, run `nexus opencode off`.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin.

- Instead of a Provider Key, a developer can save their own key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key) and run `nexus opencode` again. Nexus CLI adds the saved key to the provider headers in `opencode.json`. A Provider Key needs nothing saved locally.
- Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
- Nexus Auto (`auto`) is supported on the Chat Completions API.
- Manual setup sends `x-anthropic-api-key` and `x-openai-api-key` headers itself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* Nexus CLI doesn't add [web search](/nexus/auto#web-search) to OpenCode.

MCP servers stay in the `mcp` block of `opencode.json`:

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

## Troubleshooting

Fixes for issues that affect every harness are in [Nexus Auto troubleshooting](/nexus/auto#troubleshooting).

* Upgrading from an earlier version: see [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

In OpenCode, run `/connect`, search **fireworks.ai**, paste your key, and pick a model with `/models`.

To add models and set a default instead, edit the config:

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

Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

* `/connect` is the fastest manual path.
* Check: `opencode run -m fireworks-ai/auto "hello"` answers through Nexus Auto.

## What the Nexus CLI writes

```json ~/.config/opencode/opencode.json theme={null}
{
  "provider": {
    "fireworks-ai": {
      "options": {
        "apiKey": "fw_...",
        "headers": { "x-anthropic-api-key": "sk-ant-..." }
      },
      "models": {
        "auto": {
          "name": "Auto",
          "limit": { "context": 1048575, "output": 131072 },
          "modalities": { "input": ["text", "image"] }
        }
      }
    }
  },
  "model": "fireworks-ai/auto"
}
```

* The `x-anthropic-api-key` and `x-openai-api-key` headers appear only for keys you saved with `nexus auto`. Nexus CLI also adds its own attribution headers.
* If your `opencode.json` uses OpenCode v2's `providers` map, Nexus CLI writes the Fireworks provider there too, so the models appear in `/models`.
* The file is saved with mode `0600`. Nexus CLI never changes `auth.json`.
* `off` restores `opencode.json` byte-for-byte from the snapshot under `~/.nexus/opencode/`.
* Use `--config-path` for a config stored elsewhere.
