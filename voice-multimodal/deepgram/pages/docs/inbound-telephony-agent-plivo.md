---
title: "Build an Inbound Telephony Agent with Plivo"
source: https://developers.deepgram.com/docs/inbound-telephony-agent-plivo.md
path: docs/inbound-telephony-agent-plivo
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build an Inbound Telephony Agent with Plivo

> **Info**
>
> For more information and to use the reference implementation, visit the [Deepgram Voice Agent example in the Plivo agent examples repo](https://github.com/plivo/python-agents-examples/tree/main/deepgram-voiceagent).

A reference implementation for building a secure inbound telephony voice agent using [Deepgram's Voice Agent API](/docs/voice-agent) and [Plivo](https://www.plivo.com/). Uses [Deepgram Flux](/docs/flux/feature-overview) for speech-to-text with native turn-taking optimized for real-time voice agent conversations.

Callers dial a Plivo number and talk to Alex, a customer support agent for a sample software company called TechFlow. Alex can look up an order, send a text message, schedule a callback, transfer the call, and end the call. `end_call` hangs up the call. The other functions return sample data. To fit the agent to your use case, see [Customize the agent](#customize-the-agent).

For how the bridge works, see [Plivo and Deepgram Voice Agent](/docs/plivo-and-deepgram-voice-agent).

## Architecture

One FastAPI server answers Plivo's webhooks and bridges the call audio to the Voice Agent API.

```text
                    ┌──────────────┐
                    │  Phone Call  │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │    Plivo     │
                    │ Audio Stream │
                    └──────┬───────┘
                           │ WebSocket (μ-law audio as base64 JSON)
                           │
              ┌────────────▼────────────────┐
              │     Application Server      │
              │          (FastAPI)          │
              │                             │
              │  POST /answer               │  ← Answer URL (returns <Stream> XML)
              │  POST /hangup               │  ← Hangup URL (logs duration and cause)
              │  WS   /ws                   │  ← Plivo audio stream
              │                             │
              │  ┌───────────────────────┐  │
              │  │  DeepgramVoiceAgent   │  │  ← One per call
              │  │                       │  │
              │  │  Plivo  ←→  Deepgram  │  │  ← Audio bridge
              │  │  audio      audio     │  │
              │  │  (base64)   (raw)     │  │
              │  │                       │  │
              │  │  Function handlers    │  │  ← Run the agent's function calls
              │  └───────────┬───────────┘  │
              └──────────────┼──────────────┘
                             │ WebSocket (raw μ-law audio + JSON events)
                             │
              ┌──────────────▼──────────────┐
              │  Deepgram Voice Agent API   │
              │                             │
              │  listen   Flux (STT)        │
              │  think    LLM               │
              │  speak    Aura-2 (TTS)      │
              └─────────────────────────────┘
```

## Prerequisites

* Python 3.10+, [uv](https://docs.astral.sh/uv/), and Git 2.25+
* A [Deepgram account](https://console.deepgram.com/) and [API key](/docs/create-additional-api-keys#create-an-api-key-using-the-deepgram-console). Deepgram manages the LLM connection, so you don't need a separate LLM provider key.
* A [Plivo account](https://cx.plivo.com/signup) with a [voice-enabled phone number](https://cx.plivo.com/phone-numbers), and the Auth ID and Auth Token from the [Plivo console](https://cx.plivo.com/home)
* A tunnel that gives your local server a public HTTPS URL, so Plivo can reach it: [`cloudflared`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) or [ngrok](https://ngrok.com/download)

Install one of the tunnel tools:

```bash
# macOS

# Option 1: cloudflared. The server starts the tunnel when you run it with --tunnel.
# No Cloudflare account is needed.
brew install cloudflared

# Option 2: ngrok. You start the tunnel and set PUBLIC_URL.
# Needs an authtoken from your ngrok account.
brew install ngrok
ngrok config add-authtoken <YOUR_NGROK_AUTHTOKEN>
```

## Quick start

Three steps get you from a clone to a live call.

### 1. Set up the project

Clone the example's folder from the companion repository.

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/plivo/python-agents-examples.git
cd python-agents-examples
git sparse-checkout set deepgram-voiceagent
cd deepgram-voiceagent
cp .env.example .env
```

Edit `.env` and set four values. Everything else has a default.

```bash
DEEPGRAM_API_KEY=...
PLIVO_AUTH_ID=...
PLIVO_AUTH_TOKEN=...
PLIVO_PHONE_NUMBER=+14150000001
```

### 2. Start the server

Start the inbound server with a tunnel.

```bash
uv run python -m inbound.server --tunnel
```

> **Info**
>
> Prefer ngrok? Run `ngrok http 8000` in a second terminal. Set `PUBLIC_URL` in `.env` to the `https://` URL it prints, then start the server with `uv run python -m inbound.server`.

On startup, the server:

1. Starts a Cloudflare quick tunnel to port 8000 (`SERVER_PORT`) and uses its `https://` URL as `PUBLIC_URL`.
2. Creates a Plivo application named `Deepgram_VoiceAgent`, or updates it, with `/answer` and `/hangup` on that URL as its Answer URL and Hangup URL.
3. Links `PLIVO_PHONE_NUMBER` to that application.
4. Logs a Ready line once Plivo has accepted the URL.

```text
Ready! Call +14150000001 to talk to the agent (Ctrl+C to stop)
```

Every console line starts with a timestamp, the log level, and the source location. The log excerpts on this page show only the message that follows.

> **Warning**
>
> Wait for the Ready line before you call. Plivo accepts a new tunnel hostname only after it resolves, which can take about a minute. Until then, the server retries for up to 3 minutes and logs:
>
> ```text
> Waiting for Plivo to accept https://<random>.trycloudflare.com (a new tunnel hostname can take a minute to resolve); retrying every 5s...
> ```

### 3. Call the agent

Call your Plivo number. The agent greets you. Ask about plans or an order, talk over the agent to test barge-in, then say goodbye and let it hang up.

The console logs each turn's transcript, a barge-in line when you interrupt, and the hangup when the agent ends the call. The greeting is turn 1, so your first question is turn 2. The elapsed seconds, the transcripts, and the `cleared` count vary per call.

```text
[<call_uuid>] [  19.54s] [turn] turn 2: user 'What plans do you offer?'
[<call_uuid>] [  20.56s] [turn] turn 2: agent 'We have three main plans: TechFlow Pro for twelve dollars a month with a hundred'
[<call_uuid>] [  46.41s] [barge_in] barge-in: cleared=0
Hung up call via REST: <call_uuid>
```

Press Ctrl+C to stop the server and the tunnel.

## Test without a phone call

`tests/test_e2e_live.py` runs the agent against the real Voice Agent API with no Plivo account. It needs `DEEPGRAM_API_KEY` in `.env`, an `ffmpeg` binary, and port 18001.

```bash
uv sync    # installs the dev dependencies

# Real Deepgram, no phone call
uv run pytest tests/test_e2e_live.py -v -s

# Unit tests: offline, no API keys
uv run pytest tests/test_integration.py tests/test_observability.py -v -k unit
```

The test starts the inbound server, sends `/answer` a signed request, opens the returned stream URL with a signed connection, and sends the `start` event, then silence. It sends questions as `text` events, which the server forwards to Deepgram as `InjectUserMessage`. It transcribes the agent's audio and checks the greeting, a pricing answer, and that a goodbye makes the agent call `end_call`.

Each test runs twice: `[inline]`, and `[saved]` with a [reusable agent configuration](/docs/reusable-agent-configurations) that the test creates and deletes. The `[saved]` run is skipped unless your API key has the `agent:read` and `agent:write` scopes.

## Key technical concepts

* **Single WebSocket bridge**: `DeepgramVoiceAgent` in `inbound/agent.py` runs once per call. It connects two WebSockets: Plivo's audio stream on `/ws`, and one to the Voice Agent API at `wss://agent.deepgram.com/v1/agent/converse`. It uses the `websockets` library directly. The `<Stream>` XML and the `Settings` message both set μ-law audio at 8 kHz, so the server only converts between base64 and raw bytes.

* **Barge-in**: When Deepgram sends `UserStartedSpeaking`, `_on_user_started_speaking()` empties the server's send queue and sends Plivo a `clearAudio` event, which drops the audio Plivo has queued.

* **Function calls**: Deepgram sends a `FunctionCallRequest`. `_handle_function_call()` runs the function on your server. The server returns the result in a `FunctionCallResponse`.

* **Graceful hangup**: `end_call` only marks the hangup as pending, so the goodbye plays in full. After `AgentAudioDone`, the server sends Plivo a `checkpoint` event. When Plivo confirms playback with `playedStream`, `_hangup_call()` ends the call through the Plivo REST API. If no confirmation arrives within 15 seconds of `end_call`, the server hangs up anyway.

* **Signature validation**: `verify_plivo_signature()` checks Plivo's V3 signature on every webhook route (`/answer`, `/hangup`, `/fallback`, `/hold`) and on the `/ws` stream. Requests and streams that fail the check get a 403. The server refuses to start without `PLIVO_AUTH_TOKEN`.

## Project structure

The inbound server and agent are in `inbound/`.

```text
deepgram-voiceagent/
├── inbound/
│   ├── server.py                # FastAPI app: /answer, /hangup, /fallback, /hold, /ws and a health check on /
│   │                            # Signature validation, Plivo application setup, --tunnel, REST hangup
│   ├── agent.py                 # DeepgramVoiceAgent: Settings, audio bridge, barge-in, hangup
│   │                            # FUNCTION_DEFINITIONS and the function handlers
│   └── system_prompt.md         # The agent's instructions
├── outbound/                    # Outbound server and agent
├── utils.py                     # Phone number normalization, audio pass-through, tunnel helpers
├── tests/
│   ├── helpers.py               # Test server, Plivo request signing, recording and transcription helpers
│   ├── test_integration.py      # Unit tests, local server tests, Deepgram and Plivo checks
│   ├── test_observability.py    # Logging and tracing tests
│   ├── test_e2e_live.py         # Real Deepgram, no phone call
│   ├── test_live_call.py        # Real inbound call (needs a second Plivo number)
│   └── test_multiturn_voice.py  # Multi-turn and barge-in on a real call
├── .env.example                 # Environment variable template
├── pyproject.toml               # Dependencies, managed with uv
├── Dockerfile                   # Container image; runs the inbound server by default
└── README.md                    # Full configuration reference, observability, troubleshooting
```

## Customize the agent

The server reads the files and `.env` values below at startup, so restart it after each change.

| To change        | Edit                                                                       |
| ---------------- | -------------------------------------------------------------------------- |
| Instructions     | `inbound/system_prompt.md`                                                 |
| Greeting         | `AGENT_GREETING` in `.env`                                                 |
| Models and voice | `DEEPGRAM_*` values in `.env`                                              |
| Functions        | `FUNCTION_DEFINITIONS` and `_handle_function_call()` in `inbound/agent.py` |

### Change the instructions and greeting

For each call, the server adds the caller's number, the call ID, and the current time to the instructions. Deepgram speaks the greeting exactly as written. The prompt tells the model that it has already been spoken, so keep the two consistent.

### Choose the models

The server passes each `DEEPGRAM_*` value into `Settings` unchanged, so use the Voice Agent's [LLM](/docs/voice-agent-llm-models) and [TTS](/docs/voice-agent-tts-models) model IDs. The outbound server reads the same values. These are the defaults:

```bash
DEEPGRAM_LISTEN_MODEL=flux-general-en
DEEPGRAM_LISTEN_EOT_THRESHOLD=0.7
DEEPGRAM_LISTEN_EOT_TIMEOUT_MS=5000
DEEPGRAM_THINK_PROVIDER=open_ai
DEEPGRAM_THINK_MODEL=gpt-4.1-mini
DEEPGRAM_THINK_TEMPERATURE=0.7
DEEPGRAM_SPEAK_MODEL=aura-2-thalia-en
```

If you set `DEEPGRAM_INBOUND_AGENT_ID` to a [reusable agent configuration](/docs/reusable-agent-configurations) UUID, the server sends only that UUID in `Settings`. Then these values, the prompt file, and `FUNCTION_DEFINITIONS` are not used.

### Add functions

Each function is a JSON schema in `FUNCTION_DEFINITIONS` and a branch in `_handle_function_call()`. To connect your systems, replace the bodies of `check_order_status()`, `send_sms()`, `schedule_callback()`, and `transfer_call()`. Keep `end_call`, because the agent uses it to hang up. See [Function Calling](/docs/voice-agents-function-calling).

### Multilingual support

For languages other than English, set `DEEPGRAM_LISTEN_MODEL=flux-general-multi`, choose a `DEEPGRAM_SPEAK_MODEL` voice for the language, and write the greeting and the prompt in that language. To tell Flux which languages to expect, add `language_hints` in `_build_listen_provider()` in `inbound/agent.py`. See the [Deepgram multilingual voice agent guide](/docs/multilingual-voice-agent).

## Deploy

A tunnel is for development and testing. For production, run the server on a host with a fixed HTTPS URL. The example includes a Dockerfile:

```bash
docker build -t deepgram-voiceagent .
docker run --env-file .env -e PUBLIC_URL=https://your-host.example.com -p 8000:8000 deepgram-voiceagent
```

On startup, the container configures the Plivo application and number from `PUBLIC_URL`.

* **Choose a host that keeps WebSockets open for the whole call.** Fly.io, Render, Railway, a VM, and Kubernetes all work. Serverless functions can't hold the socket.
* **Set `PUBLIC_URL` to the exact URL Plivo calls.** The server validates each webhook and stream signature against it. If the scheme or host differs, Plivo's requests get a 403 and the server logs:

  ```text
  Rejected Plivo webhook POST /answer: signature mismatch (does PUBLIC_URL match the URL Plivo calls?)
  ```

## Additional resources

* [Plivo and Deepgram Voice Agent](/docs/plivo-and-deepgram-voice-agent) — How the bridge works, with code
* [Build an Outbound Telephony Agent with Plivo](/docs/outbound-telephony-agent-plivo)
* [Deepgram Voice Agent API Docs](/docs/voice-agent)
* [Configure the Voice Agent](/docs/configure-voice-agent) — Every field of the `Settings` message
* [Example README](https://github.com/plivo/python-agents-examples/tree/main/deepgram-voiceagent#readme) — Configuration reference, observability, and troubleshooting
* [Plivo Audio Streaming reference](https://www.plivo.com/docs/voice-agents/audio-streaming/concepts/audio-streaming-reference)
* [Plivo signature validation](https://www.plivo.com/docs/voice/concepts/signature-validation)
* [Deepgram Voice Agent Integration on Plivo](https://www.plivo.com/docs/voice-agents/audio-streaming/integration-guides/voice-agent-pipelines/deepgram-voice-agent)
