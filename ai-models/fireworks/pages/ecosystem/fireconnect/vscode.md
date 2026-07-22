---
title: "VS Code"
source: https://docs.fireworks.ai/ecosystem/fireconnect/vscode
path: ecosystem/fireconnect/vscode
---

Use Fireworks AI models in GitHub Copilot Chat with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) adds Fireworks AI models to **[GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) Chat** in [Visual Studio Code](https://code.visualstudio.com) by writing a custom language-model endpoint. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

<Card title="Manual setup (GitHub Copilot)" icon="github" href="/ecosystem/integrations/github-copilot">
  Step-by-step UI walkthrough with screenshots — add a Fireworks custom endpoint without the FireConnect CLI
</Card>

## Prerequisites

* [Visual Studio Code](https://code.visualstudio.com) with the [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) extension
* GitHub Copilot **Pro** or **Enterprise** (the free tier only supports the Auto model)
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* The FireConnect CLI (see [Install](/ecosystem/fireconnect/overview#install))

<Note>
  **Azure routing not implemented yet for VS Code.** `fireconnect vscode on` always configures direct Fireworks, even when global config has `--provider azure` or you pass `--azure`. See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry#supported-harnesses).
</Note>

## Enable Fireworks routing

VS Code stores custom-endpoint API keys (encrypted) in `state.vscdb`. **Quit VS Code** before running `on` or `off` — FireConnect hard-errors if VS Code is still running unless you pass `--force`.

```bash theme={null}
fireconnect login
fireconnect vscode on
```

Or pass the key once:

```bash theme={null}
fireconnect vscode on --api-key fw_...
```

Start or restart VS Code, then open Copilot Chat and pick a Fireworks model from the model picker.

```bash theme={null}
fireconnect vscode status   # read-only — works while VS Code is running
```

## Browse and add models

`model list`, `model add`, `model select`, and `model reset` only edit `chatLanguageModels.json`. VS Code hot-reloads that file — **no restart needed** for model changes.

```bash theme={null}
fireconnect vscode model list              # browse serverless endpoints
fireconnect vscode model list --search glm
fireconnect vscode model add glm-fast-latest
fireconnect vscode model add deepseek-v4-pro
fireconnect vscode model select            # pick a model to add interactively
```

Short model IDs are expanded to full Fireworks paths. FireConnect writes model metadata (display name, token limits, tool calling, and vision flags) into your Copilot language-model config.

In Copilot Chat, open the model picker (**Auto**), expand **Other Models**, and choose your model under **Fireworks**.

## What gets written

FireConnect merges a **Fireworks** custom endpoint into VS Code's language-model config and stores the API key in VS Code's secret storage:

| What              | Where                                                             |
| ----------------- | ----------------------------------------------------------------- |
| Provider + models | `chatLanguageModels.json`                                         |
| Encrypted API key | `state.vscdb` (`ItemTable`, key `secret://chat.lm.secret.fw-...`) |

Platform paths:

| Platform | `chatLanguageModels.json`                                         | `state.vscdb`                                                       |
| -------- | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| Linux    | `~/.config/Code/User/chatLanguageModels.json`                     | `~/.config/Code/User/globalStorage/state.vscdb`                     |
| macOS    | `~/Library/Application Support/Code/User/chatLanguageModels.json` | `~/Library/Application Support/Code/User/globalStorage/state.vscdb` |
| Windows  | `%APPDATA%\Code\User\chatLanguageModels.json`                     | `%APPDATA%\Code\User\globalStorage\state.vscdb`                     |

The endpoint uses model URL `https://api.fireworks.ai/inference` (VS Code appends `/v1/chat/completions`). The API key is **not** stored in the JSON — VS Code resolves the `${input:chat.lm.secret.<id>}` reference through its secret storage.

On macOS, `safeStorage` encrypts with a master key VS Code stores in the login Keychain. On Linux, `safeStorage` needs `libsecret` (`secret-tool`) for real encryption — without it, Chromium falls back to a hardcoded password (obfuscated, not encrypted), which FireConnect still writes but warns about.

FireConnect snapshots the original `chatLanguageModels.json` under `~/.fireconnect/vscode/` before the first change. Running `fireconnect vscode off` restores it byte-for-byte and deletes the `chat.lm.secret.fw-*` secret row from `state.vscdb`.

## CLI reference

```bash theme={null}
fireconnect vscode on              # Add the Fireworks provider (quit VS Code first)
fireconnect vscode off             # Restore config and remove the stored key
fireconnect vscode status          # Show provider, auth, and registered models
fireconnect vscode model list      # Browse serverless endpoints
fireconnect vscode model add <id>  # Add a model (hot-reloads)
fireconnect vscode model select    # Pick a model to add interactively
fireconnect vscode model reset     # Reset fireconnect-managed models to default
fireconnect vscode help            # Show harness-specific help
```

Run `fireconnect vscode help` for all options, including `--vscode-path` (explicit `chatLanguageModels.json` path) and `--force`.

### Turn off Fireworks routing

Quit VS Code, then run:

```bash theme={null}
fireconnect vscode off
```

This restores your previous `chatLanguageModels.json` from the backup in `~/.fireconnect/vscode/` and removes the FireConnect secret from `state.vscdb`. Restart VS Code for the change to take effect.

## Related

* [GitHub Copilot integration guide](/ecosystem/integrations/github-copilot) — manual custom-endpoint setup with screenshots
* [Cursor](/ecosystem/fireconnect/cursor) — use Fireworks models in Cursor IDE

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
