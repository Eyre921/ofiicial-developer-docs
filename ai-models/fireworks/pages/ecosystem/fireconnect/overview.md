---
title: "Overview"
source: https://docs.fireworks.ai/ecosystem/fireconnect/overview
path: ecosystem/fireconnect/overview
---

Route coding harnesses through Fireworks AI, with Microsoft Foundry support for compatible tools

[FireConnect](https://github.com/fw-ai/fireconnect) is an open-source CLI that routes agentic coding harnesses through Fireworks models. Install once, sign in once, then flip any supported harness on or off without hand-editing config files.

Choose where inference runs:

* **Direct Fireworks routing** (default): the [Fireworks gateway](https://fireworks.ai). Sign in with `fireconnect login` or use a Fireworks API key (`fw_...`) or [Fire Pass](/firepass) key (`fpk_...`).
* **Fireworks on Microsoft Foundry**: models in your Azure subscription, billed through Azure. See [Microsoft Foundry](/ecosystem/fireconnect/microsoft-foundry).

<Tip>
  New here? Install and sign in below, then open the [harness guide](#choose-your-harness) for the tool you use. Try the [side-by-side demo](/ecosystem/fireconnect/demo) if you want to compare before switching.
</Tip>

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or [Fire Pass](/firepass) key (`fpk_...`) for direct routing
* For Foundry: Azure resource, API key, and deployment. See [portal setup](/ecosystem/integrations/azure-foundry).
* Node.js 18+
* At least one supported harness installed locally

## Install

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
fireconnect login
```

The installer is a **bash** script. It clones the CLI to `~/.fireconnect/cli`, installs dependencies, and adds `~/.local/bin/fireconnect`. It does **not** sign you in or write harness settings.

After `login`, open your [harness guide](#choose-your-harness) and run `fireconnect <harness> on`. You can also pass `--api-key` or set `FIREWORKS_API_KEY` instead of `login`.

<Note>
  **Windows:** run from Git Bash with the same command. Piping through PowerShell corrupts line endings (`set: pipefail\r: invalid option name`).
</Note>

### Upgrade FireConnect

```bash theme={null}
fireconnect upgrade
```

Or re-run the install curl above. On v0.9.0+, harness settings stay connected across upgrade.

Check version with `fireconnect --version`. See [CLI reference: Migration](/ecosystem/fireconnect/cli-reference#migration-from-earlier-syntax) for renames.

## Sign in

```bash theme={null}
fireconnect login     # browser sign-in or paste a key
fireconnect logout    # clear stored credentials
fireconnect status    # sign-in state and key storage
```

Fire Pass keys (`fpk_...`) work during `login` or `on`. FireConnect detects the key type and applies the correct defaults.

See [CLI reference: Sign in options](/ecosystem/fireconnect/cli-reference#sign-in-options) for `--with-token`, `--account`, `logout --revoke`, and `configure`.

## Choose your harness

After install and sign-in, open the guide for the tool you use. Each page covers `on` / `off`, models, and harness-specific notes.

<CardGroup>
  <Card title="Claude Code" icon="terminal" href="/ecosystem/fireconnect/claude-code">
    Six model slots + usage meter
  </Card>

  <Card title="OpenCode" icon="terminal" href="/ecosystem/fireconnect/opencode">
    OpenAI-compatible adapter in `opencode.json`
  </Card>

  <Card title="Codex" icon="terminal" href="/ecosystem/fireconnect/codex">
    OpenAI Codex CLI via the Responses API
  </Card>

  <Card title="Pi" icon="terminal" href="/ecosystem/fireconnect/pi">
    Pi agent settings and auth
  </Card>

  <Card title="Cursor" icon="laptop-code" href="/ecosystem/fireconnect/cursor">
    OpenAI BYOK settings for Cursor IDE
  </Card>

  <Card title="VS Code" icon="code" href="/ecosystem/fireconnect/vscode">
    GitHub Copilot Chat custom endpoint
  </Card>

  <Card title="DeepSeek Harness" icon="robot" href="/ecosystem/fireconnect/deepseek">
    DeepSeek's coding agent (`dsh`)
  </Card>
</CardGroup>

## Models

```bash theme={null}
fireconnect model list --search glm
fireconnect <harness> on --model glm-fast-latest
# Cursor / VS Code: quit before on; others: restart after
```

`<harness>` is one of: `claude`, `opencode`, `codex`, `pi`, `cursor`, `vscode`, `deepseek`. Full walkthrough: **[Models](/ecosystem/fireconnect/models)**.

## Harness support

| Harness          | Fireworks gateway | Fire Pass | Microsoft Foundry | [FireRouter](/ecosystem/firerouter/overview) | Guide                                               |
| ---------------- | :---------------: | :-------: | :---------------: | :------------------------------------------: | --------------------------------------------------- |
| Claude Code      |        Yes        |    Yes    |         No        |                      Yes                     | [Claude Code](/ecosystem/fireconnect/claude-code)   |
| OpenCode         |        Yes        |    Yes    |        Yes        |                      Yes                     | [OpenCode](/ecosystem/fireconnect/opencode)         |
| Codex            |        Yes        |     No    |        Yes        |                      Yes                     | [Codex](/ecosystem/fireconnect/codex)               |
| Pi               |        Yes        |    Yes    |        Yes        |                      Yes                     | [Pi](/ecosystem/fireconnect/pi)                     |
| Cursor           |        Yes        |    Yes    |        Yes        |                Workspace BYOK                | [Cursor](/ecosystem/fireconnect/cursor)             |
| VS Code          |        Yes        |    Yes    |        Yes        |                      Yes                     | [VS Code](/ecosystem/fireconnect/vscode)            |
| DeepSeek Harness |        Yes        |    Yes    |         No        |                Workspace BYOK                | [DeepSeek Harness](/ecosystem/fireconnect/deepseek) |

**Notes**

* **Foundry**: not on Claude Code or DeepSeek Harness.
* **Fire Pass**: not on Codex or Foundry. FireConnect rejects `--model firerouter` with a Fire Pass (`fpk_...`) key on **every** harness; use an `fw_...` account key for FireRouter.
* **FireRouter**: Cursor and DeepSeek Harness need workspace BYOK for Anthropic pass-through.
* **Web search MCP**: Claude Code auto-install only; any harness can add the HTTP MCP manually. See [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp).
* **Cursor / VS Code**: quit the IDE before `on` or `off`. `status` is read-only.

## FireRouter

[FireRouter](/ecosystem/firerouter/overview) automatically routes simple requests to cheaper open models and hard requests to Claude Opus 5. In FireConnect, select it like any other model:

```bash theme={null}
fireconnect <harness> on --model firerouter
```

Requires a standard Fireworks key (`fw_...`), not Fire Pass. Cursor and DeepSeek Harness also need workspace BYOK for Anthropic pass-through. See the [FireRouter overview](/ecosystem/firerouter/overview#fireconnect) and [Harness support](#harness-support).

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)

## See also

* [CLI reference](/ecosystem/fireconnect/cli-reference)
* [Microsoft Foundry](/ecosystem/fireconnect/microsoft-foundry)
* [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp)
* [Side-by-side demo](/ecosystem/fireconnect/demo)
