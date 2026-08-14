---
title: "How can I add pauses?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-can-i-add-pauses.md
path: docs/help-center/product/core-capabilities/text-to-speech/how-can-i-add-pauses
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How can I add pauses?

There are a few ways to introduce a pause or break and influence the rhythm and cadence of the speaker. The method you use depends on the model.

## Audio tags (Eleven v3 only)

With Eleven v3, use audio tags and punctuation to control pacing and delivery. Eleven v3 does not support SSML break tags.

See the [Eleven v3 prompting guide](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v3) for guidance on prompting pauses and delivery with v3.

## Break tags (Multilingual v2, Flash v2, and Flash v2.5)

The most consistent way to add a pause on Multilingual v2, Flash v2, and Flash v2.5 is with the SSML break tag syntax `<break time="1.5s" />`. This creates an exact and natural pause in the speech. It is not just inserted silence between words—the model understands the syntax and adds a natural pause.

How the model handles these pauses can vary. The voice used plays a pivotal role in the output. Some voices, those trained with a few "uh"s and "ah"s, may insert those vocal mannerisms during pauses, like a real speaker might.

An example could look like this:

"Give me one second to think about it." `<break time="1.0s" />` "Yes, that would work."

Break time should be described in seconds. The AI can handle pauses of up to 3 seconds and can be used in Text to Speech and via the API.

If you use an excessive number of SSML breaks in your text, it might cause issues. The speech might speed up, or the audio might introduce more noise and other artifacts. We are working on resolving this.

## Punctuation

These options are less consistent than break tags or audio tags, but can still influence pacing.

A simple dash `-` or the em-dash `—` often works well. You can add multiple dashes such as `-- --` for a longer pause.

"It - is - getting late."

Ellipsis `...` can sometimes add a pause between words, but it usually also adds some hesitation or nervousness to the voice that might not always fit.

"I... yeah, I guess so..."
