---
title: "CLI Reference"
source: https://docs.fireworks.ai/nexus/cli-reference
path: nexus/cli-reference
---

Nexus CLI reference: global commands, providers, sign-in and key storage, configure defaults, and harness commands for connecting coding tools.

Connect a harness with `nexus <harness>`. Use `off` to restore its previous settings, `status` to inspect the connection, and `help` to see harness-specific options. The optional `on` command remains available for backward compatibility. `nexus chatgpt` is an alias for `nexus codex`.

For model selection, see [Open Models](/nexus/open-models). For Nexus Auto behavior and account-level credentials, see [Nexus Auto](/nexus/auto) and [Provider Keys](/nexus/provider-keys). For cross-harness support, see [Coding Harnesses](/nexus/harnesses).

## Global commands

```bash wrap theme={null}
nexus login        # Sign in: browser (creates a key) or paste a key you have
nexus logout       # Clear stored Fireworks credentials
nexus status       # Sign-in state, environment, storage, and harness key sources
nexus harnesses    # List every supported harness and whether it is connected (--json for machine-readable)
nexus configure    # Set the provider or Foundry endpoint
nexus model list   # Browse the global Fireworks coding model catalog (alias: nexus models)
nexus auto         # Show which providers Nexus Auto can use (--providers fireworks for open models only, --reset for the default)
nexus claude demo  # Race two models in live Claude Code sessions
nexus upgrade      # Update Nexus CLI and refresh connected harnesses (curl/git install only)
nexus uninstall    # Disable all harnesses, restore configs, remove CLI
nexus help         # Show help
nexus --version    # Print the installed CLI version (-V also works; --json for machine-readable)
```

`nexus auto --providers` accepts only `fireworks` today. The setting is global and takes effect in each harness the next time you connect it. It has no effect in Cursor IDE.

Global options for `model list`:

```bash wrap theme={null}
nexus model list --search glm    # filter by name
nexus model list --refresh       # bypass the 1-hour cache
nexus model list --json          # machine-readable output
```

The list opens with Nexus Auto (`auto`), which picks an open or closed model for each turn.

Run `nexus help` for the overview, or `nexus claude help` (and similarly for other harnesses) for harness-level options.

## Sign in and key storage

| Flag | Use when |
| - | - |
| `--paste` | Skip the browser chooser and paste a key at the prompt |
| `--api-key fw_...` | Sign in with a key directly (no prompt) |
| `--with-token` | Read a key from stdin (handy in CI): `echo "$FIREWORKS_API_KEY" \| nexus login --with-token` |
| `--account <id>` | Enterprise SSO sign-in (same account id as `firectl signin`) |
| `--force` | Replace an existing stored key without a confirmation prompt |
| `logout --revoke` | Clear local credentials **and** revoke the key that browser sign-in created on this machine |

After you rotate your Fireworks key, run `nexus login`, even if you're signed in. It saves the key into your connected harnesses, including VS Code. For Cursor IDE and Claude Desktop, run `nexus cursor` or `nexus claude-desktop on` again.

```bash wrap theme={null}
nexus status --json   # machine-readable sign-in and key-storage details
```

For direct Fireworks routing, `~/.nexus/config.json` usually stores a secret-store reference or `{env:FIREWORKS_API_KEY}`, not the key itself. Run `nexus status` to see which backend is active.

Nexus CLI stores Anthropic, OpenAI, and Azure keys literally when you pass them to `configure`. It writes files containing literal keys with mode `0600`.

## Configure a provider

`nexus configure` sets the default provider, Foundry endpoint, or Azure key. It does not store your Fireworks API key. Use `nexus login` for that.

```bash wrap theme={null}
nexus configure \
  --provider azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key $AZURE_API_KEY

nexus configure --unset openai-api-key
nexus configure --provider fireworks
```

In `configure`, `--api-key` is the **Azure** endpoint key and requires `--provider azure`. For Fireworks keys, use `nexus login`.

