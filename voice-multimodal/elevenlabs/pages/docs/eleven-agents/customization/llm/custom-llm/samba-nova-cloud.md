---
title: "SambaNova Cloud"
source: https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm/samba-nova-cloud.md
path: docs/eleven-agents/customization/llm/custom-llm/samba-nova-cloud
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# SambaNova Cloud

## Overview

[SambaNova Cloud](http://cloud.sambanova.ai?utm_source=elevenlabs\&utm_medium=external\&utm_campaign=cloud_signup) is the fastest provider of the best [open source models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models), including DeepSeek R1, DeepSeek V3, Llama 4 Maverick and others. Through an
OpenAI-compatible API endpoint, you can set up your ElevenLabs agent on ElevenLabs in a just few minutes.

Watch this [video](https://www.youtube.com/watch?v=46W96JcE_p8) for a walkthrough and demo of how you can configure your ElevenLabs Agents agent to leverage SambaNova's blazing-fast LLMs!

## Choosing a model

To make use of the full power of ElevenLabs Agents you need to use a model that supports tool use and structured outputs. SambaNova recommends the following models for their accuracy and performance:

* `DeepSeek-V3-0324` (671B model)
* `Meta-Llama-3.3-70B-Instruct`
* `Llama-4-Maverick-17B-128E-Instruct`
* `Qwen3-32B`

For up-to-date information on model-specific context windows, please refer to [this](https://docs.sambanova.ai/cloud/docs/get-started/supported-models) page.

Note that `Meta-Llama-3.3-70B-Instruct` is SambaNova's most battle-tested model. If any model is causing issues, you may report it on SambaNova's [Community page](https://community.sambanova.ai).

## Configuring your ElevenLabs agent with a SambaNova LLM

Navigate to [cloud.sambanova.ai/apis](https://cloud.sambanova.ai/apis?utm_source=elevenlabs\&utm_medium=external\&utm_campaign=cloud_signup) and create a new API key.

![Add Secret](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9f15e96bc7394d1be5936a155aeaf3c450c48b1164623c0ca3a05f723aec81cd/assets/images/conversational-ai/sambanova-cloud/sn-api-key.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T233231Z&X-Amz-Expires=604800&X-Amz-Signature=19327ddf2ece5212189fe5a19ca92c2695effe6d0437b5d4789159fd0e268c0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once you have your API key, you can test it by running the following curl command:

```bash
curl -H "Authorization: Bearer <your-api-key>" \
 -H "Content-Type: application/json" \
 -d '{
"stream": true,
"model": "DeepSeek-V3-0324",
"messages": [
	{
		"role": "system",
		"content": "You are a helpful assistant"
	},
	{
		"role": "user",
		"content": "Hello"
	}
]
}' \
 -X POST https://api.sambanova.ai/v1/chat/completions
```

Create a new [AI Agent](https://elevenlabs.io/app/agents/agents) or edit an existing one.

Scroll down to the "Workspace Secrets" section and select "Add Secret". Name the key `SAMBANOVA_API_KEY` and copy the value from the SambaNova Cloud dashboard. Be sure to hit "Save" to make the secret available to your agent.

![Add Secret](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8505deccfb198fbf8d33e3b936f65bf85caf59811bffbb708a5d526faa3329bc/assets/images/conversational-ai/sambanova-cloud/workspace-secret.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T233231Z&X-Amz-Expires=604800&X-Amz-Signature=86db8fc20c165859d7157ac70d2fcab58f5be01e549151f24d4f07bbf8672f14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose "Custom LLM" from the dropdown menu.

![Choose custom llm](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/45ec75f558a5c8e5070bd3170d96cbc54ef63e15d9f04ac472a45854a22a17ac/assets/images/conversational-ai/byollm-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T233231Z&X-Amz-Expires=604800&X-Amz-Signature=26c5fba8d6f74e34b4b02483d9fdf4c4dd28cdfc6b789b59f2dfecfd81d33acc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the Server URL, specify SambaNova's OpenAI-compatible API endpoint: `https://api.sambanova.ai/v1`. For the Model ID, specify one the model names indicated above (e.g., `Meta-Llama-3.3-70B-Instruct`) and select the `SAMBANOVA_API_KEY` API key from the dropdown menu.

![Enter url](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d1e6fec480a23a0c3b11ca3b675dfddeaffe59f7a24becfaf1986675b109b99b/assets/images/conversational-ai/sambanova-cloud/sn-llm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T233231Z&X-Amz-Expires=604800&X-Amz-Signature=3a34a713619549f36f9e59790904601b5e994ad87ef74c44859074f5bfb19a13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Set the max tokens to 1024 to restrict the agent's output for brevity. Also be sure to include an instruction in the System Prompt for the model to respond in 500 words or less.

![Enter url](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2be33272ea2e7aaf6166d482a41bdf492f3a75f1e43e2e8cb9cf363fb3b6188f/assets/images/conversational-ai/sambanova-cloud/sn-maxtokens.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T233231Z&X-Amz-Expires=604800&X-Amz-Signature=81b3340c1e1ab229ece79d29fa425ae9b67c05a55881bbb6ef698dfec59eb9b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Save your changes and click on "Test AI Agent" to chat with your SambaNova-powered agent!
