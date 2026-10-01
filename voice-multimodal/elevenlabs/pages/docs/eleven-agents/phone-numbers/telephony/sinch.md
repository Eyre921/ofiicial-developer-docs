---
title: "Sinch SIP trunking"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/telephony/sinch.md
path: docs/eleven-agents/phone-numbers/telephony/sinch
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Sinch SIP trunking

> **Note**
>
> Before following this guide, consider reading the [ElevenLabs SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) and [Sinch Voice SIP trunking guide](https://developers.sinch.com/docs/voice/api-reference/sip-trunking).

## Overview

This guide explains how to connect a Sinch Voice application directly to ElevenLabs Agents. The integration lets you keep your Sinch numbers and routing while ElevenLabs handles the voice AI agent experience.

## How SIP trunking with Sinch works

A Sinch SIP Trunk is a two-way connection between the Sinch network and the ElevenLabs platform:

1. **Inbound calls**: A DID assigned to your Sinch Voice application receives a call. Sinch sends the `INVITE` to the ElevenLabs origination address configured as a static endpoint on the trunk's inbound settings.
2. **Outbound calls**: Calls initiated by ElevenLabs are sent to your application's fully qualified domain name (FQDN) SIP address, which Sinch routes to the PSTN.
3. **Authentication**: Sinch requires outbound authentication (SIP credentials) and supports ACL authentication (IP allowlisting) for traffic arriving on the trunk.

## Requirements

Before you start, make sure you have:

1. An active ElevenLabs account with an agent configured
2. A Sinch account with a voice application created in the [Sinch Build dashboard](https://dashboard.sinch.com/voice/apps)
3. At least one phone number (DID) purchased in Sinch and assigned to application

## Configuring inbound calls (Sinch to ElevenLabs)

Point your application's call forwarding at the ElevenLabs SIP address.

### Sign in to the Sinch Build dashboard

Log into your Sinch account and navigate to the application you want to connect.

### Add a static endpoint for ElevenLabs

In the applications's call forwarding settings, update the call events handler to `SIP Forwarding` add a static SIP URI that targets the ElevenLabs origination address:

* **DID**: the Sinch phone number you want to dial
* **Address**: `sip.rtc.elevenlabs.io`
* **Port and transport**: `5061/TLS`, `5060/TCP`

For example: `sip:15551234567@sip.rtc.elevenlabs.io:5061;transport=tls`.

If your ElevenLabs workspace uses an isolated data residency region, or the static IP SIP infrastructure, use the corresponding endpoint instead of `sip.rtc.elevenlabs.io`. See [data residency](/docs/overview/administration/data-residency) for available regions.

### Assign your DID to the application

Assign the phone number that should reach your agent to this application.

## Configuring outbound calls (ElevenLabs to Sinch)

For outbound calls, ElevenLabs sends a SIP `INVITE` to your Sinch application and authenticates against it.

### Note your Sinch region's FQDN

Retrieve your Sinch region's [SIP FDQN](https://developers.sinch.com/docs/voice/api-reference/sip-trunking#termination-uris). This is the termination address you enter in ElevenLabs. Enter the hostname only, with no `sip:` prefix.

### Enter SIP credentials

Copy your Sinch application's key and secret securely. This will be used as your username and password in ElevenLabs.

### Forwarding number

Your Sinch application will forward the call to it's forwarding address. In order to place an outbound call to the number specified in the out-bound call request, leave this field empty in your application settings.

## Complete setup in ElevenLabs

### Import the SIP trunk phone number

Follow the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) to import your Sinch number, using these settings:

| Setting            | Value                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------- |
| Phone number       | Your Sinch DID, for example `15551234567`                                             |
| Transport type     | TLS                                                                                   |
| Media encryption   | `Disabled` for TCP; `Allowed` or `Required` when the trunk is set up for TLS and SRTP |
| Address            | Your Sinch trunk FQDN, hostname only                                                  |
| SIP trunk username | Sinch application key                                                                 |
| SIP trunk password | Sinch application secret                                                              |

Keep the transport and encryption settings consistent on both sides.

### Assign an agent

Assign an agent to the number in the [Phone Numbers dashboard](https://elevenlabs.io/app/agents/phone-numbers). Inbound calls to the DID now reach that agent.

### Test an outbound call

Place a call from the agent through your Sinch application either through the phone number menu or the outbound-call api:

```bash
curl -X POST https://api.elevenlabs.io/v1/convai/sip-trunk/outbound-call \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "agent_7101k5zvyjhmfg983brhmhkd98n6",
    "agent_phone_number_id": "phnum_8901k4t9z5defmb8vh3e9361y7nj",
    "to_number": "+15551234567"
  }'
```

See [Outbound call via SIP trunk](/docs/eleven-agents/api-reference/sip-trunk/outbound-call) for the full request schema, and [Batch calls](/docs/eleven-agents/phone-numbers/batch-calls) for running outbound campaigns.

## Configuring transfers

Agents hand calls to a human using the [`transfer_to_number`](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number) system tool.

> **Warning**
>
> Only conference transfers work over a Sinch trunk. SIP REFER and blind transfers fail.

### Conference transfers

ElevenLabs dials the destination through your Sinch trunk, joins both parties in a conference, then drops the agent.

## Using Sinch Voice API v2 instead

The setup above gives ElevenLabs the whole voice path. If you need Sinch to own call control, Sinch Voice API v2 can answer a call, apply its own logic, and bridge a second leg to your ElevenLabs agent using SVAML, without a relay server. That model is a better fit when you want to insert Sinch features such as answering machine detection, call recording, or number masking before the agent joins, or when the agent is one step in a larger Sinch call flow.

See Sinch's [Integrate an ElevenLabs AI agent via SIP](https://developers.sinch.com/docs/voice-2.0/tutorials/elevenlabs-sip) tutorial for other typical scenarios.

## Troubleshooting

#### Inbound calls fail to connect

* Confirm the trunk's static inbound endpoint targets `sip.rtc.elevenlabs.io` on the port and transport you intend to use.
* Confirm the DID is assigned to that trunk.
* Check that the number in ElevenLabs matches what Sinch sends, including the leading `+`.
* Wait at least 60 seconds after changing endpoints or ACLs, then retest.
* Verify your firewall allows SIP signaling on 5060 for TCP or 5061 for TLS, and does not block RTP.

#### Outbound calls receive 403 or 407 responses

* Confirm the SIP trunk username and password in ElevenLabs match the credentials on the Sinch trunk.
* Check that the **Address** field contains only the trunk FQDN, with no `sip:` prefix.
* Confirm country permissions are enabled on the trunk for the destination country.
* Confirm the caller ID you are presenting is a number Sinch accepts on that trunk.
* If you are relying on ACL authentication, remember that ElevenLabs signaling arrives from a distributed pool of addresses. Switch to digest authentication or move to the static IP infrastructure.

#### One-way audio or no audio

* Confirm your firewall allows RTP over UDP in both directions and is not restricted to specific static addresses.
* Check that media encryption matches: a TLS Sinch trunk expects SRTP, so set media encryption to `Allowed` or `Required` in ElevenLabs.
* Test with TCP and media encryption disabled to isolate whether the problem is TLS or SRTP related.
* Verify G711 is offered on the trunk. ElevenLabs supports G711 and G722.

#### Calls do not clear after the agent hangs up

A `481` response to a `BYE` usually means the request reached a SIP server without the dialog state for that call. Send in-dialog requests to the `Contact` URI returned in the `200 OK` rather than to the shared `sip.rtc.elevenlabs.io` address. If `BYE` or `REFER` over TLS fails certificate validation, add the FQDN your trunk's certificate is issued for to the **Remote domains** field in the phone number settings.

## FAQ

#### Which transport should I use?

TLS on 5061 for production, paired with SRTP media on the Sinch trunk. TCP on 5060 is a reasonable starting point for validation. UDP is experimental on ElevenLabs and should not carry production traffic.

#### Which audio codecs are compatible?

ElevenLabs supports G711 (8 kHz) and G722 (16 kHz). Keep G711 offered on the Sinch trunk as the common denominator.

#### How do I pass caller context into the conversation?

Custom `X-` headers on the inbound `INVITE` are exposed as dynamic variables, with `X-Contact-ID` becoming `{{sip_contact_id}}`, for example. `X-Call-ID` and `X-Caller-ID` map to `system__call_sid` and `system__caller_id`. See [SIP trunking](/docs/eleven-agents/phone-numbers/sip-trunking) for the full normalization rules.

## Useful links

* [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking)
* [SIP reference](/docs/eleven-agents/phone-numbers/sip-reference)
* [Transfer to number](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number)
* [Sinch Voice API v2: integrate an ElevenLabs AI agent via SIP](https://developers.sinch.com/docs/voice-2.0/tutorials/elevenlabs-sip)
