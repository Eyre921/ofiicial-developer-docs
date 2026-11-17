---
title: "Troubleshooting"
source: https://developers.deepgram.com/developer-tools/cli/troubleshooting.md
path: developer-tools/cli/troubleshooting
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Troubleshooting

Each heading below is an error the `dg` CLI prints, followed by its cause and the fix. The second half of the page covers the `dg debug` and `dg ffprobe` diagnostics.

## Error messages

### ``Your Deepgram credential has expired. Run `dg login` again.``

**Cause:** the time-limited credential that browser login (`dg login`) stored has expired, and no `--api-key` or `DEEPGRAM_API_KEY` supplies another key.

**Fix:** run `dg login`. For CI, set `DEEPGRAM_API_KEY`, which carries no CLI-side expiry. See [Authentication](/developer-tools/cli/authentication).

### `DEEPGRAM_API_KEY is not set in the configuration file`

**Cause:** the CLI found no credential at all: no stored `dg login` credential, no `DEEPGRAM_API_KEY`, and no `--api-key`. Every authenticated command, including `dg mcp`, exits `1` with this message.

**Fix:** run `dg login`, or export `DEEPGRAM_API_KEY`.

### `Project ID is required for this command. Set DEEPGRAM_PROJECT_ID or configure via profile.`

**Cause:** key, member, usage, billing, and request commands act on one project, and none is set.

**Fix:** run `dg projects --set-default <project-id>`, export `DEEPGRAM_PROJECT_ID`, or pass `-p <project-id>` on the command.

### `Warning: Project ID '<id>' not found. API key will still be stored.`

**Cause:** `dg login --api-key <key> --project-id <id>` looked up the project and the API returned `404 Not Found`. The CLI stores the key without the project ID and exits `0`, and its summary still shows the ID you passed. Unless `DEEPGRAM_PROJECT_ID` or `-p` supplies a project, the next project command fails with `Project ID is required for this command`.

**Fix:** find the project's ID with `dg projects --list`, then log in again with it: `dg login --api-key YOUR_API_KEY --project-id <project-id>`. Run `dg whoami` to confirm the stored project ID.

### `Warning: API key format doesn't match expected pattern`

**Status:** fixed in CLI `0.5.0`. `dg login --api-key` no longer checks a real key against a format pattern, and no longer needs `-f` to accept one. If you're on `0.5.0` or later and `dg login --api-key` still stops, see the next two entries instead.

### `ERROR: DEEPGRAM_API_KEY is set, and logging in saves a profile that dg will use instead of it.`

**Cause:** `dg login --api-key` found `DEEPGRAM_API_KEY` already set in your shell. Saving a profile now would shadow that variable the next time you run `dg`, so the command stops and exits `1` with `confirmation_required`.

**Fix:** add `--yes` if you want the new profile to take over: `dg login --api-key YOUR_API_KEY --yes`. Otherwise, drop the `dg login` step and keep using `DEEPGRAM_API_KEY` directly.

### `confirmation_required`

