---
title: "Voice activity detection"
source: https://docs.together.ai/docs/inference/transcription/voice-activity-detection
path: docs/inference/transcription/voice-activity-detection
---

Configure voice activity detection to control how speech segments are detected in real-time transcription.

Together AI's real-time transcription API uses Voice Activity Detection (VAD) to automatically identify speech segments in an audio stream. While speech is ongoing, the server streams partial transcriptions as `delta` events. When VAD detects enough silence, the segment ends and the server emits a final `completed` event with the full transcript.

VAD runs a dedicated model on the server to compute a speech probability for each audio frame. Frames above a configurable threshold are classified as speech, and the resulting speech regions are grouped into segments based on silence gaps, minimum durations, and padding.

## Parameters

All VAD parameters are optional. If omitted, the server uses sensible defaults tuned for conversational audio.

| Parameter                 | Type  | Default | Description                                                                                                                                                                            |
| ------------------------- | ----- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `threshold`               | float | `0.3`   | Speech probability threshold (0.0–1.0). Frames above this value are classified as speech. Lower values detect more speech but may increase false positives.                            |
| `min_silence_duration_ms` | int   | `500`   | How long silence must last (in ms) before a speech segment ends. Higher values prevent splitting on brief pauses.                                                                      |
| `min_speech_duration_ms`  | int   | `250`   | Minimum segment length in ms. Segments shorter than this are discarded, useful for filtering noise bursts.                                                                             |
| `max_speech_duration_s`   | float | `5.0`   | Maximum segment length in seconds. Longer segments are split at the best internal silence point.                                                                                       |
| `speech_pad_ms`           | int   | `250`   | Padding added to the start and end of each segment. Prevents clipping speech edges. Adjacent segments never overlap; if padding would cause overlap, the gap is split at the midpoint. |

## Common configurations

### Conversational audio (default)

The defaults work well for typical voice assistant and conversational use cases: clean microphone audio at 16kHz with turn-taking between speakers.

```json theme={null}
{
  "type": "server_vad",
  "threshold": 0.3,
  "min_silence_duration_ms": 500,
  "min_speech_duration_ms": 250,
  "max_speech_duration_s": 5.0,
  "speech_pad_ms": 250
}
```

### Phone calls and low-quality audio

Phone audio (8kHz, low SNR) produces lower speech probabilities, so a much lower threshold is needed. Higher `min_silence_duration_ms` prevents splitting mid-sentence pauses common in call center recordings. A higher `max_speech_duration_s` allows longer uninterrupted turns.

```json theme={null}
{
  "type": "server_vad",
  "threshold": 0.01,
  "min_silence_duration_ms": 1000,
  "min_speech_duration_ms": 500,
  "max_speech_duration_s": 60,
  "speech_pad_ms": 10
}
```

## Configure VAD

You can configure VAD in two ways:

### Query parameters at connection time

Pass VAD parameters directly in the WebSocket URL:

```
wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000&threshold=0.01&min_silence_duration_ms=1000
```

To disable VAD entirely, use `turn_detection=none`:

```
wss://api.together.ai/v1/realtime?model=openai/whisper-large-v3&input_audio_format=pcm_s16le_16000&turn_detection=none
```

### Session message after connection

Send a `transcription_session.updated` message after receiving `session.created`:

```json theme={null}
{
  "type": "transcription_session.updated",
  "session": {
    "turn_detection": {
      "type": "server_vad",
      "threshold": 0.01,
      "min_silence_duration_ms": 1000,
      "min_speech_duration_ms": 500,
      "max_speech_duration_s": 60,
      "speech_pad_ms": 10
    }
  }
}
```

To disable VAD via session message, set `turn_detection` to `null`:

```json theme={null}
{
  "type": "transcription_session.updated",
  "session": {
    "turn_detection": null
  }
}
```

## Disable VAD

With VAD disabled, the server does not automatically segment audio. No `completed` events are emitted until you explicitly send an `input_audio_buffer.commit` message, at which point the entire buffered audio is transcribed. This is useful when your application controls segmentation externally.

