---
title: "What is Eleven v3?"
source: https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/what-is-eleven-v3-alpha.md
path: docs/help-center/product/speech-synthesis/text-to-speech/what-is-eleven-v3-alpha
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What is Eleven v3?

Eleven v3 is our latest and most expressive Text to Speech model, offering:

* More human-like generations with higher quality overall

* Support for audio tags

* emotions: \[sad] \[angry] \[happily]

* delivery direction: \[whispers] \[shouts]

* non-verbal reactions: \[laughs]\[clears throat] \[sighs]

* Dialogue mode to support natural sounding audio with multiple speakers

* Support for 70+ languages

It can produce breathtaking output, but its more variable consistency and higher latency mean it’s not suitable for real-time or conversational use cases. For those, we recommend the v2/v2.5 Turbo or Flash models. We’re working on a real-time version of Eleven v3.

You can generate using v3 via API using our [Create speech](/docs/api-reference/text-to-speech/convert) and [Stream speech](/docs/api-reference/text-to-speech/stream) endpoints by specifying model ID `eleven_v3`.

You can also use our [Create dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream dialogue ](/docs/api-reference/text-to-dialogue/stream)endpoints to create a natural sounding dialogue with multiple speakers.

Visit the following resources for more information:

* [Eleven v3 overview](https://elevenlabs.io/v3)
* [Eleven v3 prompting guide](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v3)
