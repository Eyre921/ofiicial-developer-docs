---
title: "Codex"
source: https://docs.fireworks.ai/ecosystem/fireconnect/codex
path: ecosystem/fireconnect/codex
---

Use Fireworks AI models in OpenAI Codex CLI with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes the [OpenAI Codex CLI](https://developers.openai.com/codex) through Fireworks AI models via the Responses API. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

<Tip>
  **Change models:** `fireconnect codex on --model <id>`. See [Models](/ecosystem/fireconnect/models).
</Tip>

## Prerequisites

* [OpenAI Codex CLI](https://developers.openai.com/codex) installed (0.134+)
* A standard [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* FireConnect **v0.9.1+** (see [Install](/ecosystem/fireconnect/overview#install))

<Warning>
  Fire Pass keys (`fpk_...`) are not supported for Codex yet. The `/responses` endpoint requires a standard Fireworks API key.
</Warning>

## Enable Fireworks routing

```bash theme={null}
fireconnect login
fireconnect codex on
```

Or pass the key once:

```bash theme={null}
fireconnect codex on --api-key fw_...
```

After `fireconnect codex on` or `off`, `config.toml` is updated immediately. To use updated routing, exit Codex and resume with `codex resume <id>`, or start a new session.

## Default model

Codex routes a single default model. The default is `kimi-fast-latest`.

```bash theme={null}
fireconnect codex status
```

## What gets written

FireConnect edits `~/.codex/config.toml`:

* Sets root `model_provider` / `model` for Codex 0.134+ (stored as a short slug)
* Adds a `[model_providers.fireworks-ai]` block with `wire_api = "responses"` and a **baked** `experimental_bearer_token` literal (file mode `0600`). Codex reads the key from config; no shell hook is required.

FireConnect snapshots your original `~/.codex/config.toml` before the first change. The snapshot lives in `~/.fireconnect/codex/`. Running `fireconnect codex off` restores it byte-for-byte. Unrelated Codex settings (for example `[[mcp_servers]]`) are preserved via surgical TOML edits.

## Codex model catalog

When you run `fireconnect codex on`, FireConnect fetches your account's serverless catalog and writes Codex-compatible model metadata to `~/.codex/fireworks-model-catalog.json`. It links that file from `config.toml` via `model_catalog_json` so Codex knows display names, context windows, reasoning levels, and tool-calling support for each model.

```bash theme={null}
fireconnect codex status   # shows whether the catalog is linked and on disk
```

The catalog includes serverless models that support tool calling with a non-zero context window, plus curated aliases such as `glm-fast-latest`. Deprecated models are excluded. If catalog generation fails (for example, due to an invalid API key), routing still works but Codex may show limited model metadata until you re-run `fireconnect codex on`.

Browse available models globally:

```bash theme={null}
fireconnect model list --search glm
fireconnect model list --json   # includes IN / OUT pricing where known
```

## FireRouter

Route requests through [FireRouter](/ecosystem/firerouter/overview):

```bash theme={null}
fireconnect codex on --model firerouter
export ANTHROPIC_API_KEY=sk-ant-...   # optional BYOK for pass-through to Claude Opus 4.8
fireconnect codex on --model firerouter --anthropic-api-key sk-ant-...
```

FireConnect rejects `--model firerouter` with Fire Pass (`fpk_...`) on every harness; use an `fw_...` key. Codex also does not support Fire Pass for direct routing. FireRouter BYOK reads `ANTHROPIC_API_KEY` from your shell (Codex does not support `--routing-preference`).

<Warning>
  **MiniMax models are not supported in Codex.** Codex uses the Fireworks Responses API and may insert assistant messages between `tool_calls` and `tool_results`. MiniMax chat templates require `tool_results` to follow `tool_calls` directly. Use Chat Completions harnesses (for example Claude Code or OpenCode) for MiniMax.
</Warning>

## CLI reference

```bash theme={null}
fireconnect codex on              # Enable Fireworks routing
fireconnect codex off             # Restore original config
fireconnect codex status          # Check current provider and model
fireconnect codex help            # Show harness-specific help
```

Run `fireconnect codex help` for all options.

### Switch models

```bash theme={null}
fireconnect codex on --model glm-5p2
fireconnect codex on --model deepseek-v4-flash
```

Some models expose multiple reasoning levels in the Codex catalog (for example, `glm-5p2` supports `high` and `max`). Pick the model in Codex with `/model` after switching.

### Turn off Fireworks routing

```bash theme={null}
fireconnect codex off
```

This restores your previous `config.toml` from the backup in `~/.fireconnect/codex/`.

### Use a non-default config file

```bash theme={null}
fireconnect codex on --config-path /path/to/config.toml
```

## Fireworks on Microsoft Foundry

Codex supports **Fireworks on Microsoft Foundry** (CLI: `--provider azure` or `on --azure`). See the [FireConnect overview](/ecosystem/fireconnect/microsoft-foundry) and [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry) for portal setup.

<Warning>
  Foundry routing requires a standard Azure API key. Fire Pass keys (`fpk_...`) are not supported. FireConnect does not write a Fireworks model catalog on the Foundry path. Set your deployment with `--model`.
</Warning>

### Configure and enable

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect codex on --model FW-GLM-5.2
```

One-off routing:

```bash theme={null}
fireconnect codex on --azure --base-url https://<resource>.services.ai.azure.com --model FW-MiniMax-M2.5
```

### What gets written

FireConnect sets `model_provider = "fireworks-azure"` in `config.toml` with a **Fireworks on Microsoft Foundry** provider block pointed at your Foundry endpoint. The Azure API key is baked as a literal when passed with `--api-key`, or referenced via `env_key = "AZURE_API_KEY"` when resolved from the environment.

Pass your Foundry model with `--model` (for example, `FW-GLM-5.2`). Use `fireconnect model list` only for browsing Fireworks serverless models on the direct gateway path.

### Turn off Foundry routing

To switch back to the Fireworks gateway:

```bash theme={null}
fireconnect configure --provider fireworks
fireconnect codex on
```

To remove FireConnect entirely and restore your original `config.toml`:

```bash theme={null}
fireconnect codex off
```

See [Turn off Foundry routing](/ecosystem/fireconnect/microsoft-foundry#turn-off-foundry-routing) for details on global config behavior and `uninstall`.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
