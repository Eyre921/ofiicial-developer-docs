---
title: "Session Observability"
source: https://developers.deepgram.com/docs/voice-agent-observability.md
path: docs/voice-agent-observability
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Session Observability

The Voice Agent dashboard surfaces high-level usage, but it does not give you per-session, turn-by-turn observability. Everything you need is already flowing across the WebSocket. This guide explains what to capture and how to structure it so you get full observability into transcripts, agent behavior, function calls, errors, and latency.

## The Core Idea

The Agent API runs over a single WebSocket connection (`wss://agent.deepgram.com/v1/agent/converse`). All control and event traffic moves across that socket as JSON messages in both directions. There is no separate logging API, so the recommended pattern is to **tap the WebSocket and persist every non-audio frame**, in both directions, keyed to the connection's `request_id`.

That gives you a complete, replayable record of each session that you can join back to the high-level usage in the dashboard.

## What to Capture

### Connection and Metadata

* **`request_id`** from the [`Welcome`](/docs/voice-agent-welcome-message) message. This is the unique ID for the session and the key you use to correlate your logs with dashboard usage. The server sends `Welcome` as soon as the socket opens, so capture it first.
* **The full [`Settings`](/docs/voice-agent-settings) message you send.** This is your record of how the agent was configured: the listen / think / speak providers and models, the prompt, the functions, `context_length`, the `tags` array (tags also flow into usage records, so they become your filtering dimension), and flags such as `history`, `experimental`, and `mip_opt_out`.
* **`SettingsApplied`** confirmation from the server. See [Settings Applied](/docs/voice-agent-setting-applied-message).

### Server Events to Store

