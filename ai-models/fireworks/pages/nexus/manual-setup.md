---
title: "Manual setup (advanced)"
source: https://docs.fireworks.ai/nexus/manual-setup
path: nexus/manual-setup
---

Configure a coding harness for Fireworks by hand, without installing the Nexus CLI.

The recommended setup is the [Nexus CLI](/nexus/cli), which writes your harness settings and restores the originals with `nexus <harness> off`. Use manual setup when you can't install a CLI or need settings the Nexus CLI doesn't write.

## When to use manual setup

* You can't install the Nexus CLI.
* You manage harness configs yourself, through dotfiles or a team rollout.
* You want Nexus Auto to use Anthropic or OpenAI models without [Provider Keys](/nexus/provider-keys) or the Nexus CLI.
* You want to review every setting that changes.

- The Nexus CLI needs Node.js 22 or later, `git`, and `bash`, and runs an install script.
- Without Provider Keys or the Nexus CLI, you add the `x-anthropic-api-key` or `x-openai-api-key` header yourself. With the Nexus CLI, `nexus auto --anthropic-api-key` or `--openai-api-key` writes them for you.

## What changes without the Nexus CLI

The harness calls the same Fireworks endpoints with your own API key. You take over the tasks that the Nexus CLI otherwise performs.

| | With the Nexus CLI | With manual setup |
| - | - | - |
| Fireworks models in the picker | Added automatically | Set the model ID in your config |
| Anthropic model turns in Claude Code | Paid by your Claude login | Need an Anthropic [Provider Key](/nexus/provider-keys) or an `x-anthropic-api-key` header |
| MCP tool search | Turned on | Claude Code: add `ENABLE_TOOL_SEARCH`. Codex: write a model catalog that sets `supports_search_tool` (see [What the Nexus CLI writes](/nexus/harnesses/codex#what-the-nexus-cli-writes)) |
| Session cost status line (Claude Code) | Installed | Not available |
| Anthropic and OpenAI keys for Nexus Auto | Saved once with `nexus auto` and written into each harness that can send them | Add `x-anthropic-api-key` or `x-openai-api-key` headers to each config |
| Undo | `nexus <harness> off` | Restore your own backup |
| Updates | `nexus update` refreshes connected harnesses | Update your configs yourself |

## Before you start

1. Create an API key in [Nexus settings](https://nexus.fireworks.ai/settings/api-keys) and export it:

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

Follow the manual setup section for your harness:

* [Claude Code](/nexus/harnesses/claude-code#manual-setup-advanced)
* [Codex](/nexus/harnesses/codex#manual-setup-advanced)
* [ChatGPT desktop app](/nexus/harnesses/chatgpt#manual-setup-advanced)
* [OpenCode](/nexus/harnesses/opencode#manual-setup-advanced)
* [Pi](/nexus/harnesses/pi#manual-setup-advanced)
* [Cursor IDE](/nexus/harnesses/cursor#manual-setup-advanced)
* [VS Code](/nexus/harnesses/vscode#manual-setup-advanced)
* [Copilot App](/nexus/harnesses/copilot-app#manual-setup-advanced)
* [Copilot CLI](/nexus/harnesses/copilot-cli#manual-setup-advanced)
* [DeepSeek Harness](/nexus/harnesses/deepseek#manual-setup-advanced)

The [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk) reads your Claude Code settings, so set up Claude Code first. [Claude Desktop](/nexus/harnesses/claude-desktop) (Limited) has no manual setup and requires the Nexus CLI.

## Use Nexus Auto with manual setup

For Nexus Auto to use an Anthropic or OpenAI model, either:

* The harness sends an `x-anthropic-api-key` or `x-openai-api-key` header, or
* Your account has [Provider Keys](/nexus/provider-keys).

Cursor IDE and the Copilot App can't send extra headers, so they need Provider Keys. The [harness setup builder](/nexus/auto#nexus-cli) generates a config with the headers included.
