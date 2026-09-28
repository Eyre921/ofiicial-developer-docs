---
title: "What is Eleven v4?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4.md
path: docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What is Eleven v4?

> **Info**
>
> We recommend switching to Eleven v4 and testing it with your own content.

Eleven v4 is our latest and most advanced Text to Speech model, and the first in a new generation of models. It improves output quality, voice accuracy, emotion, audio tags, and language coverage compared with Eleven v3.

Voice cloning accuracy takes a major step forward with Eleven v4. Cloned voices capture the source voice's characteristics — timbre, cadence, and delivery — more faithfully than any previous model.

Instant Voice Clones (IVCs) are more accurate than ever in Eleven v4. They capture the defining characteristics of a source voice more faithfully, making it easier to create a convincing clone quickly from a short audio sample.

Professional Voice Clones (PVCs) are fully supported in Eleven v4. They build on the same advances in voice accuracy, offering a more faithful reproduction of the source voice for workflows that require the highest level of consistency and control.

Eleven v4 comes in two variants, so you can choose the right balance of quality and speed for your use case:

* **Eleven v4** (`eleven_v4`) — our highest-quality model, ideal for content creation, audiobooks, character voiceovers, and any use case where quality is the top priority.
* **Eleven v4 Turbo** (`eleven_v4_turbo`) — extremely high quality while retaining impressively low latency, purpose-built for real-time use cases like conversational agents and interactive voice experiences.

Both variants use two voice settings: Stability and Similarity. Style and Speed sliders are not available in Eleven v4, and SSML is not supported.

When the language you're generating matches the language of your reference voice, the original accent is preserved exactly as before. When the language you're generating is different from the reference voice's language, Eleven v4 generates fluent, natural-sounding speech in the target language — rather than carrying over the reference voice's accent from its original language.

You can generate with [Create speech](/docs/api-reference/text-to-speech/convert) and [Stream speech](/docs/api-reference/text-to-speech/stream) using model ID `eleven_v4`. For multiple speakers, use [Create dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream dialogue](/docs/api-reference/text-to-dialogue/stream).

For cloning, accents, comparisons, and the full description, see [Eleven v4](/docs/overview/capabilities/text-to-speech/eleven-v4). For tags and prompting, see [Prompting Eleven v4](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4).
