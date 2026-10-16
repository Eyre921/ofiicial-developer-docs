---
title: "Build an Outbound Telephony Agent with Plivo"
source: https://developers.deepgram.com/docs/outbound-telephony-agent-plivo.md
path: docs/outbound-telephony-agent-plivo
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build an Outbound Telephony Agent with Plivo

> **Info**
>
> For more information and to use the reference implementation, visit the [Deepgram Voice Agent example in the Plivo agent examples repo](https://github.com/plivo/python-agents-examples/tree/main/deepgram-voiceagent).

A reference implementation for building an outbound telephony voice agent using [Deepgram's Voice Agent API](/docs/voice-agent) and [Plivo](https://www.plivo.com/). Uses [Deepgram Flux](/docs/flux/feature-overview) for speech-to-text with native turn-taking optimized for real-time voice agent conversations.

You place each call with Plivo's [Create a Call API](https://www.plivo.com/docs/voice/api/calls#create-a-call). When the callee answers, they talk to Alex, an AI agent for a sample software company called TechFlow. Alex follows up on a free trial signup or demo request. Alex opens with a greeting you set per call, qualifies the lead (team size, use case, timeline, decision process), and offers a meeting with a sales specialist. Alex can also look up an order, send a text message, schedule a callback, and transfer the call. `end_call` hangs up the call. The other functions return sample data. To fit the agent to your use case, see [Customize the agent](#customize-the-agent).

For how the bridge works, see [Plivo and Deepgram Voice Agent](/docs/plivo-and-deepgram-voice-agent).

## Architecture

One FastAPI server answers Plivo's webhooks and bridges the call audio to the Voice Agent API.

```text
   Your backend, CRM, or shell
               │
               │  POST /v1/Account/<auth_id>/Call/       ← Plivo Create a Call API
               ▼
         ┌───────────┐      dials      ┌──────────┐
         │   Plivo   │ ──────────────► │  Callee  │
         └─────┬─────┘                 └──────────┘
               │  callee answers
               ▼
 ┌───────────────────────────────────────────┐
 │       Application Server (FastAPI)        │
 │                port 8001                  │
 │                                           │
 │  POST /outbound/answer?greeting=...       │  ← Answer URL (returns <Stream> XML)
 │  WS   /ws                                 │  ← Plivo audio stream
 │  POST /outbound/hangup                    │  ← Hangup URL (logs duration and cause)
 │                                           │
 │  ┌─────────────────────────────────────┐  │
 │  │  DeepgramVoiceAgent                 │  │  ← One per call
 │  │                                     │  │
 │  │  Plivo ←→ Deepgram                  │  │  ← Audio bridge, μ-law 8 kHz both ways
 │  │  barge-in, function calls, hangup   │  │
 │  └──────────────────┬──────────────────┘  │
 └─────────────────────┼─────────────────────┘
                       │  WebSocket (raw μ-law audio + JSON events)
                       ▼
          ┌──────────────────────────┐
          │ Deepgram Voice Agent API │
          │  listen → think → speak  │
          └──────────────────────────┘
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

The outbound server uses `PLIVO_PHONE_NUMBER` as the caller ID in the command it logs. It doesn't change the number's settings.

### 2. Start the server

Start the outbound server with a tunnel.

```bash
uv run python -m outbound.server --tunnel
```

> **Info**
>
> Prefer ngrok? Run `ngrok http 8001` in a second terminal. Then start the server with `PUBLIC_URL=https://<your-outbound-host> uv run python -m outbound.server`. `<your-outbound-host>` is the hostname ngrok prints.

On startup, the server:

1. Starts a Cloudflare quick tunnel to port 8001 (`OUTBOUND_SERVER_PORT`) and uses its `https://` URL as `PUBLIC_URL`.
2. Logs a Ready message with a cURL command for Plivo's Create a Call API.

```text
Ready! Place a call with Plivo's Make Call API; Plivo then requests this server's answer URL:
  curl -X POST "https://api.plivo.com/v1/Account/$PLIVO_AUTH_ID/Call/" \
    -u "$PLIVO_AUTH_ID:$PLIVO_AUTH_TOKEN" -H "Content-Type: application/json" \
    -d '{"from": "+14150000001", "to": "<E.164 number to call>",
         "answer_url": "https://<random>.trycloudflare.com/outbound/answer?greeting=Hi%2C%20this%20is%20Alex%20from%20TechFlow.%20I%27m%20reaching%20out%20because%20you%20requested%20a%20demo.%20Is%20now%20a%20good%20time%20for%20a%20quick%20chat%3F",
         "hangup_url": "https://<random>.trycloudflare.com/outbound/hangup",
         "answer_method": "POST", "hangup_method": "POST"}'
  Optional answer_url query param (URL-encoded): greeting — spoken verbatim when the callee answers (Deepgram agent.greeting); a default is used when absent.
  A new tunnel hostname can take a minute before Plivo accepts it; retry if the API answers "Must be a valid url".
(Ctrl+C to stop)
```

Every console line starts with a timestamp, the log level, and the source location. The log excerpts on this page show only the message that follows.

### 3. Place a test call

In a second terminal, export your credentials from `.env` in the example folder, then place the call with cURL or the Plivo Python SDK. In both, `<your-outbound-host>` is the hostname in the logged command.

```bash
set -a && source .env && set +a
```

#### cURL

Run the logged command with `to` set to the number to call. This is the same command with placeholders:

```bash
curl -X POST "https://api.plivo.com/v1/Account/$PLIVO_AUTH_ID/Call/" \
  -u "$PLIVO_AUTH_ID:$PLIVO_AUTH_TOKEN" -H "Content-Type: application/json" \
  -d '{"from": "+14150000001", "to": "+14155550123",
       "answer_url": "https://<your-outbound-host>/outbound/answer?greeting=Hi%2C%20this%20is%20Alex%20from%20TechFlow.%20I%27m%20reaching%20out%20because%20you%20requested%20a%20demo.%20Is%20now%20a%20good%20time%20for%20a%20quick%20chat%3F",
       "hangup_url": "https://<your-outbound-host>/outbound/hangup",
       "answer_method": "POST", "hangup_method": "POST"}'
```

#### Python SDK

Set `to_` to the number to call, then paste the script into `uv run python` in the same terminal.

```python
import os
from urllib.parse import quote, urlencode

import plivo

client = plivo.RestClient(
    auth_id=os.environ["PLIVO_AUTH_ID"], auth_token=os.environ["PLIVO_AUTH_TOKEN"]
)

base_url = "https://<your-outbound-host>"
greeting = (
    "Hi, this is Alex from TechFlow. I'm reaching out because you requested a demo. "
    "Is now a good time for a quick chat?"
)

response = client.calls.create(
    from_="+14150000001",
    to_="+14155550123",
    answer_url=f"{base_url}/outbound/answer?" + urlencode({"greeting": greeting}, quote_via=quote),
    answer_method="POST",
    hangup_url=f"{base_url}/outbound/hangup",
    hangup_method="POST",
)
print(response)
```

The phone rings, and the greeting you passed is the first thing the callee hears. If Plivo rejects the `answer_url` as not valid, the new tunnel hostname doesn't resolve yet. Wait a minute and retry.

These log lines mark the start and end of the call. The duration and hangup cause vary.

```text
Outbound call answered: CallUUID=<call_uuid>, To=14155550123, greeting: from answer_url
Outbound call ended: CallUUID=<call_uuid>, Duration=20s, HangupCause=NORMAL_CLEARING
```

Press Ctrl+C to stop the server and the tunnel.

## Call initiation flow

1. Your backend calls Plivo's Create a Call API at `https://api.plivo.com/v1/Account/<auth_id>/Call/`. The `answer_url` points at this server's `/outbound/answer` route and carries the greeting.
2. Plivo dials the callee.
3. The callee answers, and Plivo requests `/outbound/answer?greeting=...`. The server returns `<Stream>` XML that points at its `/ws` route.
4. Plivo opens the `/ws` WebSocket and streams the call audio.
5. The server connects to the Voice Agent API and sends a `Settings` message with the greeting as `agent.greeting`. Deepgram speaks the greeting, and the conversation runs.
6. The model calls `end_call` and says goodbye. The server hangs up after the goodbye has played, and Plivo requests `/outbound/hangup`.

## Key technical concepts

* **Outbound call initiation**: You pass the Answer URL with each call instead of linking it to a number. The server has no dial endpoint. It still needs a public URL, because Plivo requests the Answer URL and opens a WebSocket to the server.

* **Per-call greeting**: The `greeting` query parameter on the Answer URL is the only per-call input. The server passes it unchanged as `agent.greeting`, and Deepgram speaks it exactly as written. It is not an instruction to the model. Without it, the agent says `DEFAULT_OUTBOUND_GREETING` from `outbound/agent.py`.

* **Single WebSocket bridge**: `DeepgramVoiceAgent` in `outbound/agent.py` runs once per call. It connects two WebSockets: Plivo's audio stream on `/ws`, and one to the Voice Agent API at `wss://agent.deepgram.com/v1/agent/converse`. It uses the `websockets` library directly. The `<Stream>` XML and the `Settings` message both set μ-law audio at 8 kHz, so the server only converts between base64 and raw bytes.

* **Barge-in**: When Deepgram sends `UserStartedSpeaking`, `_on_user_started_speaking()` empties the server's send queue and sends Plivo a `clearAudio` event, which drops the audio Plivo has queued.

* **Function calls**: Deepgram sends a `FunctionCallRequest`. `_handle_function_call()` runs the function on your server. The server returns the result in a `FunctionCallResponse`.

* **Graceful hangup**: `end_call` only marks the hangup as pending, so the goodbye plays in full. After `AgentAudioDone`, the server sends Plivo a `checkpoint` event. When Plivo confirms playback with `playedStream`, `_hangup_call()` ends the call through the Plivo REST API. If no confirmation arrives within 15 seconds of `end_call`, the server hangs up anyway.

* **Signature validation**: `verify_plivo_signature()` checks Plivo's V3 signature on both webhook routes (`/outbound/answer`, `/outbound/hangup`) and on the `/ws` stream. Requests and streams that fail the check get a 403. The server refuses to start without `PLIVO_AUTH_TOKEN`. Plivo signs the URL it requested, including the query string. If a proxy between Plivo and your server rewrites the greeting, validation fails.

## Track calls

For a call's status, duration, and hangup cause, use Plivo's [Call API](https://www.plivo.com/docs/voice/api/calls) or the [voice logs](https://cx.plivo.com/logs?tab=voice) in the Plivo console. If you pass the optional `hangup_url`, the server also logs the `CallUUID`, duration, and hangup cause when the call ends.

## Project structure

The outbound server and agent are in `outbound/`.

```text
deepgram-voiceagent/
├── outbound/
│   ├── server.py                # FastAPI app: /outbound/answer, /outbound/hangup, /ws and a health check on /
│   │                            # Signature validation, Ready message, --tunnel, REST hangup
│   ├── agent.py                 # DeepgramVoiceAgent: Settings, audio bridge, barge-in, hangup
│   │                            # FUNCTION_DEFINITIONS, the function handlers, DEFAULT_OUTBOUND_GREETING
│   └── system_prompt.md         # The agent's instructions
├── inbound/                     # Inbound server and agent (port 8000)
├── utils.py                     # Phone number normalization, audio pass-through, tunnel helpers
├── tests/
│   └── test_outbound_call.py    # Real outbound call
├── .env.example                 # Environment variable template
├── pyproject.toml               # Dependencies, managed with uv
├── Dockerfile                   # Container image; runs the inbound server by default (see Deploy for outbound)
└── README.md                    # Full configuration reference, observability, troubleshooting
```

## Customize the agent

The server reads the files and `.env` values below at startup, so restart it after changing them. The greeting is set per call.

| To change        | Edit                                                                        |
| ---------------- | --------------------------------------------------------------------------- |
| Instructions     | `outbound/system_prompt.md`                                                 |
| Greeting         | `greeting` parameter on the Answer URL                                      |
| Models and voice | `DEEPGRAM_*` values in `.env`                                               |
| Functions        | `FUNCTION_DEFINITIONS` and `_handle_function_call()` in `outbound/agent.py` |

### Change the instructions and greeting

Pass the greeting, URL-encoded, as the `greeting` query parameter on the Answer URL. For each call, the server adds the callee's number, your Plivo number, the call ID, and the current time to the instructions. The prompt tells the model that the greeting has already been spoken, so keep the two consistent.

### Choose the models

The server passes each `DEEPGRAM_*` value into `Settings` unchanged, so use the Voice Agent's [LLM](/docs/voice-agent-llm-models) and [TTS](/docs/voice-agent-tts-models) model IDs. The inbound server reads the same values. These are the defaults:

```bash
DEEPGRAM_LISTEN_MODEL=flux-general-en
DEEPGRAM_LISTEN_EOT_THRESHOLD=0.7
DEEPGRAM_LISTEN_EOT_TIMEOUT_MS=5000
DEEPGRAM_THINK_PROVIDER=open_ai
DEEPGRAM_THINK_MODEL=gpt-4.1-mini
DEEPGRAM_THINK_TEMPERATURE=0.7
DEEPGRAM_SPEAK_MODEL=aura-2-thalia-en
```

If you set `DEEPGRAM_OUTBOUND_AGENT_ID` to a [reusable agent configuration](/docs/reusable-agent-configurations) UUID, the server sends only that UUID in `Settings`. Then these values, the prompt file, and `FUNCTION_DEFINITIONS` are not used. The per-call greeting still applies. The server sends it as `InjectAgentMessage`.

### Add functions

Each function is a JSON schema in `FUNCTION_DEFINITIONS` and a branch in `_handle_function_call()`. To connect your systems, replace the bodies of `check_order_status()`, `send_sms()`, `schedule_callback()`, and `transfer_call()`. Keep `end_call`, because the agent uses it to hang up. See [Function Calling](/docs/voice-agents-function-calling).

### Multilingual support

For languages other than English, set `DEEPGRAM_LISTEN_MODEL=flux-general-multi`, choose a `DEEPGRAM_SPEAK_MODEL` voice for the language, and write the prompt and each call's greeting in that language. To tell Flux which languages to expect, add `language_hints` in `_build_listen_provider()` in `outbound/agent.py`. See the [Deepgram multilingual voice agent guide](/docs/multilingual-voice-agent).

### Extend the example

**Pass more per-call details.** Add query parameters to the Answer URL. Then change `outbound/server.py` to forward them the way it forwards `greeting`. Change `outbound/agent.py` to add them to the instructions, for example in `_build_call_context()`.

**Detect answering machines.** Plivo's [Create a Call API](https://www.plivo.com/docs/voice/api/calls#create-a-call) has a `machine_detection` parameter. Use it to decide whether to start the agent or leave a voicemail message, the way the [Twilio outbound reference implementation](/docs/outbound-telephony-agent) does.

**Store call outcomes.** Add a function that records the result of each call, and extend `outbound_hangup_webhook()` to save the duration and hangup cause to your CRM.

## Deploy

A tunnel is for development and testing. For production, run the server on a host with a fixed HTTPS URL. The example's Dockerfile starts the inbound server by default, so pass the outbound command and publish port 8001:

```bash
docker build -t deepgram-voiceagent .
docker run --env-file .env -e PUBLIC_URL=https://<your-outbound-host> -p 8001:8001 deepgram-voiceagent \
  uv run python -m outbound.server
```

Use the same host in the `answer_url` and `hangup_url` of each call.

* **Choose a host that keeps WebSockets open for the whole call.** Fly.io, Render, Railway, a VM, and Kubernetes all work. Serverless functions can't hold the socket.
* **Set `PUBLIC_URL` to the exact URL Plivo calls.** The server validates each webhook and stream signature against it. If the scheme or host differs, Plivo's requests get a 403 and the server logs:

  ```text
  Rejected Plivo webhook POST /outbound/answer: signature mismatch (does PUBLIC_URL match the URL Plivo calls?)
  ```

## Compliance note

This example shows the technical setup, not how to comply with calling laws. Outbound calling is regulated in many places, for example by the TCPA in the United States. The sample scenario assumes the callee signed up for a trial or asked for a demo. Add the disclosures your use case needs to the greeting, such as saying that the caller is an AI. Check the legal and regulatory rules that apply before you call real customers.

## Additional resources

* [Plivo and Deepgram Voice Agent](/docs/plivo-and-deepgram-voice-agent) — How the bridge works, with code
* [Build an Inbound Telephony Agent with Plivo](/docs/inbound-telephony-agent-plivo)
* [Deepgram Voice Agent API Docs](/docs/voice-agent)
* [Function Calling](/docs/voice-agents-function-calling)
* [Plivo Create a Call API](https://www.plivo.com/docs/voice/api/calls#create-a-call)
* [Plivo Audio Streaming reference](https://www.plivo.com/docs/voice-agents/audio-streaming/concepts/audio-streaming-reference)
* [Plivo signature validation](https://www.plivo.com/docs/voice/concepts/signature-validation)
* [Deepgram Voice Agent Integration on Plivo](https://www.plivo.com/docs/voice-agents/audio-streaming/integration-guides/voice-agent-pipelines/deepgram-voice-agent)
