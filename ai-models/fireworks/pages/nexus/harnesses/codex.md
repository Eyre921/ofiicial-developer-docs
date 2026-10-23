---
title: "Codex"
source: https://docs.fireworks.ai/nexus/harnesses/codex
path: nexus/harnesses/codex
---

Connect the Codex CLI to Fireworks with the Nexus CLI or manual setup, and see who pays for OpenAI model turns with Nexus Auto.

The Codex CLI and the [ChatGPT desktop app](/nexus/harnesses/chatgpt) both read `~/.codex/config.toml`, so connecting one connects the other.

**Close open Codex sessions and quit the ChatGPT desktop app** before connecting or running `off`. In a terminal, Nexus CLI waits for them to close. In a script, it exits with an error. `--force` writes anyway, which isn't recommended.

Generally availableOpenAI ResponsesNexus AutoNative web search

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

**2. Connect Codex**

```bash wrap theme={null}
nexus codex
nexus codex status
```

**3. Restart and pick a model**

Start a new Codex session. Codex opens on Nexus Auto (`auto`). Run `nexus codex` again at any time. It keeps the model you're on.

> [!TIP]
>
> `/model` lists Codex's OpenAI models first, then an **Auto** row for Nexus Auto, then the other Fireworks models. Set [effort](/nexus/orchestration-preferences) in that picker.

## Use Nexus Auto

**Codex keeps its own sign-in.** When Codex asks, pick ChatGPT, a device code, or an API key, or run `codex login`. Your Fireworks key pays for Fireworks models. Your Codex sign-in pays for OpenAI models. See [Who pays for OpenAI model turns](#who-pays-for-openai-model-turns).

* Nexus Auto (`auto`) is supported on the Responses API, and Codex defaults to it.
* On Codex, `auto` picks a model for each turn from Fireworks open models and the closed models your Codex sign-in and keys allow. See [which models `auto` can use](/nexus/auto#which-models-auto-can-use).
* With only a Fireworks key (no ChatGPT or OpenAI sign-in), `auto` can still use OpenAI models through an OpenAI Provider Key, and Anthropic models through an Anthropic key. Without either key, it uses open models.
* **Anthropic model turns:** connect an Anthropic [Provider Key](/nexus/provider-keys), or save your own key with `nexus auto --anthropic-api-key` (it prompts for the key) and run `nexus codex` again. Nexus CLI adds the saved key to Codex's `http_headers`.
* Nexus CLI never sends an OpenAI key you saved with `nexus auto` to Codex. Your Codex sign-in covers OpenAI model turns.
* With [manual setup](#manual-setup-advanced), Codex can send `x-anthropic-api-key` and `x-openai-api-key` headers.

### Who pays for OpenAI model turns

With Nexus CLI, your Codex sign-in decides who pays for OpenAI model turns:

| Codex sign-in | Who pays for OpenAI model turns |
| - | - |
| ChatGPT | Your ChatGPT plan. Older models, such as `gpt-5.6-terra`, use an OpenAI Provider Key instead |
| OpenAI API key | That OpenAI key |
| Fireworks key only | An OpenAI [Provider Key](/nexus/provider-keys). Without one, an OpenAI model you pick fails with `no usable openai credential` |

* For OpenAI model turns, Nexus Auto uses an `x-openai-api-key` header first, then your Codex sign-in, then an OpenAI Provider Key.
* Your ChatGPT plan doesn't cover `gpt-5.5`, `gpt-5.6-terra`, or `gpt-5.6-luna`. Those turns need an OpenAI Provider Key.
* Nexus CLI doesn't hand a saved OpenAI key to Codex. To pay with it, sign Codex in with it: `nexus key export --openai | codex login --with-api-key`.
* No browser on the machine? `codex login --device-auth` signs in with ChatGPT through a one-time code.

## MCP and tools

Your servers stay in `[mcp_servers]` in `~/.codex/config.toml`. MCP and app connector tools load through Codex's tool search on every model.

```toml theme={null}
# ~/.codex/config.toml, next to the settings Nexus CLI adds
[mcp_servers.docs]
command = "npx"
args = ["-y", "your-mcp-server"]
```

Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results. You don't need an MCP server or a search service.

## Troubleshooting

**Nothing changed after `--model`?** Start a new or resumed session. Codex loads a new model only then.

Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

When you resume an old session, select the provider explicitly:

```bash wrap theme={null}
codex resume <id> -c model_provider="fireworks-ai"
```

> [!WARNING]
>
> **MiniMax models don't work on Codex.** Codex may insert assistant messages between `tool_calls` and `tool_results`, which MiniMax templates reject. Nexus CLI leaves MiniMax out of the Codex model list and rejects `--model minimax-...`. Use a Chat Completions harness such as OpenCode for MiniMax.

## Manual setup (advanced)

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

Without a model catalog, Codex warns that it has no metadata for Fireworks models and uses fallback limits. The catalog also turns on MCP tool search and runs auto-review on your chosen model. Nexus CLI writes that catalog for you.

To pay for OpenAI model turns with your Codex sign-in, as Nexus CLI does, replace the `env_key` line with these two:

```toml ~/.codex/config.toml theme={null}
requires_openai_auth = true
env_http_headers = { "x-fireworks-api-key" = "FIREWORKS_API_KEY" }
```

Codex then sends its own sign-in, and reads your Fireworks key from the environment.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

**\~/.codex**

**config.toml**

**fireworks-model-catalog.json**

> **See what Nexus CLI writes**
>
> ```toml ~/.codex/config.toml theme={null}
> model_provider = "fireworks-ai"
> model_catalog_json = "~/.codex/fireworks-model-catalog.json"
> model = "auto"
>
> [model_providers.fireworks-ai]
> name = "Fireworks"
> base_url = "https://api.fireworks.ai/inference/v1"
> wire_api = "responses"
> requires_openai_auth = true
> http_headers = { "X-Title" = "Codex", "HTTP-Referer" = "nexus/v<version>", "x-fireworks-api-key" = "fw_..." }
> ```
>
> * `requires_openai_auth = true` makes Codex send its own sign-in. The Fireworks key travels in `x-fireworks-api-key`.
> * Nexus CLI writes the same provider table for every model. It never adds an OpenAI key. An Anthropic key saved with `nexus auto --anthropic-api-key` adds an `x-anthropic-api-key` entry to `http_headers`.
> * Nexus CLI keeps your other TOML settings, including `[mcp_servers]`, and saves `config.toml` and the catalog with mode `0600`.
> * `fireworks-model-catalog.json` tells Codex each model's context window and capabilities. It also turns on MCP tool search for the Fireworks models, so MCP and app connector tools load on demand, and makes Codex auto-review run on the model you picked.
