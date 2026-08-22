---
title: "Azure Communication Services"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/microsoft-teams/azure-communication-services.md
path: docs/eleven-agents/phone-numbers/microsoft-teams/azure-communication-services
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Azure Communication Services

## Overview

This approach gives your agent a **phone number**. A caller dials it, [Azure Communication Services](https://learn.microsoft.com/en-us/azure/communication-services/concepts/call-automation/call-automation) (ACS) answers with **bidirectional media streaming**, and a small bridge relays PCM audio between ACS and the ElevenLabs agent using the standard [agent WebSocket protocol](/docs/eleven-agents/libraries/web-sockets). It's the contact-center / IVR pattern — the same shape as a [SIP trunking](/docs/eleven-agents/phone-numbers/sip-trunking) deployment, with ACS as the carrier.

It also connects to Teams two ways: a Teams user with a Calling Plan can dial the ACS number directly, or you can front the number with **Teams Phone Extensibility** so calls to a Teams resource account route into ACS.

ACS provisions PSTN numbers only in a [limited set of
countries](https://learn.microsoft.com/en-us/azure/communication-services/concepts/numbers/sub-eligibility-number-capability).
If a number isn't available in your region, use a SIP provider with [SIP
trunking](/docs/eleven-agents/phone-numbers/sip-trunking) instead, or the [Graph calling
bot](/docs/eleven-agents/phone-numbers/microsoft-teams/graph-media-bot).

## How it works

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e77a27148e217fc7dc06c25007c1c141913fc831cbfe8a2f57405137646271af/assets/images/conversational-ai/teams-acs-architecture.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T100015Z&X-Amz-Expires=604800&X-Amz-Signature=946f0fcefd95834b7a31e43f5f07eee9101daefffd2f61f7af23939cea99bf93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="A caller dials the ACS number; ACS fires IncomingCall via Event Grid to the bridge, which answers with bidirectional PCM 16k media streaming and relays it to the ElevenLabs agent over a WebSocket" />

Audio is **PCM 16 kHz mono** on both legs (the agent's input/output format is `pcm_16000`), so it passes through as base64 with no resampling.

The bridge exposes these routes:

| Route                    | Purpose                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| `POST /api/incomingCall` | Event Grid webhook: validates the subscription, then `answer_call` with media streaming   |
| `POST /api/callbacks`    | Call Automation lifecycle events (`CallConnected`, `CallDisconnected`, `AddParticipant*`) |
| `GET\|WS /ws`            | ACS media-streaming socket ↔ ElevenLabs                                                   |
| `POST /api/outboundCall` | Optional: place an outbound call that connects the answerer to the agent                  |

## Requirements

1. A **paid** Azure subscription (MCA / EA / Pay-As-You-Go) — free/trial/sponsorship subs cannot buy numbers.
2. An [Azure Communication Services resource](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource).
3. An HTTPS host for the bridge with a public WebSocket (Azure Container Apps, App Service, or a VM).
4. An [ElevenLabs agent](/docs/eleven-agents/quickstart) set to **PCM 16000 Hz** on both legs: TTS output format on the **Voice** tab, user input audio format on the **Advanced** tab.

## Permissions & roles

| Scope              | Role / permission                              | Why                                                                 |
| ------------------ | ---------------------------------------------- | ------------------------------------------------------------------- |
| Azure RBAC         | **Contributor** on the resource group          | create the ACS resource, Container App, and Event Grid subscription |
| Azure subscription | **Owner or Contributor** on the subscription   | purchase phone numbers (the buy option is disabled otherwise)       |
| Billing            | **MCA / EA / Pay-As-You-Go** subscription type | free, trial, sponsorship, and Dev subscriptions cannot buy numbers  |

Under **Contributor** (not Owner), `az containerapp up` can't create the managed-identity ACR pull
role assignment. Enable the registry admin user and attach it instead — see the warning in Step 2.

## Step 1 — Provision the ACS resource and number

```bash
RG=my-rg
# Register providers (once)
az provider register -n Microsoft.Communication --wait
az provider register -n Microsoft.EventGrid --wait

# Create the ACS resource
az communication create --name my-acs --resource-group $RG \
  --location global --data-location unitedstates
```

Buy a number in the resource (Portal → your ACS resource → **Phone numbers → Get**, or the [phone-numbers SDK](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/telephony/get-phone-number)). For an agent that **answers** calls, a number with **inbound calling** is enough; add **outbound** capability if you also want `/api/outboundCall`.

![The ACS resource Phone numbers blade listing active numbers with their calling
capabilities](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9d14034ee9f81e2ebcf64e30371f914ef6f87a8da30ac250e702662f2e5e1cc1/assets/images/conversational-ai/teams-acs-phone-number.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T100015Z&X-Amz-Expires=604800&X-Amz-Signature=632bc7c271b26957640a263917e2767a4992a409544cafc160fa610085f47cf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To verify from the CLI (requires `az extension add --name communication`), and to fetch the connection string the bridge uses as `ACS_CONNECTION_STRING`:

```bash
CONN=$(az communication list-key -n my-acs -g $RG --query primaryConnectionString -o tsv)
az communication phonenumber list --connection-string "$CONN" --query "[].phoneNumber"
```

## Step 2 — Deploy the bridge

The bridge is a small Flask + `flask-sock` app using `azure-communication-callautomation`. The core of the inbound flow:

```python title="bridge.py (excerpt)"
from azure.communication.callautomation import (
    CallAutomationClient, MediaStreamingOptions, StreamingTransportType,
    MediaStreamingContentType, MediaStreamingAudioChannelType, AudioFormat,
)

@app.route("/api/incomingCall", methods=["POST"])
def incoming_call():
    for event in request.get_json():
        # Event Grid subscription validation handshake
        if event.get("eventType") == "Microsoft.EventGrid.SubscriptionValidationEvent":
            return jsonify({"validationResponse": event["data"]["validationCode"]})

        if event.get("eventType") == "Microsoft.Communication.IncomingCall":
            client = CallAutomationClient.from_connection_string(ACS_CONNECTION_STRING)
            client.answer_call(
                incoming_call_context=event["data"]["incomingCallContext"],
                callback_url=f"https://{HOST}/api/callbacks",
                media_streaming=MediaStreamingOptions(
                    transport_url=f"wss://{HOST}/ws",
                    transport_type=StreamingTransportType.WEBSOCKET,
                    content_type=MediaStreamingContentType.AUDIO,
                    audio_channel_type=MediaStreamingAudioChannelType.MIXED,
                    start_media_streaming=True,
                    enable_bidirectional=True,
                    audio_format=AudioFormat.PCM16_K_MONO,
                ),
            )
    return jsonify({"status": "ok"})
```

On the `/ws` socket, relay PCM16 both ways: forward ACS `AudioData` frames to ElevenLabs as `{"user_audio_chunk": "<base64>"}`, and send the agent's audio back as `{"Kind":"AudioData","AudioData":{"Data":"<base64>"},"StopAudio":null}`. The first frame ACS sends is `AudioMetadata` (the negotiated format) — log it and ignore it. The ElevenLabs side is the standard [agent WebSocket protocol](/docs/eleven-agents/libraries/web-sockets).

ACS uses different JSON casing per direction: inbound frames it **sends** are camelCase (`kind`,
`audioData.data`), while outbound frames it **expects** are PascalCase (`Kind`, `AudioData.Data`,
`StopAudio`). Keep the two cases distinct — the relay below mirrors this.

```python title="bridge.py — media relay"
import asyncio, json, os, queue, threading, websockets
from flask_sock import Sock

sock = Sock(app)
AGENT_ID = os.environ["ELEVENLABS_AGENT_ID"]
# US default; data residency: wss://api.eu.residency.elevenlabs.io, .in., or .sg.
EL_ORIGIN = os.environ.get("ELEVENLABS_ORIGIN", "wss://api.elevenlabs.io")
EL_WS = f"{EL_ORIGIN}/v1/convai/conversation?agent_id={AGENT_ID}"

@sock.route("/ws")
def media_stream(ws):
    loop = asyncio.new_event_loop()
    el = {"ws": None}
    to_acs = queue.Queue()  # outbound frames; only this handler thread touches `ws`

    async def el_session():
        async with websockets.connect(EL_WS) as elws:
            el["ws"] = elws
            await elws.send(json.dumps({"type": "conversation_initiation_client_data"}))
            async for msg in elws:
                data = json.loads(msg)
                kind = data.get("type")
                if kind == "audio":  # agent audio -> caller
                    b64 = data["audio_event"]["audio_base_64"]
                    to_acs.put({"Kind": "AudioData", "AudioData": {"Data": b64}, "StopAudio": None})
                elif kind == "ping":
                    await elws.send(json.dumps({"type": "pong", "event_id": data["ping_event"]["event_id"]}))
                elif kind == "interruption":  # barge-in
                    to_acs.put({"Kind": "StopAudio", "AudioData": None, "StopAudio": {}})

    threading.Thread(target=lambda: loop.run_until_complete(el_session()), daemon=True).start()

    # Keep all ACS-socket I/O on this one thread: receive with a short timeout,
    # then drain any audio the ElevenLabs thread queued. Sending from the other
    # thread would race flask-sock and corrupt the stream.
    try:
        while True:
            raw = ws.receive(timeout=0.02)  # None when no frame arrived this tick
            if raw:
                evt = json.loads(raw)
                if evt.get("kind") == "AudioData" and el["ws"]:  # caller audio -> agent
                    asyncio.run_coroutine_threadsafe(
                        el["ws"].send(json.dumps({"user_audio_chunk": evt["audioData"]["data"]})), loop)
            while not to_acs.empty():
                ws.send(json.dumps(to_acs.get_nowait()))
    except Exception:
        pass  # ACS socket closed
```

This relay is intentionally minimal. For production, add logging, reconnection, and graceful
teardown. The full message reference is in the [WebSocket
docs](/docs/eleven-agents/libraries/web-sockets).

`EL_WS` connects to a **public** agent. For a private agent, have the bridge request a short-lived
signed URL server-side — `GET /v1/convai/conversation/get-signed-url?agent_id=...` with your API
key — and connect to the returned URL instead. On [data
residency](/docs/overview/administration/data-residency), set `ELEVENLABS_ORIGIN` to your
residency host (`wss://api.eu.residency.elevenlabs.io`, `.in.`, or `.sg.`) — signed-URL requests
use the matching `https://` host.

Deploy to Azure Container Apps and capture the public FQDN:

```bash
az containerapp up --name acs-el-bridge --resource-group $RG \
  --source . --ingress external --target-port 8080 \
  --env-vars ELEVENLABS_AGENT_ID=$AGENT_ID \
    ELEVENLABS_ORIGIN=wss://api.elevenlabs.io

FQDN=$(az containerapp show -n acs-el-bridge -g $RG \
  --query properties.configuration.ingress.fqdn -o tsv)
```

Then set `BRIDGE_PUBLIC_HOST=$FQDN` and the ACS connection string (as a secret) on the app.

Under **Contributor** (not Owner), `az containerapp up` cannot create the managed-identity ACR
pull role. Enable the registry admin user (`az acr update --admin-enabled true`) and attach it
with `az containerapp registry set`, then `az containerapp update --image ...`.

## Step 3 — Route IncomingCall to the bridge

Create an Event Grid subscription on the ACS resource that posts `IncomingCall` to the bridge. The bridge's validation handshake (above) completes the subscription automatically.

```bash
ACS_ID=$(az communication show -n my-acs -g $RG --query id -o tsv)
az eventgrid event-subscription create \
  --name acs-incomingcall \
  --source-resource-id "$ACS_ID" \
  --endpoint "https://$FQDN/api/incomingCall" \
  --endpoint-type webhook \
  --included-event-types Microsoft.Communication.IncomingCall

# Verify — should print "Succeeded"
az eventgrid event-subscription show --name acs-incomingcall \
  --source-resource-id "$ACS_ID" --query provisioningState -o tsv
```

The subscription appears under the ACS resource's **Events** blade:

![The Events blade of the ACS resource listing the acs-incomingcall webhook subscription filtered
to
Microsoft.Communication.IncomingCall](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f310aed9637e06b81906ca188350e3e721aaa5f4de69af2b3b6e7d157817a1ea/assets/images/conversational-ai/teams-acs-event-grid.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T100015Z&X-Amz-Expires=604800&X-Amz-Signature=27b5e74f5ccd732894671bc2c5213e2a78b817bd9506e2d912e56535fc92c2fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Dial the number — the agent answers.

## Connecting it to Teams

* **Direct dial:** a Teams user with Teams Phone + a Calling Plan can dial the ACS number like any external number.
* **Teams resource account (TPE):** bind a Teams resource account to the ACS resource with [Teams Phone Extensibility](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/tpe/teams-phone-extensibility-quickstart) so calls to the resource account fire the same `IncomingCall` → bridge flow.

## End of call

When the agent ends the conversation (e.g. its **End Call** tool), ElevenLabs closes the WebSocket. Hang up the ACS leg so the caller isn't left on a dead line:

```python
CallAutomationClient.from_connection_string(ACS_CONNECTION_STRING) \
    .get_call_connection(call_connection_id).hang_up(is_for_everyone=True)
```

## Warm transfer to a human

ElevenLabs' native transfer tools only apply when ElevenLabs owns the telephony, so here the agent fires a **custom client tool** (e.g. `transfer_to_human`) that your bridge handles by **adding** the human to the live call with `add_participant` (warm) rather than a blind transfer:

```python
conn = client.get_call_connection(call_connection_id)
conn.add_participant(
    PhoneNumberIdentifier(human_number),
    source_caller_id_number=PhoneNumberIdentifier(your_outbound_number),
    invitation_timeout=30,
)
# then mute the bot and skip the end-of-call hangup so the human's leg survives
```

ACS emits `AddParticipantSucceeded` / `AddParticipantFailed` callbacks to `/api/callbacks`. Return a `client_tool_result` to the agent so it can say its handoff line. See [system tools](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number) for the agent-side configuration.

Set the transfer guard the instant the tool fires (before calling `add_participant`), or a fast EL
WebSocket close can race the hangup and drop the call before the human joins.

## Troubleshooting

#### No IncomingCall reaches the bridge

Confirm the Event Grid subscription provisioned (`provisioningState: Succeeded`) and the
bridge's `/api/incomingCall` returned the validation echo. Confirm the number has inbound
calling and is in the same ACS resource the subscription is on. On the subscription's
**Filters** tab, the event types must include **Incoming Call**:

![The event subscription Filters tab with the event type filtered to Incoming
Call](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c7026e86d96551d713e4fd7d5753062f643fcd6a67b455866bb8f1bbb6b57eb1/assets/images/conversational-ai/teams-acs-event-grid-filter.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T100015Z&X-Amz-Expires=604800&X-Amz-Signature=b495a86b8b5235e1be320cd33f235d8567151f54f334a039683e10ce9106bb15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### \`CreateCallFailed\` / \`AddParticipantFailed\` for an international number

ACS outbound to some destinations (e.g. India) is restricted/intermittent. Use a supported
destination, or front the human leg with a SIP/Operator number. The bridge logic is unaffected —
it's a carrier-level failure on the outbound leg.

#### Audio is distorted or wrong speed

Both sides must be PCM 16 kHz mono. Set the agent's input/output format to `pcm_16000`; the
bridge logs the negotiated format from `conversation_initiation_metadata`.

#### Can't buy a number / number not available in my country

Number purchase requires a paid subscription type (MCA/EA/PAYG). If ACS doesn't offer numbers in
your country, use a [SIP](/docs/eleven-agents/phone-numbers/sip-trunking) provider instead.

## Useful links

* [ACS Call Automation overview](https://learn.microsoft.com/en-us/azure/communication-services/concepts/call-automation/call-automation)
* [ACS audio streaming](https://learn.microsoft.com/en-us/azure/communication-services/concepts/call-automation/audio-streaming-concept)
* [Call control actions (transfer / add participant)](https://learn.microsoft.com/en-us/azure/communication-services/how-tos/call-automation/actions-for-call-control)
* [Teams Phone Extensibility](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/tpe/teams-phone-extensibility-quickstart)
* [Agent WebSocket protocol](/docs/eleven-agents/libraries/web-sockets)
* [ElevenLabs SIP trunking](/docs/eleven-agents/phone-numbers/sip-trunking)
