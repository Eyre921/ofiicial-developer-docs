---
title: "Claude Code"
source: https://docs.fireworks.ai/nexus/harnesses/claude-code
path: nexus/harnesses/claude-code
---

Connect the Claude Code CLI to Fireworks with the Nexus CLI or manual setup, and use Nexus Auto with your Claude login.

Claude Code keeps your Claude login for Anthropic model turns. Claude Code on the web and other cloud sessions aren't supported.

Support summary:

* API the harness speaks to Fireworks: Anthropic Messages
* Nexus Auto: Supported
* Native web search: Supported. Fireworks runs the harness's native web search server-side, with any Fireworks model. See [Web search](/nexus/auto#web-search).

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

**2. Connect Claude Code**

```bash wrap theme={null}
nexus claude
```

Nexus Auto is the default model. To pick another one, run `nexus claude --model <id>`.

`--model` sets the default model for new sessions and adds it to `/model`. `/model` also lists a **Nexus Auto** row (model ID `auto`). Enterprise accounts, which get general access to open models, also see the Fireworks catalog. Your own picker rows are not changed. Set [effort](/nexus/orchestration-preferences) in that same picker.

To send one Anthropic model tier or your subagents to a specific model, pin that slot:

```bash wrap theme={null}
nexus claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest
```

Tier flags are `--opus`, `--sonnet`, `--haiku`, `--fable`, and `--subagent`. Unpinned slots stay on Claude Code's defaults. Running `nexus claude` again keeps your pins. Pass `native`, such as `--sonnet native`, to release a slot.

`nexus claude status` shows the provider, where the key comes from, and the configured model.

**3. Restart and pick Nexus Auto**

Start a new session, then pick **Nexus Auto** in `/model`.

To keep a session, exit and run `claude --resume <id>`. The Fireworks catalog in `/model` needs Claude Code 2.1.242 or later. On an older version, `nexus claude` says so. Run `claude update`, then `nexus claude` again.

To restore your original settings, run `nexus claude off`.

## Use Nexus Auto

* **Anthropic model turns** use your Claude login.
* **OpenAI model turns** need an OpenAI [Provider Key](/nexus/provider-keys) from your admin.

