---
title: "CLI Reference"
source: https://docs.fireworks.ai/nexus/cli-reference
path: nexus/cli-reference
---

Nexus CLI reference: global commands, providers, sign-in and key storage, configure defaults, and harness commands for connecting coding tools.

Connect a harness with `nexus <harness>`. Use `off` to restore its previous settings, `status` to inspect the connection, and `help` to see harness-specific options. `nexus <harness> on` is the explicit form of the connect command. `nexus codex` and `nexus chatgpt` take the same options and switch both apps, because the Codex CLI and the ChatGPT desktop app share `~/.codex/config.toml`.

For model selection, see [Open Models](/nexus/open-models). For Nexus Auto behavior and account-level credentials, see [Nexus Auto](/nexus/auto) and [Provider Keys](/nexus/provider-keys). For cross-harness support, see [Coding Harnesses](/nexus/harnesses).

## Global commands

```bash wrap theme={null}
nexus login        # Sign in: browser (creates a key) or paste a key you have
nexus logout       # Clear the stored Fireworks key and saved Anthropic and OpenAI keys
nexus status       # Sign-in state, environment, key storage, and every harness (connected, installed)
nexus configure    # Set the provider: Fireworks or Microsoft Foundry
nexus model list   # Browse the Fireworks coding model catalog (alias: nexus models)
nexus auto         # Show Nexus Auto's providers, saved keys, and Provider Keys
nexus update       # Update Nexus CLI (alias: nexus upgrade; curl/git install only)
nexus uninstall    # Restore every connected harness, then remove Nexus CLI and ~/.nexus
nexus help         # Show help (nexus help <topic> for one command)
nexus --version    # Print the installed CLI version (-V also works; --json for machine-readable)
```

* `nexus status --json` returns the same details for scripts. `nexus status` exits non-zero when you're signed out.
* `nexus harnesses` still works but is deprecated. `nexus status` lists every harness.
* `nexus logout` does not unset `FIREWORKS_API_KEY` in your shell.
* `nexus uninstall` asks you to quit open IDEs before it restores them. `nexus uninstall --force` skips the questions, for CI and scripts.

`nexus auto --providers` accepts only `fireworks` today. `nexus auto --reset` returns to the default. The setting is global and takes effect in each harness the next time you connect it. It has no effect in Cursor IDE. Your account's model restrictions always apply first.

`nexus key export` prints your Fireworks key for scripts. Add `--openai` or `--anthropic` to print a saved provider key instead, and `--stored-only` to prefer the stored key over environment variables.

## Save Anthropic and OpenAI keys for Nexus Auto

`nexus auto` saves the Anthropic and OpenAI keys Nexus Auto can use. Run your harness command again afterward:

```bash wrap theme={null}
nexus auto --anthropic-api-key     # prompts for the key (or --openai-api-key)
nexus opencode
nexus auto                         # shows providers, saved keys, and Provider Keys
nexus auto --unset openai-api-key  # removes the key here and from every harness
```

