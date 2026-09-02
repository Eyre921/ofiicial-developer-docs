---
title: "Voice Agent TTS Controls"
source: https://developers.deepgram.com/docs/voice-agent-tts-controls.md
path: docs/voice-agent-tts-controls
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Voice Agent TTS Controls

If you're building with the [Voice Agent API](/docs/voice-agent), Deepgram's [TTS voice controls](/docs/tts-voice-controls) — speed, expressivity, pronunciation, and pacing — work inside your agent pipeline. Where you apply each control depends on what it does and what context the decision needs.

Speed applies to both [Flux TTS](/docs/flux-tts/overview) (`agent.speak.provider.version` `v2`) and Aura (`v1`), with different accepted values for each. Expressivity applies to Flux TTS only. The pronunciation and pacing guidance applies to every TTS model you can use with the Voice Agent, though the inline pronunciation control syntax itself works with Aura (`v1`) only.

## Where each control belongs

| Control                | Applies to        | Apply at          | Why                                                                                |
| ---------------------- | ----------------- | ----------------- | ---------------------------------------------------------------------------------- |
| Speed                  | Flux TTS and Aura | Session settings  | A single rate applies to the whole conversation.                                   |
| Expressivity           | Flux TTS (`v2`)   | Session settings  | The delivery register is a property of the agent, not of one turn.                 |
| Pronunciation override | All TTS models    | LLM system prompt | Needs sentence-level context to disambiguate heteronyms.                           |
| Pause and pacing       | All TTS models    | LLM system prompt | Voice models shape pacing from the text they receive; the specifics vary by model. |

## Speed: configure once at the session level

Speed is a session-level setting on the agent's `speak` provider, and both Deepgram TTS families support it. Configure it when you initialize the agent, and every response from the agent uses that rate.

```json title="Flux TTS (v2)"
{
  "type": "Settings",
  "agent": {
    "speak": {
      "provider": {
        "type": "deepgram",
        "version": "v2",
        "model": "flux-kit-en",
        "speed": 1.05
      }
    }
  }
}
```

```json title="Aura (v1)"
{
  "type": "Settings",
  "agent": {
    "speak": {
      "provider": {
        "type": "deepgram",
        "model": "aura-2-thalia-en",
        "speed": 0.9
      }
    }
  }
}
```

Each family accepts a different range, and the default is `1.0` for both:

* **Flux TTS** accepts `0.5` to `1.5` in `0.05` increments.
* **Aura** accepts any float between `0.7` and `1.5`. For Spanish voices the recommended range is `0.9`–`1.5`; values below `0.9` may introduce disfluencies.

See [TTS Models](/docs/voice-agent-tts-models#deepgram-tts-models) for the full parameter reference and [TTS Voice Controls](/docs/tts-voice-controls#speed-control) for the underlying behavior.

A consistent session-level speed is useful for agents that serve accessibility-sensitive audiences, or any conversation where pacing should stay steady throughout the call.

The `speed` parameter is also supported for Cartesia TTS in Voice Agent sessions. See [Deepgram-managed Cartesia TTS models](/docs/voice-agent-tts-models#deepgram-managed-cartesia-tts-models) for the accepted values.

## Expressivity: set the delivery register at the session level

`agent.speak.provider.expressivity` shifts a Flux TTS voice's delivery along a calm to animated axis. Like speed, it is a session-level setting on the `speak` provider, and the value applies to every response the agent speaks.

```json title="Flux TTS (v2)"
{
  "type": "Settings",
  "agent": {
    "speak": {
      "provider": {
        "type": "deepgram",
        "version": "v2",
        "model": "flux-kit-en",
        "expressivity": -1
      }
    }
  }
}
```

It accepts the whole numbers `-2` to `2` and defaults to `0`, the voice's tuned delivery. Negative values produce calmer, steadier delivery; positive values produce more animated delivery with a wider pitch range. Every Flux voice supports it.

Match the register to the conversation your agent handles: the calm end suits support, de-escalation, healthcare, and IVR, and the animated end suits consumer, entertainment, and outbound engagement. Because each voice has its own character, the same value lands differently from one voice to the next.

`expressivity` is a beta parameter. `0` is the only value validated for production, and moving away from it raises the chance of hallucinations and pronunciation errors, so test the value you plan to ship and re-check it after model updates.

Expressivity is not a speed control: it changes pitch range, pacing variation, and timbre together rather than the speaking rate. Combine it with `speed` when you need both, and test the combination.

For value-by-value guidance, see [Expressivity](/docs/tts-expressivity), and [TTS Models](/docs/voice-agent-tts-models#flux-tts) for the parameter reference.

## Pronunciation and pacing: handle them in the LLM prompt

Pronunciation overrides and pause cues are most effective when the LLM produces them — not when they're added downstream — because both depend on the meaning of the surrounding text. The text your LLM emits is the text the voice model speaks, so pacing through punctuation works with every TTS model you can use with the Voice Agent, Deepgram and third-party alike.

* **Pronunciation needs context to handle heteronyms.** Words like *lead* (the metal vs. to guide), *read* (present vs. past), *bass* (fish vs. instrument), or *Polish* vs. *polish* are spelled identically but pronounced differently. Only the LLM, which has the full conversational context, can decide which IPA override to apply for a given utterance. A static lexicon applied after the fact will mispronounce these words whenever the wrong sense is meant.
* **Pacing needs to match what's being said.** Voice models take their pacing cues from the text they receive, so asking the LLM to produce well-punctuated output is more reliable than post-processing a flat string. Aura-2 responds to punctuation in documented ways: commas and periods produce short pauses, ellipses (`...`) produce longer ones, and digits separated by periods slow down readback for phone numbers, account numbers, and IDs. Other models interpret punctuation differently — check your provider's documentation. See [Text to Speech Prompting](/docs/text-to-speech-prompting) for Aura-2's full set of pacing techniques.

Put your pronunciation map and pacing rules in the system prompt and the Voice Agent passes the LLM's output through to the voice model unchanged.

### Example system prompt snippet

The inline pronunciation block below applies to Aura (`v1`) voices. With Flux TTS, keep the digit-grouping pacing rules and replace the inline block with plain-language pronunciation instructions: Flux TTS rejects text containing inline controls, ending the session with a `DATA-0002` error.

```text
When saying the following terms, use these inline pronunciation controls so the
voice model produces the correct phonetic output:

- dupilumab → \{"word": "dupilumab", "pronounce": "duːˈpɪljuːmæb"\}
- adalimumab → \{"word": "adalimumab", "pronounce": "ˌædəˈlɪmjuːmæb"\}

When reading back phone numbers, account numbers, or order IDs, group digits in
twos or threes and separate each group with a period to introduce a short pause.
For example, prefer "555. 867. 5309" over "5558675309".
```

This keeps your pronunciation map and pacing rules in the LLM layer, not in a separate lexicon or orchestration config. To add a term, edit the prompt — no redeploy required.

For Aura's override syntax, validation rules, and IPA sourcing tips, see [TTS Voice Controls](/docs/tts-voice-controls#pronunciation-control); check your provider's documentation when using a third-party voice. The curly braces must be escaped (`\{` and `\}`); unescaped braces are treated as plain text and read aloud. Flux TTS does not support inline pronunciation controls in the Voice Agent and rejects any request whose text contains them, ending the session with a `DATA-0002` error — prompt the LLM for the pronunciation you want instead. For pause and pacing techniques, see [Text to Speech Prompting](/docs/text-to-speech-prompting) and [Formatting Text for Aura-2](/docs/improving-aura-2-formatting).
