---
title: "DeepSeek Harness"
source: https://docs.fireworks.ai/ecosystem/fireconnect/deepseek
path: ecosystem/fireconnect/deepseek
---

Use Fireworks AI models in DeepSeek Harness with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

<Tip>
  **Change models:** `fireconnect deepseek on --model <id>`. See [Models](/ecosystem/fireconnect/models).
</Tip>

## Prerequisites

* [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* FireConnect **v0.9.3+** (see [Install](/ecosystem/fireconnect/overview#install))

## Enable Fireworks routing

```bash theme={null}
fireconnect login
fireconnect deepseek on
```

Or pass the key once:

```bash theme={null}
fireconnect deepseek on --api-key fw_...
```

Restart `dsh` after `on` or `off` if it is already running.

```bash theme={null}
fireconnect deepseek status
```

## Default model

DeepSeek Harness routes a single default model. The default is `kimi-fast-latest`.

## What gets written

FireConnect updates two files under `$DSH_HOME` (default `~/.dsh`):

* Adds a custom `fireworks` provider under `llm-pi-ai.providers` in `settings.yaml`, using the OpenAI-compatible endpoint at `https://api.fireworks.ai/inference/v1`
* Sets `agent-default-model` to the selected Fireworks model
* Stores the key as `FIREWORKS_API_KEY` in `.credentials.yaml` with file mode `0600`

FireConnect snapshots both files under `~/.fireconnect/deepseek/` before the first change. Running `fireconnect deepseek off` restores them.

## Browsing and picking models

```bash theme={null}
fireconnect model list --search glm
fireconnect deepseek on --model glm-5p2
```

Fire Pass keys only list Fire Pass routers. FireConnect rejects `--model firerouter` with Fire Pass (`fpk_...`) on every harness; use an `fw_...` key.

## FireRouter

```bash theme={null}
fireconnect deepseek on --model firerouter
```

DeepSeek Harness cannot attach a local Anthropic key, so Anthropic pass-through requires workspace BYOK.

## CLI reference

```bash theme={null}
fireconnect deepseek on              # Enable Fireworks routing
fireconnect deepseek off             # Restore original settings and credentials
fireconnect deepseek status          # Check current provider and model
fireconnect deepseek help            # Show harness-specific help
```

Run `fireconnect deepseek help` for all options.

### Switch models

```bash theme={null}
fireconnect deepseek on --model deepseek-flash-latest
```

### Turn off Fireworks routing

```bash theme={null}
fireconnect deepseek off
```

This restores the previous `settings.yaml` and `.credentials.yaml` snapshots.

### Use a non-default config file

```bash theme={null}
fireconnect deepseek on --config-path /path/to/settings.yaml
```

The credentials file remains beside the selected settings file.

<Note>
  Fireworks on Microsoft Foundry is not supported for DeepSeek Harness. `fireconnect deepseek on` uses the direct Fireworks gateway.
</Note>

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
