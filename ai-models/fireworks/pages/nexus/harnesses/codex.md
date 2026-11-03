---
title: "Codex"
source: https://docs.fireworks.ai/nexus/harnesses/codex
path: nexus/harnesses/codex
---

Connect the Codex CLI to Fireworks with the Nexus CLI or manual setup, and see who pays for OpenAI model turns with Nexus Auto.

Codex keeps its own sign-in for OpenAI model turns. Codex cloud tasks aren't supported.

Codex and the [ChatGPT desktop app](/nexus/harnesses/chatgpt) share `~/.codex/config.toml`, so connecting one connects the other.

Support summary:

* API the harness speaks to Fireworks: OpenAI Responses
* Nexus Auto: Supported
* Native web search: Supported. Fireworks runs the harness's native web search server-side, with any Fireworks model. See [Web search](/nexus/auto#web-search).

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

If the Nexus CLI is already installed and signed in, skip to step 2.

**2. Connect Codex**

Close open Codex sessions and quit the ChatGPT desktop app, then run:

```bash wrap theme={null}
nexus codex
```

* Close them before `off` too. In a terminal, Nexus CLI waits for them to close. In a script, it exits with an error. `--force` writes anyway, which isn't recommended.
* `nexus codex status` shows the current connection.
* Run `nexus codex` again at any time. It keeps the model you're on.

**3. Restart and pick Auto**

Start a new Codex session. Codex opens on Nexus Auto (**Auto** in `/model`).

* Nexus Auto's model ID is `auto`.
* `/model` shows Nexus Auto along with your ChatGPT models. Enterprise accounts also get general access to open models on Fireworks serverless. Set [effort](/nexus/orchestration-preferences) in that picker.

To restore your original settings, run `nexus codex off`.

## Use Nexus Auto

* **Fireworks model turns** use your Fireworks key.
* **OpenAI model turns** use your Codex sign-in. When Codex asks, pick ChatGPT, a device code, or an API key, or run `codex login`.
* **Anthropic model turns** need an Anthropic [Provider Key](/nexus/provider-keys) from your admin.

