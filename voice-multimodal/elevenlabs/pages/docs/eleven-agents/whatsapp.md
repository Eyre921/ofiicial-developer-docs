---
title: "WhatsApp"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp.md
path: docs/eleven-agents/whatsapp
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WhatsApp

## Overview

You can connect your WhatsApp business account to an ElevenLabs Agent. The agent can then handle:

* Message conversations
* Calls

## Importing a WhatsApp business account

#### Import your account

Go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp) and click the ***Import account*** button:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/734d6e0c2af1c50b769700e084368bed2a8c7eccf47aece6cfb6fc5ca7623f44/assets/images/agents/whatsapp/main-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=6683a83968592d2a811bee2133714f21a2cb907474122f5865dc39b65a91f977&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp page" />

#### Authorize ElevenLabs

This will open the authorization flow where you select your account and give ElevenLabs permission to manage it:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9e5238e98f926582db314e9debc187a7dc29fd38a980cb732b4563b373110351/assets/images/agents/whatsapp/auth-flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=931f78729c8388d7dfa6d53a56bcfd2708754c1e49fb531480875ce28ab0d244&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp authorization flow" />

#### Assign an agent

When you finish importing your account, you will be taken to its settings page where you can assign an agent to it:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f5598ac70ade00048effb5ee3bf6cbc93cd61876652eb3ce5917ac21c6209bf6/assets/images/agents/whatsapp/account-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=47cf6f2e43efd58fdfebaa3ca099311e9ce357887493284d62e80b3cb39021f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp account page" />

If you don't assign an agent to your account, inbound messages will be ignored and inbound calls
will be rejected. However, you will still be able to make outbound calls.

#### Configure WhatsApp Manager

Go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/) to:

* Configure your profile picture, etc.: open the ***Phone numbers*** page, select a phone number and go to the ***Profile*** tab
* Allow voice calls: open the ***Phone numbers*** page, select a phone number and go to the ***Call settings*** tab
* If you want to make outbound calls, add a payment method: open the ***Overview*** page and click the ***Add payment method*** button

## Message conversations

### Inbound

You can send a message to your WhatsApp business account and the agent will respond:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4c31b4d2b5eccccd7cddfa81144176a6d3c32f4670add5306f3a6ef78bc05244/assets/images/agents/whatsapp/text-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=ba75b7fbe6f8db295e4beb5fd9f9425c14dfdce25bceabae0558bb95ee612de8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp text conversation" width="300" />

The conversation will be ended either by the ***End conversation*** system tool (if you have it enabled on your agent) or after the ***Max conversation duration*** timeout.

Set a ***Max conversation duration message*** in your agent config so that users are aware when
the conversation ends due to a timeout.

### Outbound

You can start a conversation by sending an outbound message.

First, go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates) and create a message template.

You can then go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp), select your account, and click the ***Outbound -> Message*** button. This will open a dialog where you select an agent, provide a WhatsApp user ID, as well as the message template & its parameters:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/13913c2ccc1d92cb59e7332b6fdb4a8c8c64760a334d1a311fa2007831eeb986/assets/images/agents/whatsapp/outbound-message-dialog.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=7c75f9659256af8af21dcec82841a385e7bdb6906eb413227a1363c1ea7957cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp outbound message dialog" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8d9022503a76eb94a6f674ed22cd6f5ad1cc24d34fd8c50cefa35da6b9fc508d/assets/images/agents/whatsapp/text-conversation-outbound.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=411c3e28783f95ed9428a434bccf6a1810f6cfbdc3181df001159a07ddf6d6c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp text conversation" width="300" />

Alternatively, you can send the message via [the API](/docs/api-reference/whats-app/outbound-message).

For outbound messages, the timer for max conversation duration only starts after the user
responds.

### Message types

In addition to text, you can also send:

* audio
  * Inbound audio messages will be transcribed to text before being passed to the agent.
  * By default, the agent will respond to audio messages with audio messages. You can make the agent always respond with text in your WhatsApp account settings.
  * Audio messages result in extra charges for speech-to-text and text-to-speech. Pricing is the same as in the STT and TTS APIs.
