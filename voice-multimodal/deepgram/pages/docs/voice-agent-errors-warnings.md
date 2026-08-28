---
title: "Errors & Warnings"
source: https://developers.deepgram.com/docs/voice-agent-errors-warnings.md
path: docs/voice-agent-errors-warnings
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Errors & Warnings

&#x20;Voice Agent

The server sends two diagnostic event types when something goes wrong:

* **`Error`** signals a fatal issue. The session usually cannot continue and the connection often closes shortly after. Treat every `Error` as a session-ending event and reconnect if your application needs to keep talking.
* **`Warning`** signals a non-fatal issue. The session continues. Log the warning, fix the underlying cause if you control it, and otherwise carry on.

Both events follow the same payload shape: a `type` discriminator, a `code` you can branch on, and a human-readable `description`.

## `Error`

The server sends an `Error` message when something prevents the session from continuing.

```json
{
  "type": "Error",
  "description": "A description of what went wrong",
  "code": "The error code"
}
```

### Error codes

| Code                                   | Description                                                                                                   | Recommended action                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `INTERNAL_SERVER_ERROR`                | An internal server error occurred while processing the request.                                               | Retry the connection. If the issue persists, contact Deepgram Support with your `request_id`.                                                                |
| `CLIENT_MESSAGE_TIMEOUT`               | The server waited too long for a WebSocket message from the client.                                           | Send messages (audio or [`KeepAlive`](/docs/agent-keep-alive)) within the expected timeframe. Check your WebSocket connection for network issues.            |
| `UNPARSABLE_CLIENT_MESSAGE`            | A message from the client could not be deserialized according to the expected schema.                         | Verify that every message conforms to the [Voice Agent API schema](/reference/voice-agent/voice-agent). Check for malformed JSON or incorrect message types. |
| `NON_SETTINGS_MESSAGE_BEFORE_SETTINGS` | The client sent a message on the WebSocket before sending a [`Settings`](/docs/voice-agent-settings) message. | Always send a `Settings` message as the first message after the WebSocket opens, before sending any other message.                                           |
| `SETTINGS_ALREADY_APPLIED`             | A `Settings` message arrived after settings were already established.                                         | Send only one `Settings` message per session. To change settings, close the connection and open a new one.                                                   |
| `INVALID_SETTINGS`                     | The `Settings` message parsed but contained invalid values.                                                   | Review the fields in your `Settings` message. See [Configure the Voice Agent](/docs/configure-voice-agent).                                                  |
| `FAILED_TO_START_LISTENING`            | The server failed to open the `listen` (speech-to-text) connection.                                           | Retry the connection. If the issue persists, verify your account has access to Deepgram's speech-to-text service and contact Deepgram Support.               |
| `ASR_CONNECTION_CLOSED`                | The speech-to-text connection closed unexpectedly.                                                            | Retry the connection. This is usually transient. If it persists, contact Deepgram Support with your `request_id`.                                            |
| `ASR_DRIVER_TIMEOUT`                   | No speech-to-text transcript arrived within the expected timeout.                                             | Check that you are sending valid audio data in the correct format. Retry the connection if the issue persists.                                               |
| `USER_AUDIO_FORMAT`                    | The user audio did not match the format the client declared.                                                  | Match the encoding and sample rate in your `Settings` message to the audio you stream. See [Media Inputs & Outputs](/docs/voice-agent-media-inputs-outputs). |
| `FAILED_TO_SPEAK`                      | The agent could not speak after exhausting all retries and fallbacks.                                         | Review your `speak` provider configuration and error messages. Always specify a fallback `speak` provider to survive individual provider outages.            |
| `SERVER_GOING_AWAY`                    | The server running this agent session is shutting down.                                                       | Reconnect to start a new session. This usually means routine server maintenance.                                                                             |
| `NON_EXISTENT_FUNCTION_CALLED`         | A function call referenced a function that does not exist.                                                    | Verify that every function referenced in your agent configuration is defined and registered.                                                                 |
| `AGENT_ID_NOT_SUPPORTED`               | Agent ID is not supported in the current server configuration.                                                | Authenticate the project. Self-hosted builds do not support Agent ID in unauthenticated mode.                                                                |
| `INVALID_AGENT_ID`                     | The Agent ID is invalid.                                                                                      | Verify the Agent ID exists and the format is correct. Check the Deepgram console for valid Agent IDs.                                                        |
| `FAILED_TO_THINK`                      | The agent could not produce an LLM response after exhausting all retries and fallbacks.                       | Review your `think` provider configuration and error messages. Always specify a fallback `think` provider to survive individual provider outages.            |
| `MAXIMUM_SESSION_LENGTH_REACHED`       | The session was closed after reaching the maximum session length of 2 hours.                                  | Start a new session and carry the conversation forward with `agent.context`. See [Maximum session length](#maximum-session-length).                          |

## `Warning`

The server sends a `Warning` message when something needs your attention but does not stop the session.

```json
{
  "type": "Warning",
  "description": "A description of the warning",
  "code": "The warning code"
}
```

Warnings are non-fatal. The application continues to function normally.

### Warning codes

| Code                                       | Description                                                                                             | Recommended action                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `INJECT_AGENT_MESSAGE_DURING_USER_SPEECH`  | `InjectAgentMessage` was ignored during user speech.                                                    | Wait for the user to finish before injecting a new agent message.                                                                                                                                    |
| `INJECT_AGENT_MESSAGE_DURING_AGENT_SPEECH` | `InjectAgentMessage` was ignored during agent speech.                                                   | Wait for the agent to finish its current response before injecting a new message, or send `InjectAgentMessage` with `behavior: "queue"`. See [Inject Agent](/docs/voice-agent-inject-agent-message). |
| `PROMPT_TOO_LONG`                          | The prompt exceeded the maximum allowed length and was truncated.                                       | Reduce prompt length. The limit is 25,000 characters for managed LLMs and unlimited for BYO LLMs.                                                                                                    |
| `THINK_REQUEST_FAILED`                     | A `think` provider request failed.                                                                      | Review the provider error message. Specify a fallback `think` provider to survive individual provider outages.                                                                                       |
| `SPEAK_REQUEST_FAILED`                     | A `speak` provider request failed.                                                                      | Review the provider error message. Specify a fallback `speak` provider to survive individual provider outages.                                                                                       |
| `FUNCTION_CALL_FAILED`                     | A function call failed.                                                                                 | Review the provider error message. Specify a fallback `think` provider to survive individual provider outages.                                                                                       |
| `SLOW_THINK_REQUEST`                       | A `think` provider request is taking a long time.                                                       | Monitor for ongoing slowness and consider a different `think` provider if your use case is latency-sensitive.                                                                                        |
| `SLOW_SPEAK_REQUEST`                       | A `speak` provider request is taking a long time.                                                       | Monitor for ongoing slowness and consider a different `speak` provider if your use case is latency-sensitive.                                                                                        |
| `FORCE_END_TURN_UNSUPPORTED`               | `ForceEndTurn` requires a Deepgram V2 (Flux) listen provider. The current turn was not ended.           | Switch `agent.listen.provider` to a Flux model with `version: "v2"`. See [Force End Turn](/docs/voice-agent-force-end-turn).                                                                         |
| `GPT_4O_STREAM_END_ERROR`                  | `gpt-4o` failed to send a final done message.                                                           | Monitor for ongoing errors and consider a different LLM model or provider.                                                                                                                           |
| `MAXIMUM_SESSION_LENGTH_APPROACHING`       | The session will automatically close in 5 minutes after reaching the maximum session length of 2 hours. | End the conversation, or start a new session and pass the prior turns in `agent.context`. See [Maximum session length](#maximum-session-length).                                                     |

## Maximum session length

A Voice Agent session runs for a maximum of 2 hours. Two events mark the limit:

| Time into the session | Event              | Code                                 |
| --------------------- | ------------------ | ------------------------------------ |
| 1 hour 55 minutes     | `Warning`          | `MAXIMUM_SESSION_LENGTH_APPROACHING` |
| 2 hours               | `Error` (terminal) | `MAXIMUM_SESSION_LENGTH_REACHED`     |

At 2 hours the server closes the session, so treat the warning as your cue to wrap up. To continue a conversation past the limit, open a new WebSocket connection and pass the prior turns in `agent.context.messages` — the agent resumes with full awareness of what was said. See [Maintaining Context](/docs/voice-agent-conversation-context#history).

[`KeepAlive`](/docs/agent-keep-alive) holds an idle connection open, but it does not extend the 2-hour limit.

## Handling errors and warnings

Treat the two events asymmetrically:

* On `Error`, log the `code` and `description`, surface the failure to your application, and reconnect if the use case allows.
* On `Warning`, log the `code` and `description` and continue. If the warning indicates a configuration problem (`PROMPT_TOO_LONG`, `INJECT_AGENT_MESSAGE_DURING_*`), fix the cause on the client side.

Always specify a fallback provider for [`think`](/docs/voice-agent-llm-models) and [`speak`](/docs/voice-agent-tts-models) to survive individual provider outages.
