---
title: "Batch vs Streaming: Which Should I Use?"
source: https://developers.deepgram.com/docs/flux-tts/batch-vs-streaming.md
path: docs/flux-tts/batch-vs-streaming
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Batch vs Streaming: Which Should I Use?

**Early Access.** Flux TTS and the `/v2/speak` API are in Early Access — the API surface and voice catalog may change before general availability.

Flux TTS is served on `/v2/speak` over two transports against the same voices. They're not tiers — pick by how the audio is consumed.

## The short answer

* **Building a voice agent or any live, conversational experience?** Use **[streaming](/docs/flux-tts/quickstart)** (WebSocket) — it streams audio as text arrives and keeps prosody consistent across turns.
* **Pre-rendering audio you know up front** (IVR prompts, notifications, audiobook lines)? Use **[batch](/docs/flux-tts/batch)** (REST).

## Side by side

|                                     | Streaming (WebSocket)                                 | Batch (REST)                                                         |
| ----------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- |
| Endpoint                            | `wss://api.deepgram.com/v2/speak`                     | `POST https://api.deepgram.com/v2/speak`                             |
| Input                               | Text streamed in as it's produced (LLM tokens)        | One complete block of text                                           |
| Output                              | Audio streams back incrementally                      | Full audio in one response                                           |
| Time-to-first-byte                  | Low — playback starts before the full response exists | Whole clip generated before you get it                               |
| Interruption / barge-in             | Yes *(planned for GA)*                                | N/A                                                                  |
| Turn lifecycle & cross-turn context | Yes                                                   | N/A (stateless request/response)                                     |
| Mid-stream control                  | `Configure` speed *(planned for GA)*                  | Fixed per request                                                    |
| Encodings                           | Raw `linear16` / `mulaw` / `alaw`                     | Containerized/compressed too: `mp3` (default), `opus`, `flac`, `aac` |
| Operational model                   | Long-lived connection, lifecycle to manage            | Stateless: simple retries, high fan-out                              |

## Choose streaming when

* The text is produced incrementally (you're streaming from an LLM).
* The user may barge in mid-response — when barge-in ships at GA, `Interrupt` will cancel in-flight synthesis and report what they heard.
* You want the lowest possible time-to-first-audio in a back-and-forth conversation.
* You want tone to carry across turns.

## Choose batch when

* The full text is known before you synthesize.
* You're pre-generating reusable assets (prompts, notifications, narration).
* You want a stateless request/response with easy retries and high concurrency, and don't need incremental playback or interruption.

## Related resources

* [Real-Time / Conversational Getting Started](/docs/flux-tts/quickstart)
* [Batch (REST) Getting Started](/docs/flux-tts/batch)
* [Build a Flux TTS Voice Agent](/docs/flux-tts/voice-agent)

***
