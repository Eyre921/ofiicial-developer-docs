---
title: "Inject Agent"
source: https://developers.deepgram.com/docs/voice-agent-inject-agent-message.md
path: docs/voice-agent-inject-agent-message
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Inject Agent

&#x20;Voice Agent

The `InjectAgentMessage` message is a JSON message you can send to immediately trigger an agent statement.

## Purpose

`InjectAgentMessage` lets your server put words in the agent's mouth mid-conversation. The optional `behavior` field controls how the message interacts with any ongoing user or agent turn: wait for silence, or queue within the current turn.

## Fields

| Field      | Type   | Required | Description                                                                                               |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------- |
| `type`     | string | Yes      | Must be `"InjectAgentMessage"`.                                                                           |
| `message`  | string | Yes      | The statement the agent should say.                                                                       |
| `behavior` | string | No       | How the injection interacts with the current turn: `"default"` or `"queue"`. Uses `"default"` if omitted. |

### `behavior` values

* **`default`**: the agent speaks only if neither the user nor the agent is mid-turn. If a turn is in progress, the server rejects the request and replies with [`InjectionRefused`](#injectionrefused). This matches the original `InjectAgentMessage` behavior.
* **`queue`**: the server appends the message after any `ConversationText` that is already queued, without interrupting the current agent turn or the in-flight think response. If nothing is queued, the agent speaks the message immediately.

## Example Payloads

### `default`: wait for silence

```json JSON
{
  "type": "InjectAgentMessage",
  "behavior": "default",
  "message": "Are you still on the line?"
}
```

### `queue`: append after any current ConversationText

```json JSON
{
  "type": "InjectAgentMessage",
  "behavior": "queue",
  "message": "Thanks for your patience, the system is still loading."
}
```

## Responses

The server sends an [`AgentAudioDone`](/docs/voice-agent-agent-audio-done) message after the last `InjectAgentMessage` is spoken.

```json JSON
{
  "type": "AgentAudioDone"
}
```

### `InjectionRefused`

When `behavior` is `default` or `queue` and the request arrives while the *user* is mid-turn, the server ignores the request and replies with `InjectionRefused`. If the *agent* is mid-turn, the server returns `InjectionRefused` only when `behavior` is `default`.

```json JSON
{
  "type": "InjectionRefused"
}
```

## Use Cases

Pick the `behavior` value that matches what you want to happen to the current turn.

### When to use `default`

Use `default` when the injection is only appropriate during silence and you would rather drop it than step on the conversation.

* Prompting the user to continue if they have been silent for a while ("Are you still on the line?").
* Optional nudges where being ignored is acceptable if the caller is already talking.

### When to use `queue`

Use `queue` when you want the agent to say something *after* whatever it is currently saying, without stepping on it. This is the right choice for filler during function calls, where the model has already emitted pre-function narration and you want to extend it rather than replace it.

* Filling silence during a long-running function call ("One moment while I pull that up") without cutting off the model's current response.
* Chaining a follow-up sentence after the agent finishes its current turn ("...and I've also emailed you a copy.").
* Streaming progress updates from a backend job so the caller hears them in order.
