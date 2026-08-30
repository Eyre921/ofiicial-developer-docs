---
title: "Language detection"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/language-detection.md
path: docs/eleven-agents/customization/tools/system-tools/language-detection
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Language detection

## Overview

The `language detection` system tool allows your ElevenLabs agent to switch its output language to any the agent supports.
This system tool is not enabled automatically. Its description can be customized to accommodate your specific use case.

Where possible, we recommend enabling all languages for an agent and enabling the language
detection system tool.

Our language detection tool triggers language switching in two cases, both based on the received audio's detected language and content:

* `detection` if a user speaks a different language than the current output language, a switch will be triggered
* `content` if the user asks in the current language to change to a new language, a switch will be triggered

**Purpose**: Automatically switch to the user's detected language during conversations.

**Trigger conditions**: The LLM should call this tool when:

* User speaks in a different language than the current conversation language
* User explicitly requests to switch languages
* Multi-language support is needed for the conversation

**Parameters**:

* `reason` (string, required): The reason for the language switch
* `language` (string, required): The language code to switch to (must be in supported languages list)

**Function call format**:

```json
{
  "type": "function",
  "function": {
    "name": "language_detection",
    "arguments": "{\"reason\": \"User requested Spanish\", \"language\": \"es\"}"
  }
}
```

**Implementation**: Configure supported languages in agent settings and add the language detection system tool. The agent will automatically switch voice and responses to match detected languages.

## Enabling language detection

#### Configure supported languages

The languages that the agent can switch to must be defined in the `Agent` settings tab.

![Agent languages](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/633707d54276febd3baa054c4f41b186225b74f606307a46e8262607befc8381/assets/images/conversational-ai/agent-languages.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T113147Z&X-Amz-Expires=604800&X-Amz-Signature=81e1eb7ceaa6e3a4ce4d99777667fb46ea4012629f05a723b3f21b60f2f7a338&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add the language detection tool

Enable language detection by selecting the pre-configured system tool to your agent's tools in the `Agent` tab.
This is automatically available as an option when selecting `add tool`.

![System tool](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3d17048ab2bc1a0547c49056abb98f624caf866927ff1714af27f898b06ab18f/assets/images/conversational-ai/language-detection-preconfig.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T113147Z&X-Amz-Expires=604800&X-Amz-Signature=0716e7b045f924a36e8bc1ec46c7c21dd69f767cda6e535a9f10d1c39b6c09c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Configure tool description

Add a description that specifies when to call the tool

![Description](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3bebc9fe07dba7121bce7793f3793858c710fc8ea1c221347604eb05929271df/assets/images/conversational-ai/language_detection.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T113147Z&X-Amz-Expires=604800&X-Amz-Signature=7e444e3bda29b9abce9d8fc13a799b56a466f6b36dcf19f01d6a0f85cfd5c5b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Restricting switching to the start of the conversation

In a long conversation, background speech or an unusual accent can occasionally trigger a switch the
caller did not intend. Enabling `only_at_conversation_start` confines switching to the first two user
turns.

If the language does not switch during those two turns, language detection is disabled for the rest
of the conversation: every later attempt fails and the agent keeps speaking the current language. If
the language does switch within that window, switching stays available for the rest of the
conversation, so an incorrect detection can still be corrected.

The option is disabled by default.

#### Update via the dashboard

Select the **Detect language** tool in the **Tools** tab and enable **Only at start of conversation**.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `only_at_conversation_start` on the language detection tool. Surrounding fields are
omitted here for brevity.

```json
{
  "conversation_config": {
    "agent": {
      "prompt": {
        "built_in_tools": {
          "language_detection": {
            "type": "system",
            "name": "language_detection",
            "params": {
              "system_tool_type": "language_detection",
              "only_at_conversation_start": true
            }
          }
        }
      }
    }
  }
}
```

#### Push your changes

```bash
elevenlabs agents push
```

#### Update via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "agent": {
            "prompt": {
                "built_in_tools": {
                    "language_detection": {
                        "type": "system",
                        "name": "language_detection",
                        "params": {
                            "system_tool_type": "language_detection",
                            "only_at_conversation_start": True,
                        },
                    }
                }
            }
        }
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    agent: {
      prompt: {
        builtInTools: {
          languageDetection: {
            type: "system",
            name: "language_detection",
            params: {
              systemToolType: "language_detection",
              onlyAtConversationStart: true,
            },
          },
        },
      },
    },
  },
});
```

When switching is blocked, the tool returns an error to the LLM instructing it to keep speaking
the current language. The reason is not exposed to the caller.

## API Implementation

When creating an agent via API, you can add the `language detection` tool to your agent configuration. It should be defined as a system tool:

```python
from elevenlabs import (
    ConversationalConfig,
    ElevenLabs,
    AgentConfig,
    PromptAgent,
    PromptAgentInputToolsItem_System,
    LanguagePresetInput,
    ConversationConfigClientOverrideInput,
    AgentConfigOverride,
)

