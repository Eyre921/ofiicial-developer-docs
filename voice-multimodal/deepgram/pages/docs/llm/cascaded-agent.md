---
title: "Build a cascaded agent"
source: https://developers.deepgram.com/docs/llm/cascaded-agent.md
path: docs/llm/cascaded-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a cascaded agent

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

A cascaded agent runs three stages in sequence: speech-to-text, an LLM, and text-to-speech. This guide uses [Flux STT](/docs/flux/agent) to detect end of turn, Think-Fast to generate the reply, and [Flux TTS](/docs/flux-tts/voice-agent) to speak it. Each pattern is small, so you can drop it into your own pipeline.

> **Info**
>
> The snippets focus on message flow rather than a specific SDK. For the STT and TTS connection code, see the [Flux STT quickstart](/docs/flux/quickstart) and the [Flux TTS quickstart](/docs/flux-tts/quickstart).

## Stream tokens from Think-Fast

Request a streamed response and yield each token as it arrives. The function raises an error if the stream ends without `[DONE]`, because a missing `[DONE]` means the response was cut off.

```python
import json
import os

import httpx

THINK_URL = "https://agent.deepgram.com/v1/think"


async def think_stream(http: httpx.AsyncClient, messages: list[dict]):
    # Ask for a streamed response; streaming requires include_usage.
    payload = {
        "model": "think-fast",
        "messages": messages,
        "stream": True,
        "stream_options": {"include_usage": True},
    }
    headers = {"Authorization": f"Token {os.environ['DEEPGRAM_API_KEY']}"}

    done = False
    async with http.stream("POST", THINK_URL, json=payload, headers=headers) as response:
        # Fail fast on a 4xx or 5xx before reading the stream.
        response.raise_for_status()
        async for line in response.aiter_lines():
            # Each server-sent event arrives as a "data: " line; skip blank separators.
            if not line.startswith("data: "):
                continue
            data = line.removeprefix("data: ")
            if data == "[DONE]":
                done = True
                break
            # Yield each token; the final usage chunk has no choices.
            chunk = json.loads(data)
            for choice in chunk["choices"]:
                token = choice["delta"].get("content")
                if token:
                    yield token

    # A stream without [DONE] was cut off; treat it as a failure.
    if not done:
        raise RuntimeError("Think stream ended without [DONE]")
```

## The agent loop

The agent keeps the conversation history and runs each reply in its own task, so a barge-in can cancel it. Before streaming, the agent adds an empty assistant message to the history. That message fills in as tokens arrive, and a barge-in can later replace it with what the caller actually heard. Route Flux STT events to `run`, and `SpeechInterrupted` messages from your Flux TTS receive loop to `on_speech_interrupted`.

```python
import asyncio

SYSTEM_PROMPT = "You are a friendly voice agent. Reply in one or two short sentences."


class Agent:
    def __init__(self, speak_conn, http, playback):
        self.speak_conn = speak_conn  # Flux TTS WebSocket
        self.http = http  # httpx.AsyncClient
        self.playback = playback  # your audio player
        self.history = [{"role": "system", "content": SYSTEM_PROMPT}]
        self.reply_task = None

    async def on_end_of_turn(self, transcript):
        # Record what the caller said.
        self.history.append({"role": "user", "content": transcript})
        reply = {"role": "assistant", "content": ""}
        self.history.append(reply)
        # Send everything except the empty reply placeholder.
        self.reply_task = asyncio.create_task(self.speak_reply(self.history[:-1], reply))

    async def speak_reply(self, messages, reply):
        # Stream tokens from Think-Fast straight into Flux TTS, keeping a copy in the history.
        async for token in think_stream(self.http, messages):
            reply["content"] += token
            await self.speak_conn.send({"type": "Speak", "text": token})
        # The reply is complete: tell Flux TTS to finish the turn.
        await self.speak_conn.send({"type": "Flush"})

    async def on_start_of_turn(self):
        # The caller started talking. Stop generating first, even if no audio has played yet.
        generating = self.reply_task is not None and not self.reply_task.done()
        if generating:
            self.reply_task.cancel()
        playing = self.playback.is_playing()
        if not generating and not playing:
            return
        # Stop local playback and drop any queued audio for this reply.
        self.playback.stop()
        interrupt = {"type": "Interrupt"}
        if playing:
            # ms of audio played since the start of the session, not the turn
            interrupt["playback_offset"] = {"type": "time_ms", "value": self.playback.session_offset_ms()}
        else:
            # Nothing was heard, so clear the reply now.
            self.history[-1]["content"] = ""
        # Interrupt stops Flux TTS from synthesizing tokens it already received.
        await self.speak_conn.send(interrupt)

    def on_speech_interrupted(self, message):
        # Call this from your Flux TTS receive loop on a SpeechInterrupted message.
        if self.history[-1]["role"] == "assistant":
            self.history[-1]["content"] = message.get("text_spoken", "")


async def run(stt_conn, agent):
    # Route Flux STT turn events to the agent.
    async for event in stt_conn:
        if event.event == "StartOfTurn":
            await agent.on_start_of_turn()
        elif event.event == "EndOfTurn":
            await agent.on_end_of_turn(event.transcript)
```

Send tokens to Flux TTS as they arrive. Keep the whitespace in each token, and skip sentence chunking: Flux TTS streams audio as text comes in.

## Handle barge-in

When the caller starts talking over the agent:

1. Cancel the reply task, so Think-Fast stops generating. Do this even when no audio has played yet.
2. Stop playback locally.
3. Send `Interrupt` to Flux TTS so it stops synthesizing the tokens it already received. If audio was playing, include `playback_offset`. Flux TTS returns `text_spoken` in `SpeechInterrupted` only when `Interrupt` includes `playback_offset`.
4. When `SpeechInterrupted` arrives, replace the assistant message with `text_spoken`.

Without step 4, the next request tells the model it said things the caller never heard.

`on_start_of_turn` and `on_speech_interrupted` in the `Agent` class above implement these steps.

See [Interruption Handling](/docs/flux-tts/interrupt-handling) for how to track the playback offset and discard in-flight audio.

## Add function calling

To let the agent take actions, pass `tools` in the request and handle `tool_calls` before you speak. See [Function calling](/docs/llm/request-response-format#function-calling).

## Related resources

* [Request and response format](/docs/llm/request-response-format): every field `/v1/think` accepts
* [Build a Flux-enabled Voice Agent](/docs/flux/agent): the STT side of the pipeline
* [Voice Agent Integration Patterns](/docs/flux-tts/voice-agent): the TTS side of the pipeline
* [Prompting Deepgram LLMs](/docs/llm/prompting): system prompts for Think-Fast
