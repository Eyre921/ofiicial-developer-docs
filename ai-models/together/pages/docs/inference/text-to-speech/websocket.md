---
title: "WebSocket API"
source: https://docs.together.ai/docs/inference/text-to-speech/websocket
path: docs/inference/text-to-speech/websocket
---

Stream text in and audio out over a single WebSocket connection for the lowest interactive latency.

For the lowest latency and most interactive applications, use the WebSocket API. It lets you stream text input and receive audio chunks in real time over a single persistent connection, which is ideal for chatbots, live assistants, and voice agents.

For one-shot requests where you only need a stream of audio bytes back, see [Streaming](/docs/inference/text-to-speech/streaming) instead.

<Warning>
  The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.
</Warning>

## Establish a connection

Connect to: `wss://api.together.ai/v1/audio/speech/websocket`

### Authentication

* Include your API key as a query parameter: `?api_key=<your_api_key>`.
* Or use the `Authorization` header when establishing the WebSocket connection.

## Client-to-server messages

### Append text to buffer

```json theme={null}
{
  "type": "input_text_buffer.append",
  "text": "Hello, this is a test sentence."
}
```

Appends text to the input buffer. Text is buffered until sentence completion or maximum length is reached.

### Commit buffer

```json theme={null}
{
  "type": "input_text_buffer.commit"
}
```

Forces processing of all buffered text. Use this at the end of your input stream.

### Clear buffer

```json theme={null}
{
  "type": "input_text_buffer.clear"
}
```

Clears all buffered text without processing (except text already being processed by the model).

### Update session parameters

```json theme={null}
{
  "type": "tts_session.updated",
  "session": {
    "voice": "new_voice_id"
  }
}
```

Updates TTS session settings like voice in real time. If no `context_id` is specified, all contexts are updated.

## Server-to-client messages

### Session created

```json theme={null}
{
  "event_id": "uuid-string",
  "type": "session.created",
  "session": {
    "id": "session-uuid",
    "object": "realtime.tts.session",
    "modalities": ["text", "audio"],
    "model": "canopylabs/orpheus-3b-0.1-ft",
    "voice": "tara"
  }
}
```

### Text received acknowledgment

```json theme={null}
{
  "type": "conversation.item.input_text.received",
  "text": "Hello, this is a test sentence."
}
```

### Audio delta (streaming chunks)

```json theme={null}
{
  "type": "conversation.item.audio_output.delta",
  "item_id": "tts_1",
  "delta": "base64-encoded-audio-chunk"
}
```

### Audio complete

```json theme={null}
{
  "type": "conversation.item.audio_output.done",
  "item_id": "tts_1"
}
```

### Word timestamps

Sent when `alignment=word` is set. Contains word-level timing information for the generated audio.

```json theme={null}
{
  "type": "conversation.item.word_timestamps",
  "item_id": "tts_1",
  "words": ["Hello", "world"],
  "start_seconds": [0.0, 0.4],
  "end_seconds": [0.4, 0.8]
}
```

### TTS error

```json theme={null}
{
  "type": "conversation.item.tts.failed",
  "error": {
    "message": "Error description",
    "type": "error_type",
    "code": "error_code"
  }
}
```

