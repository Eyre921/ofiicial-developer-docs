---
title: "Dynamic variables"
source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables.md
path: docs/eleven-agents/customization/personalization/dynamic-variables
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dynamic variables

**Dynamic variables** allow you to inject runtime values into your agent's messages, system prompts, and tools. This enables you to personalize each conversation with user-specific data without creating multiple agents.

## Overview

Dynamic variables can be integrated into multiple aspects of your agent:

* **System prompts** to customize behavior and context
* **First messages** to personalize greetings
* **Tool parameters and headers** to pass user-specific data

Here are a few examples where dynamic variables are useful:

* **Personalizing greetings** with user names
* **Including account details** in responses
* **Passing data** to tool calls
* **Customizing behavior** based on subscription tiers
* **Accessing system information** like conversation ID or call duration

Dynamic variables support three value types:

#### String

Text values

#### Number

Numeric values

#### Boolean

True/false values

## System dynamic variables

Your agent has access to built-in `system__*` variables in every conversation without runtime configuration. These variables are prefixed with the reserved `system__` namespace and update automatically as the conversation progresses. Custom dynamic variables cannot use the `system__` prefix or override system variables.

Variables marked with † change between turns. Placing them in prompt text can prevent prompt caching; see [Best practices](#best-practices) for alternatives.

### Agent and conversation identity

| Variable                   | Type             | Description                                                                                                                               | Example                                |
| -------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `system__agent_id`         | `string`         | Unique identifier of the agent that started the conversation. Never changes during a conversation.                                        | `"agent_8401kp8bt0jdf14rzzcv5veq94yg"` |
| `system__current_agent_id` | `string`         | Unique identifier of the currently active agent. Updates when the conversation transfers to another agent.                                | `"agent_8401kp8bt0jdf14rzzcv5veq94yg"` |
| `system__conversation_id`  | `string`         | ElevenLabs unique conversation identifier.                                                                                                | `"conv_1801kp8qtb2begztn7zyf446v4jk"`  |
| `system__user_id`          | `string \| null` | Client-provided user ID for tracking and analytics. Must not be trusted for authentication.                                               | `"G6yhJW8MktQdhUquvXD1iKpPHql2"`       |
| `system__initiator_id`     | `string \| null` | Identifier corresponding to the authentication method used to initiate the conversation.                                                  | `"user_1801kp8qtb2begztn7zyf446v4jk"`  |
| `system__channel`          | `string`         | Channel source through which the conversation was initiated.                                                                              | `"slack_integration"`                  |
| `system__is_text_only`     | `boolean`        | `true` when the conversation is running in text-only (chat) mode; `false` for voice calls.                                                | `true`                                 |
| `system__environment`      | `string`         | Environment the conversation is running in, used to resolve [environment variables](/docs/eleven-agents/integrate/environment-variables). | `"production"`                         |

### Time and timezone

| Variable                | Type             | Description                                                                                                                     | Example                              |
| ----------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `system__timezone`      | `string \| null` | Configured timezone (`conversation_config.agent.prompt.timezone`) or caller-provided IANA timezone. Defaults to UTC when unset. | `"America/New_York"`                 |
| `system__time` †        | `string`         | Current date and time in the configured timezone (`%A, %H:%M %d %B %Y`). Re-evaluated on every turn (changes once per minute).  | `"Friday, 12:33 12 December 2025"`   |
| `system__time_utc` †    | `string`         | Current UTC timestamp in ISO 8601 format. Re-evaluated on every turn.                                                           | `"2025-12-12T12:33:45.123456+00:00"` |
| `system__time_date`     | `string`         | Current date in the configured timezone (or UTC if none is set) (`%A, %d %B %Y`). Changes once per day.                         | `"Friday, 12 December 2025"`         |
| `system__time_hour`     | `integer`        | Current hour (`0`–`23`) in the configured timezone (or UTC if none is set). Changes at most once per hour.                      | `12`                                 |
| `system__time_minute` † | `integer`        | Current minute (`0`–`59`) in the configured timezone (or UTC if none is set). Changes once per minute.                          | `33`                                 |
| `system__time_second` † | `integer`        | Current second (`0`–`59`) in the configured timezone (or UTC if none is set). Changes on every turn.                            | `45`                                 |

### Telephony and messaging

These variables are populated when applicable for telephony and messaging channels:

| Variable                | Type             | Description                                                | Example                                  |
| ----------------------- | ---------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `system__caller_id`     | `string \| null` | Caller's phone number (voice/SMS/WhatsApp/Amazon Connect). | `"+14155552671"`                         |
| `system__called_number` | `string \| null` | Destination phone number called.                           | `"+18005551234"`                         |
| `system__call_sid`      | `string \| null` | Twilio Call SID (Twilio calls only).                       | `"CA3498076234a8bbf65c8f09fb8ad7ac1b"`   |
| `system__call_id`       | `string \| null` | SIP Call-ID (SIP trunk calls only).                        | `"757f72cf-e80f-44f7-87d6-a961ffbf5b3d"` |

### Per-turn conversation state

| Variable                           | Type      | Description                                                                                                                                                                            | Example                |
| ---------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `system__call_duration_secs` †     | `integer` | Elapsed conversation time in seconds. Re-evaluated on every turn.                                                                                                                      | `142`                  |
| `system__agent_turns` †            | `integer` | Total number of agent turns in the conversation so far. Increments on every turn.                                                                                                      | `5`                    |
| `system__current_agent_turns` †    | `integer` | Number of agent turns for the current agent; resets to `0` after an agent transfer.                                                                                                    | `3`                    |
| `system__current_subagent_turns` † | `integer` | Number of agent turns in the current workflow node; resets to `0` on node transition.                                                                                                  | `2`                    |
| `system__conversation_history` †   | `string`  | JSON-serialized conversation transcript up to the current turn (`{"entries": [{"role": "user", "message": "..."}]}`). See [Conversation history format](#conversation-history-format). | `'{"entries": [...]}'` |

### Conversation history format

The `system__conversation_history` variable contains a JSON object with the following structure:

```json
{
  "x-elevenlabs-history": true,
  "entries": [
    { "role": "user", "message": "Hello" },
    { "role": "agent", "message": "Hi, how can I help?" },
    {
      "role": "agent",
      "tool_requests": [{ "tool_name": "lookup_order", "params_as_json": { "order_id": "123" } }]
    },
    {
      "role": "tool",
      "tool_results": [{ "tool_name": "lookup_order", "result_value": "{\"status\": \"shipped\"}" }]
    }
  ]
}
```

Each entry includes a `role` (`"user"`, `"agent"`, or `"tool"`) and one of:

* `message`: The text content of the turn
* `tool_requests`: An array of tool calls made by the agent, with resolved parameter values
* `tool_results`: An array of tool responses

If a tool result or parameter contains a nested conversation history, it is redacted to a placeholder (such as `[conversation_history (5 turns)]`) to avoid unbounded recursive expansion.

This variable is useful for passing conversation context to tools (such as webhooks or custom LLMs) or for including conversation history in sub-agent prompts during handoffs.

## Secret dynamic variables

Secret dynamic variables are populated in the same way as normal dynamic variables, but indicate to ElevenAgents that they should only be used in dynamic variable headers and never sent to an LLM provider as part of an agent's system prompt or first message.

Use secret dynamic variables for auth tokens or private IDs that should not be sent to an LLM. To create a secret dynamic variable, prefix the dynamic variable with `secret__`.

> **Warning**
>
> Secret values are stored redacted, so the conversations API returns them as `<REDACTED>`.
> Post-call transcription webhooks deliver the original values, so make sure your webhook endpoint
> handles them as secrets. Don't use the `secret__` prefix for values you need to read back from the
> conversations API. Pass those as regular dynamic variables, or pass a non-sensitive identifier and
> look up the sensitive value on your own system.

## Updating dynamic variables from tools

[Tool calls](/docs/eleven-agents/customization/tools) can create or update dynamic variables if they return a valid JSON object. To specify what should be extracted, set the object paths using dot notation. If the field or path doesn't exist, nothing is updated.

Example of a response object and dot notation:

* Status corresponds to the path: `response.status`
* The first user's email in the users array corresponds to the path: `response.users.0.email`

**`JSON`**

```JSON title="JSON"
{
  "response": {
    "status": 200,
    "message": "Successfully found 5 users",
    "users": [
      "user_1": {
        "user_name": "test_user_1",
        "email": "test_user_1@email.com"
      }
    ]
  }
}
```

To update a dynamic variable to be the first user's email, set the assignment like so.

![Query parameters](/docs/_fern-img/95ff0cae8613eafa8bc4312e7cafa39ac0eab34d2fd2b21f0894a30775366110.webp)

Assignments are configured on each webhook tool; see [tool assignments](/docs/eleven-agents/api-reference/tools/create#response.body.tool_config.SystemToolConfig.assignments) in the API reference.

## Guide

Prerequisites:

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenAgents agent (follow the [quickstart](/docs/eleven-agents/quickstart) to create one)

#### Define dynamic variables in prompts

Add variables using double curly braces `{{variable_name}}` in your:

* System prompts
* First messages
* Tool parameters

![Dynamic variables in messages](/docs/_fern-img/84a9870018a436215fe8d6563a47f42b1b45e005c56dffff3b37dbfe8a25adf3.webp)

![Dynamic variables in messages](/docs/_fern-img/052ab733ff3ecb2512218c70d82a4337764577b0082cdc4b2fb4415d273d2cbe.webp)

#### Define dynamic variables in tools

You can also define dynamic variables in the tool configuration.
To create a new dynamic variable, set the value type to Dynamic variable and click the `+` button.

![Setting placeholders](/docs/_fern-img/7da35479f409f1505dc528e78d782d74e226fa51b2a5d3b6ede3929359be8ddd.webp)

![Setting placeholders](/docs/_fern-img/21856929c95fe77b274dc1a849668c144554719cd468a225d110295ae94c7713.webp)

#### Set placeholders

Configure default values for testing without passing variables at runtime.

#### Update via the dashboard

Set default values for each dynamic variable in the agent's dashboard.

![Setting placeholders](/docs/_fern-img/dbea803919e315240202a3cb355ef7f62f25a5182d9aa99d0916177349c70ae4.webp)

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent_configs/\<agent-name>.json\`

Set `conversation_config.agent.dynamic_variables.dynamic_variable_placeholders`. Each key is the variable name; the value is the placeholder used during testing:

```json
{
  "conversation_config": {
    "agent": {
      "dynamic_variables": {
        "dynamic_variable_placeholders": {
          "user_name": "Angelo",
          "account_type": "premium"
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
        "agent": {
            "dynamic_variables": {
                "dynamic_variable_placeholders": {
                    "user_name": "Angelo",
                    "account_type": "premium",
                }
            }
        },
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    agent: {
      dynamicVariables: {
        dynamicVariablePlaceholders: {
          user_name: "Angelo",
          account_type: "premium",
        },
      },
    },
  },
});
```

#### Pass variables at runtime

When starting a conversation, provide the dynamic variables in your code:

> **Tip**
>
> Ensure you have the latest [SDK](/docs/eleven-agents/libraries/python) installed.

**`Python`**

```python title="Python" focus={10-23} maxLines=25
import os
import signal
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(api_key=api_key)

dynamic_vars = {
    "user_name": "Angelo",
}

config = ConversationInitiationData(
    dynamic_variables=dynamic_vars
)

conversation = Conversation(
    elevenlabs,
    agent_id,
    config=config,
    # Assume auth is required when API_KEY is set.
    requires_auth=bool(api_key),
    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),
    # Callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),
    # Uncomment the below if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
)

conversation.start_session()

signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())
```

**`JavaScript`**

```javascript title="JavaScript" focus={7-20} maxLines=25
import { Conversation } from '@elevenlabs/client';

class VoiceAgent {
  ...

  async startConversation() {
    try {
        // Request microphone access
        await navigator.mediaDevices.getUserMedia({ audio: true });

        this.conversation = await Conversation.startSession({
            agentId: 'agent_7101k5zvyjhmfg983brhmhkd98n6',

            dynamicVariables: {
                user_name: 'Angelo'
            },

            ... add some callbacks here
        });
    } catch (error) {
        console.error('Failed to start conversation:', error);
        alert('Failed to start conversation. Please ensure microphone access is granted.');
    }
  }
}
```

**`Swift`**

```swift title="Swift"
let dynamicVars: [String: DynamicVariableValue] = [
  "customer_name": .string("John Doe"),
  "account_balance": .number(5000.50),
  "user_id": .int(12345),
  "is_premium": .boolean(true)
]

// Create session config with dynamic variables
let config = SessionConfig(
    agentId: "agent_7101k5zvyjhmfg983brhmhkd98n6",
    dynamicVariables: dynamicVars
)

// Start the conversation
let conversation = try await Conversation.startSession(
    config: config
)
```

**`Widget`**

```html title="Widget"
<elevenlabs-convai
  agent-id="agent_7101k5zvyjhmfg983brhmhkd98n6"
  dynamic-variables='{"user_name": "John", "account_type": "premium"}'
></elevenlabs-convai>
```

## Public talk-to page integration

The public talk-to page supports dynamic variables through URL parameters, enabling you to personalize conversations when sharing agent links. This is particularly useful for embedding personalized agents in websites, emails, or marketing campaigns.

### URL parameter methods

There are two methods to pass dynamic variables to the public talk-to page:

#### Method 1: Base64-encoded JSON

Pass variables as a base64-encoded JSON object using the `vars` parameter:

```
https://elevenlabs.io/app/talk-to?agent_id=agent_7101k5zvyjhmfg983brhmhkd98n6&vars=eyJ1c2VyX25hbWUiOiJKb2huIiwiYWNjb3VudF90eXBlIjoicHJlbWl1bSJ9
```

The `vars` parameter contains base64-encoded JSON:

```json
{ "user_name": "John", "account_type": "premium" }
```

#### Method 2: Individual query parameters

Pass variables using `var_` prefixed query parameters:

```
https://elevenlabs.io/app/talk-to?agent_id=agent_7101k5zvyjhmfg983brhmhkd98n6&var_user_name=John&var_account_type=premium
```

### Parameter precedence

When both methods are used simultaneously, individual `var_` parameters take precedence over the base64-encoded variables to prevent conflicts:

```
https://elevenlabs.io/app/talk-to?agent_id=agent_7101k5zvyjhmfg983brhmhkd98n6&vars=eyJ1c2VyX25hbWUiOiJKYW5lIn0=&var_user_name=John
```

In this example, `user_name` will be `"John"` (from `var_user_name`) instead of `"Jane"` (from the base64-encoded `vars`).

### Implementation examples

#### JavaScript URL generation

```javascript
// Method 1: Base64-encoded JSON
function generateTalkToURL(agentId, variables) {
  const baseURL = 'https://elevenlabs.io/app/talk-to';
  const encodedVars = btoa(JSON.stringify(variables));
  return `${baseURL}?agent_id=${agentId}&vars=${encodedVars}`;
}

// Method 2: Individual parameters
function generateTalkToURLWithParams(agentId, variables) {
  const baseURL = 'https://elevenlabs.io/app/talk-to';
  const params = new URLSearchParams({ agent_id: agentId });

  Object.entries(variables).forEach(([key, value]) => {
    params.append(`var_${key}`, encodeURIComponent(value));
  });

  return `${baseURL}?${params.toString()}`;
}

// Usage
const variables = {
  user_name: "John Doe",
  account_type: "premium",
  session_id: "sess_123"
};

const urlMethod1 = generateTalkToURL("agent_7101k5zvyjhmfg983brhmhkd98n6", variables);
const urlMethod2 = generateTalkToURLWithParams("agent_7101k5zvyjhmfg983brhmhkd98n6", variables);
```

#### Python URL generation

```python
import base64
import json
from urllib.parse import urlencode, quote

def generate_talk_to_url(agent_id, variables):
    """Generate URL with base64-encoded variables"""
    base_url = "https://elevenlabs.io/app/talk-to"
    encoded_vars = base64.b64encode(json.dumps(variables).encode()).decode()
    return f"{base_url}?agent_id={agent_id}&vars={encoded_vars}"

def generate_talk_to_url_with_params(agent_id, variables):
    """Generate URL with individual var_ parameters"""
    base_url = "https://elevenlabs.io/app/talk-to"
    params = {"agent_id": agent_id}

    for key, value in variables.items():
        params[f"var_{key}"] = value

    return f"{base_url}?{urlencode(params)}"

# Usage
variables = {
    "user_name": "John Doe",
    "account_type": "premium",
    "session_id": "sess_123"
}

url_method1 = generate_talk_to_url("agent_7101k5zvyjhmfg983brhmhkd98n6", variables)
url_method2 = generate_talk_to_url_with_params("agent_7101k5zvyjhmfg983brhmhkd98n6", variables)
```

#### Manual URL construction

```
# Base64-encoded method
1. Create JSON: {"user_name": "John", "account_type": "premium"}
2. Encode to base64: eyJ1c2VyX25hbWUiOiJKb2huIiwiYWNjb3VudF90eXBlIjoicHJlbWl1bSJ9
3. Add to URL: https://elevenlabs.io/app/talk-to?agent_id=agent_7101k5zvyjhmfg983brhmhkd98n6&vars=eyJ1c2VyX25hbWUiOiJKb2huIiwiYWNjb3VudF90eXBlIjoicHJlbWl1bSJ9

# Individual parameters method
1. Add each variable with var_ prefix
2. URL encode values if needed
3. Final URL: https://elevenlabs.io/app/talk-to?agent_id=agent_7101k5zvyjhmfg983brhmhkd98n6&var_user_name=John&var_account_type=premium
```

## Best practices

#### Set a timezone instead of placing the current time in prompts

Variables in the system prompt, [workflow](/docs/eleven-agents/customization/agent-workflows) nodes, and [procedures](/docs/eleven-agents/customization/procedures) are resolved on every turn. If a value changes between turns, the prompt can't be cached, which increases cost and latency. `{{system__time_utc}}` and `{{system__time_second}}` change every turn; `{{system__time}}` and `{{system__time_minute}}` change every minute.

To give the agent the current date and time, set a timezone with the timezone button in the System Prompt editor (`conversation_config.agent.prompt.timezone`) instead of placing `{{system__time}}` or `{{system__time_utc}}` in prompt text. When a timezone is set, the platform adds the current date and time outside the cached prompt prefix, so your system prompt stays cached across turns. Without a timezone, the agent doesn't receive the current date and time.

If your prompt needs the date or hour inline, combine `{{system__time_date}}`, `{{system__time_hour}}`, and `{{system__timezone}}` (for example, `Today is {{system__time_date}}, hour {{system__time_hour}} ({{system__timezone}})`). These change at most once per hour.

#### Bind live state variables to tool parameters and headers

If a tool needs a value marked †, bind it to the tool parameter or header instead of placing it in the prompt. Tool parameters resolve only when the tool is called, so they don't affect prompt caching. The LLM already sees the conversation, so `{{system__conversation_history}}` is rarely needed in prompts.

#### Consider alternatives to turn counters in prompts

If your prompt checks turn counters such as `{{system__agent_turns}}`, consider these alternatives. Use `first_message` for static opening greetings or disclosures.

For first-reply behavior, you can phrase the instruction around the conversation history (for example, *"On your first reply, when you have not yet greeted the caller..."*). This relies on the LLM following the instruction, so test it with your model and keep the turn counter if results are less reliable.

If the counter only decides when to branch or escalate, a [workflow edge expression condition](/docs/eleven-agents/customization/agent-workflows#edges-and-flow-control) or a structured procedure [If step expression](/docs/eleven-agents/customization/procedures/structured-procedures#if-else-if-and-else) (such as `system__agent_turns >= 5`) can handle it outside the prompt. This doesn't cover cases where the LLM needs the value itself.

#### Use secret\_\_ only for values that stay in tool headers

Prefix auth tokens and API keys with `secret__` so they can only be bound to tool headers and are never sent to the LLM. Because `secret__` values are redacted as `<REDACTED>` in the conversations API (post-call transcription webhooks still receive the original values), pass values you need to read back from the conversations API as regular dynamic variables, or pass a non-sensitive identifier and look up the sensitive value on your own system.

#### Do not rely on system\_\_user_id for authentication

`system__user_id` is provided by the client for tracking and analytics and is not verified by ElevenAgents. Verify caller identity through a [conversation initiation webhook](/docs/eleven-agents/customization/personalization#conversation-initiation-webhooks), a signed token in a `secret__` header variable, or a verification tool call before exposing account data.

#### Configure placeholders for testing and previews

Set default values in `dynamic_variable_placeholders` for every custom variable used in your prompts, first messages, and tools. Preview conversations in the dashboard and [simulation tests](/docs/eleven-agents/customization/agent-testing) do not run conversation initiation webhooks, so unset variables remain as literal `{{variable_name}}` placeholders during testing.

## Troubleshooting

#### Variables not replacing

Verify that:

* Variable names match exactly (case-sensitive)
* Variables use double curly braces: `{{variable_name}}`
* Variables are included in your `dynamic_variables` object

#### Type errors

Ensure that:

* Variable values match the expected type
* Values are strings, numbers, or booleans only
