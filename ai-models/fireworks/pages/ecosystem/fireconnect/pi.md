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
* FireConnect **v0.9.1+** (see [Install](/ecosystem/fireconnect/overview#install))

## Enable Fireworks routing

```bash theme={null}
fireconnect login
fireconnect pi on
```

Restart Pi after enabling if it is already running.

```bash theme={null}
fireconnect pi status
```

## Using Fire Pass

Use your `fpk_...` key during `login` or with `--api-key`:

```bash theme={null}
fireconnect pi on --api-key fpk_...
```

FireConnect detects Fire Pass keys and defaults Pi to `kimi-fast-latest`.

## Default model

Pi routes a single default model. The default is `kimi-fast-latest`.

## What gets written

FireConnect:

* Sets `defaultProvider` / `defaultModel` in `~/.pi/agent/settings.json`
* Stores a **baked plaintext literal** in `fireworks.key` in `~/.pi/agent/auth.json` (mode `0600`)
* Registers the **preferred serverless catalog** in `~/.pi/agent/models.json` for Pi's `/model` picker

FireConnect snapshots both files under `~/.fireconnect/pi/` before the first change. Running `fireconnect pi off` restores them byte-for-byte.

## Browsing and picking models

```bash theme={null}
fireconnect model list --search glm
fireconnect pi on --model glm-5p1
```

Fire Pass keys (`fpk_...`) show Fire Pass-supported routers only and cannot select `firerouter`.

## FireRouter

```bash theme={null}
fireconnect pi on --model firerouter
fireconnect pi on --model firerouter --anthropic-api-key sk-ant-...
```

## CLI reference

```bash theme={null}
fireconnect pi on              # Enable Fireworks routing
fireconnect pi off             # Restore original settings and auth
fireconnect pi status          # Check current provider and model
fireconnect pi help            # Show harness-specific help
```

Run `fireconnect pi help` for all options.

### Switch models

```bash theme={null}
fireconnect pi on --model glm-5p1
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

Pi supports **Fireworks on Microsoft Foundry** (CLI: `--provider azure` or `on --azure`). See the [FireConnect overview](/ecosystem/fireconnect/microsoft-foundry) and [Microsoft Foundry integration guide](/ecosystem/integrations/azure-foundry) for portal setup.

### Configure and enable

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect pi on --model FW-GLM-5.2
```

One-off routing:

```bash theme={null}
fireconnect pi on --azure --base-url https://<resource>.services.ai.azure.com --model FW-MiniMax-M2.5
```

### What gets written

FireConnect registers a `fireworks-azure` **openai-completions** provider in Pi's `models.json` (labeled **Fireworks on Microsoft Foundry**) and sets `defaultProvider` / `defaultModel` in `settings.json`. The Azure API key is stored in `auth.json` as a literal when passed with `--api-key`, or as `$AZURE_API_KEY` when resolved from the environment.

Pass your Foundry model with `--model` (for example, `FW-GLM-5.2`). Use `fireconnect model list` only for browsing Fireworks serverless models on the direct gateway path.

### Turn off Foundry routing

To switch back to the Fireworks gateway:

```bash theme={null}
fireconnect configure --provider fireworks
fireconnect pi on
```

To remove FireConnect entirely and restore your original `settings.json`, `auth.json`, and `models.json`:

```bash theme={null}
fireconnect pi off
```

Restart Pi after switching or running `off`. See [Turn off Foundry routing](/ecosystem/fireconnect/microsoft-foundry#turn-off-foundry-routing) for details on global config behavior and `uninstall`.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
