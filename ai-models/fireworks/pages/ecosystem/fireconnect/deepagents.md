---
title: "Deep Agents"
source: https://docs.fireworks.ai/ecosystem/fireconnect/deepagents
path: ecosystem/fireconnect/deepagents
---

Use Fireworks AI models in LangChain Deep Agents Code with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [LangChain Deep Agents Code](https://docs.langchain.com/oss/python/deepagents/cli) (`dcode`) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

## Prerequisites

* [Deep Agents Code](https://docs.langchain.com/oss/python/deepagents/cli) (`dcode`) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* FireConnect **v0.9.0+** (see [Install](/ecosystem/fireconnect/overview#install))

<Note>
  **Azure routing not implemented yet for Deep Agents.** `fireconnect deepagents on` always configures direct Fireworks, even when global config has `--provider azure`. See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry#supported-harnesses).
</Note>

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

Deep Agents routes a single default model. The default is `glm-fast-latest`, written to config as `fireworks:<model-id>`.

## What gets written

FireConnect edits `~/.deepagents/config.toml`:

* Sets `[models].default` to `fireworks:<model>` and configures `[models.providers.fireworks]` with the Fireworks OpenAI-compatible base URL (`https://api.fireworks.ai/inference`) and a **baked** `api_key` literal (file mode `0600`)
* Stores your Fireworks API key in the FireConnect keychain via `login` or `deepagents on --api-key`, then bakes it into `config.toml`
* FireConnect does **not** write `~/.deepagents/.state/auth.json` — use dcode's `/auth` for credentials stored in that file

FireConnect snapshots `config.toml` under `~/.fireconnect/deepagents/` before the first change. Running `fireconnect deepagents off` restores it byte-for-byte.

## Browsing and picking models

```bash theme={null}
fireconnect model list --search glm
fireconnect deepagents on --model glm-5p1
```

Fire Pass keys (`fpk_...`) show Fire Pass-supported routers only.

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
fireconnect deepagents on --model glm-5p1
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

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
