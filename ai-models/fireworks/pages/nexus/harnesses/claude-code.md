---
title: "Claude Code"
source: https://docs.fireworks.ai/nexus/harnesses/claude-code
path: nexus/harnesses/claude-code
---

Connect the Claude Code CLI to Fireworks with the Nexus CLI or manual setup, and use Nexus Auto with your Claude login.

Connect the Claude Code CLI to Fireworks models and Nexus Auto. Your Claude login stays signed in for Anthropic model turns.

Generally availableAnthropic MessagesNexus AutoNative web search

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

**2. Connect Claude Code**

```bash wrap theme={null}
nexus claude
nexus claude status
```

Nexus CLI selects Nexus Auto by default. To choose another model, pass `--model`:

```bash wrap theme={null}
nexus claude --model glm-5p3-flash
```

`--model` sets the default model for new sessions and adds it to `/model`. `/model` also lists the Fireworks catalog and an **Auto** row for Nexus Auto (`auto`). Your own picker rows are not changed. Set [effort](/nexus/orchestration-preferences) in that same picker.

To send one Anthropic model tier or your subagents to a specific model, pin that slot:

```bash wrap theme={null}
nexus claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest
```

Tier flags are `--opus`, `--sonnet`, `--haiku`, `--fable`, and `--subagent`. Unpinned slots stay on Claude Code's defaults. Running `nexus claude` again keeps your pins. Pass `native`, such as `--sonnet native`, to release a slot.

**3. Restart and pick a model**

Start a new session, or exit and run `claude --resume <id>`. Open `/model`:

