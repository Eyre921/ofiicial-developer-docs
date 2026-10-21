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

Requires Node.js 18 or later, `git`, and `bash`. On Windows, run it from Git Bash; PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks key.

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

> [!TIP]
>
> `nexus claude status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Messages API.

* **Anthropic model turns:** your Claude login (OAuth), or an exported `ANTHROPIC_API_KEY`.
* **OpenAI model turns:** connect an OpenAI [Provider Key](/nexus/provider-keys). Nexus CLI doesn't send a key from `--openai-api-key` or `nexus configure` on `auto`. See [how `auto` picks its closed model](/nexus/auto#how-auto-picks-its-closed-model).
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Your servers stay in `~/.claude.json`, and Nexus CLI sets `ENABLE_TOOL_SEARCH`.

Add a server with `claude mcp add <name> -- <command>`, and confirm it's configured:

```bash theme={null}
claude mcp list
# docs: npx -y your-mcp-server - ✔ Connected
```

Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results, with no MCP server or search service to set up.

## Usage and cost

For the session cost status line, `nexus claude usage`, and how its estimate differs from Claude Code's own cost, see [Usage and Cost](/nexus/metrics).

## Troubleshooting

* Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).
* Text-only models fail on pasted images. Use `/rewind`, or switch to a vision model such as `glm-5p3-flash`.
* Resume or restart the session after changing models.
* Auto mode says classifier requests are billed: this is expected, once per session, and auto mode keeps working. Its safety checks run on your Sonnet slot and bill to Anthropic. To bill them at Fireworks rates, pin Sonnet with `nexus claude --sonnet <id>`.

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

`ANTHROPIC_AUTH_TOKEN` sends the key as an `Authorization: Bearer` header, and `ANTHROPIC_API_KEY` sends it as an `x-api-key` header, which is why Claude Code asks you to approve it.

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
>     "ANTHROPIC_CUSTOM_HEADERS": "X-Fireworks-Api-Key: fw_...",
>     "DISABLE_TELEMETRY": "1",
>     "DO_NOT_TRACK": "1",
>     "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
>     "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1",
>     "CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE": "0",
>     "ENABLE_TOOL_SEARCH": "true"
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
> * The Fireworks key goes in a custom header, so your Claude login stays available for Anthropic model turns.
> * `[1m]` marks 1M-context models.
> * A pinned tier adds `ANTHROPIC_DEFAULT_<TIER>_MODEL` to `env`, such as `ANTHROPIC_DEFAULT_SONNET_MODEL`. A pinned subagent adds `CLAUDE_CODE_SUBAGENT_MODEL`.
> * The status line shows the estimated session cost. It is added only if you do not already have one.
> * Nexus CLI also turns off Claude Code telemetry, nonessential traffic, adaptive thinking, and package manager auto-updates, and enables MCP tool search.
> * `~/.claude.json`: if you export `ANTHROPIC_API_KEY`, Nexus CLI pre-approves it so Claude Code doesn't prompt. Nexus CLI also removes its retired `fireworks-websearch` server here.

## Claude Agent SDK

PreviewAnthropic Messages

The Claude Agent SDK can reuse the Claude Code settings above. Connect Claude Code first, with Nexus CLI or manually:

```bash wrap theme={null}
nexus claude --model auto
```

In the SDK query options, include `settingSources: ["user"]`. The SDK then reads the Fireworks endpoint, model, and credentials from `~/.claude/settings.json`.

Nexus CLI doesn't touch MCP for the SDK. MCP follows the setting sources your application loads.

`nexus claude` does not configure Claude Desktop. See [Claude Desktop](/nexus/harnesses/claude-desktop).
