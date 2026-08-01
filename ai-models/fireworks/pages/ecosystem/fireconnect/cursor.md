---
title: "Cursor"
source: https://docs.fireworks.ai/ecosystem/fireconnect/cursor
path: ecosystem/fireconnect/cursor
---

Use Fireworks AI models in Cursor IDE with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [Cursor](https://cursor.com) through Fireworks AI models via Cursor's OpenAI-compatible BYOK path. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

## Prerequisites

* [Cursor](https://cursor.com) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* FireConnect **v0.9.1+** (see [Install](/ecosystem/fireconnect/overview#install))

<Note>
  **Azure routing not implemented yet for Claude Code.** `fireconnect claude on` always configures direct Fireworks, even when global config has `--provider azure` or you pass `--azure`. See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry#supported-harnesses).
</Note>

<Warning>
  **FireRouter is not supported in Cursor.** Use Claude Code, OpenCode, Codex, Pi, or VS Code for FireRouter. Fire Pass keys cannot select `firerouter` in FireConnect on any harness.
</Warning>

## Enable Fireworks routing

Cursor stores AI settings in a SQLite database (`state.vscdb`). **Fully quit Cursor** before running commands that write to it (for example, **Cmd+Q** on macOS or close all Cursor windows on Linux). Otherwise Cursor's in-memory state can overwrite FireConnect's changes.

In an interactive terminal, if Cursor is still running FireConnect asks you to quit it and press Enter to continue. Pass `--force` to write anyway without waiting.

```bash theme={null}
fireconnect login
fireconnect cursor on
```

Or pass the key once:

```bash theme={null}
fireconnect cursor on --api-key fw_...
```

`cursor on` sets **every mode that already exists** in `modelConfig` to the default Fireworks model (non-destructive: it won't create mode entries that aren't already there) and registers the preferred serverless catalog in the picker.

Quit and reopen Cursor for the change to take effect, then open the model picker and choose a Fireworks model.

```bash theme={null}
fireconnect cursor status   # read-only; works while Cursor is running
```

## Browse and pick models

Browse the global catalog, then switch models with `on`:

```bash theme={null}
fireconnect model list --search glm
fireconnect cursor on --model glm-fast-latest
```

`fireconnect model list` and `status` are read-only and work while Cursor is running. Commands that write to `state.vscdb` (`on`, `off`) require Cursor to be quit first.

Short model IDs are expanded to full Fireworks paths automatically.

Cursor modes include `composer` (default), `cmd-k`, `background-composer`, `composer-ensemble`, `plan-execution`, `spec`, `deep-search`, and `quick-agent`. Run `fireconnect cursor status` to see the current model for each mode.

<Warning>
  Cursor enforces an allowlist on the server side. Not every Fireworks model appears in the picker even after you add it. Models such as GLM 5.2 and Kimi K2.6 are known to work; if a model is blocked, Cursor shows an error when you select it.
</Warning>

<Warning>
  **While FireConnect is on, only Fireworks models in your picker work.** Cursor subscription models, Opus modes, and other built-in models won't respond. Run `fireconnect cursor off` to restore built-in Cursor models.
</Warning>

## What gets written

FireConnect writes Cursor's BYOK OpenAI settings in the local SQLite state database at `state.vscdb`:

| Setting        | Location                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------- |
| API key        | `cursorAuth/openAIKey` (plaintext)                                                           |
| Base URL       | `openAIBaseUrl` on the `applicationUser` blob: `https://api.fireworks.ai/inference/v1`       |
| Custom models  | `aiSettings.userAddedModels` + `aiSettings.fireconnectAddedModels` (tracked for clean `off`) |
| Per-mode model | `aiSettings.modelConfig[<mode>]`                                                             |

Platform paths for `state.vscdb`:

| Platform | Path                                                                  |
| -------- | --------------------------------------------------------------------- |
| Linux    | `~/.config/Cursor/User/globalStorage/state.vscdb`                     |
| macOS    | `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb` |
| Windows  | `%APPDATA%\Cursor\User\globalStorage\state.vscdb`                     |

FireConnect snapshots your previous Cursor auth state under `~/.fireconnect/cursor/` before the first change. Running `fireconnect cursor off` restores it. `off` only removes models FireConnect registered; your own custom models are preserved.

## Cursor feature coverage

FireConnect configures Cursor's OpenAI BYOK path. Features that route through that path can use Fireworks models.

Some Cursor features (for example, Composer, inline edit, and autocomplete) may still use Cursor's own backend depending on your plan and Cursor version. Test the workflows you care about after enabling.

## Using Fire Pass

Use your `fpk_...` key during `login` or with `--api-key`:

```bash theme={null}
fireconnect cursor on --api-key fpk_...
```

Fire Pass keys default to `kimi-fast-latest`.

## CLI reference

```bash theme={null}
fireconnect cursor on                    # Enable Fireworks routing (quit Cursor first)
fireconnect cursor off                   # Restore your previous Cursor auth state
fireconnect cursor status                # Show provider, auth, modes, and per-mode models
fireconnect cursor help                  # Show harness-specific help
```

Run `fireconnect cursor help` for all options, including `--db-path` (explicit `state.vscdb` path) and `--force` (write even if Cursor appears to be running; not recommended).

### Turn off Fireworks routing

Quit Cursor, then run:

```bash theme={null}
fireconnect cursor off
```

This restores your previous Cursor auth state from the backup in `~/.fireconnect/cursor/`. Quit and reopen Cursor for full effect.

## Manual setup

You can also configure Cursor without FireConnect:

1. In Cursor settings, add a **Custom Model** with a Fireworks model ID (for example, `accounts/fireworks/models/glm-5p2` or a short alias like `glm-fast-latest`).
2. Set **Override OpenAI Base URL** to `https://api.fireworks.ai/inference/v1`.
3. Paste your Fireworks or Fire Pass API key.

FireConnect automates these steps and makes it easy to swap models from the terminal.

## Fireworks on Microsoft Foundry

Cursor supports **Fireworks on Microsoft Foundry** (CLI: `--provider azure` or `on --azure`). See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry) and the [portal setup guide](/ecosystem/integrations/azure-foundry).

<Warning>
  Foundry routing requires a standard Azure API key. Fire Pass keys (`fpk_...`) are not supported. **Quit Cursor** before `on` or `off`.
</Warning>

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect cursor on --model FW-GLM-5.2
```

One-off routing without changing global config:

```bash theme={null}
fireconnect cursor on \
  --azure \
  --base-url https://<resource>.services.ai.azure.com \
  --model FW-MiniMax-M2.5
```

Pass your Foundry model with `--model` (for example, `FW-GLM-5.2`), not a Fireworks serverless short ID.

FireConnect points Cursor's OpenAI BYOK override at your Foundry OpenAI-compatible endpoint and registers the deployment in the model picker. `fireconnect model list` only browses the Fireworks serverless catalog on the direct gateway path.

To switch back to the Fireworks gateway:

```bash theme={null}
fireconnect configure --provider fireworks
fireconnect cursor on
```

See [Turn off Foundry routing](/ecosystem/fireconnect/microsoft-foundry#turn-off-foundry-routing) for `off` and global config behavior.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