| Message                                                                                                                     | Why It Matters                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ConversationText`](/docs/voice-agent-conversation-text) (`role`, `content`)                                               | The transcript of every user and agent turn. The core record. Includes `languages` / `languages_hinted` when using `flux-general-multi`.                                                  |
| [`AgentThinking`](/docs/voice-agent-agent-thinking) (`content`)                                                             | What the agent was processing before it responded.                                                                                                                                        |
| [`FunctionCallRequest`](/docs/voice-agent-function-call-request)                                                            | Tool-call requests with `id`, `name`, `arguments`, and the `client_side` flag. See [Function Calling](/docs/voice-agents-function-calling) for details.                                   |
| [`LatencyReport`](/docs/voice-agent-latency-report)                                                                         | Detailed LLM, TTS, and end-to-end latency breakdown. See [section below](#latencyreport-detailed-latency-telemetry).                                                                      |
| [`UserStartedSpeaking`](/docs/voice-agent-user-started-speaking) / [`AgentAudioDone`](/docs/voice-agent-agent-audio-done)   | Turn boundaries and barge-in timing.                                                                                                                                                      |
| [`Error` / `Warning`](/docs/voice-agent-errors-warnings) (`code`, `description`)                                            | Failure and degradation tracking.                                                                                                                                                         |
| [`Acknowledgements`](/docs/voice-agent-acknowledgements) (`ListenUpdated`, `ThinkUpdated`, `SpeakUpdated`, `PromptUpdated`) | Confirms the exact moment an `Update*` message was applied. If an acknowledgement is missing, the update may not have landed — useful for troubleshooting mid-call configuration changes. |
| [`History`](/docs/voice-agent-history)                                                                                      | Full conversation plus function-call records, useful for session reconstruction and resume. Requires `flags.history: true` (default on).                                                  |

For a complete reference of all server events, see [Outputs: Server Events](/docs/voice-agent-outputs).

### Client Messages to Store

* [`Settings`](/docs/voice-agent-settings)
* [`InjectUserMessage`](/docs/voice-agent-inject-user-message) / [`InjectAgentMessage`](/docs/voice-agent-inject-agent-message) (injected text turns)
* [`UpdatePrompt`](/docs/voice-agent-update-prompt) / [`UpdateThink`](/docs/voice-agent-update-think) / [`UpdateSpeak`](/docs/voice-agent-update-speak) / [`UpdateListen`](/docs/voice-agent-update-listen) (mid-call configuration changes, so you can reconstruct agent state at any point in the call)
* [`FunctionCallResponse`](/docs/voice-agent-function-call-response) (function results returned to the agent)

For a complete reference of all client messages, see [Inputs: Client Messages](/docs/voice-agent-inputs).

Skip the raw binary audio frames unless you specifically need call recordings. If you do, store them separately.

## LatencyReport: Detailed Latency Telemetry

The server emits a [`LatencyReport`](/docs/voice-agent-latency-report) event after each turn. This is the richest latency signal available. Capture it the same way as every other frame.

It breaks down LLM, TTS, and end-to-end latency. All fields are floats in seconds, and each is optional (omitted when not applicable to that turn):

| Field                  | What It Measures                                               |
| ---------------------- | -------------------------------------------------------------- |
| `ttt_token_latency`    | Time to first token of any type (text, tool call, or thinking) |
| `ttt_text_latency`     | Time to first text token from the LLM                          |
| `ttt_tool_latency`     | Time to first tool-call token from the LLM                     |
| `ttt_thinking_latency` | Time to first thinking token from the LLM                      |
| `tts_latency`          | Text-to-speech: first text token to first audio byte           |
| `total_latency`        | End-to-end: user utterance end to first audio byte             |

This lets you attribute latency to the right stage — for example, separating LLM time-to-first-token from TTS time, and isolating tool-call and thinking overhead.

Because the fields are optional, log defensively rather than assuming every field is present on every report.

## Recommended Logging Shape

Wrap every captured frame in your own envelope. Most Agent messages do not carry their own timestamps, so stamp them yourself on send or receive.

```json
{
  "request_id": "fc553ec9-...",
  "session_id": "your-internal-id",
  "customer_id": "...",
  "seq": 42,
  "ts": "2025-06-26T15:04:05.123Z",
  "direction": "server_to_client",
  "payload": { /* the full original JSON message, including its "type" field */ }
}
```

* **`request_id`**: from the [`Welcome`](/docs/voice-agent-welcome-message) message — the correlation key for joining your logs with dashboard usage.
* **`seq`**: a monotonic counter you assign for ordering.
* **`ts`**: wall-clock time when you sent or received the frame.
* **`direction`**: `server_to_client` or `client_to_server`.

Write these append-only, one record per frame (JSONL per session, or a table keyed on `request_id` + `seq`). From that store you can:

* Reconstruct the transcript by ordering [`ConversationText`](/docs/voice-agent-conversation-text) events.
* Chart latency from `LatencyReport`.
* Audit agent behavior via [`AgentThinking`](/docs/voice-agent-agent-thinking), [function calls](/docs/voice-agents-function-calling), and mid-call `Update*` messages.
* Alert on [`Error` / `Warning`](/docs/voice-agent-errors-warnings) rates.

## Things to Keep in Mind

* **Timestamps are yours to add.** The protocol does not stamp messages, so record wall-clock time on send and receive, and assign a monotonic sequence number for ordering.
* **Keep `flags.history` enabled** if you want [`History`](/docs/voice-agent-history) events. It is on by default.
* **Set `mip_opt_out`** in [`Settings`](/docs/voice-agent-settings) if the data should not be used for model improvement.

## Related Resources

* [Inputs: Client Messages](/docs/voice-agent-inputs)
* [Outputs: Server Events](/docs/voice-agent-outputs)
* [Voice Agent Overview](/docs/voice-agent)
* [Voice Agent API Reference](/reference/voice-agent/voice-agent)
* [Conversation Text](/docs/voice-agent-conversation-text)
* [History](/docs/voice-agent-history)
* [Acknowledgements](/docs/voice-agent-acknowledgements)
* [Message Flow](/docs/voice-agent-message-flow)
* [Welcome](/docs/voice-agent-welcome-message)
