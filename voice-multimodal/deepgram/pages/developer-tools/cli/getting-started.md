---
title: "Getting started"
source: https://developers.deepgram.com/developer-tools/cli/getting-started.md
path: developer-tools/cli/getting-started
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Getting started

By the end of this guide you'll have `dg` installed and logged in, a transcript of one audio file printed in your terminal, one WAV file of generated speech on disk, and a starter app scaffolded by `dg init` with your API key in its `.env`.

The `dg` CLI transcribes files, streams live audio, synthesizes speech, analyzes text, and manages your Deepgram account from the terminal.

The Deepgram CLI command is `dg`; the PyPI package that installs it is `deepctl`, and it needs Python 3.10 or later. Install it with `curl -fsSL https://deepgram.com/install.sh | sh`, `brew install deepgram/tap/deepgram`, or `pip install deepctl` (also `pipx install deepctl`, `uv tool install deepctl`, and `npm install -g @deepgram/cli`). `dg listen` defaults to Nova-3 (`nova-3`); `--model flux-general-en` selects Flux STT on streaming input (`--mic` or stdin). `dg speak` defaults to the Flux TTS voice `flux-alexis-en`. On a standard install, `dg --help` lists 24 commands; installed plugins add their own. For voice agents, use the Voice Agent API or scaffold a starter with `dg init --list --search voice-agent`.

The Deepgram CLI command is `dg` (PyPI package `deepctl`, Python 3.10+). `dg mcp` is a local stdio bridge to Deepgram's docs-search MCP server and exposes one tool, `search_deepgram_knowledge_sources`. The Voice Agent API has no `dg` command.

## Prerequisites

