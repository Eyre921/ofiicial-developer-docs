---
title: "Bring Your Own Turn Detection"
source: https://developers.deepgram.com/docs/flux/own-turn-detection.md
path: docs/flux/own-turn-detection
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Bring Your Own Turn Detection

Streaming:Flux

Flux detects the end of a turn natively, and for most voice agents that is the right default. But if you have already invested in a turn detection stack — a VAD, an endpointing model, push-to-talk, or your own detector — you can keep it and adopt Flux for transcription without ripping out that logic. This guide shows the recipe for taking full ownership of turn endings.

## The recipe

Two settings put you in control:

1. **Set `eot_threshold` to `1.0`.** This suppresses Flux's natural `EndOfTurn` events — the model will not end a turn on its own confidence.
2. **Leave `eager_eot_threshold` unset.** Eager end-of-turn is off by default; keep it off so no `EagerEndOfTurn` events fire.

Then send a [`ForceEndTurn`](/docs/flux/force-end-turn) message whenever your own detector decides the turn is over. Flux ends the turn and emits an `EndOfTurn` with `"trigger": "manual"`.

```python Python
import json
import websockets

url = (
    "wss://api.deepgram.com/v2/listen?model=flux-general-en"
    "&eot_threshold=1.0"       # suppress natural end-of-turn
    "&eot_timeout_ms=30000"    # safety-net backstop (see below)
)
headers = {"Authorization": "Token YOUR_DEEPGRAM_API_KEY"}

async with websockets.connect(url, additional_headers=headers) as ws:
    # When your turn detector fires:
    await ws.send(json.dumps({"type": "ForceEndTurn"}))
```

```text Direct WebSocket
wss://api.deepgram.com/v2/listen?model=flux-general-en&eot_threshold=1.0&eot_timeout_ms=30000
```

## How it works

1. **Send audio as usual.** Flux transcribes continuously and emits `StartOfTurn` and `Update` events. With `eot_threshold=1.0`, it never emits `EndOfTurn` on its own.
2. **Your detector decides the turn is over.** A push-to-talk release, a VAD silence event, a DTMF tone — whatever signal you rely on.
3. **Send `ForceEndTurn`.** Flux ends the turn and emits `EndOfTurn` with the transcript decoded so far and `"trigger": "manual"`.
4. **Dispatch the transcript.** Treat the `EndOfTurn` transcript as final and hand it to your agent. `turn_index` increments and Flux is ready for the next turn.

## What still ends a turn

With `eot_threshold=1.0`, three things can still end a turn:

* **`ForceEndTurn`** — your explicit signal (`"trigger": "manual"`).
* **`eot_timeout_ms`** — a safety net. If this much silence passes, Flux force-ends the turn with `"trigger": "timeout"`. Set it high enough that it only fires when your own detection has failed. The maximum is `60000` (60 seconds).
* **`CloseStream`** — closes the connection without finalizing the active turn. No `EndOfTurn` is emitted for it; treat the most recent `Update` as the last transcript for that turn.

Keep `eot_timeout_ms` as a backstop, not a primary mechanism. If it fires often, your external detection is missing turn endings. Tune your detector rather than lowering the timeout.

## Example

This loop wires an external detector to Flux. When your detector fires, it sends a `ForceEndTurn`; Flux replies with an `EndOfTurn` you treat as final.

```javascript JavaScript
// Send audio frames to Flux as you receive them.
function onAudioFrame(frame) {
  ws.send(frame);
}

// Your existing turn detector fires -> force the turn to end.
function onTurnDetected() {
  ws.send(JSON.stringify({ type: "ForceEndTurn" }));
}

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type !== "TurnInfo") return;

  if (data.event === "EndOfTurn") {
    // trigger is "manual" for ForceEndTurn, "timeout" for the backstop.
    console.log(`Turn ended (${data.trigger}):`, data.transcript);
    dispatchToAgent(data.transcript);
  }
};
```

```python Python
import json

# Send audio frames to Flux as you receive them.
async def on_audio_frame(frame):
    await ws.send(frame)

# Your existing turn detector fires -> force the turn to end.
async def on_turn_detected():
    await ws.send(json.dumps({"type": "ForceEndTurn"}))

# Handle messages from Flux.
async for raw in ws:
    data = json.loads(raw)
    if data.get("type") != "TurnInfo":
        continue

    if data.get("event") == "EndOfTurn":
        # trigger is "manual" for ForceEndTurn, "timeout" for the backstop.
        print(f"Turn ended ({data['trigger']}): {data['transcript']}")
        dispatch_to_agent(data["transcript"])
```

## When to use this

* **You already have turn detection you trust** and don't want to migrate off it to adopt Flux.
* **Your turn-end signal is external and definitive** — push-to-talk, DTMF, a UI action.
* **You are migrating from Nova-3** and want to keep your existing endpointing while gaining Flux transcript quality. See [Migrating from Nova-3 to Flux](/docs/flux/nova-3-migration).

If you don't already have a turn detection stack, prefer Flux's native detection — it is purpose-built for conversational turn-taking. See [End-of-Turn Detection Parameters](/docs/flux/configuration).

## Related Resources

* [Force End Turn](/docs/flux/force-end-turn) - The control message reference
* [End-of-Turn Detection Parameters](/docs/flux/configuration) - Tune `eot_threshold`, `eager_eot_threshold`, and `eot_timeout_ms`
* [Understanding the Flux State Machine](/docs/flux/state) - Turn events and state transitions
* [Migrating from Nova-3 to Flux](/docs/flux/nova-3-migration) - Migration guide

---
