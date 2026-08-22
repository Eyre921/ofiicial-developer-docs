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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e560b1b2a4345bd2fbe9519f7146b87d195268955d2b2aa2c6221629d97e4384/assets/images/agents/whatsapp/integration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=ac81811179f4a3515f1c32e3238597e088257e525713368f1e239c63ac055cec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp integration" />

#### Add a tool

Go to the [Tools page](https://elevenlabs.io/app/agents/tools), click the ***Add integration
tool*** button, select the WhatsApp integration and the ***Send Message*** tool:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e85dcc3a3e3581250604311c516e080fb7f61f100b98b4b55be5f6071866e888/assets/images/agents/whatsapp/tool.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=771a07ef35380e6b2e2fa01a09d8efd4be33a805acbd19919d3150cc686f166c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp tool" />

## Using the tool

#### Create a message template

Go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/), open the
***Manage templates*** page and create a message template:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e2d2c8bcab0b4c664261a57658627fd4368fc00e4768e4bd4c16264c59d07e16/assets/images/agents/whatsapp/template-simple.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=56aee4a5d64f18351f0f1405ee3f1cfa6a15e47fca8dba613bbc5503a0b17a9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp message template" />

The tool currently only supports parameters in message body.

#### Configure your agent

Go to your agent configuration and add the tool:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0e078a4206030111493387ec6c9bc2235106ac3cb763d4555dd1ae7307c6d46a/assets/images/agents/whatsapp/tool-agent-config-tools.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=829188cad2fab88faf5248c0c1627e523e1f2caa5181ff2e3d2b7a9347577607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Agent configuration: tools" />

In the system prompt, tell the agent:

* when to use the tool
* what template name and language code to use
* what parameters to pass

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/893aa34f7bd3e01a0cbb919f08f801398de318d46e1d8d1a6c72a945193f7de9/assets/images/agents/whatsapp/tool-agent-config-prompt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=50d03385e7a307e9652afdaa57ff58f56fe1b729a706b5a53fc87518d7de52d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Agent configuration: prompt" />

#### Test

Test the tool configuration:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/47d48232a04cd47112d5637288c6225761f7f66f3016f5fc7d9cf38a34b3782d/assets/images/agents/whatsapp/tool-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=c4faef392e896814b3e5d832afac00f8bf3f17fcb92e0f5dbcc8904419e189b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Test conversation" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6b3809101caa5d38cf7ea761feb38f4ee316bfde4bef20e2e22eca6b14d0262f/assets/images/agents/whatsapp/tool-message-simple.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260822%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260822T233244Z&X-Amz-Expires=604800&X-Amz-Signature=27243f970910c3924239922e48025fb78e2716d1a3c4b7eaacbbe523e95d0cb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Test message received" width="300" />

## Parameters and language codes

The tool fills the template's **body** parameters only — templates with parameterized headers or buttons are not supported by this tool. The recipient is a WhatsApp user ID: digits only, with country code and no `+` (for example `14155552671`) — see the [recipient number format rules](/docs/eleven-agents/whatsapp/outbound#recipient-number-format) for country-specific caveats.

The template language code must match the language the template was created with in WhatsApp Manager — see [supported language codes](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/supported-languages/). A common mistake is passing `en` for a template created as `en_US` (or vice versa); Meta treats these as different templates.

## Troubleshooting

* **Template not found**: the template name or language code doesn't match WhatsApp Manager exactly, or the template belongs to a different WhatsApp business account than the connected one.
* **Message accepted but not delivered**: the template is not approved, a body parameter is missing, or the account has payment issues — see [Troubleshooting & FAQ](/docs/eleven-agents/whatsapp/troubleshooting#message-accepted-but-not-delivered).
* **The agent passes wrong parameters**: state the template's exact parameter names and expected values in the system prompt, and give one example invocation.
