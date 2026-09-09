---
title: "CLI reference"
source: https://docs.fireworks.ai/ecosystem/fireconnect/cli-reference
path: ecosystem/fireconnect/cli-reference
---

FireConnect global commands, providers, authentication, and migration

FireConnect uses **harness-first** syntax: `fireconnect <harness> <command>`. Bare harness names run `on` (for example, `fireconnect claude` is the same as `fireconnect claude on`).

To pick or switch models, see **[Models](/ecosystem/fireconnect/models)**. This page is the command and auth reference.

## Global commands

```bash theme={null}
fireconnect login        # Sign in: browser (creates a key) or paste a key you have
fireconnect logout       # Clear the stored key (keychain entry + config ref)
fireconnect status       # Sign-in state, machine environment, key storage, harness state
fireconnect configure    # Set the provider (Azure/Foundry) and Anthropic key for FireRouter
fireconnect model list   # Browse the global Fireworks coding model catalog
fireconnect claude demo  # Race two models in live Claude Code sessions
fireconnect upgrade      # Update FireConnect (curl/git install only)
fireconnect uninstall    # Disable all harnesses, restore configs, remove CLI
fireconnect help         # Show help
fireconnect --version    # Print the installed CLI version (-V also works; --json for machine-readable)
```

Global options for `model list`:

```bash theme={null}
fireconnect model list --search glm    # filter by name
fireconnect model list --refresh       # bypass the 1-hour cache
fireconnect model list --json            # machine-readable output
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

| Provider flag         | Where inference runs           | API key                                           | Supported harnesses                                   |
| --------------------- | ------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| `fireworks` (default) | Fireworks gateway              | `fw_...` (all harnesses) or `fpk_...` (not Codex) | All harnesses with a supported key                    |
| `azure`               | Fireworks on Microsoft Foundry | Azure API key                                     | All harnesses except Claude Code and DeepSeek Harness |

Set the default with `fireconnect configure --provider fireworks` or `--provider azure`. Harness `on` commands use the configured provider unless you pass `--azure` or per-command `--base-url` / `--api-key` overrides.

## Per-harness commands

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --model glm-fast-latest --sonnet kimi-latest
fireconnect opencode on --model glm-fast-latest
```

Each CLI harness (`claude`, `opencode`, `codex`, `chatgpt`, `pi`, `deepseek`) supports:

* `fireconnect <harness> on`: route through the configured provider
* `fireconnect <harness> off`: restore your previous config
* `fireconnect <harness> status`: show provider, auth, and models
* `fireconnect <harness> help`: harness-specific help

