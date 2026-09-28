---
title: "What is Eleven v3?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v3-alpha.md
path: docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v3-alpha
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What is Eleven v3?

> **Info**
>
> We recommend switching to [Eleven v4](/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4) and testing it
> with your own content. Many of the prompting techniques for [Eleven v4](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4) also apply to
> Eleven v3.

Eleven v3 is an emotionally rich, expressive Text to Speech model. It produces natural, life-like speech with high emotional range and contextual understanding across 70+ languages.

Eleven v3 offers:

* Support for audio tags
  * emotions: `[sad]` `[angry]` `[happily]`
  * delivery direction: `[whispers]` `[shouts]`
  * non-verbal reactions: `[laughs]` `[clears throat]` `[sighs]`
* Dialogue mode for natural-sounding audio with multiple speakers
* Support for 70+ languages

This model works well for character discussions, audiobook narration, and emotional dialogue.

You can generate using v3 via API using our [Create speech](/docs/api-reference/text-to-speech/convert) and [Stream speech](/docs/api-reference/text-to-speech/stream) endpoints by specifying model ID `eleven_v3`.

You can also use our [Create dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream dialogue](/docs/api-reference/text-to-dialogue/stream) endpoints to create a natural sounding dialogue with multiple speakers.

Visit the following resources for more information:

* [Models](/docs/overview/models#eleven-v3)
* [Prompting guide](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4)
