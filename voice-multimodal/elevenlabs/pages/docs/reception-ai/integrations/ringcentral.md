---
title: "RingCentral"
source: https://elevenlabs.io/docs/reception-ai/integrations/ringcentral.md
path: docs/reception-ai/integrations/ringcentral
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# RingCentral

RingCentral has no direct SIP connection to Reception.ai. RingCentral only lets SIP devices register to it, using an outbound proxy and an authorization ID. Reception.ai's [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk) receives calls from your provider and doesn't register. Choose one of the options below.

| Option                                                        | Effort | Keeps your number on RingCentral |
| ------------------------------------------------------------- | ------ | -------------------------------- |
| [Forward to your receptionist](#forward-to-your-receptionist) | Low    | Yes                              |
| [Bridge with a PBX](#bridge-with-a-pbx)                       | High   | Yes                              |
| [Port your number to Twilio](#port-your-number-to-twilio)     | Medium | No                               |

## Forward to your receptionist

This is the quickest setup. Your receptionist answers on its own Reception.ai number, and RingCentral forwards calls to it.

### Get a receptionist number

Go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

### Forward calls in RingCentral

In the RingCentral Admin Portal, open the user, call queue, or site that owns the number. Under **Call Handling & Forwarding**, add your receptionist's number as a forwarding number. Forward every call, or only calls nobody answers after a few rings.

### Test it

Call your RingCentral number from another phone and check that your receptionist answers.

Callers keep dialing your RingCentral number. RingCentral may charge for forwarded minutes, and the receptionist sees the forwarded call's caller ID as RingCentral passes it.

## Bridge with a PBX

A self-hosted PBX such as FreePBX or Asterisk registers with RingCentral as a SIP phone and passes calls to Reception.ai over a SIP trunk. Use this if you need calls to stay on RingCentral's network without forwarding. It requires a server with a static public IP and someone comfortable running Asterisk.

### Get RingCentral SIP credentials

In the RingCentral Admin Portal, add a phone using **Existing Phone** (bring your own device) and choose **Other phone**. RingCentral shows the **SIP domain**, **Outbound proxy**, **User name**, **Password**, and **Authorization ID**.

### Register the PBX with RingCentral

On your PBX, create a SIP trunk that registers to the SIP domain through the outbound proxy, using the user name, password, and authorization ID. The authorization ID is not the same as the user name.

### Connect Reception.ai

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add your PBX's public IP address. Set **Outbound SIP address** to your PBX if you want transfers to go back through RingCentral.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter your RingCentral number, and select **Add SIP Trunk number**. Reception.ai shows the SIP servers to send calls to and the request URI to use.

### Route calls to Reception.ai

On your PBX, create a second trunk to one of those SIP servers over TCP or TLS, and route inbound calls from the RingCentral trunk to it. The request URI must start with the number in E.164 format, for example `+14155550123@`.

## Port your number to Twilio

If you can move the number off RingCentral, port it to Twilio and connect it with Reception.ai's [Twilio integration](/docs/reception-ai/phone-numbers/bring-your-own-number#twilio). Keep RingCentral active until the port completes, or the port can fail.

## Troubleshooting

| Problem                                         | What to check                                                                                                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Forwarded calls never reach the receptionist    | Call the receptionist's number directly. If that works, check the forwarding rule and its ring count in RingCentral.                                |
| PBX shows the RingCentral trunk as unregistered | Check that the authorization ID, not the user name, is in the authorization field, and that the outbound proxy and port match RingCentral's values. |
| Calls from the PBX are rejected                 | Add the PBX's public IP to **Inbound allowed addresses**, and send the number in E.164 format with a leading `+`.                                   |
| One-way or no audio                             | Open your PBX's RTP port range in the firewall and set its external IP address so media isn't sent to a private address.                            |
