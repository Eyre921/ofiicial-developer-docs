---
title: "How do I use the Pronunciations Editor in Studio?"
source: https://elevenlabs.io/docs/help-center/product/studio/studio/how-do-i-use-the-pronunciations-editor-in-studio.md
path: docs/help-center/product/studio/studio/how-do-i-use-the-pronunciations-editor-in-studio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I use the Pronunciations Editor in Studio?

Sometimes you may want to specify the pronunciation of certain words, such as character or brand names, or specify how acronyms should be read. You can use the **Pronunciations editor** to add rules about how specified words should be pronounced, either using a phonetic alphabet (phoneme tags) or word substitutions (alias tags).

Phoneme tags are only compatible with Eleven Flash v2 and Eleven Turbo v2.

These rules will be saved to a Pronunciation Dictionary which will be connected to your project. Whenever one of these words is encountered in a project, the AI will pronounce the word using the specified replacement.

You can add aliases and phonemes from directly within Studio by clicking the **Open pronunciations editor** button.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/08c03ab47aca4dd436e2c1380f41838bfbdd5b23fa7c4ca2ef8a7055cf676013/assets/images/help-center/product/studio/studio-pronunciations.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T113452Z&X-Amz-Expires=604800&X-Amz-Signature=7b645b9bd4b5f790d46bc82bf90200368602c79c38161194ca5d97ecfd1018f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you do this while you have a word selected, this word will automatically populate the input field. Otherwise, you can enter the word yourself. You can use the Play button in the Output to preview how it will sound.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/af89c0002944f33b1982157fd8fc0070201ade4b282bf1d39cffe9a731e1c97e/assets/images/help-center/product/studio/studio-pronunciations-editor.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T113452Z&X-Amz-Expires=604800&X-Amz-Signature=c7c20f6957e75f7659adf2d80159db8e79b2d9dfd9d814d482cb2f1a393da268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When you add a new rule, you can either select an existing dictionary to add the rule to, or create a new dictionary. If you add the rule to an existing dictionary, this will automatically connect it to your project.
