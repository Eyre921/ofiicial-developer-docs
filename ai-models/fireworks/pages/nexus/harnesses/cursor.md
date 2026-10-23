---
title: "Cursor IDE"
source: https://docs.fireworks.ai/nexus/harnesses/cursor
path: nexus/harnesses/cursor
---

Connect Cursor IDE to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

`nexus cursor` configures Cursor IDE. Cursor CLI (`agent` or `cursor-agent`) is not supported.

PreviewOpenAI Chat CompletionsNexus Auto with Provider Keys

## Quick start

**1. Install and sign in**

```bash wrap theme={null}
curl -fsSL https://nexus.fireworks.ai/install.sh | bash
```

You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks API key (`fw_...`).

Already set up? Skip to step 2.

**2. Quit Cursor IDE**

**Fully quit Cursor IDE before you connect or run `off`.** A running Cursor IDE overwrites the change from memory. If it's open, Nexus CLI waits until you quit. `--force` writes anyway, which isn't recommended.

**3. Connect Cursor IDE**

```bash wrap theme={null}
nexus cursor
nexus cursor status
```

Nexus CLI registers the Fireworks catalog in the picker and points every mode you already have in `modelConfig` at the default model. It never adds modes.

**4. Reopen and pick a model**

Reopen Cursor IDE and choose a Fireworks model. The default is `nexus/auto`. To change the default for every mode, run `nexus cursor --model glm-latest`.

![Cursor IDE model picker showing Auto selected with Fireworks DeepSeek, GLM, Kimi, and MiniMax models](https://mintcdn.com/fireworksai/DBOQdoU3Q63xUkRQ/images/nexus/cursor-ide-model-picker.png?fit=max\&auto=format\&n=DBOQdoU3Q63xUkRQ\&q=85\&s=8800ed6ae6cf56db81205d2f342011a2)

Cursor IDE after Nexus CLI, with Auto selected

> [!TIP]
>
> `nexus cursor status` shows the provider, where the key comes from, and the configured model.

> [!WARNING]
>
> **While connected, only Fireworks models work.** Cursor IDE's built-in models are hidden until you run `off`. Cursor IDE also enforces a server-side allowlist, so not every Fireworks model is selectable. Some features may still use Cursor's own backend, depending on plan and version.

## Use Nexus Auto

Nexus CLI registers Nexus Auto in Cursor IDE as `nexus/auto`, because Cursor reserves the bare `auto` name for its own router.

* **Anthropic and OpenAI model turns:** connect a [Provider Key](/nexus/provider-keys). Cursor IDE can't send extra headers, so Nexus CLI doesn't send keys saved with `nexus auto`, and manual setup can't add them either. Without a Provider Key, Nexus Auto serves every turn with open models.
* **Provider scope:** `nexus auto --providers` has no effect in Cursor IDE.

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in Cursor IDE as usual.

Nexus CLI does not add web search to Cursor IDE. See [Web Search](/nexus/web-search).

## Microsoft Foundry

Nexus CLI can connect Cursor IDE to Fireworks models deployed in your Azure subscription. See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry). Nexus Auto is not available on Foundry.

## Troubleshooting

* **`Model name is not valid: "auto"`, or the same error for another Fireworks ID:** Cursor IDE stopped sending your Fireworks key. Cursor can turn the key off after Fireworks rejects a request, such as when the key is revoked or a model ID is not found. Without a key, Cursor treats Fireworks IDs as unknown models. Open **Settings → Models**, turn **OpenAI API Key** back on, and retry.
* **The key was revoked:** turning it back on is not enough. Run `nexus login --force` for a new key, fully quit Cursor IDE, and run `nexus cursor`. With manual setup, paste a new key from [Fireworks settings](https://app.fireworks.ai/settings/users/api-keys).

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness.

## Manual setup (advanced)

**1. Open model settings**

In Cursor IDE, open **Settings**, then **Models**.

**2. Add your Fireworks key**

Under **API Keys**, paste your Fireworks key into **OpenAI API Key**. Turn on **Override OpenAI Base URL** and enter `https://api.fireworks.ai/inference/v1`.

**3. Add a model**

Add a custom model with a Fireworks ID, such as `glm-latest`, then select it in chat.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> Cursor IDE stores AI settings in SQLite, in `User/globalStorage/state.vscdb` under `~/.config/Cursor` (Linux), `~/Library/Application Support/Cursor` (macOS), or `%APPDATA%\Cursor` (Windows):
>
> | Setting | Value |
> | - | - |
> | `secret://cursorAuth/openAIKey` | Your Fireworks key, encrypted with Electron `safeStorage` |
> | `cursorAuth/openAIKey` | The same key in plain text, for older Cursor builds |
> | `openAIBaseUrl` | `https://api.fireworks.ai/inference/v1` |
> | `useOpenAIKey` | `true` |
> | `aiSettings.userAddedModels` | The Fireworks catalog, tracked for a clean `off` |
> | `aiSettings.modelOverrideDisabled` | Cursor's built-in models, hidden while connected |
> | `aiSettings.modelConfig[<mode>]` | The Fireworks model for each mode |
>
> On Linux, encryption needs `libsecret`. Without it, Cursor IDE only obfuscates the key and Nexus CLI warns you.
>
> `off` restores your previous AI settings and key from the snapshot under `~/.nexus/cursor/`. Without a snapshot, it removes only what Nexus CLI added. Use `--db-path` for a non-default `state.vscdb`.
