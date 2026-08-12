---
title: "Flux TTS Overview"
source: https://developers.deepgram.com/docs/flux-tts/overview.md
path: docs/flux-tts/overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux TTS Overview

Flux TTS brings the Flux promise to speech synthesis: a model and API built for the realities of a voice agent pipeline, not a one-shot text-to-audio pipe. It is served on the `/v2/speak` endpoint and shares one set of Flux voices across two transports. When a user barges in, `Interrupt` reports exactly what they heard (`text_spoken`) — the hard part of agent state reconciliation, answered by the API instead of reconstructed by hand.

## Two transports, one voice family

| Transport                                  | Endpoint                                 | Best for                                                                                                        |
| ------------------------------------------ | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Real-time / conversational** (WebSocket) | `wss://api.deepgram.com/v2/speak`        | Live voice agents: stream LLM tokens in, stream audio back, interrupt and resume across turns                   |
| **Batch / pre-recorded** (REST)            | `POST https://api.deepgram.com/v2/speak` | Pre-generating fixed audio (IVR prompts, notifications, audiobook lines) where the whole text is known up front |

Not sure which to use? See [Batch vs Streaming](/docs/flux-tts/batch-vs-streaming).

## Why Flux TTS

* **Streaming-first** — Stream LLM tokens straight into the socket; the server places flush boundaries internally.
* **Turn-based lifecycle** — Each agent response is a turn with a clean start/finish, reported per turn.
* **Cross-turn voice consistency** — Conversational state persists across turns, so tone carries forward. See [Cross-Turn Context](/docs/flux-tts/context).

On barge-in, `Interrupt` reports exactly what the user heard, and mid-stream `Configure` adjusts speed without reconnecting.

## Start here

* [Real-Time Getting Started](/docs/flux-tts/quickstart)
* [Batch (REST) Getting Started](/docs/flux-tts/batch)
* [Batch vs Streaming](/docs/flux-tts/batch-vs-streaming)
* [Build a Flux TTS Voice Agent](/docs/flux-tts/voice-agent)
* [Migrating from Aura](/docs/flux-tts/migrating)

---
