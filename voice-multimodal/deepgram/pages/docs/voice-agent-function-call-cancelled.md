---
title: "Function Call Cancelled"
source: https://developers.deepgram.com/docs/voice-agent-function-call-cancelled.md
path: docs/voice-agent-function-call-cancelled
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Function Call Cancelled

Voice Agent

The Voice Agent server sends `FunctionCallCancelled` when a client-side function call it already sent you is cancelled because the user started speaking again, either inside the speculative window (the turn resumed) or after the turn was confirmed (barge-in). Only calls the client already received are announced.

## Purpose

The agent begins building a reply before the user's turn is confirmed. Function calls produced in that window are dispatched immediately unless the function sets [`defer_until_eot`](/docs/configure-voice-agent#agentthinkfunctionsdefer_until_eot). When the turn resumes, those calls are cancelled, and this message tells you which ones. The same message arrives when the user barges in after the turn was confirmed and the agent abandons the reply that produced the call.

Without it, a client holding a [`FunctionCallRequest`](/docs/voice-agent-function-call-request) cannot tell a live request from an abandoned one. For background on the window itself, see [Speculative Replies & Turn Confirmation](/docs/voice-agent-speculative-replies).

## When you receive it

The server sends this message only for calls it already sent you, whether the cancellation came from a resumed turn or from a barge-in after the turn was confirmed. A call that was still held when the turn resumed was never announced, so there is nothing to cancel and no message arrives.

## Handling the message

When your client receives a `FunctionCallCancelled`:

1. Stop any work in progress for each `id` in the list.
2. Do not send a [`FunctionCallResponse`](/docs/voice-agent-function-call-response) for those ids. A late response is dropped.
3. Roll back anything you already committed, if your function is not idempotent. Better still, set `defer_until_eot: true` on functions that cannot be rolled back, so they never fire speculatively.

## Example payload

```json
{
  "type": "FunctionCallCancelled",
  "functions": [
    {
      "id": "fc_12345678-90ab-cdef-1234-567890abcdef",
      "name": "book_appointment"
    }
  ]
}
```

## Fields

| Field              | Type   | Description                                                    |
| ------------------ | ------ | -------------------------------------------------------------- |
| `type`             | string | Always `"FunctionCallCancelled"`.                              |
| `functions[].id`   | string | The `id` from the `FunctionCallRequest` that is now cancelled. |
| `functions[].name` | string | The name of the cancelled function.                            |

## Related messages

* [`FunctionCallRequest`](/docs/voice-agent-function-call-request): The message this one cancels.
* [`UserStartedSpeaking`](/docs/voice-agent-user-started-speaking): Sent when the turn resumes, which is what triggers the cancellation.
* [Speculative Replies & Turn Confirmation](/docs/voice-agent-speculative-replies): Why calls can be cancelled, and how to stop it happening.