# Initialize the client
elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

# Create the language detection tool
language_detection_tool = PromptAgentInputToolsItem_System(
    name="language_detection",
    description=""  # Optional: Customize when the tool should be triggered
)

# Create language presets
language_presets = {
    "nl": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Hoi, hoe gaat het met je?",
                language=None
            ),
            tts=None
        ),
        first_message_translation=None
    ),
    "fi": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                first_message="Hei, kuinka voit?",
            ),
            tts=None
        ),
    ),
    "tr": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Merhaba, nasılsın?",
                language=None
            ),
            tts=None
        ),
    ),
    "ru": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Привет, как ты?",
                language=None
            ),
            tts=None
        ),
    ),
    "pt": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Oi, como você está?",
                language=None
            ),
            tts=None
        ),
    )
}

# Create the agent configuration
conversation_config = ConversationalConfig(
    agent=AgentConfig(
        prompt=PromptAgent(
            tools=[language_detection_tool],
            first_message="Hi how are you?"
        )
    ),
    language_presets=language_presets
)

# Create the agent
response = elevenlabs.conversational_ai.agents.create(
    conversation_config=conversation_config
)
```

```javascript
import { ElevenLabs } from "@elevenlabs/elevenlabs-js";

// Initialize the client
const elevenlabs = new ElevenLabs({
  apiKey: "YOUR_API_KEY",
});

// Create the agent with language detection tool
await elevenlabs.conversationalAi.agents.create({
  conversationConfig: {
    agent: {
      prompt: {
        tools: [
          {
            type: "system",
            name: "language_detection",
            description: "", // Optional: Customize when the tool should be triggered
          },
        ],
        firstMessage: "Hi, how are you?",
      },
    },
    languagePresets: {
      nl: {
        overrides: {
          agent: {
            prompt: null,
            firstMessage: "Hoi, hoe gaat het met je?",
            language: null,
          },
          tts: null,
        },
      },
      fi: {
        overrides: {
          agent: {
            prompt: null,
            firstMessage: "Hei, kuinka voit?",
            language: null,
          },
          tts: null,
        },
        firstMessageTranslation: {
          sourceHash: '{"firstMessage":"Hi how are you?","language":"en"}',
          text: "Hei, kuinka voit?",
        },
      },
      tr: {
        overrides: {
          agent: {
            prompt: null,
            firstMessage: "Merhaba, nasılsın?",
            language: null,
          },
          tts: null,
        },
      },
      ru: {
        overrides: {
          agent: {
            prompt: null,
            firstMessage: "Привет, как ты?",
            language: null,
          },
          tts: null,
        },
      },
      pt: {
        overrides: {
          agent: {
            prompt: null,
            firstMessage: "Oi, como você está?",
            language: null,
          },
          tts: null,
        },
      },
      ar: {
        overrides: {
          agent: {
            prompt: null,
            firstMessage: "مرحبًا كيف حالك؟",
            language: null,
          },
          tts: null,
        },
      },
    },
  },
});
```

```bash
curl -X POST https://api.elevenlabs.io/v1/convai/agents/create \
     -H "xi-api-key: YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
  "conversation_config": {
    "agent": {
      "prompt": {
        "first_message": "Hi how are you?",
        "tools": [
          {
            "type": "system",
            "name": "language_detection",
            "description": ""
          }
        ]
      }
    },
    "language_presets": {
      "nl": {
        "overrides": {
          "agent": {
            "prompt": null,
            "first_message": "Hoi, hoe gaat het met je?",
            "language": null
          },
          "tts": null
        }
      },
      "fi": {
        "overrides": {
          "agent": {
            "prompt": null,
            "first_message": "Hei, kuinka voit?",
            "language": null
          },
          "tts": null
        }
      },
      "tr": {
        "overrides": {
          "agent": {
            "prompt": null,
            "first_message": "Merhaba, nasılsın?",
            "language": null
          },
          "tts": null
        }
      },
      "ru": {
        "overrides": {
          "agent": {
            "prompt": null,
            "first_message": "Привет, как ты?",
            "language": null
          },
          "tts": null
        }
      },
      "pt": {
        "overrides": {
          "agent": {
            "prompt": null,
            "first_message": "Oi, como você está?",
            "language": null
          },
          "tts": null
        }
      },
      "ar": {
        "overrides": {
          "agent": {
            "prompt": null,
            "first_message": "مرحبًا كيف حالك؟",
            "language": null
          },
          "tts": null
        }
      }
    }
  }
}'
```

Leave the description blank to use the default language detection prompt.
