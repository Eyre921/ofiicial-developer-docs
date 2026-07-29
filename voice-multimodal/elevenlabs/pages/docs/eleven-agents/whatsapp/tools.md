---
title: "WhatsApp tools"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp/tools.md
path: docs/eleven-agents/whatsapp/tools
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WhatsApp tools

## Overview

You can give your agent a tool to send messages on WhatsApp, even during conversations on another channel (e.g. phone).

## Setup

#### Import your account

Follow the instructions [here](/docs/eleven-agents/whatsapp) to import your WhatsApp business
account.

#### Add an integration

Go to the [Integrations page](https://elevenlabs.io/app/agents/integrations), click the ***Add
integration*** button, select WhatsApp and connect your account:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e560b1b2a4345bd2fbe9519f7146b87d195268955d2b2aa2c6221629d97e4384/assets/images/agents/whatsapp/integration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=9959a0e7e7595968e27a98da58cdd62df1fa9abff79dd1904fc712e254eadb9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp integration" />

#### Add a tool

Go to the [Tools page](https://elevenlabs.io/app/agents/tools), click the ***Add integration
tool*** button, select the WhatsApp integration and the ***Send Message*** tool:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e85dcc3a3e3581250604311c516e080fb7f61f100b98b4b55be5f6071866e888/assets/images/agents/whatsapp/tool.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=9ffe22701f2250122164dad6e1a02fd1c6a9039a37b2ffecffdb36d64b04afc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp tool" />

## Using the tool

#### Create a message template

Go to [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/), open the
***Manage templates*** page and create a message template:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e2d2c8bcab0b4c664261a57658627fd4368fc00e4768e4bd4c16264c59d07e16/assets/images/agents/whatsapp/template-simple.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=5f6824b84aad92555ee10b802ee4924d5b7965e43524656c6a0c495d287c1b3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="WhatsApp message template" />

The tool currently only supports parameters in message body.

#### Configure your agent

Go to your agent configuration and add the tool:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0e078a4206030111493387ec6c9bc2235106ac3cb763d4555dd1ae7307c6d46a/assets/images/agents/whatsapp/tool-agent-config-tools.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=bc6f7481bffa5d5a26c2be47bfb0a3270514ef01fe3804380e8240fe05ceb57d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Agent configuration: tools" />

In the system prompt, tell the agent: - when to use the tool - what template name and language
code to use - what parameters to pass

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/893aa34f7bd3e01a0cbb919f08f801398de318d46e1d8d1a6c72a945193f7de9/assets/images/agents/whatsapp/tool-agent-config-prompt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=ba8a682ab5966df446c9809c89b431527a3760f8848d10104fe74c73383ea41e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Agent configuration: prompt" />

#### Test

Finally, it's time to test the tool configuration:

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/47d48232a04cd47112d5637288c6225761f7f66f3016f5fc7d9cf38a34b3782d/assets/images/agents/whatsapp/tool-conversation.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=171b0c62e9b1430d223fcdf971217602135ba6c4bac6a250a6dbd9deee595b3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Test conversation" />

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6b3809101caa5d38cf7ea761feb38f4ee316bfde4bef20e2e22eca6b14d0262f/assets/images/agents/whatsapp/tool-message-simple.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T113256Z&X-Amz-Expires=604800&X-Amz-Signature=14a7dba5556e696f3bc83851af53558ce90c0f178cf230c602316b7f75baff52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Test message received" width="300" />
