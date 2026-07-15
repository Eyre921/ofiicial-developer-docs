---
title: "Voice Agent Integration Patterns"
source: https://developers.deepgram.com/docs/flux-tts/voice-agent.md
path: docs/flux-tts/voice-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Voice Agent Integration Patterns

Flux TTS is built to sit downstream of an LLM in a voice agent pipeline. This guide shows the common integration patterns, pairing Flux TTS's `/v2/speak` with a streaming STT (such as [Flux STT](/docs/flux/quickstart)) and an LLM. Each pattern is intentionally small — drop it into your pipeline and adapt.

For the messages used here, see [Client Messages](/docs/flux-tts/client-messages) and [Server Messages](/docs/flux-tts/server-messages).

The snippets below focus on **message flow** rather than a specific SDK. For the concrete `speak.v2` calls, see [Getting Started](/docs/flux-tts/quickstart) and the [template apps](/docs/flux-tts/template-apps) — the Python (`deepgram-sdk`) and JavaScript (`@deepgram/sdk`) SDKs both ship a `speak.v2` client for `/v2/speak`.

## Pattern 1: Basic agent loop

On each end-of-turn from STT, stream the LLM response into the active turn and flush when the response is complete.

```python
async def agent_loop(stt_conn, speak_conn, llm):
    async for event in stt_conn:
        if event.event == "EndOfTurn":
            async for token in llm.generate_stream(event.transcript):
                await speak_conn.send({"type": "Speak", "text": token})
            await speak_conn.send({"type": "Flush"})
```

**Barge-in / interruption handling is planned for GA.** At Early Access, when the user speaks over the agent, stop local playback and open a new turn with the next `Speak`. Once it ships, `Interrupt` will cancel the active turn and return `text_spoken` / `text_remaining` so you can reconcile LLM context with exactly what the user heard. The split is computed from an **optional playback position** you include — how much of the turn's audio actually played before the barge-in — so it reflects what the user really heard, not just what the server sent. If your client doesn't already track audio-playback position, it's worth wiring up now.

## Streaming text correctly

Streaming text into Flux TTS is mostly about *not* doing extra work — your LLM plumbing almost certainly handles it already:

1. **Keep the whitespace your LLM emits.** Most LLM token streams already include the spaces between tokens; just don't strip them. The one thing to confirm: when you stitch together two *separate* generations (a reply, then a tool-call result, then another reply), keep a space between them — otherwise `"Hello world."` followed by `"How are you?"` becomes `"Hello world.How are you?"`.
2. **Don't chunk or buffer text.** You don't need to detect sentence boundaries or hold text back — the server streams a turn's audio as tokens arrive. Send them as they come and `Flush` only when the agent's response is complete.

## A note on transport

The Flux TTS WebSocket is the **framework-to-Deepgram** leg of your pipeline, not the end-user audio leg. For the user-facing real-time audio path, voice agent frameworks typically use WebRTC. Keep that distinction in mind when reasoning about end-to-end latency: the TTS WebSocket carries the framework-to-Deepgram leg, while stopping audio in the user's ear is always your client's job, done locally.

## Related resources

* [The Speech Lifecycle](/docs/flux-tts/state) — the state machine behind these loops
* [Client Messages](/docs/flux-tts/client-messages) / [Server Messages](/docs/flux-tts/server-messages) — full wire reference
* [Cross-Turn Context](/docs/flux-tts/context) — what persists across turns
* [Build a Flux-enabled Voice Agent (STT)](/docs/flux/agent) — the STT side of the pipeline

***
