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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/734d6e0c2af1c50b769700e084368bed2a8c7eccf47aece6cfb6fc5ca7623f44/assets/images/agents/whatsapp/main-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=4d2b11d53b20f5e8a59568e640a580ee665b292683fd60e3ae0dee91b8479f9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp page" />

#### Authorize ElevenLabs

This will open the authorization flow where you select your account and give ElevenLabs permission to manage it:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9e5238e98f926582db314e9debc187a7dc29fd38a980cb732b4563b373110351/assets/images/agents/whatsapp/auth-flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=0f9ae59d879fe58a7c601e45b5231ebb48c97cdc449c31b979699d0afed373d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp authorization flow" />

#### Assign an agent

When you finish importing your account, you will be taken to its settings page where you can assign an agent to it:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f5598ac70ade00048effb5ee3bf6cbc93cd61876652eb3ce5917ac21c6209bf6/assets/images/agents/whatsapp/account-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=f4edd7229700c2960ad8188e2d009c87fbc3c3611da817b8eed77850fbbd1f22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp account page" />

If you don't assign an agent to your account, inbound messages will be ignored and inbound calls
will be rejected. However, you will still be able to make outbound calls.

#### Configure WhatsApp Manager

Go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/) to:

* Configure your profile picture, etc.: open the ***Phone numbers*** page, select a phone number and go to the ***Profile*** tab
* Allow voice calls: open the ***Phone numbers*** page, select a phone number and go to the ***Call settings*** tab
* If you want to make outbound calls, add a payment method: open the ***Overview*** page and click the ***Add payment method*** button

## Message conversations

WhatsApp message conversations end when the agent uses the ***End conversation*** system tool, the
configured ***Max conversation duration*** elapses, or the default inactivity timeout elapses after
the agent's most recent response.

WhatsApp message conversations have a default 15-minute inactivity timeout measured from the
agent's most recent response. Learn more about [conversation
timeouts](/docs/eleven-agents/customization/conversation-flow#maximum-conversation-duration).

### Inbound

You can send a message to your WhatsApp business account and the agent will respond:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4c31b4d2b5eccccd7cddfa81144176a6d3c32f4670add5306f3a6ef78bc05244/assets/images/agents/whatsapp/text-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=bc5c5ee2bcdc047397b3e381e66e107d602b6f3969c7d828f72272cdd3cca33a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp text conversation" width="300" />

When either timeout expires, ElevenAgents sends the configured ***Max conversation duration
message*** before closing the conversation. If the message is empty, the conversation closes
without a farewell.

### Outbound

You can start a conversation by sending an outbound message.

First, go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates) and create a message template.

You can then go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp), select your account, and click the ***Outbound -> Message*** button. This will open a dialog where you select an agent, provide a WhatsApp user ID, as well as the message template & its parameters:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/13913c2ccc1d92cb59e7332b6fdb4a8c8c64760a334d1a311fa2007831eeb986/assets/images/agents/whatsapp/outbound-message-dialog.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=2d839c55e8db1402cbe57adcdd8d09c914038714f7eb7dfa788a6e62c9c7600c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp outbound message dialog" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8d9022503a76eb94a6f674ed22cd6f5ad1cc24d34fd8c50cefa35da6b9fc508d/assets/images/agents/whatsapp/text-conversation-outbound.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=ff03373b5e02bdb297f842ee56a12031feff4f844582d3190d11edcbeda04e8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp text conversation" width="300" />

Alternatively, you can send the message via [the API](/docs/api-reference/whats-app/outbound-message). The `conversation_initiation_client_data` field lets you set [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) for the conversation, and pin it to a specific [agent branch](/docs/eleven-agents/operate/versioning) and [environment](/docs/eleven-agents/integrate/environment-variables):

```python title="Python"
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.whatsapp.outbound_message(
    whatsapp_phone_number_id="524029457612345",
    whatsapp_user_id="12213231492",
    template_name="welcome",
    template_language_code="en",
    template_params=[
      {
        "type":"text",
        "parameter_name":"name",
        "text":"Daniele"
      }
    ],
    agent_id="agent_9201kwcrbq9qfxaa2t8nnnkqf2w9",
    conversation_initiation_client_data={
        "dynamic_variables": {"customer_name": "Daniele"},
        "branch_id": "agtbrch_8721kwarbs83e233mg1fzkaf9pg0",
        "environment": "staging",
    }
)
```

