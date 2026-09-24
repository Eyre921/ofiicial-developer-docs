---
title: "CLI Reference"
source: https://docs.fireworks.ai/nexus/cli-reference
path: nexus/cli-reference
---

FireConnect global commands, providers, authentication, and migration

Connect a harness with `fireconnect <harness>`. Use `off` to restore its previous settings, `status` to inspect the connection, and `help` to see harness-specific options. The optional `on` command remains available for backward compatibility.

For model selection and credentials, see [Open Models](/nexus/open-models) and [Harness Compatibility](/nexus/harness-compatibility). For router behavior, see [FireRouter](/nexus/firerouter).

## Global commands

```bash wrap theme={null}
fireconnect login        # Sign in: browser (creates a key) or paste a key you have
fireconnect logout       # Clear stored Fireworks credentials
fireconnect status       # Sign-in state, environment, storage, and harness key sources
fireconnect configure    # Set the provider, Foundry endpoint, or Anthropic key
fireconnect model list   # Browse the global Fireworks coding model catalog
fireconnect claude demo  # Race two models in live Claude Code sessions
fireconnect upgrade      # Update FireConnect (curl/git install only)
fireconnect uninstall    # Disable all harnesses, restore configs, remove CLI
fireconnect help         # Show help
fireconnect --version    # Print the installed CLI version (-V also works; --json for machine-readable)
```

Global options for `model list`:

```bash wrap theme={null}
fireconnect model list --search glm    # filter by name
fireconnect model list --refresh       # bypass the 1-hour cache
fireconnect model list --json            # machine-readable output
```

Run `fireconnect help` for the overview, or `fireconnect claude help` (and similarly for other harnesses) for harness-level options.

## Sign in and key storage

| Flag               | Use when                                                                                           |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| `--paste`          | Skip the browser chooser and paste a key at the prompt                                             |
| `--api-key fw_...` | Sign in with a key directly (no prompt)                                                            |
| `--with-token`     | Read a key from stdin (handy in CI): `echo "$FIREWORKS_API_KEY" \| fireconnect login --with-token` |
| `--account <id>`   | Enterprise SSO sign-in (same account id as `firectl signin`)                                       |
| `--force`          | Replace an existing stored key without a confirmation prompt                                       |
| `logout --revoke`  | Clear local credentials **and** revoke the machine key on Fireworks                                |

```bash wrap theme={null}
fireconnect status --json   # machine-readable sign-in and key-storage details
```

For direct Fireworks routing, `~/.fireconnect/config.json` usually stores a secret-store reference or `{env:FIREWORKS_API_KEY}`, not the key itself. Run `fireconnect status` to see which backend is active.

FireConnect may store an Anthropic or Azure key literally when you pass `--api-key`. It writes files containing literal keys with mode `0600`.

## Configure a provider

`fireconnect configure` sets the default provider, Foundry endpoint, Azure key, or shared Anthropic key. It does not store your Fireworks API key. Use `fireconnect login` for that.

```bash wrap theme={null}
fireconnect configure \
  --provider azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key $AZURE_API_KEY

fireconnect configure --anthropic-api-key sk-ant-...
fireconnect configure --provider fireworks
```

In `configure`, `--api-key` is the **Azure** endpoint key and requires `--provider azure`. For Fireworks keys, use `fireconnect login`.

## Providers

| Provider              | Where inference runs           | Credential        |
| --------------------- | ------------------------------ | ----------------- |
| `fireworks` (default) | Fireworks gateway              | Fireworks API key |
| `azure`               | Fireworks on Microsoft Foundry | Azure API key     |

See [Coding Harnesses](/nexus/harnesses#foundry-across-harnesses) for current Foundry compatibility. Connections use the configured provider by default. To use Foundry for one command, pass `--azure`, or pass both `--base-url` and `--api-key`.

## Harness commands

CLI harnesses support connect, `off`, `status`, and `help`. Claude Code also supports `usage`, `live`, and `demo`.

IDE commands require you to quit the app before FireConnect writes settings. `status` is read-only. See [Coding Harnesses](/nexus/harnesses) for app-specific commands and restart rules.

## Choose a model or router

Use `--model <id>` to add or select a model. In Claude Code, this adds one row to `/model`; native tiers remain unchanged.

```bash wrap theme={null}
fireconnect model list --search glm
fireconnect claude --model glm-fast-latest
fireconnect opencode --model glm-fast-latest
```

On Microsoft Foundry, pass the Azure deployment name, such as `FW-GLM-5.2`.

When using a model router:

* Pass any router ID with `--model`, such as `firerouter`, `firerouter/opus`, `firerouter/claude-opus-5-5`, or a custom route such as `firerouter/opus/glm-5p3`.
* Pass `--anthropic-api-key sk-ant-...` when the route contains a Claude family alias or Anthropic model ID and the harness must forward a local key.
* Pass `--routing-preference <level>` on supported harnesses. Claude Code accepts this flag only with bare `firerouter`.

## API key resolution

After `fireconnect login`, run `fireconnect <harness>` without `--api-key`. The flag on connect commands is an optional override (CI, rotation, or a key you have not stored yet). For the normal path, sign in once and omit it.

**Direct Fireworks routing** (`--provider fireworks`)

1. Explicit `--api-key` on the connect command
2. `FIREWORKS_API_KEY` environment variable
3. Stored credential referenced by `~/.fireconnect/config.json`

When `FIREWORKS_API_KEY` is set, `login` uses it without storing a copy. Unset it before `login --api-key`, `--with-token`, or browser sign-in.

When no global key resolves, connect can reuse a Fireworks key already stored in that harness's config. Claude Code status and usage also read its connected key from `~/.claude/settings.json`.

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Existing Azure key stored by the harness
3. Literal Azure key saved by `fireconnect configure`
4. `AZURE_API_KEY`, including a saved environment reference

## Legacy syntax

Current usage is `fireconnect <harness> --model <id>`.

| Earlier syntax                       | Current syntax                       |
| ------------------------------------ | ------------------------------------ |
| `fireconnect on`                     | `fireconnect claude`                 |
| `fireconnect off`                    | `fireconnect claude off`             |
| `fireconnect on --harness opencode`  | `fireconnect opencode`               |
| `fireconnect <harness> model list`   | `fireconnect model list`             |
| `fireconnect <harness> model select` | `fireconnect <harness> --model <id>` |
| `fireconnect <harness> model reset`  | `fireconnect <harness>`              |
| `fireconnect demo`                   | `fireconnect claude demo`            |
| `fireconnect deepagents`             | `fireconnect deepseek`               |

`--main` is rejected with a hint to use `--model`. Claude tier flags such as `--opus` and `--sonnet` are rejected on connect. `--interactive` is not supported for Claude Code.
