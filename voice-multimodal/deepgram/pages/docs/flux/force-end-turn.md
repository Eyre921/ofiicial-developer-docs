---
title: "Force End Turn"
source: https://developers.deepgram.com/docs/flux/force-end-turn.md
path: docs/flux/force-end-turn
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Force End Turn

Streaming:Flux

Flux detects the end of a turn natively. The `ForceEndTurn` message lets you override that detection and end the current turn immediately, on your own signal. Flux ends the turn on the audio transcribed so far and emits a standard `EndOfTurn` message.

## Turn-taking modes

`ForceEndTurn` and `eot_threshold` together give you a spectrum of control over how turns end, and you can move between these modes mid-stream with a [`Configure`](/docs/flux/configure) message:

* **Automatic** — Flux's native end-of-turn detection decides (the default). `EndOfTurn` carries `"trigger": "model"`.
* **Semi-manual** — keep native detection running and override it with `ForceEndTurn` whenever you have a definitive signal. The model handles the ambiguous endings; you handle the unambiguous ones.
* **Fully manual** — set `eot_threshold=1.0` to suppress native detection entirely and drive every turn ending with `ForceEndTurn`. See [Bring Your Own Turn Detection](/docs/flux/own-turn-detection).

Because `eot_threshold` can be changed on the fly with `Configure`, you can switch modes for a single turn — for example, raise it to `1.0` while a caller reads a fixed-length account ID so Flux won't end the turn early, then lower it again for natural conversation.

## Purpose

Some turn endings are unambiguous and don't require the model to infer them. `ForceEndTurn` gives you an explicit override for these cases:

* **Push-to-talk release** — the user holds a button to speak and releases when done. The release is a definitive turn-end signal.
* **DTMF tones and IVR events** — a keypad press or menu selection ends the turn.
* **UI actions** — a "send" button or other application event marks the utterance complete.
* **Application timeouts** — your own logic decides the turn is over.
* **External turn detection** — you already run a VAD or endpointing stack and want to keep it while adopting Flux for transcription. See [Bring Your Own Turn Detection](/docs/flux/own-turn-detection).

## Send a ForceEndTurn message

Send the following JSON as a WebSocket text frame. The message has no additional fields — it operates on the turn currently in progress.

```json JSON
{
  "type": "ForceEndTurn"
}
```

## Response

When a turn is active, the server responds with a standard `EndOfTurn` message. The `trigger` field is set to `manual`, and the `transcript` reflects all audio received before the `ForceEndTurn` message arrived.

```json JSON
{
  "type": "TurnInfo",
  "request_id": "ad12514a-0d38-4f7e-8fba-cce10d8f174c",
  "sequence_id": 42,
  "event": "EndOfTurn",
  "turn_index": 3,
  "audio_window_start": 4.2,
  "audio_window_end": 6.8,
  "transcript": "I need to cancel my subscription",
  "words": [
    { "word": "I", "confidence": 0.95 },
    { "word": "need", "confidence": 0.93 },
    { "word": "to", "confidence": 0.97 },
    { "word": "cancel", "confidence": 0.91 },
    { "word": "my", "confidence": 0.96 },
    { "word": "subscription", "confidence": 0.89 }
  ],
  "end_of_turn_confidence": 0.35,
  "trigger": "manual"
}
```

The response behaves exactly like a natural `EndOfTurn`, with two things to note:

* **`transcript` reflects the audio transcribed so far.** `ForceEndTurn` ends the turn on the latest transcription rather than triggering an additional decode pass, so the transcript matches the most recent `Update`. Audio received after `ForceEndTurn` belongs to the next turn.
* **`end_of_turn_confidence` is the model's actual confidence** at the moment you forced the end — it is not inflated to `1.0`. In the example above, `0.35` shows the model was well short of ending the turn on its own. Use it as diagnostic data.

After the `EndOfTurn`, `turn_index` increments and Flux is ready for the next `StartOfTurn` — the same post-turn state as a natural end-of-turn.

## The `trigger` field

`trigger` is present on every `EndOfTurn` event and only there. It states what caused the turn to end.

| Value     | Meaning                                                   |
| --------- | --------------------------------------------------------- |
| `model`   | The turn ended by Flux's native end-of-turn detection.    |
| `manual`  | The turn ended because you sent a `ForceEndTurn` message. |
| `timeout` | The turn ended because `eot_timeout_ms` elapsed.          |

`trigger` is an open set — new values may be added, so handle unrecognized ones gracefully.

## Behavior and edge cases

| Condition                                                  | Behavior                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No active turn (before `StartOfTurn` or after `EndOfTurn`) | **Ignored, with a `Warning`.** No `EndOfTurn` is emitted and `turn_index` does not advance. The server returns a `Warning` message with code `FORCE_END_TURN_NO_ACTIVE_TURN` (not an `Error`). Timing races between an external signal and Flux's `StartOfTurn` are normal, so this is not a hard error. |
| An `EagerEndOfTurn` is pending                             | `ForceEndTurn` supersedes the eager state. `EndOfTurn` fires with `"trigger": "manual"` and no `TurnResumed` is emitted.                                                                                                                                                                                 |
| Active turn, no eager pending                              | `EndOfTurn` is emitted directly with `"trigger": "manual"`. No `EagerEndOfTurn` is synthesized, and `end_of_turn_confidence` may be below `eager_eot_threshold`.                                                                                                                                         |
| Sent alongside `CloseStream`                               | Messages are processed in strict order. `ForceEndTurn` then `CloseStream`: the turn ends with the transcript decoded so far, then the connection closes. `CloseStream` then `ForceEndTurn`: the connection closes and the later `ForceEndTurn` has no effect.                                            |
| Repeated `ForceEndTurn` messages                           | The first ends the turn. Subsequent messages arrive with no active turn, so each returns a `FORCE_END_TURN_NO_ACTIVE_TURN` `Warning` and is otherwise ignored.                                                                                                                                           |
| Sent on `/v1/listen` (Nova-3)                              | Returns an error. `ForceEndTurn` is supported only on the Flux `/v2/listen` endpoint.                                                                                                                                                                                                                    |

## Related Resources

* [Bring Your Own Turn Detection](/docs/flux/own-turn-detection) - Keep your existing turn detection and drive Flux turns with `ForceEndTurn`
* [End-of-Turn Detection Parameters](/docs/flux/configuration) - Tune `eot_threshold`, `eager_eot_threshold`, and `eot_timeout_ms`
* [Configure](/docs/flux/configure) - Update stream configuration mid-stream
* [Close Stream](/docs/flux/close-stream) - Close the WebSocket stream
* [Understanding the Flux State Machine](/docs/flux/state) - Turn events and state transitions
* [Getting Started with Flux](/docs/flux/quickstart) - Quickstart guide with basic configuration

---
