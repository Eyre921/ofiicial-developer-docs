---
title: "Text-to-Speech Commands"
source: https://developers.deepgram.com/developer-tools/cli/text-to-speech.md
path: developer-tools/cli/text-to-speech
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Text-to-Speech Commands

## Basic Synthesis

```shell
dg speak "Hello from Deepgram"
```

## Save to File

```shell
dg speak "Hello from Deepgram" -o hello.wav
dg speak "Hello" -o hello.mp3
```

## Pipe to Speaker

```shell
echo "Latest headlines" | dg speak | ffplay -nodisp -autoexit -
```

## Options

### Voice Selection

```shell
dg speak "Hello" --voice aura-2-luna-en
dg speak "Hola" --voice aura-2-asteria-en
```

List available voices:

```shell
dg speak --list-voices
```

### Output Format

```shell
dg speak "Hello" -o wav    # WAV (default)
dg speak "Hello" -o mp3    # MP3
dg speak "Hello" -o flac   # FLAC
```

### Streaming

For low-latency streaming, use the WebSocket mode:

```shell
dg speak "Hello" --stream
```

## Example Workflows

### Batch Synthesis

```shell
# Synthesize multiple phrases
for text in "Hello" "Goodbye" "Thank you"; do
  dg speak "$text" -o "$text.wav"
done
```

### Language Selection

```shell
dg speak "Bonjour" --language fr-FR
dg speak "Guten Tag" --language de-DE
```
