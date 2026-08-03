---
title: "Client Messages"
source: https://developers.deepgram.com/docs/flux-tts/client-messages.md
path: docs/flux-tts/client-messages
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Client Messages

**Early Access.** Flux TTS and the `/v2/speak` API are in Early Access — the API surface and voice catalog may change before general availability.

All client-to-server traffic on `/v2/speak` is JSON text frames. You stream synthesis text with `Speak`, end a turn with `Flush`, and shut down with `Close`. The server replies on a parallel set of [Server Messages](/docs/flux-tts/server-messages).

A **turn** is one complete agent response, bounded by `Flush`. The server streams a turn's audio as text arrives; only `Flush` completes the turn. For how these messages drive turn state, see [The Speech Lifecycle](/docs/flux-tts/state).

**Early Access surface.** At EA the client messages are `Speak`, `Flush`, and `Close`. Interruption (`Interrupt`) and mid-stream configuration (`Configure`) are planned for GA.

## Speak

Send text to be synthesized into the active turn. The `Speak` shape is unchanged from `/v1/speak`. The server tracks the active turn internally and assigns it a **`speech_id`** — a server-generated turn identifier, included in `SpeechStarted` (the start of a turn) and `SpeechMetadata` (the completion of the turn's synthesis). Binary audio frames aren't labeled with the `speech_id`, but all of a turn's audio — and only that turn's audio — arrives between those two messages. Clients do **not** specify one.

```json
{
  "type": "Speak",
  "text": "Sure, I can help you cancel your subscription."
}
```

| Field  | Type      | Required | Description                                                     |
| ------ | --------- | -------- | --------------------------------------------------------------- |
| `type` | `"Speak"` | yes      | Message type identifier.                                        |
| `text` | string    | yes      | Text to synthesize — see [Text handling](#text-handling) below. |

### Streaming LLM tokens

Streaming is just sending `Speak` messages as tokens arrive, then flushing at the end of the turn:

```json
{"type": "Speak", "text": "Sure, "}
{"type": "Speak", "text": "I can "}
{"type": "Speak", "text": "help you "}
{"type": "Speak", "text": "cancel your "}
{"type": "Speak", "text": "subscription."}
{"type": "Flush"}
```

You may send `Speak` at any time. Text sent while the current turn is still generating **appends to that turn**. Once you `Flush`, though, the turn is closed — a later `Speak` starts a **new** turn, which the server queues as *pending* behind any turn still being synthesized. Only `Flush` ends a turn.

### Text handling

Send **plain text**. The server applies text normalization (for example, expanding numbers and dates) before synthesis, but it does not reorder your content or insert or strip whitespace between successive `Speak` messages — so you can stream LLM tokens directly without coordinating chunk boundaries.

**Insert whitespace between distinct generations.** Because the server doesn't add whitespace between `Speak` messages, sending `"Hello world."` immediately followed by `"How are you?"` is processed as `"Hello world.How are you?"`, which can trigger sentence-boundary artifacts. When you concatenate separate LLM responses (a reply, a tool-call result, another reply), insert a single space — or the appropriate separator for non-whitespace languages — between them.

**Markup isn't interpreted.** The model synthesizes plain text; SSML and competitor audio tags aren't supported at EA. Automatic detection and stripping of known markup, with a `Warning`, is planned for GA — until then, send plain text.

## Flush

End the active turn. The server drains the buffer, generates the remaining audio, and reports the turn. `Flush` is how you signal "the agent's response is complete."

```json
{"type": "Flush"}
```

On `Flush`, the server generates any remaining audio for the active turn and emits [`Flushed`](/docs/flux-tts/server-messages#flushed) **when the turn's buffer has actually been flushed** — not on receipt, and it can be held back behind earlier pending turns — followed by [`SpeechMetadata`](/docs/flux-tts/server-messages#speechmetadata) with the turn's billing and timing. The next `Speak` begins a new turn with a new `speech_id`.

**`Flush` is what ends a turn.** The server may already be streaming a turn's audio before you flush, but only `Flush` closes the turn and produces `Flushed` + `SpeechMetadata`. A `Flush` with no active turn is a no-op and produces a `NO_ACTIVE_SPEECH` warning.

## Close

Gracefully close the connection. The server finishes draining all queued audio, emits a final [`SessionMetadata`](/docs/flux-tts/server-messages#sessionmetadata) with cumulative totals, then closes the socket.

```json
{"type": "Close"}
```

## Keeping a session alive

The server closes an idle session after **60 seconds** with no inbound client message ([`NET-0004`](/docs/flux-tts/server-messages#error-codes)). If your agent may go quiet longer than that between turns, send a WebSocket **Ping** or **Pong** to reset the timer.

## Related resources

* [Server Messages](/docs/flux-tts/server-messages) — the responses to everything on this page
* [The Speech Lifecycle](/docs/flux-tts/state) — how these messages drive turn state
* [Build a Flux TTS Voice Agent](/docs/flux-tts/voice-agent) — these messages in a full agent loop
* [Getting Started](/docs/flux-tts/quickstart) — connect and send your first turn

---
