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

> **Note**
>
> During phone number import, ElevenLabs automatically detects the capabilities of your number based
> on its configuration in Twilio.

## Guide

### Prerequisites

* A [Twilio account](https://twilio.com/).
* Either:
  * A purchased & provisioned Twilio [phone number](https://www.twilio.com/docs/phone-numbers) (for inbound + outbound)
  * OR a [verified caller ID](https://www.twilio.com/docs/voice/make-calls#verify-your-caller-id) in Twilio (for outbound only)

#### Import a Twilio phone number

In the ElevenAgents dashboard, go to the [**Phone Numbers**](https://elevenlabs.io/app/agents/phone-numbers) tab.

![ElevenAgents phone numbers page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7efb681147acd8f04803f84ed7f3289f0e90eb1fb0173e2a825836408cee89d1/assets/images/conversational-ai/phone-numbers-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=ced2140345932f6dc274d6fc51f7e63bb56d8e705669ff8dd416aa1a64790415&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Next, fill in the following details:

* **Label:** A descriptive name (e.g., `Customer Support Line`).
* **Phone Number:** The Twilio number you want to use.
* **Twilio SID:** Your Twilio Account SID or API Key SID.
* **Twilio Token:** Your Twilio Auth Token or API Key Secret.

> **Tip**
>
> **Recommended: Use API keys for better security.** Instead of using your account-wide credentials, you can [create a Twilio API key](https://www.twilio.com/docs/iam/api-keys) with limited permissions. When you create an API key, Twilio provides a **SID** (starts with `SK`) and a **Secret** — use these in the fields above.

> **Note**
>
> You can find your account SID and auth token [**in the Twilio admin console**](https://www.twilio.com/console), or create API keys in the [API keys section](https://www.twilio.com/console/project/api-keys).

#### ElevenAgents dashboard

![Phone number configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9501110d58bfeca27cb9983bc44035864504bdc2ed9c78d9decbd04802f64418/assets/images/conversational-ai/phone-numbers-new.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=92775b86c1298da4a9c60edbb023c8e1cb06c5d25c7610e6db1b3ee4e91bf6cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Twilio admin console

Copy the Twilio SID and Auth Token from the [Twilio admin console](https://www.twilio.com/console).

![Phone number details](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/42da512d1cdfb4ca4504c3162fecfed108580d9488236a0cc6a4a1d23a19da14/assets/images/conversational-ai/twilio-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=cdbcf0f5448ad044222e4633dd8a86b3216e39e971934437cdb0ce51c45ff623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Note**
>
> ElevenLabs automatically configures the Twilio phone number with the correct settings.

#### Applied settings

![Twilio phone number configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b11d57a0aa588964bbd0117d2135c55592569a4bf051f00f17aa3ee632833a47/assets/images/conversational-ai/twilio-configuration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=9adcd0fb0bd3dfb3e85c1697decc49cc1582c7ebb58792a58371c4b6649b1e78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Info**
>
> **Phone Number Detection**: ElevenLabs will automatically detect whether your number supports:
>
> * **Inbound + Outbound**: Numbers purchased through Twilio
> * **Outbound Only**: Numbers verified as caller IDs in Twilio
>
> If your number is not found in either category, you'll receive an error asking you to verify it exists in your Twilio account.

#### Assign your agent (Inbound-capable numbers only)

If your phone number supports inbound calls, you can assign an agent to handle incoming calls.

![Select agent for inbound calls](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b85c122ef8607527041516e789b0a19047cbf85a13cd3237ee5a7670683815a7/assets/images/conversational-ai/twilio-assigned-agent.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=c24de27db6f68463f655827c6b92a5f6c35f91a6c6a1c63cebc594ea756f5968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Note**
>
> Numbers that only support outbound calls (verified caller IDs) cannot be assigned to agents and
> will show as disabled in the agent dropdown.

Test the agent by giving the phone number a call. Your agent is now ready to handle inbound calls and engage with your customers.

> **Tip**
>
> Monitor your first few calls in the [Calls History dashboard](https://elevenlabs.io/app/agents/history) to ensure everything is working as expected.

## Making Outbound Calls

> **Info**
>
> Both purchased Twilio numbers and verified caller IDs can be used for outbound calls. The outbound
> call button will be disabled for numbers that don't support outbound calling.

Your imported Twilio phone number can also be used to initiate outbound calls where your agent calls a specified phone number.

#### Initiate an outbound call

From the [**Phone Numbers**](https://elevenlabs.io/app/agents/phone-numbers) tab, locate your imported Twilio number and click the **Outbound call** button.

![Outbound call button](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/953a870b0ab0c0aa30872b3692260f0879f390d4b4b83c7f82e816385504034f/assets/images/conversational-ai/outbound-button.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=805011e8fa35c68c06beed57bcc55d4d254cfbdaf485364b739bf252913daaa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Configure the call

In the Outbound Call modal:

1. Select the agent that will handle the conversation
2. Enter the phone number you want to call
3. Click **Send Test Call** to initiate the call

![Outbound call configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f6b01412a68217661028e6924ce90089bdd5eaa693c8aeafbc321c632de921b7/assets/images/conversational-ai/outbound-modal.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095309Z&X-Amz-Expires=604800&X-Amz-Signature=02b7c5baa7fde0b8325ced3eb383a99e1c2665ee10aa81ba0a0b7c3ebf39e3df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once initiated, the recipient will receive a call from your Twilio number. When they answer, your agent will begin the conversation.

> **Tip**
>
> Outbound calls appear in your [Calls History dashboard](https://elevenlabs.io/app/agents/history)
> alongside inbound calls, allowing you to review all conversations.

> **Note**
>
> When making outbound calls, your agent will be the initiator of the conversation, so ensure your
> agent has appropriate initial messages configured to start the conversation effectively.
