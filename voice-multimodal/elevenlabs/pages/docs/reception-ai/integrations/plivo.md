---
title: "Plivo"
source: https://elevenlabs.io/docs/reception-ai/integrations/plivo.md
path: docs/reception-ai/integrations/plivo
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Plivo

Plivo's Zentrunk sends calls to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). Your numbers stay on Plivo, and Plivo bills you for the minutes.

## Before you start

* A Plivo account with Zentrunk enabled and at least one phone number.
* Plivo's Zentrunk signaling IP addresses, listed in Plivo's documentation. Reception.ai only accepts calls from addresses you allow.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add Plivo's Zentrunk signaling IP addresses.

To let your receptionist transfer calls back out through Plivo, create an outbound trunk in Plivo with a credentials list. Set **Outbound SIP address** to its termination SIP domain, which ends in `zt.plivo.com`, and enter the credentials.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter your Plivo number, and select **Add SIP Trunk number**. Reception.ai shows the SIP servers to send calls to.

### Create an inbound trunk in Plivo

In the Plivo console, go to **Zentrunk** → **Inbound Trunks** and create a trunk. Set its primary URI to one of the Reception.ai SIP servers, with transport TCP or TLS.

### Assign your number

In **Phone Numbers**, open your number and attach it to the inbound trunk.

### Test it

Call the number from another phone and check that your receptionist answers.

## Troubleshooting

| Problem                         | What to check                                                                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calls are rejected              | Add every Zentrunk signaling IP to **Inbound allowed addresses**. The request URI must start with the number in E.164 format with a leading `+`. If Plivo sends it without `+`, ask Plivo support. |
| Calls fail before ringing       | Check the inbound trunk's URI and that the transport is TCP or TLS.                                                                                                                                |
| The receptionist doesn't answer | Make sure the number is added on the receptionist's **Phone** tile.                                                                                                                                |
| Transfers fail                  | Check the outbound SIP address and credentials against Plivo's outbound trunk.                                                                                                                     |
