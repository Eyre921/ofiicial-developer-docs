---
title: "Overrides"
source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/overrides.md
path: docs/eleven-agents/customization/personalization/overrides
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Overrides

While overrides are still supported for completely replacing system prompts or first messages, we
recommend using [Dynamic Variables](/docs/eleven-agents/customization/personalization/dynamic-variables) as the preferred
way to customize your agent's responses and inject real-time data. Dynamic Variables offer better
maintainability and a more structured approach to personalization.

**Overrides** enable your assistant to adapt its behavior for each user interaction. You can pass custom data and settings at the start of each conversation, allowing the assistant to personalize its responses and knowledge with real-time context. Overrides completely override the agent's default values defined in the agent's [dashboard](https://elevenlabs.io/app/agents/agents).

## Overview

Overrides allow you to modify your AI agent's behavior in real-time without creating multiple agents. This enables you to personalize responses with user-specific data.

Overrides can be enabled for the following fields in the agent's security settings:

* System prompt
* First message
* Language
* Voice ID
* LLM (Large Language Model)
* Tools
* Knowledge base
* Text-only mode
* Stability
* Speed
* Similarity boost
* ASR keywords

When overrides are enabled for a field, providing an override is still optional. If not provided, the agent will use the default values defined in the agent's [dashboard](https://elevenlabs.io/app/agents/agents). For most fields, an error will be thrown if an override is provided when that field does not have overrides enabled.

**ASR keywords** use soft disallow: if the Security toggle is off and the client still sends
`asr.keywords`, the conversation continues and the keywords are ignored (no error). Enable the
**ASR keywords** override in Security settings when you want per-conversation keyword boosting to
apply. Up to 50 keywords are supported per conversation.

Here are a few examples where overrides can be useful:

* **Greet users** by their name
* **Include account-specific details** in responses
* **Adjust the agent's language** or tone based on user preferences
* **Pass real-time data** like account balances or order status
* **Boost transcription** of per-call names or terms (for example CRM company names) via ASR keywords

Overrides are particularly useful for applications requiring personalized interactions or handling
sensitive user data that shouldn't be stored in the agent's base configuration.

## Guide

### Prerequisites

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenLabs Conversational Agent ([create one here](/docs/eleven-agents/quickstart))

This guide shows you how to override the default agent **System prompt**, **First message**, **LLM**, **Tools**, **Knowledge base**, **TTS settings**, and **ASR keywords**.

#### Enable overrides

For security reasons, overrides are disabled by default. Enable the fields you want to allow overriding, such as `first_message`, `prompt.prompt`, `prompt.tool_ids`, `prompt.knowledge_base`, `language`, or `asr.keywords`.

#### Update via the dashboard

Navigate to your agent's settings and select the **Security** tab. Enable the `First message`, `System prompt`, `Tools`, `Knowledge base`, `ASR keywords`, and any other overrides you need, such as `LLM`.

![Enable overrides](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/496f20380ffe29fc46275bbfe5c6eaabdb5e211c780188243a018b38715ea779/assets/images/conversational-ai/enable-overrides.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T070932Z&X-Amz-Expires=604800&X-Amz-Signature=ae790dc195021ad7a9baf4873180f7d581adc526db5cbbf1dda6815868e8522f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set fields under `platform_settings.overrides.conversation_config_override` to `true` to allow runtime overrides for that field:

```json
{
  "platform_settings": {
    "overrides": {
      "conversation_config_override": {
        "agent": {
          "first_message": true,
          "language": true,
          "prompt": {
            "prompt": true,
            "tool_ids": true,
            "knowledge_base": true
          }
        },
        "tts": { "voice_id": true },
        "asr": { "keywords": true }
      }
    }
  }
}
```

#### Push your changes

```bash
elevenlabs agents push --agent "<agent-name>"
```

#### Update via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    platform_settings={
        "overrides": {
            "conversation_config_override": {
                "agent": {
                    "first_message": True,
                    "language": True,
                    "prompt": {
                        "prompt": True,
                        "tool_ids": True,
                        "knowledge_base": True,
                    },
                },
                "tts": {"voice_id": True},
                "asr": {"keywords": True},
            },
        },
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  platformSettings: {
    overrides: {
      conversationConfigOverride: {
        agent: {
          firstMessage: true,
          language: true,
          prompt: {
            prompt: true,
            toolIds: true,
            knowledgeBase: true,
          },
        },
        tts: { voiceId: true },
        asr: { keywords: true },
      },
    },
  },
});
```

#### Override the conversation

In your code, where the conversation is started, pass the overrides as a parameter. Tool and knowledge base overrides replace the default arrays for that conversation. ASR keyword overrides replace the agent's default keyword list for that conversation (maximum 50 keywords).

```json title="Conversation initiation payload" focus={4-15}
{
  "conversation_config_override": {
    "agent": {
      "prompt": {
        "tool_ids": ["tool_7101k5zvyjhmfg983brhmhkd98n6"],
        "knowledge_base": [
          {
            "type": "file",
            "name": "Unladen Swallow Facts",
            "id": "5xM3yVvZQKV0EfqQpLrJ",
            "usage_mode": "auto"
          }
        ]
      }
    },
    "asr": {
      "keywords": ["Acme Corp", "Contoso", "Globex"]
    }
  }
}
```

Ensure you have the latest [SDK](/docs/eleven-agents/libraries/python) installed.

```python title="Python" focus={3-28} maxLines=28
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
...
conversation_override = {
    "agent": {
        "prompt": {
            "prompt": f"The customer's bank account balance is {customer_balance}. They are based in {customer_location}.", # Optional: override the system prompt.
            "llm": "gpt-4o", # Optional: override the LLM model.
            "tool_ids": [
                "tool_7101k5zvyjhmfg983brhmhkd98n6"
            ], # Optional: replace the tools available to the agent.
            "knowledge_base": [
                {
                    "type": "file",
                    "name": "Unladen Swallow Facts",
                    "id": "5xM3yVvZQKV0EfqQpLrJ",
                    "usage_mode": "auto",
                }
            ], # Optional: replace the knowledge base available to the agent.
        },
        "first_message": f"Hi {customer_name}, how can I help you today?", # Optional: override the first_message.
        "language": "en" # Optional: override the language.
    },
    "tts": {
        "voice_id": "custom_voice_id", # Optional: override the voice.
        "stability": 0.7, # Optional: override stability (0.0 to 1.0).
        "speed": 1.1, # Optional: override speed (0.7 to 1.2).
        "similarity_boost": 0.9 # Optional: override similarity boost (0.0 to 1.0).
    },
    "conversation": {
        "text_only": True # Optional: enable text-only mode (no audio).
    },
    "asr": {
        "keywords": ["Acme Corp", "Contoso"] # Optional: boost ASR for per-call terms (max 50). Requires Security → ASR keywords.
    }
}