## Example: real-time transcription with custom VAD

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import base64
  import json
  import os

  import websockets

  API_KEY = os.environ["TOGETHER_API_KEY"]
  MODEL = "openai/whisper-large-v3"

  VAD_CONFIG = {
      "type": "server_vad",
      "threshold": 0.3,
      "min_silence_duration_ms": 500,
      "min_speech_duration_ms": 250,
      "max_speech_duration_s": 5.0,
      "speech_pad_ms": 250,
  }


  async def transcribe():
      url = f"wss://api.together.ai/v1/realtime?model={MODEL}&input_audio_format=pcm_s16le_16000"
      headers = {"Authorization": f"Bearer {API_KEY}"}

      async with websockets.connect(url, additional_headers=headers) as ws:
          # Wait for session.created, then send VAD config
          msg = json.loads(await ws.recv())
          if msg["type"] == "session.created":
              await ws.send(
                  json.dumps(
                      {
                          "type": "transcription_session.updated",
                          "session": {"turn_detection": VAD_CONFIG},
                      }
                  )
              )

          # Send audio in 100ms chunks at real-time pace
          with open("audio.wav", "rb") as f:
              audio = f.read()

          CHUNK = 3200  # 100ms at 16kHz 16-bit
          for i in range(0, len(audio), CHUNK):
              await ws.send(
                  json.dumps(
                      {
                          "type": "input_audio_buffer.append",
                          "audio": base64.b64encode(
                              audio[i : i + CHUNK]
                          ).decode(),
                      }
                  )
              )
              await asyncio.sleep(0.1)

          await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

          # Receive transcription results
          async for message in ws:
              data = json.loads(message)
              if (
                  data["type"]
                  == "conversation.item.input_audio_transcription.completed"
              ):
                  print(data["transcript"])
              elif (
                  data["type"]
                  == "conversation.item.input_audio_transcription.failed"
              ):
                  print(f"Error: {data['error']['message']}")
                  break


  asyncio.run(transcribe())
  ```

  ```javascript JavaScript theme={null}
  import WebSocket from "ws";
  import fs from "fs";

  const API_KEY = process.env.TOGETHER_API_KEY;
  const MODEL = "openai/whisper-large-v3";

  const VAD_CONFIG = {
    type: "server_vad",
    threshold: 0.3,
    min_silence_duration_ms: 500,
    min_speech_duration_ms: 250,
    max_speech_duration_s: 5.0,
    speech_pad_ms: 250,
  };

  const url = `wss://api.together.ai/v1/realtime?model=${MODEL}&input_audio_format=pcm_s16le_16000`;
  const ws = new WebSocket(url, {
    headers: { Authorization: `Bearer ${API_KEY}` },
  });

  ws.on("open", () => console.log("Connected"));

  ws.on("message", (raw) => {
    const data = JSON.parse(raw);

    if (data.type === "session.created") {
      // Send VAD config
      ws.send(JSON.stringify({
        type: "transcription_session.updated",
        session: { turn_detection: VAD_CONFIG },
      }));

      // Send audio in 100ms chunks at real-time pace
      const audio = fs.readFileSync("audio.wav");
      const CHUNK = 3200; // 100ms at 16kHz 16-bit
      let i = 0;
      const interval = setInterval(() => {
        if (i < audio.length) {
          ws.send(JSON.stringify({
            type: "input_audio_buffer.append",
            audio: audio.subarray(i, i + CHUNK).toString("base64"),
          }));
          i += CHUNK;
        } else {
          clearInterval(interval);
          ws.send(JSON.stringify({ type: "input_audio_buffer.commit" }));
        }
      }, 100);
    }

    if (data.type === "conversation.item.input_audio_transcription.completed") {
      console.log(data.transcript);
    }

    if (data.type === "conversation.item.input_audio_transcription.failed") {
      console.error("Error:", data.error.message);
      ws.close();
    }
  });
  ```
</CodeGroup>

## Next steps

* See [Streaming transcription](/docs/inference/transcription/streaming) for the full real-time streaming guide.
* See the [API reference](/reference/audio-transcriptions-realtime) for the complete WebSocket endpoint specification.
