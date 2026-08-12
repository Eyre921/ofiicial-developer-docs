---
title: "Migrating from /v1/speak to Flux TTS"
source: https://developers.deepgram.com/docs/flux-tts/migrating.md
path: docs/flux-tts/migrating
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Migrating from /v1/speak to Flux TTS

Flux TTS ships on a new endpoint, `/v2/speak`. The `/v1/speak` endpoint stays available and unchanged, and all Aura model strings continue to work on it — there is no aliasing, redirect, or deprecation. You migrate when you're ready to build on the streaming-first surface.

## Which should you use?

**Use Flux TTS** for new voice-agent work: streaming LLM output, barge-in, and multi-turn conversations where tone should carry across turns.

**Stay on Aura** if you're using Aura voices. Aura voices are served only on `/v1/speak`; Flux voices only on `/v2/speak` (where a `flux-*` model is required).

## What changes

| Dimension          | `/v1/speak`                              | `/v2/speak` (Flux TTS)                                                                                                 |
| ------------------ | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Mental model       | Text buffer → audio stream               | Streaming-first, turn-based conversation                                                                               |
| Text input         | `Speak` messages into a global buffer    | `Speak` messages; server tracks the active turn and assigns `speech_id` (informational)                                |
| Flushing           | Manual `Flush` + flush toggles           | `Flush` signals no more text is coming for the turn; once its synthesis completes, you get the turn's `SpeechMetadata` |
| Interruption       | `Clear` discards the buffer, no feedback | `Interrupt` with spoken-text feedback (`text_spoken` / `text_remaining`)                                               |
| Context reset      | None (reconnect the WebSocket)           | Not needed — prosody carries across turns automatically (no API surface)                                               |
| Turn metadata      | None                                     | You mark end-of-turn with `Flush` and get per-turn `SpeechMetadata` (billing, timing) back                             |
| Dynamic config     | None (fixed at connection)               | Mid-stream `Configure` for `speed`                                                                                     |
| Cross-turn context | None                                     | Model state persists across turns                                                                                      |

## Migration steps

1. **Change the endpoint.** Point your WebSocket at `/v2/speak` (was `/v1/speak`). The Python (`deepgram-sdk`) and JavaScript (`@deepgram/sdk`) SDKs expose a `speak.v2` client — see [Getting Started](/docs/flux-tts/quickstart) and the [template apps](/docs/flux-tts/template-apps) — or integrate against the WebSocket directly.
2. **Keep your `Speak` messages.** The `Speak` shape is unchanged. Do **not** specify `speech_id` — the server assigns it and returns it for debuggability.
3. **Require a `model`.** `model` is required on every `/v2/speak` connection. Use a Flux TTS voice string (e.g. `flux-haley-en`); Aura voices are served by `/v1/speak`, not `/v2/speak`.
4. **Replace `Clear` with `Interrupt`.** End each turn with `Flush`; on barge-in, send `Interrupt` and use the returned `text_spoken` / `text_remaining` to reconcile your LLM context — see [Interruption Handling](/docs/flux-tts/interrupt-handling).
5. **Treat `Flush` as end-of-turn, and read `SpeechMetadata`.** `Flush` marks the end of a turn (there's no separate `Finalize`). The turn's `SpeechMetadata` reports billing and timing — use it as your end-of-turn signal (not `Flushed`), and drop any client-side character-count or audio-duration tracking.
6. **Drop the flush toggles.** The v1 `flush_send`-style toggles don't exist on v2 — audio starts streaming for a turn on its own, and you `Flush` only to mark the end of the turn.
7. **Drop reconnect-to-reset logic.** Prosody carries across turns automatically; there's no reset step to port.
8. **Insert whitespace between distinct LLM responses.** The server doesn't add whitespace between `Speak` messages — see [Text handling](/docs/flux-tts/client-messages#text-handling).

## Message mapping

The `/v2/speak` column mixes messages you send (`Speak`, `Flush`, `Close`) with messages the server sends back (`Connected`, `Flushed`, `SpeechMetadata`, `SessionMetadata`). See [Client Messages](/docs/flux-tts/client-messages) and [Server Messages](/docs/flux-tts/server-messages) for the full split.

| `/v1/speak`            | `/v2/speak`                                    |
| ---------------------- | ---------------------------------------------- |
| `Speak`                | `Speak` (unchanged)                            |
| `Flush` (buffer flush) | `Flush` (ends the turn)                        |
| `Clear`                | `Interrupt`                                    |
| `Finalize`             | folded into `Flush`                            |
| `Metadata` (on open)   | `Connected`                                    |
| `Flushed` / `Cleared`  | `Flushed`, `SpeechMetadata`, `SessionMetadata` |
| `Close`                | `Close` (+ final `SessionMetadata`)            |

## Behaviors carried forward

* The **`Speak`** message shape is unchanged from v1.
* **1-hour max session duration** carries over from v1. New on v2: a **60s inactivity timeout** (`NET-0004`) — send a WebSocket Ping (or Pong) to keep long-idle sessions alive.

Markup handling carries its own warning codes, and inline pause and pronunciation controls are coming soon — see [Markup handling](/docs/flux-tts/client-messages#markup-handling) and the [warning codes](/docs/flux-tts/server-messages#warning-codes).

## Related resources

* [Getting Started with Flux TTS](/docs/flux-tts/quickstart) — connect and send your first turn
* [Client Messages](/docs/flux-tts/client-messages) / [Server Messages](/docs/flux-tts/server-messages) — full wire reference
* [The Speech Lifecycle](/docs/flux-tts/state) — the turn model that replaces v1's buffer model
* [Aura (/v1/speak) docs](/docs/tts-websocket) — the endpoint you're migrating from

---
