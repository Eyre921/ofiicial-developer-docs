---
title: "SMS conversations"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/twilio-integration/sms-conversations.md
path: docs/eleven-agents/phone-numbers/twilio-integration/sms-conversations
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# SMS conversations

## Overview

This guide shows you how to enable SMS conversations with your ElevenLabs agent. After you connect a Twilio phone number, users can send text messages to that number and receive replies from your agent.

## Prerequisites

* A [Twilio account](https://twilio.com/) with a purchased phone number that supports SMS.
* An ElevenLabs agent to handle inbound messages.

Verified caller IDs support outbound calls only. Use a purchased Twilio phone number for inbound
SMS. See [Twilio native
integration](/docs/eleven-agents/phone-numbers/twilio-integration/native-integration#phone-number-types--capabilities).

## Enable SMS

#### Import your Twilio phone number

Phone numbers you imported before SMS support are not automatically enabled for SMS. To enable
SMS, re-import your Twilio number.

Follow the [Twilio native integration](/docs/eleven-agents/phone-numbers/twilio-integration/native-integration) guide to import your number and add your Twilio Account SID and Auth Token.

#### Assign an agent

On the [**Phone Numbers**](https://elevenlabs.io/app/agents/phone-numbers) page, open your imported number and assign the agent that should handle inbound SMS.

![Outbound call button](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/953a870b0ab0c0aa30872b3692260f0879f390d4b4b83c7f82e816385504034f/assets/images/conversational-ai/outbound-button.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260817%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260817T100015Z&X-Amz-Expires=604800&X-Amz-Signature=e9e402753ed627648db18aea3edcb96ccead59a5da4271faa053054a7e022645&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Test the integration

Send a text message to your Twilio number from a mobile device. Your agent should reply over SMS.

![SMS conversation between a user and an ElevenLabs
agent](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/759839ae9ab62d9a958f9875580e345194c7a4974783904606f254a9f88722cb/assets/images/conversational-ai/agent-sms-native.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260817%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260817T100015Z&X-Amz-Expires=604800&X-Amz-Signature=9441c594dc40330bd5206ae6a6f0539483c621f28d5e0efca6ac7d393d61933b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Review conversations in the [Calls History dashboard](https://elevenlabs.io/app/agents/history).

## Related guides

* [Twilio native integration](/docs/eleven-agents/phone-numbers/twilio-integration/native-integration) — Import a Twilio number and configure voice calls.
* [SMS OTP verification](/docs/eleven-agents/phone-numbers/twilio-integration/sms-otp-verification) — Send and verify one-time passcodes over SMS during a voice call with Twilio Verify.
