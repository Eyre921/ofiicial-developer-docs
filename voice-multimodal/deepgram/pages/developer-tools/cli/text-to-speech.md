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
dg speak "Hello from Deepgram" -o hello.wav
```

## Save to File

```shell
dg speak "Hello from Deepgram" -o hello.wav
dg speak "Hello" -m aura-2-luna-en --encoding mp3 -o hello.mp3
```

## Pipe to Speaker

```shell
echo "Latest headlines" | dg speak | ffplay -nodisp -autoexit -
```

## Options

### Model Selection

```shell
dg speak "Hello" --model flux-alexis-en -o hello.wav
dg speak "Hello" -m aura-2-luna-en --encoding mp3 -o hello.mp3
```

`dg speak` defaults to `flux-alexis-en`. Flux TTS uses the Speak v2 WebSocket API and streams raw audio; when writing the default `linear16` output to a file, the CLI wraps it in a WAV container. Use an `aura-*` model for the Speak v1 REST API.

List available TTS models:

```shell
dg models --type tts
```

### Output Format

`-o` or `--output` sets the output file path. To select audio encoding, use `--encoding`; Aura models also support `--container`.

```shell
dg speak "Hello" -o hello.wav
dg speak "Hello" -m aura-2-asteria-en --encoding mp3 -o hello.mp3
dg speak "Hello" -m aura-2-asteria-en --encoding linear16 --container wav -o hello.wav
```

### Streaming

Flux TTS streams audio by default. Pipe the WAV stream to a player instead of writing it to a file:

```shell
dg speak "Hello" | ffplay -loglevel error -nodisp -autoexit -
```

Flux models also support `--speed` from `0.85` to `1.15` in `0.05` increments and beta `--expressivity` from `-2` to `2`:

```shell
dg speak "A little slower" --speed 0.9 --expressivity 1 -o slow.wav
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

Choose a model for the required language. The language is part of the model identifier; `dg speak` does not have a `--language` option.

```shell
dg speak "Hola" -m aura-2-selena-es --encoding mp3 -o hola.mp3
```
