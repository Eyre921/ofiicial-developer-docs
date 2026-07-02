---
title: "Advanced transcription options"
source: https://docs.together.ai/docs/inference/transcription/features
path: docs/inference/transcription/features
---

Speaker diarization, word-level timestamps, response formats, async support, and best practices.

## Speaker diarization

Enable diarization to identify who is speaking when. If you know the expected speaker count, pass `min_speakers` and `max_speakers` to improve accuracy.

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file=Path("meeting.mp3"),
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      diarize="true",  # Enable speaker diarization
      min_speakers=1,
      max_speakers=5,
  )

  # Access speaker segments
  print(response.speaker_segments)
  ```

  ```typescript TypeScript theme={null}
  import { createReadStream } from 'fs';
  import Together from 'together-ai';

  const together = new Together();

  async function transcribeWithDiarization() {
    const response = await together.audio.transcriptions.create({
      file: createReadStream('meeting.mp3'),
      model: 'openai/whisper-large-v3',
      diarize: true  // Enable speaker diarization
    });

    // Access the speaker segments
    console.log(`Speaker Segments: ${response.speaker_segments}\n`);
  }

  transcribeWithDiarization();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@meeting.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "diarize=true"
  ```
</CodeGroup>

**Example response with diarization:**

```json theme={null}
AudioSpeakerSegment(
    id=1,
    speaker_id='SPEAKER_01',
    start=6.268,
    end=30.776,
    text=(
        "Hello. Oh, hey, Justin. How are you doing? ..."
    ),
    words=[
        AudioTranscriptionWord(
            word='Hello.',
            start=6.268,
            end=11.314,
            id=0,
            speaker_id='SPEAKER_01'
        ),
        AudioTranscriptionWord(
            word='Oh,',
            start=11.834,
            end=11.894,
            id=1,
            speaker_id='SPEAKER_01'
        ),
        AudioTranscriptionWord(
            word='hey,',
            start=11.914,
            end=11.995,
            id=2,
            speaker_id='SPEAKER_01'
        ),
        ...
    ]
)
```

## Word-level timestamps

Get word-level timing information:

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.transcriptions.create(
      file=Path("audio.mp3"),
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      timestamp_granularities="word",
  )

  print(f"Text: {response.text}")
  print(f"Language: {response.language}")
  print(f"Duration: {response.duration}s")

  ## Access individual words with timestamps
  if response.words:
      for word in response.words:
          print(f"'{word['word']}' [{word['start']:.2f}s - {word['end']:.2f}s]")
  ```
</CodeGroup>

**Example output:**

```text Text theme={null}
Text: It is certain that Jack Pumpkinhead might have had a much finer house to live in.
Language: en
Duration: 7.2562358276643995s

'It' [0.00s - 0.36s]
'is' [0.42s - 0.47s]
'certain' [0.51s - 0.74s]
'that' [0.79s - 0.86s]
'Jack' [0.90s - 1.11s]
'Pumpkinhead' [1.15s - 1.66s]
'might' [1.81s - 2.00s]
'have' [2.04s - 2.13s]
'had' [2.16s - 2.26s]
'a' [2.30s - 2.32s]
'much' [2.36s - 2.48s]
'finer' [2.54s - 2.74s]
'house' [2.78s - 2.93s]
'to' [2.96s - 3.03s]
'live' [3.07s - 3.21s]
'in.' [3.26s - 7.27s]
```

## Response formats

### JSON format (default)

Returns only the transcribed/translated text:

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.transcriptions.create(
      file=Path("audio.mp3"),
      model="openai/whisper-large-v3",
      response_format="json",
  )

  print(response.text)  # "Hello, this is a test recording."
  ```
</CodeGroup>

### Verbose JSON format

Returns detailed information including timestamps:

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.transcriptions.create(
      file=Path("audio.mp3"),
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      timestamp_granularities="segment",
  )

  ## Access segments with timestamps
  for segment in response.segments:
      print(
          f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: {segment['text']}"
      )
  ```
</CodeGroup>

**Example output:**

```text Text theme={null}
[0.11s - 10.85s]: Call is now being recorded. Parker Scarves, how may I help you? Online for my wife, and it turns out they shipped the wrong... Oh, I am so sorry, sir. I got it for her birthday, which is tonight, and now I'm not 100% sure what I need to do. Okay, let me see if I can help. Do you have the item number of the Parker Scarves? I don't think so. Call the New Yorker, I... Excellent. What color do...

[10.88s - 21.73s]: Blue. The one they shipped was light blue. I wanted the darker one. What's the difference? The royal blue is a bit brighter. What zip code are you located in? One nine.

[22.04s - 32.62s]: Karen's Boutique, Termall. Is that close? I'm in my office. Okay, um, what is your name, sir? Charlie. Charlie Johnson. Is that J-O-H-N-S-O-N? And Mr. Johnson, do you have the Parker scarf in light blue with you now? I do. They shipped it to my office. It came in not that long ago. What I will do is make arrangements with Karen's Boutique for...

[32.62s - 41.03s]: you to Parker Scarf at no additional cost. And in addition, I was able to look up your order in our system, and I'm going to send out a special gift to you to make up for the inconvenience. Thank you. You're welcome. And thank you for calling Parker Scarf, and I hope your wife enjoys her birthday gift. Thank you. You're very welcome. Goodbye.

[43.50s - 44.20s]: you
```