![Claude Code model picker showing Auto, DeepSeek, Ember, and GLM Fireworks serverless models](https://mintcdn.com/fireworksai/DBOQdoU3Q63xUkRQ/images/nexus/claude-code-model-picker.png?fit=max\&auto=format\&n=DBOQdoU3Q63xUkRQ\&q=85\&s=44699935bfc797c540976eec4805b11d)

Fireworks models in the Claude Code model picker

> [!TIP]
>
> `nexus claude status` shows the provider, where the key comes from, and the configured model.

The Fireworks catalog in `/model` needs Claude Code 2.1.242 or later. On an older version, `nexus claude` says so. Run `claude update`, then `nexus claude` again.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Messages API.

* **Anthropic model turns:** your Claude login (OAuth), or an exported `ANTHROPIC_API_KEY`.
* **OpenAI model turns:** connect an OpenAI [Provider Key](/nexus/provider-keys), or save your own key with `nexus auto --openai-api-key` (it prompts for the key) and run `nexus claude` again. Nexus CLI adds the saved key to `ANTHROPIC_CUSTOM_HEADERS`.
* Nexus CLI never sends an Anthropic key you saved with `nexus auto` to Claude Code. Your Claude login covers Anthropic model turns.
* See [which models `auto` can use](/nexus/auto#which-models-auto-can-use).
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Your MCP servers stay in `~/.claude.json`. Nexus CLI sets `ENABLE_TOOL_SEARCH` so MCP tool search stays on.

Add a server with `claude mcp add <name> -- <command>`, and confirm it's configured:

```bash theme={null}
claude mcp list
# docs: npx -y your-mcp-server - ✔ Connected
```

Native web search and web fetch keep working while connected through Nexus CLI. Fireworks runs the search server-side and returns the results. You don't need an MCP server or a search service.

## Usage and cost

For the session cost status line, `nexus claude usage`, and how its estimate differs from Claude Code's own cost, see [Usage and Cost](/nexus/metrics).

## Troubleshooting

* Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).
* Text-only models fail on pasted images. Use `/rewind`, or switch to a vision model such as `glm-5p3-flash`.
* Resume or restart the session after changing models.
* `/model` doesn't list the Fireworks catalog: update Claude Code to 2.1.242 or later with `claude update`, then run `nexus claude` again.
* Auto mode says classifier requests are billed: this notice is expected. It appears once per session, and auto mode keeps working. The safety checks run on your Sonnet slot, so they bill to Anthropic. To bill them at Fireworks rates, pin Sonnet with `nexus claude --sonnet <id>`.

## Manual setup (advanced)

**1. Point Claude Code at Fireworks**

Add these values to `~/.claude/settings.json`:

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

`ENABLE_TOOL_SEARCH` keeps MCP tool search on. Claude Code turns it off when `ANTHROPIC_BASE_URL` points anywhere other than Anthropic.

Or set them for one shell:

```bash wrap theme={null}
export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"
export ANTHROPIC_API_KEY="$FIREWORKS_API_KEY"
claude --model glm-latest
```

`ANTHROPIC_AUTH_TOKEN` sends the key as an `Authorization: Bearer` header. `ANTHROPIC_API_KEY` sends it as an `x-api-key` header, so Claude Code asks you to approve it.

**2. Start a session**

Run `claude`. Claude Code may ask once whether to use the API key; approve it.
\[!TIP] The first reply comes from the Fireworks model you set.

**3. Optional: use Nexus Auto**

Set `"model": "auto"`. For Anthropic model turns, connect an Anthropic [Provider Key](/nexus/provider-keys), or add `x-anthropic-api-key` to `ANTHROPIC_CUSTOM_HEADERS`.

Claude Code's `/model` picker does not list Fireworks models you set by hand. Change models in `settings.json` or with `claude --model <id>`. Claude Code may log `unrecognized_model` for Fireworks IDs; requests still succeed.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

**\~**

**.claude**

**settings.json**

**.claude.json**

**.nexus**

**backup for off**

> **See what Nexus CLI writes**
>
> ```json ~/.claude/settings.json theme={null}
> {
>   "env": {
>     "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
>     "ANTHROPIC_CUSTOM_HEADERS": "X-Fireworks-Api-Key: fw_...\nX-Title: Claude Code\nHTTP-Referer: nexus/v<version>",
>     "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1",
>     "ENABLE_TOOL_SEARCH": "true",
>     "CLAUDE_CODE_DISABLE_EXPLORE_INHERIT_CAP": "1"
>   },
>   "modelPicker": {
>     "options": [
>       { "model": "auto[1m]", "label": "Auto" }
>     ]
>   },
>   "model": "auto[1m]",
>   "statusLine": { "type": "command", "command": "... claude-statusline.mjs" }
> }
> ```
>
> * The Fireworks key goes in a custom header, so your Claude login stays available for Anthropic model turns. The same header names the client (`X-Title`, `HTTP-Referer`).
> * An OpenAI key saved with `nexus auto --openai-api-key` adds an `x-openai-api-key` line to that header.
> * `[1m]` marks 1M-context models.
> * A pinned tier adds `ANTHROPIC_DEFAULT_<TIER>_MODEL` to `env`, such as `ANTHROPIC_DEFAULT_SONNET_MODEL`. A pinned subagent adds `CLAUDE_CODE_SUBAGENT_MODEL`.
> * The status line shows the estimated session cost and, on `auto`, the model that served the latest turn. Nexus CLI adds it only if you don't already have one.
> * The other `env` values turn off adaptive thinking, keep MCP tool search on, and let the Explore agent inherit the session model. Exploration then stays on Fireworks rates.
> * Nexus CLI leaves Claude Code telemetry and auto-updates as you have them. An upgrade removes the telemetry and auto-update settings that earlier versions wrote.
> * `~/.claude.json`: if you export `ANTHROPIC_API_KEY`, Nexus CLI pre-approves it so Claude Code doesn't prompt. Nexus CLI also removes its retired `fireworks-websearch` server from this file.

## Claude Agent SDK

PreviewAnthropic Messages

The Claude Agent SDK can reuse the Claude Code settings above. Connect Claude Code first, with Nexus CLI or manually:

```bash wrap theme={null}
nexus claude --model auto
```

In the SDK query options, include `settingSources: ["user"]`. The SDK then reads the Fireworks endpoint, model, and credentials from `~/.claude/settings.json`.

Nexus CLI doesn't touch MCP for the SDK. MCP follows the setting sources your application loads.

`nexus claude` does not configure Claude Desktop. See [Claude Desktop](/nexus/harnesses/claude-desktop).
