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
* The FireConnect CLI (see [Install](/ecosystem/fireconnect/overview#install))

<Note>
  **Azure routing not implemented yet for Cursor.** `fireconnect cursor on` always configures direct Fireworks (`https://api.fireworks.ai/inference/v1`), even when global config has `--provider azure` or you pass `--azure`. See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry#supported-harnesses).
</Note>

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

`cursor on` sets **every mode that already exists** in `modelConfig` to the default Fireworks model (non-destructive — it won't create mode entries that aren't already there). Use `cursor model select --mode <mode>` to point an individual mode at a different model.

Quit and reopen Cursor for the change to take effect, then open the model picker and choose a Fireworks model.

```bash theme={null}
fireconnect cursor status   # read-only — works while Cursor is running
```

## Browse and pick models

`model list` and `status` are read-only and work while Cursor is running. Commands that write to `state.vscdb` require Cursor to be quit first.

```bash theme={null}
fireconnect cursor model list              # browse serverless endpoints
fireconnect cursor model list --search glm
fireconnect cursor model select            # pick a model for a Cursor mode
fireconnect cursor model select --mode composer
fireconnect cursor model add glm-fast-latest
fireconnect cursor model add deepseek-v4-flash
```

Short model IDs are expanded to full Fireworks paths automatically.

Cursor modes you can pass to `--mode` include `composer` (default), `cmd-k`, `background-composer`, `composer-ensemble`, `plan-execution`, `spec`, `deep-search`, and `quick-agent`. Run `fireconnect cursor status` to see the current model for each mode.

<Warning>
  Cursor enforces an allowlist on the server side. Not every Fireworks model appears in the picker even after you add it. Models such as GLM 5.2 and Kimi K2.6 are known to work; if a model is blocked, Cursor shows an error when you select it.
</Warning>

## What gets written

FireConnect writes Cursor's BYOK OpenAI settings in the local SQLite state database at `state.vscdb`:

| Setting        | Location                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------- |
| API key        | `cursorAuth/openAIKey` (plaintext)                                                           |
| Base URL       | `openAIBaseUrl` on the `applicationUser` blob — `https://api.fireworks.ai/inference/v1`      |
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
fireconnect cursor model add glm-fast-latest
```

Fire Pass keys default to `glm-fast-latest`.

## CLI reference

```bash theme={null}
fireconnect cursor on                    # Enable Fireworks routing (quit Cursor first)
fireconnect cursor off                   # Restore your previous Cursor auth state
fireconnect cursor status                # Show provider, auth, modes, and per-mode models
fireconnect cursor model list            # Browse serverless endpoints
fireconnect cursor model add <id>        # Add a model to Cursor's picker
fireconnect cursor model select          # Pick a model for a mode (--mode)
fireconnect cursor model reset           # Reset fireconnect-managed model selections
fireconnect cursor help                  # Show harness-specific help
```

Run `fireconnect cursor help` for all options, including `--db-path` (explicit `state.vscdb` path) and `--force` (write even if Cursor appears to be running — not recommended).

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

FireConnect automates these steps and makes it easy to add or swap models from the terminal.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
