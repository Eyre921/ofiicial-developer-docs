---
title: "FireConnect"
source: https://docs.fireworks.ai/nexus/fireconnect
path: nexus/fireconnect
---

Point Claude Code, Claude Desktop, Codex, the ChatGPT desktop app, OpenCode, Cursor IDE, VS Code, and Copilot at Fireworks with one FireConnect command

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

[FireConnect](https://github.com/fw-ai/fireconnect) is the easiest way to use Fireworks models in the coding harness you already use. It is an open-source CLI that rewrites your harness settings to call Fireworks, adds Fireworks models to the model picker, and restores your original settings when you turn it off. You do not need to host a service or edit config files by hand.

**Command line**

> **[Claude Code](/nexus/harnesses#claude-code)**

> **[Codex CLI](/nexus/harnesses#codex)**

> **[OpenCode](/nexus/harnesses#opencode)**

> **[Pi](/nexus/harnesses#pi)**

> **[Copilot CLI](/nexus/harnesses#copilot-cli)**

> **[DeepSeek](/nexus/harnesses#deepseek-harness)**

**Desktop and IDE apps**

> **[Claude Desktop](/nexus/harnesses#claude-desktop)**

> **[ChatGPT desktop app](/nexus/harnesses#chatgpt-desktop-app)**

> **[Cursor IDE](/nexus/harnesses#cursor-ide)**

> **[VS Code](/nexus/harnesses#vs-code)**

> **[Copilot App](/nexus/harnesses#copilot-app)**

## Quick start

**1. Install**

```bash wrap theme={null}
curl -fsSL https://fireconnect.fireworks.ai/install.sh | bash
```

Requires Node.js 18 or later. On Windows, run it from Git Bash; PowerShell breaks the script's line endings.

> **Alternative installer**
>
> ```bash wrap theme={null}
> curl -fsSL \
>   https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh \
>   | bash
> ```

**2. Sign in**

```bash wrap theme={null}
fireconnect login
```

Sign in with your browser, or paste a Fireworks key.

**3. Connect a harness**

```bash wrap theme={null}
fireconnect claude
```

Replace `claude` with any harness from [Coding Harnesses](/nexus/harnesses). For Claude Desktop, run `fireconnect claude-desktop on`. For the ChatGPT desktop app, run `fireconnect chatgpt`; it shares a config with the Codex CLI, so it connects both. `cursor` means **Cursor IDE** only; Cursor CLI is not supported.

Not sure of the name? Run `fireconnect` on its own and pick from the [interactive menu](#interactive-menu). The ChatGPT desktop app is the `codex` row.

**4. Restart and check**

```bash wrap theme={null}
fireconnect claude status
```

> [!TIP]
>
> `status` shows the configured model and the Fireworks models in the picker.

> [!TIP]
>
> **Rather edit settings yourself?** Each harness in
> [Coding Harnesses](/nexus/harnesses) has a **Manual setup** tab with the
> exact settings FireConnect would write.

## Interactive menu

Run `fireconnect` with no arguments to pick a harness and an action from a menu:

```bash wrap theme={null}
fireconnect
```

![Terminal running fireconnect: the menu lists each harness with its status, codex is selected, then on, and FireConnect connects Codex and prints the direct command, fireconnect codex](https://mintcdn.com/fireworksai/uH3av4WCHDokF6Sc/images/fireconnect/interactive-launcher.gif?s=7ea80319c27db140143cc98d21da8e97)

* Each harness shows its status: `on`, `off`, `off · detected` (installed but not connected), or `not detected`.
* Use the arrow keys and Enter, or press 1-9 to pick a row directly. Esc goes back one menu, or exits from the top menu.
* Pick a harness, then `on`, `off`, or `status`. Claude Code also offers `usage` and `live`.
* `configure`, `key`, and `help` sit at the bottom of the list.
* After the action runs, FireConnect prints the direct command, such as `fireconnect codex`, so you can skip the menu next time.

![FireConnect interactive menu listing claude, claude-desktop, opencode, codex, pi, cursor, vscode, copilot-app, copilot-cli, and deepseek with their status, then configure, key, and help](https://mintcdn.com/fireworksai/uH3av4WCHDokF6Sc/images/fireconnect/interactive-launcher.png?fit=max\&auto=format\&n=uH3av4WCHDokF6Sc\&q=85\&s=24882a9cb87f66ba5153f62528ee4375)

## In Claude Code

Run `fireconnect claude`, then start a new session and open `/model`. It lists `auto`, FireRouter, and the Fireworks models next to Claude Code's own models:

![Claude Code model picker with FireRouter selected and Auto, DeepSeek, GLM, Kimi, and MiniMax options](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/claude-model-picker.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=cab8623549ed73df655ebfb39dd11fb0)

Your Claude login stays signed in. See [Claude Code](/nexus/harnesses#claude-code) for tier pins, the status line, and manual setup.

## In Codex

Close open Codex sessions, then connect:

```bash wrap theme={null}
fireconnect codex
```

Start a new Codex session. `/model` lists FireRouter, then Codex's GPT models, then the Fireworks models:

![Codex CLI Select Model and Effort picker with FireRouter (current) selected, described as routing each user turn between open models and the closed models you have access to, followed by GPT-6.1-Sol, GPT-6-Astra, GPT-6-Sol, GPT-6-Luna, and older GPT models](https://mintcdn.com/fireworksai/uH3av4WCHDokF6Sc/images/fireconnect/codex-model-picker.png?fit=max\&auto=format\&n=uH3av4WCHDokF6Sc\&q=85\&s=bf7f6cb2cd9aba89399ed89ddc2f63d2)

Codex keeps its own sign-in. Your Fireworks key pays for Fireworks models, and your Codex sign-in pays for GPT models. See [Codex](/nexus/harnesses#codex) for sign-in, billing, and manual setup.

## In the ChatGPT desktop app

Quit the ChatGPT desktop app, then connect:

```bash wrap theme={null}
fireconnect chatgpt
```

Reopen the app. The Fireworks models appear in its model list next to the GPT models. The app shares its config with the Codex CLI, so this also connects Codex. See [ChatGPT desktop app](/nexus/harnesses#chatgpt-desktop-app).

## Connect and restore

* **Connect** rewrites the harness config to call Fireworks and saves a snapshot under `~/.fireconnect/`.
* **`off`** restores file-based harnesses from that snapshot byte-for-byte. For IDE databases, it removes the settings and models FireConnect added.
* **`fireconnect upgrade`** updates FireConnect and brings connected harnesses up to date, keeping the model you picked. Restart each harness the upgrade output names.
* **Sign-in credentials and harness configurations are stored separately.** `fireconnect login` saves your credential through FireConnect's secret store. If a harness requires the key in its own configuration, FireConnect copies it there and restricts the file permissions. Run `fireconnect status` to see the active storage backend without revealing the key.

## Choose a model

Connecting registers coding-ready Fireworks models, including `auto`. Use `--model` to add or select a specific model:

```bash wrap theme={null}
fireconnect opencode --model glm-latest
```

Restart or reopen the harness after changing a model. Browse IDs with `fireconnect model list`. See [Open Models](/nexus/open-models) for aliases and pinned versions, and [Coding Harnesses](/nexus/harnesses) for app-specific rules.

To route each turn between open models and the Claude or GPT models you have access to, use FireRouter. [FireRouter Setup](/nexus/firerouter/setup#fireconnect) covers the FireConnect command and the credentials each harness can send.

## Web search

Web search works through Fireworks with no extra setup. In Claude Code, the native `WebSearch` and `WebFetch` tools run server-side on Fireworks. The Codex CLI and the ChatGPT desktop app keep their native web search. Search works with any Fireworks model or FireRouter ID. Web search pricing will be published soon; see [Web Search](/nexus/web-search).

> [!NOTE]
>
> Earlier FireConnect versions installed a `fireworks-websearch` MCP server for
> Claude Code. That MCP is no longer available. Run `fireconnect upgrade` to
> remove it; your own MCP servers are not changed. See
> [Web Search](/nexus/web-search).

## Upgrade and uninstall

For upgrade and uninstall commands, see the [CLI Reference](/nexus/cli-reference).
