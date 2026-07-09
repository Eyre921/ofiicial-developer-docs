---
title: "Codex"
source: https://docs.fireworks.ai/ecosystem/fireconnect/codex
path: ecosystem/fireconnect/codex
---

Use Fireworks AI models in OpenAI Codex CLI with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes the [OpenAI Codex CLI](https://developers.openai.com/codex) through Fireworks AI models via the Responses API. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

## Prerequisites

* [OpenAI Codex CLI](https://developers.openai.com/codex) installed (0.134+)
* A standard [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* The FireConnect CLI (see [Install](/ecosystem/fireconnect/overview#install))

<Warning>
  Fire Pass keys (`fpk_...`) are not supported for Codex yet. The `/responses` endpoint requires a standard Fireworks API key.
</Warning>

## Enable Fireworks routing

```bash theme={null}
fireconnect login
fireconnect codex on
source ~/.zshrc   # keychain mode: load FIREWORKS_API_KEY for Codex
```

Or pass the key once:

```bash theme={null}
fireconnect codex on --api-key fw_...
```

After `fireconnect codex on`, `off`, `model select`, or `model reset`, `config.toml` is updated immediately. To use the updated routing in Codex, run `/model` in the same session, start a new session, or `/exit` and resume with `codex resume <id>`.

## Default model

Codex routes a single default model. The default is `glm-fast-latest`.

```bash theme={null}
fireconnect codex status
```

## What gets written

FireConnect edits `~/.codex/config.toml`:

* Sets root `model_provider` / `model` for Codex 0.134+
* Adds a `[model_providers.fireworks-ai]` block with `wire_api = "responses"` and `env_key = "FIREWORKS_API_KEY"`
* Harness configs never contain literal keys

In keychain mode, FireConnect installs a marked block in `~/.zshrc` (or bash profile) that exports `FIREWORKS_API_KEY="$(fireconnect key export)"`. Open a new terminal or `source` your profile after enabling.

FireConnect snapshots your original `~/.codex/config.toml` before the first change. The snapshot lives in `~/.fireconnect/codex/`. Running `fireconnect codex off` restores it byte-for-byte and removes the shell hook when no env-based harnesses remain. Unrelated Codex settings (for example `[[mcp_servers]]`) are preserved via surgical TOML edits.

## Codex model catalog

When you run `fireconnect codex on`, FireConnect fetches your account's serverless catalog and writes Codex-compatible model metadata to `~/.codex/fireworks-model-catalog.json`. It links that file from `config.toml` via `model_catalog_json` so Codex knows display names, context windows, reasoning levels, and tool-calling support for each model.

```bash theme={null}
fireconnect codex status   # shows whether the catalog is linked and on disk
```

The catalog includes serverless models that support tool calling with a non-zero context window, plus curated aliases such as `glm-fast-latest`. Deprecated models are excluded. If catalog generation fails (for example, due to an invalid API key), routing still works but Codex may show limited model metadata until you re-run `fireconnect codex on`.

`fireconnect codex model list` and `model select` filter the picker to models present in the catalog. JSON output from `model list` includes Fireworks IN / OUT pricing where known.

## Browsing and picking models

```bash theme={null}
fireconnect codex model list              # browse Codex-compatible serverless endpoints
fireconnect codex model select            # pick Codex's default model
fireconnect codex model select --search glm
fireconnect codex model list --json       # includes pricing metadata where known
```

## CLI reference

```bash theme={null}
fireconnect codex on              # Enable Fireworks routing
fireconnect codex off             # Restore original config
fireconnect codex status          # Check current provider and model
fireconnect codex model list      # Browse serverless endpoints
fireconnect codex model select    # Pick a model interactively
fireconnect codex model reset     # Reset model to default
fireconnect codex help            # Show harness-specific help
```

Run `fireconnect codex help` for all options.

### Switch models

```bash theme={null}
fireconnect codex on --main glm-5p2
fireconnect codex on --main deepseek-v4-flash
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
  Foundry routing requires a standard Azure API key. Fire Pass keys (`fpk_...`) are not supported. FireConnect does not write a Fireworks model catalog on the Foundry path — set your deployment with `--main`.
</Warning>

### Configure and enable

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect codex on --main FW-GLM-5.1
```

One-off routing:

```bash theme={null}
fireconnect codex on --azure --base-url https://<resource>.services.ai.azure.com --main FW-MiniMax-M2.5
```

### What gets written

FireConnect sets `model_provider = "fireworks-azure"` in `config.toml` with a **Fireworks on Microsoft Foundry** provider block pointed at your Foundry endpoint. The Azure API key is stored as `env_key = "AZURE_API_KEY"` when resolved from the environment, or written literally when passed with `--api-key`.

Pass your Foundry **deployment name** with `--main`. `model list` and `model select` browse the Fireworks serverless catalog only.

### Turn off Foundry routing

To switch back to the Fireworks gateway:

```bash theme={null}
fireconnect configure --provider fireworks
fireconnect codex on
source ~/.zshrc   # reload FIREWORKS_API_KEY if using keychain mode
```

To remove FireConnect entirely and restore your original `config.toml`:

```bash theme={null}
fireconnect codex off
```

See [Turn off Foundry routing](/ecosystem/fireconnect/microsoft-foundry#turn-off-foundry-routing) for details on global config behavior and `uninstall`.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
