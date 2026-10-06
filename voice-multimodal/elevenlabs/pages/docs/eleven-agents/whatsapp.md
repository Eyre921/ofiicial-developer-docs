---
title: "WhatsApp"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp.md
path: docs/eleven-agents/whatsapp
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WhatsApp

## Overview

You can connect your WhatsApp business account to an ElevenLabs Agent. The agent can then handle:

* Message conversations — text, voice notes, media, and [interactive messages](/docs/eleven-agents/whatsapp/interactive-messages)
* Calls — inbound and [outbound](/docs/eleven-agents/whatsapp/outbound#scheduling-an-outbound-call)

Agents on other channels can also send WhatsApp messages through [WhatsApp tools](/docs/eleven-agents/whatsapp/tools).

New to WhatsApp on ElevenLabs? Follow the [getting started guide](/docs/eleven-agents/whatsapp/getting-started).

## Importing a WhatsApp business account

#### Import your account

Go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp) and click the ***Import account*** button:

![WhatsApp page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/734d6e0c2af1c50b769700e084368bed2a8c7eccf47aece6cfb6fc5ca7623f44/assets/images/agents/whatsapp/main-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=fe8bc658eb674bac7cf13e556f1226b9fda95ba1b3b33ceca06645e2f4328295&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Authorize ElevenLabs

This will open the authorization flow where you select your account and give ElevenLabs permission to manage it:

![WhatsApp authorization flow](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9e5238e98f926582db314e9debc187a7dc29fd38a980cb732b4563b373110351/assets/images/agents/whatsapp/auth-flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=7ed7bac76523c09aa8f1ee405c80d921bde447b63d9c6ac05c02254b36813fcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Assign an agent

When you finish importing your account, you will be taken to its settings page where you can assign an agent to it:

![WhatsApp account page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f5598ac70ade00048effb5ee3bf6cbc93cd61876652eb3ce5917ac21c6209bf6/assets/images/agents/whatsapp/account-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=24650ce242e42e0968e8d27f7c0de9431daf6fab179091a51beaaf6f43213703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Info**
>
> If you don't assign an agent to your account, inbound messages will be ignored and inbound calls
> will be rejected. However, you will still be able to make outbound calls.

#### Configure WhatsApp Manager

Go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/) to:

* Configure your profile picture, etc.: open the ***Phone numbers*** page, select a phone number and go to the ***Profile*** tab
* Allow voice calls: open the ***Phone numbers*** page, select a phone number and go to the ***Call settings*** tab
* If you want to make outbound calls, add a payment method: open the ***Overview*** page and click the ***Add payment method*** button

## Account settings

Each imported number has settings that control the agent's behavior:

* **Enable messaging** — whether the agent responds to messages. Turn it off to let ElevenLabs handle only calls while your own application handles messages.
* **Enable audio message response** — when on (the default), the agent answers voice notes with voice notes; when off, it always replies with text.
* **Enable typing indicator** — when on (the default), the agent marks incoming messages as read and shows a typing indicator while composing its response.

## Message conversations

WhatsApp message conversations end when the agent uses the [***End conversation*** system tool](/docs/eleven-agents/customization/tools/system-tools/end-call), the configured ***Max
conversation duration*** elapses, or the default inactivity timeout elapses after the agent's most
recent response.

> **Info**
>
> WhatsApp message conversations have a default 15-minute inactivity timeout measured from the
> agent's most recent response. Learn more about [conversation timeouts](/docs/eleven-agents/customization/conversation-flow#maximum-conversation-duration).

### Inbound

You can send a message to your WhatsApp business account and the agent will respond:

![WhatsApp text conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4c31b4d2b5eccccd7cddfa81144176a6d3c32f4670add5306f3a6ef78bc05244/assets/images/agents/whatsapp/text-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=91c6c9ff3669eeb0d193ae3db8e622f9a61ff7f412112d65c541d9668a9ea253&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When either timeout expires, ElevenAgents sends the configured ***Max conversation duration
message*** before closing the conversation. If the message is empty, the conversation closes
without a farewell.

The agent understands more than plain text:

* **Quoted replies** — when the user long-presses a message and replies to it, the agent knows which message they are responding to.
* **Reactions** — emoji reactions to the agent's messages are passed to the agent.
* **Template button taps** — when the user taps a quick-reply button on a template, the agent sees which button was chosen.
* **Interactive replies** — taps on [interactive buttons and lists](/docs/eleven-agents/whatsapp/interactive-messages) arrive with the selected option.

> **Note**
>
> The agent responds to each incoming message individually. Rapid consecutive messages are not
> batched into a single reply.

### Outbound

You can start a conversation by sending a Meta-approved message template, from the dashboard or the API, and schedule outbound calls with a call permission request. See [Outbound messages & templates](/docs/eleven-agents/whatsapp/outbound) for template creation, code examples, recipient format rules, and batch campaigns.

### Message types

In addition to text, you can also send:

* audio
  * Inbound voice notes are transcribed to text before being passed to the agent.
  * By default, the agent responds to voice notes with voice notes, generated in the agent's configured voice — any voice, any language. Turn off ***Enable audio message response*** in the account settings to always respond with text. If audio generation fails, the agent falls back to a text reply.
  * Audio messages result in extra charges for speech-to-text and text-to-speech. Pricing is the same as in the STT and TTS APIs.
* image
* document
* sticker
* location
* contact

![WhatsApp audio conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/372158bc0f86d62b6742f2bb44a741e5299ee7b95e36e38c3df1f9c06cffe2a0/assets/images/agents/whatsapp/audio-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=580a24d43b155b0d91e16effdd274bbe9c548674de4ffd17c22721672ad5863d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)![WhatsApp image conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/cbfbadb9d0a20f35537ce3bd137eb12b1005a862a7e1cf0155d271502fb713da/assets/images/agents/whatsapp/image-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=9a3b2291924d642643fd63ea9ed2b7835f604679d72943586b6e5e2f94802ac1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)![WhatsApp document conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2b91d4077ac19a56dda9c5c016a47ed7d574ba2cb77ac89eb8785925bc89fa13/assets/images/agents/whatsapp/document-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=551e4edfc41fd8b3bc31aec194a46191989a1b32feb57d97140ba4e516085c5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)![WhatsApp location conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bcd0d8f7df69d6c381be5be7c7a91ec7752b2b1894a80539823b7d9266beb3dd/assets/images/agents/whatsapp/location-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=3326667a02dca68f99400d38239e4ae96379c9a5557f6bfb32944e94132112ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)![WhatsApp contacts conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/75e56544700c87817a7f842943301a95e9e0b1fb84fc87e19139adb77f49ea5a/assets/images/agents/whatsapp/contacts-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T091754Z&X-Amz-Expires=604800&X-Amz-Signature=e96cddff46012d379e98ed5ec4490d53962769dc5c44c11208b603b5207e0a47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Calls

### Inbound

You can call your WhatsApp business account and the agent will respond. During the call, you can also send text messages and they will be incorporated into the conversation.

### Outbound

Outbound calls require the user's permission, requested through a template. See [scheduling an outbound call](/docs/eleven-agents/whatsapp/outbound#scheduling-an-outbound-call) for the flow, code examples, and batch calling.

## Personalization

We set the `{{system__caller_id}}` and `{{system__called_number}}` [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) to the WhatsApp user ID and your WhatsApp phone number ID (or vice versa, depending on who started the conversation). You can use those in a tool or a [conversation initiation webhook](/docs/eleven-agents/customization/personalization#conversation-initiation-webhooks) to fetch information about your user in the conversation.

> **Info**
>
> You can find your WhatsApp phone number ID by going to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp), clicking the menu next to your account and
> selecting ***Copy phone number ID***.

### Initialization context

If your agent uses [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) beyond the system variables above, you will need to plan where their values come from. If your agent uses no dynamic variables, none of this applies.

**Inbound conversations** start with no user-provided dynamic variables. The supported way to provide values is a [conversation initiation webhook](/docs/eleven-agents/customization/personalization#conversation-initiation-webhooks): when a WhatsApp message starts a conversation, ElevenAgents calls your endpoint with the WhatsApp user ID as `caller_id` and your WhatsApp phone number ID as `called_number`, and applies the dynamic variables your response returns. Have the webhook always return every variable the agent requires — a CRM value when you have one, a fallback constant otherwise.

> **Warning**
>
> The values entered under **Dynamic Variables** in the agent editor are test placeholders for
> previewing the agent. They are not used in production and do not act as defaults for inbound
> conversations.

**Outbound conversations** receive their values from the `conversation_initiation_client_data.dynamic_variables` field of the [outbound message or call request](/docs/eleven-agents/whatsapp/outbound#dynamic-variables-branches-and-environments). These values persist for the conversation and are still available when the user replies. Template parameters are a separate field and do not populate dynamic variables.

A required variable that ends up without a value will fail the conversation. See [missing dynamic variables](/docs/eleven-agents/whatsapp/troubleshooting#the-agent-doesnt-respond-to-inbound-messages) in the troubleshooting guide.

> **Note**
>
> The `system__called_number` value is your WhatsApp **phone number ID**, not the phone number
> itself. WhatsApp user identifiers are also migrating to [Business-Scoped User IDs (BSUIDs)](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids);
> ElevenAgents supports BSUIDs, so conversations work even when Meta provides an ID rather than the
> user's phone number.

## Limitations

The following are not currently supported:

* **WhatsApp Flows** — interactive forms cannot be sent, and Flow replies are not passed to the agent.
* **Video messages** — inbound videos are not passed to the agent.
* **Message batching** — the agent replies to each message individually rather than coalescing rapid consecutive messages.
* **Numbers managed by another provider** — a number registered with another WhatsApp provider, or active in the WhatsApp Business app, cannot be imported. We are working with Meta to enable [Multi-Solution Conversations](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/multi-solution-conversations); voice-only setups may already be possible over SIP (see the [FAQ](/docs/eleven-agents/whatsapp/troubleshooting#faq)).
* **WABAs created under a developer app** — these cannot be imported through the standard flow.
* **Ad referral metadata** — Click-to-WhatsApp ad attribution data is not exposed to the agent (see the [FAQ](/docs/eleven-agents/whatsapp/troubleshooting#faq)).
* **Human handoff** — coming soon (see the [FAQ](/docs/eleven-agents/whatsapp/troubleshooting#faq)).

## FAQ

Common questions — pricing, multi-provider setups, human handoff, Zero-Retention Mode, OTP, compliance — are answered in [Troubleshooting & FAQ](/docs/eleven-agents/whatsapp/troubleshooting).
