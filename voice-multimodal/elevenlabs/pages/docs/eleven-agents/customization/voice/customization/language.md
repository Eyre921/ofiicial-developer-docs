---
title: "Language"
source: https://elevenlabs.io/docs/eleven-agents/customization/voice/customization/language.md
path: docs/eleven-agents/customization/voice/customization/language
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Language

## Overview

This guide shows you how to configure your agent to speak multiple languages. You'll learn to:

* Configure your agent's primary language
* Add support for multiple languages
* Set language-specific voices and first messages
* Optimize voice selection for natural pronunciation
* Enable automatic language switching

#### Manage agents from your AI assistant

You can also make these changes conversationally. The [hosted MCP
server](/docs/eleven-agents/operate/hosted-mcp) lets Claude and other MCP clients create,
configure, and manage your agents through natural language.

## Guide

#### Default agent language

When you create a new agent, it's configured with:

* English as the primary language
* Flash v2 model for fast, English-only responses
* A default first message.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c533094b96146b19a31fd712a02a4b0b6d63790aa2168698e7dc682291c04e0b/assets/images/conversational-ai/language-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260802T113218Z&X-Amz-Expires=604800&X-Amz-Signature=7d44ccd0a0671d92ec69befdce942902105bfe39d7a2c0e305b496f01b3aeb79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Additional languages switch the agent to use the v2.5 Multilingual model. English will always use
the v2 model.

#### Add additional languages

#### Update via the dashboard

Navigate to your agent's configuration page and locate the **Agent** tab.

1. In the **Additional Languages** add an additional language (e.g. French)
2. Review the first message, which is automatically translated using a Large Language Model (LLM). Customize it as needed for each additional language to ensure accuracy and cultural relevance.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a5db1d23c7c1cc22b41f9093839cd76b078e6cbef69230714f8c0e58f3609b2f/assets/images/conversational-ai/language-selection.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260802T113218Z&X-Amz-Expires=604800&X-Amz-Signature=6517e7e2737ac3a68d6411314d0a712a12ce6a63ce78a4933830df67c5c2b954&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `conversation_config.agent.language` for the primary language and add entries to `conversation_config.language_presets` for each additional language. Each preset can override the first message and other conversation config fields per language:

```json
{
  "conversation_config": {
    "agent": {
      "language": "en"
    },
    "language_presets": {
      "fr": {
        "overrides": {
          "agent": {
            "first_message": "Bonjour, comment puis-je vous aider ?"
          }
        }
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
    conversation_config={
        "agent": {"language": "en"},
        "language_presets": {
            "fr": {
                "overrides": {
                    "agent": {"first_message": "Bonjour, comment puis-je vous aider ?"},
                },
            },
        },
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    agent: { language: "en" },
    languagePresets: {
      fr: {
        overrides: {
          agent: { firstMessage: "Bonjour, comment puis-je vous aider ?" },
        },
      },
    },
  },
});
```

Selecting the **All** option in the **Additional Languages** dropdown will configure the agent to
support 31 languages. Collectively, these languages are spoken by approximately 90% of the world's
population.

#### Configure language-specific voices

For optimal pronunciation, configure each additional language with a language-specific voice from our [Voice Library](https://elevenlabs.io/app/voice-library).

To find great voices for each language curated by the ElevenLabs team, visit the [language top
picks](https://elevenlabs.io/app/voice-library/collections).

#### Language-specific voice settings

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e1335d0fc8fe77691f00b928c9aeb5e050226a0d766dbab325ded52e97ed4399/assets/images/conversational-ai/language-voice.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260802T113218Z&X-Amz-Expires=604800&X-Amz-Signature=38d8b6014035a46160ad4193080f5fa8679cc3c2fcc286f41bb8209e8b9d2965&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Voice library

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/975e3c0207d86c06d4d68db0ef600ec6a716596062eabfec395b0356265f3583/assets/images/conversational-ai/voice-library-language.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260802T113218Z&X-Amz-Expires=604800&X-Amz-Signature=96854db4671593137d23647538dace8f08148d497ec342f3f349cdb8a82e2dbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Enable language detection

Add the [language detection tool](/docs/eleven-agents/customization/tools/system-tools/language-detection) to your agent can automatically switch to the user's preferred language.

#### Starting a call

Now that the agent is configured to support additional languages, the widget will prompt the user for their preferred language before the conversation begins.

If using the SDK, the language can be set programmatically using conversation overrides. See the
[Overrides](/docs/eleven-agents/customization/personalization/overrides) guide for implementation details.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4252ccb78e8c03f864b3389ec641a296ec99b9e89ae7d7efe2de36ef6132a152/assets/images/conversational-ai/widget-language.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260802T113218Z&X-Amz-Expires=604800&X-Amz-Signature=cad35b3c639aa29b046a1032cb351771fe42cdf84e358587ace7650f1caf1e97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Language selection is fixed for the duration of the call - users cannot switch languages
mid-conversation.

### Internationalization

You can integrate the widget with your internationalization framework by dynamically setting the language and UI text attributes.

```html title="Widget"
<elevenlabs-convai
  language="es"
  action-text={i18n["es"]["actionText"]}
  start-call-text={i18n["es"]["startCall"]}
  end-call-text={i18n["es"]["endCall"]}
  expand-text={i18n["es"]["expand"]}
  listening-text={i18n["es"]["listening"]}
  speaking-text={i18n["es"]["speaking"]}
></elevenlabs-convai>
```

Ensure the language codes match between your i18n framework and the agent's supported languages.

## Best practices

#### Voice selection

Select voices specifically trained in your target languages. This ensures:

* Natural pronunciation
* Appropriate regional accents
* Better handling of language-specific nuances

#### First message customization

While automatic translations are provided, consider:

* Reviewing translations for accuracy
* Adapting greetings for cultural context
* Adjusting formal/informal tone as needed
