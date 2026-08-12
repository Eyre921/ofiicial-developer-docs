---
title: "Expressivity"
source: https://developers.deepgram.com/docs/tts-expressivity.md
path: docs/tts-expressivity
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Expressivity

**`expressivity` is a beta parameter.**

* **Behavior may change** in future model versions.
* **The default (`0`) is production-ready.** It's Deepgram's tuned delivery for enterprise voice agents and the only value validated for production.
* **Changing it can degrade quality** — hallucinations (extra, dropped, or repeated words) and pronunciation errors — with more risk at larger magnitudes.
* **Audition before shipping.** Test any non-default value in the Playground and check for hallucinations and pronunciation issues.

The `expressivity` parameter shifts a Flux TTS voice's delivery register along a calm ↔ animated axis.

Every Flux voice is tuned by Deepgram to its most natural delivery out of the box. `expressivity` lets you adjust that delivery for your use case — calmer and more measured for empathetic or de-escalation contexts, or more animated and upbeat for energetic interactions.

**Availability: Flux TTS only.** `expressivity` is available on Flux TTS (`/v2/speak`), on both streaming and batch. It is not available on Aura-2 (`/v1/speak`).

## Parameter reference

|                |                                               |
| -------------- | --------------------------------------------- |
| **Parameter**  | `expressivity`                                |
| **Type**       | integer                                       |
| **Range**      | `-2` to `2`                                   |
| **Default**    | `0` (the voice's tuned, recommended delivery) |
| **Applies to** | All Flux TTS voices                           |
| **Status**     | Beta                                          |

`expressivity` is an integer dial centered on each voice's tuned default at `0`, from `-2` (calmer) to `2` (more animated). Omitting the parameter is equivalent to `0`.

* **`0` (default)** — The voice's natural, tuned delivery, and the recommended setting for production.
* **Negative values (`-1`, `-2`)** — Progressively calmer, more measured delivery: steadier pacing, narrower pitch movement, and a slightly lower overall pitch.
* **Positive values (`1`, `2`)** — Progressively more animated delivery: wider pitch contours, more pacing variation, and a slightly brighter overall pitch.

The `-2` to `2` range is intentionally conservative during beta, and values must be whole numbers. Out-of-range values return [`EXPRESSIVITY_OUT_OF_RANGE`](/docs/flux-tts/server-messages#connection-rejection-codes); fractional values such as `1.5` return [`EXPRESSIVITY_INCREMENT_INVALID`](/docs/flux-tts/server-messages#connection-rejection-codes).

## How it works

`expressivity` adjusts the voice model's delivery characteristics as a bundle — pitch range, pacing variation, overall pitch, and timbre (the voice's tonal color) all move together. Because timbre shifts along with the rest, the voice's character audibly changes as you move away from `0`, not just its energy level. It is not a pitch-shift or speed control: negative values don't slow the voice down, and positive values don't speed it up. (For speaking rate, see `speed` — on Flux TTS, `0.85` to `1.15` in `0.05` increments.)

Because each voice has its own natural character, **the same value can sound different across voices**. A `2` may be a subtle change on one voice and pronounced on another. Audition your specific voice at the value you plan to use.

**Evaluating Flux TTS?** Evaluate voices at the default (`0`) or above. Low values intentionally produce flatter, more uniform delivery and aren't representative of the model's expressive range.

## Usage

Set `expressivity` as a query parameter on either `/v2/speak` transport.

### Streaming

```text
wss://api.deepgram.com/v2/speak?model=flux-haley-en&expressivity=2
```

### Batch

```bash
curl "https://api.deepgram.com/v2/speak?model=flux-haley-en&expressivity=2" \
     -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"text": "Your appointment is confirmed for 3pm tomorrow."}' \
     --output audio.mp3
```

On streaming, the value is fixed when you open the connection and applies for its duration. On batch, it applies to that request.

## Behavior notes

* **Delivery character shifts with the value.** Moving away from `0` intentionally changes how the voice sounds — including shifts in pitch and timbre (the voice's tonal color). This is the parameter working as designed, not an artifact.
* **The lowest values can enter an "ASMR" register.** On some voices, the calmest values push delivery past merely measured into a soft, breathy, intimate character — an intentional extension of the calm end of the range. Audition to confirm it suits your use case.
* **Higher values increase natural variation.** The higher the value, the more delivery varies between generations of the same text — part of what makes speech sound animated and human. If your use case requires highly uniform delivery across repeated prompts, use `0` or a lower value.
* **Output consistency guarantees apply at the default.** Deepgram's determinism characteristics for Flux TTS are measured at the default (`expressivity` omitted or `0`).
* **Effect and risk grow with magnitude.** The further from `0`, the stronger the effect — and the higher the chance of hallucinations or pronunciation errors. The range is kept narrow during beta for this reason; audition any non-default value before production.

## FAQ

**Does this change which voice I'm using?**

You're always getting the same underlying voice. That said, `expressivity` does more than adjust energy — pitch and timbre (tonal color) shift too — so the voice's character changes noticeably, especially toward the ends of the range, the way a person sounds different reading a bedtime story versus hosting a game show.

**Can I change it mid-conversation?**

No. `expressivity` is set when you open the connection and applies for the whole session.

**How does it interact with `speed`?**

They're independent controls: `speed` adjusts speaking rate (on Flux TTS, `0.85` to `1.15` in `0.05` increments), `expressivity` adjusts delivery character. They can be combined; larger values of both together are more likely to sound less natural, so audition combined settings.

**Why does the same value sound different on different voices?**

Each voice has its own character and its own sensitivity to the dial. `0` is every voice's tuned default, but a given step away from `0` lands differently from one voice to the next — so the same value can be a subtle shift on one voice and a pronounced one on another. Audition your specific voice.
