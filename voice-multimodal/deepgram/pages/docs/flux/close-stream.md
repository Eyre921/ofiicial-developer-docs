---
title: "Close Stream"
source: https://developers.deepgram.com/docs/flux/close-stream.md
path: docs/flux/close-stream
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Close Stream

Streaming:Flux

Use the `CloseStream` message to close the WebSocket stream. Flux decodes the audio it has already received — emitting the corresponding interim `Update` messages — and then closes the connection.

## Purpose

In conversational audio processing, there are scenarios where you need to stop a stream and close the connection. The `CloseStream` message instructs the server to finish decoding the audio it has already received, emit the corresponding `Update` messages, and then terminate the WebSocket connection.

`CloseStream` does not finalize the active turn. No `EndOfTurn` event is emitted, so the last message you receive is an interim `Update`, not a confirmed final transcript — treat the most recent `Update` as the final transcript for the stream. Flux does not emit a summary metadata object, and the server closes the connection without sending a WebSocket close status code.

## Example Payloads

To send the `CloseStream` message, you need to send the following JSON message to the server:

```json JSON
{
  "type": "CloseStream"
}
```

Upon receiving `CloseStream`, the server emits `Update` messages for any audio it has already received, then closes the connection. A representative interim `Update`:

```json JSON
{
"type": "TurnInfo",         // Message type
"request_id": "uuid",       // Unique identifier of the request (UUID format)
"sequence_id": 0,           // Message sequence number, starts at 0 and increments for each server message
"event": "Update",          // Interim result — CloseStream does not emit an EndOfTurn
"turn_index": 0,            // The index of the current turn
"audio_window_start": 0.0,  // Start time in seconds of the transcribed audio range
"audio_window_end": 0.0,    // End time in seconds of the transcribed audio range
"transcript": "string",     // Interim transcript — treat the latest as final
"words": [...],             // Array of word objects
"end_of_turn_confidence": 0.0 // Confidence score 0-1
}
```

## Related Resources

* [Configure](/docs/flux/configure) - Update stream configuration mid-stream
* [Force End Turn](/docs/flux/force-end-turn) - End the current turn immediately from an external signal
* [Getting Started with Flux](/docs/flux/quickstart) - Quickstart guide with basic configuration

---
