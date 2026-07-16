---
title: "Transcribe audio"
source: https://docs.together.ai/docs/inference/transcription/overview
path: docs/inference/transcription/overview
---

Transcribe and translate audio into text.

<Tip>
  Using a coding agent? Install the [together-audio](https://github.com/togethercomputer/skills/tree/main/skills/together-audio) skill to let your agent write correct speech-to-text code automatically. See [agent skills](/docs/agent-skills) for details.
</Tip>

Together AI hosts speech recognition models including OpenAI's Whisper and NVIDIA Parakeet for batch transcription and real-time streaming.

<Tip>
  Read the [end-to-end guide](/docs/how-to-build-phone-voice-agent) to build a live voice agent powered by Together AI's real-time STT and TTS pipeline.
</Tip>

## Quickstart

Basic transcription and translation:

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  from together import Together

  client = Together()

  ## Basic transcription

  response = client.audio.transcriptions.create(
      file=Path("audio.mp3"),
      model="openai/whisper-large-v3",
      language="en",
  )
  print(response.text)

  ## Basic translation

  response = client.audio.translations.create(
      file=Path("foreign_audio.mp3"),
      model="openai/whisper-large-v3",
  )
  print(response.text)
  ```

  ```typescript TypeScript theme={null}
  import { createReadStream } from 'fs';
  import Together from 'together-ai';

  const together = new Together();

  // Basic transcription
  const transcription = await together.audio.transcriptions.create({
    file: createReadStream('audio.mp3'),
    model: 'openai/whisper-large-v3',
    language: 'en',
  });
  console.log(transcription.text);

  // Basic translation
  const translation = await together.audio.translations.create({
    file: createReadStream('foreign_audio.mp3'),
    model: 'openai/whisper-large-v3',
  });
  console.log(translation.text);
  ```

  ```bash cURL theme={null}
  # Use -F for each field. Append ;type=<format> to the file field so the
  # server knows the audio format. Common values:
  #   audio/mpeg  → .mp3
  #   audio/wav   → .wav
  #   audio/mp4   → .m4a
  #   audio/webm  → .webm
  #   audio/flac  → .flac

  # Transcription (MP3)
  curl -X POST "https://api.together.ai/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@audio.mp3;type=audio/mpeg" \
       -F "model=openai/whisper-large-v3" \
       -F "language=en" \
       -F "response_format=json"

  # Translation (MP3)
  curl -X POST "https://api.together.ai/v1/audio/translations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@foreign_audio.mp3;type=audio/mpeg" \
       -F "model=openai/whisper-large-v3"

  # Transcription (WAV)
  curl -X POST "https://api.together.ai/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@audio.wav;type=audio/wav" \
       -F "model=openai/whisper-large-v3"
  ```
</CodeGroup>

## Available models

The following speech-to-text models are available:

| Organization | Model                           | Model string for API                     | Serverless | Dedicated |
| :----------- | :------------------------------ | :--------------------------------------- | :--------: | :-------: |
| OpenAI       | Whisper Large v3                | `openai/whisper-large-v3`                |      ✅     |     ✅     |
| NVIDIA       | Parakeet TDT 0.6B v3            | `nvidia/parakeet-tdt-0.6b-v3`            |      ✅     |     ✅     |
| NVIDIA       | Nemotron 3 ASR Streaming 0.6B   | `nvidia/nemotron-3-asr-streaming-0.6b`   |      ✅     |     ✅     |
| NVIDIA       | Nemotron 3.5 ASR Streaming 0.6B | `nvidia/nemotron-3.5-asr-streaming-0.6b` |      ✅     |     ✅     |
| Deepgram     | Nova-3 (English)                | `deepgram/nova-3-en`                     |      ❌     |     ✅     |
| Deepgram     | Nova-3 Multilingual             | `deepgram/nova-3-multi`                  |      ❌     |     ✅     |
| Deepgram     | Flux                            | `deepgram/flux`                          |      ❌     |     ✅     |

See the [serverless catalog](/docs/serverless/models) and the [dedicated model inference catalog](/docs/dedicated-endpoints/models) for pricing and additional deployment options.

## Limits

| Limit                            | Value                                                             | Notes                                                                                                                                                                                    |
| -------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Max request size (direct upload) | **500 MB**                                                        | Requests above this are rejected at the edge with `HTTP 413 Payload Too Large`. For anything larger, host the audio at a public HTTPS URL and pass that URL as the `file` field instead. |
| Max file size (URL fetch)        | **1 GB**                                                          | When you submit an HTTPS URL instead of binary, the server downloads up to 1 GB. Larger downloads fail with `400 file_too_large`.                                                        |
| Max audio duration               | **4 hours** per request                                           | Longer audio is rejected with `400 audio_too_long`. Split into ≤ 4 h segments and submit separately.                                                                                     |
| Supported formats                | `.wav`, `.mp3`, `.m4a`, `.webm`, `.flac`, `.ogg`, `.opus`, `.aac` |                                                                                                                                                                                          |

For payloads above 500 MB, host the file at a public HTTPS URL and pass that URL as the `file` field instead of a binary upload. The 500 MB edge cap only applies to direct uploads. See [Errors and troubleshooting](/docs/inference/transcription/features#errors-and-troubleshooting) for the full list of error codes.

## Audio transcription

Audio transcription is speech-to-text in the same language as the source audio.

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file=Path("meeting_recording.mp3"),
      model="openai/whisper-large-v3",
      language="en",
      response_format="json",
  )

  print(f"Transcription: {response.text}")
  ```

  ```typescript TypeScript theme={null}
  import { createReadStream } from 'fs';
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.audio.transcriptions.create({
    file: createReadStream('meeting_recording.mp3'),
    model: 'openai/whisper-large-v3',
    language: 'en',
    response_format: 'json',
  });

  console.log(`Transcription: ${response.text}`);
  ```
</CodeGroup>

The API supports the following audio formats:

* `.wav` (audio/wav)
* `.mp3` (audio/mpeg)
* `.m4a` (audio/mp4)
* `.webm` (audio/webm)
* `.flac` (audio/flac)
* `.ogg` (audio/ogg)
* `.opus` (audio/opus)
* `.aac` (audio/aac)

### Audio limits

The same limits apply to both `/v1/audio/transcriptions` and `/v1/audio/translations`:

* **Maximum duration:** 4 hours. Longer audio is rejected with an `audio_too_long` error.
* **Binary uploads:** Capped at 500 MB. Larger uploads return HTTP 413. Submit the audio via an HTTPS URL on the `file` field instead.
* **URL-fetched audio:** Capped at 1 GB and 4 hours when you pass a public HTTPS URL as `file`.

For longer recordings, chunk the audio into ≤ 4 h segments and submit each chunk as a separate URL request.

When sending a binary upload, put the `model` form field **before** the `file` field in the multipart body so the server can dispatch the request without buffering the full audio payload.

### Input methods

#### Path object

```python Python theme={null}
from pathlib import Path

response = client.audio.transcriptions.create(
    file=Path("recordings/interview.wav"),
    model="openai/whisper-large-v3",
)
```

#### File-like object

```python Python theme={null}
with open("audio.mp3", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        file=audio_file,
        model="openai/whisper-large-v3",
    )
```

#### Remote URL

The Python SDK doesn't accept a string URL on `file=`. To transcribe a remote file, download it first.

### Language support

Specify the audio language using ISO 639-1 language codes:

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.transcriptions.create(
      file=Path("spanish_audio.mp3"),
      model="openai/whisper-large-v3",
      language="es",  # Spanish
  )
  ```
</CodeGroup>

Common language codes:

* `"en"`: English.
* `"es"`: Spanish.
* `"fr"`: French.
* `"de"`: German.
* `"ja"`: Japanese.
* `"zh"`: Chinese.
* `"auto"`: Auto-detect (default).

### Custom prompts

Use prompts to improve transcription accuracy for specific contexts.

<Note>
  Prompts are supported only on Whisper-family models (for example, `openai/whisper-large-v3`). Other STT models (for example, `nvidia/parakeet-tdt-0.6b-v3`) accept the field for API compatibility but ignore it.
</Note>

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.transcriptions.create(
      file=Path("medical_consultation.mp3"),
      model="openai/whisper-large-v3",
      language="en",
      prompt="This is a medical consultation discussing patient symptoms, diagnosis, and treatment options.",
  )
  ```
</CodeGroup>

## Next steps

* [Streaming transcription](/docs/inference/transcription/streaming): real-time WebSocket transcription for low-latency applications.
* [Audio translation](/docs/inference/transcription/translation): translate speech in any language to English text.
* [Transcription features](/docs/inference/transcription/features): speaker diarization, word-level timestamps, response formats, async support, and best practices.
