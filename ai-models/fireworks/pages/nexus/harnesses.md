---
title: "Coding Harnesses"
source: https://docs.fireworks.ai/nexus/harnesses
path: nexus/harnesses
---

Connect Claude Code, OpenCode, Codex, Pi, Cursor IDE, VS Code, Copilot, or DeepSeek Harness to Fireworks

Install [FireConnect](/nexus/fireconnect) and run `fireconnect login` once. Then choose your harness below. Each section shows the connect command, the settings FireConnect writes, and how to apply a new `--model`.

## Shared rules

* **Auth:** `fireconnect login` once, then `fireconnect <harness>`. You do not need `--api-key` on connect when a key is already saved.
* **Quit first:** fully quit Cursor IDE, VS Code, and the Copilot App before connecting or running `off`. Restart other harnesses after connect.
* **`status` is read-only** while the app is open.
* **Models:** Pass `--model <id>` when you connect. Browse IDs with `fireconnect model list`. See [FireRouter](/nexus/firerouter) for router behavior.
* **Web search:** Claude Code, Codex, and ChatGPT keep native search. See [Web Search](/nexus/web-search) for details.

## Claude Code

```bash wrap theme={null}
fireconnect login
fireconnect claude                  # appends the catalog to /model
fireconnect claude status
```

Connection and model changes take effect in a new or resumed session. Exit and resume with `claude --resume <id>`, or start a new session.

**Model picker.** FireConnect adds `auto`, model routers, and Fireworks models to `/model`. Native Anthropic tiers remain unchanged. `--model` adds a row; it does not pin the default:

```bash wrap theme={null}
fireconnect claude --model firerouter
fireconnect claude --model glm-5p3-flash
```

**What gets written**

* Fireworks key in `ANTHROPIC_CUSTOM_HEADERS` (`X-Fireworks-Api-Key`), backup under `~/.fireconnect/` for `off`.
* Serverless rows in `/model`; `[1m]` tag on 1M-context models.
* Optional `statusLine` unless you already have one.
* Native web search and fetch stay on.

**Usage.** For the status line and `fireconnect claude usage`, see [Usage and Cost](/nexus/metrics). For a side-by-side model comparison, see the [Side-by-Side Demo](/nexus/demo).

**Routers**

* Bare `firerouter` and routes containing a Claude family alias or Anthropic model ID can use your Claude login.
* `firerouter/astra` requires an OpenAI key configured in [Provider Keys](/nexus/provider-keys).
* See [Harness Compatibility](/nexus/harness-compatibility) for `--routing-preference` and `--anthropic-api-key`.

**Troubleshooting**

* Text-only models fail on pasted images. Use `/rewind`.
* Claude Code calculates its in-app cost with Anthropic list prices. Use the FireConnect status line for the Fireworks estimate.
* Resume or restart the session after changing models.

## OpenCode

```bash wrap theme={null}
fireconnect login
fireconnect opencode
fireconnect opencode status
```

Restart OpenCode after connecting. With a standard Fireworks key, the default model is `auto`, stored as `fireworks-ai/auto`. FireConnect expands short model IDs to full Fireworks paths automatically.

<Frame>
  <img alt="OpenCode model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and other models" />
</Frame>

**What gets written**

* A `fireworks-ai` provider using the OpenAI-compatible endpoint at `https://api.fireworks.ai/inference/v1`
* The default model and serverless `/model` catalog in `~/.config/opencode/opencode.json`
* The API key in that file with mode `0600`

FireConnect snapshots the original file under `~/.fireconnect/opencode/`. It never changes `auth.json`. Use `--config-path` for a configuration stored elsewhere.

```bash wrap theme={null}
fireconnect model list --search glm
fireconnect opencode --model glm-5p2
```

Without FireConnect, OpenCode can also connect directly: `/connect` → search **fireworks.ai** → paste your key → `/models` to pick.

## Codex

`fireconnect codex` and `fireconnect chatgpt` share one config. The Codex CLI and the ChatGPT desktop app route through Fireworks with a single command. **Quit the ChatGPT app** before connecting or running `off` so its model list refreshes. Native web search stays on.

**ChatGPT connectors.** Connectors you added before connecting continue to work. You cannot add a new connector while connected.

```bash wrap theme={null}
fireconnect login
fireconnect codex
```

`config.toml` updates immediately; exit Codex and `codex resume <id>` (or start fresh) to load it. With a standard Fireworks key, the default model is `auto`.

To add FireRouter to the Codex and ChatGPT pickers, reconnect with `fireconnect codex --model firerouter`.

<Frame>
  <img alt="Codex CLI model picker showing Auto selected, FireRouter, and Fireworks DeepSeek, GLM, and Kimi models" />
</Frame>

<Frame>
  <img alt="ChatGPT desktop model picker showing FireRouter selected alongside Auto and Fireworks models" />
</Frame>

**What gets written**

* Root `model_provider` and `model` values in `~/.codex/config.toml`
* A `[model_providers.fireworks-ai]` block using the Responses API
* The API key in `config.toml` with mode `0600`
* A serverless catalog at `~/.codex/fireworks-model-catalog.json`, linked through `model_catalog_json`