`configure` still accepts `--anthropic-api-key` and `--openai-api-key`, but Nexus CLI doesn't send those keys on `auto` requests. They were for FireRouter routes. For Anthropic and OpenAI model turns, connect a [Provider Key](/nexus/provider-keys) or send headers with [manual setup](/nexus/manual-setup).

`--unset openai-api-key` and `--unset anthropic-api-key` clear a saved key from Nexus CLI and from every harness holding a copy. Restart those harnesses afterward. If Claude Code signs in with an Anthropic key in its own settings, Nexus CLI leaves that key alone.

## Providers

| Provider | Where inference runs | Credential |
| - | - | - |
| `fireworks` (default) | Fireworks gateway | Fireworks API key |
| `azure` | Fireworks on Microsoft Foundry | Azure API key |

See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry#choose-a-path) for current compatibility. Connections use the configured provider by default. To use Foundry for one command, pass `--azure`. Add `--base-url` or `--api-key` to override the saved endpoint or key. OpenCode, Pi, Cursor IDE, and VS Code accept `--azure`.

## Harness commands

CLI harnesses support connect, `off`, `status`, and `help`. Claude Code also supports `usage`, `live`, and `demo`. Claude Desktop (macOS and Linux) uses `nexus claude-desktop on`, `off`, and `status`, plus `mcp list`, `mcp add`, `mcp remove`, and `mcp sync` for connectors.

IDE commands require you to quit the app before Nexus CLI writes settings. `status` is read-only. See [Coding Harnesses](/nexus/harnesses) for app-specific commands and restart rules.

## Choose a model

Use `--model <id>` to select a model. The rest of the catalog stays in the picker.

```bash wrap theme={null}
nexus model list --search glm
nexus claude --model glm-fast-latest
nexus opencode --model glm-fast-latest
```

* `--model <id>`: sets the default model for new sessions.
* `--opus`, `--sonnet`, `--haiku`, `--fable`, `--subagent`: Claude Code only. Pin a tier slot to a model, or pass `native` to release it. See [Claude Code](/nexus/harnesses/claude-code).

```bash wrap theme={null}
nexus claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest
nexus claude --sonnet native
```

On Microsoft Foundry, pass the Azure deployment name, such as `FW-GLM-5.2`.

When using Nexus Auto:

* `--model auto`: use Nexus Auto. It's the default in every harness.
* `--anthropic-api-key` and `--openai-api-key`: these were for FireRouter routes. Connect commands reject them, and `nexus claude` accepts `--openai-api-key` but doesn't send it on `auto`. Connect a [Provider Key](/nexus/provider-keys) for Anthropic and OpenAI model turns instead.
* `--routing-preference`: Nexus CLI ignores this flag and removes an `x-routing-preference` header from Claude Code, OpenCode, Pi, and VS Code configs. Set [effort](/nexus/orchestration-preferences) in the harness instead.

See [Which harnesses can send provider keys](/nexus/auto#nexus-cli) for each harness's credentials.

## API key resolution

After `nexus login`, run `nexus <harness>` without `--api-key`. The flag on connect commands is an optional override (CI, rotation, or a key you have not stored yet). For the normal path, sign in once and omit it.

**Direct Fireworks routing** (`--provider fireworks`)

1. Explicit `--api-key` on the connect command
2. `FIREWORKS_API_KEY` environment variable
3. Stored credential referenced by `~/.nexus/config.json`

When `FIREWORKS_API_KEY` is set, `login` uses it without storing a copy. Unset it before `login --api-key`, `--with-token`, or browser sign-in.

When no global key resolves, connect can reuse a Fireworks key already stored in that harness's config. Claude Code status and usage also read its connected key from `~/.claude/settings.json`.

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Existing Azure key stored by the harness
3. Literal Azure key saved by `nexus configure`
4. `AZURE_API_KEY`, including a saved environment reference
