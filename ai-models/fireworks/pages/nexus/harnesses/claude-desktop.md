---
title: "Claude Desktop"
source: https://docs.fireworks.ai/nexus/harnesses/claude-desktop
path: nexus/harnesses/claude-desktop
---

Run Claude Desktop's Chat, Cowork, and Code on Fireworks models with the Nexus CLI, and manage connectors in third-party mode.

Claude Desktop is supported on macOS through the Nexus CLI only, with no manual setup. Linux support is coming soon.

> [!WARNING]
>
> **Limited support.** Claude Desktop can't stay signed in to claude.ai while it runs through Nexus. It opens a separate local workspace instead:
>
> * Your claude.ai chats, plugins, and custom skills don't appear.
> * claude.ai connectors aren't available. Nexus CLI brings over the connectors and skills saved on your computer, and each connector asks you to sign in again.
>
> **Nothing is lost.** Run `nexus claude-desktop off` and reopen Claude Desktop to get your main workspace back. For full support, use [Claude Code](/nexus/harnesses/claude-code), [Codex](/nexus/harnesses/codex), or [ChatGPT](/nexus/harnesses/chatgpt).

Support summary:

* Status: Limited
* API the harness speaks to Fireworks: Anthropic Messages
* Nexus Auto: Supported
* Native web search: Supported. Fireworks runs the harness's native web search server-side, with any Fireworks model. See [Web search](/nexus/auto#web-search).
* Platforms: macOS. Linux is coming soon

Requirements:

* A stored credential from `nexus login`.

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

If the Nexus CLI is already installed and signed in, skip to step 2.

**2. Connect Claude Desktop**

```bash wrap theme={null}
nexus claude-desktop on
```

Check the connection with `nexus claude-desktop status`.

**3. Quit, reopen, and pick Nexus Auto**

Quit and reopen Claude Desktop. Nexus Auto appears along with your Claude models.

Nexus Auto's model ID is `auto`. Enterprise accounts also get general access to open models on Fireworks serverless.

To restore your original settings and your claude.ai models, run `nexus claude-desktop off`, then quit and reopen Claude Desktop.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin, or your own saved key. Without either, Nexus Auto serves every turn with Fireworks open models.

- Save your own key with `nexus auto --anthropic-api-key` or `nexus auto --openai-api-key`. Each prompts for the key.
- The local gateway adds a saved key to `auto` turns from the next request. You don't need to run `nexus claude-desktop on` again or restart the app.
- Pinned Fireworks models never get the key.
- `nexus auto --unset anthropic-api-key` stops sending it on the next request.
- After `nexus update`, the local gateway restarts on its own so it runs the new version.

## MCP and tools

* Native web search is supported. Fireworks runs the search server-side, so no search MCP server is required.
* Third-party mode hides the in-app connector browser, so you manage [connectors](#connectors) with Nexus CLI.
* `on` copies your custom skills and plugins once. Run `nexus claude-desktop on` again to copy ones you add later.

- Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results. No search service is needed.
- Skill and plugin changes you make while connected do not copy back.

## Connectors

`on` imports your existing connectors. Each one asks you to sign in once, the first time you use it after `on`.

```bash wrap theme={null}
nexus claude-desktop mcp list
```

Run `nexus claude-desktop mcp sync` after you add a connector outside third-party mode.

* `on` reads Desktop session history and your previous Desktop config. When the Claude Code CLI is installed and signed in to claude.ai, it also reads your organization's connector registry.
* `nexus claude-desktop mcp sync` imports again from the same sources.
* `nexus claude-desktop mcp add <name> <url>` and `mcp remove <name>` manage entries by hand. Removals stick across syncs.
* `nexus claude-desktop mcp list` shows what is set up.
* Your connector setup survives `off` and `on`. OAuth clients you register are saved in `~/.nexus/claude-desktop/oauth-clients.json`, readable only by you.
* Connectors hosted by Anthropic or Google sign in through claude.ai, so Nexus CLI skips them unless you register your own OAuth client. If you need one that has no recipe on this page, [reach out to the team](https://fireworks.ai/contact).
* Google-hosted connectors (Gmail, Google Drive, Google Calendar, BigQuery) need a Google OAuth client you own, created as a **Desktop app** client in Google Cloud. One client covers all four:

```bash wrap theme={null}
nexus claude-desktop mcp add gmail https://gmailmcp.googleapis.com/mcp/v1 \
  --client-id "<ID>.apps.googleusercontent.com" --client-secret "<SECRET>"
```

* The hosted Figma connector does not work in third-party mode. Turn on the Figma desktop app's local server in Dev Mode, then run `nexus claude-desktop mcp add figma-desktop http://127.0.0.1:3845/mcp`.

## What stays with your claude.ai subscription

Your claude.ai chats, projects, artifacts, memory, and scheduled tasks are hidden while connected, but not deleted. New work is saved only on this computer.

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

* **`status` shows the local gateway is not responding:** run `nexus claude-desktop on` to restart it.
* **Models are missing from the picker:** run `on` once while online, then restart Claude Desktop.
* **The Code tab says the API key was rejected:** run `on` again to refresh the key from your stored credential.

- A connector sign-in error won't clear: `mcp remove` it, then `mcp add` it again with your own OAuth client (Google) or the local server (Figma).

## What the Nexus CLI writes

* `on` writes a third-party inference provider profile, Claude Desktop's own supported mechanism. The profile points at a small local gateway that Nexus CLI runs as a background service. It starts at login and restarts after a crash.
* The service is a launchd agent (`~/Library/LaunchAgents/ai.fireworks.nexus.claude-desktop-shim.plist`).
* Nexus CLI keeps its Claude Desktop state, connector list, and OAuth clients in `~/.nexus/claude-desktop/`.
* `on` copies your custom skills and plugins into third-party mode. It never overwrites a file that is already there. Conversations stay in the mode they were made in.
* `off` restores your previous provider profile and the device settings Nexus CLI changed, then removes the local gateway service. Nothing of yours is deleted.
