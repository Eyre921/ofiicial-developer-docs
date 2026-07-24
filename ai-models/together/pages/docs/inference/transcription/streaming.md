---
title: "Streaming transcription"
source: https://docs.together.ai/docs/inference/transcription/streaming
path: docs/inference/transcription/streaming
---

Use the real-time WebSocket API for low-latency, incremental speech-to-text.

For applications requiring the lowest latency, use the real-time WebSocket API. This provides streaming transcription with incremental results.

You have two ways to connect:

* The [Python SDK](#python-sdk) (`client.beta.realtime.transcription()`), which handles the WebSocket, reconnection, and audio replay for you. Use this for most applications.
* The [raw WebSocket protocol](#raw-websocket-protocol), for languages other than Python or when you need full control over the wire.

<Tip>
  The server uses Voice Activity Detection (VAD) to automatically segment speech. You can tune VAD parameters for your audio characteristics. See the [Voice activity detection guide](/docs/inference/transcription/voice-activity-detection) for configuration details and common presets.
</Tip>

## Python SDK

<Note>
  The Python SDK for real-time transcription is in beta, and the API surface may change before it stabilizes. Share feedback with [support@together.ai](mailto:support@together.ai).
</Note>

The SDK opens the WebSocket, streams your audio, and returns transcription events. When the connection drops mid-conversation, the session holds on to the speech the server hadn't transcribed yet, reconnects automatically, and picks up where the transcript left off, so words spoken during the outage still come back as text.

Install the SDK with the `realtime` extra:

```bash theme={null}
pip install "together[realtime]"
```

### Basic usage

Call `client.beta.realtime.transcription()` to open a session, feed audio with `session.append()`, and consume events by iterating the session. Each `TranscriptDelta` is an interim result that updates while a phrase is being spoken; each `TranscriptCompleted` is the finalized transcript for one utterance.

```python theme={null}
import asyncio

from together import AsyncTogether
from together.realtime import TranscriptCompleted, TranscriptDelta


async def main():
    client = AsyncTogether()

    async with client.beta.realtime.transcription(
        model="openai/whisper-large-v3",
        sample_rate=16_000,
    ) as session:
        # Feed audio from your capture source as it arrives (any chunk size).
        await session.append(pcm_chunk)  # 16 kHz mono 16-bit PCM

        async for event in session:
            if isinstance(event, TranscriptDelta):
                print("interim:", event.text)
            elif isinstance(event, TranscriptCompleted):
                print("final:", event.text)

        # Finalize whatever was said last.
        transcript = await session.flush()
        print("full transcript:", transcript)


asyncio.run(main())
```

`session.append()` never blocks on network state, so it is safe to call from a capture loop. Instead of iterating the session, you can pass an `event_callback=` function to handle events as they arrive.

### Audio format

Audio in is 16 kHz mono 16-bit PCM (`pcm_s16le_16000`). Resample your source before appending. Passing `sample_rate=` lets the SDK reject a mismatch loudly instead of silently transcribing the wrong sample rate.

### Utterance boundaries

Utterance boundaries are detected server-side by default. Final transcripts arrive on their own as the speaker pauses. To control segmentation yourself, pass `turn_detection={"type": "none"}` and call `await session.commit()` when each segment ends.

### Session events

Iterate the session (or pass `event_callback=`) to receive normalized events. Import them from `together.realtime`.

| Event                 | Meaning                                                                                                 |
| :-------------------- | :------------------------------------------------------------------------------------------------------ |
| `SessionStarted`      | The session opened. `session_id` is useful for correlating with server-side logs.                       |
| `TranscriptDelta`     | Interim text for the current utterance. Updates as the phrase is spoken.                                |
| `TranscriptCompleted` | Finalized transcript for one utterance.                                                                 |
| `TranscriptFailed`    | One utterance failed server-side. The session continues.                                                |
| `Reconnecting`        | A transient failure occurred and the SDK is reconnecting with backoff. No action needed.                |
| `Reconnected`         | The connection recovered. `replayed_seconds` reports how much speech was replayed.                      |
| `BufferGap`           | Audio was dropped beyond recovery (an outage longer than the retention window). `dropped_seconds` lost. |

`TranscriptDelta` and `TranscriptCompleted` may also include optional quality fields when the server sends them: `logprobs` (`avg_logprob`, `token_logprobs`, `token_texts`) and `tokens` (per-token `token_id`, `text`, and `confidence`).

### Reconnection and replay

When the connection drops, the session emits `Reconnecting` and `Reconnected` events and retries on its own. By default the SDK makes up to two same-endpoint reconnect attempts (`reconnect={"max_attempts": 2}`) before raising. Transcripts recomputed from speech carried across the reconnect are marked `replayed=True` and may overlap text you already received. Voice agents that act on each final result can set `buffer={"max_replay_seconds": 0}` to resume live with no re-emission instead.

### Failover across endpoints

If an endpoint fails for good, calls raise `RealtimeConnectionError`. When the server reports it cannot currently serve (`exc.code == "no_healthy_workers"`, including WebSocket close code `4503`), the SDK raises immediately with no same-endpoint retry so you can rotate. To keep a conversation alive across endpoint outages, run a failover ring: on failure, `session.pending_audio()` hands you the un-transcribed speech to seed a new session on another endpoint.

```python theme={null}
from together import AsyncTogether
from together.realtime import RealtimeConnectionError

# Independent deployments of the same model. On failure, move to the next.
endpoints = [
    ("https://api.together.ai/v1", "openai/whisper-large-v3-endpoint1"),
    ("https://api.together.ai/v1", "openai/whisper-large-v3-endpoint2"),
]

carry_over = b""  # audio a failed endpoint received but never transcribed

for base_url, model in endpoints:
    client = AsyncTogether(base_url=base_url)
    session = client.beta.realtime.transcription(
        model=model,
        sample_rate=16_000,
        reconnect={"max_attempts": 0},  # switch endpoints immediately
    )
    try:
        async with session:
            if carry_over:
                await session.append(carry_over)
            # ... stream the rest of your audio ...
        break
    except RealtimeConnectionError as exc:
        # Includes exc.code == "no_healthy_workers". Take back untranscribed audio.
        carry_over = session.pending_audio()
```

### Synchronous usage

`Together().beta.realtime.transcription(...)` mirrors the async API on a background thread. Use it for a handful of concurrent sessions. For high concurrency, use the async client.

### Key parameters

| Parameter            | Description                                                                                                 |
| :------------------- | :---------------------------------------------------------------------------------------------------------- |
| `model`              | Model to use, for example `openai/whisper-large-v3`.                                                        |
| `sample_rate`        | Sample rate of the audio you append. Lets the SDK validate the format.                                      |
| `input_audio_format` | Wire audio format. Defaults to `pcm_s16le_16000`.                                                           |
| `language`           | Source language hint passed through to the service.                                                         |
| `prompt`             | Text prompt to bias transcription, passed through to the service.                                           |
| `turn_detection`     | Turn-detection config (for example `{"type": "none"}`, `min_silence_duration_ms`, `max_speech_duration_s`). |
| `reconnect`          | Reconnection policy. Defaults to `max_attempts=2`. Use `{"max_attempts": 0}` to fail over immediately.      |
| `buffer`             | Replay buffer config, for example `{"max_replay_seconds": 0}` to resume live without re-emitting speech.    |
| `keepalive_silence`  | When `True`, send silence so idle sessions stay alive past the server idle timeout.                         |
| `event_callback`     | A function called with each event, as an alternative to iterating the session.                              |

For full manual control over the raw wire events with no automatic recovery, use `client.beta.realtime.connect()`.

## Raw WebSocket protocol

Use the raw WebSocket protocol from languages other than Python, or when you need full control over the wire. The SDK above wraps this same protocol.

### Establish a connection

Connect to: `wss://api.together.ai/v1/realtime?model={model}&input_audio_format=pcm_s16le_16000`

**Headers:**

```javascript theme={null}
{
  'Authorization': 'Bearer $TOGETHER_API_KEY',
  'OpenAI-Beta': 'realtime=v1'
}
```

### Query parameters

| Parameter            | Type   | Required | Description                                    |
| :------------------- | :----- | :------- | :--------------------------------------------- |
| model                | string | Yes      | Model to use (e.g., `openai/whisper-large-v3`) |
| input\_audio\_format | string | Yes      | Audio format: `pcm_s16le_16000`                |

### Client-to-server messages

#### Append audio to buffer

```json theme={null}
{
  "type": "input_audio_buffer.append",
  "audio": "base64-encoded-audio-chunk"
}
```

Send audio data in base64-encoded PCM format.

#### Commit audio buffer

```json theme={null}
{
  "type": "input_audio_buffer.commit"
}
```

Forces transcription of any remaining audio in the server-side buffer.

### Server-to-client messages

#### Delta events (intermediate results)

```json theme={null}
{
  "type": "conversation.item.input_audio_transcription.delta",
  "delta": "The quick brown fox jumps"
}
```

Delta events are intermediate transcriptions. The model is still processing and may revise the output. Each delta message overrides the previous delta.

#### Completed events (final results)

```json theme={null}
{
  "type": "conversation.item.input_audio_transcription.completed",
  "transcript": "The quick brown fox jumps over the lazy dog"
}
```

Completed events are final transcriptions. The model is confident about this text. The next delta event continues from where this completed.

### Real-time example

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import base64
  import json
  import os
  import sys

  import numpy as np
  import sounddevice as sd
  import websockets

  # Configuration
  API_KEY = os.getenv("TOGETHER_API_KEY")
  MODEL = "openai/whisper-large-v3"
  SAMPLE_RATE = 16000
  BATCH_SIZE = 4096  # 256ms batches for optimal performance

  if not API_KEY:
      print("Error: Set TOGETHER_API_KEY environment variable")
      sys.exit(1)


  class RealtimeTranscriber:
      """Realtime transcription client for Together AI."""

      def __init__(self):
          self.ws = None
          self.stream = None
          self.is_ready = False
          self.audio_buffer = np.array([], dtype=np.float32)
          self.audio_queue = asyncio.Queue()

      async def connect(self):
          """Connect to Together AI API."""
          url = (
              f"wss://api.together.ai/v1/realtime"
              f"?intent=transcription"
              f"&model={MODEL}"
              f"&input_audio_format=pcm_s16le_16000"
              f"&authorization=Bearer {API_KEY}"
          )

          self.ws = await websockets.connect(
              url,
              subprotocols=[
                  "realtime",
                  f"openai-insecure-api-key.{API_KEY}",
                  "openai-beta.realtime-v1",
              ],
          )

      async def send_audio(self):
          """Capture and send audio to API."""

          def audio_callback(indata, frames, time, status):
              self.audio_queue.put_nowait(indata.copy().flatten())

          # Start microphone stream
          self.stream = sd.InputStream(
              samplerate=SAMPLE_RATE,
              channels=1,
              dtype="float32",
              blocksize=1024,
              callback=audio_callback,
          )
          self.stream.start()

          # Process and send audio
          while True:
              try:
                  audio = await asyncio.wait_for(
                      self.audio_queue.get(), timeout=0.1
                  )

                  if self.ws and self.is_ready:
                      # Add to buffer
                      self.audio_buffer = np.concatenate(
                          [self.audio_buffer, audio]
                      )

                      # Send when buffer is full
                      while len(self.audio_buffer) >= BATCH_SIZE:
                          batch = self.audio_buffer[:BATCH_SIZE]
                          self.audio_buffer = self.audio_buffer[BATCH_SIZE:]

                          # Convert float32 to int16 PCM
                          audio_int16 = (
                              np.clip(batch, -1.0, 1.0) * 32767
                          ).astype(np.int16)
                          audio_base64 = base64.b64encode(
                              audio_int16.tobytes()
                          ).decode()

                          # Send to API
                          await self.ws.send(
                              json.dumps(
                                  {
                                      "type": "input_audio_buffer.append",
                                      "audio": audio_base64,
                                  }
                              )
                          )

              except asyncio.TimeoutError:
                  continue
              except Exception as e:
                  print(f"Error: {e}", file=sys.stderr)
                  break

      async def receive_transcriptions(self):
          """Receive and display transcription results."""
          current_interim = ""

          try:
              async for message in self.ws:
                  data = json.loads(message)

                  if data["type"] == "session.created":
                      self.is_ready = True

                  elif (
                      data["type"]
                      == "conversation.item.input_audio_transcription.delta"
                  ):
                      # Interim result
                      print(
                          f"\r\033[90m{data['delta']}\033[0m", end="", flush=True
                      )
                      current_interim = data["delta"]

                  elif (
                      data["type"]
                      == "conversation.item.input_audio_transcription.completed"
                  ):
                      # Final result
                      if current_interim:
                          print("\r\033[K", end="")
                      print(f"\033[92m{data['transcript']}\033[0m")
                      current_interim = ""

                  elif data["type"] == "error":
                      print(f"\nError: {data.get('message', 'Unknown error')}")

          except websockets.exceptions.ConnectionClosed:
              pass

      async def close(self):
          """Close connections and cleanup."""
          if self.stream:
              self.stream.stop()
              self.stream.close()

          # Flush remaining audio
          if len(self.audio_buffer) > 0 and self.ws and self.is_ready:
              try:
                  audio_int16 = (
                      np.clip(self.audio_buffer, -1.0, 1.0) * 32767
                  ).astype(np.int16)
                  audio_base64 = base64.b64encode(audio_int16.tobytes()).decode()
                  await self.ws.send(
                      json.dumps(
                          {
                              "type": "input_audio_buffer.append",
                              "audio": audio_base64,
                          }
                      )
                  )
              except Exception:
                  pass

          if self.ws:
              await self.ws.close()

      async def run(self):
          """Main execution loop."""
          try:
              print("🎤 Together AI Realtime Transcription")
              print("=" * 40)
              print("Connecting...")

              await self.connect()

              print("✓ Connected")
              print("✓ Recording started - speak now\n")

              # Run audio capture and transcription concurrently
              await asyncio.gather(
                  self.send_audio(), self.receive_transcriptions()
              )

          except KeyboardInterrupt:
              print("\n\nStopped")
          except Exception as e:
              print(f"Error: {e}", file=sys.stderr)
          finally:
              await self.close()


  async def main():
      transcriber = RealtimeTranscriber()
      await transcriber.run()


  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import WebSocket from 'ws';
  import recorder from 'node-record-lpcm16';

  // Configuration
  const API_KEY = process.env.TOGETHER_API_KEY;
  const MODEL = 'openai/whisper-large-v3';
  const SAMPLE_RATE = 16000;

  if (!API_KEY) {
    console.error('Error: Set TOGETHER_API_KEY environment variable');
    process.exit(1);
  }

  class RealtimeTranscriber {
    /** Realtime transcription client for Together AI. */
    private ws: WebSocket | null = null;
    private isReady = false;
    private currentInterim = '';

    async connect() {
      /** Connect to Together AI API. */
      const url =
        `wss://api.together.ai/v1/realtime` +
        `?intent=transcription` +
        `&model=${MODEL}` +
        `&input_audio_format=pcm_s16le_16000` +
        `&authorization=Bearer ${API_KEY}`;

      this.ws = new WebSocket(url, [
        'realtime',
        `openai-insecure-api-key.${API_KEY}`,
        'openai-beta.realtime-v1',
      ]);

      this.ws.on('message', (data) => this.receiveTranscriptions(data));
      this.ws.on('error', (err) => console.error(`Error: ${err}`));

      return new Promise((resolve) => {
        this.ws?.on('open', () => {
          resolve(null);
        });
      });
    }

    sendAudio() {
      /** Capture and send audio to API. */
      const mic = recorder.record({
        sampleRate: SAMPLE_RATE,
        threshold: 0,
        verbose: false,
      });

      mic.stream().on('data', (chunk: Buffer) => {
        if (this.ws && this.isReady && this.ws.readyState === WebSocket.OPEN) {
          this.ws.send(
            JSON.stringify({
              type: 'input_audio_buffer.append',
              audio: chunk.toString('base64'),
            })
          );
        }
      });

      mic.stream().on('error', (err) => {
        console.error('Microphone Error:', err);
      });
    }

    receiveTranscriptions(data: WebSocket.Data) {
      /** Receive and display transcription results. */
      const message = JSON.parse(data.toString());

      if (message.type === 'session.created') {
        this.isReady = true;
      } else if (
        message.type === 'conversation.item.input_audio_transcription.delta'
      ) {
        // Interim result
        process.stdout.write(`\r\x1b[90m${message.delta}\x1b[0m`);
        this.currentInterim = message.delta;
      } else if (
        message.type === 'conversation.item.input_audio_transcription.completed'
      ) {
        // Final result
        if (this.currentInterim) {
          process.stdout.write('\r\x1b[K');
        }
        console.log(`\x1b[92m${message.transcript}\x1b[0m`);
        this.currentInterim = '';
      } else if (message.type === 'error') {
        console.error(`\nError: ${message.message || 'Unknown error'}`);
      }
    }

    async run() {
      /** Main execution loop. */
      try {
        console.log('🎤 Together AI Realtime Transcription');
        console.log('='.repeat(40));
        console.log('Connecting...');

        await this.connect();

        console.log('✓ Connected');
        console.log('✓ Recording started - speak now\n');

        this.sendAudio();
      } catch (e) {
        console.error(`Error: ${e}`);
      }
    }
  }

  async function main() {
    const transcriber = new RealtimeTranscriber();
    await transcriber.run();
  }

  main();
  ```
</CodeGroup>