**Cause:** `dg login` or `dg init` needs to confirm an action (saving a profile that would shadow `DEEPGRAM_API_KEY`, or running a template's setup and start steps) and nothing can answer the prompt: there's no terminal, and no `-f`/`--yes`/`--install`/`--start`. The command exits `1` instead of running the action.

**Fix:** pass the flag the command's own `--help` names for that confirmation (`--yes` for `dg login`; `--yes` inside an AI-agent session, or `--install`/`--start` outside one, for `dg init`).

### `"code": "invalid_argument"` from `dg speak` under agent mode

**Cause:** under a hard agent signal (see [Agent-Friendly Mode](/developer-tools/cli/getting-started#agent-friendly-mode)), `dg speak` applies two guardrails that don't apply on an interactive terminal: it refuses to read piped stdin unless the text argument is literally `-`, and it refuses to write audio into a pipe. Both print an error and a hint, then exit `1` with the generic `"code": "invalid_argument"` (there's no separate machine-readable code for each case).

**Fix:** pass `-` explicitly to read stdin (`dg speak - --out-file out.wav < text.txt`), and always pass `--out-file` for the audio when running under CI, Claude Code, Codex, or another agent signal; don't rely on piping audio to a player in that environment.

### `WARN: dg ignored <VARIABLE>: it holds a placeholder that was never filled in (${…}).`

**Cause:** `DEEPGRAM_API_KEY`, `DEEPGRAM_PROFILE`, `DEEPGRAM_PROJECT_ID`, or `DEEPGRAM_BASE_URL` still holds an unexpanded `${...}` placeholder, usually from a CI template variable that was never substituted. The CLI treats the variable as unset rather than using the literal placeholder text, and prints this warning on stderr; stdout stays clean.

**Fix:** fix the CI template so the variable expands, or unset it if it's not meant to be used.

### `WARN: The system keyring didn't answer within 2 s, so dg didn't use the key stored there.`

**Cause:** off a terminal, the system keyring didn't respond within 2 seconds, so the CLI skipped it for that lookup and fell through to the next credential source (`DEEPGRAM_API_KEY`, then the config file).

**Fix:** usually nothing to do, since the CLI already fell through; if this happens often, check whether the keyring backend on that machine is slow or misconfigured.

### `validation errors for MemberInfo`

**Cause:** `dg members --list` fails on a project member whose account has no first or last name.

**Fix:** list members through the API: `dg api /v1/projects/<project-id>/members`.

### `Flux STT (flux-general-en) is streaming-only and cannot transcribe a file or URL.`

**Cause:** `--model flux-general-en` with a file or URL source. Flux STT runs on live audio only. The command exits `1`.

**Fix:** stream the audio through `--mic` or stdin, or use `nova-3` for pre-recorded audio:

```shell
ffmpeg -i call.wav -f s16le -ar 16000 -ac 1 - | dg listen --model flux-general-en --encoding linear16
```

### `Error: No such option '-o'.`

**Cause:** `-o` placed after a subcommand that has no `-o` of its own, such as `dg skills list -o json`. The CLI follows the error with `Hint: '-o' is a global option and must come before the subcommand` and exits `1`.

**Fix:** put `-o` before the subcommand: `dg -o json skills list`.

### `Refusing to delete key ... without confirmation. Pass --yes to confirm.`

**Cause:** `dg keys --delete` in a non-interactive session (CI, an agent, a pipe) without `--yes`. The command exits `1`.

**Fix:** add `--yes` after you confirm the key ID, or run `--dry-run` first to preview.

### `Missing required tools:`

**Cause:** `dg init` needs `git`, `node`, `npm`, `make`, and `curl` on your PATH. It prints one line per missing tool and exits `1` before cloning.

**Fix:** install the listed tools and run `dg init` again.

### `Template not found: <slug>`

**Cause:** the slug passed to `dg init` is not in the template gallery. The command exits `1`.

**Fix:** run `dg init --list` to see every slug, or `dg init --list --search <keyword>` to filter.

### `Host key verification failed`

**Cause:** during `dg init`, the starter's `make init` clones its `frontend/` and `contracts/` submodules over SSH, which fails without a GitHub SSH key. `dg init` still prints `Done! ... is ready` and exits `0`.

**Fix:** fetch the submodules over HTTPS, then run setup again:

```shell
# Rewrite the SSH submodule URLs to HTTPS and fetch them
git -c url."https://github.com/".insteadOf="git@github.com:" submodule update --init --recursive
# Install the backend and frontend dependencies
make init
```

### `ERROR: dg mcp supports only the stdio transport, not <value>. Nothing was started.`

**Cause:** `dg mcp --transport` with a value other than `stdio`, most often an old config left over from before CLI `0.4.1` removed the SSE transport. `--transport`, `--host`, and `-p`/`--port` still exist as flags for compatibility with those configs, but `dg mcp` now runs only over stdio. The command exits `1`.

**Fix:** remove `--transport` (and `--host`/`--port`, if set) from your MCP client config and let it start `dg mcp` with no flags. For a client that needs streamable HTTP, add the hosted docs MCP server URL directly instead of `dg mcp`; see [MCP Server](/developer-tools/cli/mcp-server).

### `Please update using apt`

**Cause:** `dg update` can report this for a CLI that was installed with `pip` as root into the system Python.

**Fix:** run `pip install --upgrade deepctl`. See [Installation](/developer-tools/cli/installation).

### `Error accessing credentials:`

**Cause:** `dg profiles --switch` on a machine with no system keyring.

**Fix:** pass `--profile <name>` on each command instead.

## Diagnose with `dg debug`

### `dg debug audio`

Analyzes a file's or URL's compatibility with Deepgram using ffprobe and suggests encoding settings.

```shell
dg debug audio -f recording.wav
```

| Option                   | Effect                                                           |
| ------------------------ | ---------------------------------------------------------------- |
| `-f`, `--file`           | Path or URL of the audio to check (required)                     |
| `-v`, `--verbose`        | Show detailed diagnostic information                             |
| `-vv`, `--extra-verbose` | Show raw ffprobe output                                          |
| `--ffprobe-args`         | Custom ffprobe arguments, such as `'-show_streams -show_format'` |

### `dg debug network`

Tests connectivity to Deepgram and reports the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` settings it sees.

```shell
dg debug network --test-websocket
```

| Option             | Effect                                                   |
| ------------------ | -------------------------------------------------------- |
| `-e`, `--endpoint` | Endpoint to test (default `api.deepgram.com`)            |
| `--test-websocket` | Also test WebSocket connectivity (`wss://`)              |
| `--timeout`        | Timeout in seconds for network operations (default `10`) |
| `--skip-commands`  | Skip system commands such as `openssl` and `curl`        |
| `--save-report`    | Save the full diagnostic report to a file                |
| `-v`, `--verbose`  | Show detailed diagnostic information                     |

`--timeout` defaults to 10 seconds, and `--endpoint` defaults to `api.deepgram.com`. `dg debug network`'s probe requests never carry stored Deepgram credentials: the throwaway HTTP client it builds for each test has no `auth` configured and doesn't read `~/.netrc`, so there's nothing for a `~/.netrc` entry to attach even if one exists for your Deepgram host.

### `dg debug browser`

Starts a local debug server that checks a browser's compatibility with Deepgram services.

```shell
dg debug browser --no-browser
```

| Option          | Effect                                                       |
| --------------- | ------------------------------------------------------------ |
| `-p`, `--port`  | Port for the debug server (default: auto-selected from 3000) |
| `--no-browser`  | Start the server without opening a browser                   |
| `--timeout`     | Seconds to wait for a browser connection (default `60`)      |
| `--save-report` | Save the report to a JSON file                               |

The port is auto-selected starting from 3000, and the session waits 60 seconds for a browser by default.

### `dg debug probe`

Runs a local WebSocket proxy that forwards streaming audio to Deepgram and runs ffprobe on it at intervals. Point your app at `ws://localhost:<port>/v1/listen` in place of `wss://api.deepgram.com/v1/listen`.

```shell
dg debug probe --port 3100
```

| Option                     | Effect                                                      |
| -------------------------- | ----------------------------------------------------------- |
| `-p`, `--port`             | Local proxy port (default: auto-selected from 3100 to 3199) |
| `--probe-interval-bytes`   | Probe every N bytes of audio (default `131072`)             |
| `--probe-interval-seconds` | Probe every N seconds (default `10`)                        |
| `-v`, `--verbose`          | Show per-frame details                                      |

The proxy picks a port from 3100 to 3199 and probes every 131,072 bytes of audio or every 10 seconds.

### `dg ffprobe`

`dg ffprobe` shows which ffprobe binary the CLI uses for audio analysis. `--path` sets a custom binary, stored as `tools.ffprobe_path`, and `--reset` returns to auto-detection.

```shell
# Show the ffprobe status
dg ffprobe
# Use a specific binary
dg ffprobe --path /usr/bin/ffprobe
# Return to auto-detection
dg ffprobe --reset
```

## Get more help

Paste the error and this page into your coding agent. For anything this page does not cover, see [Support](/support) or open an issue on the [CLI issue tracker](https://github.com/deepgram/cli/issues).
