---
title: "Personalization"
source: https://elevenlabs.io/docs/eleven-agents/customization/personalization.md
path: docs/eleven-agents/customization/personalization
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Personalization

## Overview

Personalization allows you to adapt your agent's behavior for each individual user, enabling more natural and contextually relevant conversations. ElevenLabs offers multiple approaches to personalization:

1. **Dynamic Variables** - Inject runtime values into prompts and messages
2. **Overrides** - Completely replace system prompts or messages
3. **Conversation initiation webhooks** - Fetch that data from your server when a conversation starts

## Personalization Methods

#### [Dynamic Variables](/docs/eleven-agents/customization/personalization/dynamic-variables)

Define runtime values using `{{ var_name }}` syntax to personalize your agent's messages, system
prompts, and tools.

#### [Overrides](/docs/eleven-agents/customization/personalization/overrides)

Completely replace system prompts, first messages, language, or voice settings for each
conversation.

#### [Conversation initiation webhooks](/docs/eleven-agents/customization/personalization#conversation-initiation-webhooks)

Fetch dynamic variables and overrides from your server for inbound conversations.

## Conversation Initiation Client Data Structure

The `conversation_initiation_client_data` object defines what can be customized when starting a conversation. Clients can send it directly. A conversation initiation webhook returns the same object.

```json
{
  "type": "conversation_initiation_client_data",
  "conversation_config_override": {
    "agent": {
      "prompt": {
        "prompt": "overriding system prompt",
        "llm": "gpt-5.6-luna"
      },
      "first_message": "overriding first message",
      "language": "en"
    },
    "tts": {
      "voice_id": "voice-id-here"
    },
    "conversation": {
      "text_only": false
    },
    "asr": {
      "keywords": ["Acme Corp", "Contoso"]
    }
  },
  "custom_llm_extra_body": {
    "temperature": 0.7,
    "max_tokens": 100
  },
  "dynamic_variables": {
    "string_var": "text value",
    "number_var": 1.2,
    "integer_var": 123,
    "boolean_var": true
  },
  "user_id": "your_custom_user_id",
  "branch_id": "agtbrch_xxxx",
  "environment": "production"
}
```

System dynamic variables (those prefixed with `system__`) cannot be sent or overridden in the
client initiation payload. Only custom dynamic variables can be set via the `dynamic_variables`
field.

## Conversation initiation webhooks

For inbound telephony and messaging, ElevenAgents can fetch this initiation data from your server instead of from the client. When the webhook is enabled, ElevenAgents sends a `POST` request and applies the JSON you return.

Configure the webhook URL and header secrets in [Agents settings](https://elevenlabs.io/app/agents/settings). On the agent **Security** tab, enable **Fetch initiation client data from a webhook** and any override fields your response may include.

The webhook runs for a new inbound conversation on Twilio voice, Exotel, SIP trunk, WhatsApp, or Twilio SMS when initiation client data is not already present.

Outbound Twilio voice, Exotel, SIP, and WhatsApp calls trigger it only if the outbound request did not include `conversation_initiation_client_data`. Outbound WhatsApp messages never trigger it — pass dynamic variables on the outbound request instead.

It does not run for widget or SDK conversations, other messaging integrations, or resumed WhatsApp and SMS threads.

Preview conversations started from the agent settings page do not trigger conversation initiation
webhooks. Use the **Dynamic Variables** placeholders in the agent editor while testing in Preview.
Those placeholders are not used in production inbound conversations.

ElevenAgents sends caller context in the request body:

```json
{
  "caller_id": "+15551234567",
  "called_number": "+15557654321",
  "agent_id": "agent_7101k5zvyjhmfg983brhmhkd98n6",
  "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "conversation_id": "conv_8901k5zvyjhmfg983brhmhkd98n6"
}
```

`caller_id` and `called_number` are phone numbers on Twilio, Exotel, SIP, and SMS. On inbound WhatsApp they are the WhatsApp user ID and your WhatsApp phone number ID. On outbound calls, `caller_id` is your number and `called_number` is the person being dialed. `call_sid` is the provider call SID on telephony and an empty string on WhatsApp and SMS. SIP calls may also include `call_id` and `sip_headers`.

Your response must use the `conversation_initiation_client_data` shape above. Include every custom dynamic variable the agent defines. Overrides are optional and must be enabled in **Security**.

A failed or timed-out webhook can prevent the conversation from starting. For Twilio setup, see [Twilio personalization](/docs/eleven-agents/customization/personalization/twilio-personalization). This webhook is separate from [post-call webhooks](/docs/eleven-agents/workflows/post-call-webhooks).

## Choosing the Right Approach

<thead>
  <tr>
    <th>
      Method
    </th>

    <th>
      Best For
    </th>

    <th>
      Implementation
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      **Dynamic Variables**
    </td>

    <td>
      * Inserting user-specific data into templated content - Maintaining consistent agent
        behavior with personalized details - Personalizing tool parameters
    </td>

    <td>
      Define variables with 

      `{{ variable_name }}`

       and pass values at runtime
    </td>
  </tr>

  <tr>
    <td>
      **Overrides**
    </td>

    <td>
      * Completely changing agent behavior per user - Switching languages or voices - Legacy
        applications (consider migrating to Dynamic Variables)
    </td>

    <td>
      Enable specific override permissions in security settings and pass complete replacement
      content
    </td>
  </tr>

  <tr>
    <td>
      **Conversation initiation webhooks**
    </td>

    <td>
      * Personalizing inbound Twilio, SIP, WhatsApp, or SMS conversations from your server -
        Looking up caller context before the conversation starts
    </td>

    <td>
      Enable the webhook in Security settings and return `conversation_initiation_client_data`
    </td>
  </tr>
</tbody>

## Learn More

* [Dynamic Variables Documentation](/docs/eleven-agents/customization/personalization/dynamic-variables)
* [Overrides Documentation](/docs/eleven-agents/customization/personalization/overrides)
* [Twilio personalization](/docs/eleven-agents/customization/personalization/twilio-personalization)