FireConnect preserves unrelated TOML settings and snapshots the original under `~/.fireconnect/codex/`. Use `--config-path` for a configuration stored elsewhere.

```bash wrap theme={null}
fireconnect codex status
fireconnect codex --model glm-5p2
```

When you resume an old session, explicitly select its provider: `codex resume <id> -c model_provider="fireworks-ai"` (or `"fireworks-azure"` on the Foundry path).

<Warning>
  **MiniMax models don't work on Codex.** Codex may insert assistant messages between `tool_calls` and `tool_results`, which MiniMax templates reject. Use a Chat Completions harness (Claude Code, OpenCode) for MiniMax.
</Warning>

## Pi

```bash wrap theme={null}
fireconnect login
fireconnect pi
fireconnect pi status
```

Restart Pi after connecting if it was already running. With a standard Fireworks key, the default model is `auto`.

**What gets written**

* `defaultProvider` and `defaultModel` in `~/.pi/agent/settings.json`
* The API key in `auth.json` with mode `0600`
* The serverless catalog in `~/.pi/agent/models.json`

FireConnect snapshots all three files under `~/.fireconnect/pi/`. It tracks the IDs it adds so `off` removes only those entries. Use `--settings-path` for a settings file stored elsewhere.

```bash wrap theme={null}
fireconnect model list --search glm
fireconnect pi --model glm-5p2
```

## Cursor IDE

`fireconnect cursor` configures Cursor IDE. Cursor CLI (`agent` or `cursor-agent`) is not supported.

Cursor IDE keeps AI settings in SQLite (`state.vscdb`). **Fully quit Cursor IDE before connecting or running `off`.** In an interactive terminal FireConnect waits for you (or `--force` to write anyway). `status` is read-only while Cursor IDE runs.

```bash wrap theme={null}
fireconnect login
fireconnect cursor
fireconnect cursor status
```

Connecting updates every existing mode in `modelConfig` to use the Fireworks default. FireConnect never creates modes. It also registers the serverless catalog in the picker. `status` shows the model assigned to each mode. Reopen Cursor IDE and choose a Fireworks model.

<Frame>
  <img alt="Cursor IDE model picker showing Auto selected with Fireworks DeepSeek, GLM, Kimi, and MiniMax models" />
</Frame>

**What gets written** (under `~/.config/Cursor`, `~/Library/Application Support/Cursor`, or `%APPDATA%\Cursor`):

| Setting          | Location                                                  |
| ---------------- | --------------------------------------------------------- |
| API key          | `cursorAuth/openAIKey`                                    |
| Base URL         | `openAIBaseUrl` → `https://api.fireworks.ai/inference/v1` |
| Custom models    | `aiSettings.userAddedModels` (tracked for clean `off`)    |
| Hidden built-ins | `aiSettings.modelOverrideDisabled`                        |
| Per-mode model   | `aiSettings.modelConfig[<mode>]`                          |

Your previous auth state is snapshotted under `~/.fireconnect/cursor/`. Use `--db-path` for a non-default `state.vscdb` (for example Insiders).

<Warning>
  **While connected, only Fireworks models work.** Built-ins are hidden. `off` brings them back. Cursor IDE also enforces a server-side allowlist, so not every Fireworks model is selectable even after registering. Some Cursor IDE features may still use the IDE's own backend depending on plan and version.
</Warning>

Without FireConnect: add a Custom Model with a Fireworks ID, set Override OpenAI Base URL to `https://api.fireworks.ai/inference/v1`, paste your key.

## VS Code

FireConnect adds a `Fireworks` provider to GitHub Copilot Chat's custom endpoints. Requires Copilot **Pro or Enterprise** (free tier only supports Auto). **Quit VS Code before connecting or running `off`**; `status` is read-only while running.

```bash wrap theme={null}
fireconnect login
fireconnect vscode
fireconnect vscode status
```

Restart VS Code, then pick a Fireworks model under **Other Models → Fireworks** in Copilot Chat. Vision support comes from the current model catalog. `glm-latest` and `glm-fast-latest` are text-only; `glm-5p3-flash` supports images. Run `fireconnect model list` to check other model IDs.

<Frame>
  <img alt="VS Code Chat model picker showing the Fireworks provider with Auto selected and DeepSeek, GLM, and Kimi models" />
</Frame>

**What gets written.** FireConnect adds a custom endpoint to `chatLanguageModels.json`. VS Code appends `/v1/chat/completions` to `https://api.fireworks.ai/inference`. FireConnect also stores the API key in `state.vscdb` under `chat.lm.secret.fw-*`, encrypted through Electron `safeStorage`:

| Platform | `chatLanguageModels.json`                  | `state.vscdb`                                            |
| -------- | ------------------------------------------ | -------------------------------------------------------- |
| Linux    | `~/.config/Code/User/`                     | `~/.config/Code/User/globalStorage/`                     |
| macOS    | `~/Library/Application Support/Code/User/` | `~/Library/Application Support/Code/User/globalStorage/` |
| Windows  | `%APPDATA%\Code\User\`                     | `%APPDATA%\Code\User\globalStorage\`                     |

On macOS, VS Code encrypts the key through the login Keychain. Open VS Code once before connecting. On Linux, encryption requires `libsecret`; otherwise, Chromium uses obfuscation and FireConnect warns you.

FireConnect snapshots the original JSON under `~/.fireconnect/vscode/`. `off` restores that file and deletes the secret row. Use `--vscode-path` for a non-default configuration path. For UI setup, see [GitHub Copilot](/ecosystem/integrations/github-copilot).

## Copilot App

The GitHub Copilot **desktop app** routes through Fireworks without changing its built-in models. FireConnect adds a provider alongside them. **Quit the app before connecting or running `off`.** `status` is read-only while the app runs. The app and CLI both store files under `~/.copilot`, but they use separate settings and are configured independently.

```bash wrap theme={null}
fireconnect login
fireconnect copilot-app
fireconnect copilot-app status
```

Reopen the app and pick a Fireworks model in Settings → Model providers.

To add FireRouter to the picker, reconnect with `fireconnect copilot-app --model firerouter`.

<Frame>
  <img alt="GitHub Copilot desktop app model picker showing Auto selected from Fireworks alongside FireRouter, DeepSeek, GLM, Kimi, and MiniMax models" />
</Frame>

**What gets written** to `~/.copilot/data.db` (SQLite, movable via `COPILOT_HOME`):

| Table             | What FireConnect adds                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| `model_providers` | One row, id starting `fc-`, named `Fireworks`, type `openai`                                                       |
| `settings_json`   | `baseUrl` → `https://api.fireworks.ai/inference/v1`, `wireApi: completions`, your key as an `Authorization` header |
| `provider_models` | One row per model: name, display name, token limits, reasoning efforts (`low`/`medium`/`high`/`max`)               |

`off` deletes the `fc-` provider and its models. The desktop app's BYOK path does not support image input, the hover-card Context row, or AI-credits pricing. Billing runs through Fireworks. Use `--db-path` for a non-default database.

## Copilot CLI

The **`copilot` command** (`@github/copilot`) reads plain JSON, never the desktop app's database.

```bash wrap theme={null}
fireconnect login
fireconnect copilot-cli
fireconnect copilot-cli status
```

Restart `copilot` after enabling.

<Frame>
  <img alt="Copilot CLI model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and MiniMax models" />
</Frame>

**What gets written** under `~/.copilot`:

| File             | What FireConnect writes                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `providers.json` | One `providers[]` entry named `fireworks` + one `models[]` entry per model (limits, per-model vision, and a reasoning toggle) |
| `settings.json`  | The selected `model`. The CLI requires this because BYOK providers do not define a default                                    |

**Use provider-prefixed model IDs:** use `fireworks/glm-latest`, not bare `glm-latest`. The CLI rejects a bare model name and silently falls back to its configured model.

Switch models with `copilot --model fireworks/<name>` or `/model`. The CLI supports image input according to each model's catalog entry.

Because `providers.json` is user-editable, `off` restores its snapshot or deletes the file if FireConnect created it. Your existing entries remain intact. Use `--providers-path` for a non-default location.

## DeepSeek Harness

DeepSeek's coding agent (`dsh`) routes through a custom OpenAI-compatible provider under `$DSH_HOME` (default `~/.dsh`). Restart `dsh` after connecting or running `off`.

```bash wrap theme={null}
fireconnect login
fireconnect deepseek
fireconnect deepseek status
```

With a standard Fireworks key, the default model is `auto`.

**What gets written**

* A `fireworks` provider under `llm-pi-ai.providers` in `settings.yaml`
* `agent-default-model` set to the selected model
* The API key as `FIREWORKS_API_KEY` in `.credentials.yaml` with mode `0600`

FireConnect snapshots both files under `~/.fireconnect/deepseek/`. Use `--config-path` for a different `settings.yaml`; the credentials file stays beside it.

```bash wrap theme={null}
fireconnect model list --search glm
fireconnect deepseek --model glm-5p2
```

## Foundry across harnesses

[Microsoft Foundry](/nexus/microsoft-foundry) runs Fireworks models in your Azure subscription and bills usage through Azure. Direct FireConnect routing supports **OpenCode, Codex, Pi, Cursor IDE, and VS Code**. Direct routing does not support Claude Code, DeepSeek Harness, Copilot, or model routers.

Pass the Foundry **deployment name** (`FW-GLM-5.2`), not a Fireworks short ID. Setup, switching, and restore behavior: [Microsoft Foundry](/nexus/microsoft-foundry).

<Note>
  **Need Claude Code on Foundry?** Use an LLM gateway between Claude Code and Foundry. Two proven patterns are Claude Code to Envoy AI Gateway to Foundry, and Claude Code to LiteLLM to Foundry. The gateway translates requests and responses. FireConnect does not configure this path. See [Microsoft Foundry](/nexus/microsoft-foundry#claude-code-through-a-gateway) for details and a reference implementation.
</Note>