```typescript title="TypeScript"
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.whatsapp.outboundMessage({
  whatsappPhoneNumberId: "524029457612345",
  whatsappUserId: "12213231492",
  templateName: "welcome",
  templateLanguageCode: "en",
  templateParams: [
    {
      type: "text",
      parameterName: "name",
      text: "Daniele",
    },
  ],
  agentId: "agent_9201kwcrbq9qfxaa2t8nnnkqf2w9",
  conversationInitiationClientData: {
    dynamicVariables: { customer_name: "Daniele" },
    branchId: "agtbrch_8721kwarbs83e233mg1fzkaf9pg0",
    environment: "staging",
  },
});
```

These settings persist for the conversation: when the user replies, the agent resumes on the requested branch and environment. The branch and environment are validated first — if either does not exist, the request fails with an error and no message is sent.

Sending an outbound template starts neither timer. The maximum conversation duration begins when
the customer responds and the conversation resumes. The inactivity timeout begins after the agent
sends its first live response.

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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/372158bc0f86d62b6742f2bb44a741e5299ee7b95e36e38c3df1f9c06cffe2a0/assets/images/agents/whatsapp/audio-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=7a29c2243e7fcbb9a15b05f292dd5cf2efca85086e65b4a431cb36fde7728d1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp audio conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/cbfbadb9d0a20f35537ce3bd137eb12b1005a862a7e1cf0155d271502fb713da/assets/images/agents/whatsapp/image-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=fed27ff5eb0d948ab4bf849d4536289bd8beb1ec8f3be408302d6a16778c51a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp image conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2b91d4077ac19a56dda9c5c016a47ed7d574ba2cb77ac89eb8785925bc89fa13/assets/images/agents/whatsapp/document-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=3bb51b00558224b27419e286d37a433c12769f0cbbce2281b6ee956e5266452b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp document conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bcd0d8f7df69d6c381be5be7c7a91ec7752b2b1894a80539823b7d9266beb3dd/assets/images/agents/whatsapp/location-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=54677ba255843e5321e63f51ee3b400a79262de8ddddd6da73b51464944fe428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp location conversation" width="300" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/75e56544700c87817a7f842943301a95e9e0b1fb84fc87e19139adb77f49ea5a/assets/images/agents/whatsapp/contacts-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=33b8d720cd4540b0c5d7a7102d1e5ef505e25cf6c46dbe1bd37c6950fbb29ada&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp contacts conversation" width="300" />

## Calls

### Inbound

You can call your WhatsApp business account and the agent will respond. During the call, you can also send text messages and they will be incorporated into the conversation.

### Outbound

Making an outbound call requires permission from the user. You can read more about this in [WhatsApp documentation](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/user-call-permissions). When you schedule an outbound call, we will automatically send a template message with a call permission request if necessary, and make the call as soon as the user approves it.

First, go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates) and create a message template with a call permission request component.

You can then go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp), select your account, and click the ***Outbound -> Call*** button. This will open a dialog where you select an agent, provide a WhatsApp user ID, and the call permission request template to use:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1fcf7968f1651ce8e9474e770aad4dce4e702c69b4522f5bcc65efcd8bf8a3e4/assets/images/agents/whatsapp/outbound-call-dialog.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T113226Z&X-Amz-Expires=604800&X-Amz-Signature=08372ff18a0a0b3bbba859abac37334a73bd009572600d159174a74accf0d50a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp outbound call dialog" />

Alternatively, you can schedule the call via [the API](/docs/api-reference/whats-app/outbound-call) or schedule multiple calls with [batch calling](/docs/eleven-agents/phone-numbers/batch-calls).

As with outbound messages, the API accepts `conversation_initiation_client_data` to set dynamic variables and pin the conversation to a specific [agent branch](/docs/eleven-agents/operate/versioning) and [environment](/docs/eleven-agents/integrate/environment-variables). An unknown branch or environment is rejected with an error before the call is scheduled.

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
