---
title: "Multimodal input"
source: https://elevenlabs.io/docs/eleven-agents/customization/multimodal-input.md
path: docs/eleven-agents/customization/multimodal-input
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Multimodal input

## Overview

Multimodal input settings control extra ways users can send information to the agent beyond speech. They live in the agent's **Advanced** tab, under **Multimodal input**.

#### [File input](#file-input)

Let users attach images and PDFs in chat

#### [DTMF input](#dtmf-input)

Collect keypad digits from callers during phone conversations

## File input

File input lets users send images and PDFs to the agent in chat. The agent can read those files when the selected [model](/docs/eleven-agents/customization/llm) supports image and/or document input.

Attachments are ignored if the model does not support the file type, even when file input is
enabled.

### Configuration

| Field                        | Type      | Default | Description                                                                                                                                                            |
| ---------------------------- | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                    | `boolean` | `true`  | When `true`, users may attach images or PDFs if the model supports that input type.                                                                                    |
| `max_files_in_memory`        | `integer` | `10`    | How many recently uploaded files are held in memory at once. Range: `1` to `10`. When the limit is reached, older files are replaced with a brief summary.             |
| `max_files_per_conversation` | `integer` | `10`    | Total files a user can upload in one conversation. Uploads are billed per file. Use `-1` for no limit. Must be `-1` or greater than or equal to `max_files_in_memory`. |

Users can attach files in the [widget](/docs/eleven-agents/customization/widget), supported chat channels such as [Slack](/docs/eleven-agents/customization/integrations/slack), or the [upload conversation file](/docs/eleven-agents/api-reference/conversations/upload-file) API.

#### Update via the dashboard

#### Open Multimodal input

Open your agent in the dashboard, confirm the selected model supports image and/or PDF input, then go to the **Advanced** tab.

#### Enable file attachments

Under **Multimodal input**, turn on **Allow file attachments**.

#### Set file limits

Optionally set **Files kept in memory** and **Max files per conversation**.

#### Save your changes

Save the agent. Users can then attach images and PDFs in chat.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Edit the agent configuration

Set `conversation_config.conversation.file_input`:

```json
{
  "conversation_config": {
    "conversation": {
      "file_input": {
        "enabled": true,
        "max_files_in_memory": 10,
        "max_files_per_conversation": 10
      }
    }
  }
}
```

#### Push the agent configuration

```bash
elevenlabs agents push --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Update via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "conversation": {
            "file_input": {
                "enabled": True,
                "max_files_in_memory": 10,
                "max_files_per_conversation": 10,
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
    conversation: {
      fileInput: {
        enabled: true,
        maxFilesInMemory: 10,
        maxFilesPerConversation: 10,
      },
    },
  },
});
```

## DTMF input

DTMF input lets callers enter digits on their phone keypad during a call. Use it to collect phone numbers, menu choices, and other numeric input without relying on speech recognition.

This is the inverse of the [play keypad touch tone](/docs/eleven-agents/customization/tools/system-tools/play-keypad-touch-tone) system tool, which sends tones from the agent.

Only out-of-band DTMF from
[Twilio](/docs/eleven-agents/phone-numbers/twilio-integration/native-integration), [SIP trunking](/docs/eleven-agents/phone-numbers/sip-trunking) (Telephony), or
[Genesys](/docs/eleven-agents/phone-numbers/c-caa-s-integrations/genesys) is supported. In-band
tones in the audio stream are ignored. The web widget and chat channels cannot send DTMF.

Each keypad press is buffered until the sequence is complete. Completing a sequence creates one user turn.

1. The caller presses a key. The first digit interrupts the agent if it is speaking.
2. Further digits append to the same buffer.
3. The sequence completes when the caller presses `#` (if hash termination is enabled) or when no further digits arrive before the timeout.
4. The agent receives the collected digits as a user turn and responds.

`#` is a terminator when hash termination is enabled; it is not included in the collected string. A `#` pressed with an empty buffer is ignored. The buffer accepts `0-9`, `*`, `#`, and `A-D`, up to 50 characters.

### Configuration

`conversation_config.conversation.dtmf_input_settings` is `null` when DTMF input is disabled. When enabled, the defaults are:

| Field                | Type      | Default | Description                                                                                                        |
| -------------------- | --------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `dtmf_input_timeout` | `float`   | `2.0`   | Seconds to wait after the last keypress before completing the sequence. Range: `0.5` to `10.0`.                    |
| `hash_terminator`    | `boolean` | `true`  | If `true`, `#` immediately completes the sequence and is not included in the collected digits.                     |
| `redact_input`       | `boolean` | `false` | If `true`, keypad entries are replaced with `<REDACTED>` in the stored transcript, conversation log, and analysis. |

Redaction applies to the keypad turn in stored conversation data. It does not hide digits from the agent during the live call, and it does not rewrite digits the agent speaks back or sends to a tool. That is separate from [conversation history redaction](/docs/eleven-agents/customization/privacy/conversation-history-redaction).

#### Update via the dashboard

#### Open Multimodal input

Open your agent in the dashboard and go to the **Advanced** tab.

#### Enable DTMF input

Under **Multimodal input**, turn on **Enable DTMF input**.

#### Configure timeout and redaction

Optionally set **DTMF input timeout**, **Use # to complete DTMF input**, and **Redact DTMF input**.

#### Save your changes

Save the agent, then place a phone call and enter digits on the keypad.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Edit the agent configuration

Set `conversation_config.conversation.dtmf_input_settings`. Omit the object, or set it to `null`, to disable DTMF input.

```json
{
  "conversation_config": {
    "conversation": {
      "dtmf_input_settings": {
        "dtmf_input_timeout": 2.0,
        "hash_terminator": true,
        "redact_input": false
      }
    }
  }
}
```

#### Push the agent configuration

```bash
elevenlabs agents push --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Update via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "conversation": {
            "dtmf_input_settings": {
                "dtmf_input_timeout": 2.0,
                "hash_terminator": True,
                "redact_input": False,
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
    conversation: {
      dtmfInputSettings: {
        dtmfInputTimeout: 2.0,
        hashTerminator: true,
        redactInput: false,
      },
    },
  },
});
```

Update the agent's [system prompt](/docs/eleven-agents/best-practices/prompting-guide) so it knows when to ask for keypad input. For example:

```text
If you need the caller's phone number, ask them to type it on their keypad. Wait for the DTMF
input before continuing.
```
