---
title: "Real-time audio transcription via WebSocket"
source: https://docs.together.ai/reference/audio-transcriptions-realtime
path: reference/audio-transcriptions-realtime
---

openapi.yaml GET /realtime
Establishes a WebSocket connection for real-time audio transcription. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/realtime) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, input_audio_format)

**Client Events:**
- `input_audio_buffer.append`: Send audio chunks as base64-encoded data
  ```json
  {
    "type": "input_audio_buffer.append",
    "audio": "<base64_encoded_audio_chunk>"
  }
  ```
- `input_audio_buffer.commit`: Signal end of audio stream. When VAD is enabled, the server automatically detects speech boundaries and emits `completed` events. When VAD is disabled, you must send `commit` to trigger transcription of the buffered audio.
  ```json
  {
    "type": "input_audio_buffer.commit"
  }
  ```
- `transcription_session.updated`: Update session configuration, including Voice Activity Detection (VAD) parameters. Send this after receiving `session.created`. Can also be sent at any time during the session to change VAD settings.
  ```json
  {
    "type": "transcription_session.updated",
    "session": {
      "turn_detection": {
        "type": "server_vad",
        "threshold": 0.3,
        "min_silence_duration_ms": 500,
        "min_speech_duration_ms": 250,
        "max_speech_duration_s": 5.0,
        "speech_pad_ms": 250
      }
    }
  }
  ```
  To disable VAD entirely (manual commit mode), set `turn_detection` to `null`:
  ```json
  {
    "type": "transcription_session.updated",
    "session": {
      "turn_detection": null
    }
  }
  ```

**Voice Activity Detection (VAD)**

VAD controls how the server automatically detects speech segments in the audio stream. When enabled (the default), the server uses Silero VAD to identify speech regions and emits transcription events as each segment completes. When disabled, you must manually call `input_audio_buffer.commit` to trigger transcription.

VAD can be configured in two ways:
1. **Query parameters** at connection time: `turn_detection=server_vad&threshold=0.3&min_silence_duration_ms=500`
2. **Session message** after connection: Send `transcription_session.updated` with a `turn_detection` object (see above)

To disable VAD at connection time, use `turn_detection=none` as a query parameter.

**VAD Parameters:**

All parameters are Omitted fields use their defaults.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `type` | string | `server_vad` | VAD mode. Use `server_vad` to enable, or set `turn_detection` to `null` to disable. |
| `threshold` | float | `0.3` | Speech probability threshold (0.0–1.0). Audio frames with probability above this value are classified as speech. Lower values detect more speech but may increase false positives. For low-SNR audio (e.g., 8kHz phone calls), values of 0.01–0.2 may work better. |
| `min_silence_duration_ms` | int | `500` | Minimum silence duration in milliseconds before ending a speech segment. Higher values merge nearby speech bursts into single segments. For phone calls with mid-sentence pauses, 2000–5000ms prevents over-segmentation. |
| `min_speech_duration_ms` | int | `250` | Minimum speech segment duration in milliseconds. Segments shorter than this are discarded. Filters out brief noise bursts or clicks. |
| `max_speech_duration_s` | float | `5.0` | Maximum speech segment duration in seconds. Segments longer than this are force-split at the longest internal silence gap. Useful for continuous speech without natural pauses. |
| `speech_pad_ms` | int | `250` | Padding in milliseconds added to the start and end of each detected segment. Prevents clipping speech edges. When padding would cause adjacent segments to overlap, the gap is split at the midpoint instead. |

**Server Events:**
- `session.created`: Initial session confirmation (sent first)
  ```json
  {
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.session",
      "modalities": ["audio"],
      "model": "openai/whisper-large-v3"
    }
  }
  ```
- `transcription_session.updated`: Confirms session configuration was applied. Sent in response to a client `transcription_session.updated` message.
  ```json
  {
    "type": "transcription_session.updated",
    "session": {
      "turn_detection": {
        "type": "server_vad",
        "threshold": 0.3,
        "min_silence_duration_ms": 500,
        "min_speech_duration_ms": 250,
        "max_speech_duration_s": 5.0,
        "speech_pad_ms": 250
      }
    }
  }
  ```
- `conversation.item.input_audio_transcription.delta`: Partial transcription results
  ```json
  {
    "type": "conversation.item.input_audio_transcription.delta",
    "delta": "The quick brown"
  }
  ```
- `conversation.item.input_audio_transcription.completed`: Final transcription
  ```json
  {
    "type": "conversation.item.input_audio_transcription.completed",
    "transcript": "The quick brown fox jumps over the lazy dog"
  }
  ```
- `conversation.item.input_audio_transcription.failed`: Error occurred
  ```json
  {
    "type": "conversation.item.input_audio_transcription.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
  ```

**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Unsupported audio format errors (400)
