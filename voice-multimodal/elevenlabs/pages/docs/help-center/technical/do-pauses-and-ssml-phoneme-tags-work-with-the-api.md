---
title: "Do pauses and SSML phoneme tags work with the API?"
source: https://elevenlabs.io/docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api.md
path: docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Do pauses and SSML phoneme tags work with the API?

**Pauses:**

You can use the break tag when generating audio via the API. This will create an exact and natural pause in the speech. It is not just added silence between words, but the AI has an actual understanding of this syntax and will add a natural pause.

The syntax for the break tag is `<break time="1.5s" />` and the AI can handle pauses of up to 3 seconds in length.

All of our models, **with the exception of [Eleven v4](/docs/overview/capabilities/text-to-speech/eleven-v4) and Eleven v3**, support SSML break tags, and these can be used when generating audio via the API.

If you are using **Eleven v4** or **Eleven v3**, use audio tags, punctuation, and text structure to control pauses. See [Prompting Eleven v4](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4).

For more information, please see the [Pause](/docs/overview/capabilities/text-to-speech/best-practices#pauses) section of our [guide to Prompting](/docs/overview/capabilities/text-to-speech/best-practices).

**Phonemes:**

[Eleven v4](/docs/overview/capabilities/text-to-speech/eleven-v4) has improved native support for IPA. For more information, see [IPA with Eleven v4](/docs/overview/capabilities/text-to-speech/best-practices#ipa-with-eleven-v4).

Our **Eleven Flash v2** and **Eleven Turbo v2** models support **SSML phoneme tags**, and these can be used when generating audio via the API using these models.

Please note that phonemes are available only for English language models and are currently not supported for other languages.

For full details on how to use phoneme tags, please see the [Pronunciation](/docs/overview/capabilities/text-to-speech/best-practices#pronunciation) section of our guide to Prompting.
