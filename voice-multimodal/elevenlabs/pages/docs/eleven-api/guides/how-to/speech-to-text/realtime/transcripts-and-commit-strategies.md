---
title: "Transcripts and commit strategies"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies.md
path: docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Transcripts and commit strategies

> **Note**
>
> **How-to guide** · Assumes you have completed the
> [client-side](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming) or
> [server-side streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming) guide.

## Overview

When transcribing audio, you will receive partial and committed transcripts.

* **Partial transcripts** - the interim results of the transcription
* **Committed transcripts** - the final results of the transcription segment that are sent when a "commit" message is received. A session can have multiple committed transcripts.

The commit transcript can optionally contain word-level timestamps. This is only received when the "include timestamps" option is set to `true`.

```python
# Initialize the connection
connection = await elevenlabs.speech_to_text.realtime.connect(RealtimeUrlOptions(
  model_id="scribe_v2_realtime",
  include_timestamps=True, # Include this to receive the RealtimeEvents.COMMITTED_TRANSCRIPT_WITH_TIMESTAMPS event with word-level timestamps
))
```

```typescript
// Initialize the connection
const connection = await elevenlabs.speechToText.realtime.connect({
  modelId: "scribe_v2_realtime",
  includeTimestamps: true, // Include this to receive the RealtimeEvents.COMMITTED_TRANSCRIPT_WITH_TIMESTAMPS event with word-level timestamps
});
```

**`React`**

```typescript title="React"
const connection = useScribe({
  modelId: "scribe_v2_realtime",
  // Configuring this callback will automatically set the `includeTimestamps` option to `true`
  onCommittedTranscriptWithTimestamps: (data) => {
    console.log("Committed with timestamps:", data.text);
    console.log("Timestamps:", data.words);
  },
});
```

**`JavaScript`**

```typescript title="JavaScript"
const connection = Scribe.connect({
  modelId: "scribe_v2_realtime",
  includeTimestamps: true, // Include this to receive the RealtimeEvents.COMMITTED_TRANSCRIPT_WITH_TIMESTAMPS event with word-level timestamps
});
```

## Commit strategies

When sending audio chunks via the WebSocket, transcript segments can be committed in two ways: Manual Commit or Voice Activity Detection (VAD).

### Manual commit

With the manual commit strategy, you control when to commit transcript segments. This is the strategy that is used by default. Committing a segment will clear the processed accumulated transcript and start a new segment without losing context. Committing every 20-30 seconds is good practice to improve latency. Even if you do not commit manually, the model automatically commits after approximately 36 seconds of accumulated audio.

For best results, commit during silence periods or another logical point like a turn model.

> **Info**
>
> Transcript processing starts after the first 2 seconds of audio are sent.

```python
await connection.send({
  "audio_base_64": audio_base_64,
  "sample_rate": 16000,
})

# When ready to finalize the segment
await connection.commit()
```

```typescript
connection.send({
  audioBase64: audioBase64,
  sampleRate: 16000,
});

// When ready to finalize the segment
connection.commit();
```

> **Warning**
>
> Committing manually several times in a short sequence can degrade model performance.

#### Sending previous text context

When sending audio for transcription, you can send previous text context alongside the first audio chunk to help the model understand the context of the speech. This is useful in a few scenarios:

* Agent text for conversational AI use cases - Allows the model to more easily understand the context of the conversation and produce better transcriptions.
* Reconnection after a network error - This allows the model to continue transcribing, using the previous text as guidance.
* General contextual information - A short description of what the transcription will be about helps the model understand the context.

> **Warning**
>
> Sending `previous_text` context is only possible when sending the first audio chunk via
> `connection.send()`. Sending it in subsequent chunks will result in an error. Previous text works
> best when it's under *50* characters long.

```python
await connection.send({
  "audio_base_64": audio_base_64,
  "previous_text": "The previous text context",
})
```

```typescript
connection.send({
  audioBase64: audioBase64,
  previousText: "The previous text context",
});
```

### Voice Activity Detection (VAD)

With the VAD strategy, the transcription engine automatically detects speech and silence segments. When a silence threshold is reached, the transcription engine will commit the transcript segment automatically.

When transcribing audio from the microphone in the [client-side integration](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming), it is recommended to use the VAD strategy.

**`Client`**

```typescript title="Client"
import { Scribe, AudioFormat, CommitStrategy } from "@elevenlabs/client";

const connection = Scribe.connect({
  token: "sutkn_1234567890",
  modelId: "scribe_v2_realtime",
  audioFormat: AudioFormat.PCM_16000,
  commitStrategy: CommitStrategy.VAD,
  vadSilenceThresholdSecs: 1.5,
  vadThreshold: 0.4,
  minSpeechDurationMs: 100,
  minSilenceDurationMs: 100,
});
```

