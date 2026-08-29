---
title: "How do I select the language and accent?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-i-select-the-language-and-accent.md
path: docs/help-center/product/core-capabilities/text-to-speech/how-do-i-select-the-language-and-accent
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I select the language and accent?

<strong>
  Language when generating via the website
</strong>

When you generate audio on the ElevenLabs website, our AI automatically detects the language based on the context of the text of your prompt. This means that it's best to avoid using multiple languages in a single prompt, as this can cause confusion about which language should be used. At the moment, it isn’t possible to specify a language when generating on the website. 

 

<strong>
  Language when generating via API
</strong>

If you generate audio through the API, you can manually specify the language of your prompt using the `language_code` parameter. This is an optional parameter that accepts ISO 639-1 language codes. 

This can be useful for short or ambiguous prompts, such as when the text includes only numbers. Specifying the language ensures the normalizer applies the correct rules for that language.

For more information on normalization, see [this article. ](/docs/help-center/product/core-capabilities/text-to-speech/why-are-numbers-dates-symbols-and-acronyms-not-properly-pronounced-or-spoken-in-the-correct-language)

 

<strong>
  Accent
</strong>

The accent that is used for your generation comes from the voice you're using. If you use a voice that hasn’t been trained on the language you’re generating, you may notice a slight accent from the voice’s original language.

For the best results, we recommend using a voice that has been trained on audio in the language you’re generating, with your preferred accent. This helps the AI understand pronunciation and intonation more accurately.

This is especially important for languages that are similar or share many common words. Choosing a voice trained on the correct language ensures that the AI uses the correct pronunciation and accent.

You can:

* <strong>Create a cloned voice</strong> using audio in your preferred language and accent.
* <strong>Browse the Voice Library</strong> and use the search filters to find suitable voices that
  match your needs.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b3e4de803d69ffbd3aed314c2c5f9defa87d3d7fd6fc1931a4a02278041c1c43/assets/images/help-center/product/core-capabilities/text-to-speech/how-do-i-select-the-language-and-accent.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260829%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260829T190309Z&X-Amz-Expires=604800&X-Amz-Signature=dbbc56b4e469b86964adae81bf59db1d3e9067a78ddf6372c2973a929959a278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />
