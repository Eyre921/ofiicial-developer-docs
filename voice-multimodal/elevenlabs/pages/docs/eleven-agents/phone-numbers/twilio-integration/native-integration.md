---
title: "Twilio native integration"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/twilio-integration/native-integration.md
path: docs/eleven-agents/phone-numbers/twilio-integration/native-integration
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Twilio native integration

## Overview

This guide shows you how to connect a Twilio phone number to your ElevenLabs agent to handle both inbound and outbound calls.

You will learn to:

* Import an existing Twilio phone number.
* Link it to your agent to handle inbound calls.
* Initiate outbound calls using your agent.

## Phone Number Types & Capabilities

ElevenLabs supports two types of Twilio phone numbers with different capabilities:

### Purchased Twilio Numbers (Full Support)

* **Inbound calls**: Supported - Can receive calls and route them to agents
* **Outbound calls**: Supported - Can make calls using agents
* **Requirements**: Number must be purchased through Twilio and appear in your "Phone Numbers" section

### Verified Caller IDs (Outbound Only)

* **Inbound calls**: Not supported - Cannot receive calls or be assigned to agents
* **Outbound calls**: Supported - Can make calls using agents
* **Requirements**: Number must be verified in Twilio's "Verified Caller IDs" section
* **Use case**: Ideal for using your existing business number for outbound AI calls

Learn more about [verifying caller IDs at scale](https://www.twilio.com/docs/voice/api/verifying-caller-ids-scale) in Twilio's documentation.

During phone number import, ElevenLabs automatically detects the capabilities of your number based
on its configuration in Twilio.

## Guide

### Prerequisites

* A [Twilio account](https://twilio.com/).
* Either:
  * A purchased & provisioned Twilio [phone number](https://www.twilio.com/docs/phone-numbers) (for inbound + outbound)
  * OR a [verified caller ID](https://www.twilio.com/docs/voice/make-calls#verify-your-caller-id) in Twilio (for outbound only)

#### Import a Twilio phone number

In the ElevenAgents dashboard, go to the [**Phone Numbers**](https://elevenlabs.io/app/agents/phone-numbers) tab.

![ElevenAgents phone numbers page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7efb681147acd8f04803f84ed7f3289f0e90eb1fb0173e2a825836408cee89d1/assets/images/conversational-ai/phone-numbers-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=ae885e64cdcdca9e8c237d4a1ad7e8a4bd0eb80200d5197cc65b8d6c7e7ca7c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Next, fill in the following details:

* **Label:** A descriptive name (e.g., `Customer Support Line`).
* **Phone Number:** The Twilio number you want to use.
* **Twilio SID:** Your Twilio Account SID or API Key SID.
* **Twilio Token:** Your Twilio Auth Token or API Key Secret.

**Recommended: Use API keys for better security.** Instead of using your account-wide credentials, you can [create a Twilio API key](https://www.twilio.com/docs/iam/api-keys) with limited permissions. When you create an API key, Twilio provides a **SID** (starts with `SK`) and a **Secret** — use these in the fields above.

You can find your account SID and auth token [**in the Twilio admin console**](https://www.twilio.com/console), or create API keys in the [API keys section](https://www.twilio.com/console/project/api-keys).

#### ElevenAgents dashboard

![Phone number configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9501110d58bfeca27cb9983bc44035864504bdc2ed9c78d9decbd04802f64418/assets/images/conversational-ai/phone-numbers-new.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=3000192c1de130e636b604f185d9663e62707682f1c03850c3b24931f362a1c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Twilio admin console

Copy the Twilio SID and Auth Token from the [Twilio admin
console](https://www.twilio.com/console).

![Phone number details](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/42da512d1cdfb4ca4504c3162fecfed108580d9488236a0cc6a4a1d23a19da14/assets/images/conversational-ai/twilio-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=60147873c9ff5e51bc6272469b28c8f607b791e44e974bb7d1de1476a9bc47b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

ElevenLabs automatically configures the Twilio phone number with the correct settings.

#### Applied settings

![Twilio phone number configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b11d57a0aa588964bbd0117d2135c55592569a4bf051f00f17aa3ee632833a47/assets/images/conversational-ai/twilio-configuration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=25b93f1d16040eaf805466ebdaa458fa4c930771dea59059652a44eaaa6fddb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Phone Number Detection**: ElevenLabs will automatically detect whether your number supports:

* **Inbound + Outbound**: Numbers purchased through Twilio
* **Outbound Only**: Numbers verified as caller IDs in Twilio

If your number is not found in either category, you'll receive an error asking you to verify it exists in your Twilio account.

#### Assign your agent (Inbound-capable numbers only)

If your phone number supports inbound calls, you can assign an agent to handle incoming calls.

![Select agent for inbound calls](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b85c122ef8607527041516e789b0a19047cbf85a13cd3237ee5a7670683815a7/assets/images/conversational-ai/twilio-assigned-agent.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=0e57a23a84c415bb637f03e81c916b8bd5b2a77a2f94190221a63f5b32d60499&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Numbers that only support outbound calls (verified caller IDs) cannot be assigned to agents and
will show as disabled in the agent dropdown.

Test the agent by giving the phone number a call. Your agent is now ready to handle inbound calls and engage with your customers.

Monitor your first few calls in the [Calls History
dashboard](https://elevenlabs.io/app/agents/history) to ensure everything is working as expected.

## Making Outbound Calls

Both purchased Twilio numbers and verified caller IDs can be used for outbound calls. The outbound
call button will be disabled for numbers that don't support outbound calling.

Your imported Twilio phone number can also be used to initiate outbound calls where your agent calls a specified phone number.

#### Initiate an outbound call

From the [**Phone Numbers**](https://elevenlabs.io/app/agents/phone-numbers) tab, locate your imported Twilio number and click the **Outbound call** button.

![Outbound call button](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/953a870b0ab0c0aa30872b3692260f0879f390d4b4b83c7f82e816385504034f/assets/images/conversational-ai/outbound-button.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=04457f5be0a7343e9975fde7989437a0599914aa8fc0a2e7c17c634708b57c95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Configure the call

In the Outbound Call modal:

1. Select the agent that will handle the conversation
2. Enter the phone number you want to call
3. Click **Send Test Call** to initiate the call

![Outbound call configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f6b01412a68217661028e6924ce90089bdd5eaa693c8aeafbc321c632de921b7/assets/images/conversational-ai/outbound-modal.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T233250Z&X-Amz-Expires=604800&X-Amz-Signature=e85f3466ab2fa6771d5ff46ddcffa5b180709dbfc93efc8c3d5ad988b8570b98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once initiated, the recipient will receive a call from your Twilio number. When they answer, your agent will begin the conversation.

Outbound calls appear in your [Calls History dashboard](https://elevenlabs.io/app/agents/history)
alongside inbound calls, allowing you to review all conversations.

When making outbound calls, your agent will be the initiator of the conversation, so ensure your
agent has appropriate initial messages configured to start the conversation effectively.
