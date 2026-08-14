---
title: "Architecture Overview"
source: https://developers.deepgram.com/docs/voice-agent-architecture.md
path: docs/voice-agent-architecture
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Architecture Overview

Building a voice agent usually means stitching together a speech-to-text service, an LLM, a text-to-speech service, and a pile of glue code to manage turn-taking, interruptions, and audio streaming between them. Each hop adds latency, failure modes, and conversational state you have to track yourself.

Deepgram's Voice Agent API collapses that stack into a **single, unified API**. You open one WebSocket connection, send audio in, and receive audio out. Deepgram runs the full speech loop — speech-to-text, LLM orchestration, and text-to-speech — and handles the hard real-time problems (end-of-turn detection, interruption handling, function calling) natively. You spend your engineering time on what your agent *does*, not on how it hears or talks.

![Unified speech-to-speech Voice Agent API architecture. A customer's audio, including telephony, streams to and from the Voice Agent API. Inside the API, speech-to-text (Deepgram Flux or Nova-3) leads to an LLM (managed, BYO, or custom), which leads to text-to-speech (Deepgram Aura-2, managed, or BYO). End-of-thought detection, interruption handling, and function calling are built in. The API connects to external systems including databases, an embedding model, and a retrieval API.](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/312bf9bf3b58bca3cec4d9380f4182ac1836edef65788a972246bdd1890d57bd/images/voice-agent-architecture.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260814%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260814T100435Z&X-Amz-Expires=604800&X-Amz-Signature=f336b4f236cb4dba95ef3f152462e0cfad08439c8f96375be64efc42a3674583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## One connection, the whole loop

A voice conversation is a loop: the user speaks, the agent understands, decides what to say, and speaks back — over and over, in real time. The Voice Agent API owns that entire loop so you don't have to coordinate it across services.

Audio streams in from any source — a browser, a mobile app, or a phone call over your telephony provider. Deepgram transcribes it, passes the text to the language model, converts the model's reply back to speech, and streams the audio out. Because all three stages live behind one API, the handoffs happen in-process: there are no extra network round trips between transcription, reasoning, and synthesis, which is what keeps responses fast enough to feel like a real conversation.

## What the API handles for you

Each stage of the loop is a component you configure, not infrastructure you build.

* [**Speech-to-Text**](/docs/voice-agent-stt-models): Real-time transcription with Deepgram Flux or Nova-3. Flux is purpose-built for conversation, with a turn-aware model that signals start-of-turn and end-of-turn directly from the audio.
* [**LLM**](/docs/voice-agent-llm-models): Use a Deepgram-managed model, bring your own provider, or point at a custom endpoint. The model can call functions and reach your external systems mid-conversation.
* [**Text-to-Speech**](/docs/voice-agent-tts-models): Natural, low-latency voices with Deepgram Aura-2, or bring your own TTS provider.

Beyond the three stages, the conversational hard parts are built in:

* **End-of-turn detection** — the agent knows when the user has actually finished a thought, not just paused, so it can respond promptly without talking over them. This comes from Flux's turn model rather than a bolted-on voice-activity detector. See [Understanding the Flux State Machine](/docs/flux/state).
* **Interruption handling (barge-in)** — when the user starts speaking while the agent is talking, the agent stops and listens, the way a person would.
* **Function calling** — the LLM can call external tools and APIs in the middle of a conversation to fetch data or take action. See [Function Calling](/docs/voice-agents-function-calling).

## How a single turn flows

#### Audio in

The customer's audio streams into the API over one connection, from a browser, app, or phone call.

#### Transcribe

Speech-to-text turns the audio into text in real time and detects when the user's turn ends.

#### Think

The transcript goes to the LLM, which decides what to say next — calling functions or external systems if needed.

#### Speak

Text-to-speech converts the reply to audio and streams it back to the customer. If the customer interrupts, the agent yields and the loop restarts.

Each of these stages maps to a concrete WebSocket message: `Settings` configures the pipeline, transcript events flow from STT, `AgentThinking` and `FunctionCallRequest` capture LLM decisions, and audio responses stream back as binary frames. To see the exact message sequence — from opening the connection through a full conversation loop — read the [Voice Agent Message Flow](/docs/voice-agent-message-flow).

## Connecting to the outside world

The API is the conversational core, and it extends in three directions:

* **External systems** — within a turn, your LLM and [function calls](/docs/voice-agents-function-calling) can reach embedding models, databases, and retrieval APIs to ground responses in your own data.
* **Telephony** — connect the agent to phone networks for [inbound](/docs/inbound-telephony-agent) and [outbound](/docs/outbound-telephony-agent) calls through providers like [Twilio](/docs/twilio-and-deepgram-voice-agent), [Genesys](/docs/genesys-and-deepgram-voice-agent), [Amazon Connect](/docs/amazon-connect-and-deepgram-voice-agent), and [AudioCodes](/docs/integrate-deepgram-voice-agent-with-audiocodes).
* **Response injections** — [push messages](/docs/voice-agent-inject-agent-message) into the conversation from your application, so server-side events can shape what the agent says.

## Next steps

* [Build a Voice Agent](/docs/build-a-voice-agent) — A step-by-step guide to your first agent in Python, JavaScript, C#, or Go.
* [Configure Your Agent](/docs/configure-voice-agent) — Choose STT, LLM, and TTS models and set up audio formats and endpointing.
* [Feature Overview](/docs/voice-agent-feature-overview) — The full list of Voice Agent API capabilities.
* [API Reference](/reference/voice-agent/voice-agent) — The complete WebSocket protocol for the Agent API.