config = ConversationInitiationData(
    conversation_config_override=conversation_override
)
conversation = Conversation(
    ...
    config=config,
    ...
)
conversation.start_session()
```

```javascript title="JavaScript" focus={4-29} maxLines=29
...
const conversation = await Conversation.startSession({
  ...
  overrides: {
      agent: {
          prompt: {
              prompt: `The customer's bank account balance is ${customer_balance}. They are based in ${customer_location}.`, // Optional: override the system prompt.
              llm: "gpt-4o", // Optional: override the LLM model.
              toolIds: [
                  "tool_7101k5zvyjhmfg983brhmhkd98n6"
              ], // Optional: replace the tools available to the agent.
              knowledgeBase: [
                  {
                      type: "file",
                      name: "Unladen Swallow Facts",
                      id: "5xM3yVvZQKV0EfqQpLrJ",
                      usageMode: "auto",
                  }
              ], // Optional: replace the knowledge base available to the agent.
          },
          firstMessage: `Hi ${customer_name}, how can I help you today?`, // Optional: override the first message.
          language: "en" // Optional: override the language.
      },
      tts: {
          voiceId: "custom_voice_id", // Optional: override the voice.
          stability: 0.7, // Optional: override stability (0.0 to 1.0).
          speed: 1.1, // Optional: override speed (0.7 to 1.2).
          similarityBoost: 0.9 // Optional: override similarity boost (0.0 to 1.0).
      },
      conversation: {
          textOnly: true // Optional: enable text-only mode (no audio).
      },
      asr: {
          keywords: ["Acme Corp", "Contoso"] // Optional: boost ASR for per-call terms (max 50). Requires Security → ASR keywords.
      }
  },
  ...
})
```

```swift title="Swift" focus={3-16} maxLines=16
import ElevenLabsSDK

let promptOverride = ElevenLabsSDK.AgentPrompt(
    prompt: "The customer's bank account balance is \(customer_balance). They are based in \(customer_location).", // Optional: override the system prompt.
    llm: "gpt-4o" // Optional: override the LLM model.
)
let agentConfig = ElevenLabsSDK.AgentConfig(
    prompt: promptOverride, // Optional: override the system prompt.
    firstMessage: "Hi \(customer_name), how can I help you today?", // Optional: override the first message.
    language: .en // Optional: override the language.
)
let ttsConfig = ElevenLabsSDK.TTSConfig(
    voiceId: "custom_voice_id", // Optional: override the voice.
    stability: 0.7, // Optional: override stability (0.0 to 1.0).
    speed: 1.1, // Optional: override speed (0.7 to 1.2).
    similarityBoost: 0.9 // Optional: override similarity boost (0.0 to 1.0).
)
let conversationConfig = ElevenLabsSDK.ConversationConfig(
    textOnly: true // Optional: enable text-only mode (no audio).
)
let overrides = ElevenLabsSDK.ConversationConfigOverride(
    agent: agentConfig, // Optional: override agent settings.
    tts: ttsConfig, // Optional: override TTS settings.
    conversation: conversationConfig // Optional: override conversation settings.
)

let config = ElevenLabsSDK.SessionConfig(
    agentId: "",
    overrides: overrides
)

let conversation = try await ElevenLabsSDK.Conversation.startSession(
  config: config,
  callbacks: callbacks
)
```

```html title="Widget"
  <elevenlabs-convai
    agent-id="agent_7101k5zvyjhmfg983brhmhkd98n6"
    override-language="es"         <!-- Optional: override the language -->
    override-prompt="Custom system prompt for this user"  <!-- Optional: override the system prompt -->
    override-first-message="Hi! How can I help you today?"  <!-- Optional: override the first message -->
    override-voice-id="custom_voice_id"  <!-- Optional: override the voice -->
  ></elevenlabs-convai>
```

When using overrides, omit any fields you don't want to override rather than setting them to empty strings or null values. Only include the fields you specifically want to customize.

To find the correct LLM model string, refer to the [Agent API reference](/docs/api-reference/agents/create#request.body.conversation_config.agent.prompt.llm) which lists all supported LLM models and their exact string identifiers.
