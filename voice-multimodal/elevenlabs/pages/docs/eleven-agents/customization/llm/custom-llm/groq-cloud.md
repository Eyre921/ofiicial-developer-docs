---
title: "Groq Cloud"
source: https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm/groq-cloud.md
path: docs/eleven-agents/customization/llm/custom-llm/groq-cloud
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Groq Cloud

## Overview

[Groq Cloud](https://console.groq.com/) provides easy access to fast AI inference, giving you OpenAI-compatible API endpoints in a matter of clicks.

Use leading [Openly-available Models](https://console.groq.com/docs/overview/models) like Llama, Mixtral, and Gemma as the brain for your ElevenLabs agents in a few easy steps.

## Choosing a model

To make use of the full power of ElevenLabs agents you need to use a model that supports tool use and structured outputs. Groq recommends the following Llama-3.3 models their versatility and performance:

* meta-llama/llama-4-scout-17b-16e-instruct (10M token context window) and support for 12 languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese)
* llama-3.3-70b-versatile (128k context window | 32,768 max output tokens)
* llama-3.1-8b-instant (128k context window | 8,192 max output tokens)

With this in mind, it's recommended to use `meta-llama/llama-4-scout-17b-16e-instruct` for your ElevenLabs Agents agent.

## Set up Llama 3.3 on Groq Cloud

Navigate to [console.groq.com/keys](https://console.groq.com/keys) and create a new API key.

![Add Secret](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2dc1bdac30871fb4059a394b8edfedd4cf953f8e1f787ca8b807a9f195e7fdf3/assets/images/conversational-ai/groq-cloud/groq-api-key.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261007T113228Z&X-Amz-Expires=604800&X-Amz-Signature=a2cf7b50dd13c74140b876c8efdfae4447440fb4861256a6f71221d8ffa6fab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once you have your API key, you can test it by running the following curl command:

```bash
curl https://api.groq.com/openai/v1/chat/completions -s \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $GROQ_API_KEY" \
-d '{
"model": "llama-3.3-70b-versatile",
"messages": [{
    "role": "user",
    "content": "Hello, how are you?"
}]
}'
```

Navigate to your [AI Agent](https://elevenlabs.io/app/agents), scroll down to the "Secrets" section and select "Add Secret". After adding the secret, make sure to hit "Save" to make the secret available to your agent.

![Add Secret](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/464e123d926fbd9e6986a382af8da55d9f3861d1e593bb1f4b41ba33bed67ae1/assets/images/conversational-ai/groq-cloud/groq-secret.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261007T113228Z&X-Amz-Expires=604800&X-Amz-Signature=2120afa4354d0cb0723a73295a14f2a1ecf87ab0fe23422bbd001a69410e6694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose "Custom LLM" from the dropdown menu.

![Choose custom llm](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/45ec75f558a5c8e5070bd3170d96cbc54ef63e15d9f04ac472a45854a22a17ac/assets/images/conversational-ai/byollm-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261007T113228Z&X-Amz-Expires=604800&X-Amz-Signature=60c6c1cdc4abf5a00f7485744e2214e04a55094c8eec1d35404a423936e834f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the Server URL, specify Groq's OpenAI-compatible API endpoint: `https://api.groq.com/openai/v1`. For the Model ID, specify `meta-llama/llama-4-scout-17b-16e-instruct` as discussed above, and select your API key from the dropdown menu.

![Enter url](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/70555982e71101023f8e988102ab505c964fd6796a190a9bce74f3c0ed1b56be/assets/images/conversational-ai/groq-cloud/groq-llm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261007T113228Z&X-Amz-Expires=604800&X-Amz-Signature=ec3ba3b208ca7bfe4a8c9ea8fb463a6695cc3ef6d5d5fe06aed6d405a9c4e174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Now you can go ahead and click "Test AI Agent" to chat with your custom Llama 3.3 model.
