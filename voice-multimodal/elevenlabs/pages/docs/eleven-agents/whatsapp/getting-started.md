---
title: "Getting started"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp/getting-started.md
path: docs/eleven-agents/whatsapp/getting-started
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Getting started

## What you'll build

By the end of this guide, your agent answers WhatsApp text messages and voice notes on your business number, and you have sent one API-initiated template message. Expect about 20 minutes, plus a short wait for Meta to approve your first template.

## Before you start

You need:

* An [ElevenLabs agent](/docs/eleven-agents/quickstart). Any existing agent works.
* A [Meta business portfolio](https://business.facebook.com/) you can administer.
* A phone number that is **not** currently used in the WhatsApp Business app or registered with another WhatsApp provider. Numbers in use elsewhere cannot be imported — see [Limitations](/docs/eleven-agents/whatsapp#limitations).
* A payment method in [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/) if you plan to send templates or make calls. Meta bills these separately from ElevenLabs.

#### Import your WhatsApp business account

Go to the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp) and click the ***Import account*** button. This opens Meta's authorization flow, where you select (or create) the WhatsApp business account and phone number and grant ElevenLabs permission to manage it:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9e5238e98f926582db314e9debc187a7dc29fd38a980cb732b4563b373110351/assets/images/agents/whatsapp/auth-flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T070857Z&X-Amz-Expires=604800&X-Amz-Signature=d8b93932528c3803999bbc1661d4b79466fe6cfa8347ec84f605ba7f880520de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp authorization flow" />

#### Assign your agent and choose behaviors

After the import you land on the account settings page. Assign an agent — until you do, inbound messages are ignored and inbound calls are rejected:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f5598ac70ade00048effb5ee3bf6cbc93cd61876652eb3ce5917ac21c6209bf6/assets/images/agents/whatsapp/account-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T070857Z&X-Amz-Expires=604800&X-Amz-Signature=403b3f438fb5a8a44d7ae6985b5059ce3949e0c8bcbea4731a4cf66308ba3159&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp account page" />

Configure how the agent behaves on this number (see [account
settings](/docs/eleven-agents/whatsapp#account-settings) for the full reference):

* **Enable messaging** — whether the agent responds to messages at all. Turn it off if another system handles messages and ElevenLabs should only handle calls.
* **Enable audio message response** — when on, the agent answers voice notes with voice notes in its own voice; when off, it always replies with text.
* **Enable typing indicator** — when on, the agent marks incoming messages as read and shows a typing indicator while it works.

#### Have your first conversation

Message your business number from a personal phone. The agent replies. Send a voice note — it is transcribed for the agent, and the agent responds with a voice note of its own:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4c31b4d2b5eccccd7cddfa81144176a6d3c32f4670add5306f3a6ef78bc05244/assets/images/agents/whatsapp/text-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T070857Z&X-Amz-Expires=604800&X-Amz-Signature=b75c62056689a63264340e9e4c7db8320c44c13533d59c51019a78ded9c4d940&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp text conversation" width="300" />

The conversation appears in your [conversation history](https://elevenlabs.io/app/agents/history) as it happens.

A message conversation ends when the agent uses the ***End conversation*** system tool, the
***Max conversation duration*** elapses, or the default 15-minute inactivity timeout passes
after the agent's most recent response. The next message from the user starts a new
conversation. Learn more about [conversation
timeouts](/docs/eleven-agents/customization/conversation-flow#maximum-conversation-duration).

#### Send your first outbound message

Reaching a user first requires a Meta-approved **message template** — WhatsApp only allows free-form business messages inside an active conversation. Create a simple Utility template in [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates), for example:

```text
Hi {{name}}, thanks for signing up. Reply here if you have any questions.
```

Once the template is approved, send it:

#### Python

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.whatsapp.outbound_message(
    whatsapp_phone_number_id="524029457612345",
    whatsapp_user_id="12213231492",
    template_name="welcome",
    template_language_code="en",
    template_params=[
        {
            "type": "body",
            "parameters": [
                {"type": "text", "parameter_name": "name", "text": "Daniele"}
            ],
        }
    ],
    agent_id="agent_9201kwcrbq9qfxaa2t8nnnkqf2w9",
)
```

#### TypeScript

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.whatsapp.outboundMessage({
  whatsappPhoneNumberId: "524029457612345",
  whatsappUserId: "12213231492",
  templateName: "welcome",
  templateLanguageCode: "en",
  templateParams: [
    {
      type: "body",
      parameters: [{ type: "text", parameterName: "name", text: "Daniele" }],
    },
  ],
  agentId: "agent_9201kwcrbq9qfxaa2t8nnnkqf2w9",
});
```

#### cURL

```bash
curl -X POST https://api.elevenlabs.io/v1/convai/whatsapp/outbound-message \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "whatsapp_phone_number_id": "524029457612345",
    "whatsapp_user_id": "12213231492",
    "template_name": "welcome",
    "template_language_code": "en",
    "template_params": [
      {
        "type": "body",
        "parameters": [
          {"type": "text", "parameter_name": "name", "text": "Daniele"}
        ]
      }
    ],
    "agent_id": "agent_9201kwcrbq9qfxaa2t8nnnkqf2w9"
  }'
```

Two details matter here:

* `template_params` is a list of component objects — the `{"type": "body", ...}` wrapper is required.
* `whatsapp_user_id` is digits only, with country code and no `+` (for example `14155552671`).

Find your `whatsapp_phone_number_id` on the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp) via the account menu's ***Copy phone number ID*** option.

Your phone receives the template. Reply to it — the agent picks up the conversation from there.

## If something didn't work

* **The agent never replies**: no agent is assigned to the number, or **Enable messaging** is off. If those look right, check whether the agent requires [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) — an inbound WhatsApp conversation starts with no user-provided values, so an agent whose tools or first message require one fails before replying unless a conversation initiation webhook supplies it. See [initialization context](/docs/eleven-agents/whatsapp#initialization-context).
* **The import fails**: the number is already registered with another provider or the WhatsApp Business app.
* **The API returned 200 but no message arrived**: the template is not approved yet, the parameters don't match the template, or your WhatsApp business account has unsettled payments (Meta error 131042).
* **The user's reply started a separate conversation without context**: the recipient ID format was off — see [recipient number format](/docs/eleven-agents/whatsapp/outbound#recipient-number-format).

For everything else, see [Troubleshooting & FAQ](/docs/eleven-agents/whatsapp/troubleshooting).

## Next steps

* Personalize conversations with [dynamic variables](/docs/eleven-agents/whatsapp/outbound#dynamic-variables-branches-and-environments) and the [personalization system variables](/docs/eleven-agents/whatsapp#personalization).
* Run outreach at scale with [outbound messages & templates](/docs/eleven-agents/whatsapp/outbound).
* Let the agent offer tappable choices with [interactive messages](/docs/eleven-agents/whatsapp/interactive-messages).
* Send WhatsApp messages from agents on other channels with [WhatsApp tools](/docs/eleven-agents/whatsapp/tools).
* Understand costs in the [pricing FAQ](/docs/eleven-agents/whatsapp/troubleshooting#faq).
