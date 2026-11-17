---
title: "Configuration & environment"
source: https://developers.deepgram.com/developer-tools/cli/configuration.md
path: developer-tools/cli/configuration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Configuration & environment

The `dg` CLI reads settings from global options, a user config file, an optional project file, and environment variables. This page lists each one and the order the CLI applies them in.

## Global options

Global options go before the subcommand: `dg -o json listen audio.mp3`.

| Option              | Short | Default                    | Effect                                                                                                                                                                                                                                                                                                                                                 |
| ------------------- | ----- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--output`          | `-o`  | Human-readable text        | Output format: `json`, `yaml`, `table`, or `csv`. On `dg listen`, `json` and `yaml` print the server's real response body rather than an SDK-shaped one, `table`/`csv` are no-ops, and a `dg listen`-only `text` format (placed after the subcommand, not here) prints the transcript alone; see [Speech-to-text](/developer-tools/cli/speech-to-text) |
| `--quiet`           | `-q`  | Off                        | Suppress non-essential output                                                                                                                                                                                                                                                                                                                          |
| `--verbose`         | `-v`  | Off                        | Enable verbose output                                                                                                                                                                                                                                                                                                                                  |
| `--profile`         | `-p`  | The active profile         | Configuration profile to use                                                                                                                                                                                                                                                                                                                           |
| `--config`          | `-c`  | The user config file       | Path to another configuration file                                                                                                                                                                                                                                                                                                                     |
| `--base-url`        | none  | `https://api.deepgram.com` | API base URL; REST and WebSocket endpoints derive from it. Also set by `DEEPGRAM_BASE_URL`                                                                                                                                                                                                                                                             |
| `--api-key`         | none  | none                       | API key that overrides login, profile, and environment credentials                                                                                                                                                                                                                                                                                     |
| `--timing`          | none  | Off                        | Show performance timing                                                                                                                                                                                                                                                                                                                                |
| `--timing-detailed` | none  | Off                        | Show detailed performance timing                                                                                                                                                                                                                                                                                                                       |
| `--non-interactive` | none  | Off                        | Skip interactive prompts and use defaults                                                                                                                                                                                                                                                                                                              |

`--base-url` defaults to `https://api.deepgram.com`.

* `-o`, `-q`, and `-v` also work after the subcommand on most commands (`dg read ... -o json`). On `dg speak`, `-o`/`--output` after the subcommand still sets the output file path but is deprecated; use `--out-file` instead. On `dg plugin` and `dg skills` subcommands, put `-o` before the subcommand.
* On the root `dg`, `-p` means `--profile`; on `dg login` and the account commands (`dg keys`, `dg members`, `dg usage`, `dg billing`, `dg requests`), `-p` means `--project-id`.

## Config file location

* On Linux the file is `~/.config/deepctl/config.yaml`; on macOS, `~/Library/Application Support/deepctl/config.yaml`; on Windows, `%LOCALAPPDATA%\deepgram\deepctl\config.yaml`.
* The CLI copies a config file from the older `deepgram` directory into the `deepctl` directory automatically.
* `dg -c PATH` reads another file for one command.

## Project file

A `deepgram.yaml` file in the working directory (or a file passed with a non-default `-c`/`--config`) is loaded after the user config, but it can only override a restricted subset of settings: an allowlisted set of `output.*` fields, the `profiles` section (itself filtered the same way), and `base_url`, and only when `base_url` is a regional Deepgram API URL. Credentials, a non-regional `base_url`, and any other key are dropped, each with its own `WARN:`/`HINT:` pair on stderr naming the rejected key (never its value); stdout stays clean. Keep API keys out of a `deepgram.yaml` you commit regardless; the system keyring, which `dg login` uses by default, is the place for keys.

## Config schema

These are the keys the CLI reads:

