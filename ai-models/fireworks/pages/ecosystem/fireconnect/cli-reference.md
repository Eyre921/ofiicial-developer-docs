---
title: "CLI reference"
source: https://docs.fireworks.ai/ecosystem/fireconnect/cli-reference
path: ecosystem/fireconnect/cli-reference
---

FireConnect global commands, providers, authentication, and migration

FireConnect uses **harness-first** syntax: `fireconnect <harness> <command>`. Bare harness names run `on` (for example, `fireconnect claude` is the same as `fireconnect claude on`).

## Global commands

```bash theme={null}
fireconnect login        # Sign in: browser (creates a key) or paste a key you have
fireconnect logout       # Clear the stored key (keychain entry + config ref)
fireconnect status       # Show sign-in state and where the key is stored
fireconnect configure    # Set the provider (Azure/Foundry) and Anthropic key for FireRouter
fireconnect model list   # Browse the global Fireworks coding model catalog
fireconnect demo         # Race Anthropic vs Fireworks on the same prompt
fireconnect upgrade      # Update FireConnect (curl/git install only)
fireconnect uninstall    # Disable all harnesses, restore configs, remove CLI
fireconnect help         # Show help
fireconnect --version    # Print the installed CLI version (-V also works)
```

Run `fireconnect help` for the overview, or `fireconnect claude help` (and similarly for other harnesses) for harness-level options.

## Sign in options

| Flag               | Use when                                                                                           |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| `--paste`          | Skip the browser chooser and paste a key at the prompt                                             |
| `--api-key fw_...` | Sign in with a key directly (no prompt)                                                            |
| `--with-token`     | Read a key from stdin (handy in CI): `echo "$FIREWORKS_API_KEY" \| fireconnect login --with-token` |
| `--account <id>`   | Enterprise SSO sign-in (same account id as `firectl signin`)                                       |
| `--force`          | Replace an existing stored key without a confirmation prompt                                       |
| `logout --revoke`  | Clear local credentials **and** revoke the machine key on Fireworks                                |

```bash theme={null}
fireconnect status --json   # machine-readable sign-in and key-storage details
```

`~/.fireconnect/config.json` stores a reference such as `{keychain:fireworks-api-key}` or `{env:FIREWORKS_API_KEY}`. It never stores a literal key in global config.

## Global configuration

`fireconnect configure` sets provider defaults and shared keys. It does **not** sign you in. Use `login` for your Fireworks API key.

```bash theme={null}
fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY

fireconnect configure --anthropic-api-key sk-ant-...
fireconnect configure --provider fireworks
```

In `configure`, `--api-key` is the **Azure** endpoint key and requires `--provider azure`. For Fireworks keys, use `fireconnect login`.

## Providers

| Provider flag         | Where inference runs           | API key               | Supported harnesses              |
| --------------------- | ------------------------------ | --------------------- | -------------------------------- |
| `fireworks` (default) | Fireworks gateway              | `fw_...` or `fpk_...` | All harnesses                    |
| `azure`               | Fireworks on Microsoft Foundry | Azure API key         | All harnesses except Claude Code |

Set the default with `fireconnect configure --provider fireworks` or `--provider azure`. Harness `on` commands use the configured provider unless you pass `--azure` or per-command `--base-url` / `--api-key` overrides.

## Per-harness commands

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --model glm-fast-latest --sonnet kimi-latest
fireconnect opencode on --model glm-fast-latest
```

Each CLI harness (`claude`, `opencode`, `codex`, `pi`, `deepagents`) supports:

* `fireconnect <harness> on`: route through the configured provider
* `fireconnect <harness> off`: restore your previous config
* `fireconnect <harness> status`: show provider, auth, and models
* `fireconnect <harness> help`: harness-specific help

Claude Code also has `fireconnect claude usage`. See [Session usage](/ecosystem/fireconnect/claude-code#session-usage).

Each IDE harness (`cursor`, `vscode`) supports `on`, `off`, `status`, and `help`. Commands that write settings require quitting the IDE first; `status` is read-only.

### Model flags

Use `--model <id>` for the primary model. Claude Code also supports slot flags: `--opus`, `--sonnet`, `--haiku`, `--fable`, `--subagent`.

Claude Code-only flags:

* `--interactive` — open the model mapping wizard (cannot combine with model flags)
* `--non-interactive` — skip first-run onboarding; use saved preferences or example defaults

On the Foundry path, pass your model with `--model` (for example, `--model FW-GLM-5.2`).

<Tip>
  `--main` is a retired alias for `--model` in v0.9.0+. Prefer `--model` in new scripts.
</Tip>

FireRouter flags (when a slot uses `firerouter`):

* `--anthropic-api-key sk-ant-...`: BYOK for pass-through to Claude Opus 4.8
* `--routing-preference <1-5>`: tune savings vs. quality (see [Routing preferences](/ecosystem/firerouter/routing-preferences))

## API key resolution

**Direct Fireworks routing** (`--provider fireworks`)

1. Explicit `--api-key`
2. OS keychain (via `fireconnect login`)
3. Global `~/.fireconnect/config.json` reference
4. `FIREWORKS_API_KEY` environment variable

Claude Code additionally reads harness-local keys from `~/.claude/settings.json` when FireConnect is already enabled there.

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Global `~/.fireconnect/config.json`
3. `AZURE_API_KEY` environment variable

## Migration from earlier syntax

### Pre-0.5.0 syntax

| Before                              | After                                         |
| ----------------------------------- | --------------------------------------------- |
| `fireconnect on`                    | `fireconnect claude on`                       |
| `fireconnect off`                   | `fireconnect claude off`                      |
| `fireconnect status`                | `fireconnect claude status`                   |
| `fireconnect list`                  | `fireconnect claude status`                   |
| `fireconnect set --main <id>`       | `fireconnect claude on --model <id>`          |
| `fireconnect reset`                 | `fireconnect claude on` (re-applies defaults) |
| `fireconnect on --harness opencode` | `fireconnect opencode on`                     |

### v0.9.1 changes

| Feature                | Details                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `fireconnect upgrade`  | In-place upgrade for curl/git installs; interactive terminals may prompt **Upgrade now?**      |
| Seamless upgrade       | From 0.9.0 on, harness settings (including Claude Code) are preserved across upgrade/reinstall |
| Claude `--interactive` | Model mapping wizard with fast/non-fast profile toggle; preferences persist per key type       |

### v0.9.0 changes

| Before                               | After                                                  |
| ------------------------------------ | ------------------------------------------------------ |
| `fireconnect <harness> model list`   | `fireconnect model list`                               |
| `fireconnect <harness> model select` | `fireconnect <harness> on --model <id>` or slot flags  |
| `fireconnect <harness> model reset`  | `fireconnect <harness> on` (re-applies defaults)       |
| `--main <id>` on `on`                | `--model <id>`                                         |
| Claude `apiKeyHelper` auth           | `X-Fireworks-Api-Key` custom header in `settings.json` |

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [Recommended models](/ecosystem/fireconnect/recommended-models)
* [Upgrade FireConnect](/ecosystem/fireconnect/overview#upgrade-fireconnect)
