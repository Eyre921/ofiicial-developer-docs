---
title: "Bring your own number"
source: https://elevenlabs.io/docs/reception-ai/phone-numbers/bring-your-own-number.md
path: docs/reception-ai/phone-numbers/bring-your-own-number
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Bring your own number

Connect your own telephony provider to use numbers you already own, get numbers in countries Reception.ai does not offer, or send SMS from your own number. Reception.ai supports Twilio and SIP trunks.

Numbers you bring don't count toward your plan's phone number limit. Both integrations are available on every plan.

## Twilio

### Connect your Twilio account

### Open the Twilio integration

Go to **Integrations**, select **Add integration**, and choose **Twilio**.

### Enter your credentials

Enter your **Twilio Account SID** (starting with `AC`) and **Twilio Auth Token**, both found in the Twilio Console. Select **Enable**.

To rotate your Auth Token later, edit the integration and use **Rotate Auth Token**.

### Add a Twilio number to a receptionist

1. Go to **Receptionists** and select the **Phone** tile.
2. Choose a number from **Select a Twilio number**, then select **Add**.

Reception.ai updates the number's voice and SMS webhooks in Twilio to route calls to your receptionist. If your Twilio account has no numbers, buy one in the Twilio Console first.

Turn on **Enable inbound SMS** to route texts sent to the number to Reception.ai. This is required to process replies such as STOP.

Twilio numbers also enable [SMS sending](/docs/reception-ai/features/notifications#sms), [caller ID on transfers](/docs/reception-ai/receptionist/call-handling#caller-id-on-transfers), and transfers outside the US.

## SIP trunk

Use a SIP trunk to connect numbers from another carrier or your PBX.

### Connect your SIP trunk

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**.

| Setting                            | Description                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Outbound SIP address**           | Your provider's SIP address, for example `sip.example.com`                                         |
| **Outbound username and password** | Optional credentials for calls from Reception.ai to your provider                                  |
| **Inbound allowed addresses**      | IP addresses or CIDR ranges allowed to send calls, for example `203.0.113.10` or `198.51.100.0/24` |
| **Inbound username and password**  | Optional credentials your provider uses to send calls. Don't reuse the outbound pair.              |

**Advanced settings** include the outbound transport (TLS, TCP, or UDP), media encryption (allowed, required, or disabled), and custom outbound headers.

> **Note**
>
> The inbound allowed addresses list starts empty. Add your provider's IP addresses, or inbound
> calls are rejected.

### Add a SIP number to a receptionist

1. Go to **Receptionists** and select the **Phone** tile.
2. Enter the number and select **Add SIP Trunk number**.
3. The number shows the SIP servers to send calls to, over TCP or TLS, and the request URI to use.
4. In your provider or PBX, route the number to one of those SIP servers.

The part of the request URI before `@` must be the number in E.164 format, for example `+14155550123`, or the call is rejected.

> **Warning**
>
> Adding a number in Reception.ai does not configure your provider. Calls only reach your
> receptionist after you route the number in your provider's settings.
