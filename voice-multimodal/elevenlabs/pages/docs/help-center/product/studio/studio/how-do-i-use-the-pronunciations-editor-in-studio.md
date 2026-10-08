---
title: "How do I use the Pronunciations Editor in Studio?"
source: https://elevenlabs.io/docs/help-center/product/studio/studio/how-do-i-use-the-pronunciations-editor-in-studio.md
path: docs/help-center/product/studio/studio/how-do-i-use-the-pronunciations-editor-in-studio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I use the Pronunciations Editor in Studio?

Sometimes you may want to specify the pronunciation of certain words, such as character or brand names, or specify how acronyms should be read. You can use the **Pronunciations editor** to add rules about how specified words should be pronounced, either using a phonetic alphabet (phoneme tags) or word substitutions (alias tags).

> **Note**
>
> Phoneme tags are only compatible with Eleven Flash v2.

These rules will be saved to a Pronunciation Dictionary which will be connected to your project. Whenever one of these words is encountered in a project, the AI will pronounce the word using the specified replacement.

You can add aliases and phonemes from directly within Studio by clicking the **Open pronunciations editor** button.

If you do this while you have a word selected, this word will automatically populate the input field. Otherwise, you can enter the word yourself. You can use the Play button in the Output to preview how it will sound.

![Pronunciation dictionaries in Studio](/docs/_fern-img/529a45f8a99dd533047caade26211cacfae53245a43f791efe34d8723555619c.webp)

When you add a new rule, you can either select an existing dictionary to add the rule to, or create a new dictionary. If you add the rule to an existing dictionary, this will automatically connect it to your project.
