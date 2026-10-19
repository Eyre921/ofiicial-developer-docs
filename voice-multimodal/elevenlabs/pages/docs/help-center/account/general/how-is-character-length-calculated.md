---
title: "How is character length calculated?"
source: https://elevenlabs.io/docs/help-center/account/general/how-is-character-length-calculated.md
path: docs/help-center/account/general/how-is-character-length-calculated
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How is character length calculated?

Text to Speech requests are charged based on character count. Every letter, number, punctuation mark, and space in your input text counts toward the total.

Several factors can affect the number of characters counted for a request:

* **Pronunciation dictionaries:** Custom pronunciation rules applied to your text can affect the final character count.
* **Tags:** SSML and audio tags count toward the request's character total.

The cost of a generation is converted to credits. The conversion rate depends on the model and whether you generate through the website or API. For current rates, see [ElevenCreative](https://elevenlabs.io/pricing?price.section=text_to_speech#pricing-table) and [ElevenAPI](https://elevenlabs.io/pricing/api).
