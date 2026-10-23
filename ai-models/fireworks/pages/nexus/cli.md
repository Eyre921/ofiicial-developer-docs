---
title: "Nexus CLI"
source: https://docs.fireworks.ai/nexus/cli
path: nexus/cli
---

Connect Claude Code, ChatGPT, Codex, Cursor IDE, VS Code, Copilot, and more to Fireworks with one Nexus CLI command, and undo it with one more.

[Nexus CLI](https://github.com/fw-ai/nexus-cli) is the easiest way to use Fireworks models in the coding harness you already use. It's an open-source CLI that:

* Rewrites your harness settings to call Fireworks.
* Adds Fireworks models to the harness's model picker.
* Restores your original settings when you turn it off.

You don't host a service or edit config files by hand. Claude Desktop is the one harness that also runs a small local helper on your machine.

> [!NOTE]
>
> Nexus CLI was formerly called FireConnect. The command is now `nexus`, settings live in `~/.nexus`, and the installer is at `nexus.fireworks.ai`. Still on FireConnect? Run `fireconnect upgrade` once, or re-run the installer. Your settings and connected harnesses carry over. See [Upgrading from FireConnect](#upgrading-from-fireconnect).

## Connections

### Code

> **[Claude Code](/nexus/harnesses/claude-code)**

> **[Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk)**

> **[Codex CLI](/nexus/harnesses/codex)**

> **[OpenCode](/nexus/harnesses/opencode)**

> **[Pi](/nexus/harnesses/pi)**

> **[DeepSeek Harness](/nexus/harnesses/deepseek)**

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

You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks API key (`fw_...`).

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

Replace `claude` with your harness: `chatgpt`, `codex`, `opencode`, `pi`, `cursor`, `vscode`, `copilot-app`, `copilot-cli`, or `deepseek`. Claude Desktop uses `nexus claude-desktop on`. Each harness page in [Coding Harnesses](/nexus/harnesses) has the details.

Quit Cursor IDE, VS Code, or the Copilot App before you connect them. A running app saves over the new settings.

**3. Restart and check**

Restart the harness, or start a new session. Then run:

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

* **Connect** (`nexus <harness>`) rewrites the harness config to call Fireworks and saves a snapshot under `~/.nexus/`. It only connects a harness that's installed on this machine. If yours is installed somewhere Nexus CLI doesn't look, pass `--skip-install-check`.
* **`off`** (`nexus <harness> off`) restores file-based harnesses from that snapshot, byte for byte. For IDE databases, it removes only the settings and models Nexus CLI added.
* **`nexus status`** lists every harness, whether it's connected, and whether it's installed.
* **`nexus update`** updates Nexus CLI and brings connected harnesses up to date. It keeps the model you picked. Restart each harness the update output names. `nexus upgrade` still works. See what changed in [Release Notes](/nexus/release-notes).
* **Your key is stored once.** `nexus login` saves your Fireworks key in the OS keychain, or in an encrypted file when no keychain is available. Some harnesses need the key in their own config. Nexus CLI copies it there and makes the file readable only by you. Run `nexus status` to see the storage backend without revealing the key.

## Choose a model

Connecting registers coding-ready Fireworks models, including `auto`, and starts the harness on `auto`. Use `--model` to add or select a specific model:

```bash wrap theme={null}
nexus opencode --model glm-latest
```

Restart or reopen the harness after you change a model. Browse model IDs with `nexus model list`. See [Open Models](/nexus/open-models) for aliases and pinned versions, and [Coding Harnesses](/nexus/harnesses) for app-specific rules.

Nexus Auto picks between open models and the Anthropic or OpenAI models you have access to, one turn at a time. [Nexus Auto](/nexus/auto#nexus-cli) covers the `nexus auto` command and which credentials each harness can send.

Web search works through Fireworks with no extra setup. See [Web Search](/nexus/web-search) for which harnesses support it.

## MCP servers

> **Your servers stay**
>
> Nexus CLI keeps every MCP server you configured, and
> `nexus <harness> off` leaves them in place. Claude Desktop is the
> exception. Its third-party mode hides the connector browser, so
> Nexus CLI imports your connectors, and you manage them with
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

Run `fireconnect upgrade` once, or re-run the installer. Your command, settings, and connected harnesses move to Nexus CLI:

* `~/.fireconnect` moves to `~/.nexus`, and the old path stays as a link.
* Environment variables are now `NEXUS_*`. `FIRECONNECT_*` still works, but rename them in your scripts and shell profile.
* A harness on a FireRouter model moves to `auto`. See [Nexus Auto](/nexus/auto).
* If `~/.nexus` already exists and Nexus CLI didn't create it, the update stops before changing anything.

### Codex and ChatGPT desktop app

* Connected with FireConnect 0.9.9 or earlier? Run `nexus update`, or `nexus codex` (`nexus chatgpt` for the app). Then restart Codex or reopen the app. MCP and app connector tools then load through Codex's tool search on every model.
* If Codex was on FireRouter (`firerouter` or a route such as `firerouter/opus`), `nexus update` moves that selection to `auto`. Other models stay as they are. Run `codex login` if Codex asks.

### DeepSeek Harness

Connected before FireConnect 0.9.8? Run `nexus deepseek` once, so `dsh` 0.1.7 and later stop asking for a DeepSeek key.

### OpenCode

If your `opencode.json` uses OpenCode v2's `providers` map and you connected with an earlier version, run `nexus update`. The Fireworks models then appear in `/models`.

### Claude Code

FireConnect versions before 0.9.7 installed the `fireworks-websearch` MCP server for Claude Code. `nexus update` removes it and leaves your other MCP servers in place. See [Web Search](/nexus/web-search#upgrade-from-the-retired-mcp).

## Update and uninstall

For update and uninstall commands, see the [CLI Reference](/nexus/cli-reference).
