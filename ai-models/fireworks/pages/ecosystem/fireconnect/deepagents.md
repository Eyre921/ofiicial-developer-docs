---
title: "Deep Agents"
source: https://docs.fireworks.ai/ecosystem/fireconnect/deepagents
path: ecosystem/fireconnect/deepagents
---

Use Fireworks AI models in LangChain Deep Agents Code with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [LangChain Deep Agents Code](https://docs.langchain.com/oss/python/deepagents/cli) (`dcode`) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

<Tip>
  **Change models:** `fireconnect deepagents on --model <id>`. See [Models](/ecosystem/fireconnect/models).
</Tip>

## Prerequisites

* [Deep Agents Code](https://docs.langchain.com/oss/python/deepagents/cli) (`dcode`) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* FireConnect **v0.9.1+** (see [Install](/ecosystem/fireconnect/overview#install))

## Enable Fireworks routing

```bash theme={null}
fireconnect login
fireconnect deepagents on
```

Or pass the key once:

```bash theme={null}
fireconnect deepagents on --api-key fw_...
```

Restart `dcode` after `on` or `off` if it is already running.

```bash theme={null}
fireconnect deepagents status
```

## Default model

Deep Agents routes a single default model. The default is `kimi-fast-latest`, written to config as `fireworks:<model-id>`.

## What gets written

FireConnect edits `~/.deepagents/config.toml`:

* Sets `[models].default` to `fireworks:<model>` and configures `[models.providers.fireworks]` with the Fireworks OpenAI-compatible base URL (`https://api.fireworks.ai/inference`) and a **baked** `api_key` literal (file mode `0600`)
* Stores your Fireworks API key in the FireConnect keychain via `login` or `deepagents on --api-key`, then bakes it into `config.toml`
* FireConnect does **not** write `~/.deepagents/.state/auth.json`. Use dcode's `/auth` for credentials stored in that file

FireConnect snapshots `config.toml` under `~/.fireconnect/deepagents/` before the first change. Running `fireconnect deepagents off` restores it byte-for-byte.

## Browsing and picking models

```bash theme={null}
fireconnect model list --search glm
fireconnect deepagents on --model glm-5p2
```

Fire Pass keys only list Fire Pass routers. FireConnect rejects `--model firerouter` with Fire Pass (`fpk_...`) on every harness; use an `fw_...` key.

## FireRouter

```bash theme={null}
fireconnect deepagents on --model firerouter
```

Needs workspace BYOK (same as Cursor).

## CLI reference

```bash theme={null}
fireconnect deepagents on              # Enable Fireworks routing
fireconnect deepagents off             # Restore original config
fireconnect deepagents status          # Check current provider and model
fireconnect deepagents help            # Show harness-specific help
```

Run `fireconnect deepagents help` for all options.

### Switch models

```bash theme={null}
fireconnect deepagents on --model glm-5p2
```

### Turn off Fireworks routing

```bash theme={null}
fireconnect deepagents off
```

This restores your previous `config.toml` from the backup in `~/.fireconnect/deepagents/`.

### Use a non-default config file

```bash theme={null}
fireconnect deepagents on --config-path /path/to/config.toml
```

## Fireworks on Microsoft Foundry

Deep Agents supports **Fireworks on Microsoft Foundry** (CLI: `--provider azure` or `on --azure`). See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry) and the [portal setup guide](/ecosystem/integrations/azure-foundry).

<Warning>
  Foundry routing requires a standard Azure API key. Fire Pass keys (`fpk_...`) are not supported.
</Warning>

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect deepagents on --model FW-GLM-5.2
```

Pass your Foundry model with `--model` (for example, `FW-GLM-5.2`), not a Fireworks serverless short ID.

FireConnect writes a `fireworks-azure` provider in `config.toml` with the Foundry base URL and deployment name. `fireconnect model list` only browses the Fireworks serverless catalog on the direct gateway path.

To switch back to the Fireworks gateway:

```bash theme={null}
fireconnect configure --provider fireworks
fireconnect deepagents on
```

See [Turn off Foundry routing](/ecosystem/fireconnect/microsoft-foundry#turn-off-foundry-routing) for `off` and global config behavior.

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
