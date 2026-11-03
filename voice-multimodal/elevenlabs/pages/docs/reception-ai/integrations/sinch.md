---
title: "Sinch"
source: https://elevenlabs.io/docs/reception-ai/integrations/sinch.md
path: docs/reception-ai/integrations/sinch
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Sinch

Sinch forwards calls to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). Your numbers stay on Sinch, and Sinch bills you for the minutes. Sinch uses one Voice app to send calls to Reception.ai and a second app to carry transfers back out.

## Before you start

* A Sinch account with at least one phone number.
* Sinch's SIP signaling IP ranges for your region, listed under [IP allowlisting](https://developers.sinch.com/docs/voice/api-reference/sip-trunking#ip-allowlisting) in Sinch's documentation. Reception.ai only accepts calls from addresses you allow.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add Sinch's SIP signaling ranges for the regions you use. Leave the inbound username and password empty; Sinch's SIP forwarding doesn't send credentials.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter your Sinch number with its country code, and select **Add SIP Trunk number**. Reception.ai shows the SIP servers and the request URI to use, over TCP or TLS.

### Forward calls in Sinch

In the Sinch Build Dashboard, go to **Voice and Video** → **Apps** and open (or create) the app your number belongs to. Under **Settings**, set **Handle call events with** to **SIP Forwarding** and enter a forwarding URI that uses the Reception.ai SIP server, for example:

`sip:{number}@SIP_SERVER:5061;transport=tls`

Sinch replaces `{number}` with the number that was called. Use port `5060` with `transport=tcp` if you prefer TCP. Don't leave out the `transport` parameter: Sinch uses UDP by default, which Reception.ai doesn't accept.

### Assign your number

Assign your Sinch number to the app that forwards to Reception.ai.

### Set up transfers

Your receptionist transfers calls by placing a new call through your outbound trunk. In Sinch, create a second app for SIP termination and note its **Application Key** and **Application Secret**. In the Reception.ai SIP trunk, set:

| Setting                  | Value                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Outbound SIP address** | Your region's Sinch termination host, for example `use1.vp.sip.sinch.com` (North America) or `euc1.vp.sip.sinch.com` (Europe) |
| **Outbound username**    | The termination app's Application Key                                                                                         |
| **Outbound password**    | The termination app's Application Secret                                                                                      |
| **Transport** (advanced) | TCP                                                                                                                           |

The full list of regional hosts is under [Termination URIs](https://developers.sinch.com/docs/voice/api-reference/sip-trunking) in Sinch's documentation.

### Test it

Call your Sinch number from another phone and check that your receptionist answers. Then ask to be transferred.

> **Warning**
>
> The Application Secret lets anyone place calls billed to your Sinch account. Keep it out of shared
> documents, and regenerate it in Sinch if it leaks.

## Troubleshooting

| Problem                         | What to check                                                                                                                                                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calls fail before ringing       | Check that the forwarding URI ends in `;transport=tls` or `;transport=tcp` and uses the matching port, `5061` or `5060`.                                                                                                              |
| Calls are rejected              | Add Sinch's signaling ranges to **Inbound allowed addresses**. The request URI must start with the number in E.164 format, for example `+14155550123`. If Sinch sends it without `+`, change the forwarding URI to `sip:+{number}@…`. |
| The receptionist doesn't answer | Make sure the number is added on the receptionist's **Phone** tile and assigned to the forwarding app in Sinch.                                                                                                                       |
| One-way or no audio             | Sinch offers encrypted media (SRTP) when calls arrive over TLS. Check that **Media encryption** in the trunk's advanced settings allows it, or switch to TCP.                                                                         |
| Transfers fail                  | Check the outbound host, key and secret, and that the transport is TCP. Sinch only accepts caller IDs that are Sinch numbers or verified in the Build Dashboard.                                                                      |
