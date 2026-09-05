---
title: "Conversation flow"
source: https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow.md
path: docs/eleven-agents/customization/conversation-flow
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Conversation flow

## Overview

Conversation flow settings determine how your assistant handles periods of user silence, interruptions during speech, and turn-taking behavior. These settings help create more natural conversations and can be customized based on your use case.

#### [Maximum conversation duration](#maximum-conversation-duration)

Limit the total duration of each conversation

#### [Take turn after silence](#turn-timeout)

Configure how long your assistant waits during periods of silence

#### [Soft timeout](#soft-timeout)

Provide natural audio feedback when your agent needs time to think

#### [Interruptions](#interruptions)

Control whether users can interrupt your assistant while speaking

#### [Turn eagerness](#turn-eagerness)

Adjust how quickly your assistant responds to user input

## Maximum conversation duration

The **Max conversation duration** setting limits the total time a conversation can remain active.
This global limit starts when the conversation begins and applies independently of turn-level
timeouts. The default is 600 seconds (10 minutes). You can set a value from 60 to 7,200 seconds.

### Configuration

In the CLI and API, configure this setting with the
`conversation_config.conversation.max_duration_seconds` field.

#### Update via the dashboard

Open your agent in the dashboard, navigate to the **Advanced** tab, and adjust **Max conversation
duration** under **Call limits**. Save your changes.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Edit the agent configuration

Set `conversation_config.conversation.max_duration_seconds`:

```json
{
  "conversation_config": {
    "conversation": {
      "max_duration_seconds": 1200
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
        "conversation": {"max_duration_seconds": 1200},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    conversation: { maxDurationSeconds: 1200 },
  },
});
```

