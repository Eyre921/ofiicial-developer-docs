---
title: "Function Call Context"
source: https://developers.deepgram.com/docs/voice-agent-function-call-context.md
path: docs/voice-agent-function-call-context
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Function Call Context

&#x20;Voice Agent

When starting a new conversation session with the Voice Agent, you can provide historical context about previous function calls using the `agent.context` parameter. This allows the agent to maintain awareness of past function executions, enabling more coherent and contextual conversations.

## Purpose

Function call context is particularly useful when:

* Resuming a conversation from a previous session
* Providing background context about function calls already executed
* Maintaining continuity in multi-session interactions
* Allowing the agent to reference previous function results

## Message Schema

Function call context is included in the conversation history using the `History` message type with a `function_calls` array. Each function call entry contains complete information about the execution, including arguments and results.

Function call context can be disabled by setting `settings.flags.history` to `false` in the agent configuration. History is enabled by default.

```json JSON
{
  "type": "Settings",
  "settings": {
    "flags": {
      "history": true
    }
  },
  "agent": {
    "context": {
      "messages": [
        {
          "type": "History",
          "role": "user",
          "content": "What's the weather like in New York?"
        },
        {
          "type": "History",
          "function_calls": [
            {
              "id": "fc_weather_12345",
              "name": "get_weather",
              "client_side": true,
              "arguments": "{\"location\": \"New York\"}",
              "response": "The current weather in New York is partly cloudy with a temperature of 295.15°K."
            }
          ]
        },
        {
          "type": "History",
          "role": "assistant",
          "content": "The weather in New York is partly cloudy with a temperature of about 72°F (295.15°K)."
        }
      ]
    },
    "think": {
      "provider": {
        "type": "open_ai",
        "model": "gpt-4o-mini"
      },
      "functions": [
        {
          "name": "get_weather",
          "description": "Get the current weather for a specific location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city or location to get weather for"
              }
            },
            "required": ["location"]
          }
        }
      ]
    }
  }
}
```

## Multiple Message Types

Function call history works seamlessly with [Conversation Context](/docs/voice-agent-history) to provide complete context. You can mix conversation messages and function call messages in the same context array.

## Function Call Context History Structure

Each function call in the history includes the following fields:

| Field         | Type    | Description                                                       |
| ------------- | ------- | ----------------------------------------------------------------- |
| `id`          | String  | A unique identifier for the function call                         |
| `name`        | String  | The name of the function that was called                          |
| `client_side` | Boolean | Indicates if the function was executed client-side or server-side |
| `arguments`   | String  | JSON string containing the arguments passed to the function       |
| `response`    | String  | The response/result returned by the function                      |

## Benefits of Function Call Context History

Including function call history in your agent context provides several advantages:

### Continuity

The agent understands what functions were previously called and their results, enabling natural conversation flow across sessions.

### Efficiency

The agent can reference previous function results instead of making redundant calls for the same information.

### Context Awareness

The agent can make informed decisions based on the complete interaction history, including both conversations and actions taken.

### Natural Interactions

Users can refer to previous actions ("like we did before") and the agent will understand the context.

## Best Practices

### Unique IDs

In most cases the LLM will assign ids. If the LLM does not assign ids, Deepgram will assign ids to the function calls.

### Complete Information

Include both the arguments passed to the function and the complete response received.

### Chronological Order

Maintain the chronological order of function calls and conversations in your history.

### Relevant Context Only

Include only the function call history that's relevant to the current conversation to avoid overwhelming the context.