```python
from dotenv import load_dotenv
from elevenlabs import AudioFormat, CommitStrategy, ElevenLabs, RealtimeAudioOptions

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

connection = await elevenlabs.speech_to_text.realtime.connect(
    RealtimeAudioOptions(
        model_id="scribe_v2_realtime",
        audio_format=AudioFormat.PCM_16000,
        commit_strategy=CommitStrategy.VAD,
        vad_silence_threshold_secs=1.5,
        vad_threshold=0.4,
        min_speech_duration_ms=100,
        min_silence_duration_ms=100,
    )
)
```

**`TypeScript`**

```typescript title="TypeScript"
import { ElevenLabsClient, AudioFormat, CommitStrategy } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient();

const connection = await elevenlabs.speechToText.realtime.connect({
  modelId: "scribe_v2_realtime",
  audioFormat: AudioFormat.PCM_16000,
  commitStrategy: CommitStrategy.VAD,
  vadSilenceThresholdSecs: 1.5,
  vadThreshold: 0.4,
  minSpeechDurationMs: 100,
  minSilenceDurationMs: 100,
});
```

## Keeping the connection alive during silence

The official SDKs don't drop the connection when no messages arrive, so most integrations don't need this. If your own WebSocket client, or a proxy or load balancer in between, closes the connection when no frames arrive for a while, pass the optional `keepalive_interval_ms` query parameter when connecting. This matters during long stretches of silence, for example a phone call with 10-15 second pauses. About once per interval, the server sends a keepalive `partial_transcript`: empty (`text: ""`) if the current segment has no uncommitted text, or a repeat of the latest partial text if it does.

> **Warning**
>
> Keepalives are not a free-running ping: you must keep streaming audio (silence frames are fine).
> If you stop sending audio, no keepalives are sent, and the server closes the connection after 15
> seconds without any client messages. This server limit is not configurable.

* Accepts an integer between `500` and `10000` (milliseconds). It is disabled by default; omit the parameter to keep the existing behavior.
* Out-of-range or non-integer values cause the server to send an `invalid_request` error and close the connection.
* Keepalives are driven by the model actually processing the silent audio you send, not a free-running timer, so they also confirm the transcription path is alive.
* Audio is processed in roughly 1-second chunks, so keepalives arrive about once per interval rounded to that cadence (for example, `1000` fires about once a second, `3000` about once every 3 seconds). The first keepalive of a session arrives about 2 seconds after it starts, since the server buffers the first \~2 seconds of audio before transcribing. Set your interval to at most about a third of your own read timeout to leave margin.
* A keepalive's `text` is only empty when the current segment has no uncommitted text yet. If a pause happens after speech but before a commit — most visible with `filter_background_audio=true` or in manual commit mode without committing — the keepalive repeats the latest partial text instead, so it never blanks interim text. After a commit, keepalives go back to empty until new speech arrives.
* Works with both `commit_strategy=manual` and `commit_strategy=vad`, and with `filter_background_audio=true`. Has no billing impact beyond the audio you're already streaming.
* The `session_started` message's `config` echoes back `keepalive_interval_ms` (`null` when disabled).

> **Info**
>
> An empty `partial_transcript` (`text: ""`) means "no speech in the current segment." A repeated,
> identical `partial_transcript` during a pause is also a keepalive — clients should simply render
> partials as they already do rather than special-casing the repeat.

Add the parameter to the WebSocket URL:

```text
wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v2_realtime&commit_strategy=vad&keepalive_interval_ms=1000
```

## Supported audio formats

| Format     | Sample Rate | Description                             |
| ---------- | ----------- | --------------------------------------- |
| pcm\_8000  | 8 kHz       | 16-bit PCM, little-endian               |
| pcm\_16000 | 16 kHz      | 16-bit PCM, little-endian (recommended) |
| pcm\_22050 | 22.05 kHz   | 16-bit PCM, little-endian               |
| pcm\_24000 | 24 kHz      | 16-bit PCM, little-endian               |
| pcm\_44100 | 44.1 kHz    | 16-bit PCM, little-endian               |
| pcm\_48000 | 48 kHz      | 16-bit PCM, little-endian               |
| ulaw\_8000 | 8 kHz       | 8-bit μ-law encoding                    |

## Best practices

### Audio quality

* For best results, use a 16kHz sample rate for an optimum balance of quality and bandwidth.
* Ensure clean audio input with minimal background noise.
* Use an appropriate microphone gain to avoid clipping.
* Only mono audio is supported at this time.

### Chunk size

* Send audio chunks of 0.1 - 1 second in length for smooth streaming.
* Smaller chunks result in lower latency but more overhead.
* Larger chunks are more efficient but can introduce latency.

## Next steps

#### [Server-side streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming)

Set up server-side audio transcription using the WebSocket API.

#### [Event reference](/docs/eleven-api/guides/how-to/speech-to-text/realtime/event-reference)

Full list of events and error types from the realtime STT API.
