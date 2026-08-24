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
from elevenlabs import (
    ConversationalConfig,
    ElevenLabs,
    AgentConfig,
    PromptAgent,
    PromptAgentInputToolsItem_System
)

# Initialize the client
elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

# Create the skip turn tool
skip_turn_tool = PromptAgentInputToolsItem_System(
    name="skip_turn",
    description=""  # Optional: Customize when the tool should be triggered, or leave blank for default.
)

# Create the agent configuration
conversation_config = ConversationalConfig(
    agent=AgentConfig(
        prompt=PromptAgent(
            tools=[skip_turn_tool]
        )
    )
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

// Create the agent with skip turn tool
await elevenlabs.conversationalAi.agents.create({
  conversationConfig: {
    agent: {
      prompt: {
        tools: [
          {
            type: "system",
            name: "skip_turn",
            description: "", // Optional: Customize when the tool should be triggered, or leave blank for default.
          },
        ],
      },
    },
  },
});
```

## UI configuration

You can also configure the Skip Turn tool directly within the Agent's UI, in the tools section.

### Step 1: Add a new tool

Navigate to your agent's configuration page. In the "Tools" section, click on "Add tool", the `Skip Turn` option will already be available.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8b95051da94ada3dae7e42121148ad4509b49413e73bd16351142372ca26a68d/assets/images/conversational-ai/skip-turn-option.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T100018Z&X-Amz-Expires=604800&X-Amz-Signature=a2ecf7383d5013d67f030456f599cc0213aca21e489eb2c4f3a263120a31861b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Add Skip Turn Tool Option" />

### Step 2: Configure the tool

You can optionally provide a description to customize when the LLM should trigger this tool, or leave it blank to use the default behavior.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/cbb419db630beb4feefc390ef3f3576f7a6dc2df098faec4fbd2d1d5e703364f/assets/images/conversational-ai/skip-turn-config.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T100018Z&X-Amz-Expires=604800&X-Amz-Signature=355750d9a7c0561f8fe98a79d2a68d0f5ab157d69fd75a58771af749b89f7862&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Configure Skip Turn Tool" />

### Step 3: Enable the tool

Once configured, the `Skip Turn` tool will appear in your agent's list of enabled tools and the agent will be able to skip turns. .

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bdb738dc85ff91107cafa5899aad116420aabe9fe794b648bc1f0751729ba5af/assets/images/conversational-ai/skip-turn-enabled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T100018Z&X-Amz-Expires=604800&X-Amz-Signature=c3f0c99331cacfdff7ef92b3e980d08cea0d81832995ecc2b09c6c9180d6da2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Skip Turn Tool Enabled" />
