---
title: "Flux TTS Overview"
source: https://developers.deepgram.com/docs/flux-tts/overview.md
path: docs/flux-tts/overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux TTS Overview

**Early Access.** Flux TTS and the `/v2/speak` API are in Early Access — the API surface and voice catalog may change before general availability.

Flux TTS brings the Flux promise to speech synthesis: a model and API built for the realities of a voice agent pipeline, not a one-shot text-to-audio pipe. It is served on the `/v2/speak` endpoint and shares one set of Flux voices across two transports.

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

*Planned for GA:* interruption feedback (the server reports exactly what the user heard on barge-in) and mid-stream `Configure` (speed).

## Start here

* [Real-Time Getting Started](/docs/flux-tts/quickstart)
* [Batch (REST) Getting Started](/docs/flux-tts/batch)
* [Batch vs Streaming](/docs/flux-tts/batch-vs-streaming)
* [Build a Flux TTS Voice Agent](/docs/flux-tts/voice-agent)
* [Migrating from Aura](/docs/flux-tts/migrating)

***
