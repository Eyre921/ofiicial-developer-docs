---
title: "Flowroute"
source: https://elevenlabs.io/docs/reception-ai/integrations/flowroute.md
path: docs/reception-ai/integrations/flowroute
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Flowroute

Flowroute sends calls to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). Your numbers stay on Flowroute, and Flowroute bills you for the minutes. Each number gets its own inbound route in Flowroute.

## Before you start

* A Flowroute account with at least one phone number.
* Flowroute's SIP signaling IP ranges, listed in the PoP table of [Configure an Inbound Route With Your Preferred PoP](https://support.bcmone.com/docs/configure-an-inbound-route-with-your-preferred-pop). Reception.ai only accepts calls from addresses you allow.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add the IP ranges of every Flowroute PoP in your region. Flowroute fails calls over between PoPs, so a call can come from any of them.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter your Flowroute number with its country code, and select **Add SIP Trunk number**. Reception.ai shows the request URI for the number, for example `sip:+14155550123@SIP_SERVER:5060;transport=tcp`.

### Create an inbound route in Flowroute

In the Flowroute Manage portal, go to **Interconnection** → **Inbound Routes** and fill in **Add new Route**:

| Field             | Value                                                 |
| ----------------- | ----------------------------------------------------- |
| **Route Alias**   | A name, for example `Reception 4155550123`            |
| **Route type**    | **URI**                                               |
| **Route value**   | The TCP request URI Reception.ai shows for the number |
| **Edge strategy** | The PoP closest to you                                |

Select **Add Route**. Because the route value includes the number itself, the request URI always starts with `+` and the country code, as Reception.ai requires. Create one route per number.

### Assign the route to your number

Go to **DIDs**, select the number, choose **Choose a DID Action** → **Set Route**, and select **Apply Action**. Pick the route you created and select **Set Route**.

### Set up transfers

Your receptionist transfers calls by placing a new call through your outbound trunk. Find your SIP credentials on the **Interconnection** → **Registration** page in Flowroute. In the Reception.ai SIP trunk, set:

| Setting                  | Value                                                       |
| ------------------------ | ----------------------------------------------------------- |
| **Outbound SIP address** | A Flowroute PoP, for example `us-west-or.sip.flowroute.com` |
| **Outbound username**    | Your Flowroute SIP username                                 |
| **Outbound password**    | Your Flowroute SIP password                                 |
| **Transport** (advanced) | TCP                                                         |

Use username and password authentication. Flowroute's IP-based authentication needs a tech prefix in front of every dialed number, which Reception.ai doesn't add, and Reception.ai calls from a changing pool of addresses.

### Test it

Call your Flowroute number from another phone and check that your receptionist answers. Then ask to be transferred.

> **Warning**
>
> Your Flowroute SIP password lets anyone place calls billed to your account. If you turn on
> **Disable Credentials** in Flowroute's fraud settings, transfers from Reception.ai stop working.

> **Note**
>
> Flowroute also offers TLS signaling as an advanced option with its own
> [requirements](https://support.bcmone.com/docs/tls-requirements). TCP works without extra setup.

## Troubleshooting

| Problem                         | What to check                                                                                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Calls fail before ringing       | Check that the route value ends in `;transport=tcp`. Without it, Flowroute may use UDP, which Reception.ai doesn't accept.                             |
| Calls are rejected              | Add every Flowroute PoP range in your region to **Inbound allowed addresses**, and check that the route value starts with `sip:+` and the full number. |
| A call reaches the wrong number | Each number needs its own route, because the number is part of the route value. Check which route is set on the DID.                                   |
| The receptionist doesn't answer | Make sure the number is added on the receptionist's **Phone** tile.                                                                                    |
| Transfers fail                  | Check the outbound SIP address, username and password, and that SIP credentials are still enabled in Flowroute.                                        |
