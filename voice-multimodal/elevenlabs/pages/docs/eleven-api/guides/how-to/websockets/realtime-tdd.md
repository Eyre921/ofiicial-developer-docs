---
title: "Stream dialogue in real-time"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd.md
path: docs/eleven-api/guides/how-to/websockets/realtime-tdd
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Stream dialogue in real-time

The Text to Dialogue WebSocket (`/v1/text-to-dialogue/stream-input`) keeps a single connection open while you send dialogue lines and receive base64-encoded audio chunks. It is intended for **Eleven v3** dialogue models only (`model_id` must start with `eleven_v3`).

This guide covers the **Text to Dialogue** WebSocket. For **Flash**, **Multilingual v2**, or other
non-v3 TTS models, use the [Realtime TTS
WebSocket](/docs/eleven-api/guides/how-to/websockets/realtime-tts). For a side-by-side summary of
both protocols, see [Text to Speech vs Text to Dialogue
WebSockets](/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets).

## Requirements

* An ElevenLabs account with an API key ([authentication](/docs/api-reference/authentication)).
* The API key must have `Text to Speech` permissions.
* Python or Node.js installed on your machine.

## Setup

```python Python
pip install python-dotenv websockets
```

```typescript TypeScript
npm install dotenv ws
npm install @types/dotenv @types/ws --save-dev
```

Create a `.env` file:

```bash .env
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

Pick a **voice ID** from the [Voice Library](https://elevenlabs.io/voice-library). The examples below use `eleven_v3_conversational`, which allows **one** registered voice per connection.

## Open the WebSocket

Connect to `wss://api.elevenlabs.io/v1/text-to-dialogue/stream-input` with query parameters such as `model_id` and `output_format`. You can send the API key in the `xi-api-key` header or in the first JSON message (shown here in the body for a single pattern across languages).

```python text-to-dialogue-websocket.py
import asyncio
import base64
import json
import os

from dotenv import load_dotenv
import websockets

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
MODEL_ID = "eleven_v3_conversational"

URI = (
    "wss://api.elevenlabs.io/v1/text-to-dialogue/stream-input"
    f"?model_id={MODEL_ID}&output_format=mp3_44100_128"
)
```

```typescript text-to-dialogue-websocket.ts
import * as dotenv from "dotenv";
import * as fs from "node:fs";
import WebSocket from "ws";

dotenv.config();
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
const voiceId = "21m00Tcm4TlvDq8ikWAM";
const modelId = "eleven_v3_conversational";

const uri = `wss://api.elevenlabs.io/v1/text-to-dialogue/stream-input?model_id=${modelId}&output_format=mp3_44100_128`;
const websocket = new WebSocket(uri);

const outputDir = "./output";
try {
  fs.accessSync(outputDir, fs.constants.R_OK | fs.constants.W_OK);
} catch {
  fs.mkdirSync(outputDir);
}
const writeStream = fs.createWriteStream(`${outputDir}/dialogue-ws.mp3`, { flags: "a" });
```

## Register voices and stream text

Send a **first message** that includes `voices` (required) and `xi_api_key` if you did not set the `xi-api-key` header. Then send one or more frames with `inputs`: each item has `text`, `voice_id`, and optional `new_turn`.

The server buffers text until it has enough context (about **40 characters** and **8 words**), then emits `audio` chunks. Response fields use **snake\_case** (for example `is_final`).

```python text-to-dialogue-websocket.py
async def stream_dialogue():
    async with websockets.connect(URI) as websocket:
        await websocket.send(
            json.dumps(
                {
                    "voices": [VOICE_ID],
                    "xi_api_key": ELEVENLABS_API_KEY,
                }
            )
        )

        line = (
            "This is a longer line of dialogue used to exceed the minimum buffer so the model "
            "starts generating streamed audio for the registered voice. "
        )
        await websocket.send(
            json.dumps(
                {
                    "inputs": [
                        {"text": line, "voice_id": VOICE_ID, "new_turn": False},
                    ],
                }
            )
        )

        await websocket.send(json.dumps({"close_socket": True}))

        os.makedirs("output", exist_ok=True)
        out_path = "output/dialogue-ws.mp3"
        with open(out_path, "wb") as audio_file:
            while True:
                raw = await websocket.recv()
                msg = json.loads(raw)
                if msg.get("error"):
                    raise RuntimeError(msg)
                if msg.get("audio"):
                    audio_file.write(base64.b64decode(msg["audio"]))
                if msg.get("is_final"):
                    break
        print(f"Wrote {out_path}")


asyncio.run(stream_dialogue())
```

```typescript text-to-dialogue-websocket.ts
websocket.on("open", () => {
  websocket.send(
    JSON.stringify({
      voices: [voiceId],
      xi_api_key: ELEVENLABS_API_KEY,
    })
  );

  const line =
    "This is a longer line of dialogue used to exceed the minimum buffer so the model starts generating streamed audio for the registered voice. ";

  websocket.send(
    JSON.stringify({
      inputs: [{ text: line, voice_id: voiceId, new_turn: false }],
    })
  );

  websocket.send(JSON.stringify({ close_socket: true }));
});

websocket.on("message", (data) => {
  const msg = JSON.parse(data.toString());
  if (msg.error) {
    console.error(msg);
    return;
  }
  if (msg.audio) {
    writeToLocal(msg.audio, writeStream);
  }
});

function writeToLocal(base64str: string, stream: fs.WriteStream) {
  stream.write(Buffer.from(base64str, "base64"));
}

websocket.on("close", () => {
  writeStream.end();
});
```

`close_socket` flushes any buffered text, sends remaining audio, then a final frame with `is_final: true` before the connection closes. To **keep the connection open** between lines, omit `close_socket` until the session ends; use `flush` to force audio for shorter buffers without closing.

## Run the script

```python Python
python text-to-dialogue-websocket.py
```

```typescript TypeScript
npx tsx text-to-dialogue-websocket.ts
```

You should get an MP3 file under `output/` (filename as in the example above).

## Behaviour notes

### Buffering

Unlike the TTS WebSocket `chunk_length_schedule`, dialogue streaming uses a **fixed server threshold** (character and word count) before the first partial audio. If you send short lines and hear delays, batch slightly more text per `inputs` frame or send `flush: true` to force generation without closing the socket.

### Turns and voices

Set `new_turn: true` when a speaker finishes a turn so prosody resets cleanly. Changing `voice_id` between `inputs` entries also starts a new turn. With `eleven_v3_conversational`, register **exactly one** voice in `voices`; `eleven_v3` supports up to **10** registered voices.

### Inactivity

If the server receives **no client message for 20 seconds**, the connection ends. Send `{"keep_alive": true}` to reset the timer without synthesizing audio.

### Alignment

Add `sync_alignment=true` to the query string to receive `alignment` objects (snake\_case timing arrays) on chunks when available. See the [API reference](/docs/api-reference/text-to-dialogue/ttd-websocket).

## Next steps

#### [TTS vs TTD WebSockets](/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets)

Choose the right WebSocket and compare message shapes.

#### [Text to Dialogue WebSocket (API)](/docs/api-reference/text-to-dialogue/ttd-websocket)

Query parameters, message schemas, and examples.

#### [Stream dialogue (HTTP)](/docs/api-reference/text-to-dialogue/stream)

When full request text is available without a WebSocket.

#### [Realtime TTS WebSocket](/docs/eleven-api/guides/how-to/websockets/realtime-tts)

Single-voice non-v3 streaming over WebSockets.
