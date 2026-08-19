---
title: "Deepgram CLI — Getting Started"
source: https://developers.deepgram.com/developer-tools/cli/getting-started.md
path: developer-tools/cli/getting-started
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deepgram CLI — Getting Started

The `dg` CLI gives you full access to Deepgram APIs from your terminal. Transcribe files, stream live audio, synthesize speech, analyze text, and manage your Deepgram account — without writing a single line of code.

## Prerequisites

* Python 3.10 or later
* A Deepgram API key ([get one free](https://console.deepgram.com/signup))

## Quick Start

```shell
# Install
curl -fsSL deepgram.com/install.sh | sh

# Authenticate
dg login

# Transcribe an audio file
dg listen recording.wav

# Synthesize text-to-speech
dg speak "Hello from Deepgram"
```

## Core Workflows

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
dg speak "Hello from Deepgram" -o hello.wav

# Pipe audio to your speaker
echo "Latest headlines" | dg speak | ffplay -nodisp -autoexit -
```

### Text intelligence

```shell
# Analyze a document
dg read report.txt --topics --sentiment --summarize

# Summarize piped text
cat transcript.txt | dg read --summarize
```

### Account management

```shell
# List your projects
dg projects --list

# Create an API key
dg keys --create --comment "ci-runner"

# Check your usage
dg usage
```

Account commands are flag-based. Run `dg keys --help` or `dg projects --help` for the full set.

## Output Formats

The CLI defaults to human-readable output in the terminal. Use `-o` or `--output` to switch formats:

```shell
dg -o json listen audio.mp3   # Structured JSON
dg -o yaml listen audio.mp3   # YAML
dg -o table listen audio.mp3  # ASCII table
dg -o csv listen audio.mp3    # CSV
```

`-o` belongs to `dg` itself, so it goes before the subcommand name. After the subcommand it fails to parse — `dg listen audio.mp3 -o json` exits `1` with `Error: No such option '-o'.` On `dg speak` the collision is quieter: there, a bare `-o` is the output file path, not a format.

[Agent-friendly mode](#agent-friendly-mode) selects JSON on its own, without `-o`. A piped stdout alone does not trigger it.

Usage errors, cancellation messages, and progress output go to stderr rather than stdout, so redirecting stderr leaves stdout carrying the payload:

```shell
dg -o json listen audio.mp3 2>/dev/null > transcript.json
```

Some command-level errors still print to stdout — an authentication failure is the common one — so check the exit code rather than assuming stdout parses.

## Exit Codes

Every command reports its outcome through the exit code, so scripts and CI steps can branch on it:

| Code | Meaning                                                                              |
| ---- | ------------------------------------------------------------------------------------ |
| `0`  | Success                                                                              |
| `1`  | Error, including crashes and usage errors such as an unknown command or invalid flag |
| `2`  | User interrupt: Ctrl-C, or Ctrl-D at a prompt                                        |

```shell
if dg -o json listen audio.mp3 > transcript.json; then
  echo "transcribed"
else
  echo "failed with code $?" >&2
fi
```

Exit codes are enforced as of CLI `0.3.0`. Earlier versions exited `0` regardless of outcome, so a pipeline that ignored the exit code may begin surfacing failures it previously swallowed. No command that succeeds changes its exit code.

## Agent-Friendly Mode

The CLI auto-detects AI agent environments (Claude Code, Aider, OpenAI Codex, Gemini) and adjusts its behavior:

* Disables interactive prompts
* Defaults to JSON output
* Routes status messages and warnings to stderr

To force the mode on:

```shell
CI=true dg listen audio.mp3
dg listen audio.mp3 --non-interactive
```

`--agent-friendly` does something different on a subcommand: it prints that command's parameter documentation as JSON and exits without running it.

```shell
dg listen --agent-friendly
```

## Next Steps

* [Install the CLI](/developer-tools/cli/installation) — More installation methods including pip, pipx, and Homebrew
* [Authenticate](/developer-tools/cli/authentication) — Learn about authentication options
* [Speech-to-Text](/developer-tools/cli/speech-to-text) — Full transcription reference
* [Text-to-Speech](/developer-tools/cli/text-to-speech) — Full TTS reference
