---
title: "Server Messages"
source: https://developers.deepgram.com/docs/flux-tts/server-messages.md
path: docs/flux-tts/server-messages
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Server Messages

**Early Access.** Flux TTS and the `/v2/speak` API are in Early Access — the API surface and voice catalog may change before general availability.

The server replies to your [Client Messages](/docs/flux-tts/client-messages) with JSON text frames interleaved with binary audio frames. This page documents every server-to-client message and the error/warning code reference.

**Early Access surface.** At EA the server emits the events below. Interruption reporting (`SpeechInterrupted`) and configuration responses (`ConfigureSuccess` / `ConfigureFailure`) are planned for GA alongside `Interrupt` and `Configure`.

**Cadence at a glance:** `SpeechStarted` marks the start of a turn and `SpeechMetadata` marks its end — **every audio frame for a turn arrives between the two.** `Flush` is your signal that all of the turn's text has been sent; once it arrives, `SpeechMetadata` is our signal that all of the turn's audio has been sent.

## Connected

Sent immediately on a successful connection. Successor to v1/speak's `Metadata` message.

```json
{
  "type": "Connected",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "model_name": "flux-haley-en",
  "model_version": "2026.06.01",
  "model_uuids": ["b3e47c20-9f81-4a2e-bd15-8d7c6e2a1f09"]
}
```

| Field           | Type                   | Description                                                                                             |
| --------------- | ---------------------- | ------------------------------------------------------------------------------------------------------- |
| `request_id`    | string (UUID)          | ID of the `/v2/speak` request.                                                                          |
| `model_name`    | string                 | Resolved model name (e.g. `flux-haley-en`).                                                             |
| `model_version` | string                 | Resolved model version.                                                                                 |
| `model_uuids`   | array of string (UUID) | Resolved model UUIDs. A list, because a resolved model may be backed by more than one underlying model. |

## SpeechStarted

Emitted at the **start of each new turn**, before audio streaming begins. Carries the server-assigned `speech_id`. Fires **once per turn**.

```json
{
  "type": "SpeechStarted",
  "speech_id": "dg_sp_a1b2c3d4e5f6"
}
```

The `speech_id` is a server-minted identifier of the form `dg_sp_<12 hex digits>`. It is informational — useful for correlating logs.

**When a turn becomes active.** A `Speak` received while idle (the first `Speak`, or the first after a `SpeechMetadata`) starts a new active turn, and we emit `SpeechStarted`. There is only ever **one active turn**: a `Speak` received *after* you've `Flush`ed the active turn but *before* its `SpeechMetadata` starts a **pending** turn. The active turn stays active until its `SpeechMetadata` — if you haven't received `SpeechMetadata`, the turn is still being synthesized — at which point the next pending turn becomes active and gets its own `SpeechStarted`.

## SpeechMetadata

Emitted once per turn, after we've sent **all** of the turn's audio — our signal that synthesis for the turn is complete and no more audio is coming for it. It follows your `Flush`, which tells us no more text is coming for the turn. Reports billing and timing for the completed turn.

```json
{
  "type": "SpeechMetadata",
  "speech_id": "dg_sp_a1b2c3d4e5f6",
  "audio_duration_ms": 3200,
  "input_character_count": 47,
  "billable_character_count": 47,
  "controls_applied": {
    "pronunciations_applied": 0,
    "pronunciation_warnings": 0
  }
}
```

| Field                      | Type    | Description                                                                                                                                                         |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `speech_id`                | string  | Server-assigned turn identifier. Informational.                                                                                                                     |
| `audio_duration_ms`        | integer | Total audio duration produced for this turn, in milliseconds.                                                                                                       |
| `input_character_count`    | integer | Raw input character count for this turn, before text normalization.                                                                                                 |
| `billable_character_count` | integer | Billable character count for this turn — the input minus stripped inline-control characters; always ≤ `input_character_count`.                                      |
| `controls_applied`         | object  | Controls applied during the turn. At Early Access it always reports `pronunciations_applied` and `pronunciation_warnings`, both `0` — these tallies populate at GA. |

**Per-turn vs. cumulative.** Per-turn counts are reported here, once per turn (at `Flush`). Cumulative totals are reported once, at session end, in [`SessionMetadata`](#sessionmetadata) as `total_*`.

## Flushed

Emitted when the turn's buffer has actually been flushed after a manual [`Flush`](/docs/flux-tts/client-messages#flush) — **not** on receipt of the `Flush`, and it can be held back behind earlier pending turns. The turn's `SpeechMetadata` follows.

```json
{
  "type": "Flushed",
  "speech_id": "dg_sp_a1b2c3d4e5f6"
}
```

## SessionMetadata

Final server message before the WebSocket closes. Reports cumulative session totals — the sum across all turns.

```json
{
  "type": "SessionMetadata",
  "total_audio_duration_ms": 184500,
  "total_input_character_count": 4280,
  "total_billable_character_count": 4280
}
```

This is the one place cumulative totals are reported. Combined with the per-turn numbers in `SpeechMetadata`, you get clean reconciliation: per-turn for granular tracking, plus a final authoritative total.

## Warning

Informational message; synthesis continues and the connection is unaffected. Every warning carries a `code` and a human-readable `description`.

```json
{
  "type": "Warning",
  "code": "NO_ACTIVE_SPEECH",
  "description": "There is no active turn. The request will be ignored."
}
```

See the [warning codes](#warning-codes) below. Warnings are not rate-limited — every occurrence is emitted.

## Error

A fatal, server-originated error. Unlike a `Warning`, an `Error` is always followed by a WebSocket close.

```json
{
  "type": "Error",
  "code": "MESSAGE-0000",
  "description": "The message could not be parsed."
}
```

See the [error codes](#error-codes) below.

## Warning codes

All warning codes follow Deepgram's `SCREAMING_SNAKE_CASE` convention; the session stays open in every case.

| Code                 | Trigger                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `NO_ACTIVE_SPEECH`   | A speech-scoped message (e.g. `Flush`) was received with no active turn. No-op.                                                             |
| `SYNTHESIS_RETRYING` | A synthesis request to the model failed and is being retried. The session continues; a fatal `Error` is sent only if retries are exhausted. |

Additional warning codes (pronunciation and inline-control validation, markup stripping) are planned for GA with the features that emit them.

## Error codes

Every error is fatal and is followed by a WebSocket close frame. Codes use Deepgram's `DOMAIN-NNNN` convention.

| Code           | Error                      | Trigger                                                                                                                                          |
| -------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `MESSAGE-0000` | Unparseable client message | A client message could not be parsed.                                                                                                            |
| `DATA-0000`    | Invalid command            | A message contained an invalid command.                                                                                                          |
| `BIG-0000`     | Message too large          | A message was too large to process.                                                                                                              |
| `NET-0000`     | Internal server error      | The server hit an unexpected condition.                                                                                                          |
| `NET-0001`     | Failed to receive message  | The server failed to receive a message.                                                                                                          |
| `NET-0002`     | Failed to send message     | The server failed to send a message. In practice you won't observe this — if the server can't send messages, it can't deliver this error either. |
| `NET-0003`     | Time limit exceeded        | The session time limit (1 hour) was exceeded.                                                                                                    |
| `NET-0004`     | Inactive client            | No client message arrived within the 60s inactivity window; the session was closed. Send a WebSocket Ping or Pong to keep an idle session alive. |

## Related resources

* [Client Messages](/docs/flux-tts/client-messages) — the messages these respond to
* [The Speech Lifecycle](/docs/flux-tts/state) — how these events sequence across a turn
* [Cross-Turn Context](/docs/flux-tts/context) — voice consistency across turns

---
