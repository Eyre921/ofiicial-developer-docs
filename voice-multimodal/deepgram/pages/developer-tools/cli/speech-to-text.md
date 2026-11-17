---
title: "Speech-to-text commands"
source: https://developers.deepgram.com/developer-tools/cli/speech-to-text.md
path: developer-tools/cli/speech-to-text
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Speech-to-text commands

> Deepgram CLI speech-to-text with Nova-3: transcribe audio files, URLs, the microphone, and stdin with dg listen.

## Transcribe a file

```shell
dg listen audio.mp3
```

## Transcribe a URL

```shell
dg listen https://example.com/audio.mp3
```

## Live microphone

Stream from your default microphone:

```shell
dg listen --mic
```

Press `Ctrl+C` to stop. On Linux with a pip, pipx, or uv install, `--mic` needs the PortAudio library; see [Installation](/developer-tools/cli/installation).

## stdin / Piped Input

Pipe audio from another tool:

```shell
ffmpeg -i video.mp4 -f s16le -ar 16000 -ac 1 - | dg listen --encoding linear16
```

`dg listen -` reads raw audio from stdin. `dg listen` with no source opens an interactive source picker.

## Options

### Output format

```shell
# Full API response as JSON, with -o before the subcommand
dg -o json listen audio.mp3
# The same output, with -o after the subcommand
dg listen audio.mp3 -o json
# YAML, same body as -o json
dg listen audio.mp3 -o yaml
# Transcript alone, no other output (listen-only; must go after the subcommand)
dg listen audio.mp3 -o text
```

Without `-o`, `dg listen` on a terminal prints a summary table and the transcript. `-o json` and `-o yaml` print the server's prerecorded response body as sent, formatted as JSON or YAML; `-o table` and `-o csv` are no-ops on `dg listen` and print that same default summary instead. If a script expects the older, SDK-parsed JSON shape (indented, with `datetime`-style timestamps), set `DEEPCTL_LISTEN_JSON=sdk` to restore it.

`dg listen` also accepts a local `text` format for the transcript alone. It only works after the subcommand (`dg listen audio.mp3 -o text`); the global `-o text` placed before the subcommand fails, because `text` isn't a valid value for `--output` at the root level.

`-o` works before the subcommand (`dg -o json read ...`) or after it on most commands (`dg read ... -o json`). On `dg speak`, `-o`/`--output` after the subcommand still sets the output file path but is deprecated; use `--out-file` instead. On `dg plugin` and `dg skills` subcommands, put `-o` before the subcommand.

In an AI-agent session, a prerecorded result over 64 KiB saves to a file under `~/.deepctl/results/` instead of printing, with a summary on stdout; pass `--full-output` to print the full payload anyway.

`--timeout` sets how many seconds `dg listen` waits at each step (connecting, sending, the response) for a file or URL source, not a cap on the whole run. Default `300`, minimum `1`; it doesn't apply to `--mic` or live stdin.

### Model Selection

`nova-3` is the default and the model to use for new builds:

```shell
# Default model
dg listen audio.mp3 --model nova-3
```

`--model` (`-m`) also accepts `nova-2` and `whisper` for workloads that already depend on them. `dg models --type stt` lists the speech-to-text models your key can use; see [Account Management](/developer-tools/cli/account-management).

#### Flux STT

```shell
# Flux STT on the microphone (live audio only)
dg listen --mic --model flux-general-en
# Flux STT on raw audio piped through stdin
ffmpeg -i call.wav -f s16le -ar 16000 -ac 1 - | dg listen --model flux-general-en --encoding linear16
```

* Flux STT runs on live audio (`--mic` or stdin). A file or URL exits `1` with `Flux STT (flux-general-en) is streaming-only and cannot transcribe a file or URL.` followed by `Use a live source (--mic, stdin, or '-'), or pick a v1 model (e.g. nova-3) for pre-recorded audio.`
* `--diarize` is ignored with a warning.
* `--channels` must be `1`.
* `--redact` accepts only `numbers` and `aggressive_numbers`.

