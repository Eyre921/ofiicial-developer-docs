---
title: "How do I use the Pronunciations Editor in Studio?"
source: https://elevenlabs.io/docs/help-center/product/studio/studio/how-do-i-use-the-pronunciations-editor-in-studio.md
path: docs/help-center/product/studio/studio/how-do-i-use-the-pronunciations-editor-in-studio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I use the Pronunciations Editor in Studio?

Sometimes you may want to specify the pronunciation of certain words, such as character or brand names, or specify how acronyms should be read. You can use the <strong>Pronunciations editor</strong> to add rules about how specified words should be pronounced, either using a phonetic alphabet (phoneme tags) or word substitutions (alias tags).

Phoneme tags are only compatible with Eleven Flash v2 and Eleven Turbo v2.

These rules will be saved to a Pronunciation Dictionary which will be connected to your project. Whenever one of these words is encountered in a project, the AI will pronounce the word using the specified replacement.

You can add aliases and phonemes from directly within Studio by clicking the <strong>Open pronunciations editor</strong> button.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/08c03ab47aca4dd436e2c1380f41838bfbdd5b23fa7c4ca2ef8a7055cf676013/assets/images/help-center/product/studio/studio-pronunciations.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113448Z&X-Amz-Expires=604800&X-Amz-Signature=f9aa1568346ff76e12685232afc2b161fd875be12a0bd5859569e448f406ffbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

If you do this while you have a word selected, this word will automatically populate the input field. Otherwise, you can enter the word yourself. You can use the Play button in the Output to preview how it will sound.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/af89c0002944f33b1982157fd8fc0070201ade4b282bf1d39cffe9a731e1c97e/assets/images/help-center/product/studio/studio-pronunciations-editor.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113448Z&X-Amz-Expires=604800&X-Amz-Signature=b2619ba325e82a1bab55a6b6c90d182e8f4851f8f65052e609c045002931a5ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

When you add a new rule, you can either select an existing dictionary to add the rule to, or create a new dictionary. If you add the rule to an existing dictionary, this will automatically connect it to your project.
