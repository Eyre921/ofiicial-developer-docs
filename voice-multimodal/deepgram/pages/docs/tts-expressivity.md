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

* **Behavior and values may be tuned** based on feedback before the parameter is finalized. Re-validate the value you ship after model updates rather than treating it as a contract.
* **The default (`0`) is production-ready.** It is Deepgram's tuned delivery for enterprise voice agents and the only value validated for production.
* **Changing it can degrade quality** - hallucinations (extra, dropped, or repeated words) and pronunciation errors become more likely at larger magnitudes.
* **Audition before shipping.** Test the exact value you plan to ship and check for hallucinations and pronunciation issues. The API covers every voice and every value; see the Usage section below. [talk.deepgram.com](https://talk.deepgram.com) is faster for a first listen: it offers the full `-2` to `2` range, labeled Calm to Animated, on a subset of voices. Expressivity controls in the Playground are coming soon.

The `expressivity` parameter shifts a Flux TTS voice's delivery register along a calm to animated axis. Negative values typically produce calmer, steadier, slightly lower-pitched delivery; positive values typically produce more animated delivery with a wider pitch range.

Every Flux voice is tuned by Deepgram to its most natural delivery out of the box, and `0` is that tuned default. Think of `expressivity` as a signed offset from the default rather than a required setting: the voice already sounds good at `0`, and the parameter shifts its register when your use case calls for it.

Expressivity is a register dial, not a quality slider. The calm end is a deliberate production choice for contexts like support and IVR, not a lesser mode; the animated end is a different character, not a better one.

**Availability: Flux TTS only.** `expressivity` is available on Flux TTS (`/v2/speak`), on both streaming and batch. It is not available on Aura-2 (`/v1/speak`).

## Parameter reference

|                |                                                                         |
| -------------- | ----------------------------------------------------------------------- |
| **Parameter**  | `expressivity`                                                          |
| **Type**       | integer                                                                 |
| **Range**      | `-2` to `2`                                                             |
| **Default**    | `0` (the voice's tuned default)                                         |
| **Set**        | As a query parameter, per connection (streaming) or per request (batch) |
| **Applies to** | All Flux TTS voices                                                     |
| **Status**     | Beta                                                                    |

Values must be whole numbers, and omitting the parameter is equivalent to `0`. The server rejects invalid values rather than clamping or rounding them: out-of-range values return [`EXPRESSIVITY_OUT_OF_RANGE`](/docs/flux-tts/server-messages#connection-rejection-codes), and fractional values such as `1.5` return [`EXPRESSIVITY_INCREMENT_INVALID`](/docs/flux-tts/server-messages#connection-rejection-codes).

## What each value sounds like

| Value | Delivery                                                                                                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-2`  | The calm end of the range: noticeably steadier, with measured pacing, narrow pitch movement, and typically a slightly lower overall pitch. On some voices this setting becomes soft and breathy. |
| `-1`  | Slightly subdued: a more measured take on the voice's default delivery.                                                                                                                          |
| `0`   | The voice's tuned default, and the recommended setting for production.                                                                                                                           |
| `1`   | More animated: wider pitch contours and livelier pacing than the default.                                                                                                                        |
| `2`   | The animated end of the range: the widest pitch range and typically the brightest overall pitch.                                                                                                 |

Because each voice has its own natural character, the same value can sound different across voices: a `2` may be a subtle change on one voice and a pronounced one on another.

## Matching register to use case

| Register | Values     | Often suited to                                                                  |
| -------- | ---------- | -------------------------------------------------------------------------------- |
| Calm     | `-2`, `-1` | Support and de-escalation, healthcare, IVR and self-service, empathetic contexts |
| Default  | `0`        | Production voice agents generally; the only value validated for production       |
| Animated | `1`, `2`   | Consumer applications, entertainment and media, outbound engagement              |

These are starting points, not rules. The right value depends on the voice, the content, and the audience, so audition candidate values with your own prompts before committing to one.

### Choosing a value

The fastest way to choose is to hear a few values side by side before hardcoding one. Generate the same line at `-1`, `0`, and `1` with the requests in the Usage section below. For a first listen, [talk.deepgram.com](https://talk.deepgram.com) offers the full `-2` to `2` range, labeled Calm to Animated, on a subset of voices; to audition your exact script, voice, and encoding, use the API. Expressivity controls in the Playground are coming soon.

Because the parameter is in beta, re-validate your chosen value when Deepgram ships model updates rather than treating it as a fixed contract.

## Usage

Set `expressivity` as a query parameter on either `/v2/speak` transport. On streaming, the value is fixed when you open the connection and applies for its duration; on batch, it applies to that request.

### Streaming

```text
wss://api.deepgram.com/v2/speak?model=flux-haley-en&encoding=linear16&sample_rate=24000&expressivity=-1
```

### Batch

```bash
curl "https://api.deepgram.com/v2/speak?model=flux-haley-en&expressivity=2" \
     -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"text": "Your appointment is confirmed for 3pm tomorrow."}' \
     --output audio.mp3
```

## Behavior notes

* **The register shift is intentional behavior.** Moving away from `0` changes pitch range, pacing variation, overall pitch, and timbre (the voice's tonal color) together, so the voice's character audibly changes toward the ends of the range. This is the parameter working as designed, not a side effect.
* **It is not a speed or pitch-shift control.** Negative values do not slow the voice down, and positive values do not speed it up. For speaking rate, use `speed` (on Flux TTS, `0.85` to `1.15` in `0.05` increments).
* **Animated delivery naturally varies more.** At higher values, delivery tends to vary more between generations of the same text; that variation is part of what makes speech sound animated and human. Deepgram's output-consistency characteristics for Flux TTS are measured at the default (`expressivity` omitted or `0`).
* **Effect and risk grow with magnitude.** The further from `0`, the stronger the shift, and the higher the chance of hallucinations or pronunciation errors. The range is kept narrow during beta for this reason; audition any non-default value before production.
* **Comparing text-to-speech providers?** Evaluate Flux TTS at the default (`0`) or above. The calm end deliberately narrows delivery for production contexts like support and IVR, so it does not showcase the model's expressive range.

## FAQ

**Does this change which voice I'm using?**

You are always getting the same underlying voice. That said, `expressivity` does more than adjust energy: pitch and timbre shift too, so the voice's character changes noticeably toward the ends of the range, the way a person sounds different reading a bedtime story versus hosting a game show.

**Can I change it mid-conversation?**

No. `expressivity` is set when you open the connection and applies for the whole session.

**How does it interact with `speed`?**

They are independent controls: `speed` adjusts speaking rate, and `expressivity` adjusts delivery register. They can be combined, but larger values of both together are more likely to sound less natural, so audition combined settings.

**Why does the same value sound different on different voices?**

Each voice has its own character and its own sensitivity to the dial. `0` is every voice's tuned default, but a given step away from `0` lands differently from one voice to the next, so the same value can be a subtle shift on one voice and a pronounced one on another. Audition your specific voice.
