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

You can also make these changes conversationally. The [hosted MCP server](/docs/eleven-agents/operate/hosted-mcp) lets Claude and other MCP clients create,
configure, and manage your agents through natural language.

## Guide

#### Default agent language

When you create a new agent, it's configured with:

* English as the primary language
* Flash v2 model for fast, English-only responses
* A default first message.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c533094b96146b19a31fd712a02a4b0b6d63790aa2168698e7dc682291c04e0b/assets/images/conversational-ai/language-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T230159Z&X-Amz-Expires=604800&X-Amz-Signature=2832039b136e4b7e4773f917fcbcea4046fcdeffefc334c97c3e82e279d09631&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Additional languages switch the agent to use the v2.5 Multilingual model. English will always use
the v2 model.

#### Add additional languages

#### Update via the dashboard

Navigate to your agent's configuration page and locate the **Agent** tab.

1. In the **Additional Languages** add an additional language (e.g. French)
2. Review the first message, which is automatically translated using a Large Language Model (LLM). Customize it as needed for each additional language to ensure accuracy and cultural relevance.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a5db1d23c7c1cc22b41f9093839cd76b078e6cbef69230714f8c0e58f3609b2f/assets/images/conversational-ai/language-selection.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T230159Z&X-Amz-Expires=604800&X-Amz-Signature=84453c81b3b56a2bce52ffb73ffc8600f42ced0d29b285b0e2ee484af7484550&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

To find great voices for each language curated by the ElevenLabs team, visit the [language top picks](https://elevenlabs.io/app/voice-library/collections).

#### Language-specific voice settings

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e1335d0fc8fe77691f00b928c9aeb5e050226a0d766dbab325ded52e97ed4399/assets/images/conversational-ai/language-voice.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T230159Z&X-Amz-Expires=604800&X-Amz-Signature=ccf61013d180272da5f12eaf4de3cb4114d8e40746aa6046bfefe954458ea74e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Voice library

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/975e3c0207d86c06d4d68db0ef600ec6a716596062eabfec395b0356265f3583/assets/images/conversational-ai/voice-library-language.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T230159Z&X-Amz-Expires=604800&X-Amz-Signature=6f5da909bfce055f0dd5162e3dc25de32ee98363d7e00a89f08d3a233440e315&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Enable language detection

Add the [language detection tool](/docs/eleven-agents/customization/tools/system-tools/language-detection) to your agent can automatically switch to the user's preferred language.

#### Starting a call

Now that the agent is configured to support additional languages, the widget will prompt the user for their preferred language before the conversation begins.

If using the SDK, the language can be set programmatically using conversation overrides. See the
[Overrides](/docs/eleven-agents/customization/personalization/overrides) guide for implementation details.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4252ccb78e8c03f864b3389ec641a296ec99b9e89ae7d7efe2de36ef6132a152/assets/images/conversational-ai/widget-language.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T230159Z&X-Amz-Expires=604800&X-Amz-Signature=801359247f9a8ff60b62fa30d228953b2e17034eabbb9ea2c779c2a5949bcbb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
