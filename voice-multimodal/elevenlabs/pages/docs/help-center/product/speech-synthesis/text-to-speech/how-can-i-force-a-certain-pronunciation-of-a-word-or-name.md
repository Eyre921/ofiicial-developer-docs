---
title: "How can I force a certain pronunciation of a word or name?"
source: https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/how-can-i-force-a-certain-pronunciation-of-a-word-or-name.md
path: docs/help-center/product/speech-synthesis/text-to-speech/how-can-i-force-a-certain-pronunciation-of-a-word-or-name
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How can I force a certain pronunciation of a word or name?

If you want to force a certain pronunciation, you can use SSML phoneme tags. We support both IPA and CMU. However, we have found that CMU, with the current implementation, seems to be a bit more predictable, consistent, and better overall. You can find out more about this in our [guide to Prompting.](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v3)

This is available on the following models:

* English v1
* Turbo v2
* Flash v2

Alternatively, a workaround is to find an alternative spelling and write a word more phonetically. You can employ various tricks such as capital letters, dashes, apostrophes, or even single quotation marks around a single letter or letters.

As an example, a word like "trapezii" could be spelt "trapezIi" to put more emphasis on the "ii" of the word.
