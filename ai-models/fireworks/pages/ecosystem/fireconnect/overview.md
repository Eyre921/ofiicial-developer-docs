---
title: "Overview"
source: https://docs.fireworks.ai/ecosystem/fireconnect/overview
path: ecosystem/fireconnect/overview
---

Route Claude Code, OpenCode, Codex, Pi, Cursor, VS Code, and Deep Agents through Fireworks AI or Microsoft Foundry models

[FireConnect](https://github.com/fw-ai/fireconnect) is an open-source CLI that routes agentic coding harnesses through Fireworks models. It is a core component of [Fireworks Nexus](/fireworks-nexus/overview) and also works standalone with any Fireworks API key. Install once, sign in once, then flip any supported harness on or off without hand-editing config files.

Choose where inference runs:

* **Direct Fireworks routing** (default): the [Fireworks gateway](https://fireworks.ai). Sign in with `fireconnect login` or use a Fireworks API key (`fw_...`) or [Fire Pass](/firepass) key (`fpk_...`).
* **Fireworks on Microsoft Foundry**: models in your Azure subscription, billed through Azure. See [Microsoft Foundry](/ecosystem/fireconnect/microsoft-foundry).

<Tip>
  New here? Run `fireconnect login`, then `fireconnect claude on`, restart Claude Code, and send `hi`. Try the [side-by-side demo](/ecosystem/fireconnect/demo) if you want to compare before switching.
</Tip>

## What's new in v0.9.1

FireConnect **0.9.1** improves upgrades and Claude model setup:

* **Seamless upgrades**: from 0.9.0 on, reinstalling or running `fireconnect upgrade` keeps harness settings in place — Claude Code stays connected
* **In-place upgrade**: `fireconnect upgrade`, or answer **Yes** when an interactive terminal prompts you that a newer version is available
* **Claude model preferences**: first-run onboarding wizard, `--interactive` / `--non-interactive`, and persisted mappings per key type (`fw_...` vs `fpk_...`)
* **Reliability**: baked API keys across harness configs, WebSearch MCP auth refresh on upgrade/login, clearer catalog labels

## What's new in v0.9.0

FireConnect **0.9.0** adds a global model catalog, first-class FireRouter support, and safer upgrades:

* **Global model catalog**: `fireconnect model list`
* **FireRouter as a model**: `on --model firerouter` on supported harnesses
* **Claude usage reports**: `fireconnect claude usage`
* **Web search MCP**: HTTP MCP for live search with a Fireworks API key ([details](/ecosystem/fireconnect/websearch-mcp)). FireConnect auto-install on Claude Code; other harnesses coming soon.

If you are upgrading from **before 0.9.0**, see [Upgrade FireConnect](#upgrade-fireconnect) before enabling FireRouter or web search.

## Guides

<CardGroup>
  <Card title="Side-by-side demo" icon="bolt" href="/ecosystem/fireconnect/demo">
    Race Anthropic vs Fireworks on the same prompt
  </Card>

  <Card title="Recommended models" icon="list" href="/ecosystem/fireconnect/recommended-models">
    Serverless short IDs and Fire Pass defaults
  </Card>

  <Card title="CLI reference" icon="terminal" href="/ecosystem/fireconnect/cli-reference">
    Commands, providers, auth, and migration
  </Card>

  <Card title="Microsoft Foundry" icon="microsoft" href="/ecosystem/fireconnect/microsoft-foundry">
    Route harnesses through Azure deployments
  </Card>

  <Card title="WebSearch MCP" icon="globe" href="/ecosystem/fireconnect/websearch-mcp">
    Live web search from any harness; FireConnect on Claude Code today
  </Card>
</CardGroup>

## Harness guides

<CardGroup>
  <Card title="Claude Code" icon="terminal" href="/ecosystem/fireconnect/claude-code">
    Multi-slot model aliases
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

  <Card title="Deep Agents" icon="robot" href="/ecosystem/fireconnect/deepagents">
    LangChain Deep Agents Code (`dcode`)
  </Card>
</CardGroup>

## Harness support

| Harness     | Fireworks gateway | Fire Pass | Microsoft Foundry | [FireRouter](/ecosystem/firerouter/overview) | Guide                                             |
| ----------- | :---------------: | :-------: | :---------------: | :------------------------------------------: | ------------------------------------------------- |
| Claude Code |        Yes        |    Yes    |         No        |                      Yes                     | [Claude Code](/ecosystem/fireconnect/claude-code) |
| OpenCode    |        Yes        |    Yes    |        Yes        |                      Yes                     | [OpenCode](/ecosystem/fireconnect/opencode)       |
| Codex       |        Yes        |     No    |        Yes        |                      Yes                     | [Codex](/ecosystem/fireconnect/codex)             |
| Pi          |        Yes        |    Yes    |        Yes        |                      Yes                     | [Pi](/ecosystem/fireconnect/pi)                   |
| Cursor      |        Yes        |    Yes    |        Yes        |                      No                      | [Cursor](/ecosystem/fireconnect/cursor)           |
| VS Code     |        Yes        |    Yes    |        Yes        |                      Yes                     | [VS Code](/ecosystem/fireconnect/vscode)          |
| Deep Agents |        Yes        |    Yes    |        Yes        |                      No                      | [Deep Agents](/ecosystem/fireconnect/deepagents)  |

**Notes**

* **Microsoft Foundry**: Claude Code does not read `--provider azure` yet. Every other harness in the matrix supports Foundry routing in FireConnect v0.9.0+.
* **Fire Pass**: not supported on Codex or Foundry. FireConnect also rejects `--model firerouter` with Fire Pass keys (`fpk_...`) on every harness. Use a standard Fireworks API key (`fw_...`) for FireRouter.
* **Web search MCP**: works from any harness via HTTP MCP with a Fireworks API key (request access from Fireworks). FireConnect auto-install is Claude Code only for now; other harnesses coming soon. See [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp).
* **Cursor / VS Code**: quit the IDE before `on` or `off` (SQLite writes). `status` is read-only.

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or [Fire Pass](/firepass) key (`fpk_...`) for direct routing
* For Foundry: Azure resource, API key, and deployment. See [portal setup](/ecosystem/integrations/azure-foundry).
* Node.js 18+
* At least one supported harness installed locally

## Install

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
fireconnect login
fireconnect claude on
```

The installer clones the CLI to `~/.fireconnect/cli`, installs dependencies, and adds `~/.local/bin/fireconnect`. It does **not** sign you in or write harness settings.

You do not have to run `login` first. `fireconnect claude on` runs sign-in inline if needed.

### Upgrade FireConnect

Upgrade with either command:

```bash theme={null}
fireconnect upgrade
# or
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
```

**On FireConnect 0.9.0 or newer**, harness settings are preserved — Claude Code and other harnesses stay connected across upgrade or reinstall. No need to run `fireconnect claude off` first.

In an interactive terminal, FireConnect may prompt **Upgrade now?** when a newer release is available. Answer **Yes** to run `fireconnect upgrade`, or **No** to snooze the prompt for a day.

**Upgrading from before 0.9.0** with Claude Code connected: FireConnect temporarily restores your original Claude settings before updating. Reconnect after upgrade:

```bash theme={null}
fireconnect claude on
```

For non-interactive installs (CI), set `FIRECONNECT_AUTO_OFF_CLAUDE=1` to restore automatically. Check version with `fireconnect --version`.

After upgrading, see the [CLI reference](/ecosystem/fireconnect/cli-reference), [recommended models](/ecosystem/fireconnect/recommended-models), [side-by-side demo](/ecosystem/fireconnect/demo), and [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp).

## Sign in

```bash theme={null}
fireconnect login     # browser sign-in or paste a key
fireconnect logout    # clear stored credentials
fireconnect status    # sign-in state and key storage
```

Fire Pass keys (`fpk_...`) work during `login` or `on`. FireConnect detects the key type and applies the correct defaults.

See [CLI reference: Sign in options](/ecosystem/fireconnect/cli-reference#sign-in-options) for `--with-token`, `--account`, `logout --revoke`, and `configure`.

## FireRouter

[FireRouter](/ecosystem/firerouter/overview) automatically routes simple requests to cheaper open models and hard requests to Claude Opus 4.8. In FireConnect, select it like any other model:

```bash theme={null}
fireconnect claude on --model firerouter
```

Cursor does not support FireRouter. See the [FireRouter overview](/ecosystem/firerouter/overview#fireconnect) for auth, routing preferences, and supported harnesses.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
