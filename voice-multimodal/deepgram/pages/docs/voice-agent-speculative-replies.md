---
title: "Speculative Replies & Turn Confirmation"
source: https://developers.deepgram.com/docs/voice-agent-speculative-replies.md
path: docs/voice-agent-speculative-replies
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Speculative Replies & Turn Confirmation

Voice Agent

Every turn has two moments, not one. The agent begins working at the first, and commits at the second.

1. **The agent starts thinking.** Speech-to-text is moderately confident the user has stopped, so the agent closes the utterance internally and sends the request to the LLM. The turn is not yet confirmed.
2. **The agent is cleared to reply.** Speech-to-text is confident the user has stopped. The turn is confirmed and the reply is released.

The window between those two moments is the **speculative window**. Working inside it is what removes hundreds of milliseconds from response time: by the time the turn is confirmed, the reply is usually already generated.

If the user turns out not to have finished, the turn resumes. The agent sends `UserStartedSpeaking`, drops the in-flight LLM stream, and discards the speculative reply.

## What waits for turn confirmation

| Behavior                                  | Gated on confirmation?                                                                                                                                                                                                      |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent audio (TTS)                         | **Yes.** Audio is held until the turn is confirmed, so the agent never speaks over a user who is still talking.                                                                                                             |
| `ConversationText` for the user's message | **Yes.** The user message is held as non-final until the turn is confirmed.                                                                                                                                                 |
| Function calls                            | **No, by default.** A tool call is dispatched as soon as the LLM emits it, inside the speculative window. Set [`defer_until_eot`](/docs/configure-voice-agent#agentthinkfunctionsdefer_until_eot) on a function to hold it. |

The asymmetry in that last row is deliberate. Most functions read data, and dispatching them early is where the latency win comes from. Some functions change the world, and those should wait.

## Why an irreversible function call needs to wait

Consider an agent with an `end_call` function. The user says "that's all I need," the agent starts thinking, and `end_call` fires. The user then says "actually, put me through to a person." The turn resumes and the agent cancels the call.

Cancellation is bookkeeping. The telephony call is already hung up.

The same shape applies to booking a reservation the user amends mid-turn, charging a card, or sending a message. When the side effect cannot be taken back, the function must not run until the turn is confirmed.

Set `defer_until_eot: true` on those functions:

```json
{
  "name": "end_call",
  "description": "End the conversation and close the connection",
  "parameters": { "type": "object", "properties": {} },
  "defer_until_eot": true
}
```

A deferred call is held through the speculative window and dispatched when the turn is confirmed. If the turn resumes instead, the call is discarded before it does anything.

Deferring one function does not slow the others. A call that did not opt in still dispatches immediately, even when a deferred call sits ahead of it in the same turn. See [`defer_until_eot`](/docs/configure-voice-agent#agentthinkfunctionsdefer_until_eot) for the full ordering rules.

## When a turn resumes

Everything the agent built speculatively is torn down together:

* The in-flight LLM stream is dropped.
* Every queued and in-progress function call for that turn is marked `CANCELLED`.
* For each cancelled call your client had already received, the server sends [`FunctionCallCancelled`](/docs/voice-agent-function-call-cancelled). Stop work on that `id` and do not reply to it.

A server-side function that already reached your endpoint is a different matter. Deepgram discards the response, but your endpoint ran. This is the reason to defer rather than to rely on cancellation.

## Every listen provider does this

Speculative replies are not specific to Flux. Deepgram STT models inside the Voice Agent support building a reply before the turn is confirmed. Flux uses its built in end of turn detection, and Nova models use independent end-of-turn detection.

`defer_until_eot` works with all of them, and produces no warning on any of them.

## Tuning the window

These parameters set how wide the speculative window is. See [Configure the Voice Agent](/docs/configure-voice-agent) for the full reference.

* `agent.listen.provider.eager_eot_threshold` opens the window earlier. Lower values mean earlier thinking, lower latency, and more resumed turns.
* `agent.listen.provider.eot_threshold` sets the confidence needed to confirm the turn. Higher values are more reliable and slower.
* `agent.listen.provider.eot_timeout_ms` confirms the turn after a fixed amount of time regardless of confidence. A turn confirmed this way clears the reply like any other, so deferred function calls dispatch rather than being dropped.
* Setting `eot_threshold` to `1.0` suppresses natural end-of-turn detection entirely. The turn is then confirmed only by [`ForceEndTurn`](/docs/voice-agent-force-end-turn), and deferred function calls wait for it.

If you are wiring Flux yourself rather than using the managed agent, see [Optimize Voice Agent Latency with Eager End of Turn](/docs/flux/voice-agent-eager-eot).
