---
title: "Quickstart"
source: https://docs.fireworks.ai/nexus/quickstart
path: nexus/quickstart
---

Connect Nexus to Claude Code, ChatGPT, or another AI tool you already use, in a few minutes.

## Create a Nexus account

Sign up at [nexus.fireworks.ai](https://nexus.fireworks.ai) and choose a [plan](/nexus/plans): Pro, Team, or Enterprise. Nexus accounts are separate from Fireworks platform accounts.

## Set up with Nexus Desktop or Nexus CLI

> [tab] Nexus Desktop
>
> Nexus Desktop connects your tools without the command line.
>
> > [card] [Download Nexus Desktop for macOS](https://nexus.fireworks.ai/desktop/download/darwin-universal/latest)
> >
> > Universal build for Apple silicon and Intel Macs. Linux and Windows are coming soon.
>
> 1. Open the `.dmg` and drag Nexus to your Applications folder.
> 2. Sign in with your Nexus account.
> 3. Turn on each tool you use, then restart that tool.
>
> To restore your original setup, turn the tool off in [Nexus Desktop](/nexus/desktop) and restart it.
>
> ![Nexus Desktop Connect screen with an account picker in the sidebar and on and off switches for Claude Desktop, ChatGPT, Claude Code, Codex, Cursor, and other tools](https://mintcdn.com/fireworksai/zB7PRUO6m5X1UU4P/images/nexus/nexus-desktop-connect.png?fit=max\&auto=format\&n=zB7PRUO6m5X1UU4P\&q=85\&s=0439d0837530dae934cdbd68702cea47)
>
> Nexus Desktop: turn on Fireworks in each app

> [tab] Nexus CLI
>
> ```bash wrap theme={null}
> curl -fsSL https://nexus.fireworks.ai/install.sh | bash
> ```
>
> You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.
>
> ```bash wrap theme={null}
> nexus login
> ```
>
> Sign in with your browser, or paste a Fireworks API key (`fw_...`).
>
> Then choose your tool under [Connect your tool](#connect-your-tool) and follow its setup steps.

### Supported systems

| | macOS | Linux | Windows |
| - | - | - | - |
| **Nexus Desktop** | Yes | Coming soon | Coming soon |
| **Nexus CLI** | Yes | Yes. Claude Desktop is coming soon | Limited. Install and run it from Git Bash. Claude Desktop isn't supported |

## Featured connections

> [card] [Claude Code CLI](/nexus/harnesses/claude-code)
>
> Nexus Auto sends each turn to an open model or an Anthropic model. Anthropic turns use your Claude login.

> [card] [ChatGPT](/nexus/harnesses/chatgpt)
>
> Nexus Auto appears next to your ChatGPT models. The same connection sets up the Codex CLI.

### Code

> [card] [Claude Code CLI](/nexus/harnesses/claude-code)

> [card] [Claude Agent SDK](/nexus/harnesses/claude-code#claude-agent-sdk)

> [card] [Codex CLI](/nexus/harnesses/codex)

> [card] [OpenCode](/nexus/harnesses/opencode)

> [card] [Pi](/nexus/harnesses/pi)

> [card] [DeepSeek Harness](/nexus/harnesses/deepseek)

> [card] [Cursor IDE](/nexus/harnesses/cursor)

> [card] [VS Code](/nexus/harnesses/vscode)

> [card] [Copilot App](/nexus/harnesses/copilot-app)

> [card] [Copilot CLI](/nexus/harnesses/copilot-cli)

### Cowork

> [card] [ChatGPT](/nexus/harnesses/chatgpt)

> [card] [Claude Desktop (Limited)](/nexus/harnesses/claude-desktop)
>
> Opens a separate workspace without your claude.ai chats, connectors, or skills.
