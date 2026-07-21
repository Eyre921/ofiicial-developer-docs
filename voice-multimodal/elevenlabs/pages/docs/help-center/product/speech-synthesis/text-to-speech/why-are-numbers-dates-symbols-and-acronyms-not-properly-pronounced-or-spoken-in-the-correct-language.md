---
title: "Why are numbers, dates, symbols and acronyms not properly pronounced or spoken in the correct language?"
source: https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/why-are-numbers-dates-symbols-and-acronyms-not-properly-pronounced-or-spoken-in-the-correct-language.md
path: docs/help-center/product/speech-synthesis/text-to-speech/why-are-numbers-dates-symbols-and-acronyms-not-properly-pronounced-or-spoken-in-the-correct-language
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why are numbers, dates, symbols and acronyms not properly pronounced or spoken in the correct language?

Numbers, dates, symbols and acronyms can present a challenge to the AI, as there are often multiple ways that they could be delivered correctly. This can also depend on the language that is being used, for example, “11” could be read as "Eleven," but it could also be "Once" in Spanish or "Elf" in German.  

There are several ways you can ensure the correct delivery of numbers, dates, acronyms and symbols.

 

<strong>
  Write out fully, in words
</strong>

For the best results, we recommend writing numbers, acronyms, dates and symbols fully, in words, in the way that you would like the AI to deliver them. This ensures that the AI has the most context so that it will provide the correct output. For example, for “\$100”, we would recommend writing either "a hundred dollars" or "one hundred dollars" to ensure you get the result you would like.  

 

<strong>
  Using an LLM
</strong>

If you are using a large language model to generate your text prompts, for example, when using [ElevenAgents](/docs/conversational-ai/overview), you can prompt the model to always write numbers, dates, symbols, and acronyms out in words in whichever way you would prefer them to be delivered by the AI.

 

<strong>
  Normalization
</strong>

If you’re generating via the API, you can specify whether to apply text normalization using the `apply_text_normalization` parameter. Text normalization spells out numbers and dates to ensure better pronunciation  This option does add latency as the normalization process takes additional processing time.

The`apply_text_normalization` parameter has three modes:

* on, which means it is always applied
* off, which means it is never applied
* auto, which means that the AI will automatically decide when to apply text normalization

You can also specify the language of your prompt using the `language_code`parameter. This is an optional parameter that accepts ISO 639-1 language codes. 

This can be useful for short or ambiguous prompts, such as when the text includes only numbers or symbols. Specifying the language ensures the normalizer applies the correct rules for that language.

For more information, see our <a href="/docs/api-reference/introduction">API reference.</a>

Normalization is enabled by default when generating using Text to Speech via the website.  

In Studio, the default is for normalization to be automatically applied, meaning that the AI will decide when to apply text normalization. You can also set normalization to be always applied - this option is in <strong>Project settings</strong> under the <strong>Advanced</strong> tab.
