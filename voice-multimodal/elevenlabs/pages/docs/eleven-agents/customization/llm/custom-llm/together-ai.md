---
title: "Together AI"
source: https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm/together-ai.md
path: docs/eleven-agents/customization/llm/custom-llm/together-ai
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Together AI

## Overview

[Together AI](https://www.together.ai/) provides an AI Acceleration Cloud, allowing you to train, fine-tune, and run inference on AI models blazing fast, at low cost, and at production scale.

Instantly run [200+ models](https://together.xyz/models) including DeepSeek, Llama3, Mixtral, and Stable Diffusion, optimized for peak latency, throughput, and context length.

## Choosing a model

To make use of the full power of ElevenLabs Agents you need to use a model that supports tool use and structured outputs. Together AI supports function calling for [these models](https://docs.together.ai/docs/function-calling):

* meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
* meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo
* meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo
* meta-llama/Llama-3.3-70B-Instruct-Turbo
* mistralai/Mixtral-8x7B-Instruct-v0.1
* mistralai/Mistral-7B-Instruct-v0.1

With this in mind, it's recommended to use at least `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo` for your ElevenLabs Agents agent.

## Set up Llama 3.1 on Together AI

Navigate to [api.together.xyz/settings/api-keys](https://api.together.xyz/settings/api-keys) and create a new API key.

![Add Secret](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/97323ef6ffb761b54a7b5c4183054bc1fd621d1069a38cbeb474444e84de75f4/assets/images/conversational-ai/together-ai/together-ai-api-key.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261003T233250Z&X-Amz-Expires=604800&X-Amz-Signature=26023ecab5af12c9d90f3f6994019479434da3a52cb2bf86859d27e4e9003521&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once you have your API key, you can test it by running the following curl command:

```bash
curl https://api.together.xyz/v1/chat/completions -s \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <API_KEY>" \
-d '{
"model": "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
"messages": [{
    "role": "user",
    "content": "Hello, how are you?"
}]
}'
```

Navigate to your [AI Agent](https://elevenlabs.io/app/agents), scroll down to the "Secrets" section and select "Add Secret". After adding the secret, make sure to hit "Save" to make the secret available to your agent.

![Add Secret](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/43e5478a3c62f31d2d9f66f9919e7c4c1b5878e3b79681d08741221ce3e689d8/assets/images/conversational-ai/together-ai/together-ai-secret.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261003T233250Z&X-Amz-Expires=604800&X-Amz-Signature=98bd374d3c395a0bd686baf6413db9691edefbb4d2f88f7061740eee47c65d52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose "Custom LLM" from the dropdown menu.

![Choose custom llm](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/45ec75f558a5c8e5070bd3170d96cbc54ef63e15d9f04ac472a45854a22a17ac/assets/images/conversational-ai/byollm-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261003T233250Z&X-Amz-Expires=604800&X-Amz-Signature=46f038b57cf6a28a4aa0c13ec5c0b4d5a6cc08188772ba9d7c5dee0c383aba95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the Server URL, specify Together AI's OpenAI-compatible API endpoint: `https://api.together.xyz/v1`. For the Model ID, specify `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo` as discussed above, and select your API key from the dropdown menu.

![Enter url](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/94d7f96a16d483327751195b306431b5d7c0e4df237510b74d7e98f28b58efe1/assets/images/conversational-ai/together-ai/together-ai-llm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261003T233250Z&X-Amz-Expires=604800&X-Amz-Signature=19779c9d1711dd53986a2fac995ce12985b504d1c36d616228b70f598a5f04db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Now you can go ahead and click "Test AI Agent" to chat with your custom Llama 3.1 model.
