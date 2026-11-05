---
title: "Nexus CLI"
source: https://docs.fireworks.ai/nexus/cli
path: nexus/cli
---

Connect Claude Code, ChatGPT, Codex, Cursor IDE, VS Code, Copilot, and more to Fireworks with one Nexus CLI command, and undo it with one more.

[Nexus CLI](https://github.com/fw-ai-external/nexus-cli) is an open-source command-line tool that connects your coding harness to Fireworks models.

* It rewrites your harness settings to call Fireworks.
* It adds Nexus Auto to the harness's model picker.
* It restores your original settings when you turn it off.

Nexus CLI was formerly FireConnect. If you still use FireConnect, run `fireconnect upgrade` once to [upgrade](#upgrading-from-fireconnect).

* Enterprise accounts also get general access to open models on Fireworks serverless.
* You don't host a service or edit config files by hand. Claude Desktop is the one harness that also runs a small local helper on your machine.
* After the rename, the command is `nexus`, settings live in `~/.nexus`, and the installer is at `nexus.fireworks.ai`. Re-running the installer also upgrades from FireConnect. Settings and connected harnesses carry over.

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

Alternative installer:

```bash wrap theme={null}
curl -fsSL \
  https://raw.githubusercontent.com/fw-ai-external/nexus-cli/main/install.sh \
  | bash
```

**2. Connect a harness**

```bash wrap theme={null}
nexus claude
```

Replace `claude` with your harness:

| Harness | Command |
| - | - |
| [Claude Code](/nexus/harnesses/claude-code), [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk) | `nexus claude` |
| [Claude Desktop](/nexus/harnesses/claude-desktop) | `nexus claude-desktop on` |
| [Codex CLI](/nexus/harnesses/codex) | `nexus codex` |
| [ChatGPT desktop app](/nexus/harnesses/chatgpt) | `nexus chatgpt` |
| [OpenCode](/nexus/harnesses/opencode) | `nexus opencode` |
| [Pi](/nexus/harnesses/pi) | `nexus pi` |
| [DeepSeek Harness](/nexus/harnesses/deepseek) | `nexus deepseek` |
| [Cursor IDE](/nexus/harnesses/cursor) | `nexus cursor` |
| [VS Code](/nexus/harnesses/vscode) | `nexus vscode` |
| [Copilot App](/nexus/harnesses/copilot-app) | `nexus copilot-app` |
| [Copilot CLI](/nexus/harnesses/copilot-cli) | `nexus copilot-cli` |

> [!WARNING]
>
> Quit desktop apps before you connect them or run `off`, then reopen them: Cursor IDE, VS Code, the Copilot App, the ChatGPT and Codex apps, and Claude Desktop. A running app can save over the new settings or keep showing the old models.

* Nexus CLI checks for a running Cursor IDE, VS Code, Copilot App, or ChatGPT app and waits until it's quit. `--force` writes anyway, which isn't recommended. The ChatGPT app shares `~/.codex/config.toml` with Codex and loads the model catalog only at launch.
* Nexus CLI doesn't check for a running Claude Desktop, but Claude Desktop only picks up the change after it's quit and reopened.
* Terminal harnesses (Claude Code, Codex CLI, OpenCode, Pi, Copilot CLI, DeepSeek Harness) need a new session, not a quit.
* Harnesses group into Code (Claude Code, Claude Agent SDK, Codex CLI, OpenCode, Pi, DeepSeek Harness, Cursor IDE, VS Code, Copilot App, Copilot CLI) and Cowork (ChatGPT desktop app, Claude Desktop).
* Each harness page in [Coding Harnesses](/nexus/harnesses) has the details.

**3. Restart and check**

Restart the harness, or start a new session. Then run `nexus claude status` (use your harness name). It shows the provider, where the key comes from, and the configured model.

To undo, run `nexus <harness> off`. To configure a harness yourself, follow [Manual setup](/nexus/manual-setup).

## Connect and restore

* **`nexus <harness>`** connects a harness and saves a snapshot of its settings.
* **`nexus <harness> off`** restores your original settings.
* **`nexus status`** lists every harness and whether it's connected.
* **`nexus update`** updates Nexus CLI and your connected harnesses. Restart each harness it names.

- Connect rewrites the harness config to call Fireworks and saves the snapshot under `~/.nexus/`. It only connects a harness that's installed on this machine. If yours is installed somewhere Nexus CLI doesn't look, pass `--skip-install-check`.
- `off` restores file-based harnesses from that snapshot, byte for byte. For IDE databases, it removes only the settings and models Nexus CLI added.
- `nexus status` also shows whether each harness is installed, and the key storage backend without revealing the key.
- `nexus update` keeps the model you picked. `nexus upgrade` still works. See what changed in [Release Notes](/nexus/release-notes).
- **Your key is stored once.** `nexus login` saves your Fireworks key in the OS keychain, or in an encrypted file when no keychain is available. Some harnesses need the key in their own config. Nexus CLI copies it there and makes the file readable only by you.
- For update and uninstall commands, see the [CLI Reference](/nexus/cli-reference).

## Choose a model

Connecting starts the harness on `auto`. On Enterprise, use `--model` to add or select a specific model, then restart the harness:

```bash wrap theme={null}
nexus opencode --model glm-latest
```

* Connecting registers coding-ready Fireworks models, including `auto`.
* Restart or reopen the harness after you change a model. Browse model IDs with `nexus model list`. See [Open Models](/nexus/open-models) for aliases and pinned versions, and [Coding Harnesses](/nexus/harnesses) for app-specific rules.
* Nexus Auto picks between open models and the Anthropic or OpenAI models you have access to, one turn at a time. [Nexus Auto](/nexus/auto#nexus-cli) covers the `nexus auto` command and which credentials each harness can send.

## MCP servers and web search

* MCP servers are unchanged, and `nexus <harness> off` leaves them in place. The exception is Claude Desktop, which manages them as [connectors](/nexus/harnesses/claude-desktop#connectors).
* Tool search stays on, so large MCP tool sets load on demand.
* [Web search](/nexus/auto#web-search) works through Fireworks in Claude Code, Claude Desktop, Codex, and the ChatGPT desktop app without additional configuration.

- Claude Desktop's third-party mode hides the connector browser, so Nexus CLI imports your connectors, and you manage them with `nexus claude-desktop mcp`.
- In Claude Code, Nexus CLI sets `ENABLE_TOOL_SEARCH`. In Codex and the ChatGPT desktop app, it turns on tool search for every model.

## Upgrading from earlier versions

### Upgrading from FireConnect

Run `fireconnect upgrade` once, or re-run the installer. Your command, settings, and connected harnesses move to Nexus CLI.

* `~/.fireconnect` moves to `~/.nexus`, and the old path stays as a link.
* Environment variables are now `NEXUS_*`. `FIRECONNECT_*` still works, but rename them in your scripts and shell profile.
* A harness on a FireRouter model moves to `auto`. See [Nexus Auto](/nexus/auto).
* If `~/.nexus` already exists and Nexus CLI didn't create it, the update stops before changing anything.

### Per harness

| Harness | If you connected with | Run |
| - | - | - |
| Codex, ChatGPT desktop app | FireConnect 0.9.9 or earlier | `nexus update`, then restart Codex or reopen the app |
| DeepSeek Harness | FireConnect before 0.9.8 | `nexus deepseek` once |
| OpenCode | An earlier version, with OpenCode v2's `providers` map | `nexus update` |
| Claude Code | FireConnect before 0.9.7 | `nexus update` |

* **Codex and ChatGPT desktop app:** `nexus codex` (`nexus chatgpt` for the app) also works instead of `nexus update`. Afterward, MCP and app connector tools load through Codex's tool search on every model. If Codex was on FireRouter (`firerouter` or a route such as `firerouter/opus`), `nexus update` moves that selection to `auto`. Other models stay as they are. Run `codex login` if Codex asks.
* **DeepSeek Harness:** after `nexus deepseek`, `dsh` 0.1.7 and later stop asking for a DeepSeek key.
* **OpenCode:** after `nexus update`, the Fireworks models appear in `/models`.
* **Claude Code:** versions before 0.9.7 installed the `fireworks-websearch` MCP server. `nexus update` removes it and leaves your other MCP servers in place. See [Web search](/nexus/auto#web-search).
