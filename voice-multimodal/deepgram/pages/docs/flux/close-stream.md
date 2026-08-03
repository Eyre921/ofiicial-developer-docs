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

Use the `CloseStream` message to close the WebSocket stream. This forces the server to immediately process any unprocessed audio data and return the final transcription results.

## Purpose

In conversational audio processing, there are scenarios where you may need to force the server to close. Deepgram supports a `CloseStream` message to handle such situations. This message will send a shutdown command to the server instructing it to finish processing any cached data, send the response to the client, send a summary metadata object, and then terminate the WebSocket connection.

## Example Payloads

To send the `CloseStream` message, you need to send the following JSON message to the server:

```json JSON
{
  "type": "CloseStream"
}
```

Upon receiving the `CloseStream` message, the server will process all remaining audio data and return the following:

```json JSON
{
"type": "TurnInfo",         // Message type
"request_id": "uuid",       // Unique identifier of the request (UUID format)
"sequence_id": 0,           // Message sequence number, starts at 0 and increments for each server message
"event": "Update|StartOfTurn|EagerEndOfTurn|TurnResumed|EndOfTurn", // Event type enum
"turn_index": 0,            // The index of the current turn
"audio_window_start": 0.0,  // Start time in seconds of the transcribed audio range
"audio_window_end": 0.0,    // End time in seconds of the transcribed audio range
"transcript": "string",     // Current turn transcript
"words": [...],             // Array of word objects
"end_of_turn_confidence": 0.0 // Confidence score 0-1
}
```

## Related Resources

* [Configure](/docs/flux/configure) - Update stream configuration mid-stream
* [Getting Started with Flux](/docs/flux/quickstart) - Quickstart guide with basic configuration

---
