---
title: "AudioCodes (LiveHub) and Deepgram Voice Agent API"
source: https://developers.deepgram.com/docs/integrate-deepgram-voice-agent-with-audiocodes.md
path: docs/integrate-deepgram-voice-agent-with-audiocodes
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# AudioCodes (LiveHub) and Deepgram Voice Agent API

[AudioCodes VoiceAI Connect](https://voiceaiconnect.audiocodes.com/) is a powerful platform that enables the integration of telephony and contact center platforms with the cloud, thus facilitating the use of Deepgram in your customer journey.

It offers a simple user interface for standing up connections and developer-friendly APIs for advanced integrations.

Note, AudioCodes offers [two versions of this platform](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/editions_and_deployment.htm?TocPath=VoiceAI%2520Connect%257C_____1) - LiveHub, which is the self serve version, as well as VoiceAI Connect Enterprise, which is the managed services version.

This guide will focus on LiveHub, as it is accessible to all users. However, if you are using VoiceAI Connect Enterprise, the steps and instructions laid out here will be very similar. In addition, you will have the help of the AudioCodes Professional Services team to help you with the configuration. Refer to this doc for guidance, but note that the exact steps may vary slightly depending on how your specific version of VoiceAI Connect Enterprise is built.

## Before you Begin

Before you start, you'll need to follow the steps in the [Make Your First API Request](/docs/make-your-first-api-request) guide to obtain a Deepgram API key.

You will need an [AudioCodes LiveHub](https://livehub.audiocodes.io/login) account to connect the two services.

## The Problem This SDK Solves

Most enterprise call centers ultimately rely on SIP for call signaling and RTP for media transport — the core VoIP protocols that have underpinned telephony since the late 1990s. Deepgram's [Voice Agent API](/reference/voice-agent/voice-agent) speaks WebSocket. These worlds don't connect natively.

AudioCodes VoiceAI Connect already bridges that gap for thousands of enterprises — it accepts calls from any number of call center platforms or telephony systems and exposes them as WebSocket connections that AI systems can connect to.

But there is still a missing piece. Someone has to take that WebSocket audio stream, forward it to Deepgram's Voice Agent API in real time, route the agent's synthesized speech back to the caller, and handle everything that can go wrong in between. Rather than have every customer write that plumbing from scratch, Deepgram maintains an open-source SDK — [`deepgram-audiocodes-bridge`](https://github.com/deepgram/deepgram-audiocodes-bridge) — that solves it once.

```text
AudioCodes VoiceAI Connect 
(Bot API - websocket mode)
            ↕
deepgram-audiocodes-bridge
            ↕
Deepgram Voice Agent API
```

## What the SDK Does

The bridge runs a WebSocket server that speaks the AudioCodes Bot API, manages a Deepgram Voice Agent connection per call, routes audio bidirectionally in real time, and emits typed events your application code hooks into. Audio frame parsing, protocol handshaking, barge-in handling, TTS streaming, and session teardown all live inside the SDK — your code stays focused on business logic.

For installation, the full event and method reference, authentication walkthroughs, and runnable examples, see the [`deepgram-audiocodes-bridge` README](https://github.com/deepgram/deepgram-audiocodes-bridge). The rest of this page covers the AudioCodes-specific context that's most useful to know before you start.

A minimal bridge looks like this:

```python
# Configure the bridge: Deepgram credentials + your Voice Agent settings.
bridge = DeepgramBridge(BridgeConfig(
    deepgram_api_key="your-deepgram-api-key",
    deepgram_config={
        "agent": {
            "listen": {
                "provider": {
                    "type": "deepgram", 
                    "model": "flux-general-en"
                    }
                },
            "think": {
                "provider": {
                    "type": "open_ai",  
                    "model": "gpt-5.4-mini"
                    },
                "prompt":   "You are a helpful assistant."},
            "speak": {
                "provider": {
                    "type": "deepgram", 
                    "model": "aura-2-helena-en"
                    }
                },
            "greeting": "Hi! How can I help today?",
        },
    },
    port=8000,
))

# Hook into typed events — your business logic lives here.
@bridge.on("session_start")
async def on_start(session, event):
    print(f"Call started: conversation_id={session.conversation_id}")

@bridge.on("conversation_text")
async def on_text(session, event):
    print(f"{event.role}: {event.content}")

# Start the WebSocket server — now accepting connections at ws://localhost:8000
asyncio.run(bridge.run())
```

That's the whole shape of an integration: configure once, register handlers for the events you care about, and run. Everything else — audio routing, barge-in, session teardown — is handled inside the SDK.

## Tying Calls Back to Your CCaaS: `conversation_id`

Every `session_start` event includes a `conversation_id` — the AudioCodes conversation identifier surfaced from the `session.initiate` handshake.

This is the foreign key that ties the Deepgram session to the upstream CCaaS call record. Use it to associate transcript writes, screen pops, disposition codes, and compliance logs with the correct call in Genesys, Amazon Connect, Salesforce, or wherever your call data ultimately lives. Without it, you have a transcript with no way to reconcile it back to the call it came from.

```python
@bridge.on("session_end")
async def on_end(session, event):
    transcript = session.get_transcript()
    await write_to_crm(session.conversation_id, transcript)
```

## Configuring AudioCodes LiveHub

Once your bridge is running and reachable from the public internet (via your own hosting, or a tunnel like ngrok for testing), point an AudioCodes LiveHub Bot Connection at it.

Follow the [LiveHub Bot Connection setup guide](https://techdocs.audiocodes.com/livehub/#LiveHub/Creating%20your%20Bot.htm?TocPath=Bot%2520connectivity%257CDefine%2520your%2520bot%2520connection%257C_____0), following the "Add new voice bot connection" instructions:

* **Bot connection API type** - select Websocket mode
* **Bot URL** — the WebSocket URL of your running bridge (for example, `wss://your-host.example.com/`).
* **Authentication** — LiveHub supports No Auth, Permanent Token (shared secret), and OAuth 2.0. Pick one and match it on the bridge side via `BridgeConfig`. See the SDK's [auth example](https://github.com/deepgram/deepgram-audiocodes-bridge/tree/main/examples/03_auth) for copy-pasteable walkthroughs of all three modes.
* **Barge-in** — toggle on if you want callers to interrupt the agent. The Voice Agent API supports barge-in natively and the bridge handles it for you, but VAIC's own barge-in setting can override it. **This defaults to off** when you create a new Bot Connection. See [Edit your Bot Connection](https://techdocs.audiocodes.com/livehub/#LiveHub/Editing%20your%20bot.htm?TocPath=Bot%2520connectivity%257C_____6) for the toggle.

Always consult the [AudioCodes API documentation](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_API/Speech-to-Text.htm?TocPath=AudioCodes%2520API%257C_____4) for the most up to date information.
