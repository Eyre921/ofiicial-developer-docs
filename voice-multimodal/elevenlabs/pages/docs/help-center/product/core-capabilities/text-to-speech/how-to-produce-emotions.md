---
title: "How to produce emotions?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-to-produce-emotions.md
path: docs/help-center/product/core-capabilities/text-to-speech/how-to-produce-emotions
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How to produce emotions?

The model is sensitive to the wider situation surrounding each utterance - it assesses whether something makes sense by how it ties to preceding and succeeding text. This zoomed-out perspective allows it to intonate longer fragments properly by overlaying a particular train of thought stretching multiple sentences with a unifying emotional pattern.

Tips for producing emotions:

* Context is key for generating specific emotions. If you input laughing or funny text, you might get a happy output. The same applies for anger, sadness, and other emotions — setting the context is key.
* Punctuation and voice settings play the leading role in how the output is delivered.
* Add emphasis by putting the relevant words or phrases in quotation marks.
* For speech generated using a cloned voice, the speaking style in the samples you upload for cloning is replicated in the output. If the speech in the uploaded sample is monotone, the model will struggle to produce expressive output.

With Eleven v3, you can also use [audio tags](/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-alpha) to control emotion and delivery more directly, for example `[happy]`, `[sad]`, `[angry]`, `[whispers]`, and `[laughs]`. See the [Eleven v3 prompting guide](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v3) for more detail.

These tips help guide emotional delivery but do not guarantee a specific result.
