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
dg listen audio.mp3 -o json | jq '.results.channels[0].alternatives[0].transcript'
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
dg projects list

# Create an API key
dg keys create "ci-runner"

# Check your usage
dg usage
```

## Output Formats

The CLI defaults to human-readable output in the terminal. Use `-o` or `--output` to switch formats:

```shell
dg listen audio.mp3 -o json   # Structured JSON
dg listen audio.mp3 -o yaml   # YAML
dg listen audio.mp3 -o table  # ASCII table
dg listen audio.mp3 -o csv    # CSV
```

When stdout is a pipe, the CLI automatically switches to JSON.

## Agent-Friendly Mode

The CLI auto-detects AI agent environments (Claude Code, Aider, OpenAI Codex, Gemini) and adjusts its behavior:

* Disables interactive prompts
* Routes status messages to stderr
* Defaults to JSON output

To explicitly enable agent-friendly mode:

```shell
dg listen audio.mp3 --agent-friendly
```

To get machine-readable parameter documentation:

```shell
dg listen --agent-friendly
```

## Next Steps

* [Install the CLI](/developer-tools/cli/installation) — More installation methods including pip, pipx, and Homebrew
* [Authenticate](/developer-tools/cli/authentication) — Learn about authentication options
* [Speech-to-Text](/developer-tools/cli/speech-to-text) — Full transcription reference
* [Text-to-Speech](/developer-tools/cli/text-to-speech) — Full TTS reference
