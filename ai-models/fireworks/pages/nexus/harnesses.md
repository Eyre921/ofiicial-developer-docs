---
title: "Coding Harnesses"
source: https://docs.fireworks.ai/nexus/harnesses
path: nexus/harnesses
---

Connect Claude Code, Claude Agent SDK, Claude Desktop, Codex, the ChatGPT app, OpenCode, Pi, Cursor, VS Code, Copilot, or DeepSeek Harness to Fireworks.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

Most harnesses below work two ways. **FireConnect** writes the settings for you and restores them with `off`. **Manual setup** shows the same settings so you can apply them yourself, with no extra tool installed. Claude Desktop is FireConnect only.

> **[Claude Code](#claude-code)**
>
> Messages API

> **[Claude Desktop](#claude-desktop)**
>
> macOS only

> **[Codex](#codex)**
>
> Responses API

> **[ChatGPT desktop app](#chatgpt-desktop-app)**
>
> Responses API

> **[OpenCode](#opencode)**
>
> Chat Completions

> **[Pi](#pi)**
>
> Chat Completions

> **[Cursor IDE](#cursor-ide)**
>
> Chat Completions

> **[VS Code](#vs-code)**
>
> Chat Completions

> **[Copilot App](#copilot-app)**
>
> Chat Completions

> **[Copilot CLI](#copilot-cli)**
>
> Chat Completions

> **[DeepSeek Harness](#deepseek-harness)**
>
> Chat Completions

## Before you start

**FireConnect**

[Install FireConnect](/nexus/fireconnect#quick-start) and sign in once:

```bash wrap theme={null}
fireconnect login
```

* **Connect:** `fireconnect <harness>`. Add `--model <id>` to choose a model or router. Browse IDs with `fireconnect model list`.
* **Quit first:** fully quit Cursor IDE, VS Code, the Copilot App, and the ChatGPT desktop app before connecting or running `off`. Restart other harnesses, including Claude Desktop, after connecting.
* **Check:** `fireconnect <harness> status` is read-only and safe while the app is open.
* **Undo:** `fireconnect <harness> off` restores the settings FireConnect saved under `~/.fireconnect/`.

**Manual setup**

Create an API key in [Fireworks settings](https://app.fireworks.ai/settings/users/api-keys) and export it:

```bash wrap theme={null}
export FIREWORKS_API_KEY="fw_..."
```

Every harness uses the same Fireworks endpoints:

| Harness API | Base URL |
| - | - |
| Anthropic Messages | `https://api.fireworks.ai/inference` |
| OpenAI Chat Completions or Responses | `https://api.fireworks.ai/inference/v1` |

Use any model ID from [Open Models](/nexus/open-models), such as `glm-latest`, or [FireRouter](/nexus/firerouter) as `firerouter`. Back up a settings file before you edit it.

## Claude Code

Anthropic MessagesFireRouterNative web search

**FireConnect**

```bash wrap theme={null}
fireconnect claude
fireconnect claude status
```

Start a new session, or exit and run `claude --resume <id>`. FireConnect selects FireRouter by default. To choose another model, pass `--model`:

```bash wrap theme={null}
fireconnect claude --model glm-5p3-flash
```

`--model` sets the default model for new sessions and adds it to `/model`. `/model` also lists `auto`, the routers, and the Fireworks catalog. Your own picker rows are not changed.

To send one Claude tier or your subagents to a specific model, pin that slot:

```bash wrap theme={null}
fireconnect claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest
```

Tier flags are `--opus`, `--sonnet`, `--haiku`, `--fable`, and `--subagent`. Unpinned slots stay on Claude Code's defaults. Running `fireconnect claude` again keeps your pins. Pass `native`, such as `--sonnet native`, to release a slot.

**\~**

**.claude**

**settings.json**

**.claude.json**

**.fireconnect**

**backup for off**

> **See what FireConnect writes**
>
> ```json ~/.claude/settings.json theme={null}
> {
>   "env": {
>     "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
>     "ANTHROPIC_CUSTOM_HEADERS": "X-Fireworks-Api-Key: fw_...",
>     "DISABLE_TELEMETRY": "1",
>     "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
>     "ENABLE_TOOL_SEARCH": "true"
>   },
>   "modelPicker": {
>     "options": [
>       { "model": "firerouter[1m]", "label": "FireRouter" },
>       { "model": "auto[1m]", "label": "Auto" }
>     ]
>   },
>   "model": "firerouter[1m]",
>   "statusLine": { "type": "command", "command": "... claude-statusline.mjs" }
> }
> ```
>
> * The Fireworks key goes in a custom header, so your Claude login stays available for Claude turns.
> * `[1m]` marks 1M-context models.
> * A pinned tier adds `ANTHROPIC_DEFAULT_<TIER>_MODEL` to `env`, such as `ANTHROPIC_DEFAULT_SONNET_MODEL`. A pinned subagent adds `CLAUDE_CODE_SUBAGENT_MODEL`.
> * The status line shows the estimated session cost. It is added only if you do not already have one.
> * FireConnect also turns off Claude Code telemetry and nonessential traffic, and enables MCP tool search.
> * `~/.claude.json`: if you export `ANTHROPIC_API_KEY`, FireConnect pre-approves it so Claude Code doesn't prompt. FireConnect also removes its retired `fireworks-websearch` server here.

**Manual setup**

**1. Point Claude Code at Fireworks**

Add these values to `~/.claude/settings.json`:

```json ~/.claude/settings.json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_AUTH_TOKEN": "fw_YOUR_FIREWORKS_API_KEY"
  },
  "model": "glm-latest"
}
```

Or set them for one shell:

```bash wrap theme={null}
export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"
export ANTHROPIC_API_KEY="$FIREWORKS_API_KEY"
claude --model glm-latest
```

**2. Start a session**

Run `claude`. Claude Code may ask once whether to use the API key; approve it.
\[!TIP] The first reply comes from the Fireworks model you set.

**3. Optional: use FireRouter**

Set `"model": "firerouter"`. For Claude turns, connect an Anthropic [Provider Key](/nexus/provider-keys), or add `x-anthropic-api-key` to `ANTHROPIC_CUSTOM_HEADERS`.

Claude Code's `/model` picker does not list Fireworks models you set by hand. Change models in `settings.json` or with `claude --model <id>`. Claude Code may log `unrecognized_model` for Fireworks IDs; requests still succeed.

> **Routers and credentials**
>
> * `firerouter` can use your Claude login for Claude turns when you connect with FireConnect.
> * Optional: save an OpenAI key once with `fireconnect configure --openai-api-key sk-...` so `firerouter` can also reach GPT models. See [how `firerouter` picks its closed model](/nexus/firerouter#how-bare-firerouter-picks-its-closed-model).
> * See [Harness Compatibility](/nexus/harness-compatibility) for cross-harness support.

> **Usage and cost**
>
> For the status line and `fireconnect claude usage`, see [Usage and Cost](/nexus/metrics). Claude Code's own in-app cost uses Anthropic list prices; use the FireConnect status line for the Fireworks estimate. For a side-by-side comparison, see the [Side-by-Side Demo](/nexus/demo).

> **Troubleshooting**
>
> * Text-only models fail on pasted images. Use `/rewind`, or switch to a vision model such as `glm-5p3-flash`.
> * Resume or restart the session after changing models.
> * Auto mode says classifier requests are billed: this is expected, once per session, and auto mode keeps working. Its safety checks run on your Sonnet slot and bill to Anthropic. To bill them at Fireworks rates, pin Sonnet with `fireconnect claude --sonnet <id>`.

## Claude Agent SDK

Anthropic Messages

The Claude Agent SDK can reuse the Claude Code settings above. Connect Claude Code first, with FireConnect or manually:

```bash wrap theme={null}
fireconnect claude --model firerouter
```

In the SDK query options, include `settingSources: ["user"]`. The SDK then reads the Fireworks endpoint, model, and credentials from `~/.claude/settings.json`.

`fireconnect claude` does not configure Claude Desktop. See [Claude Desktop](#claude-desktop).

## Claude Desktop

Anthropic MessagesmacOS only

FireConnect runs Claude Desktop's Chat, Cowork, and Code on Fireworks models. It requires macOS and a stored credential from `fireconnect login`. **Quit and reopen Claude Desktop after `on` or `off`.**

**FireConnect**

```bash wrap theme={null}
fireconnect claude-desktop on
fireconnect claude-desktop status
```

Reopen Claude Desktop. The picker starts on `auto`, followed by the Fireworks models, in place of your claude.ai subscription models.

`on` brings your connectors along automatically. Each one asks you to sign in once the first time you use it. `off` puts your previous setup back, including your claude.ai models.

![Claude Desktop model picker in Cowork showing Auto selected, then Kimi K3 Fast, Kimi K3, MiniMax M3, GLM 5.3 Fast, GLM 5.3, and DeepSeek V4.1 Flash](https://mintcdn.com/fireworksai/StEyUO7myzGItQyb/images/fireconnect/claude-desktop-model-picker.png?fit=max\&auto=format\&n=StEyUO7myzGItQyb\&q=85\&s=50b2ae761c052bb50c36bb6176a87d42)

> **See what FireConnect writes**
>
> * `on` writes a third-party inference provider profile, Claude Desktop's own supported mechanism. The profile points at a small local gateway that FireConnect runs as a launchd service. It starts at login and restarts after a crash.
> * `on` copies your custom skills and plugins into third-party mode. It never overwrites a file that is already there. Conversations stay in the mode they were made in.
> * Connector OAuth clients you register are saved in `~/.fireconnect/claude-desktop/oauth-clients.json`, readable only by you. They survive `off` and `on`.
> * `off` restores your previous provider profile and the device settings FireConnect changed, then removes the local gateway service. Nothing of yours is deleted.

**What moves with you**

* Connectors move automatically with `on`. Sign in to each one once the first time you use it.
* Connector OAuth clients you register are saved and survive `off` and `on`.
* `on` copies your custom skills and plugins once. Run `fireconnect claude-desktop on` again to copy ones you add later. Changes you make while connected do not copy back.
* MCPs that need an OAuth client ID and secret do not move. Create your own client, such as a **Desktop app** client in Google Cloud for the Google-hosted connectors. If you need one of these connectors, [reach out to the team](https://fireworks.ai/contact).

Run `fireconnect claude-desktop mcp sync` when you add a connector later and want it in third-party mode too.

**What stays with your claude.ai subscription**

Third-party mode does not show your claude.ai chats, projects, artifacts, memory, or scheduled tasks. Nothing is deleted. Run `fireconnect claude-desktop off` and reopen Claude Desktop to get them back.

| claude.ai item | While connected |
| - | - |
| Chats | Hidden. New chats start empty. |
| Projects | Hidden. You can create new projects. |
| Artifacts | Hidden in the app. New artifacts save as files in `~/Claude/`. |
| Memory | Not carried over. New memory builds up on this computer. |
| Scheduled tasks | Not carried over. You can create new ones. |

New work while connected:

* Chats, projects, artifacts, and memory save only on this computer. They do not appear on claude.ai web or mobile, and you cannot share them.
* Scheduled tasks run only while the computer is awake. A missed run starts when it wakes.
* Chat cannot search past chats and does not get nightly memory summaries. Chat uses memory only inside a project.
* Voice mode is not available.

Anthropic lists these limits in its [third-party feature matrix](https://claude.com/docs/third-party/claude-desktop/feature-matrix) and [local data guide](https://claude.com/docs/third-party/claude-desktop/data-storage).

> **Where did my previous conversations go?**
>
> Your conversations are still there. Conversations stay in the mode they were made in. Claude Desktop's third-party mode does not show conversations from your claude.ai subscription, and your subscription does not show conversations you start while connected. Nothing is deleted. Run `fireconnect claude-desktop off` and reopen Claude Desktop to see your previous conversations again.

> **Connectors**
>
> Claude Desktop's third-party mode hides the in-app connector browser. Manage connectors with FireConnect instead:
>
> * `on` imports the connectors you already use, from Desktop session history and your previous Desktop config.
> * `mcp sync` also adds connectors from your claude.ai organization when the Claude Code CLI is installed and signed in, plus any you added later.
> * `fireconnect claude-desktop mcp add <name> <url>` and `mcp remove <name>` manage entries by hand. Removals stick across syncs.
> * Each connector asks you to sign in once the first time you use it after `on`.
>
> Google-hosted connectors (Gmail, Google Drive, Google Calendar, BigQuery) need a Google OAuth client you own, created as a **Desktop app** client in Google Cloud. One client covers all four:
>
> ```bash wrap theme={null}
> fireconnect claude-desktop mcp add gmail https://gmailmcp.googleapis.com/mcp/v1 \
>   --client-id "<ID>.apps.googleusercontent.com" --client-secret "<SECRET>"
> ```
>
> The hosted Figma connector does not work in third-party mode. Turn on the Figma desktop app's local server in Dev Mode, then run `fireconnect claude-desktop mcp add figma-desktop http://127.0.0.1:3845/mcp`.

> **Troubleshooting**
>
> * `status` shows the local gateway is not responding: run `fireconnect claude-desktop on` to restart it.
> * Models are missing from the picker: run `on` once while online, then restart Claude Desktop.
> * The Code tab says the API key was rejected: run `on` again to refresh the key from your stored credential.
> * A connector sign-in error won't clear: `mcp remove` it, then `mcp add` it again with your own OAuth client (Google) or the local server (Figma).

## Codex

OpenAI ResponsesFireRouterNative web search

The Codex CLI reads `~/.codex/config.toml`. The [ChatGPT desktop app](#chatgpt-desktop-app) reads the same file, so connecting one connects the other. **Close open Codex sessions and quit the ChatGPT desktop app** before connecting or running `off`. In a terminal, FireConnect waits for them to close; in a script, it exits with an error. `--force` writes anyway, which isn't recommended.

**FireConnect**

```bash wrap theme={null}
fireconnect codex
fireconnect codex status
```

Start a new Codex session. Codex opens on FireRouter (`firerouter`). Run `fireconnect codex` again at any time. It keeps the model you're on.

![Codex CLI Select Model and Effort picker with FireRouter (current) selected, described as routing each user turn between open models and the closed models you have access to, followed by GPT-6.1-Sol, GPT-6-Astra, GPT-6-Sol, GPT-6-Luna, and older GPT models](https://mintcdn.com/fireworksai/uH3av4WCHDokF6Sc/images/fireconnect/codex-model-picker.png?fit=max\&auto=format\&n=uH3av4WCHDokF6Sc\&q=85\&s=bf7f6cb2cd9aba89399ed89ddc2f63d2)

`/model` lists FireRouter first, then Codex's GPT models, then Fireworks models.

**Codex keeps its own sign-in.** Pick ChatGPT, a device code, or an API key when it asks, or run `codex login`. Your Fireworks key pays for Fireworks models. Your Codex sign-in pays for GPT models; open **Who pays for GPT turns** below for the details.

**Upgrading from an earlier FireConnect?** Run `fireconnect upgrade`, then restart Codex. Your model stays. If FireConnect 0.9.9 set up the FireRouter row as `firerouter/astra`, it becomes `firerouter`. Run `codex login` if Codex asks.

**\~/.codex**

**config.toml**

**fireworks-model-catalog.json**

> **See what FireConnect writes**
>
> ```toml ~/.codex/config.toml theme={null}
> model_provider = "fireworks-ai"
> model_catalog_json = "~/.codex/fireworks-model-catalog.json"
> model = "firerouter"
>
> [model_providers.fireworks-ai]
> name = "Fireworks"
> base_url = "https://api.fireworks.ai/inference/v1"
> wire_api = "responses"
> requires_openai_auth = true
> http_headers = { "X-Title" = "Codex", "HTTP-Referer" = "fireconnect/v<version>", "x-fireworks-api-key" = "fw_..." }
> ```
>
> `requires_openai_auth = true` makes Codex send its own sign-in, and the Fireworks key travels in `x-fireworks-api-key`. FireConnect writes the same provider table for every model and sends no Anthropic or OpenAI key.
>
> FireConnect keeps your other TOML settings, including `[mcp_servers]`, saves the file with mode `0600`, and writes a model catalog so Codex knows each model's context window and capabilities. The catalog also turns on Codex's MCP tool search for every model, so MCP and app connector tools load on demand, and makes Codex auto-review run on the model you picked.

**Manual setup**

**1. Add a Fireworks provider**

```toml ~/.codex/config.toml theme={null}
model_provider = "fireworks-ai"
model = "glm-latest"

[model_providers.fireworks-ai]
name = "Fireworks"
base_url = "https://api.fireworks.ai/inference/v1"
wire_api = "responses"
env_key = "FIREWORKS_API_KEY"
```

**2. Run Codex**

```bash wrap theme={null}
codex
```

> [!TIP]
>
> Codex answers from `glm-latest`.

Without a model catalog, Codex warns that it has no metadata for Fireworks models and uses fallback limits. FireConnect writes that catalog for you.

To pay for GPT turns with your Codex sign-in, as FireConnect does, replace the `env_key` line with these two:

```toml ~/.codex/config.toml theme={null}
requires_openai_auth = true
env_http_headers = { "x-fireworks-api-key" = "FIREWORKS_API_KEY" }
```

Codex then sends its own sign-in, and reads your Fireworks key from the environment.

When you resume an old session, select the provider explicitly:

```bash wrap theme={null}
codex resume <id> -c model_provider="fireworks-ai"
```

> **Who pays for GPT turns**
>
> With FireConnect, your Codex sign-in decides who pays for GPT turns:
>
> | Codex sign-in | Who pays for GPT turns |
> | - | - |
> | ChatGPT | Your ChatGPT plan. Older models, such as `gpt-5.6-terra`, use an OpenAI Provider Key instead |
> | OpenAI API key | That OpenAI key |
> | Fireworks key only | An OpenAI [Provider Key](/nexus/provider-keys). Without one, a GPT model you pick fails with `no usable openai credential` |
>
> * FireConnect doesn't hand a saved OpenAI key to Codex. To pay with it, sign Codex in with it: `fireconnect key export --openai | codex login --with-api-key`.
> * No browser on the machine? `codex login --device-auth` signs in with ChatGPT through a one-time code.

> **Routers and credentials**
>
> * On Codex, `firerouter` routes between GPT Sol and Fireworks open models. See [how `firerouter` picks its closed model](/nexus/firerouter#how-bare-firerouter-picks-its-closed-model).
> * With only a Fireworks key, `firerouter` uses GPT Sol if you have an OpenAI Provider Key, otherwise Claude Opus if you have an Anthropic Provider Key, otherwise open models.
> * Codex doesn't send an Anthropic key, so Claude turns on Codex need an Anthropic [Provider Key](/nexus/provider-keys).

> [!WARNING]
>
> **MiniMax models don't work on Codex.** Codex may insert assistant messages between `tool_calls` and `tool_results`, which MiniMax templates reject. FireConnect leaves MiniMax out of the Codex model list and rejects `--model minimax-...`. Use a Chat Completions harness such as OpenCode for MiniMax.

## ChatGPT desktop app

OpenAI ResponsesFireRouterNative web search

The ChatGPT desktop app reads the same `~/.codex/config.toml` as the [Codex CLI](#codex), so connecting one connects the other. **Quit the ChatGPT desktop app and close open Codex sessions before connecting or running `off`.** The app loads its model list only at startup. FireConnect waits for both to close, or use `--force` to write anyway.

**FireConnect**

```bash wrap theme={null}
fireconnect chatgpt
fireconnect chatgpt status
```

`fireconnect chatgpt` is the same command as `fireconnect codex`. Reopen the app. Its model list starts on FireRouter (`firerouter`) and adds the Fireworks models next to the GPT models.

* **Sign-in:** the app keeps its own ChatGPT sign-in, which pays for GPT turns. Your Fireworks key pays for Fireworks models. See **Who pays for GPT turns** under [Codex](#codex).
* **MCP servers and plugins** keep working, through Codex's tool search. Connected with FireConnect 0.9.9 or earlier? Run `fireconnect upgrade`, then reopen the app.
* **Files:** FireConnect writes the same `config.toml` and model catalog as for Codex. See **See what FireConnect writes** under [Codex](#codex).

> [!NOTE]
>
> **Threads keep the provider they started on.** A thread started on an
> OpenAI model before you connected stays on OpenAI, even after you pick
> FireRouter or a Fireworks model. ChatGPT then shows an error such as
> `The 'firerouter' model is not supported when using Codex with a ChatGPT account.`
> The error names whichever Fireworks model you picked.
>
> * Start a new thread to use FireRouter and Fireworks models.
> * To keep working in the old thread, switch back to an OpenAI model, or run
>   `fireconnect chatgpt off` and turn it back on when you start a new thread.
> * After `off`, threads started on Fireworks models don't open until you run `fireconnect chatgpt` again.

> [!NOTE]
>
> Sign-in billing is tested in the Codex CLI. The ChatGPT desktop app is not
> tested yet.

**Manual setup**

Quit the app, then follow the [Codex manual setup](#codex). The app reads the same `~/.codex/config.toml`. Reopen the app and pick the model you set.

## OpenCode

OpenAI Chat CompletionsFireRouter

**FireConnect**

```bash wrap theme={null}
fireconnect opencode
fireconnect opencode status
```

Restart OpenCode. The default model is `auto`, stored as `fireworks-ai/auto`. Short IDs such as `glm-latest` expand to full Fireworks paths.

![OpenCode model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and other models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/opencode-model-picker.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=e141d84459d67717e8a32ca0de036288)

> **See what FireConnect writes**
>
> ```json ~/.config/opencode/opencode.json theme={null}
> {
>   "provider": {
>     "fireworks-ai": {
>       "options": { "apiKey": "fw_..." },
>       "models": {
>         "auto": { "name": "Auto", "limit": { "context": 1048575, "output": 131072 } },
>         "glm-latest": { "name": "GLM (Latest)" }
>       }
>     }
>   },
>   "model": "fireworks-ai/auto"
> }
> ```
>
> If your `opencode.json` uses OpenCode v2's `providers` map, FireConnect writes the Fireworks provider there too, so the models appear in `/models`. Connected with an earlier FireConnect? Run `fireconnect upgrade` to add them.
>
> The file is saved with mode `0600`. FireConnect never changes `auth.json`. Use `--config-path` for a config stored elsewhere.

**Manual setup**

**Fastest:** in OpenCode, run `/connect`, search **fireworks.ai**, paste your key, and pick a model with `/models`.

**Or edit the config** to add routers and pin a default:

```json ~/.config/opencode/opencode.json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "fireworks-ai": {
      "options": { "apiKey": "{env:FIREWORKS_API_KEY}" },
      "models": {
        "glm-latest": { "name": "GLM (Latest)" },
        "firerouter": { "name": "FireRouter" }
      }
    }
  },
  "model": "fireworks-ai/glm-latest"
}
```

> [!TIP]
>
> `opencode run -m fireworks-ai/firerouter "hello"` answers through FireRouter.

## Pi

OpenAI Chat CompletionsFireRouter

**FireConnect**

```bash wrap theme={null}
fireconnect pi
fireconnect pi status
```

Restart Pi if it was running. The default model is `auto`.

**\~/.pi/agent**

**settings.json**

**auth.json**

**models.json**

> **See what FireConnect writes**
>
> ```json ~/.pi/agent/settings.json theme={null}
> {
>   "defaultProvider": "fireworks",
>   "defaultModel": "auto",
>   "enabledModels": ["fireworks/accounts/fireworks/routers/*", "fireworks/auto"]
> }
> ```
>
> ```json ~/.pi/agent/auth.json theme={null}
> { "fireworks": { "type": "api_key", "key": "fw_..." } }
> ```
>
> `models.json` adds the Fireworks catalog to Pi's built-in `fireworks` provider. FireConnect tracks the IDs it adds so `off` removes only those. Use `--settings-path` for a settings file stored elsewhere.

**Manual setup**

Pi has a built-in `fireworks` provider that reads `FIREWORKS_API_KEY`. Set it as the default:

```json ~/.pi/agent/settings.json theme={null}
{
  "defaultProvider": "fireworks",
  "defaultModel": "accounts/fireworks/routers/glm-latest"
}
```

> [!TIP]
>
> `pi -p "hello"` answers from GLM.

## Cursor IDE

OpenAI Chat CompletionsFireRouter with Provider Keys

`fireconnect cursor` configures Cursor IDE. Cursor CLI (`agent` or `cursor-agent`) is not supported. **Fully quit Cursor IDE before connecting or running `off`.**

**FireConnect**

```bash wrap theme={null}
fireconnect cursor
fireconnect cursor status
```

FireConnect points every existing mode in `modelConfig` at the Fireworks default and registers the catalog in the picker. Reopen Cursor IDE and choose a Fireworks model.

![Cursor IDE model picker showing Auto selected with Fireworks DeepSeek, GLM, Kimi, and MiniMax models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/cursor-ide-model-picker.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=0723405d7520caf2846e3e8c6199353b)

> **See what FireConnect writes**
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
> Your previous auth state is saved under `~/.fireconnect/cursor/`. Use `--db-path` for a non-default `state.vscdb`.

**Manual setup**

**1. Open model settings**

In Cursor IDE, open **Settings**, then **Models**.

**2. Add your Fireworks key**

Under **API Keys**, paste your Fireworks key into **OpenAI API Key**. Turn on **Override OpenAI Base URL** and enter `https://api.fireworks.ai/inference/v1`.

**3. Add a model**

Add a custom model with a Fireworks ID, such as `glm-latest`, then select it in chat.

> [!WARNING]
>
> **While connected, only Fireworks models work.** Cursor IDE's built-in models are hidden until you run `off`. Cursor IDE also enforces a server-side allowlist, so not every Fireworks model is selectable. Some features may still use Cursor's own backend, depending on plan and version.

> **Troubleshooting**
>
> * **`Model name is not valid: "firerouter"`, or the same error for another Fireworks ID:** Cursor IDE stopped sending your Fireworks key. Cursor can turn the key off after Fireworks rejects a request, such as when the key is revoked or a model ID is not found. Without a key, Cursor treats Fireworks IDs as unknown models. Open **Settings → Models**, turn **OpenAI API Key** back on, and retry.
> * **The key was revoked:** turning it back on is not enough. Run `fireconnect login --force` for a new key, fully quit Cursor IDE, and run `fireconnect cursor`. With manual setup, paste a new key from [Fireworks settings](https://app.fireworks.ai/settings/users/api-keys).

## VS Code

OpenAI Chat CompletionsFireRouter

FireConnect adds a **Fireworks** provider to GitHub Copilot Chat's custom endpoints. This requires Copilot **Pro or Enterprise**. **Quit VS Code before connecting or running `off`.**

**FireConnect**

```bash wrap theme={null}
fireconnect vscode
fireconnect vscode status
```

Restart VS Code, then pick a model under **Other Models → Fireworks** in Copilot Chat. `glm-latest` and `glm-fast-latest` are text-only; `glm-5p3-flash` supports images.

![VS Code Chat model picker showing the Fireworks provider with Auto selected and DeepSeek, GLM, and Kimi models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/vscode-chat-model-picker.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=57a8a5e11075319df3829e424183a6a2)

> **See what FireConnect writes**
>
> ```json chatLanguageModels.json theme={null}
> [
>   {
>     "name": "Fireworks",
>     "vendor": "customendpoint",
>     "apiType": "chat-completions",
>     "apiKey": "${input:chat.lm.secret.fw-...}",
>     "models": [
>       {
>         "id": "auto",
>         "name": "Auto",
>         "url": "https://api.fireworks.ai/inference",
>         "maxInputTokens": 1048575,
>         "maxOutputTokens": 131072,
>         "vision": true,
>         "toolCalling": true
>       }
>     ]
>   }
> ]
> ```
>
> The key is stored separately in `state.vscdb`, encrypted with Electron `safeStorage`. On Linux, encryption needs `libsecret`; without it, VS Code only obfuscates the key and FireConnect warns you.
>
> | Platform | `chatLanguageModels.json` | `state.vscdb` |
> | - | - | - |
> | Linux | `~/.config/Code/User/` | `~/.config/Code/User/globalStorage/` |
> | macOS | `~/Library/Application Support/Code/User/` | `~/Library/Application Support/Code/User/globalStorage/` |
> | Windows | `%APPDATA%\Code\User\` | `%APPDATA%\Code\User\globalStorage\` |

**Manual setup**

In Copilot Chat, open **Language Models**, click **+ Add Models...**, and choose **Custom Endpoint**. Use `https://api.fireworks.ai/inference/v1`, your Fireworks key, and a model ID such as `glm-latest`.

Follow the step-by-step screenshots in [GitHub Copilot](/ecosystem/integrations/github-copilot).

## Copilot App

OpenAI Chat CompletionsFireRouter with Provider Keys

The GitHub Copilot **desktop app** keeps its built-in models and adds Fireworks alongside them. **Quit the app before connecting or running `off`.**

**FireConnect**

```bash wrap theme={null}
fireconnect copilot-app
fireconnect copilot-app status
```

Reopen the app and pick a Fireworks model in **Settings → Model providers**.

> **See what FireConnect writes**
>
> FireConnect writes to `~/.copilot/data.db` (SQLite, movable with `COPILOT_HOME`):
>
> | Table | What FireConnect adds |
> | - | - |
> | `model_providers` | One `Fireworks` provider of type `openai`, with base URL `https://api.fireworks.ai/inference/v1` and your key as an `Authorization: Bearer` header |
> | `provider_models` | One row per model, with token limits and reasoning efforts (`low`, `medium`, `high`, `max`) |
>
> `off` deletes the provider and its models. Use `--db-path` for a non-default database.

**Manual setup**

In **Settings → Model providers**, add a provider with the values FireConnect uses:

| Field | Value |
| - | - |
| Base URL | `https://api.fireworks.ai/inference/v1` |
| API key | Your Fireworks key |
| Models | Fireworks IDs, such as `glm-latest` or `kimi-latest` |

The app's bring-your-own-key path does not support image input, the hover-card Context row, or AI-credits pricing. FireConnect can add `firerouter`, but the app cannot send a local Anthropic or OpenAI key. Without a matching [Provider Key](/nexus/provider-keys), FireRouter serves every turn with open models. See [Harness Compatibility](/nexus/harness-compatibility).

## Copilot CLI

OpenAI Chat CompletionsFireRouter with manual setup

The `copilot` command (`@github/copilot`) reads plain JSON under `~/.copilot`, separate from the desktop app.

**FireConnect**

```bash wrap theme={null}
fireconnect copilot-cli
fireconnect copilot-cli status
```

Start a new `copilot` session. Switch models with `copilot --model fireworks/<name>` or `/model`.

![Copilot CLI model picker showing Auto selected and Fireworks DeepSeek, GLM, Kimi, and MiniMax models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireconnect/copilot-cli-model-picker.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=61b0cc5e13f64bb8fadb383890980d56)

`off` restores `providers.json` from its snapshot, or deletes it if FireConnect created it. Use `--providers-path` for a non-default location.

**Manual setup**

```json ~/.copilot/providers.json theme={null}
{
  "providers": [
    {
      "name": "fireworks",
      "type": "openai",
      "wireApi": "completions",
      "baseUrl": "https://api.fireworks.ai/inference/v1",
      "apiKey": "fw_YOUR_FIREWORKS_API_KEY"
    }
  ],
  "models": [
    {
      "id": "glm-latest",
      "provider": "fireworks",
      "wireModel": "glm-latest",
      "name": "GLM (Latest)",
      "maxPromptTokens": 1048576,
      "maxContextWindowTokens": 1048576,
      "maxOutputTokens": 131072,
      "capabilities": { "supports": { "reasoningEffort": true } }
    }
  ]
}
```

```json ~/.copilot/settings.json theme={null}
{ "model": "fireworks/glm-latest" }
```

To use FireRouter with Claude or GPT turns, add a `headers` map to the provider, such as `"headers": { "x-anthropic-api-key": "sk-ant-..." }`, and use `firerouter` as the model `id` and `wireModel`. FireConnect adds `firerouter` but does not send your provider keys, so use manual setup to send them yourself. The [harness setup](/nexus/firerouter/setup#set-up-your-harness) generates the full file.

> [!NOTE]
>
> Use provider-prefixed model IDs such as `fireworks/glm-latest`. The CLI rejects a bare `glm-latest` and silently falls back to its configured model.

## DeepSeek Harness

OpenAI Chat CompletionsFireRouter with manual setup

DeepSeek's coding agent (`dsh`) runs named profiles, such as `tui`, `web`, and `headless`, under `$DSH_HOME`, which defaults to `~/.dsh`. Restart `dsh` after changing a profile.

**FireConnect**

```bash wrap theme={null}
fireconnect deepseek
fireconnect deepseek status
```

Restart `dsh`. It starts on `auto` and goes straight to Fireworks, with no DeepSeek key prompt.

FireConnect adds a `fireworks` provider to `~/.dsh/settings.yaml` and to each existing profile's `cordis.patch.yml`, which `dsh` 0.1.7 and later read. `off` restores both from the snapshot under `~/.fireconnect/deepseek/`.

**\~/.dsh**

**settings.yaml**

**.credentials.yaml**

**profiles/\<profile>**

**cordis.patch.yml**

Connected before FireConnect 0.9.8? Run `fireconnect deepseek` once so `dsh` 0.1.7 and later stop asking for a DeepSeek key.

FireConnect can add `firerouter`, but it does not send provider keys from `dsh`. For Claude or GPT turns, connect a [Provider Key](/nexus/provider-keys) or use manual setup.

**Manual setup**

Create the profile folder once, then add a patch to it. Repeat for each profile you use.

```bash wrap theme={null}
dsh --profile tui --dump-config > /dev/null
```

```yaml ~/.dsh/profiles/tui/cordis.patch.yml theme={null}
- id: llm-pi-ai
  config:
    providers:
      fireworks:
        displayName: Fireworks
        apiKeyEnv: FIREWORKS_API_KEY
        api: openai-completions
        baseURL: https://api.fireworks.ai/inference/v1
        models:
          - id: glm-latest
            name: GLM (Latest)
            reasoning: true
            contextWindow: 1048576
            maxTokens: 131072
- id: agent-default-model
  config:
    provider: fireworks
    model: glm-latest
```

```bash wrap theme={null}
export FIREWORKS_API_KEY="fw_..."
dsh tui
```

To use FireRouter with Claude or GPT turns, add `headers` to the provider, such as `x-anthropic-api-key: sk-ant-...`, and use `firerouter` as the model. The [harness setup](/nexus/firerouter/setup#set-up-your-harness) generates the full patch.
