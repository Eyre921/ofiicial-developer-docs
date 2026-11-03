---
title: "Coding Harnesses"
source: https://docs.fireworks.ai/nexus/harnesses
path: nexus/harnesses
---

Connect Claude Code, Claude Agent SDK, Claude Desktop, Codex CLI, ChatGPT, OpenCode, Pi, Cursor IDE, VS Code, Copilot, or DeepSeek Harness to Fireworks.

Every harness except Claude Desktop also supports [manual setup](/nexus/manual-setup).

Nexus CLI sets each harness's main model to `auto`, and a [Provider Key](/nexus/provider-keys) on your account works in every harness.

## Code

> [card] [Claude Code](/nexus/harnesses/claude-code)
>
> Messages API

> [card] [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk)
>
> Messages API

> [card] [Codex](/nexus/harnesses/codex)
>
> Responses API

> [card] [OpenCode](/nexus/harnesses/opencode)
>
> Chat Completions

> [card] [Pi](/nexus/harnesses/pi)
>
> Chat Completions

> [card] [DeepSeek Harness](/nexus/harnesses/deepseek)
>
> Chat Completions

> [card] [Cursor IDE](/nexus/harnesses/cursor)
>
> Chat Completions

> [card] [VS Code](/nexus/harnesses/vscode)
>
> Chat Completions

> [card] [Copilot App](/nexus/harnesses/copilot-app)
>
> Chat Completions

> [card] [Copilot CLI](/nexus/harnesses/copilot-cli)
>
> Chat Completions

## Cowork

> [card] [ChatGPT desktop app](/nexus/harnesses/chatgpt)
>
> Responses API

> [card] [Claude Desktop](/nexus/harnesses/claude-desktop)
>
> Limited support on macOS. Linux is coming soon

## What works where

| Harness | API | Nexus Auto | How Anthropic and OpenAI keys arrive | MCP | Manual setup |
| - | - | - | - | - | - |
| **Code** | | | | | |
| [Claude Code](/nexus/harnesses/claude-code) | Messages | Supports `auto` | Your Claude login or `ANTHROPIC_API_KEY` for Anthropic models. OpenAI models use a key saved with `nexus auto` or an OpenAI Provider Key | Servers stay in `~/.claude.json`. Nexus CLI sets `ENABLE_TOOL_SEARCH` | Yes |
| [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk) | Messages | Supported when the SDK reads the user settings written by Nexus CLI | Same as Claude Code | Not touched. Follows the setting sources your application loads | Through Claude Code settings |
| [Codex](/nexus/harnesses/codex) | Responses | Supports `auto` | Codex sign-in for OpenAI models. Anthropic models use a key saved with `nexus auto` or an Anthropic Provider Key | Servers stay in `[mcp_servers]`. Tools load through Codex's tool search | Yes |
| [OpenCode](/nexus/harnesses/opencode) | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Servers stay in the `mcp` block of `opencode.json` | Yes |
| [Pi](/nexus/harnesses/pi) | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| [DeepSeek Harness](/nexus/harnesses/deepseek) | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| [Cursor IDE](/nexus/harnesses/cursor) | Chat Completions | Supports `auto`. Closed models need Provider Keys. `nexus auto --providers` has no effect | Provider Keys only | Not touched | Yes |
| [VS Code](/nexus/harnesses/vscode) | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| [Copilot App](/nexus/harnesses/copilot-app) | Chat Completions | Supports `auto`. Closed models need Provider Keys | Provider Keys only | Not touched | Yes |
| [Copilot CLI](/nexus/harnesses/copilot-cli) | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| **Cowork** | | | | | |
| [ChatGPT desktop app](/nexus/harnesses/chatgpt) | Responses | Supports `auto` | Same as Codex | Same as Codex | Yes |
| [Claude Desktop](/nexus/harnesses/claude-desktop) (Limited) | Messages | Supports `auto`. Closed models need a key saved with `nexus auto` or Provider Keys | A key saved with `nexus auto`, added to `auto` turns by the local proxy | `on` imports your connectors. It includes your claude.ai organization's when the Claude Code CLI is installed and signed in. `nexus claude-desktop mcp sync` imports ones you add later | No |
