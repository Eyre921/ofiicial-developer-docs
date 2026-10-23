---
title: "Coding Harnesses"
source: https://docs.fireworks.ai/nexus/harnesses
path: nexus/harnesses
---

Connect Claude Code, Claude Agent SDK, Claude Desktop, Codex CLI, ChatGPT, OpenCode, Pi, Cursor IDE, VS Code, Copilot, or DeepSeek Harness to Fireworks.

Pick your harness for its quick start, Nexus Auto setup, and troubleshooting. Most harnesses also have [manual setup](/nexus/manual-setup). Claude Desktop is Nexus CLI only.

Harnesses marked Preview work, but they may change and some features are limited. Each harness page lists its limits.

## Connections

### Code

> **[Claude Code](/nexus/harnesses/claude-code)**
>
> Messages API

> **[Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk)**
>
> Messages API

> **[Codex](/nexus/harnesses/codex)**
>
> Responses API

> **[OpenCode](/nexus/harnesses/opencode)**
>
> Chat Completions

> **[Pi](/nexus/harnesses/pi)**
>
> Chat Completions

> **[DeepSeek Harness](/nexus/harnesses/deepseek)**
>
> Chat Completions

> **[Cursor IDE](/nexus/harnesses/cursor)**
>
> Chat Completions

> **[VS Code](/nexus/harnesses/vscode)**
>
> Chat Completions

> **[Copilot App](/nexus/harnesses/copilot-app)**
>
> Chat Completions

> **[Copilot CLI](/nexus/harnesses/copilot-cli)**
>
> Chat Completions

### Cowork

> **[ChatGPT desktop app](/nexus/harnesses/chatgpt)**
>
> Responses API

> **[Claude Desktop](/nexus/harnesses/claude-desktop)**
>
> macOS and Linux

## What works where

Nexus CLI starts each harness's main model on `auto`. A Provider Key on your account works in every harness.

| Harness | Status | API | Nexus Auto | How Anthropic and OpenAI keys arrive | MCP | Manual setup |
| - | - | - | - | - | - | - |
| **Code** | | | | | | |
| [Claude Code](/nexus/harnesses/claude-code) | Generally available | Messages | Supports `auto` | Your Claude login or `ANTHROPIC_API_KEY` for Anthropic models. OpenAI models use a key saved with `nexus auto` or an OpenAI Provider Key | Servers stay in `~/.claude.json`. Nexus CLI sets `ENABLE_TOOL_SEARCH` | Yes |
| [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk) | Preview | Messages | Supported when the SDK reads the user settings written by Nexus CLI | Same as Claude Code | Not touched. Follows the setting sources your application loads | Through Claude Code settings |
| [Codex](/nexus/harnesses/codex) | Generally available | Responses | Supports `auto` | Codex sign-in for OpenAI models. Anthropic models use a key saved with `nexus auto` or an Anthropic Provider Key | Servers stay in `[mcp_servers]`. Tools load through Codex's tool search | Yes |
| [OpenCode](/nexus/harnesses/opencode) | Generally available | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Servers stay in the `mcp` block of `opencode.json` | Yes |
| [Pi](/nexus/harnesses/pi) | Generally available | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| [DeepSeek Harness](/nexus/harnesses/deepseek) | Generally available | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| [Cursor IDE](/nexus/harnesses/cursor) | Preview | Chat Completions | Supports `auto`. Closed models need Provider Keys. `nexus auto --providers` has no effect | Provider Keys only | Not touched | Yes |
| [VS Code](/nexus/harnesses/vscode) | Preview | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| [Copilot App](/nexus/harnesses/copilot-app) | Preview | Chat Completions | Supports `auto`. Closed models need Provider Keys | Provider Keys only | Not touched | Yes |
| [Copilot CLI](/nexus/harnesses/copilot-cli) | Preview | Chat Completions | Supports `auto`. Closed models need a key saved with `nexus auto`, Provider Keys, or manual setup | A key saved with `nexus auto`, or headers in manual setup | Not touched | Yes |
| **Cowork** | | | | | | |
| [ChatGPT desktop app](/nexus/harnesses/chatgpt) | Generally available | Responses | Supports `auto` | Same as Codex | Same as Codex | Yes |
| [Claude Desktop](/nexus/harnesses/claude-desktop) | Preview | Messages | Supports `auto`. Closed models need a key saved with `nexus auto` or Provider Keys | A key saved with `nexus auto`, added to `auto` turns by the local proxy | `on` imports your connectors. It includes your claude.ai organization's when the Claude Code CLI is installed and signed in. `nexus claude-desktop mcp sync` imports ones you add later | No |

Nexus Auto is not available on Microsoft Foundry, and Foundry support differs by harness. See the compatibility matrix in [Nexus for Microsoft Foundry](/nexus/microsoft-foundry#choose-a-path), including [Claude Code through a gateway](/nexus/microsoft-foundry#claude-code-through-a-gateway).

### Claude Code

Moved to [Claude Code](/nexus/harnesses/claude-code).

### Claude Agent SDK

Moved to [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk).

### Codex

Moved to [Codex](/nexus/harnesses/codex).

### OpenCode

Moved to [OpenCode](/nexus/harnesses/opencode).

### Pi

Moved to [Pi](/nexus/harnesses/pi).

### DeepSeek Harness

Moved to [DeepSeek Harness](/nexus/harnesses/deepseek).

### Cursor IDE

Moved to [Cursor IDE](/nexus/harnesses/cursor).

### VS Code

Moved to [VS Code](/nexus/harnesses/vscode).

### Copilot App

Moved to [Copilot App](/nexus/harnesses/copilot-app).

### Copilot CLI

Moved to [Copilot CLI](/nexus/harnesses/copilot-cli).

### ChatGPT desktop app

Moved to [ChatGPT desktop app](/nexus/harnesses/chatgpt).

### Claude Desktop

Moved to [Claude Desktop](/nexus/harnesses/claude-desktop).
