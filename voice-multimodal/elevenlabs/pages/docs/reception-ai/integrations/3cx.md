---
title: "3CX"
source: https://elevenlabs.io/docs/reception-ai/integrations/3cx.md
path: docs/reception-ai/integrations/3cx
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# 3CX

Your 3CX system keeps its carrier and numbers, and passes the calls you choose to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). You add a generic IP-based trunk in 3CX that points at Reception.ai, then forward a number to it.

## Before you start

* 3CX V20 on a dedicated install: self-hosted, on-premise, or a dedicated instance hosted by 3CX. Generic SIP trunks aren't available on the shared (multi-tenant) free and SMB plans.
* A static public IP address for the 3CX server. Reception.ai only accepts calls from addresses you allow.
* Someone comfortable with 3CX trunks, outbound rules and firewall settings.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add the 3CX server's public IP address. Leave the inbound username and password empty: an IP-based 3CX trunk doesn't authenticate.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter the number callers dial, with its country code, and select **Add SIP Trunk number**. Reception.ai shows the SIP server host to send calls to.

### Create the trunk in 3CX

In the 3CX Admin Console, go to **Voice & Chat** and select **Add Trunk**. Choose the **Generic** country and the generic SIP trunk template, then set:

| Field                                       | Value                                         |
| ------------------------------------------- | --------------------------------------------- |
| **Registrar/Server/Gateway Hostname or IP** | The Reception.ai SIP server host, port `5060` |
| **Authentication**                          | **Do not require - IP Based**                 |
| **Transport** (on the **Options** tab)      | **TCP**                                       |

Use TCP. 3CX only supports TLS on trunks that authenticate with a username and password, and Reception.ai's SIP trunk doesn't register.

In the trunk's caller ID settings, let 3CX pass the original caller's number. Otherwise your receptionist sees your main number on every call.

### Add an outbound rule that sends +E.164

Go to **Outbound Rules** and add a rule for numbers starting with an unused prefix, such as `999`. Set **Route 1** to the Reception.ai trunk, strip `3` digits, and prepend `+`. A call to `99914155550123` then leaves the trunk as `+14155550123`, which is the format Reception.ai requires.

### Forward calls to Reception.ai

3CX V20 can't send a DID straight to an external number. Create a user (or use an existing extension) that only exists for this, assign your DID to it, and forward all its calls to `999` followed by the number in E.164 format without `+`, for example `99914155550123`. You can also reach that extension from an IVR option or a queue's no-answer destination.

### Check the firewall

Open 3CX's RTP port range (UDP) in your firewall so audio from Reception.ai reaches the server. Run the 3CX firewall check if you're unsure.

### Test it

Call your DID from another phone and check that your receptionist answers.

## Limitations

* **Transfers.** Your receptionist transfers calls by placing a new call to the **Outbound SIP address**. Point it at your SIP carrier, using a carrier account that accepts a username and password. Routing transfers back into 3CX isn't covered here: an IP-based 3CX trunk matches calls by source address, and Reception.ai calls from a changing pool of addresses.
* **No TLS.** 3CX doesn't support TLS on IP-based trunks, so signaling between 3CX and Reception.ai uses TCP.
* **Your 3CX system carries every call twice**, once from the carrier and once to Reception.ai, so your license needs enough simultaneous calls.

## Troubleshooting

| Problem                                              | What to check                                                                                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Calls fail before ringing                            | Check that the trunk's transport is TCP and the port is `5060`.                                                                    |
| Calls are rejected                                   | Add the 3CX server's public IP to **Inbound allowed addresses**, and check that the outbound rule prepends `+` to the full number. |
| Calls go out through your carrier instead            | Make sure the forwarding number starts with the rule's prefix and the rule sits above your other outbound rules.                   |
| The receptionist sees your main number as the caller | Let the Reception.ai trunk pass the original caller ID.                                                                            |
| One-way or no audio                                  | Open the RTP port range in your firewall and run the 3CX firewall check.                                                           |
