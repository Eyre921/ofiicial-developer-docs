---
title: "Audio"
source: https://openrouter.ai/docs/guides/overview/multimodal/audio.md
path: docs/guides/overview/multimodal/audio
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio

> How to send and receive audio with OpenRouter models

OpenRouter supports both sending audio files to compatible models and receiving audio responses via the API. This guide covers how to work with audio inputs and outputs.

## Audio Inputs

Send audio files to compatible models for transcription, analysis, and processing. Audio input requests use the `/api/v1/chat/completions` API with the `input_audio` content type. Audio files must be base64-encoded and include the format specification.

**Note**: Audio files must be **base64-encoded** - direct URLs are not supported for audio content.

You can search for models that support audio input by filtering to audio input modality on our [Models page](https://openrouter.ai/docs/guides/overview/models.md).

### Sending Audio Files

Here's how to send an audio file for processing:

### Supported Audio Input Formats

Supported audio formats vary by provider. Common formats include:

* `wav` - WAV audio
* `mp3` - MP3 audio
* `aiff` - AIFF audio
* `aac` - AAC audio
* `ogg` - OGG Vorbis audio
* `flac` - FLAC audio
* `m4a` - M4A audio
* `pcm16` - PCM16 audio
* `pcm24` - PCM24 audio

**Note:** Check your model's documentation to confirm which audio formats it supports. Not all models support all formats.

## Audio Output

OpenRouter supports receiving audio responses from models that have audio output capabilities. To request audio output, include the `modalities` and `audio` parameters in your request.

You can search for models that support audio output by filtering to audio output modality on our [Models page](https://openrouter.ai/docs/guides/overview/models.md).

### Requesting Audio Output

To receive audio output, set `modalities` to `["text", "audio"]` and provide the `audio` configuration with your desired voice and format:

### Streaming Chunk Format

Audio output requires streaming (`stream: true`). Audio data and transcript are delivered incrementally via the `delta.audio` field in each chunk:

```json lines theme={null}
{
  "choices": [
    {
      "delta": {
        "audio": {
          "data": "<base64-encoded audio chunk>",
          "transcript": "Hello"
        }
      }
    }
  ]
}
```

### Audio Configuration Options

The `audio` parameter accepts the following options:

| Option | Description |
| - | - |
| `voice` | The voice to use for audio generation (e.g., `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`). Available voices vary by model. |
| `format` | The audio format for the output (e.g., `wav`, `mp3`, `flac`, `opus`, `pcm16`). Available formats vary by model. |

