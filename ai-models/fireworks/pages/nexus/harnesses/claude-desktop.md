---
title: "Claude Desktop"
source: https://docs.fireworks.ai/nexus/harnesses/claude-desktop
path: nexus/harnesses/claude-desktop
---

Run Claude Desktop's Chat, Cowork, and Code on Fireworks models with the Nexus CLI, and manage connectors in third-party mode.

Nexus CLI runs Claude Desktop's Chat, Cowork, and Code on Fireworks models. It runs on macOS and Linux and needs a stored credential from `nexus login`. Linux support is unofficial: Anthropic documents third-party mode for macOS and Windows, but the Linux build uses the same mechanism. On Linux, `on` needs a systemd user session. **Quit and reopen Claude Desktop after `on` or `off`.**

PreviewAnthropic MessagesNative web searchmacOS and Linux

Claude Desktop has no manual setup. Use the Nexus CLI.

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

**2. Connect Claude Desktop**

```bash wrap theme={null}
nexus claude-desktop on
nexus claude-desktop status
```

**3. Reopen and pick a model**

Reopen Claude Desktop. The picker starts on `auto`, followed by the Fireworks models, in place of your claude.ai subscription models.

![Claude Desktop model picker in Cowork showing Auto selected, then Kimi K3 Fast, Kimi K3, MiniMax M3, GLM 5.3 Fast, GLM 5.3, and DeepSeek V4.1 Flash](https://mintcdn.com/fireworksai/DBOQdoU3Q63xUkRQ/images/nexus/claude-desktop-model-picker.png?fit=max\&auto=format\&n=DBOQdoU3Q63xUkRQ\&q=85\&s=2246cd8dd91fd185679de3ad756f9009)

> [!TIP]
>
> The picker starts on `auto`, followed by the Fireworks models.

`off` puts your previous setup back, including your claude.ai models.

## Use Nexus Auto

The picker lists `auto` and the Fireworks models. In Claude Desktop, `auto` uses Fireworks open models only, and there's no local provider key to set. To pick between Anthropic models and open models for each turn, use Nexus Auto in [Claude Code](/nexus/harnesses/claude-code).

## MCP and tools

Third-party mode hides the in-app connector browser, so you manage connectors with Nexus CLI. See [Connectors](#connectors).

Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results, with no MCP server or search service to set up.

## Connectors

Claude Desktop's third-party mode hides the in-app connector browser. Manage connectors with Nexus CLI instead:

* `on` imports the connectors you already use, from Desktop session history, your previous Desktop config, and your claude.ai organization's connector registry.
* `mcp sync` also adds connectors from your claude.ai organization when the Claude Code CLI is installed and signed in, plus any you added later. Run `nexus claude-desktop mcp sync` when you add a connector later and want it in third-party mode too.
* `nexus claude-desktop mcp add <name> <url>` and `mcp remove <name>` manage entries by hand. Removals stick across syncs.
* Each connector asks you to sign in once the first time you use it after `on`.
* Connector OAuth clients you register are saved in `~/.nexus/claude-desktop/oauth-clients.json`, readable only by you. They survive `off` and `on`.

MCPs that need an OAuth client ID and secret do not move. If you need one of these connectors, [reach out to the team](https://fireworks.ai/contact).

Google-hosted connectors (Gmail, Google Drive, Google Calendar, BigQuery) need a Google OAuth client you own, created as a **Desktop app** client in Google Cloud. One client covers all four:

```bash wrap theme={null}
nexus claude-desktop mcp add gmail https://gmailmcp.googleapis.com/mcp/v1 \
  --client-id "<ID>.apps.googleusercontent.com" --client-secret "<SECRET>"
```

The hosted Figma connector does not work in third-party mode. Turn on the Figma desktop app's local server in Dev Mode, then run `nexus claude-desktop mcp add figma-desktop http://127.0.0.1:3845/mcp`.

## Skills and plugins

`on` copies your custom skills and plugins once. Run `nexus claude-desktop on` again to copy ones you add later. Changes you make while connected do not copy back.

## What stays with your claude.ai subscription

Third-party mode does not show your claude.ai chats, projects, artifacts, memory, or scheduled tasks. Nothing is deleted. Run `nexus claude-desktop off` and reopen Claude Desktop to get them back.

| claude.ai item | While connected |
| - | - |
| Chats | Hidden. New chats start empty. |
| Projects | Hidden. You can create new projects. |
| Artifacts | Hidden in the app. New artifacts save as files in `~/Claude/`. |
| Memory | Not carried over. New memory builds up on this computer. |
| Scheduled tasks | Not carried over. You can create new ones. |

New work while connected:

* Chats, projects, artifacts, and memory save only on this computer. They do not appear on claude.ai web or mobile, and you cannot share them.
* Scheduled tasks run only while the computer is awake. A missed run starts when it wakes.
* Chat cannot search past chats and does not get nightly memory summaries. Chat uses memory only inside a project.
* Voice mode is not available.

Anthropic lists these limits in its [third-party feature matrix](https://claude.com/docs/third-party/claude-desktop/feature-matrix) and [local data guide](https://claude.com/docs/third-party/claude-desktop/data-storage).

## Troubleshooting

* `status` shows the local gateway is not responding: run `nexus claude-desktop on` to restart it.
* Models are missing from the picker: run `on` once while online, then restart Claude Desktop.
* The Code tab says the API key was rejected: run `on` again to refresh the key from your stored credential.
* A connector sign-in error won't clear: `mcp remove` it, then `mcp add` it again with your own OAuth client (Google) or the local server (Figma).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> * `on` writes a third-party inference provider profile, Claude Desktop's own supported mechanism. The profile points at a small local gateway that Nexus CLI runs as a background service: a launchd agent on macOS, or a systemd user unit on Linux. It starts at login and restarts after a crash.
> * `on` copies your custom skills and plugins into third-party mode. It never overwrites a file that is already there. Conversations stay in the mode they were made in.
> * `off` restores your previous provider profile and the device settings Nexus CLI changed, then removes the local gateway service. Nothing of yours is deleted.