Claude Code also has `usage`, `live`, and `demo`. See [Usage and live meter](/ecosystem/fireconnect/claude-code#usage-and-live-meter) and the [side-by-side demo](/ecosystem/fireconnect/demo).

Each IDE harness (`cursor`, `vscode`) supports `on`, `off`, `status`, and `help`. Commands that write settings require quitting the IDE first; `status` is read-only.

### Model flags

Use `--model <id>` for the primary model. Claude Code also supports slot flags: `--opus`, `--sonnet`, `--haiku`, `--fable`, `--subagent`.

See **[Models](/ecosystem/fireconnect/models)** for a cross-harness quick reference, restart requirements, and common mistakes.

Claude Code-only flags:

* `--interactive`: open the model mapping wizard (cannot combine with model flags)
* `--non-interactive`: skip first-run onboarding; use saved preferences or example defaults

On the Foundry path, pass your model with `--model` (for example, `--model FW-GLM-5.2`).

<Tip>
  `--main` is a retired alias for `--model` in v0.9.0+. Prefer `--model` in new scripts.
</Tip>

FireRouter flags (when using `firerouter`):

* `--anthropic-api-key sk-ant-...`: BYOK for Claude Opus 5 pass-through (where the harness supports it)
* `--routing-preference <1-5>`: savings vs. quality (Claude Code, OpenCode, Pi, VS Code). See [Routing preferences](/ecosystem/firerouter/routing-preferences)

## API key resolution

**Direct Fireworks routing** (`--provider fireworks`)

1. Explicit `--api-key`
2. OS keychain (via `fireconnect login`)
3. Global `~/.fireconnect/config.json` reference
4. `FIREWORKS_API_KEY` environment variable

When `FIREWORKS_API_KEY` is set, `login` uses it without storing a copy. Unset it before `login --api-key`, `--with-token`, or browser sign-in.

Claude Code additionally reads harness-local keys from `~/.claude/settings.json` when FireConnect is already enabled there.

**Fireworks on Microsoft Foundry** (`--provider azure`)

1. Explicit `--api-key`
2. Global `~/.fireconnect/config.json`
3. `AZURE_API_KEY` environment variable

## Migration from earlier syntax

Only needed if you still have old scripts or muscle memory. Day-to-day use is `fireconnect <harness> on --model <id>`.

<AccordionGroup>
  <Accordion title="Pre-0.5.0 syntax">
    | Before                              | After                                         |
    | ----------------------------------- | --------------------------------------------- |
    | `fireconnect on`                    | `fireconnect claude on`                       |
    | `fireconnect off`                   | `fireconnect claude off`                      |
    | `fireconnect status`                | `fireconnect claude status`                   |
    | `fireconnect list`                  | `fireconnect claude status`                   |
    | `fireconnect set --main <id>`       | `fireconnect claude on --model <id>`          |
    | `fireconnect reset`                 | `fireconnect claude on` (re-applies defaults) |
    | `fireconnect on --harness opencode` | `fireconnect opencode on`                     |
  </Accordion>

  <Accordion title="v0.9.5 changes">
    | Feature          | Details                                                                                                                              |
    | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
    | Status line      | Session cost bar in Claude Code showing per-model Fireworks spend and cache rates. Your own `statusLine` is preserved.               |
    | ChatGPT app      | `fireconnect chatgpt` is an alias for `codex` — routes both Codex CLI and ChatGPT desktop from one config. Quit the app before `on`. |
    | Smart routers    | Pin `auto` or `auto-instant` on Claude slots for open-model mixes (preview).                                                         |
    | Claude defaults  | Sonnet → `deepseek-pro-latest`, Opus → `glm-latest`, Fable → `glm-flash-latest`. FireRouter still auto-pins Opus on first connect.   |
    | Model list cache | Catalog cached for 1 hour, works offline, `--refresh` refetches. Lists `auto`, `auto-instant`, and FireRouter.                       |
    | `claude status`  | Shows every slot, including defaults you never explicitly set.                                                                       |
    | GLM 5.3          | `glm-5p3` and `glm-5p3-flash` added; US-only `glm-5p3-flash-us` pricing corrected.                                                   |
  </Accordion>

  <Accordion title="v0.9.4 changes">
    | Feature        | Details                                                                       |
    | -------------- | ----------------------------------------------------------------------------- |
    | `claude demo`  | Improved side-by-side race cost calculation and terminal experience           |
    | Cursor restore | More robust `on` / `off`; uninstall waits for Cursor to quit before restoring |
    | `uninstall`    | Guided harness-by-harness restore that waits for running IDEs                 |
  </Accordion>

  <Accordion title="v0.9.3 changes">
    | Feature              | Details                                                                                                                                                                       |
    | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Claude defaults      | First connect uses `firerouter` for Opus; otherwise Opus defaults to `deepseek-pro-latest`. Sonnet stays on Claude's default, and Haiku/subagents use `deepseek-flash-latest` |
    | Deprecated Flash pin | Existing Claude `deepseek-v4-flash` defaults migrate to `deepseek-flash-latest` on the next `claude on`                                                                       |
    | Mixed models         | Claude Code can mix Anthropic and Fireworks models while routed through FireConnect                                                                                           |
    | Harness replacement  | `fireconnect deepseek` for DeepSeek Harness replaces `fireconnect deepagents`                                                                                                 |
    | Demo command         | Use `fireconnect claude demo`; the old top-level `fireconnect demo` form is deprecated                                                                                        |
  </Accordion>

  <Accordion title="v0.9.2 changes">
    | Feature               | Details                                                  |
    | --------------------- | -------------------------------------------------------- |
    | `claude live`         | tmux split with live usage meter                         |
    | `claude usage --days` | Wider session picker lookback (interactive mode only)    |
    | VS Code               | Uses `chat-completions` API (auto-migrated)              |
    | Cursor                | Hides built-in models; preserves native IDs on re-enable |
  </Accordion>

  <Accordion title="v0.9.1 changes">
    | Feature                   | Details                                                                                                                                                                 |
    | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `fireconnect upgrade`     | In-place upgrade for curl/git installs; interactive terminals may prompt **Upgrade now?**                                                                               |
    | Seamless upgrade          | From 0.9.0 on, harness settings (including Claude Code) are preserved across upgrade/reinstall                                                                          |
    | Upgrade from before 0.9.0 | With Claude connected, FireConnect restores original Claude settings before updating; run `fireconnect claude on` afterward. In CI, set `FIRECONNECT_AUTO_OFF_CLAUDE=1` |
    | Claude `--interactive`    | Model mapping wizard with fast/non-fast profile toggle; preferences persist per key type                                                                                |
  </Accordion>

  <Accordion title="v0.9.0 changes">
    | Before                               | After                                                  |
    | ------------------------------------ | ------------------------------------------------------ |
    | `fireconnect <harness> model list`   | `fireconnect model list`                               |
    | `fireconnect <harness> model select` | `fireconnect <harness> on --model <id>` or slot flags  |
    | `fireconnect <harness> model reset`  | `fireconnect <harness> on` (re-applies defaults)       |
    | `--main <id>` on `on`                | `--model <id>`                                         |
    | Claude `apiKeyHelper` auth           | `X-Fireworks-Api-Key` custom header in `settings.json` |
  </Accordion>
</AccordionGroup>

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [Models](/ecosystem/fireconnect/models)
* [Upgrade FireConnect](/ecosystem/fireconnect/overview#upgrade-fireconnect)