## WebSocket example

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import aiohttp
  import json
  import base64
  import os


  async def generate_speech():
      api_key = os.environ.get("TOGETHER_API_KEY")
      url = (
          "wss://api.together.ai/v1/audio/speech"
          "/websocket?model=hexgrad/Kokoro-82M"
          "&voice=af_alloy"
          "&response_format=pcm"
          "&sample_rate=24000"
      )

      headers = {"Authorization": f"Bearer {api_key}"}

      text_chunks = [
          "Hello, this is a test.",
          "This is the second sentence.",
          "And this is the final one.",
      ]

      audio_chunks = []

      async with aiohttp.ClientSession(headers=headers) as session:
          async with session.ws_connect(url) as ws:
              # Wait for session.created
              msg = await ws.receive()
              session_data = json.loads(msg.data)
              print(f"Session created: {session_data['session']['id']}")

              async def send_text():
                  for chunk in text_chunks:
                      await ws.send_json(
                          {
                              "type": "input_text_buffer.append",
                              "text": chunk,
                          }
                      )
                      print(f"Sent: {chunk}")
                      await asyncio.sleep(0.5)
                  await ws.send_json({"type": "input_text_buffer.commit"})
                  print("Committed")

              async def receive_audio():
                  async for msg in ws:
                      if msg.type == aiohttp.WSMsgType.TEXT:
                          data = json.loads(msg.data)
                          mtype = data.get("type", "")

                          if mtype == "conversation.item.audio_output.delta":
                              chunk = base64.b64decode(data.get("delta", ""))
                              audio_chunks.append(chunk)

                          elif mtype == "conversation.item.word_timestamps":
                              words = data.get("words", [])
                              starts = data.get("start_seconds", [])
                              stamps = list(
                                  zip(words, [f"{s:.2f}s" for s in starts])
                              )
                              print(f"  timestamps: {stamps}")

                          elif mtype in (
                              "error",
                              "conversation.item.tts.failed",
                          ):
                              err = data.get(
                                  "error",
                                  data.get("message"),
                              )
                              print(f"Error: {err}")
                              return

                      elif msg.type in (
                          aiohttp.WSMsgType.CLOSE,
                          aiohttp.WSMsgType.CLOSED,
                      ):
                          break

              send_task = asyncio.create_task(send_text())
              recv_task = asyncio.create_task(receive_audio())

              await send_task

              # Wait up to 10s for audio to stop arriving
              deadline = asyncio.get_event_loop().time() + 10
              while asyncio.get_event_loop().time() < deadline:
                  await asyncio.sleep(0.1)
                  n = len(audio_chunks)
                  await asyncio.sleep(0.3)
                  if len(audio_chunks) == n:
                      break

              recv_task.cancel()
              try:
                  await recv_task
              except asyncio.CancelledError:
                  pass

      if audio_chunks:
          pcm = b"".join(audio_chunks)
          with open("output.pcm", "wb") as f:
              f.write(pcm)
          print(
              f"\nAudio saved to output.pcm ({len(pcm):,} bytes, "
              f"{len(pcm)/48000:.1f}s at 24kHz)"
          )
          print("Play with: ffplay -f s16le -ar 24000 output.pcm")
      else:
          print("No audio received")


  asyncio.run(generate_speech())
  ```

  ```typescript TypeScript theme={null}
  const WebSocket = require('ws')
  const fs = require('fs')

  const apiKey = process.env.TOGETHER_API_KEY
  const url =
    'wss://api.together.ai/v1/audio/speech/websocket' +
    '?model=hexgrad/Kokoro-82M&voice=af_alloy&response_format=pcm&sample_rate=24000'

  const textChunks = [
    'Hello, this is a test.',
    'This is the second sentence.',
    'And this is the final one.',
  ]

  const audioChunks: Buffer[] = []

  async function generateSpeech(): Promise<void> {
    const ws = new WebSocket(url, {
      headers: { Authorization: `Bearer ${apiKey}` },
    })

    await new Promise<void>((resolve, reject) => {
      ws.on('message', (data: Buffer) => {
        const msg = JSON.parse(data.toString())
        const mtype: string = msg.type ?? ''

        if (mtype === 'session.created') {
          console.log(`Session created: ${msg.session.id}`)

          ;(async () => {
            for (const chunk of textChunks) {
              ws.send(JSON.stringify({ type: 'input_text_buffer.append', text: chunk }))
              console.log(`Sent: ${chunk}`)
              await new Promise((r) => setTimeout(r, 500))
            }
            ws.send(JSON.stringify({ type: 'input_text_buffer.commit' }))
            console.log('Committed')
          })()
        } else if (mtype === 'conversation.item.audio_output.delta') {
          audioChunks.push(Buffer.from(msg.delta, 'base64'))
        } else if (mtype === 'conversation.item.word_timestamps') {
          const words: string[] = msg.words ?? []
          const starts: number[] = msg.start_seconds ?? []
          const timestamps = words.map((w, i) => `${w}(${starts[i]?.toFixed(2)}s)`)
          console.log(`  timestamps: ${timestamps.join('  ')}`)
        } else if (mtype === 'error' || mtype === 'conversation.item.tts.failed') {
          console.error(`Error: ${msg.error ?? msg.message}`)
          ws.close()
        }
      })

      ws.on('close', () => resolve())
      ws.on('error', (err: Error) => reject(err))
    })
  }

  generateSpeech().then(() => {
    if (audioChunks.length > 0) {
      const pcm = Buffer.concat(audioChunks)
      fs.writeFileSync('output.pcm', pcm)
      console.log(
        `\nAudio saved to output.pcm (${pcm.length.toLocaleString()} bytes, ${(pcm.length / 48000).toFixed(1)}s at 24kHz)`
      )
      console.log('Play with: ffplay -f s16le -ar 24000 output.pcm')
    } else {
      console.log('No audio received')
    }
  })
  ```
</CodeGroup>

## WebSocket parameters

When establishing a WebSocket connection, you can configure:

| Parameter                | Type    | Description                                                                                                                                                                                               |
| :----------------------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model                    | string  | The TTS model to use                                                                                                                                                                                      |
| voice                    | string  | The voice for generation                                                                                                                                                                                  |
| response\_format         | string  | Audio format: `mp3`, `opus`, `aac`, `flac`, `wav`, or `pcm`                                                                                                                                               |
| speed                    | float   | Playback speed (default: 1.0)                                                                                                                                                                             |
| max\_partial\_length     | integer | Character buffer length before triggering TTS generation                                                                                                                                                  |
| sample\_rate             | integer | The sample rate of the output audio in Hz (e.g., `24000`, `44100`)                                                                                                                                        |
| language                 | string  | The language or locale code for speech synthesis (e.g., `en`, `fr`, `es`). Locales are supported and must be lowercase (e.g., `zh-hk` for Cantonese)                                                      |
| alignment                | string  | Controls word-level timestamp generation. Set to `word` to receive `conversation.item.word_timestamps` events, or `none` to disable (default: `none`)                                                     |
| segment                  | string  | Controls how text is segmented before synthesis. Options: `sentence` (default) splits on sentence boundaries, `immediate` processes text as soon as it arrives, `never` waits until buffer is committed   |
| extra\_params            | object  | Additional model-specific parameters. Supported fields:                                                                                                                                                   |
|     `pronunciation_dict` | array   | A list of pronunciation rules for specific characters or symbols. Each entry uses the format `"<source>/<replacement>"` (e.g., `["omg/oh my god"]`) to override how the model pronounces matching tokens. |

<Note>
  You can pass these query parameters either in the WebSocket URL (e.g., `wss://api.together.ai/v1/audio/speech/websocket?model=hexgrad/Kokoro-82M&voice=af_alloy&sample_rate=24000&alignment=word`) or dynamically via the `tts_session.updated` event after the connection is established.
</Note>

## Multi-context support

You can manage multiple independent TTS streams over a single WebSocket connection using `context_id`. This is useful for applications handling multiple simultaneous conversations or characters.

* Add `context_id` to any client message to route it to a specific context.
* Messages without `context_id` use the `"default"` context.
* Each context maintains its own text buffer and voice settings.
* Cancel a specific context with the `context.cancel` message type.
* Send `tts_session.updated` without a `context_id` to update all contexts at once.
* Maximum 100 contexts per connection.

**Sending text to a specific context:**

```json theme={null}
{
  "type": "input_text_buffer.append",
  "text": "Hello from context one.",
  "context_id": "conversation-1"
}
```

**Cancelling a context:**

```json theme={null}
{
  "type": "context.cancel",
  "context_id": "conversation-1"
}
```

The server confirms cancellation with a `context.cancelled` message:

```json theme={null}
{
  "type": "context.cancelled",
  "context_id": "conversation-1"
}
```

## See also

* [Text-to-speech overview](/docs/inference/text-to-speech/overview) for parameters, response formats, voices, and pricing.
* [Streaming](/docs/inference/text-to-speech/streaming) for HTTP-based streaming and raw byte output.
