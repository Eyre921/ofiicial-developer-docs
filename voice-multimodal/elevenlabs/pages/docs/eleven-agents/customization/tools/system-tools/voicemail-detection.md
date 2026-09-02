---
title: "Voicemail detection"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/voicemail-detection.md
path: docs/eleven-agents/customization/tools/system-tools/voicemail-detection
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voicemail detection

## Overview

The **Voicemail Detection** tool allows your ElevenLabs agent to automatically identify when a call has been answered by a voicemail system rather than a human. This system tool enables agents to handle automated voicemail scenarios gracefully by either leaving a pre-configured message or ending the call immediately.

## Functionality

* **Automatic Detection**: The LLM analyzes conversation patterns to identify voicemail systems based on automated greetings and prompts
* **Configurable Response**: Choose to either leave a custom voicemail message or end the call immediately when voicemail is detected
* **Call Termination**: After detection and optional message delivery, the call is automatically terminated
* **Status Tracking**: Voicemail detection events are logged and can be viewed in conversation history and batch call results

**Parameters**:

* `reason` (string, required): The reason for detecting voicemail (e.g., "automated greeting detected", "no human response")

**Function call format**:

```json
{
  "type": "function",
  "function": {
    "name": "voicemail_detection",
    "arguments": "{\"reason\": \"Automated greeting detected with request to leave message\"}"
  }
}
```

## Configuration Options

The voicemail detection tool can be configured with the following options:

![Voicemail detection configuration
interface](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f2f9a87e27ce0d5f631d2d294163e8df39e6dee5b3a98aaba692589c66364550/assets/images/conversational-ai/voicemail_detection.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T233208Z&X-Amz-Expires=604800&X-Amz-Signature=f8320c00b1fc5e397ded2c2247017a50b5c6b47e799cc4c4e45e65fa0a1dd124&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

* **Voicemail Message**: You can configure an optional custom message to be played when voicemail is detected. This message supports [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables), allowing you to personalize voicemail messages with runtime values such as `{{user_name}}` or `{{appointment_time}}`

## API Implementation

When creating an agent via API, you can add the Voicemail Detection tool to your agent configuration. It should be defined as a system tool:

```python
from elevenlabs import AgentConfig, ConversationalConfig, ElevenLabs

elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

response = elevenlabs.conversational_ai.agents.create(
    conversation_config=ConversationalConfig(
        agent=AgentConfig(
            prompt={
                "built_in_tools": {
                    "voicemail_detection": {
                        "type": "system",
                        "name": "voicemail_detection",
                        # Optional: customize when the tool should be triggered
                        "description": "",
                        "params": {
                            "system_tool_type": "voicemail_detection",
                            # Optional: message left when voicemail is detected
                            "voicemail_message": "Sorry I missed you. I'll call back later.",
                        },
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
          voicemailDetection: {
            type: "system",
            name: "voicemail_detection",
            description: "", // Optional: Customize when the tool should be triggered
            params: {
              systemToolType: "voicemail_detection",
              // Optional: message left when voicemail is detected
              voicemailMessage: "Sorry I missed you. I'll call back later.",
            },
          },
        },
      },
    },
  },
});
```
