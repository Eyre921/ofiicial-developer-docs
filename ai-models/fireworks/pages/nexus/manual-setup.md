---
title: "Manual setup (advanced)"
source: https://docs.fireworks.ai/nexus/manual-setup
path: nexus/manual-setup
---

Configure a coding harness for Fireworks by hand, without installing the Nexus CLI.

The Nexus CLI writes your harness settings for you and undoes them with one command. Most people should use it. Manual setup is for when you can't install a CLI, or when you need settings the Nexus CLI doesn't write.

## When to use manual setup

* You can't install the Nexus CLI. It needs Node.js 22 or later, `git`, and `bash`, and runs an install script.
* You manage harness configs yourself, through dotfiles or a team rollout.
* You want Nexus Auto to use Anthropic or OpenAI models without [Provider Keys](/nexus/provider-keys) or the Nexus CLI. You add the `x-anthropic-api-key` or `x-openai-api-key` header yourself. With the Nexus CLI, `nexus auto --anthropic-api-key` or `--openai-api-key` writes them for you.
* You want to review every setting that changes.

## What changes without the Nexus CLI

You point the harness at the same Fireworks endpoints, with your own API key. Some things the Nexus CLI normally handles become your job.

| | With the Nexus CLI | With manual setup |
| - | - | - |
| Fireworks models in the picker | Added for you | Set the model ID in your config |
| Anthropic model turns in Claude Code | Paid by your Claude login | Need an Anthropic [Provider Key](/nexus/provider-keys) or an `x-anthropic-api-key` header |
| MCP tool search | Turned on | Claude Code: add `ENABLE_TOOL_SEARCH`. Codex: write a model catalog that sets `supports_search_tool` (see [What the Nexus CLI writes](/nexus/harnesses/codex#what-the-nexus-cli-writes)) |
| Session cost status line (Claude Code) | Installed | Not available |
| Anthropic and OpenAI keys for Nexus Auto | Saved once with `nexus auto` and written into each harness that can send them | Add `x-anthropic-api-key` or `x-openai-api-key` headers to each config |
| Undo | `nexus <harness> off` | Restore your own backup |
| Updates | `nexus update` refreshes connected harnesses | Update your configs yourself |

## Before you start

1. Create an API key in [Fireworks settings](https://app.fireworks.ai/settings/users/api-keys) and export it:

   ```bash wrap theme={null}
   export FIREWORKS_API_KEY="fw_..."
   ```

2. Back up the config file you're about to edit.

3. Use these endpoints:

   | API | Base URL to configure | Full endpoint | Typical clients |
   | - | - | - | - |
   | Anthropic Messages | `https://api.fireworks.ai/inference` | `https://api.fireworks.ai/inference/v1/messages` | Anthropic SDK, Claude Code |
   | OpenAI Chat Completions | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/chat/completions` | OpenAI SDK, Fireworks SDK, most gateways and harnesses |
   | OpenAI Responses | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/responses` | OpenAI SDK, Codex |

   Anthropic-style clients add `/v1/messages` to the base URL themselves, so their base URL ends at `/inference`.

Use any model ID from [Open Models](/nexus/open-models), such as `glm-latest`, or `auto` for [Nexus Auto](/nexus/auto).

## Set up your harness

| Harness | Status | Manual setup |
| - | - | - |
| [Claude Code](/nexus/harnesses/claude-code) | Generally available | [Manual setup tab](/nexus/harnesses/claude-code#manual-setup-advanced) |
| [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk) | Preview | Reads your Claude Code settings. Set up Claude Code first. |
| [Claude Desktop](/nexus/harnesses/claude-desktop) | Preview | Not available. Use the Nexus CLI. |
| [Codex](/nexus/harnesses/codex) | Generally available | [Manual setup tab](/nexus/harnesses/codex#manual-setup-advanced) |
| [ChatGPT desktop app](/nexus/harnesses/chatgpt) | Generally available | [Manual setup tab](/nexus/harnesses/chatgpt#manual-setup-advanced) |
| [OpenCode](/nexus/harnesses/opencode) | Generally available | [Manual setup tab](/nexus/harnesses/opencode#manual-setup-advanced) |
| [Pi](/nexus/harnesses/pi) | Generally available | [Manual setup tab](/nexus/harnesses/pi#manual-setup-advanced) |
| [Cursor IDE](/nexus/harnesses/cursor) | Preview | [Manual setup tab](/nexus/harnesses/cursor#manual-setup-advanced) |
| [VS Code](/nexus/harnesses/vscode) | Preview | [Manual setup tab](/nexus/harnesses/vscode#manual-setup-advanced) |
| [Copilot App](/nexus/harnesses/copilot-app) | Preview | [Manual setup tab](/nexus/harnesses/copilot-app#manual-setup-advanced) |
| [Copilot CLI](/nexus/harnesses/copilot-cli) | Preview | [Manual setup tab](/nexus/harnesses/copilot-cli#manual-setup-advanced) |
| [DeepSeek Harness](/nexus/harnesses/deepseek) | Generally available | [Manual setup tab](/nexus/harnesses/deepseek#manual-setup-advanced) |

## Use Nexus Auto with manual setup

For Nexus Auto to use an Anthropic or OpenAI model, one of these must be true:

* The harness sends an `x-anthropic-api-key` or `x-openai-api-key` header.
* Your account has [Provider Keys](/nexus/provider-keys).

The [harness setup builder](/nexus/auto#nexus-cli) generates a config with the headers included. Cursor IDE and the Copilot App can't send extra headers, so they need Provider Keys.

## Microsoft Foundry

To configure a harness by hand against Fireworks on Microsoft Foundry, see [Configure a harness manually](/nexus/microsoft-foundry#configure-a-harness-manually).