## Advanced features

### Temperature control

Adjust randomness in the output (0.0 = deterministic, 1.0 = creative):

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.transcriptions.create(
      file=Path("audio.mp3"),
      model="openai/whisper-large-v3",
      temperature=0.0,  # Most deterministic
  )

  print(f"Text: {response.text}")
  ```
</CodeGroup>

## Async support

All transcription and translation operations support async/await:

### Async transcription

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from pathlib import Path

  from together import AsyncTogether


  async def transcribe_audio():
      client = AsyncTogether()

      response = await client.audio.transcriptions.create(
          file=Path("audio.mp3"),
          model="openai/whisper-large-v3",
          language="en",
      )

      return response.text


  ## Run async function
  result = asyncio.run(transcribe_audio())
  print(result)
  ```
</CodeGroup>

### Async translation

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path


  async def translate_audio():
      client = AsyncTogether()

      response = await client.audio.translations.create(
          file=Path("foreign_audio.mp3"),
          model="openai/whisper-large-v3",
      )

      return response.text


  result = asyncio.run(translate_audio())
  print(result)
  ```
</CodeGroup>

### Concurrent processing

Process multiple audio files concurrently:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from pathlib import Path

  from together import AsyncTogether


  async def process_multiple_files():
      client = AsyncTogether()

      files = [Path("audio1.mp3"), Path("audio2.mp3"), Path("audio3.mp3")]

      tasks = [
          client.audio.transcriptions.create(
              file=file,
              model="openai/whisper-large-v3",
          )
          for file in files
      ]

      responses = await asyncio.gather(*tasks)

      for i, response in enumerate(responses):
          print(f"File {files[i]}: {response.text}")


  asyncio.run(process_multiple_files())
  ```
</CodeGroup>

## Best practices

### Choose the right method

* **Batch transcription:** Best for pre-recorded audio files, podcasts, or any non-real-time use case.
* **Real-time streaming:** Best for live conversations, voice assistants, or applications requiring immediate feedback.

### Audio quality tips

* Use high-quality audio files for better transcription accuracy.
* Minimize background noise.
* Ensure clear speech with good volume levels.
* Use appropriate sample rates (16kHz or higher recommended).
* For WebSocket streaming, use PCM format: `pcm_s16le_16000`.
* Direct uploads are capped at 500 MB of audio per request, while URL uploads are capped at 1 GB or 4 hours of audio per request. See [Limits](/docs/inference/transcription/overview#limits).
* For binary uploads, place the `model` form field before the `file` field in the multipart body so the server can route the request without buffering the audio.
* For long audio files (over 4 hours), chunk the audio into ≤ 4 h segments and send each chunk as a separate URL request.
* Use streaming for real-time applications when available.

### Diarization best practices

* Works best with clear audio and distinct speakers.
* Speakers are labeled as SPEAKER\_00, SPEAKER\_01, etc.
* Use with `verbose_json` format to get segment-level speaker information.

## Errors and troubleshooting

| Response                 | Meaning                                                         | Recommended action                                                                                                                        |
| ------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `400 audio_too_long`     | Audio duration exceeds the 4 hour cap.                          | Split the file into ≤ 4 h segments and submit separately.                                                                                 |
| `400 file_too_large`     | A URL-fetched audio download exceeded the 1 GB server-side cap. | Compress the source, or split into smaller files.                                                                                         |
| `400 unsupported_format` | The audio container or codec could not be decoded.              | Re-encode to a [supported format](/docs/inference/transcription/overview#limits). Run `ffprobe` on the file to confirm it is valid audio. |
| `400 invalid_params`     | Request parameters failed validation.                           | Check the [API reference](/reference/audio-transcriptions).                                                                               |
| `413 Payload Too Large`  | A direct upload exceeded the 500 MB edge limit.                 | Submit the file via an HTTPS URL on the `file` field instead, or split the file.                                                          |
| `429`                    | Rate limit exceeded.                                            | See [serverless rate limits](/docs/serverless/rate-limits).                                                                               |
| `500 processing_failed`  | Internal decode failure after the file was accepted.            | Verify the file is valid audio with `ffprobe`. If it is, [contact support](mailto:support@together.ai) with the response `id`.            |

## Next steps

* See the [API reference](/reference/audio-transcriptions) for detailed parameter documentation.
* Learn about [text-to-speech](/docs/inference/text-to-speech/overview) for the reverse operation.
* Check out the [real-time audio transcription app guide](/docs/how-to-build-real-time-audio-transcription-app).
