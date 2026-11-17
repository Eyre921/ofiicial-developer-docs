---
title: "Text-to-speech commands"
source: https://developers.deepgram.com/developer-tools/cli/text-to-speech.md
path: developer-tools/cli/text-to-speech
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Text-to-speech commands

> Deepgram CLI text-to-speech with Flux TTS and Aura-2: generate speech from text, a file, or stdin with dg speak, save it, or play it.

## Basic synthesis

```shell
dg speak "Hello from Deepgram" --out-file hello.wav
```

On a terminal, `dg speak` needs `--out-file` (an output file) or `--play`.

## Save to file

```shell
# Default Flux TTS voice, saved as WAV
dg speak "Hello from Deepgram" --out-file hello.wav
# Aura-2 voice, saved as MP3
dg speak "Hello" -m aura-2-luna-en --encoding mp3 --out-file hello.mp3
# Read the text from a file
dg speak -f message.txt --out-file message.wav
```

`-f` (`--file`) reads the text from a file. `--out-file` refuses to overwrite an existing file unless you also pass `--force`. `-o`/`--output` still works in its place but is deprecated and, unlike `--out-file`, always overwrites.

## Play audio

```shell
# Play through your system player
dg speak "Hello" --play
# Save to hello.wav and play it
dg speak "Hello" --play --out-file hello.wav
```

`--play` uses the first system player it finds: `ffplay`, `afplay`, `paplay`, or `aplay`.

* `aplay` plays WAV and raw PCM.
* `paplay` also plays FLAC and Opus.
* For Aura MP3 or AAC on Linux, install `ffplay` (part of `ffmpeg`) or pass `--encoding flac`.
* Aura models return MP3 unless you pass `--encoding`, whether you save or play. Flux TTS plays as WAV.

## Pipe to speaker

```shell
echo "Latest headlines" | dg speak | ffplay -nodisp -autoexit -
```

Under a hard agent signal (see [Agent-Friendly Mode](/developer-tools/cli/getting-started#agent-friendly-mode)), `dg speak` only reads piped stdin when the text argument is literally `-`, and refuses to write audio into a pipe; both cases exit `1` with `"code": "invalid_argument"`. This example is for an interactive terminal; it doesn't work under a hard agent signal such as CI.

## Options

### Model selection

```shell
dg speak "Hello" --model flux-alexis-en --out-file hello.wav
dg speak "Hello" -m aura-2-luna-en --encoding mp3 --out-file hello.mp3
```

`dg speak` defaults to `flux-alexis-en`. Flux TTS models use the Speak v2 WebSocket API and stream raw audio; when the default `linear16` output goes to a file, the CLI wraps it in a WAV container. Use an `aura-*` model for the Speak v1 REST API. Any Flux TTS voice ID works with `-m`.

`dg speak --list-voices` and `dg models --type tts` list the Aura-2 voices. For Flux TTS voices, see [Flux TTS Voices & Languages](/docs/flux-tts/voices).

```shell
# List the Aura-2 voices and their languages
dg speak --list-voices
```

### Output format

`--out-file` sets the file path (`-o`/`--output` still works but is deprecated; see [Save to file](#save-to-file) above), `--encoding` sets the audio encoding, and Aura models also accept `--container`. On Flux TTS models, `--sample-rate` sets the sample rate in Hz, for example `dg speak "Hello" --sample-rate 16000 --out-file hello.wav`.

```shell
dg speak "Hello" --out-file hello.wav
dg speak "Hello" -m aura-2-asteria-en --encoding mp3 --out-file hello.mp3
dg speak "Hello" -m aura-2-asteria-en --encoding linear16 --container wav --out-file hello.wav
```

Aura models accept the encodings `mp3`, `linear16`, `flac`, `mulaw`, `alaw`, `opus`, and `aac`. Flux TTS streams raw audio only: `linear16` (the default), `mulaw`, or `alaw`. `--container` takes `none`, `wav`, or `ogg` and applies to Aura only.

| Option        | Aura (`aura-*`)                                           | Flux TTS (`flux-*`)                   |
| ------------- | --------------------------------------------------------- | ------------------------------------- |
| `--encoding`  | `mp3`, `linear16`, `flac`, `mulaw`, `alaw`, `opus`, `aac` | `linear16` (default), `mulaw`, `alaw` |
| `--container` | `none`, `wav`, `ogg`                                      | Ignored; `linear16` is wrapped in WAV |

### Streaming

Flux TTS streams audio by default, so the WAV stream can go straight to a player:

```shell
dg speak "Hello" | ffplay -loglevel error -nodisp -autoexit -
```

Flux TTS models also support `--speed` from `0.85` to `1.15` in `0.05` increments (the CLI accepts a narrower set than the API's `0.5` to `1.5`) and beta `--expressivity` from `-2` to `2`. `--expressivity` takes integers only and is fixed for the connection.

```shell
dg speak "A little slower" --speed 0.9 --expressivity 1 --out-file slow.wav
```

## Example workflows

### Batch synthesis

```shell
# Synthesize multiple phrases
for text in "Hello" "Goodbye" "Thank you"; do
  dg speak "$text" --out-file "$text.wav"
done
```

### Language selection

Choose a model for the required language. The language is part of the model identifier; `dg speak` doesn't have a `--language` option.

```shell
dg speak "Hola" -m aura-2-selena-es --encoding mp3 --out-file hola.mp3
```
