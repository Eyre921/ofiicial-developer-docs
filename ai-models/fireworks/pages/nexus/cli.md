---
title: "Nexus CLI"
source: https://docs.fireworks.ai/nexus/cli
path: nexus/cli
---

Point the Claude Code CLI, ChatGPT, Claude Desktop, Codex, OpenCode, Cursor IDE, VS Code, and Copilot at Fireworks with one Nexus CLI command

[Nexus CLI](https://github.com/fw-ai/nexus-cli) is the easiest way to use Fireworks models in the coding harness you already use. It is an open-source CLI that rewrites your harness settings to call Fireworks, adds Fireworks models to the model picker, and restores your original settings when you turn it off. You do not need to host a service or edit config files by hand.

> [!NOTE]
>
> Nexus CLI was formerly called FireConnect. The command is now `nexus`, settings live in `~/.nexus`, and the installer is at `nexus.fireworks.ai`. If you still have FireConnect installed, run `fireconnect upgrade` once or re-run the installer, and your command, settings, and connected harnesses migrate automatically.

## Connections

### Code

> **[Claude Code](/nexus/harnesses/claude-code)**

> **[Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk)**

> **[Codex CLI](/nexus/harnesses/codex)**

> **[OpenCode](/nexus/harnesses/opencode)**

> **[Pi](/nexus/harnesses/pi)**

> **[DeepSeek](/nexus/harnesses/deepseek)**

> **[Cursor IDE](/nexus/harnesses/cursor)**

> **[VS Code](/nexus/harnesses/vscode)**

> **[Copilot App](/nexus/harnesses/copilot-app)**

> **[Copilot CLI](/nexus/harnesses/copilot-cli)**

### Cowork

> **[ChatGPT desktop app](/nexus/harnesses/chatgpt)**

> **[Claude Desktop](/nexus/harnesses/claude-desktop)**

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

> **Alternative installer**
>
> ```bash wrap theme={null}
> curl -fsSL \
>   https://raw.githubusercontent.com/fw-ai/nexus-cli/main/install.sh \
>   | bash
> ```

**2. Connect a harness**

```bash wrap theme={null}
nexus claude
```

Replace `claude` with any harness from [Coding Harnesses](/nexus/harnesses).

**3. Restart and check**

```bash wrap theme={null}
nexus claude status
```

> [!TIP]
>
> `status` shows the provider, where the key comes from, and the configured model.

> [!TIP]
>
> **Rather configure it yourself?** See [Manual setup](/nexus/manual-setup)
> for when to use it and what changes.

## Connect and restore

* **Connect** rewrites the harness config to call Fireworks and saves a snapshot under `~/.nexus/`.
* **`off`** restores file-based harnesses from that snapshot byte-for-byte. For IDE databases, it removes the settings and models Nexus CLI added.
* **`nexus upgrade`** updates Nexus CLI and brings connected harnesses up to date, keeping the model you picked. Restart each harness the upgrade output names.
* **Sign-in credentials and harness configurations are stored separately.** `nexus login` saves your credential through Nexus CLI's secret store. If a harness requires the key in its own configuration, Nexus CLI copies it there and restricts the file permissions. Run `nexus status` to see the active storage backend without revealing the key.

## Choose a model

Connecting registers coding-ready Fireworks models, including `auto`. Use `--model` to add or select a specific model:

```bash wrap theme={null}
nexus opencode --model glm-latest
```

Restart or reopen the harness after changing a model. Browse IDs with `nexus model list`. See [Open Models](/nexus/open-models) for aliases and pinned versions, and [Coding Harnesses](/nexus/harnesses) for app-specific rules.

To pick between open models and the Anthropic or OpenAI models you have access to for each turn, use Nexus Auto. [Nexus Auto](/nexus/auto#nexus-cli) covers the Nexus CLI command and the credentials each harness can send.

Web search works through Fireworks with no extra setup. See [Web Search](/nexus/web-search) for which harnesses support it.

## MCP servers

> **Your servers stay**
>
> Nexus CLI keeps every MCP server you configured, and
> `nexus <harness> off` leaves them in place. Claude Desktop is the
> exception. Third-party mode hides the connector browser, so Nexus CLI
> imports those connectors and you manage them with
> `nexus claude-desktop mcp`. See
> [Connectors](/nexus/harnesses/claude-desktop#connectors).

> **Tool search stays on**
>
> In Claude Code, Nexus CLI sets `ENABLE_TOOL_SEARCH`. In Codex and the
> ChatGPT desktop app, it turns on tool search for every model. Large
> MCP tool sets still load on demand.

> **[Web search is built in](/nexus/web-search)**
>
> Native web search works through Fireworks in Claude Code, Claude Desktop,
> Codex, and the ChatGPT desktop app.

## Upgrading from earlier versions

### Upgrading from FireConnect

Nexus CLI was formerly called FireConnect. The command is now `nexus`, settings live in `~/.nexus`, and the installer is at `nexus.fireworks.ai`. Run `fireconnect upgrade` once or re-run the installer, and your command, settings, and connected harnesses migrate automatically.

### Codex and ChatGPT desktop app

* Connected with FireConnect 0.9.9 or earlier? Run `nexus upgrade` or `nexus codex` (`nexus chatgpt` for the app), then restart Codex or reopen the app. MCP and app connector tools then load through Codex's tool search on every model.
* If Codex was on FireRouter (`firerouter` or a route such as `firerouter/opus`), `nexus upgrade` moves that selection to `auto`. Other models stay as they are. Run `codex login` if Codex asks.

### DeepSeek Harness

Connected before FireConnect 0.9.8? Run `nexus deepseek` once so `dsh` 0.1.7 and later stop asking for a DeepSeek key.

### OpenCode

If your `opencode.json` uses OpenCode v2's `providers` map and you connected with an earlier version, run `nexus upgrade` so the Fireworks models appear in `/models`.

### Claude Code

FireConnect versions before 0.9.7 installed the `fireworks-websearch` MCP for Claude Code. `nexus upgrade` removes it and leaves your other MCP servers in place. See [Web Search](/nexus/web-search#upgrade-from-the-retired-mcp).

## Upgrade and uninstall

For upgrade and uninstall commands, see the [CLI Reference](/nexus/cli-reference).
