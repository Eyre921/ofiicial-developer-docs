---
title: "OpenCode"
source: https://docs.fireworks.ai/ecosystem/fireconnect/opencode
path: ecosystem/fireconnect/opencode
---

Use Fireworks AI models in OpenCode with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [OpenCode](https://opencode.ai) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

## Prerequisites

* [OpenCode](https://opencode.ai) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* The FireConnect CLI (see [Install](/ecosystem/fireconnect/overview#install))

<Note>
  The installer registers Claude Code and OpenCode by default. If you only use OpenCode, you can skip `fireconnect claude on` and go straight to the steps below.
</Note>

## Enable Fireworks routing

```bash theme={null}
export FIREWORKS_API_KEY=fw_...
fireconnect opencode on
```

Restart OpenCode after enabling, then confirm routing:

```bash theme={null}
fireconnect opencode status
```

## Using Fire Pass

Use your `fpk_...` key instead of a standard `fw_...` key:

```bash theme={null}
export FIREWORKS_API_KEY=fpk_...
fireconnect opencode on --api-key fpk_...
```

FireConnect detects Fire Pass keys and defaults OpenCode to `glm-latest`.

## Default model

OpenCode routes a single default model (no opus/sonnet/haiku alias slots). The default is `glm-latest`, written to config as `fireworks-ai/glm-latest`.

Short model IDs like `glm-5p1` are expanded to full Fireworks paths (for example, `accounts/fireworks/models/glm-5p1`).

## What gets written

FireConnect merges a `fireworks-ai` provider block into `~/.config/opencode/opencode.json`:

* An OpenAI-compatible adapter pointed at `https://api.fireworks.ai/inference/v1`
* A default `model` set to `fireworks-ai/<model-id>` (for example, `fireworks-ai/glm-latest`)
* Your other providers are left untouched

FireConnect snapshots your original `opencode.json` before the first change. The snapshot lives in `~/.fireconnect/opencode/`. Running `fireconnect opencode off` restores the file byte-for-byte.

### API key handling

* If the key comes from `FIREWORKS_API_KEY`, it is written as `{env:FIREWORKS_API_KEY}` so the secret stays out of the config file.
* Passing `--api-key` writes the literal key instead.
* OpenCode's `auth.json` is never touched.

## Browsing and picking models

```bash theme={null}
fireconnect opencode model list              # browse serverless endpoints
fireconnect opencode model select            # pick OpenCode's default model
fireconnect opencode model select --search glm
```

`fireconnect opencode model list` resolves the API key from OpenCode's stored config. Fire Pass keys (`fpk_...`) show Fire Pass-supported models only.

## CLI reference

```bash theme={null}
fireconnect opencode on              # Enable Fireworks routing
fireconnect opencode off             # Restore original config
fireconnect opencode status          # Check current provider and model
fireconnect opencode model list      # Browse serverless endpoints
fireconnect opencode model select    # Pick a model interactively
fireconnect opencode model reset     # Reset model to default
fireconnect opencode help            # Show harness-specific help
```

Run `fireconnect opencode help` for all options.

### Switch models

```bash theme={null}
fireconnect opencode on --main glm-5p1
```

### Turn off Fireworks routing

```bash theme={null}
fireconnect opencode off
```

This restores your previous `opencode.json` from the backup in `~/.fireconnect/opencode/`.

### Use a non-default config file

```bash theme={null}
fireconnect opencode on --config-path /path/to/opencode.json
```

## Fireworks on Microsoft Foundry

OpenCode supports **Fireworks on Microsoft Foundry** (CLI: `--provider azure` or `on --azure`). See the [FireConnect overview](/ecosystem/fireconnect/overview#fireworks-on-microsoft-foundry) and [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry) for portal setup.

### Configure and enable

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --harnesses opencode

fireconnect opencode on --main FW-GLM-5.1
```

One-off routing without changing global config:

```bash theme={null}
fireconnect opencode on \
  --azure \
  --base-url https://<resource>.services.ai.azure.com \
  --main FW-MiniMax-M2.5
```

Pass your Foundry **deployment name** with `--main` — not a Fireworks serverless short ID like `glm-latest`.

### What gets written

FireConnect adds a `fireworks-azure` provider labeled **Fireworks on Microsoft Foundry** to `opencode.json`, pointed at your Foundry OpenAI-compatible endpoint (`.../openai/v1`). The default model reference becomes `fireworks-azure/<deployment-name>`.

`fireconnect opencode model list` and `model select` browse the Fireworks serverless catalog only. With Foundry, switch deployments with `on --main <deployment-name>`.

## Built-in provider connection

OpenCode also supports connecting to Fireworks directly without FireConnect:

1. Type `/connect` in OpenCode and search for **fireworks.ai**
2. Paste your Fireworks API key and press Enter
3. Type `/models` and select a model (for Fire Pass, choose a supported model such as **GLM Latest**)

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
