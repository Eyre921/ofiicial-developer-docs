---
title: "Voice Agent TTS Controls"
source: https://developers.deepgram.com/docs/voice-agent-tts-controls.md
path: docs/voice-agent-tts-controls
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Voice Agent TTS Controls

If you're building with the [Voice Agent API](/docs/voice-agent), Aura-2's [TTS voice controls](/docs/tts-voice-controls) — speed, pronunciation, and pacing — work inside your agent pipeline. Where you apply each control depends on what it does and what context the decision needs.

These controls apply to Aura (`agent.speak.provider.version` `v1`) only. [Flux TTS](/docs/flux-tts/overview) (Early Access, `agent.speak.provider.version` `v2`) does not support the speed, pronunciation, or pacing controls described here.

## Where each control belongs

| Control                | Apply at          | Why                                                             |
| ---------------------- | ----------------- | --------------------------------------------------------------- |
| Speed                  | Session settings  | A single rate applies to the whole conversation.                |
| Pronunciation override | LLM system prompt | Needs sentence-level context to disambiguate heteronyms.        |
| Pause and pacing       | LLM system prompt | Aura-2 shapes pacing directly from the punctuation it receives. |

## Speed: configure once at the session level

Speed is a session-level setting on the agent's `speak` provider. Configure it when you initialize the agent, and every response from the agent uses that rate. It applies to Aura (`agent.speak.provider.version` `v1`) only — [Flux TTS](/docs/flux-tts/overview) (Early Access, `v2`) does not support `speed`.

```json
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

`speed` accepts a float between `0.7` and `1.5` (default `1.0`). For Spanish voices the recommended range is `0.9`–`1.5`; values below `0.9` may introduce disfluencies. See [TTS Models](/docs/voice-agent-tts-models#deepgram-tts-models) for the full parameter reference and [TTS Voice Controls](/docs/tts-voice-controls#speed-control) for the underlying behavior.

A consistent session-level speed is useful for agents that serve accessibility-sensitive audiences, or any conversation where pacing should stay steady throughout the call.

The `speed` parameter is also supported for Cartesia TTS in Voice Agent sessions. See [Deepgram-managed Cartesia TTS models](/docs/voice-agent-tts-models#deepgram-managed-cartesia-tts-models) for the accepted values.

## Pronunciation and pacing: handle them in the LLM prompt

Pronunciation overrides and pause cues are most effective when the LLM produces them — not when they're added downstream — because both depend on the meaning of the surrounding text.

* **Pronunciation needs context to handle heteronyms.** Words like *lead* (the metal vs. to guide), *read* (present vs. past), *bass* (fish vs. instrument), or *Polish* vs. *polish* are spelled identically but pronounced differently. Only the LLM, which has the full conversational context, can decide which IPA override to apply for a given utterance. A static lexicon applied after the fact will mispronounce these words whenever the wrong sense is meant.
* **Pacing needs to match what's being said.** Aura-2 takes pacing cues directly from punctuation: commas and periods produce short pauses, ellipses (`...`) produce longer ones, and digits separated by periods slow down readback for phone numbers, account numbers, and IDs. Asking the LLM to produce well-punctuated output is more reliable than post-processing a flat string. See [Text to Speech Prompting](/docs/text-to-speech-prompting) for the full set of pacing techniques Aura-2 supports.

Put your pronunciation map and pacing rules in the system prompt and the Voice Agent passes the LLM's output through to Aura-2 unchanged.

### Example system prompt snippet

```text
When saying the following terms, use these inline pronunciation controls so the
voice model produces the correct phonetic output:

- dupilumab → {"word": "dupilumab", "pronounce": "duːˈpɪljuːmæb"}
- adalimumab → {"word": "adalimumab", "pronounce": "ˌædəˈlɪmjuːmæb"}

When reading back phone numbers, account numbers, or order IDs, group digits in
twos or threes and separate each group with a period to introduce a short pause.
For example, prefer "555. 867. 5309" over "5558675309".
```

This keeps your pronunciation map and pacing rules in the LLM layer, not in a separate lexicon or orchestration config. To add a term, edit the prompt — no redeploy required.

For the full pronunciation override syntax, validation rules, and IPA sourcing tips, see [TTS Voice Controls](/docs/tts-voice-controls#pronunciation-control). For pause and pacing techniques, see [Text to Speech Prompting](/docs/text-to-speech-prompting) and [Formatting Text for Aura-2](/docs/improving-aura-2-formatting).
