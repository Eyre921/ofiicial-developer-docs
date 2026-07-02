---
title: "Streaming transcription"
source: https://docs.together.ai/docs/inference/transcription/streaming
path: docs/inference/transcription/streaming
---

Use the real-time WebSocket API for low-latency, incremental speech-to-text.

For applications requiring the lowest latency, use the real-time WebSocket API. This provides streaming transcription with incremental results.

<Tip>
  The server uses Voice Activity Detection (VAD) to automatically segment speech. You can tune VAD parameters for your audio characteristics. See the [Voice activity detection guide](/docs/inference/transcription/voice-activity-detection) for configuration details and common presets.
</Tip>

<Warning>
  The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.
</Warning>

## Establish a connection

Connect to: `wss://api.together.ai/v1/realtime?model={model}&input_audio_format=pcm_s16le_16000`

**Headers:**

```javascript theme={null}
{
  'Authorization': 'Bearer $TOGETHER_API_KEY',
  'OpenAI-Beta': 'realtime=v1'
}
```

## Query parameters

| Parameter            | Type   | Required | Description                                    |
| :------------------- | :----- | :------- | :--------------------------------------------- |
| model                | string | Yes      | Model to use (e.g., `openai/whisper-large-v3`) |
| input\_audio\_format | string | Yes      | Audio format: `pcm_s16le_16000`                |

## Client-to-server messages

### Append audio to buffer

```json theme={null}
{
  "type": "input_audio_buffer.append",
  "audio": "base64-encoded-audio-chunk"
}
```

Send audio data in base64-encoded PCM format.

### Commit audio buffer

```json theme={null}
{
  "type": "input_audio_buffer.commit"
}
```

Forces transcription of any remaining audio in the server-side buffer.

## Server-to-client messages

### Delta events (intermediate results)

```json theme={null}
{
  "type": "conversation.item.input_audio_transcription.delta",
  "delta": "The quick brown fox jumps"
}
```

Delta events are intermediate transcriptions. The model is still processing and may revise the output. Each delta message overrides the previous delta.

### Completed events (final results)

```json theme={null}
{
  "type": "conversation.item.input_audio_transcription.completed",
  "transcript": "The quick brown fox jumps over the lazy dog"
}
```

Completed events are final transcriptions. The model is confident about this text. The next delta event continues from where this completed.

## Real-time example

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