* Pass the flag on its own and Nexus CLI prompts for the key, so it stays out of your shell history. With `--json`, pass the key as the flag's value.
* Nexus CLI sends a saved key only from harnesses with no sign-in of their own for that provider. Claude Code never gets the Anthropic key, and Codex never gets the OpenAI key. See [Which harnesses can send provider keys](/nexus/auto#nexus-cli).
* Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
* While `nexus auto --providers fireworks` is set, saved keys stay saved but aren't sent.
* `--unset` also removes the key from every harness that holds a copy. Restart those harnesses afterward.
* If an IDE is open, `--unset` skips it and tells you to quit it and run the command again.
* If Claude Code signs in with an Anthropic key in its own settings, `--unset` leaves that key alone.
* `nexus logout` also removes saved Anthropic and OpenAI keys from this machine.

`nexus auto` also shows each [Provider Key](/nexus/provider-keys) on your Fireworks account as connected, not connected, or not enabled on your account. Provider Keys work in every harness. A key saved with `nexus auto` takes precedence over the Provider Key for that provider. Nexus CLI only reads Provider Keys. Connect them in the dashboard.

`nexus auto --json` returns `keys` and `keysSent` booleans and a `providerKeys` status. It never prints a key.

Global options for `model list`:

```bash wrap theme={null}
nexus model list --search glm    # filter by name
nexus model list --refresh       # bypass the 1-hour cache (keeps the cached list if offline)
nexus model list --json          # machine-readable output
```

The list opens with Nexus Auto (`auto`), which picks an open or closed model for each turn.

Run `nexus help` for the overview, or `nexus <harness> help` (for example, `nexus claude help`) for every option on one harness.

## Sign in and key storage

| Flag | Use when |
| - | - |
| `--paste` | Skip the browser chooser and paste a key at the prompt |
| `--api-key fw_...` | Sign in with a key directly (no prompt) |
| `--with-token` | Read a key from stdin, for CI: `nexus login --with-token < key.txt` |
| `--account <id>` | Enterprise SSO sign-in (same account id as `firectl signin`) |
| `--force` | Replace an existing stored key without a confirmation prompt |
| `logout --revoke` | Clear local credentials **and** revoke the key that browser sign-in created on this machine, without asking |

After you rotate your Fireworks key, run `nexus login`, even if you're signed in. It saves the key into your connected harnesses, including VS Code. Quit VS Code first. For Cursor IDE and Claude Desktop, run `nexus cursor` or `nexus claude-desktop on` again.

```bash wrap theme={null}
nexus status --json   # machine-readable sign-in and key-storage details
```

`~/.nexus/config.json` holds a reference to your Fireworks key (`{keychain:fireworks-api-key}`), not the key itself. The key lives in the OS keychain, or in an encrypted-file or plaintext fallback when no secret service exists. Run `nexus status` to see which backend is active.

Nexus CLI stores Anthropic and OpenAI keys literally when you save them with `nexus auto`, and the Azure key when you pass it to `configure`. Files that contain literal keys have mode `0600`.

## Configure a provider

`nexus configure` sets the default provider, Foundry endpoint, or Azure key. It does not store your Fireworks API key. Use `nexus login` for that.

```bash wrap theme={null}
nexus configure \
  --provider azure \
  --base-url "https://YOUR_RESOURCE.services.ai.azure.com" \
  --api-key $AZURE_API_KEY

nexus configure --provider fireworks
```

In `configure`, `--api-key` is the **Azure** endpoint key and requires `--provider azure`. For Fireworks keys, use `nexus login`.

`configure` still accepts `--anthropic-api-key`, `--openai-api-key`, and `--unset`, but they are deprecated and print a warning. Use [`nexus auto`](#save-anthropic-and-openai-keys-for-nexus-auto) with the same flags.

## Providers

| Provider | Where inference runs | Credential |
| - | - | - |
| `fireworks` (default) | Fireworks gateway | Fireworks API key |
| `azure` | Fireworks on Microsoft Foundry | Azure API key |

See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry#choose-a-path) for current compatibility. Connections use the configured provider by default. To use Foundry for one command, pass `--azure`. Add `--base-url` or `--api-key` to override the saved endpoint or key. OpenCode, Pi, Cursor IDE, and VS Code accept `--azure`.

## Harness commands

Every harness supports connect, `off`, `status`, and `help`. `status --json` returns the same state for scripts.

Claude Code adds two commands:

```bash wrap theme={null}
nexus claude usage       # Pick a session and open its live cost meter
nexus claude demo        # Race two models on one prompt through Claude Code
nexus claude demo clean  # Remove demo output
```

See [Usage and Cost](/nexus/metrics#inspect-a-session) for `usage` options. Run `nexus help demo` for demo options.

Claude Desktop (macOS and Linux) uses `nexus claude-desktop on`, `off`, and `status`, plus `mcp list`, `mcp add`, `mcp remove`, and `mcp sync` for connectors. Quit and reopen Claude Desktop after `on` or `off`.

Quit Cursor IDE, VS Code, the Copilot App, and the ChatGPT desktop app before you connect or run `off`. If one is open, Nexus CLI waits for you to quit it. `--force` writes anyway, which isn't recommended. `status` is read-only.

Harness commands accept `--home <path>` to read configs under another home directory. Most also accept a path flag for the harness's own config, such as `--settings-path` or `--config-path`. Run `nexus <harness> help` to see it.

Connect refuses a harness that isn't installed and writes nothing. Nexus CLI counts any sign of the tool: its command, its app, its editor extension, or data only the tool writes. If the tool is installed somewhere Nexus CLI doesn't look, pass `--skip-install-check`. The check is skipped for a harness that is already connected, and when you point at a config with a path flag. See [Coding Harnesses](/nexus/harnesses) for app-specific commands and restart rules.

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

* `--model auto`: use Nexus Auto. It's the default in every harness. Claude Code's tier slots keep Claude's own defaults.
* `--anthropic-api-key` and `--openai-api-key`: harness commands don't accept them. Save the key with [`nexus auto`](#save-anthropic-and-openai-keys-for-nexus-auto), or connect a [Provider Key](/nexus/provider-keys).
* `--routing-preference`: deprecated, with no effect. `nexus update` removes the `x-routing-preference` header that earlier versions wrote into harness configs. Set [effort](/nexus/orchestration-preferences) in the harness instead.

See [Which harnesses can send provider keys](/nexus/auto#nexus-cli) for each harness's credentials.

## API key resolution

After `nexus login`, run `nexus <harness>` without `--api-key`. The flag on connect commands is an optional override, for CI, rotation, or a key you haven't stored yet. Connect also saves a key you pass this way.

**Direct Fireworks routing** (`--provider fireworks`)

1. Explicit `--api-key` on the connect command
2. `FIREWORKS_API_KEY` environment variable
3. Stored credential referenced by `~/.nexus/config.json`

When `FIREWORKS_API_KEY` is set, `login` uses it without storing a copy. Unset it before you sign in to store a key. While it is set, `login --api-key`, `--with-token`, `--paste`, and `--account` fail without changing anything.

When no global key resolves, connect can reuse a Fireworks key already stored in that harness's config and saves it to key storage. Claude Code `status` and `usage` also read the connected key from `~/.claude/settings.json`.

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Existing Azure key stored by the harness
3. Literal Azure key saved by `nexus configure`
4. `AZURE_API_KEY`, including a saved environment reference

## Deprecated and removed

**Deprecated** still works and prints a warning. **Removed** no longer works, and a removed command or flag fails with a message that names the replacement. `nexus update` moves your saved settings off removed options. See [Release Notes](/nexus/release-notes) for each version.

| Old | Status | Use instead | Since |
| - | - | - | - |
| `nexus harnesses` | Deprecated | `nexus status` | 0.10.1 |
| `nexus configure --anthropic-api-key`, `--openai-api-key`, `--unset` | Deprecated | [`nexus auto`](#save-anthropic-and-openai-keys-for-nexus-auto) with the same flags | 0.10.1 |
| `--anthropic-api-key` and `--openai-api-key` on harness commands, such as `nexus opencode` | Removed | `nexus auto --anthropic-api-key` or `--openai-api-key`, then the harness command | 0.10.1 |
| `nexus claude live` | Removed | The Claude Code status line, or `nexus claude usage` | 0.10.1 |
| `--routing-preference` | Deprecated, no effect | [Effort](/nexus/orchestration-preferences) in your harness | 0.10.0 |
| `firerouter` and `firerouter/...` models | Removed | `auto`, or pin a model ID | 0.10.0 |
| `auto-instant` | Removed | `auto` | 0.10.0 |
| `fireconnect` command | Renamed | `nexus`. See [Upgrading from FireConnect](/nexus/cli#upgrading-from-fireconnect) | 0.10.0 |
| `FIRECONNECT_*` environment variables | Deprecated | `NEXUS_*` | 0.10.0 |
| `~/.fireconnect` | Moved | `~/.nexus`. The old path stays as a link | 0.10.0 |
| Codex on Microsoft Foundry | Removed | `nexus configure --provider fireworks`, then `nexus codex`. See [Nexus for Microsoft Foundry](/nexus/microsoft-foundry) | 0.9.9 |
| `fireworks-websearch` MCP server | Removed | Native web search. See [Web Search](/nexus/web-search) | 0.9.7 |
| `nexus demo` | Deprecated | `nexus claude demo` | 0.9.3 |
| Deep Agents harness | Removed | [DeepSeek Harness](/nexus/harnesses/deepseek), `nexus deepseek` | 0.9.3 |

These old flag names fail with the current spelling:

| Old flag | Use instead |
| - | - |
| `--main`, `--model-id` | `--model` |
| `--router` | `--model auto` |
| `--fireworks-only` | `nexus auto --providers fireworks` |
| `--anthropic-key` | `nexus auto --anthropic-api-key` |
| `--last_n` | `--last-n` |
