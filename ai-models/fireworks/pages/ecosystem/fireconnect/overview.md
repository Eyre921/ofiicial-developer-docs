---
title: "Overview"
source: https://docs.fireworks.ai/ecosystem/fireconnect/overview
path: ecosystem/fireconnect/overview
---

Route Claude Code, OpenCode, Codex, Pi, Cursor, and VS Code through Fireworks AI or Microsoft Foundry models

[FireConnect](https://github.com/fw-ai/fireconnect) is an open-source CLI that routes agentic coding harnesses through Fireworks models. Choose where inference runs:

* **Direct Fireworks routing** (default) — requests go to the [Fireworks gateway](https://fireworks.ai); use a Fireworks API key (`fw_...`) or [Fire Pass](/firepass) key (`fpk_...`)
* **Fireworks on Microsoft Foundry** — the same models, deployed in your Azure subscription and billed through Azure; use `--provider azure` and an Azure API key (see [Fireworks on Microsoft Foundry](#fireworks-on-microsoft-foundry))

Install once, configure your provider, then enable or disable routing per harness without editing config files by hand.

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
</CardGroup>

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`) for direct Fireworks routing
* For **Fireworks on Microsoft Foundry**: a Microsoft Foundry resource, an Azure API key, and at least one model deployment (see [Fireworks on Microsoft Foundry](#fireworks-on-microsoft-foundry) and the [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry))
* Node.js (the installer can install it via Homebrew or apt if it is missing)
* At least one supported harness installed locally

## Install

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
```

For non-interactive setup:

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | FIREWORKS_API_KEY="fw_..." bash
```

Fire Pass users can pass a `fpk_...` key directly. FireConnect detects the key type and applies the correct defaults.

The installer:

* Clones the CLI to `~/.fireconnect/cli` and adds a `fireconnect` launcher to `~/.local/bin`
* Runs `fireconnect configure` to register harnesses and store your API key preference
* Uses Node.js to update harness settings (it does not install or update npm packages)

After install, configure your provider (Fireworks is the default), then enable a harness:

```bash theme={null}
fireconnect configure --provider fireworks --api-key fw_...
fireconnect claude on      # Claude Code (default starting point)
fireconnect opencode on    # OpenCode
fireconnect codex on       # Codex
fireconnect pi on          # Pi
fireconnect cursor on      # Cursor IDE (quit Cursor first)
fireconnect vscode on      # VS Code + GitHub Copilot Chat
```

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

## Fireworks on Microsoft Foundry

Route OpenCode, Codex, and Pi through a [Microsoft Foundry](/ecosystem/integrations/azure-foundry) deployment of Fireworks models instead of the Fireworks gateway. Usage is billed through your Azure account and counts toward Azure commitments where applicable.

<Card title="Microsoft Foundry integration guide" icon="microsoft" href="/ecosystem/integrations/azure-foundry">
  Portal setup, deployment modes (PayGo / PTU), billing, and troubleshooting — start here if you have not deployed a model yet
</Card>

<Note>
  **Terminology:** In the CLI, the Foundry provider is `--provider azure` (or `on --azure`). Harness configs display the label **Fireworks on Microsoft Foundry**. Foundry uses **deployment names** you chose at deploy time (for example, `FW-GLM-5.1`) — not Fireworks serverless short IDs like `glm-latest`.
</Note>

<Note>
  Claude Code, Cursor, and VS Code do **not** support Fireworks on Microsoft Foundry. Foundry exposes an OpenAI-compatible chat API, not the Anthropic Messages API Claude Code expects, and IDE BYOK flows require direct Fireworks credentials.
</Note>

### Prerequisites

* A Microsoft Foundry resource with at least one Fireworks model deployment (for example, `FW-GLM-5.1` or `FW-MiniMax-M2.5`)
* Your Foundry resource endpoint and Azure API key from the [Microsoft Foundry portal](https://ai.azure.com/)
* OpenCode, Codex, or Pi installed locally

Follow the [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry) and [Microsoft Learn setup steps](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models) to enable Fireworks on Foundry and create a deployment before running FireConnect.

### Configure the Foundry provider

Set the active provider once with `configure`. Harness `on` commands then use that provider — there is no separate global `azure on` command.

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --harnesses opencode,codex,pi
```

FireConnect normalizes `--base-url` to the OpenAI-compatible surface at `.../openai/v1`. You can paste the resource root, a project endpoint (`.../api/projects/<name>`), or an already-correct `.../openai/v1` URL.

To keep secrets out of `~/.fireconnect/config.json`, export `AZURE_API_KEY` before `configure` instead of passing `--api-key` — FireConnect stores an environment reference.

### Enable harnesses

After configuring the Foundry provider, enable harnesses the same way as with direct Fireworks routing:

```bash theme={null}
fireconnect opencode on
fireconnect codex on
fireconnect pi on
```

Each harness reads the provider, endpoint, and API key from `~/.fireconnect/config.json` and writes OpenAI-compatible adapter settings. In harness UIs, the provider appears as **Fireworks on Microsoft Foundry**.

### Choose a deployment

Pass the **deployment name** you chose in the Azure portal with `--main`:

```bash theme={null}
fireconnect opencode on --main FW-MiniMax-M2.5
fireconnect codex on --main FW-GLM-5.1
fireconnect pi on --main FW-GLM-5.1
```

If you omit `--main`, FireConnect defaults to `FW-GLM-5.1`.

<Warning>
  `fireconnect <harness> model list` and `model select` browse the **Fireworks serverless catalog** (direct routing only). They do not list Foundry deployments. With `--provider azure`, set your deployment with `--main` on `on`.
</Warning>

### One-off Foundry routing

To route a single harness through Foundry without changing global config, pass `--azure` on `on`:

```bash theme={null}
fireconnect opencode on \
  --azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --main FW-MiniMax-M2.5
```

If global config already has a Foundry endpoint, `--azure` alone reuses it:

```bash theme={null}
fireconnect opencode on --azure --main FW-GLM-5.1
```

### Switch between direct Fireworks and Foundry

Update global config, then re-enable each harness:

```bash theme={null}
# Foundry
fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --harnesses opencode,codex,pi

fireconnect opencode on --main FW-GLM-5.1
fireconnect codex on --main FW-GLM-5.1
fireconnect pi on --main FW-GLM-5.1

# Direct Fireworks
fireconnect configure --provider fireworks --api-key fw_...
fireconnect opencode on
fireconnect codex on
fireconnect pi on
```

Running `off` restores the harness config snapshot from before FireConnect was enabled for that provider.

### API key resolution (Foundry)

When the Foundry provider is active, FireConnect resolves credentials in this order:

1. Explicit `--api-key` on the command
2. Global `~/.fireconnect/config.json`
3. `AZURE_API_KEY` environment variable

### Verify routing

```bash theme={null}
fireconnect opencode status   # provider=azure, base URL, deployment name
fireconnect codex status
fireconnect pi status
```

Turn off routing per harness with `fireconnect <harness> off`. This restores your previous config from the snapshot in `~/.fireconnect/<harness>/`.

## CLI design

FireConnect uses **harness-first** syntax:

`fireconnect <harness> <command>`

Bare harness names run `on` (for example, `fireconnect claude` is the same as `fireconnect claude on`).

### Global commands

```bash theme={null}
fireconnect configure    # Register harnesses, provider, and API key preferences
fireconnect upgrade      # Pull the latest FireConnect from GitHub (curl install)
fireconnect uninstall    # Disable all harnesses, restore configs, remove CLI
fireconnect help         # Show help
fireconnect --version    # Print the installed CLI version (-V also works)
```

### Providers

FireConnect supports two inference backends. The CLI provider flag is shown in parentheses.

| Provider flag         | Where inference runs           | API key               | Supported harnesses                               |
| --------------------- | ------------------------------ | --------------------- | ------------------------------------------------- |
| `fireworks` (default) | Fireworks gateway              | `fw_...` or `fpk_...` | Claude Code, OpenCode, Codex, Pi, Cursor, VS Code |
| `azure`               | Fireworks on Microsoft Foundry | Azure API key         | OpenCode, Codex, Pi                               |

Set the default with `fireconnect configure --provider fireworks` or `--provider azure`. For Foundry, also pass `--base-url` with your resource endpoint. Harness `on` commands use the configured provider unless you pass `--azure` or per-command `--base-url` / `--api-key` overrides.

### Per-harness commands

Each CLI harness (`claude`, `opencode`, `codex`, `pi`) supports:

* `fireconnect <harness> on` — Route through the configured provider
* `fireconnect <harness> off` — Restore your previous config
* `fireconnect <harness> status` — Show provider, auth, and models
* `fireconnect <harness> model list` — Browse Fireworks serverless models (direct Fireworks routing only)
* `fireconnect <harness> model select` — Pick a serverless model interactively (direct Fireworks routing only)
* `fireconnect <harness> model reset` — Reset models to defaults
* `fireconnect <harness> help` — Harness-specific help

Each IDE harness (`cursor`, `vscode`) supports:

* `fireconnect <harness> on` — Configure direct Fireworks routing (not Foundry; quit the IDE first)
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
2. Harness-local stored key (for example, in `~/.claude/settings.json`)
3. Global `~/.fireconnect/config.json`
4. `FIREWORKS_API_KEY` environment variable

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Global `~/.fireconnect/config.json`
3. `AZURE_API_KEY` environment variable

## Recommended models

These **serverless model short IDs** apply to **direct Fireworks routing** and expand to full Fireworks paths automatically. With **Fireworks on Microsoft Foundry**, pass your **deployment name** instead (for example, `FW-GLM-5.1` or `FW-MiniMax-M2.5`) via `--main`.

| Short ID            | Best for                      | Notes                                                                             |
| ------------------- | ----------------------------- | --------------------------------------------------------------------------------- |
| `glm-latest`        | All-around use, agentic tasks | Default for `main` and `opus` slots in Claude Code. Strong reasoning, 1M context. |
| `glm-5p1`           | General use (lighter)         | Default `sonnet` slot in Claude Code. Good balance of speed and quality.          |
| `deepseek-v4-flash` | Background / fast tasks       | Default `haiku` and `subagent` slots in Claude Code. Lowest latency.              |

### Fire Pass keys

Fire Pass keys (`fpk_...`) default all slots to `glm-latest`. The model browser shows Fire Pass-supported models: `glm-latest`, `kimi-fast-latest`, and `kimi-k2p7-code-fast`.

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
