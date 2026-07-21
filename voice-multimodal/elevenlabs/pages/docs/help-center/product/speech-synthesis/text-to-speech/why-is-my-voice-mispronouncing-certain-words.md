---
title: "Why is my voice mispronouncing certain words?"
source: https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/why-is-my-voice-mispronouncing-certain-words.md
path: docs/help-center/product/speech-synthesis/text-to-speech/why-is-my-voice-mispronouncing-certain-words
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why is my voice mispronouncing certain words?

Mispronunciations can happen for a few different reasons. The most common one is that the word is just misspelled. The AI will not try to correct any words that are misspelled, and it will try to read them exactly as they are written. So it's important to double-check and make sure that the text is proofread and finished before having the AI read it.

If you want to force a certain pronunciation, you can use SSML phoneme tags with our English V1 and Turbo V2 models. You can find out more about this in our [guide to Prompting.](/docs/best-practices/prompting/controls#pronunciation)  

Sometimes, the AI might mispronounce words or have a strange accent that is not the one you are expecting. This can happen for a few reasons, and in most cases, it's very voice-dependent and language-dependent. The best way to ensure the correct accent and pronunciation is to clone a voice with the correct accent and pronunciation. This will give the AI the most context when generating the voiceover.

The language is specified by the text, and the accent is specified by the voice. So if you're writing in a language that might share a lot of common words or is fairly closely related to another language, the AI might have a hard time understanding how to pronounce certain words or switch between accents.

However, under certain circumstances, the AI might mispronounce words that are written correctly, even in English. This seems to be highly dependent on the voice used and the text used, but should be a rare occurrence.
