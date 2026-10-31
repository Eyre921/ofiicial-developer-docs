---
title: "Telnyx"
source: https://elevenlabs.io/docs/reception-ai/integrations/telnyx.md
path: docs/reception-ai/integrations/telnyx
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Telnyx

Telnyx sends calls to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). Your numbers stay on Telnyx, and Telnyx bills you for the minutes.

## Before you start

* A Telnyx account with at least one phone number.
* Telnyx's SIP signaling IP addresses, listed in Telnyx's documentation. Reception.ai only accepts calls from addresses you allow.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add Telnyx's signaling IP addresses. Leave the inbound username and password empty unless your Telnyx connection authenticates with credentials.

To let your receptionist transfer calls back out through Telnyx, set **Outbound SIP address** to `sip.telnyx.com` and enter the outbound credentials from your Telnyx connection.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter your Telnyx number, and select **Add SIP Trunk number**. Reception.ai shows the SIP servers to send calls to.

### Create a connection in Telnyx

In the Telnyx Mission Control Portal, go to **Voice** → **SIP Trunking** and create a connection with **FQDN** authentication. Add one of the Reception.ai SIP servers as the FQDN, with transport **TCP** or **TLS**.

### Send numbers in E.164 format

In the connection's inbound settings, set the destination number format to **+E.164**. Reception.ai rejects calls whose request URI doesn't start with the number in E.164 format, for example `+14155550123`.

### Assign your number

In **Numbers** → **My Numbers**, set the number's connection to the one you just created.

### Test it

Call the number from another phone and check that your receptionist answers.

## Troubleshooting

| Problem                         | What to check                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Calls fail before ringing       | Check that the FQDN matches a Reception.ai SIP server exactly and that the transport is TCP or TLS, not UDP. |
| Calls are rejected              | Add every Telnyx signaling IP to **Inbound allowed addresses** and send the number as +E.164.                |
| The receptionist doesn't answer | Make sure the number is added on the receptionist's **Phone** tile, not only on the SIP trunk.               |
| One-way or no audio             | Check that **Media encryption** in the trunk's advanced settings matches the Telnyx connection.              |
