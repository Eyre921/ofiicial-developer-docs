---
title: "WhatsApp tools"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp/tools.md
path: docs/eleven-agents/whatsapp/tools
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WhatsApp tools

## Overview

You can give your agent a tool to send messages on WhatsApp, even during conversations on another channel (e.g. phone).

The WhatsApp integration provides three tools:

* **Send Message** — sends a template message to any WhatsApp user. Works from any channel, so a phone agent can, for example, text a confirmation to the caller's WhatsApp. This page covers this tool.
* **Send Interactive Buttons** and **Send Interactive List** — offer tappable choices to the user of a live WhatsApp conversation. These only work within WhatsApp message conversations — see [Interactive messages](/docs/eleven-agents/whatsapp/interactive-messages).

## Setup

#### Import your account

Follow the instructions [here](/docs/eleven-agents/whatsapp) to import your WhatsApp business
account.

#### Add an integration

Go to the [Integrations page](https://elevenlabs.io/app/agents/integrations), click the ***Add
integration*** button, select WhatsApp and connect your account:

![WhatsApp integration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e560b1b2a4345bd2fbe9519f7146b87d195268955d2b2aa2c6221629d97e4384/assets/images/agents/whatsapp/integration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=fbcc6422c7919fd276f84ef90c1f03fd82254fa33303c21ebf0777d48494d1cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add a tool

Go to the [Tools page](https://elevenlabs.io/app/agents/tools), click the ***Add integration
tool*** button, select the WhatsApp integration and the ***Send Message*** tool:

![WhatsApp tool](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e85dcc3a3e3581250604311c516e080fb7f61f100b98b4b55be5f6071866e888/assets/images/agents/whatsapp/tool.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=d90aa2329a923a181b565be4ff87d20862a887da0e1aac030f242524ed52868f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Using the tool

#### Create a message template

Go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/), open the
***Manage templates*** page and create a message template:

![WhatsApp message template](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e2d2c8bcab0b4c664261a57658627fd4368fc00e4768e4bd4c16264c59d07e16/assets/images/agents/whatsapp/template-simple.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=ce85ac0df41020b0b1c283b4026e1bf2fe8607db3f1e243f1b69e1816d520d83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The tool currently only supports parameters in message body.

#### Configure your agent

Go to your agent configuration and add the tool:

![Agent configuration: tools](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0e078a4206030111493387ec6c9bc2235106ac3cb763d4555dd1ae7307c6d46a/assets/images/agents/whatsapp/tool-agent-config-tools.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=bbb6c1733c25e5fa41994f4349208be7e2d1f2217090f37dc49f402fab75b0a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

In the system prompt, tell the agent:

* when to use the tool
* what template name and language code to use
* what parameters to pass

![Agent configuration: prompt](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/893aa34f7bd3e01a0cbb919f08f801398de318d46e1d8d1a6c72a945193f7de9/assets/images/agents/whatsapp/tool-agent-config-prompt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=b9232dce24faabb65d9bacef80f8f107a12bc9e7d6361a1c1f9c7b7898ff6bf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Test

Test the tool configuration:

![Test conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/47d48232a04cd47112d5637288c6225761f7f66f3016f5fc7d9cf38a34b3782d/assets/images/agents/whatsapp/tool-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=a15aa584ba1602bf51c65d883e40db5ad56b29e0a681cd139587a0fd6f8fc0e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)![Test message received](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6b3809101caa5d38cf7ea761feb38f4ee316bfde4bef20e2e22eca6b14d0262f/assets/images/agents/whatsapp/tool-message-simple.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260909%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260909T075105Z&X-Amz-Expires=604800&X-Amz-Signature=47238308f1a1426aa031e7b1098cfb956db61544fefd648a10f030b988db90b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Parameters and language codes

The tool fills the template's **body** parameters only — templates with parameterized headers or buttons are not supported by this tool. The recipient is a WhatsApp user ID: digits only, with country code and no `+` (for example `14155552671`) — see the [recipient number format rules](/docs/eleven-agents/whatsapp/outbound#recipient-number-format) for country-specific caveats.

The template language code must match the language the template was created with in WhatsApp Manager — see [supported language codes](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/supported-languages/). A common mistake is passing `en` for a template created as `en_US` (or vice versa); Meta treats these as different templates.

## Troubleshooting

* **Template not found**: the template name or language code doesn't match WhatsApp Manager exactly, or the template belongs to a different WhatsApp business account than the connected one.
* **Message accepted but not delivered**: the template is not approved, a body parameter is missing, or the account has payment issues — see [Troubleshooting & FAQ](/docs/eleven-agents/whatsapp/troubleshooting#message-accepted-but-not-delivered).
* **The agent passes wrong parameters**: state the template's exact parameter names and expected values in the system prompt, and give one example invocation.