- Anthropic model turns can also use an exported `ANTHROPIC_API_KEY`.
- Instead of a Provider Key, a developer can save their own OpenAI key with `nexus auto --openai-api-key` (it prompts for the key) and run `nexus claude` again. Nexus CLI adds the saved key to `ANTHROPIC_CUSTOM_HEADERS`.
- Nexus CLI never sends an Anthropic key saved with `nexus auto` to Claude Code. The Claude login covers Anthropic model turns.
- Nexus Auto is supported on the Messages API. See [which models `auto` can use](/nexus/auto#which-models-auto-can-use).
- Manual setup sends `x-anthropic-api-key` and `x-openai-api-key` headers itself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* claude.ai connectors remain available when Claude Code is signed in with your claude.ai subscription.
* Native web search and web fetch are supported. Fireworks runs the search server-side, so no search MCP server is required.

- MCP servers stay in `~/.claude.json`. Nexus CLI sets `ENABLE_TOOL_SEARCH` so MCP tool search stays on.
- With an API key or another sign-in, claude.ai connectors aren't available.
- Fireworks runs web search server-side and returns the results.
- Add a server with `claude mcp add <name> -- <command>`, and confirm it with `claude mcp list`.

Nexus CLI adds a [session cost status line](/nexus/metrics) if Claude Code doesn't already have a status line.

## Troubleshooting

* **A pasted image fails:** the model is text-only. Use `/rewind`, or switch to a vision model such as `glm-5p3-flash`.
* **`/model` doesn't list Fireworks models:** run `claude update`, then `nexus claude` again.
* **Auto mode says classifier requests are billed:** this notice is expected and doesn't stop auto mode.

- Resume or restart the session after changing models.
- The Fireworks catalog in `/model` needs Claude Code 2.1.242 or later.
- The auto mode notice appears once per session. The safety checks run on the Sonnet slot, so they bill to Anthropic. To bill them at Fireworks rates, pin Sonnet with `nexus claude --sonnet <id>`.
- Upgrading from an earlier version: see [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

Add these values to `~/.claude/settings.json`, then run `claude`:

```json ~/.claude/settings.json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_AUTH_TOKEN": "fw_YOUR_FIREWORKS_API_KEY",
    "ENABLE_TOOL_SEARCH": "true"
  },
  "model": "glm-latest"
}
```

To use Nexus Auto, set `"model": "auto"` and connect an Anthropic [Provider Key](/nexus/provider-keys). Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

* `ENABLE_TOOL_SEARCH` keeps MCP tool search on. Claude Code turns it off when `ANTHROPIC_BASE_URL` points anywhere other than Anthropic.
* For one shell instead: `export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"`, `export ANTHROPIC_API_KEY="$FIREWORKS_API_KEY"`, then `claude --model glm-latest`.
* `ANTHROPIC_AUTH_TOKEN` sends the key as an `Authorization: Bearer` header. `ANTHROPIC_API_KEY` sends it as an `x-api-key` header, so Claude Code asks once to approve it.
* Instead of a Provider Key, Anthropic model turns under `auto` can use an `x-anthropic-api-key` line in `ANTHROPIC_CUSTOM_HEADERS`.
* The first reply should come from the Fireworks model you set.
* Claude Code's `/model` picker does not list Fireworks models set by hand. Change models in `settings.json` or with `claude --model <id>`. Claude Code may log `unrecognized_model` for Fireworks IDs; requests still succeed.

## Claude Agent SDK

Support summary for the Claude Agent SDK: API Anthropic Messages.

Connect Claude Code first, then include `settingSources: ["user"]` in the SDK query options. The SDK reads the Fireworks endpoint, model, and credentials from `~/.claude/settings.json`.

* Connect with `nexus claude --model auto`, or manually.
* Nexus CLI doesn't touch MCP for the SDK. MCP follows the setting sources the application loads.
* `nexus claude` does not configure Claude Desktop. See [Claude Desktop](/nexus/harnesses/claude-desktop).

## What the Nexus CLI writes

Files: `~/.claude/settings.json`, `~/.claude.json`, and a backup under `~/.nexus/` that `nexus claude off` restores.

```json ~/.claude/settings.json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_CUSTOM_HEADERS": "X-Fireworks-Api-Key: fw_...\nX-Title: Claude Code\nHTTP-Referer: nexus/v<version>",
    "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1",
    "ENABLE_TOOL_SEARCH": "true",
    "CLAUDE_CODE_DISABLE_EXPLORE_INHERIT_CAP": "1"
  },
  "modelPicker": {
    "options": [
      {
        "model": "auto[1m]",
        "label": "Nexus Auto",
        "description": "Smart routing: automatically picks the best model for the task."
      }
    ]
  },
  "model": "auto[1m]",
  "statusLine": { "type": "command", "command": "... claude-statusline.mjs" }
}
```

* The Fireworks key goes in a custom header, so the Claude login stays available for Anthropic model turns. The same header names the client (`X-Title`, `HTTP-Referer`).
* An OpenAI key saved with `nexus auto --openai-api-key` adds an `x-openai-api-key` line to that header.
* `[1m]` marks 1M-context models.
* A pinned tier adds `ANTHROPIC_DEFAULT_<TIER>_MODEL` to `env`, such as `ANTHROPIC_DEFAULT_SONNET_MODEL`. A pinned subagent adds `CLAUDE_CODE_SUBAGENT_MODEL`.
* The status line shows the estimated session cost and, on `auto`, the model that served the latest turn. Nexus CLI adds it only if none exists.
* The other `env` values turn off adaptive thinking, keep MCP tool search on, and let the Explore agent inherit the session model, so exploration stays on Fireworks rates.
* Nexus CLI leaves Claude Code telemetry and auto-updates as they are. An upgrade removes the telemetry and auto-update settings that earlier versions wrote.
* `~/.claude.json`: if `ANTHROPIC_API_KEY` is exported, Nexus CLI pre-approves it so Claude Code doesn't prompt. Nexus CLI also removes its retired `fireworks-websearch` server from this file.
