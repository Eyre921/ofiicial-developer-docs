---
title: "CLI Reference"
source: https://docs.fireworks.ai/nexus/cli-reference
path: nexus/cli-reference
---

FireConnect CLI reference: global commands, providers, sign-in and key storage, configure defaults, and harness commands for connecting coding tools.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

Connect a harness with `fireconnect <harness>`. Use `off` to restore its previous settings, `status` to inspect the connection, and `help` to see harness-specific options. The optional `on` command remains available for backward compatibility. `fireconnect chatgpt` is an alias for `fireconnect codex`. Run `fireconnect` with no arguments to use the [interactive menu](/nexus/fireconnect#interactive-menu).

For model selection, see [Open Models](/nexus/open-models). For router behavior and account-level credentials, see [FireRouter](/nexus/firerouter) and [Provider Keys](/nexus/provider-keys). For cross-harness support, see [Harness Compatibility](/nexus/harness-compatibility).

## Global commands

```bash wrap theme={null}
fireconnect              # Pick a harness and an action from the interactive menu
fireconnect login        # Sign in: browser (creates a key) or paste a key you have
fireconnect logout       # Clear stored Fireworks credentials
fireconnect status       # Sign-in state, environment, storage, and harness key sources
fireconnect harnesses    # List every supported harness and whether it is connected (--json for machine-readable)
fireconnect configure    # Set the provider, Foundry endpoint, or Anthropic and OpenAI keys
fireconnect model list   # Browse the global Fireworks coding model catalog (alias: fireconnect models)
fireconnect claude demo  # Race two models in live Claude Code sessions
fireconnect upgrade      # Update FireConnect and refresh connected harnesses (curl/git install only)
fireconnect uninstall    # Disable all harnesses, restore configs, remove CLI
fireconnect help         # Show help
fireconnect --version    # Print the installed CLI version (-V also works; --json for machine-readable)
```

Global options for `model list`:

```bash wrap theme={null}
fireconnect model list --search glm    # filter by name
fireconnect model list --refresh       # bypass the 1-hour cache
fireconnect model list --json          # machine-readable output
```

The list opens with the smart routers, which pick a model per user turn. `auto` balances cost and quality across open models. `auto-instant` is latency-first. If your account disables fast models, stay on `auto`.

Run `fireconnect help` for the overview, or `fireconnect claude help` (and similarly for other harnesses) for harness-level options.

## Sign in and key storage

| Flag | Use when |
| - | - |
| `--paste` | Skip the browser chooser and paste a key at the prompt |
| `--api-key fw_...` | Sign in with a key directly (no prompt) |
| `--with-token` | Read a key from stdin (handy in CI): `echo "$FIREWORKS_API_KEY" \| fireconnect login --with-token` |
| `--account <id>` | Enterprise SSO sign-in (same account id as `firectl signin`) |
| `--force` | Replace an existing stored key without a confirmation prompt |
| `logout --revoke` | Clear local credentials **and** revoke the key that browser sign-in created on this machine |

After you rotate your Fireworks key, run `fireconnect login`, even if you're signed in. It saves the key into your connected harnesses, including VS Code. For Cursor IDE and Claude Desktop, run `fireconnect cursor` or `fireconnect claude-desktop on` again.

```bash wrap theme={null}
fireconnect status --json   # machine-readable sign-in and key-storage details
```

For direct Fireworks routing, `~/.fireconnect/config.json` usually stores a secret-store reference or `{env:FIREWORKS_API_KEY}`, not the key itself. Run `fireconnect status` to see which backend is active.

FireConnect stores Anthropic, OpenAI, and Azure keys literally when you pass them to `configure`. It writes files containing literal keys with mode `0600`.

## Configure a provider

`fireconnect configure` sets the default provider, Foundry endpoint, Azure key, or shared Anthropic and OpenAI keys for FireRouter. It does not store your Fireworks API key. Use `fireconnect login` for that.

```bash wrap theme={null}
fireconnect configure \
  --provider azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key $AZURE_API_KEY

fireconnect configure --anthropic-api-key sk-ant-...
fireconnect configure --openai-api-key sk-...
fireconnect configure --unset openai-api-key
fireconnect configure --provider fireworks
```

In `configure`, `--api-key` is the **Azure** endpoint key and requires `--provider azure`. For Fireworks keys, use `fireconnect login`.

`--unset openai-api-key` and `--unset anthropic-api-key` clear a saved key from FireConnect and from every harness holding a copy. Restart those harnesses afterward. A key exported in your shell, such as `OPENAI_API_KEY`, still goes out until you unset it. If Claude Code signs in with an Anthropic key in its own settings, FireConnect leaves that key alone.

## Providers

| Provider | Where inference runs | Credential |
| - | - | - |
| `fireworks` (default) | Fireworks gateway | Fireworks API key |
| `azure` | Fireworks on Microsoft Foundry | Azure API key |

See [Foundry for Coding Harnesses](/nexus/microsoft-foundry#choose-a-path) for current compatibility. Connections use the configured provider by default. To use Foundry for one command, pass `--azure`. Add `--base-url` or `--api-key` to override the saved endpoint or key. OpenCode, Pi, Cursor IDE, and VS Code accept `--azure`.

## Harness commands

CLI harnesses support connect, `off`, `status`, and `help`. Claude Code also supports `usage`, `live`, and `demo`. Claude Desktop (macOS) uses `fireconnect claude-desktop on`, `off`, and `status`, plus `mcp list`, `mcp add`, `mcp remove`, and `mcp sync` for connectors.

IDE commands require you to quit the app before FireConnect writes settings. `status` is read-only. See [Coding Harnesses](/nexus/harnesses) for app-specific commands and restart rules.

## Choose a model or router

Use `--model <id>` to select a model. The rest of the catalog stays in the picker. In Claude Code, the model becomes your default and appears in `/model`; native tiers remain unchanged unless you pin them.

```bash wrap theme={null}
fireconnect model list --search glm
fireconnect claude --model glm-fast-latest
fireconnect opencode --model glm-fast-latest
```

In Claude Code, pin a tier slot with `--opus`, `--sonnet`, `--haiku`, `--fable`, or `--subagent`. Pins persist when you run `fireconnect claude` again. Pass `native` to release a slot:

```bash wrap theme={null}
fireconnect claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest
fireconnect claude --sonnet native
```

On Microsoft Foundry, pass the Azure deployment name, such as `FW-GLM-5.2`.

When using a model router:

* Pass `--model firerouter` to use FireRouter. To choose its models yourself, see [FireRouter](/nexus/firerouter).
* Pass `--anthropic-api-key sk-ant-...` when FireRouter should reach Claude models and the harness must forward a local key. Only OpenCode, Pi, and VS Code accept it. Claude Code uses its own sign-in, and other harnesses need an Anthropic [Provider Key](/nexus/provider-keys).
* Optional: pass `--openai-api-key sk-...`, or save it once with `fireconnect configure`, so FireRouter can reach GPT models. FireConnect sends it on `firerouter`. Harnesses that cannot send a local key, such as Cursor IDE, reject the flag. Codex rejects it too because GPT turns use its own sign-in. See [Codex](/nexus/harnesses#codex).
* `--routing-preference` is deprecated. FireConnect ignores it and prints a warning. See [Routing Preferences](/nexus/routing-preferences).

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
