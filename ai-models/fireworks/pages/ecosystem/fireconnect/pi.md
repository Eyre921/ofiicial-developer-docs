---
title: "Pi"
source: https://docs.fireworks.ai/ecosystem/fireconnect/pi
path: ecosystem/fireconnect/pi
---

Use Fireworks AI models in Pi with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [Pi](https://pi.dev) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

## Prerequisites

* [Pi](https://pi.dev) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* The FireConnect CLI (see [Install](/ecosystem/fireconnect/overview#install))

## Enable Fireworks routing

```bash theme={null}
export FIREWORKS_API_KEY=fw_...
fireconnect pi on
```

Restart Pi after enabling if it is already running.

```bash theme={null}
fireconnect pi status
```

## Using Fire Pass

Use your `fpk_...` key instead of a standard `fw_...` key:

```bash theme={null}
export FIREWORKS_API_KEY=fpk_...
fireconnect pi on --api-key fpk_...
```

FireConnect detects Fire Pass keys and defaults Pi to `glm-latest`.

## Default model

Pi routes a single default model. The default is `glm-latest`.

## What gets written

FireConnect:

* Sets `defaultProvider` / `defaultModel` in `~/.pi/agent/settings.json`
* Stores the API key in `~/.pi/agent/auth.json` (`$FIREWORKS_API_KEY` when from env, literal with `--api-key`)
* Writes `auth.json` at mode `0600`

FireConnect snapshots both files under `~/.fireconnect/pi/` before the first change. Running `fireconnect pi off` restores them byte-for-byte.

### API key handling

* If the key comes from `FIREWORKS_API_KEY`, it is written as `$FIREWORKS_API_KEY` so the secret stays out of settings.
* Passing `--api-key` writes the literal key to `auth.json` instead.

## Browsing and picking models

```bash theme={null}
fireconnect pi model list              # browse serverless endpoints
fireconnect pi model select            # pick Pi's default model
fireconnect pi model select --search glm
```

Fire Pass keys (`fpk_...`) show Fire Pass-supported models only.

## CLI reference

```bash theme={null}
fireconnect pi on              # Enable Fireworks routing
fireconnect pi off             # Restore original settings and auth
fireconnect pi status          # Check current provider and model
fireconnect pi model list      # Browse serverless endpoints
fireconnect pi model select    # Pick a model interactively
fireconnect pi model reset     # Reset model to default
fireconnect pi help            # Show harness-specific help
```

Run `fireconnect pi help` for all options.

### Switch models

```bash theme={null}
fireconnect pi on --main glm-5p1
```

### Turn off Fireworks routing

```bash theme={null}
fireconnect pi off
```

This restores your previous `settings.json` and `auth.json` from the backup in `~/.fireconnect/pi/`.

### Use a non-default settings file

```bash theme={null}
fireconnect pi on --settings-path /path/to/settings.json
```

## Fireworks on Microsoft Foundry

Pi supports **Fireworks on Microsoft Foundry** (CLI: `--provider azure` or `on --azure`). See the [FireConnect overview](/ecosystem/fireconnect/overview#fireworks-on-microsoft-foundry) and [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry) for portal setup.

### Configure and enable

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --harnesses pi

fireconnect pi on --main FW-GLM-5.1
```

One-off routing:

```bash theme={null}
fireconnect pi on --azure --base-url https://<resource>.services.ai.azure.com --main FW-MiniMax-M2.5
```

### What gets written

FireConnect registers a `fireworks-azure` **openai-completions** provider in Pi's `models.json` (labeled **Fireworks on Microsoft Foundry**) and sets `defaultProvider` / `defaultModel` in `settings.json`. The Azure API key is stored in `auth.json` as `$AZURE_API_KEY` when from the environment, or literally with `--api-key`.

Pass your Foundry **deployment name** with `--main`. `model list` and `model select` browse the Fireworks serverless catalog only.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
