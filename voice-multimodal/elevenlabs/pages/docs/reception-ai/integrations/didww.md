---
title: "DIDWW"
source: https://elevenlabs.io/docs/reception-ai/integrations/didww.md
path: docs/reception-ai/integrations/didww
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# DIDWW

DIDWW sends calls to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). Your numbers stay on DIDWW, and DIDWW bills you for the minutes.

## Before you start

* A DIDWW account with at least one DID number that has capacity for calls.
* DIDWW's SIP signaling IP addresses, listed in the [SIP connectivity reference](https://doc.didww.com/voice/inbound-trunks/sip-trunks/sip-connectivity-reference.html). DIDWW documents these as fixed addresses. Reception.ai only accepts calls from addresses you allow.
* For transfers: DIDWW outbound trunks, which DIDWW must approve for your account.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add every DIDWW signaling IPv4 address. DIDWW may deliver a call from any of its locations, so add them all, not only the nearest one.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter your DIDWW number with its country code, and select **Add SIP Trunk number**. Reception.ai shows the SIP servers to send calls to, over TCP or TLS.

### Create an inbound SIP trunk in DIDWW

In the DIDWW User Panel, go to **Voice** → **Inbound Trunks**, select **Create New**, and choose **SIP Trunk**. Enter a name, set **Type** to **Static Endpoint**, and fill in:

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| **Host**               | The Reception.ai SIP server host, without `sip:` or a port |
| **User Part of R-URI** | `+{DID}`                                                   |
| **Port**               | `5060` for TCP, or `5061` for TLS                          |
| **Transport**          | **TCP** or **TLS** (the default, UDP, doesn't work)        |

DIDWW's `{DID}` placeholder inserts the called number in E.164 format without the leading `+`. Typing `+` in front of it gives the format Reception.ai requires, for example `+14155550123`.

### Assign your number

Go to **Phone Numbers** → **My Numbers**, select the number's **Trunk** column, choose the new trunk, and select **Confirm**.

### Set up transfers (optional)

Skip this step if your receptionist doesn't need to transfer calls. Inbound calls work without it.

Your receptionist transfers calls by placing a new call through your outbound trunk. In DIDWW, go to **Voice** → **Outbound Trunks** and select **Create New**. Use the **Credentials & IP-Based** authentication method, then open the trunk's **Credentials** to find its username, password and hosts. In the Reception.ai SIP trunk, set:

| Setting                  | Value                                                                          |
| ------------------------ | ------------------------------------------------------------------------------ |
| **Outbound SIP address** | A DIDWW outbound host from the credentials, for example `nyc.us.out.didww.com` |
| **Outbound username**    | The trunk's username                                                           |
| **Outbound password**    | The trunk's password                                                           |
| **Transport** (advanced) | TCP or TLS                                                                     |

DIDWW also checks where outbound calls come from, and requires at least one **Allowed SIP IP address**. Reception.ai places calls from a changing pool of addresses, so the only entry that works is `0.0.0.0/0`, which leaves the username and password as the only protection.

> **Warning**
>
> With `0.0.0.0/0` allowed, anyone with the trunk's password can place calls billed to your DIDWW
> account. Use the trunk only for Reception.ai, set a capacity limit and a 24-hour spending limit,
> and restrict destinations to the countries you transfer to.

### Test it

Call your DIDWW number from another phone and check that your receptionist answers. If you set up transfers, ask to be transferred.

## Troubleshooting

| Problem                         | What to check                                                                                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calls fail before ringing       | Check that **Transport** is TCP or TLS and that **Port** matches it. With **Port** empty, DIDWW looks up DNS SRV records and may fall back to port 5060. |
| Calls are rejected              | Add every DIDWW signaling address to **Inbound allowed addresses**, and check that **User Part of R-URI** is `+{DID}`.                                   |
| The receptionist doesn't answer | Make sure the number is added on the receptionist's **Phone** tile and assigned to the trunk in **My Numbers**.                                          |
| One-way or no audio             | Check that **SRTP Mode** on the DIDWW trunk matches **Media encryption** in the Reception.ai trunk's advanced settings.                                  |
| Transfers fail                  | Check the outbound host, username and password, the trunk's allowed SIP IPs, and its destination and caller ID settings in DIDWW.                        |