### Features

```shell
# Speaker diarization; text output labels speakers as [Speaker 0], [Speaker 1], and so on
dg listen audio.mp3 --diarize
# Generate summary
dg listen audio.mp3 --summarize
# Topic detection
dg listen audio.mp3 --topics
# Sentiment analysis
dg listen audio.mp3 --sentiment
# Redact numbers and convert spoken numbers to digits
dg listen call.wav --redact numbers --numerals
# Save the transcript to a file
dg listen audio.mp3 --save-to transcript.txt
```

`--smart-format` and `--punctuate` are on by default. `--sentiment`, `--topics`, and `--summarize` apply to pre-recorded audio only; `--interim` applies to live streaming only.

| Flag               | Default    | Applies to             | Effect                                                                                                     |
| ------------------ | ---------- | ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| `--redact`         | none       | Files and live streams | Redact sensitive content, for example `pci`, `ssn`, or `numbers`; repeatable on v1 models such as `nova-3` |
| `--numerals`       | off        | Files and live streams | Convert spoken numbers to digits                                                                           |
| `--save-to`, `-s`  | none       | All sources            | Save the transcript, or the caption file, to a path                                                        |
| `--sample-rate`    | `16000`    | Raw stdin              | Sample rate in Hz                                                                                          |
| `--channels`       | `1`        | Raw stdin              | Number of audio channels                                                                                   |
| `--encoding`       | `linear16` | Raw stdin              | Raw audio encoding, for example `linear16`, `mulaw`, or `opus`                                             |
| `--probe`          | off        | Local files only       | Run ffprobe analysis before transcribing                                                                   |
| `--no-validate`    | off        | All sources            | Skip source validation (faster, with less helpful errors)                                                  |
| `--language`, `-l` | `en-US`    | All sources            | Language code                                                                                              |
| `--model`, `-m`    | `nova-3`   | All sources            | Deepgram model                                                                                             |
| `--interim`        | off        | Live streams only      | Show partial results as they arrive                                                                        |

For raw stdin, `--sample-rate` defaults to `16000` Hz and `--channels` defaults to `1`. `--encoding` isn't auto-detected: omitting it assumes `linear16` and prints `WARN: No --encoding specified — assuming linear16. Pass --encoding to suppress this warning.` on stderr; pass `--encoding` explicitly for `mulaw`, `opus`, or any other non-Linear16 stream. `--language` defaults to `en-US` and `--model` to `nova-3`.

### Subtitles

```shell
# WebVTT captions for a file or URL, saved to keynote.vtt
dg listen keynote.mp3 --webvtt --save-to keynote.vtt
# SRT captions with speaker labels
dg listen interview.mp3 --srt --diarize --save-to interview.srt
```

`--webvtt` and `--srt` work on their own; `--diarize` is optional and only adds speaker labels to the caption entries.

* `--webvtt` and `--srt` are mutually exclusive.
* WebVTT output carries its metadata in a `NOTE` block.
* In live mode (`--mic` or stdin), caption entries print as they arrive:

```shell
# Live WebVTT captions from the microphone
dg listen --mic --webvtt
# SRT captions from a video's audio track through stdin
ffmpeg -i video.mp4 -f s16le -ar 16000 -ac 1 - | dg listen --encoding linear16 --srt
```

### Language

```shell
# English (US)
dg listen audio.mp3 --language en-US
# Spanish
dg listen audio.mp3 --language es
# German
dg listen audio.mp3 --language de
```

### Boolean options

Boolean options don't take a value:

```shell
dg listen --mic --interim
```

Run `dg listen --help` for the complete set of supported CLI options. The command doesn't forward arbitrary API parameters.

## Command alias

`dg transcribe` is a deprecated alias for `dg listen`:

```shell
dg transcribe audio.mp3
```
