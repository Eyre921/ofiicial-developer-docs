---
title: "Force End Turn"
source: https://developers.deepgram.com/docs/voice-agent-force-end-turn.md
path: docs/voice-agent-force-end-turn
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Force End Turn

Voice Agent

The `ForceEndTurn` message is a JSON message that ends the current turn immediately.

`ForceEndTurn` requires a Deepgram V2 (Flux) listen provider — set `agent.listen.provider.version` to `v2` in the [`Settings`](/docs/voice-agent-settings) message. With any other listen provider the server replies with a [`FORCE_END_TURN_UNSUPPORTED`](/docs/voice-agent-errors-warnings#warning-codes) warning and the turn does not end.

## Purpose

Some turn endings are unambiguous and don't require the model to infer them. `ForceEndTurn` gives your application an explicit override:

* **Push-to-talk release** — the user holds a button to speak and releases when done.
* **DTMF tones and IVR events** — a keypad press or menu selection ends the turn.
* **UI actions** — a "send" button or other application event marks the utterance complete.
* **Your own turn detection** — you run a VAD or endpointing stack and want to own turn taking entirely. Pair `ForceEndTurn` with `eot_threshold: 1.0` to suppress natural end-of-turn detection. See [Bring Your Own Turn Detection](/docs/flux/own-turn-detection).

## Example Payloads

To send the `ForceEndTurn` message, send the following JSON message to the server. The message has no additional fields — it applies to the turn currently in progress.

```json JSON
{
  "type": "ForceEndTurn"
}
```

The agent ends the turn as if end-of-turn had been detected naturally: the [`ConversationText`](/docs/voice-agent-conversation-text) message for the user turn is sent, followed by [`AgentThinking`](/docs/voice-agent-agent-thinking) and the agent's spoken response.

## Behavior

* No turn in progress — the message is ignored. No turn ends and no warning is sent.
* Listen provider is not Deepgram V2 (Flux) — the server sends a `FORCE_END_TURN_UNSUPPORTED` warning and the turn does not end.
* Repeated messages — the first ends the turn; later messages arrive with no turn in progress and are ignored.

## Related Resources

* [Flux Force End Turn](/docs/flux/force-end-turn) - The underlying Flux `ForceEndTurn` control message
* [Bring Your Own Turn Detection](/docs/flux/own-turn-detection) - Own turn taking with `eot_threshold: 1.0` and `ForceEndTurn`
* [Update Listen](/docs/voice-agent-update-listen) - Adjust end-of-turn thresholds mid-session
* [Errors & Warnings](/docs/voice-agent-errors-warnings) - `FORCE_END_TURN_UNSUPPORTED` and other warning codes
