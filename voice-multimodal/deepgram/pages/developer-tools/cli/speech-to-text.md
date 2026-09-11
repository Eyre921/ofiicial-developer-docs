---
title: "Speech-to-Text Commands"
source: https://developers.deepgram.com/developer-tools/cli/speech-to-text.md
path: developer-tools/cli/speech-to-text
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Speech-to-Text Commands

## Transcribe a File

```shell
dg listen audio.mp3
```

## Transcribe a URL

```shell
dg listen https://example.com/audio.mp3
```

## Live Microphone

Stream from your default microphone:

```shell
dg listen --mic
```

Press `Ctrl+C` to stop.

## stdin / Piped Input

Pipe audio from another tool:

```shell
ffmpeg -i video.mp4 -f s16le -ar 16000 -ac 1 - | dg listen --encoding linear16
```

## Options

### Output Format

```shell
dg -o json listen audio.mp3    # JSON
dg -o yaml listen audio.mp3    # YAML
dg -o table listen audio.mp3   # Formatted terminal table
dg -o csv listen audio.mp3     # CSV
```

`-o` belongs to `dg` itself, so it goes before the subcommand name. Without it, `dg listen` prints the plain-text transcript.

### Model Selection

```shell
dg listen audio.mp3 --model nova-3    # Default model
dg listen audio.mp3 --model nova-2    # General purpose
dg listen audio.mp3 --model whisper   # Whisper model
```

### Features

```shell
dg listen audio.mp3 --diarize          # Speaker diarization
dg listen audio.mp3 --smart-format     # Smart formatting
dg listen audio.mp3 --summarize        # Generate summary
dg listen audio.mp3 --topics           # Topic detection
dg listen audio.mp3 --sentiment        # Sentiment analysis
```

### Subtitles

```shell
dg listen audio.mp3 --webvtt           # WebVTT captions
dg listen audio.mp3 --srt              # SRT subtitles
```

### Language

```shell
dg listen audio.mp3 --language en-US   # English (US)
dg listen audio.mp3 --language es     # Spanish
dg listen audio.mp3 --language de     # German
```

### Boolean Options

Boolean options do not take a value:

```shell
dg listen audio.mp3 --punctuate
dg listen --mic --interim
```

Run `dg listen --help` for the complete set of supported CLI options. The command does not forward arbitrary API parameters.

## Command Alias

`dg transcribe` is a deprecated alias for `dg listen`:

```shell
dg transcribe audio.mp3
```
