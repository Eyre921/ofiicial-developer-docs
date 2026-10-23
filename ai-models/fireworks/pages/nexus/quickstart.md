---
title: "Quickstart"
source: https://docs.fireworks.ai/nexus/quickstart
path: nexus/quickstart
---

Connect Nexus to Claude Code, ChatGPT, or another AI tool you already use, in a few minutes.

Nexus works inside the coding harness or AI workspace you already use. You install Nexus CLI, sign in, and connect your tool with one command.

Every connected harness starts on **Nexus Auto** (`auto`). It picks an open or closed model for each turn to balance performance and cost.

## Install the Nexus CLI

```bash wrap theme={null}
curl -fsSL https://nexus.fireworks.ai/install.sh | bash
```

You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks API key (`fw_...`).

Next, pick your tool and follow its setup.

## Featured connections

> **[Claude Code CLI](/nexus/harnesses/claude-code)**
>
> Nexus Auto sends each turn to an open model or an Anthropic model. Anthropic turns use your Claude login.

> **[ChatGPT](/nexus/harnesses/chatgpt)**
>
> Open models appear next to your OpenAI models. The same connection sets up the Codex CLI.

### Code

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

> **[Claude Desktop](/nexus/harnesses/claude-desktop)**