* image
* document
* location
* contact

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/372158bc0f86d62b6742f2bb44a741e5299ee7b95e36e38c3df1f9c06cffe2a0/assets/images/agents/whatsapp/audio-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=e3e4aa5a0cacb656a46201e061cd4e441e908a86948516b68f19eda5df833eea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp audio conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/cbfbadb9d0a20f35537ce3bd137eb12b1005a862a7e1cf0155d271502fb713da/assets/images/agents/whatsapp/image-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=b270c8f1b0d7bdeb348225f7e8af90c255a92434f07b06a19365aeaf462bd711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp image conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2b91d4077ac19a56dda9c5c016a47ed7d574ba2cb77ac89eb8785925bc89fa13/assets/images/agents/whatsapp/document-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=c0ec4acdbf0da95e326efdfcd95142edc5aba8311a2dcc0012d16a7776a09e11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp document conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bcd0d8f7df69d6c381be5be7c7a91ec7752b2b1894a80539823b7d9266beb3dd/assets/images/agents/whatsapp/location-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=29ded6297322107192bc3dbc45ac29d1b6e8af4ee70b68028e343ff59c6eef6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp location conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/75e56544700c87817a7f842943301a95e9e0b1fb84fc87e19139adb77f49ea5a/assets/images/agents/whatsapp/contacts-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=b2a791f34188bbbace6364123add17869d5dc84e385571e1afde55c8a7e2436b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp contacts conversation" width="300" />

## Calls

### Inbound

You can call your WhatsApp business account and the agent will respond. During the call, you can also send text messages and they will be incorporated into the conversation.

### Outbound

Making an outbound call requires permission from the user. You can read more about this in [WhatsApp documentation](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/user-call-permissions). When you schedule an outbound call, we will automatically send a template message with a call permission request if necessary, and make the call as soon as the user approves it.

First, go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates) and create a message template with a call permission request component.

You can then go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp), select your account, and click the ***Outbound -> Call*** button. This will open a dialog where you select an agent, provide a WhatsApp user ID, and the call permission request template to use:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1fcf7968f1651ce8e9474e770aad4dce4e702c69b4522f5bcc65efcd8bf8a3e4/assets/images/agents/whatsapp/outbound-call-dialog.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T094858Z&X-Amz-Expires=604800&X-Amz-Signature=0b617cbaa1623236ec6ffbdd3fb1bc9e7406b5c187ad0dc71619249a9ff6e2ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp outbound call dialog" />

Alternatively, you can schedule the call via [the API](/docs/api-reference/whats-app/outbound-call) or schedule multiple calls with [batch calling](/docs/eleven-agents/phone-numbers/batch-calls).

## Next steps: personalization

We set the `{{system__caller_id}}` and `{{system__called_number}}` [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) to the WhatsApp user ID and your WhatsApp phone number ID (or vice versa, depending on who started the conversation). You can use those in a tool or a [conversation initiation webhook](/docs/eleven-agents/customization/personalization/twilio-personalization) to personalize conversations.

You can find your WhatsApp phone number ID by going to the [WhatsApp
page](https://elevenlabs.io/app/agents/whatsapp), clicking the menu next to your account and
selecting ***Copy phone number ID***.

## FAQ

#### Pricing

Meta charges for outbound calls and call permission requests sent outside of a [Customer Service
Window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows).
You will not be able to make outbound calls until you add a payment method to your WhatsApp
business account. You can read more in [WhatsApp
documentation](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing).

#### Zero-Retention Mode

[Zero-Retention Mode](/docs/eleven-api/resources/zero-retention-mode) limits our ability to
provide certain functionality: we ignore messages and disallow outbound calls.

#### Joint account management

If you have your own WhatsApp app responding to messages on your account, you can configure ElevenLabs to only respond to calls: go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp), select your account and turn off the ***Enable messaging*** switch.

If you rely on a third-party partner (e.g. Gupshup) to manage your account, then you will not be able to also import it into ElevenLabs. Meta is currently working on adding support for this (see [Multi-Solution Conversations](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/multi-solution-conversations)).