```yaml
# Profile used when no active profile is set
default_profile: default
# Profile used by every command until you switch; dg login writes it
active_profile: default
# One entry per profile
profiles:
  default:
    # Present only when no system keyring is available
    api_key: YOUR_API_KEY
    project_id: YOUR_PROJECT_ID
    base_url: https://api.deepgram.com
# Automatic update check: daily (default), weekly, or never
update:
  check_enabled: true
  check_frequency: daily
# Set by dg ffprobe --path
tools:
  ffprobe_path: /usr/bin/ffprobe
# Telemetry: unhandled-exception reports to a loopback DEEPCTL_TELEMETRY_DSN only
telemetry:
  enabled: true
```

* `dg login` writes `active_profile`.
* `update.check_frequency` takes `daily` (the default), `weekly`, or `never`; `update.check_enabled: false` turns the check off.
* `dg ffprobe --path` sets `tools.ffprobe_path`, and `dg ffprobe --reset` clears it.

## Environment variables

| Variable                     | Effect                                                                                                                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEEPGRAM_API_KEY`           | API key                                                                                                                                                                                                                               |
| `DEEPGRAM_PROJECT_ID`        | Project ID for key, member, usage, billing, and request commands                                                                                                                                                                      |
| `DEEPGRAM_PROFILE`           | Sets `default_profile`; selects a profile only when no active profile is set                                                                                                                                                          |
| `DEEPGRAM_BASE_URL`          | API base URL                                                                                                                                                                                                                          |
| `DEEPCTL_TELEMETRY_DISABLED` | `1`, `true`, or `yes` turns telemetry off                                                                                                                                                                                             |
| `DEEPCTL_TELEMETRY_DSN`      | Sets the telemetry destination to a loopback address only (`localhost` or a loopback IP, for tests and local sinks); a non-loopback value is ignored, and with no DSN, telemetry sends nothing regardless of the other settings below |
| `DEEPCTL_TELEMETRY`          | `log` writes a telemetry report to stderr instead of sending it; `off` disables it, the same as `DEEPCTL_TELEMETRY_DISABLED=1`                                                                                                        |
| `DO_NOT_TRACK`               | `1` disables telemetry                                                                                                                                                                                                                |
| `DEEPCTL_SKILLS_REF`         | Git ref of `deepgram/skills` that `dg skills` installs                                                                                                                                                                                |
| `DEEPCTL_FORCE`              | Install scripts: reinstall even when the CLI is installed                                                                                                                                                                             |
| `DEEPCTL_VERSION`            | Install scripts: install a specific version                                                                                                                                                                                           |
| `CI`                         | `true` or `1` turns on Agent-Friendly Mode and disables telemetry                                                                                                                                                                     |

`DEEPGRAM_PROFILE` selects a profile only when no active profile is set; `dg login` sets one. To choose a profile per command, pass `--profile` (`-p`); to change the active one, run `dg profiles --switch <name>`.

If `DEEPGRAM_API_KEY`, `DEEPGRAM_PROFILE`, `DEEPGRAM_PROJECT_ID`, or `DEEPGRAM_BASE_URL` still holds an unexpanded `${...}` placeholder (for example, a CI template variable that was never substituted), the CLI ignores it rather than using the literal placeholder text, and prints `WARN: dg ignored <VARIABLE>: it holds a placeholder that was never filled in (${…}).` on stderr. The variable is then treated as unset, falling through to the next credential source.

## Precedence

For the API key, the CLI uses the first source that holds one:

1. `--api-key` (global flag)
2. The active profile's key in the system keyring
3. `DEEPGRAM_API_KEY`
4. The active profile's key in `config.yaml` (used only when no keyring is available, which is when `dg login` stores it there)

An expired browser-login credential counts as absent at step 2 or 4; see [Authentication](/developer-tools/cli/authentication). This order is unchanged from earlier releases, with one addition: off a terminal, a system keyring that doesn't answer within 2 seconds is skipped at step 2, falling through to the next source, with `WARN: The system keyring didn't answer within 2 s, so dg didn't use the key stored there.` on stderr.

For the project ID, the order is `-p` (`--project-id`) on the command, then `DEEPGRAM_PROJECT_ID`, then the profile's `project_id`.

`dg whoami` prints the key's source (`system keyring`, `config file`, or `DEEPGRAM_API_KEY (env)`).
