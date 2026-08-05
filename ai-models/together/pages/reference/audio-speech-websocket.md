---
title: "Create realtime text-to-speech"
source: https://docs.together.ai/reference/audio-speech-websocket
path: reference/audio-speech-websocket
---

openapi.yaml GET /audio/speech/websocket
Establishes a WebSocket connection for real-time text-to-speech generation. This endpoint uses WebSocket protocol (wss://api.together.ai/v1/audio/speech/websocket) for bidirectional streaming communication.

**Connection Setup:**
- Protocol: WebSocket (wss://)
- Authentication: Pass API key as Bearer token in Authorization header
- Parameters: Sent as query parameters (model, voice, max_partial_length, language)

**Client Events:**
- `tts_session.updated`: Update session parameters like voice. The `session` object also accepts an `extra_params` field for additional model-specific parameters that fine-tune speech generation behavior, such as `pronunciation_dict` (a list of pronunciation rules for specific characters or symbols, where each entry uses the format `"<source>/<replacement>"` (e.g., `["omg/oh my god"]`) to override how the model pronounces matching tokens).
  ```json
  {
    "type": "tts_session.updated",
    "session": {
      "voice": "tara",
      "extra_params": {
        "pronunciation_dict": ["omg/oh my god"]
      }
    }
  }
  ```
- `input_text_buffer.append`: Send text chunks for TTS generation
  ```json
  {
    "type": "input_text_buffer.append",
    "text": "Hello, this is a test."
  }
  ```
- `input_text_buffer.clear`: Clear the buffered text
  ```json
  {
    "type": "input_text_buffer.clear"
  }
  ```
- `input_text_buffer.commit`: Signal end of text input and process remaining text
  ```json
  {
    "type": "input_text_buffer.commit"
  }
  ```

**Server Events:**
- `session.created`: Initial session confirmation (sent first)
  ```json
  {
    "event_id": "evt_123456",
    "type": "session.created",
    "session": {
      "id": "session-id",
      "object": "realtime.tts.session",
      "modalities": ["text", "audio"],
      "model": "hexgrad/Kokoro-82M",
      "voice": "tara"
    }
  }
  ```
- `conversation.item.input_text.received`: Acknowledgment that text was received
  ```json
  {
    "type": "conversation.item.input_text.received",
    "text": "Hello, this is a test."
  }
  ```
- `conversation.item.audio_output.delta`: Audio chunks as base64-encoded data
  ```json
  {
    "type": "conversation.item.audio_output.delta",
    "item_id": "tts_1",
    "delta": "<base64_encoded_audio_chunk>"
  }
  ```
- `conversation.item.audio_output.done`: Audio generation complete for an item
  ```json
  {
    "type": "conversation.item.audio_output.done",
    "item_id": "tts_1"
  }
  ```
- `conversation.item.tts.failed`: Error occurred
  ```json
  {
    "type": "conversation.item.tts.failed",
    "error": {
      "message": "Error description",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  }
  ```

**Text Processing:**
- Partial text (no sentence ending) is held in buffer until:
  - We believe that the text is complete enough to be processed for TTS generation
  - The partial text exceeds `max_partial_length` characters (default: 250)
  - The `input_text_buffer.commit` event is received

**Audio Format:**
- Format: Raw PCM (s16le, mono)
- Sample Rate: 24000 Hz
- Encoding: Base64 (per delta event)
- Delivered via `conversation.item.audio_output.delta` events

**Error Codes:**
- `invalid_api_key`: Invalid API key provided (401)
- `missing_api_key`: Authorization header missing (401)
- `model_not_available`: Invalid or unavailable model (400)
- Invalid text format errors (400)


## Multi-context support

All client and server message types support an optional `context_id` field. This allows you to manage multiple independent TTS streams over a single WebSocket connection.

| Field        | Type   | Required | Description                                                                                                                                                  |
| :----------- | :----- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `context_id` | string | No       | Identifies which context this message applies to. Defaults to `"default"` if omitted. For `tts_session.updated`, omitting `context_id` updates all contexts. |

### Additional client message types

**`context.cancel`:** Cancel and clean up a specific context.

```json theme={null}
{
  "type": "context.cancel",
  "context_id": "conversation-1"
}
```

### Additional server message types

**`context.cancelled`:** Confirms a context was cancelled.

```json theme={null}
{
  "type": "context.cancelled",
  "context_id": "conversation-1"
}
```
