---
title: "How do audio tags work with Eleven v3 and v4?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-and-v4.md
path: docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-and-v4
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do audio tags work with Eleven v3 and v4?

[Eleven v4](/docs/overview/capabilities/text-to-speech/eleven-v4) and Eleven v3 support audio tags. We recommend Eleven v4. Wrap a short instruction in square brackets and place it in the text where the delivery should change. The same tags work with both models.

* Emotions: `[curious]` `[crying]` `[mischievously]`
* Delivery direction: `[whispers]` `[shouts]`
* Human reactions: `[laughs]` `[clears throat]` `[sighs]`

For more detailed information, see our [prompting guide](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4).

You can generate via API using our [Create speech](/docs/api-reference/text-to-speech/convert) and [Stream speech](/docs/api-reference/text-to-speech/stream) endpoints by specifying model ID `eleven_v4` or `eleven_v3`.

You can also use our [Create dialogue](/docs/api-reference/text-to-dialogue/convert) and [Stream dialogue](/docs/api-reference/text-to-dialogue/stream) endpoints to create a natural sounding dialogue with multiple speakers.

For real-time applications, Eleven v4 Turbo (`eleven_v4_turbo`) also supports audio tags.

Visit the following resources for more information:

* [Models](/docs/overview/models)
* [Prompting guide](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4)
