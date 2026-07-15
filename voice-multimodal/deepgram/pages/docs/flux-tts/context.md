---
title: "Cross-Turn Context"
source: https://developers.deepgram.com/docs/flux-tts/context.md
path: docs/flux-tts/context
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Cross-Turn Context

On `/v1/speak`, every request is independent: text goes in, audio comes out, and all state is discarded. Short responses like "Of course" lose the tone established earlier in the conversation, and prosody can shift at chunk boundaries. `/v2/speak` closes this gap at the model layer by **persisting conversational state across turns** — with **no new API parameters** to set or manage.

This page explains the mechanism. The protocol provides the surface ([Client Messages](/docs/flux-tts/client-messages), [Server Messages](/docs/flux-tts/server-messages)); this is what happens underneath.

## How it works

Flux TTS maintains internal state that evolves as it generates. Cross-turn context works by **not resetting that state between turns**:

1. **Turn 1** — State starts from the conditioning clip only. The model generates; state now includes the clip plus the generated audio.
2. **The user responds** — handled by your STT and LLM, not by TTS.
3. **Turn 2** — The model generates from the existing state. Delivery is informed by the prior output, so prosody and pacing carry forward.
4. **Turn N** — State has accumulated across the conversation. There is no prompt re-consumption and no replay, which is a meaningful cost and latency advantage over re-priming each turn.

**State is the model's own prior generations — nothing else.** It does **not** include the user's audio or text, and it does not include your LLM's reasoning. It is purely the model's evolving acoustic state across the turns it has spoken. No API field turns this on; it is the default behavior of `/v2/speak`.

## What resets state, and what doesn't

Ending a turn does **not** reset the model's conversational state — it carries forward into the next turn, which is what keeps prosody consistent across a back-and-forth.

| Action                  |        Resets model state       |
| ----------------------- | :-----------------------------: |
| `Flush` (ends the turn) |                No               |
| New connection          | Yes — each session starts fresh |

When barge-in (`Interrupt`) ships at GA, it will also leave model state intact — it stops synthesis and reports what the user heard, while prosody continues consistently into the next turn.

## Operational notes

* State persistence adds **no per-turn compute**. The only cost is GPU memory held for the session duration.
* Max session duration is 1 hour; the server closes the WebSocket at that mark. See [Feature Overview → Session Limits](/docs/flux-tts/feature-overview#session-limits).

## Related resources

* [The Speech Lifecycle](/docs/flux-tts/state) — the turn state machine
* [Server Messages](/docs/flux-tts/server-messages) — per-turn and cumulative reporting
* [Build a Flux TTS Voice Agent](/docs/flux-tts/voice-agent) — context behavior across a conversation

***
