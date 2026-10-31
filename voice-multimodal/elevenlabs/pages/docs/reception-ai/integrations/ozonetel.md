---
title: "Ozonetel"
source: https://elevenlabs.io/docs/reception-ai/integrations/ozonetel.md
path: docs/reception-ai/integrations/ozonetel
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Ozonetel

Ozonetel trunks register with a SIP username and password, and send calls over UDP without a `+91` prefix. Reception.ai's [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk) doesn't register, accepts TCP or TLS only, and needs numbers in E.164 format. Because of this, forwarding is the setup that works for most Ozonetel accounts.

## Forward to your receptionist

### Get a receptionist number

Go to **Receptionists**, select the **Phone** tile, and get a number. Reception.ai offers Indian numbers after a [regulatory request](/docs/reception-ai/phone-numbers/international-numbers).

### Forward your Ozonetel number

In Ozonetel, route the DID's calls to your receptionist's number, for example from an IVR or campaign that transfers to an external phone number. If your account doesn't offer this, ask Ozonetel support to forward the DID.

### Test it

Call your Ozonetel number from another phone and check that your receptionist answers.

## Connect over SIP

A direct SIP trunk only works if Ozonetel can send calls to Reception.ai in the format it accepts. Confirm the following with Ozonetel support before you start:

* Calls are sent to a SIP server over TCP or TLS, not UDP.
* The request URI starts with the number in E.164 format, for example `+918011111112`.
* Calls come from fixed IP addresses that you can allow.

If Ozonetel confirms, set up the trunk:

1. Go to **Integrations**, select **Add integration**, choose **SIP Trunk**, and add Ozonetel's IP addresses under **Inbound allowed addresses**.
2. Go to **Receptionists**, select the **Phone** tile, enter the number with `+91`, and select **Add SIP Trunk number**.
3. Send Ozonetel the SIP server and request URI that Reception.ai shows for the number.

> **Note**
>
> ElevenAgents guides for Ozonetel ask for an India residency workspace and static SIP. Those
> settings don't exist in Reception.ai.

## Troubleshooting

| Problem                                      | What to check                                                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Forwarded calls never reach the receptionist | Call the receptionist's number directly. If that works, check the forwarding rule in Ozonetel.                     |
| SIP calls are rejected                       | Check that Ozonetel sends `+91` in the request URI and that its IP addresses are in **Inbound allowed addresses**. |
| SIP calls fail before ringing                | Ozonetel may be sending over UDP. Ask them to use TCP or TLS.                                                      |
| Calls drop when it's busy                    | Each Ozonetel channel carries one call. Ask Ozonetel for more channels.                                            |
