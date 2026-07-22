---
title: "Overview"
source: https://docs.fireworks.ai/ecosystem/fireconnect/overview
path: ecosystem/fireconnect/overview
---

Route Claude Code, OpenCode, Codex, Pi, Cursor, VS Code, and Deep Agents through Fireworks AI or Microsoft Foundry models

[FireConnect](https://github.com/fw-ai/fireconnect) is an open-source CLI that routes agentic coding harnesses through Fireworks models. Choose where inference runs:

* **Direct Fireworks routing** (default) — requests go to the [Fireworks gateway](https://fireworks.ai); sign in with `fireconnect login` or use a Fireworks API key (`fw_...`) or [Fire Pass](/firepass) key (`fpk_...`)
* **Fireworks on Microsoft Foundry** — the same models, deployed in your Azure subscription and billed through Azure; use `--provider azure` and an Azure API key (see [Fireworks on Microsoft Foundry](#fireworks-on-microsoft-foundry))

Install once, sign in, then enable or disable routing per harness without editing config files by hand.

<CardGroup>
  <Card title="Claude Code" icon="terminal" href="/ecosystem/fireconnect/claude-code">
    Anthropic-compatible routing with multi-slot model aliases
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
    LangChain Deep Agents Code (`dcode`) via OpenAI-compatible config
  </Card>
</CardGroup>

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`) for direct Fireworks routing
* For **Fireworks on Microsoft Foundry**: a Microsoft Foundry resource, an Azure API key, and at least one model deployment (see [Fireworks on Microsoft Foundry](#fireworks-on-microsoft-foundry) and the [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry))
* Node.js 18+ (the installer can install it via Homebrew on macOS or prints upgrade instructions elsewhere)
* At least one supported harness installed locally

## Install

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
```

The installer:

* Clones the CLI to `~/.fireconnect/cli`, runs `npm install --omit=dev` for its runtime dependency (`cross-keychain`, used for secure API-key storage), and adds a `fireconnect` launcher to `~/.local/bin`
* Does **not** sign you in or write harness settings — run `fireconnect login` then `fireconnect <harness> on` after it finishes

After install, sign in and enable a harness:

```bash theme={null}
fireconnect login        # guided sign-in (browser or paste a key)
fireconnect claude on    # Claude Code (default starting point)
fireconnect opencode on  # OpenCode
fireconnect codex on       # Codex
fireconnect pi on          # Pi
fireconnect cursor on      # Cursor IDE (quit Cursor first)
fireconnect vscode on      # VS Code + GitHub Copilot Chat
fireconnect deepagents on  # LangChain Deep Agents Code
```

You do not have to run `login` first — any key-needing command like `fireconnect claude on` runs the same sign-in flow inline, then finishes the job.

### Upgrade

If you installed via the curl installer, pull the latest release in place:

```bash theme={null}
fireconnect upgrade
```

Re-run the install script if FireConnect was not installed with git (for example, a manual checkout).

When a newer version is available, FireConnect prints a one-line update banner on startup with upgrade instructions. The check runs in the background and does not block your command.

Check your installed version:

```bash theme={null}
fireconnect --version
```

## Sign in and API keys

FireConnect stores API keys in the OS keychain when available (via `cross-keychain`), not as plaintext in harness config files.

```bash theme={null}
fireconnect login     # browser sign-in (creates a machine key) or paste an existing key
fireconnect logout    # clear the stored key (keychain entry + config ref)
fireconnect status    # show sign-in state and where the key is stored
```

`~/.fireconnect/config.json` stores a reference such as `{keychain:fireworks-api-key}` or `{env:FIREWORKS_API_KEY}` — never a literal key. Claude Code uses `apiKeyHelper` to fetch the key at runtime; Codex, OpenCode, Pi, and Deep Agents use environment references plus a shell profile hook that exports `FIREWORKS_API_KEY="$(fireconnect key export)"`.

Fire Pass users can paste a `fpk_...` key during `login` or `on`. FireConnect detects the key type and applies the correct defaults.

## Fireworks on Microsoft Foundry

Route **OpenCode**, **Codex**, and **Pi** through a [Microsoft Foundry](/ecosystem/integrations/azure-foundry) deployment instead of the Fireworks gateway. Usage is billed through Azure and counts toward MACC where applicable.

<CardGroup>
  <Card title="FireConnect + Microsoft Foundry" icon="terminal" href="/ecosystem/fireconnect/microsoft-foundry">
    Configure `--provider azure`, deployment names, per-harness config, and switching back to direct Fireworks
  </Card>

  <Card title="Microsoft Foundry portal setup" icon="microsoft" href="/ecosystem/integrations/azure-foundry">
    Enable Fireworks on Foundry, PayGo / PTU modes, billing, and troubleshooting
  </Card>
</CardGroup>

Quick start:

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect opencode on --main FW-GLM-5.1
```

Claude Code, Cursor, VS Code, and Deep Agents do **not** have Azure routing in FireConnect yet — they always use direct Fireworks when you run `on`, even if global config has `--provider azure`. See the [full Microsoft Foundry guide](/ecosystem/fireconnect/microsoft-foundry) for which harnesses are implemented, endpoint normalization, one-off `--azure` routing, turning Foundry off, and what each harness writes.

## CLI design

FireConnect uses **harness-first** syntax:

`fireconnect <harness> <command>`

Bare harness names run `on` (for example, `fireconnect claude` is the same as `fireconnect claude on`).

### Global commands

```bash theme={null}
fireconnect login        # Sign in — browser (creates a key) or paste a key you have
fireconnect logout       # Clear the stored key (keychain entry + config ref)
fireconnect status       # Show sign-in state and where the key is stored
fireconnect configure    # Set the provider (Azure/Foundry) and Anthropic key for router mode
fireconnect demo         # Race your provider vs Fireworks GLM 5.2 Fast on the same prompt
fireconnect upgrade      # Pull the latest FireConnect from GitHub (curl install)
fireconnect uninstall    # Disable all harnesses, restore configs, remove CLI
fireconnect help         # Show help
fireconnect --version    # Print the installed CLI version (-V also works)
```

### Providers

FireConnect supports two inference backends. The CLI provider flag is shown in parentheses.

| Provider flag         | Where inference runs           | API key               | Supported harnesses                                            |
| --------------------- | ------------------------------ | --------------------- | -------------------------------------------------------------- |
| `fireworks` (default) | Fireworks gateway              | `fw_...` or `fpk_...` | Claude Code, OpenCode, Codex, Pi, Cursor, VS Code, Deep Agents |
| `azure`               | Fireworks on Microsoft Foundry | Azure API key         | OpenCode, Codex, Pi                                            |

Set the default with `fireconnect configure --provider fireworks` or `--provider azure`. For Foundry, also pass `--base-url` with your resource endpoint. Harness `on` commands use the configured provider unless you pass `--azure` or per-command `--base-url` / `--api-key` overrides.

### Per-harness commands

Each CLI harness (`claude`, `opencode`, `codex`, `pi`, `deepagents`) supports:

* `fireconnect <harness> on` — Route through the configured provider
* `fireconnect <harness> off` — Restore your previous config
* `fireconnect <harness> status` — Show provider, auth, and models
* `fireconnect <harness> model list` — Browse Fireworks serverless models (direct Fireworks routing only)
* `fireconnect <harness> model select` — Pick a serverless model interactively (direct Fireworks routing only)
* `fireconnect <harness> model reset` — Reset models to defaults
* `fireconnect <harness> help` — Harness-specific help

Claude Code also has `fireconnect claude usage` (estimate usage cost from a session log).

Each IDE harness (`cursor`, `vscode`) supports:

* `fireconnect <harness> on` — Configure direct Fireworks routing (Azure not implemented for IDE harnesses yet; quit the IDE first)
* `fireconnect <harness> off` — Restore your previous config (quit the IDE first)
* `fireconnect <harness> status` — Show provider, auth, and registered models (read-only; IDE can stay open)
* `fireconnect <harness> model list` — Browse Fireworks serverless models (read-only)
* `fireconnect <harness> model add <id>` — Add a Fireworks model to the IDE picker
* `fireconnect <harness> model select` — Pick a model interactively (Cursor: pass `--mode`)
* `fireconnect <harness> model reset` — Reset fireconnect-managed models to defaults
* `fireconnect <harness> help` — Harness-specific help

Cursor stores settings in SQLite (`state.vscdb`). Commands that write to that database (`on`, `off`, `model add`, `model select`, `model reset`) require Cursor to be fully quit first. VS Code stores the API key in `state.vscdb` as well, so `on` and `off` require quitting VS Code; `model add`, `model select`, and `model reset` only edit `chatLanguageModels.json`, which VS Code hot-reloads.

With **Fireworks on Microsoft Foundry** (`--provider azure`), pass your Foundry **deployment name** to `on` with `--main` instead of using `model list` or `model select`.

Run `fireconnect help` for the overview, or `fireconnect claude help` (and similarly for other harnesses) for harness-level options.

### API key resolution

When a command needs credentials, FireConnect resolves them based on the active provider.

**Direct Fireworks routing** (`--provider fireworks`)

1. Explicit `--api-key`
2. OS keychain (via `fireconnect login`)
3. Global `~/.fireconnect/config.json` reference
4. `FIREWORKS_API_KEY` environment variable

Claude Code additionally reads harness-local keys from `~/.claude/settings.json` when FireConnect is already enabled there.

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Global `~/.fireconnect/config.json`
3. `AZURE_API_KEY` environment variable

## Recommended models

These **serverless model short IDs** apply to **direct Fireworks routing** and expand to full Fireworks paths automatically. With **Fireworks on Microsoft Foundry**, pass your **deployment name** instead (for example, `FW-GLM-5.1` or `FW-MiniMax-M2.5`) via `--main`.

| Short ID            | Best for                      | Notes                                                                                                                                                                            |
| ------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `glm-latest`        | All-around use, agentic tasks | Version-tracking router; strong reasoning, 1M context.                                                                                                                           |
| `glm-fast-latest`   | Latency-sensitive agentic use | Default for `main`, `opus`, and `fable` slots in Claude Code. Version-tracking router on the high-speed Fast serving path (100+ tok/s), at a higher per-token price. 1M context. |
| `glm-5p2-fast`      | Latency-sensitive agentic use | Same as `glm-fast-latest` but pinned to GLM 5.2 rather than version-tracking. 1M context.                                                                                        |
| `glm-5p1`           | General use (lighter)         | Default `sonnet` slot in Claude Code. Good balance of speed and quality.                                                                                                         |
| `deepseek-v4-flash` | Background / fast tasks       | Default `haiku` and `subagent` slots in Claude Code. Lowest latency.                                                                                                             |

### Fire Pass keys

Fire Pass keys (`fpk_...`) default all slots to `glm-fast-latest`. The model browser shows Fire Pass-supported routers: `glm-latest`, `glm-fast-latest`, `glm-5p2-fast`, `kimi-fast-latest`, and `kimi-k2p7-code-fast`.

Fire Pass keys work with direct Fireworks routing only. Use an Azure API key with `--provider azure`.

<Warning>
  Codex does not support Fire Pass keys yet. Use a standard Fireworks API key (`fw_...`) with Codex.
</Warning>

## Migration from earlier syntax

FireConnect uses harness-first commands. If you have older docs or scripts from pre-0.5.0 releases, update them:

| Before                              | After                               |
| ----------------------------------- | ----------------------------------- |
| `fireconnect on`                    | `fireconnect claude on`             |
| `fireconnect off`                   | `fireconnect claude off`            |
| `fireconnect status`                | `fireconnect claude status`         |
| `fireconnect list`                  | `fireconnect claude status`         |
| `fireconnect set --main <id>`       | `fireconnect claude on --main <id>` |
| `fireconnect reset`                 | `fireconnect claude model reset`    |
| `fireconnect on --harness opencode` | `fireconnect opencode on`           |
| `fireconnect model list`            | `fireconnect <harness> model list`  |

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
