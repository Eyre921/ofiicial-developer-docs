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

Requires Node.js 18 or later, `git`, and `bash`. On Windows, run it from Git Bash; PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks key.

Already set up? Skip to step 2.

**2. Quit Cursor IDE**

**Fully quit Cursor IDE before connecting or running `off`.**

**3. Connect Cursor IDE**

```bash wrap theme={null}
nexus cursor
nexus cursor status
```

Nexus CLI points every existing mode in `modelConfig` at the Fireworks default and registers the catalog in the picker.

**4. Reopen and pick a model**

Reopen Cursor IDE and choose a Fireworks model.

![Cursor IDE model picker showing Auto selected with Fireworks DeepSeek, GLM, Kimi, and MiniMax models](https://mintcdn.com/fireworksai/DBOQdoU3Q63xUkRQ/images/nexus/cursor-ide-model-picker.png?fit=max\&auto=format\&n=DBOQdoU3Q63xUkRQ\&q=85\&s=8800ed6ae6cf56db81205d2f342011a2)

> [!TIP]
>
> `nexus cursor status` shows the provider, where the key comes from, and the configured model.

> [!WARNING]
>
> **While connected, only Fireworks models work.** Cursor IDE's built-in models are hidden until you run `off`. Cursor IDE also enforces a server-side allowlist, so not every Fireworks model is selectable. Some features may still use Cursor's own backend, depending on plan and version.

## Use Nexus Auto

Nexus CLI registers Nexus Auto in Cursor IDE as `nexus/auto`, because Cursor reserves the bare `auto` name for its own model picker. Cursor IDE cannot send a local Anthropic or OpenAI key. Without a matching [Provider Key](/nexus/provider-keys), Nexus Auto serves every turn with open models. Cursor IDE can't send extra headers, so manual setup needs Provider Keys too. `nexus auto --providers` has no effect in Cursor IDE.

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in Cursor IDE as usual.

Nexus CLI does not add web search to Cursor IDE. See [Web Search](/nexus/web-search).

## Troubleshooting

* **`Model name is not valid: "auto"`, or the same error for another Fireworks ID:** Cursor IDE stopped sending your Fireworks key. Cursor can turn the key off after Fireworks rejects a request, such as when the key is revoked or a model ID is not found. Without a key, Cursor treats Fireworks IDs as unknown models. Open **Settings → Models**, turn **OpenAI API Key** back on, and retry.
* **The key was revoked:** turning it back on is not enough. Run `nexus login --force` for a new key, fully quit Cursor IDE, and run `nexus cursor`. With manual setup, paste a new key from [Fireworks settings](https://app.fireworks.ai/settings/users/api-keys).

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
> Cursor IDE stores AI settings in SQLite (`state.vscdb` under `~/.config/Cursor`, `~/Library/Application Support/Cursor`, or `%APPDATA%\Cursor`):
>
> | Setting | Value |
> | - | - |
> | `cursorAuth/openAIKey` | Your Fireworks key |
> | `openAIBaseUrl` | `https://api.fireworks.ai/inference/v1` |
> | `aiSettings.userAddedModels` | The Fireworks catalog, tracked for a clean `off` |
> | `aiSettings.modelOverrideDisabled` | Cursor's built-in models, hidden while connected |
> | `aiSettings.modelConfig[<mode>]` | The Fireworks model for each mode |
>
> Your previous auth state is saved under `~/.nexus/cursor/`. Use `--db-path` for a non-default `state.vscdb`.
