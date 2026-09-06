---
title: "Skip turn"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/skip-turn.md
path: docs/eleven-agents/customization/tools/system-tools/skip-turn
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Skip turn

## Overview

The **Skip Turn** tool allows your conversational agent to explicitly pause and wait for the user to speak or act before continuing. This system tool is useful when the user indicates they need a moment, for example, by saying "Give me a second," "Let me think," or "One moment please."

## Functionality

* **User-Initiated Pause**: The tool is designed to be invoked by the LLM when it detects that the user needs a brief pause without interruption.
* **No Verbal Response**: After this tool is called, the assistant will not speak. It waits for the user to re-engage or for another turn-taking condition to be met.
* **Seamless Conversation Flow**: It helps maintain a natural conversational rhythm by respecting the user's need for a short break without ending the interaction or the agent speaking unnecessarily.

**Purpose**: Allow the agent to pause and wait for user input without speaking.

**Trigger conditions**: The LLM should call this tool when:

* User indicates they need a moment ("Give me a second", "Let me think")
* User requests pause in conversation flow
* Agent detects user needs time to process information

**Parameters**:

* `reason` (string, optional): Free-form reason explaining why the pause is needed

**Function call format**:

```json
{
  "type": "function",
  "function": {
    "name": "skip_turn",
    "arguments": "{\"reason\": \"User requested time to think\"}"
  }
}
```

**Implementation**: No additional configuration needed. The tool simply signals the agent to remain silent until the user speaks again.

### API implementation

When creating an agent via API, you can add the Skip Turn tool to your agent configuration. It should be defined as a system tool, with the name `skip_turn`.

```python
from elevenlabs import AgentConfig, ConversationalConfig, ElevenLabs

elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

response = elevenlabs.conversational_ai.agents.create(
    conversation_config=ConversationalConfig(
        agent=AgentConfig(
            prompt={
                "built_in_tools": {
                    "skip_turn": {
                        "type": "system",
                        "name": "skip_turn",
                        # Optional: customize when the tool should be triggered,
                        # or leave blank for the default.
                        "description": "",
                        "params": {"system_tool_type": "skip_turn"},
                    }
                }
            },
        ),
    ),
)
```

```javascript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient({
  apiKey: "YOUR_API_KEY",
});

await elevenlabs.conversationalAi.agents.create({
  conversationConfig: {
    agent: {
      prompt: {
        builtInTools: {
          skipTurn: {
            type: "system",
            name: "skip_turn",
            description: "", // Optional: Customize when the tool should be triggered, or leave blank for default.
            params: { systemToolType: "skip_turn" },
          },
        },
      },
    },
  },
});
```

## UI configuration

You can also configure the Skip Turn tool directly within the Agent's UI, in the tools section.

### Step 1: Add a new tool

Navigate to your agent's configuration page. In the "Tools" section, click on "Add tool", the `Skip Turn` option will already be available.

![Add Skip Turn Tool Option](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8b95051da94ada3dae7e42121148ad4509b49413e73bd16351142372ca26a68d/assets/images/conversational-ai/skip-turn-option.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T200344Z&X-Amz-Expires=604800&X-Amz-Signature=2270680675cbd8144be3f5531a06fe7e5aca02deea883a5e20449960632d884d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Step 2: Configure the tool

You can optionally provide a description to customize when the LLM should trigger this tool, or leave it blank to use the default behavior.

![Configure Skip Turn Tool](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/cbb419db630beb4feefc390ef3f3576f7a6dc2df098faec4fbd2d1d5e703364f/assets/images/conversational-ai/skip-turn-config.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T200344Z&X-Amz-Expires=604800&X-Amz-Signature=e7111b169226b242de42c94204d72b976dc6bb911dccd92117fe20411f7d0ff8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Step 3: Enable the tool

Once configured, the `Skip Turn` tool will appear in your agent's list of enabled tools and the agent will be able to skip turns. .

![Skip Turn Tool Enabled](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bdb738dc85ff91107cafa5899aad116420aabe9fe794b648bc1f0751729ba5af/assets/images/conversational-ai/skip-turn-enabled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T200344Z&X-Amz-Expires=604800&X-Amz-Signature=e7bc7dec1e80239dcf36bcba7dfe2d80ada2aa4ca2bfe3017cf19eef40a7d774&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