WhatsApp message conversations have a default 15-minute inactivity timeout, measured from the
agent's most recent response. This timeout can end a message conversation before the configured
maximum duration. Enterprise customers whose use case requires a different timeout should [contact support](https://help.elevenlabs.io/hc/en-us/requests/new).

## Take turn after silence

The **Take turn after silence** setting determines how long your assistant waits during periods of user silence before taking the next turn and prompting for a response.

### Configuration

The value is specified in seconds and must be between 1 and 30 seconds. In the CLI and API, configure this setting with the `conversation_config.turn.turn_timeout` field.

#### Update via the dashboard

Open your agent in the dashboard, navigate to the **Advanced** tab, and adjust the **Take turn after silence** value. Save your changes.

![Take turn after silence setting](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9de7653a0940ae3441b3470c2af53f4a72294ad3680946d4c3fa3b91df69c566/assets/images/conversational-ai/timeouts.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T070756Z&X-Amz-Expires=604800&X-Amz-Signature=4db59b81de691c30cb770c96b0f22b337cd75cb17bafcde874aaff82bd04b8db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `conversation_config.turn.turn_timeout`:

```json
{
  "conversation_config": {
    "turn": {
      "turn_timeout": 7
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
        "turn": {"turn_timeout": 7},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    turn: { turnTimeout: 7 },
  },
});
```

Choose an appropriate timeout duration based on your use case. Shorter timeouts create more
responsive conversations but may interrupt users who need more time to respond, leading to a less
natural conversation.

### Best practices

* Set shorter timeouts (5-10 seconds) for casual conversations where quick back-and-forth is expected
* Use longer timeouts (10-30 seconds) when users may need more time to think or formulate complex responses
* Consider your user context - customer service may benefit from shorter timeouts while technical support may need longer ones

## Soft timeout

Soft timeout provides immediate audio feedback when the LLM takes longer than expected to generate a response. Instead of awkward silence while waiting, your agent speaks a brief filler phrase like "Hmm..." or "Let me think..." to maintain natural conversational flow.

This feature is useful for:

* Complex queries requiring longer LLM processing
* Handling variable latency from LLM providers
* Creating more human-like conversations with natural thinking pauses

### How it works

1. When the user finishes speaking, the system starts generating an LLM response
2. A timer begins based on the configured timeout duration
3. If the LLM response arrives **before** the timeout, no filler is spoken
4. If the timeout is reached **before** the LLM responds:
   * The configured filler message is spoken immediately
   * The agent continues waiting for the actual response
   * Once ready, the agent speaks the full LLM response

Soft timeout triggers only once per turn to prevent multiple fillers in succession.

### Configuration

#### Update via the dashboard

Open your agent in the dashboard, navigate to the **Advanced** tab, and adjust the **Soft timeout** settings. Save your changes.

![Soft timeout settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7fdaca49ad50e6bc1f09f5eac46e36f0f4b071c5477e061a62791df9e100be75/assets/images/conversational-ai/soft-timeout.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T070756Z&X-Amz-Expires=604800&X-Amz-Signature=8bd413064a046aa7cae052c7e9f894d2fc32432e6d8ba1fb1781d76162306a82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `conversation_config.turn.soft_timeout_config`:

```json
{
  "conversation_config": {
    "turn": {
      "soft_timeout_config": {
        "timeout_seconds": 3.0,
        "message": "Hhmmmm...yeah.",
        "use_llm_generated_message": false
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
        "turn": {
            "soft_timeout_config": {
                "timeout_seconds": 3.0,
                "message": "Hhmmmm...yeah.",
                "use_llm_generated_message": False,
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
    turn: {
      softTimeoutConfig: {
        timeoutSeconds: 3.0,
        message: "Hhmmmm...yeah.",
        useLlmGeneratedMessage: false,
      },
    },
  },
});
```

#### Timeout duration

The time in seconds before the filler message is spoken while waiting for the LLM response.

| Setting         | Description            |
| --------------- | ---------------------- |
| **Default**     | `-1` (disabled)        |
| **Range**       | `0.5` to `8.0` seconds |
| **Recommended** | `3.0` seconds          |

Start with 3.0 seconds—long enough to avoid unnecessary fillers on fast responses, short enough to
prevent awkward silences.

#### Static message

A predefined filler phrase spoken when soft timeout triggers.

| Setting     | Description        |
| ----------- | ------------------ |
| **Default** | `"Hhmmmm...yeah."` |
| **Length**  | 1–200 characters   |

This message supports:

* **Language overrides**: Auto-translates to additional languages configured for your agent
* **Client overrides**: Can be customized per-call via the SDK

#### LLM-generated message

When enabled, generates a contextually-appropriate filler phrase dynamically using a lightweight LLM, instead of the static message.

| Setting      | Description                             |
| ------------ | --------------------------------------- |
| **Default**  | `false`                                 |
| **Fallback** | Uses static message if generation fails |

The system uses recent conversation context (up to 4 messages, 1000 characters) to generate relevant fillers like "Hmm...", "I see...", "Understood...", "Got it...", or "Alright..."

A static fallback message is still required when using LLM-generated messages.

### Best practices

* Avoid time indicators in filler messages (e.g., "One second...") as actual response times are unpredictable
* Disable soft timeout for quick FAQ bots where responses are consistently fast

## Interruptions

Interruption handling determines whether users can interrupt your assistant while it's speaking.

### Configuration

Interruption settings can be configured in the agent's **Advanced** tab under **Client Events**.

To enable interruptions, make sure interruption is a selected client event.

#### Interruptions enabled

![Interruption allowed](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1da794be8ea3bfed45d06241ce5db390480cd45d27c0f886943518bd52d76157/assets/images/conversational-ai/interruptions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T070756Z&X-Amz-Expires=604800&X-Amz-Signature=6d20da49a587efa90ead3d708e54c3b37f4b1101cc15858ca5be1366fdbeb58e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Interruptions disabled

![Interruption ignored](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/847a2ebcdfff9498501502ab4b568fc498b6995f860a5552177a7883942197ff/assets/images/conversational-ai/no-interruption.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T070756Z&X-Amz-Expires=604800&X-Amz-Signature=e4c80efe9b46c6dd2b39746270178c083295ffdccdb09a0c553d287d74c7e59f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Disable interruptions when the complete delivery of information is crucial, such as legal
disclaimers or safety instructions.

### Best practices for interruptions

* Enable interruptions for natural conversational flows where back-and-forth dialogue is expected
* Disable interruptions when message completion is critical (e.g., terms and conditions, safety information)
* Consider your use case context - customer service may benefit from interruptions while information delivery may not

## Turn eagerness

Turn eagerness controls how quickly your assistant responds to user input during conversation. This setting determines how eager the assistant is to take turns and start speaking based on detected speech patterns.

### How it works

The assistant now includes two key improvements for more natural turn-taking:

1. **Faster response generation** - The assistant starts speaking after receiving enough words and a comma from the language model, rather than waiting for complete sentences. This reduces latency and creates more responsive conversations, especially when the assistant has longer responses.

2. **Configurable turn eagerness** - Control how quickly the assistant interprets pauses or speech patterns as opportunities to respond.

### Configuration

Three modes are available:

* **Eager** - The assistant responds quickly to user input, jumping in at the earliest opportunity. Best for fast-paced conversations where immediate responses are valued.
* **Normal** - Balanced turn-taking that works well for most conversational scenarios. The assistant waits for natural conversation breaks before responding.
* **Patient** - The assistant waits longer before taking its turn, giving users more time to complete their thoughts. Ideal for collecting detailed information or when users need time to formulate responses.

#### Update via the dashboard

Open your agent in the dashboard, navigate to the **Agent** settings, and select the desired turn eagerness mode. Save your changes.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `conversation_config.turn.turn_eagerness` to one of `"patient"`, `"normal"`, or `"eager"`:

```json
{
  "conversation_config": {
    "turn": {
      "turn_eagerness": "normal"
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
        "turn": {"turn_eagerness": "normal"},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    turn: { turnEagerness: "normal" },
  },
});
```

Turn eagerness is especially powerful when combined with workflows. You can dynamically adjust the
assistant's responsiveness based on context—making it jump in faster during casual conversation,
or wait longer when collecting sensitive information like phone numbers or email addresses.

### Best practices for turn eagerness

* Use **Eager** mode for customer service scenarios where quick responses improve user experience
* Use **Patient** mode when collecting structured information like phone numbers, addresses, or email addresses
* Use **Normal** mode as a default for general conversational flows
* Combine with workflows to dynamically adjust turn eagerness based on conversation context
* Test different settings with your specific use case to find the optimal balance

## Recommended configurations

#### Customer service

* Shorter timeouts (5-10 seconds) for responsive interactions - Enable interruptions to allow
  customers to interject with questions - **Eager** turn eagerness for quick, responsive
  conversations

#### Information collection

* Moderate timeouts (10-15 seconds) to allow users time to gather information - Enable
  interruptions for natural conversation flow - **Patient** turn eagerness when collecting phone
  numbers, addresses, or email addresses

#### Legal disclaimers

* Longer timeouts (15-30 seconds) to allow for complex responses - Disable interruptions to
  ensure full delivery of legal information - **Normal** turn eagerness to maintain steady pacing

#### Conversational EdTech

* Longer timeouts (10-30 seconds) to allow time to think and formulate responses - Enable
  interruptions to allow students to interject with questions - **Patient** turn eagerness to give
  students adequate time to respond