- Nexus Auto (`auto`) is supported on the Responses API, and Codex defaults to it.
- On Codex, `auto` picks a model for each turn from Fireworks open models and the closed models your Codex sign-in and keys allow. See [which models `auto` can use](/nexus/auto#which-models-auto-can-use).
- With only a Fireworks key (no ChatGPT or OpenAI sign-in), `auto` can still use OpenAI models through an OpenAI Provider Key, and Anthropic models through an Anthropic key. Without either key, it uses open models.
- Instead of an Anthropic Provider Key, save your own key with `nexus auto --anthropic-api-key` (it prompts for the key) and run `nexus codex` again. Nexus CLI adds the saved key to Codex's `http_headers`.
- Nexus CLI never sends an OpenAI key you saved with `nexus auto` to Codex. Your Codex sign-in covers OpenAI model turns.
- With [manual setup](#manual-setup-advanced), Codex can send `x-anthropic-api-key` and `x-openai-api-key` headers.

### Who pays for OpenAI model turns

| Codex sign-in | Who pays for OpenAI model turns |
| - | - |
| ChatGPT | Your ChatGPT plan. Older models, such as `gpt-5.6-terra`, use an OpenAI Provider Key instead |
| OpenAI API key | That OpenAI key |
| Fireworks key only | An OpenAI [Provider Key](/nexus/provider-keys). Without one, an OpenAI model you pick fails with `no usable openai credential` |

* This table applies with Nexus CLI, where your Codex sign-in decides who pays.
* For OpenAI model turns, Nexus Auto uses an `x-openai-api-key` header first, then your Codex sign-in, then an OpenAI Provider Key.
* Your ChatGPT plan doesn't cover `gpt-5.5`, `gpt-5.6-terra`, or `gpt-5.6-luna`. Those turns need an OpenAI Provider Key.
* Nexus CLI doesn't hand a saved OpenAI key to Codex. To pay with it, sign Codex in with it: `nexus key export --openai | codex login --with-api-key`.
* No browser on the machine? `codex login --device-auth` signs in with ChatGPT through a one-time code.

## MCP and tools

* MCP servers and ChatGPT connectors are unchanged.
* Native web search is supported. Fireworks runs the search server-side, so no search MCP server is required.

- Servers stay in `[mcp_servers]` in `~/.codex/config.toml`. MCP and app connector tools load through Codex's tool search on every model.
- ChatGPT connectors keep working because Codex keeps your ChatGPT sign-in.
- Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results. No search service is needed.
- Example server entry, next to the settings Nexus CLI adds:

```toml ~/.codex/config.toml theme={null}
[mcp_servers.docs]
command = "npx"
args = ["-y", "your-mcp-server"]
```

## Troubleshooting

* **Nothing changed after `--model`:** start a new or resumed session, because Codex loads a new model only at session start.
* **Resuming an old session:** select the provider explicitly with `codex resume <id> -c model_provider="fireworks-ai"`.
* **MiniMax models don't work on Codex.** Use a Chat Completions harness such as OpenCode for MiniMax.

- MiniMax fails because Codex may insert assistant messages between `tool_calls` and `tool_results`, which MiniMax templates reject. Nexus CLI leaves MiniMax out of the Codex model list and rejects `--model minimax-...`.
- Upgrading from an earlier version: see [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

Add a Fireworks provider to `~/.codex/config.toml`, then run `codex`:

```toml ~/.codex/config.toml theme={null}
model_provider = "fireworks-ai"
model = "glm-latest"

[model_providers.fireworks-ai]
name = "Fireworks"
base_url = "https://api.fireworks.ai/inference/v1"
wire_api = "responses"
env_key = "FIREWORKS_API_KEY"
```

Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

* Check: Codex answers from `glm-latest`.
* Without a model catalog, Codex warns that it has no metadata for Fireworks models and uses fallback limits. The catalog also turns on MCP tool search and runs auto-review on your chosen model. Nexus CLI writes that catalog for you.
* To pay for OpenAI model turns with your Codex sign-in, as Nexus CLI does, replace the `env_key` line with these two. Codex then sends its own sign-in, and reads your Fireworks key from the environment.

```toml ~/.codex/config.toml theme={null}
requires_openai_auth = true
env_http_headers = { "x-fireworks-api-key" = "FIREWORKS_API_KEY" }
```

## What the Nexus CLI writes

Nexus CLI writes `~/.codex/config.toml` and `~/.codex/fireworks-model-catalog.json`.

```toml ~/.codex/config.toml theme={null}
model_provider = "fireworks-ai"
model_catalog_json = "~/.codex/fireworks-model-catalog.json"
model = "auto"

[model_providers.fireworks-ai]
name = "Fireworks"
base_url = "https://api.fireworks.ai/inference/v1"
wire_api = "responses"
requires_openai_auth = true
http_headers = { "X-Title" = "Codex", "HTTP-Referer" = "nexus/v<version>", "x-fireworks-api-key" = "fw_..." }
```

* `requires_openai_auth = true` makes Codex send its own sign-in. The Fireworks key travels in `x-fireworks-api-key`.
* Nexus CLI writes the same provider table for every model. It never adds an OpenAI key. An Anthropic key saved with `nexus auto --anthropic-api-key` adds an `x-anthropic-api-key` entry to `http_headers`.
* Nexus CLI keeps your other TOML settings, including `[mcp_servers]`, and saves `config.toml` and the catalog with mode `0600`.
* `fireworks-model-catalog.json` tells Codex each model's context window and capabilities. It also turns on MCP tool search for the Fireworks models, so MCP and app connector tools load on demand, and makes Codex auto-review run on the model you picked.
