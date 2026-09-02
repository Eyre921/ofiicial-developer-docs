---
title: "Maintaining Context"
source: https://developers.deepgram.com/docs/voice-agent-conversation-context.md
path: docs/voice-agent-conversation-context
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Maintaining Context

Voice Agent

A voice agent's behavior on any call is the sum of a few moving parts: the prompt that shaped it, the history you handed it on connect, anything either side has injected during the call, and any function results it has gathered. This page covers every lever the API gives you for managing that context.

## Levers at a glance

| Lever                  | When it applies | Where it lives                                                       | Effect                                                         |
| ---------------------- | --------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| System prompt          | Connect         | `agent.think.prompt` in [Settings](/docs/voice-agent-settings)       | Sets persona and rules for the whole session                   |
| Prompt update          | Mid-call        | [`UpdatePrompt`](/docs/voice-agent-update-prompt) client message     | Replaces the system prompt for the rest of the session         |
| History                | Connect         | `agent.context.messages` in [Settings](/docs/voice-agent-settings)   | Loads prior turns and function calls before the session starts |
| Inject agent message   | Mid-call        | [`InjectAgentMessage`](/docs/voice-agent-inject-agent-message)       | Makes the agent speak a specific line                          |
| Inject user message    | Mid-call        | [`InjectUserMessage`](/docs/voice-agent-inject-user-message)         | Adds a synthetic user turn the agent reacts to                 |
| Function results       | Mid-call        | Function call response payloads                                      | Becomes part of the agent's working memory                     |
| Reusable configuration | Pre-call        | [Reusable Agent Configurations](/docs/reusable-agent-configurations) | Stores a full `agent` block for reuse                          |
| History flag           | Connect         | `settings.flags.history`                                             | Disables history retention entirely                            |

The rest of this page walks each lever in detail. You can mix all of them in the same session.

## System prompt

The system prompt is the agent's initial brief. It defines persona, scope, and any rules the agent should follow throughout the call. Set it inside the `agent.think.prompt` field of your [Settings](/docs/voice-agent-settings) message at connect time.

```json
{
  "type": "Settings",
  "agent": {
    "think": {
      "provider": { "type": "open_ai", "model": "gpt-4o-mini" },
      "prompt": "You are a friendly support agent for Acme. Always confirm the customer's account number before answering billing questions."
    }
  }
}
```

For voice-specific prompt-writing patterns (formatting numbers for TTS, keeping turns short, avoiding markdown the agent will try to read aloud), see [Prompting Voice Agents](/docs/prompting-voice-agents).

## Prompt update at runtime

If you need to change the agent's behavior part-way through a call (a phase change, a hand-off to a new persona, an updated rule), send an [`UpdatePrompt`](/docs/voice-agent-update-prompt) message. The new prompt replaces the system prompt for the rest of the session.

```json
{
  "type": "UpdatePrompt",
  "prompt": "You are now a billing specialist. Resolve the dispute the customer just described."
}
```

Combine `UpdatePrompt` with [`UpdateThink`](/docs/voice-agent-update-think) if you also want to swap the LLM provider mid-call.

## History

When you start a new session, you can hand the agent the history of prior interactions so it picks up where the last call left off. History is provided through `agent.context.messages` and supports two message shapes that can be mixed in the same array.

### Conversation history

Plain back-and-forth between user and assistant.

```json
{
  "type": "Settings",
  "agent": {
    "context": {
      "messages": [
        { "type": "History", "role": "user", "content": "I'm trying to recover my account." },
        { "type": "History", "role": "assistant", "content": "Sure, I can help. What email did you use to sign up?" }
      ]
    }
  }
}
```

### Function call history

Function calls executed in earlier sessions, with arguments and results.

```json
{
  "type": "Settings",
  "agent": {
    "context": {
      "messages": [
        { "type": "History", "role": "user", "content": "What's the weather in New York?" },
        {
          "type": "History",
          "function_calls": [
            {
              "id": "fc_weather_12345",
              "name": "get_weather",
              "client_side": true,
              "arguments": "{\"location\": \"New York\"}",
              "response": "Partly cloudy, 22°C."
            }
          ]
        },
        { "type": "History", "role": "assistant", "content": "It's partly cloudy in New York, around 22 degrees." }
      ]
    }
  }
}
```

The full schema and field-by-field reference live on the [History](/docs/voice-agent-history) page.

### Continuing past the maximum session length

Sessions close automatically at 2 hours. The server sends a `MAXIMUM_SESSION_LENGTH_APPROACHING` warning at 1 hour 55 minutes and a terminal `MAXIMUM_SESSION_LENGTH_REACHED` error at 2 hours. To carry a long conversation across that boundary, capture the session's history, open a new connection, and replay the turns in `agent.context.messages`. See [Maximum session length](/docs/voice-agent-errors-warnings#maximum-session-length).

### Toggling history

History is enabled by default. To disable it, set:

```json
{
  "type": "Settings",
  "settings": {
    "flags": { "history": false }
  }
}
```

## Inject messages

Two client messages let you add to context mid-call.

### `InjectAgentMessage`

Make the agent say something specific, immediately. The injected text is treated as if the agent had just produced it.

```json
{ "type": "InjectAgentMessage", "content": "Hold on a moment while I check that for you." }
```

Useful for filler responses, status updates while a slow tool runs, or scripted follow-ups. Reference: [Inject Agent Message](/docs/voice-agent-inject-agent-message).

### `InjectUserMessage`

Push a synthetic user turn into the conversation. The agent processes it as if the user said it. Useful for orchestrated hand-offs from your application to the agent without going through the microphone.

```json
{ "type": "InjectUserMessage", "content": "The customer's authentication is now complete." }
```

Reference: [Inject User Message](/docs/voice-agent-inject-user-message).

## Function results as context

Function call responses returned to the agent become part of its working context. The agent can reference them in later turns, decide whether to call again, and use the results to shape what it says next. See [Function Calling](/docs/voice-agents-function-calling) for the full request/response loop and [Function Call Context](/docs/voice-agent-function-call-context) for how function results interact with conversation history.

## Reusable configurations

If your agent's prompt, providers, and tools are stable across many sessions, save them as a [Reusable Agent Configuration](/docs/reusable-agent-configurations). You get back a UUID that you can pass in place of the full `agent` object on every connection.

Reusable configurations are most useful when:

* The same prompt is used by many sessions
* You want to update prompts without redeploying the client
* Multiple environments need to share the same agent definition

The reusable configuration only covers the `agent` block. Per-session context (history, runtime injections) is still passed at connect time or during the call.

## Choosing which lever for which job

| You want to...                                                  | Use                                                                  |
| --------------------------------------------------------------- | -------------------------------------------------------------------- |
| Set persona and rules at the start of the call                  | [System prompt](/docs/prompting-voice-agents)                        |
| Change the agent's behavior part-way through a call             | [`UpdatePrompt`](/docs/voice-agent-update-prompt)                    |
| Resume a prior conversation seamlessly                          | [History](/docs/voice-agent-history)                                 |
| Replay function results from a prior session                    | [History with function calls](/docs/voice-agent-history)             |
| Have the agent speak a specific line right now                  | [`InjectAgentMessage`](/docs/voice-agent-inject-agent-message)       |
| Tell the agent what just happened in your application           | [`InjectUserMessage`](/docs/voice-agent-inject-user-message)         |
| Reuse the same agent definition across sessions or environments | [Reusable Agent Configurations](/docs/reusable-agent-configurations) |
| Disable history entirely                                        | `settings.flags.history: false`                                      |