* Python 3.10 or later
* A Deepgram API key ([get one free](https://console.deepgram.com/signup))

## Quick start

```shell
# Install
curl -fsSL https://deepgram.com/install.sh | sh

# Authenticate
dg login

# Transcribe an audio file
dg listen recording.wav

# Synthesize text-to-speech to a file
dg speak "Hello from Deepgram" --out-file hello.wav
```

With `recording.wav` holding the spacewalk sample (`https://dpgr.am/spacewalk.wav`), `dg listen` prints a summary table and the transcript, and `dg speak` reports the saved file. Both exit `0`; byte counts and timings vary per run:

```text
  Source      recording.wav
  Model       general-nova-3
  Version     2025-07-31.0
  Duration    0:25.93
  Channels    1

Yeah. As as much as, it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal. And, I think if it signifies anything, it is, to honor the the women who came before us who, were skilled and qualified, and didn't get the same opportunities that we have today.

Streaming flux-alexis-en — first audio 540 ms
  received 22 KB
  received 41 KB
  received 60 KB
Audio saved to hello.wav (69,164 bytes — first audio 540 ms, 1.4s total)
```

## Scaffold a starter app

`dg init` clones a template from the gallery at [templates.dx.deepgram.com](https://templates.dx.deepgram.com), writes your `DEEPGRAM_API_KEY` into the app's `.env`, and can run its setup and start steps. The templates are finished apps from the [deepgram-starters](https://github.com/deepgram-starters) organization. `dg init` needs `git`, `node`, `npm`, `make`, and `curl` on your PATH; if any is absent, it prints `Missing required tools:` with one line per missing tool and exits `1` before cloning.

```shell
# Open the interactive picker to search and choose a template
dg init

# List every template with its language, framework, and use case
dg init --list

# Filter the list; matches name, title, description, language, framework, and category
dg init --list --search voice-agent

# Clone node-transcription into ./node-transcription; on a terminal, prompts to run setup and start
dg init node-transcription

# Clone into a chosen directory and skip setup; the CLI prints the setup command to run later
dg init node-transcription --dir ./my-app --no-install
```

On a terminal, `dg init` prompts you to run the template's setup (`make init`) and start it; answer the prompts, or pass `--no-install` and `--no-start` to skip them without being asked. Outside a terminal, including any AI-agent session, nothing can answer that prompt, so `dg init` needs an explicit flag before it runs setup or starts the app:

* `--yes` confirms setup only. It's the only way to do this inside an AI-agent session.
* `--install` confirms setup outside an AI-agent session (use `--yes` inside one).
* `--start` confirms the start step; it doesn't run on its own. Combine it with `--yes` or `--install` to both set up and start in one command: `dg init node-transcription --yes --start`.
* Without one of these, `dg init` exits `1` with `confirmation_required` instead of running setup or starting the app.

Other notes:

* `dg init --list` prints the full set of available slugs, including `fastapi-transcription`, `node-live-transcription`, and `node-voice-agent`.
* `--dir` sets the target directory.
* Re-running `dg init` on a clone it already started resumes from where that attempt left off.
* When setup is skipped, the CLI ends with `To set up:  cd <dir> && make init`.
* Without a GitHub SSH key, the `make init` that `dg init` runs fails with `Host key verification failed` on starters whose `.gitmodules` use SSH URLs, `frontend/` and `contracts/` stay empty, and `dg init` still prints `Done! ... is ready` and exits `0`. Finish the checkout with `git -c url."https://github.com/".insteadOf="git@github.com:" submodule update --init --recursive`, then run `make init` again.
* An unknown slug exits `1` with `Template not found: <slug>`.
* Missing required tools exits `1` before cloning, for example `{"status": "error", "message": "Missing tools: node, npm, make", ...}`.

## Core workflows

### Transcribe audio

```shell
# Transcribe a local file
dg listen audio.mp3

# Transcribe from a URL
dg listen https://example.com/audio.mp3

# Stream from your microphone
dg listen --mic

# Pipe transcript to another tool
dg -o json listen audio.mp3 | jq '.results.channels[0].alternatives[0].transcript'
```

### Text-to-speech

```shell
# Generate speech and save to file
dg speak "Hello from Deepgram" --out-file hello.wav

# Pipe audio to your speaker
echo "Latest headlines" | dg speak | ffplay -nodisp -autoexit -
```

`-o`/`--output` still works in place of `--out-file` on `dg speak`, but it's deprecated and, unlike `--out-file`, overwrites an existing file without asking. Under a hard agent signal (see [Agent-Friendly Mode](#agent-friendly-mode) below), `dg speak` only reads piped stdin when the text argument is literally `-`, and refuses to write audio into a pipe; both cases exit `1` with `"code": "invalid_argument"`. The pipe-to-`ffplay` example above is for an interactive terminal; it doesn't work under a hard agent signal.

### Text intelligence

```shell
# Analyze a text file
dg read --file report.txt --topics --sentiment --summarize

# Summarize piped text
cat transcript.txt | dg read --summarize
```

### Account management

```shell
# List your projects
dg projects --list

# Set the project that key, member, usage, and billing commands act on
dg projects --set-default <project-id>

# Create an API key
dg keys --create --comment "ci-runner"

# Check your usage
dg usage
```

Key, member, usage, and billing commands act on one project: set it with `dg projects --set-default <project-id>` or export `DEEPGRAM_PROJECT_ID`. Without one they exit `1` with `Project ID is required for this command`. Account commands take the action as a flag. Run `dg keys --help` or `dg projects --help` for the full set.

## Output formats

Output defaults to human-readable text. `-o` (`--output`) takes `json`, `yaml`, `table`, or `csv`:

```shell
# Structured JSON
dg -o json read --file report.txt
# YAML
dg -o yaml read --file report.txt
# Formatted terminal table
dg -o table read --file report.txt
# CSV
dg -o csv read --file report.txt
```

`dg listen` is a partial exception: it prints a summary table and the transcript by default. `-o json` and `-o yaml` print the server's prerecorded response body as sent, formatted as JSON or YAML; `-o table` and `-o csv` are no-ops on `dg listen` and print the same default summary instead. If you have a script that expects the older, SDK-parsed JSON shape (indented, with `datetime`-style timestamps), set `DEEPCTL_LISTEN_JSON=sdk` to restore it.

`dg listen` also takes a local `text` format for the transcript alone, and it goes after the subcommand: `dg listen audio.mp3 -o text`. It isn't a valid value for the global `-o` placed before the subcommand (`dg -o text listen audio.mp3` fails with `Invalid value for '--output' / '-o'`).

`-o` works before the subcommand (`dg -o json read ...`) or after it on most commands (`dg read ... -o json`). On `dg speak`, `-o`/`--output` after the subcommand still sets the output file path but is deprecated; use `--out-file` instead (see [Text-to-speech](/developer-tools/cli/text-to-speech)). On `dg plugin` and `dg skills` subcommands, put `-o` before the subcommand. The same placement rule covers `-q` (`--quiet`) and `-v` (`--verbose`). [Configuration & Environment](/developer-tools/cli/configuration) lists every global option.

In an AI-agent session, a prerecorded `dg listen` result over 64 KiB saves to a file under `~/.deepctl/results/` instead of printing, with a summary on stdout; pass `--full-output` to print the full payload to stdout anyway.

`dg listen` also takes `--timeout` for files and URLs (not the microphone or live stdin): seconds to wait at each step (connecting, sending, the response) before giving up, not a cap on the whole run. Default `300`, minimum `1`.

Agent-Friendly Mode, described below, selects JSON without `-o`. A piped stdout alone does not trigger it.

For `dg -o json listen`, parse errors and progress go to stderr, so redirecting stderr leaves the payload on stdout:

```shell
dg -o json listen audio.mp3 2>/dev/null > transcript.json
```

On most failures, `-o json` writes a JSON object to stdout and the command exits `1`. Some errors write only to stderr and leave stdout empty, such as a missing project ID. The JSON object takes one of three shapes:

* `{"status": "error", "message": "..."}` for most in-command errors, such as a missing input file.
* `{"error": "...", "status": "error", "code": "...", "hint": "...", "next_step": ..., "schema_version": 1, "details": {...}}` for most failures before the command runs or that the CLI can diagnose, such as an invalid API key or a bad argument. `code` is a short, machine-readable reason (for example `auth_invalid` or `invalid_argument`); `hint` and `next_step` suggest a fix; `schema_version` marks the shape so scripts can tell it apart from the older one below.
* The older, bare `{"error": "...", "status": "error"}` shape, with no `code`, still appears for some failures, though most cases that used to return it now return the coded shape above instead.

Branch on the exit code first, then read the reason with `.message // .error` (for example, `jq -r '.message // .error'`); that read degrades safely across all three shapes. Read `.code` too if a script needs to match on a specific failure rather than its message text. Treat empty stdout with a nonzero exit code as an error whose reason is on stderr.

## Exit codes

Most command and usage outcomes use these exit codes, so scripts and CI steps can branch on them:

| Code | Meaning                                                                        |
| ---- | ------------------------------------------------------------------------------ |
| `0`  | Success                                                                        |
| `1`  | Command, execution, or usage error, such as an unknown command or invalid flag |
| `2`  | Cancelled: Ctrl-C, Ctrl-D at a prompt, or a declined confirmation              |

`dg plugin remove`, `dg update`, and `dg skills install` return `2` on cancel and `1` on failure.

```shell
# Branch on the exit code: 0 means transcript.json holds the payload
if dg -o json listen audio.mp3 > transcript.json; then
  echo "transcribed"
else
  # Any non-zero code is a command, usage, or cancellation failure
  echo "failed with code $?" >&2
fi
```

> **Note**
>
> Exit codes are enforced as of CLI `0.3.0`. Earlier versions exited `0` regardless of outcome, so a pipeline that ignored the exit code may start surfacing failures it swallowed before. `dg listen --mic`, `dg listen` reading live audio from stdin, and `dg mcp` handle Ctrl-C themselves and exit `0`, so an interrupt exit code is unreliable for those three cases. One more exception: when `dg login` or `dg init` needs a confirmation it can't get (no terminal, and no `-f`/`--yes`/`--install`), it exits `1` with `confirmation_required` rather than the exit `2` a declined confirmation would otherwise get.

## Agent-Friendly Mode

When the CLI detects an AI agent or non-interactive environment, it:

* Disables interactive prompts
* Defaults to JSON output

It switches on for any one of these hard signals:

* The environment variables `CLAUDECODE`, `CLAUDE_CODE_ENTRYPOINT`, `CODEX_SANDBOX`, or `CODEX_SANDBOX_NETWORK_DISABLED`, `OR_APP_NAME=Aider`, an `OR_SITE_URL` containing `aider`, or `CI=true` or `CI=1`
* The `--non-interactive` or `--agent-friendly` flag

It also switches on when any 3 of these soft signals hold: stdin is not a TTY, stdout is not a TTY, `TERM` is unset or `dumb`, `NO_COLOR` is set. A cron job, systemd unit, or `docker run` without `-t` can meet three soft signals and switch to JSON. A piped stdout alone does not trigger it.

This list isn't exhaustive. For the complete, current signal table (every coding agent and CI system the CLI recognizes, including OpenCode, and the source each check comes from), run `dg help agent-mode` rather than relying on a hand-copied list.

To force the mode on:

```shell
# Either form disables prompts and defaults to JSON output
CI=true dg listen audio.mp3
dg listen audio.mp3 --non-interactive
```

On a subcommand, `--agent-friendly` prints that command's parameter documentation as JSON and exits without running it. The JSON carries the fields `command`, `description`, `agent_hints`, `examples`, `requires_auth`, `requires_project`, `non_interactive`, `output_formats`, and `parameters`.

```shell
dg listen --agent-friendly
```

## Command reference

On a standard install, `dg --help` lists 24 commands. `dg transcribe` is a hidden alias for `dg listen`.

| Command         | What it does                                                                  | Page                                                          |
| --------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `dg login`      | Log in with the browser or store an API key                                   | [Authentication](/developer-tools/cli/authentication)         |
| `dg logout`     | Clear stored credentials                                                      | [Authentication](/developer-tools/cli/authentication)         |
| `dg profiles`   | List, show, and switch authentication profiles                                | [Authentication](/developer-tools/cli/authentication)         |
| `dg whoami`     | Show the active profile, masked key, and credential source                    | [Authentication](/developer-tools/cli/authentication)         |
| `dg update`     | Check for and install CLI updates                                             | [Installation](/developer-tools/cli/installation)             |
| `dg listen`     | Transcribe files, URLs, the microphone, and stdin                             | [Speech-to-Text](/developer-tools/cli/speech-to-text)         |
| `dg transcribe` | Alias for `dg listen`                                                         | [Speech-to-Text](/developer-tools/cli/speech-to-text)         |
| `dg speak`      | Generate speech with Flux TTS or Aura-2                                       | [Text-to-Speech](/developer-tools/cli/text-to-speech)         |
| `dg read`       | Summarize text and detect sentiment, topics, and intents                      | [Text Intelligence](/developer-tools/cli/text-intelligence)   |
| `dg projects`   | List, show, create, and set the default project                               | [Account Management](/developer-tools/cli/account-management) |
| `dg keys`       | List, show, create, and delete API keys                                       | [Account Management](/developer-tools/cli/account-management) |
| `dg members`    | List, invite, and remove project members                                      | [Account Management](/developer-tools/cli/account-management) |
| `dg usage`      | Show usage for a date range                                                   | [Account Management](/developer-tools/cli/account-management) |
| `dg billing`    | Show balances and billing breakdowns                                          | [Account Management](/developer-tools/cli/account-management) |
| `dg requests`   | Show request history                                                          | [Account Management](/developer-tools/cli/account-management) |
| `dg models`     | List speech-to-text and text-to-speech models                                 | [Account Management](/developer-tools/cli/account-management) |
| `dg api`        | Call any Deepgram API endpoint with your credentials                          | [Account Management](/developer-tools/cli/account-management) |
| `dg mcp`        | Run a local bridge to the Deepgram docs MCP server                            | [MCP Server](/developer-tools/cli/mcp-server)                 |
| `dg skills`     | Install, update, and remove Deepgram skills for coding agents                 | [Skills](/developer-tools/cli/skills)                         |
| `dg completion` | Generate or install shell completion                                          | [Shell Completion](/developer-tools/cli/shell-completion)     |
| `dg plugin`     | Install, list, update, and remove plugins                                     | [Plugin System](/developer-tools/cli/plugins)                 |
| `dg debug`      | Diagnose audio, network, browser, and streaming issues                        | [Troubleshooting](/developer-tools/cli/troubleshooting)       |
| `dg ffprobe`    | Show or set the ffprobe path                                                  | [Troubleshooting](/developer-tools/cli/troubleshooting)       |
| `dg init`       | Scaffold a starter app                                                        | This page, under Scaffold a Starter App                       |
| `dg help`       | Show extended help, including `dg help agent-mode`'s AI-agent detection table | This page, under Agent-Friendly Mode                          |

## What the CLI covers

* [Installation](/developer-tools/cli/installation): install the Deepgram CLI on macOS, Linux, and Windows, and keep it updated
* [Authentication](/developer-tools/cli/authentication): log in, store keys, and manage profiles
* [Configuration & Environment](/developer-tools/cli/configuration): global options, config files, environment variables, and precedence
* [Speech-to-Text](/developer-tools/cli/speech-to-text): transcribe audio files, URLs, microphone, and stdin
* [Text-to-Speech](/developer-tools/cli/text-to-speech): synthesize speech with Flux TTS and Aura-2
* [Text Intelligence](/developer-tools/cli/text-intelligence): analyze text for sentiment, topics, summaries, and intents
* [Account Management](/developer-tools/cli/account-management): manage projects, API keys, team members, usage, and request history
* [MCP Server](/developer-tools/cli/mcp-server): run `dg mcp` as a local bridge to the docs MCP server
* [Skills](/developer-tools/cli/skills): install the Deepgram skills into your coding agents
* [Shell Completion](/developer-tools/cli/shell-completion): enable tab completion for bash, zsh, and fish
* [Plugin System](/developer-tools/cli/plugins): extend the CLI with plugins, and build and publish your own
* [Troubleshooting](/developer-tools/cli/troubleshooting): error messages and the `dg debug` diagnostics

## Next steps

* [Install the CLI](/developer-tools/cli/installation): more installation methods, including pip, pipx, uv, and Homebrew
* [Authenticate](/developer-tools/cli/authentication): browser login, API keys, and profiles
* [Speech-to-Text](/developer-tools/cli/speech-to-text): full transcription reference
* [Text-to-Speech](/developer-tools/cli/text-to-speech): full text-to-speech reference
