---
title: "Why does my voice change accent or language?"
source: https://elevenlabs.io/docs/help-center/troubleshooting/why-does-my-voice-change-accent-or-language.md
path: docs/help-center/troubleshooting/why-does-my-voice-change-accent-or-language
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why does my voice change accent or language?

The accent used when generating audio comes from the voice that you use. For the best results, we recommend using a voice that has been trained on audio in the language you're generating in. You can use any voice to produce audio in any of the languages we support, but if you use a voice that is not native to the language, it might retain its native accent, or drift between different accents. 

You can either create your own cloned voice, or you can find voices in the Voice Library. You can use the language and accent filters to find suitable voices. You need to select the language before the accent filter will become available.

 

<img src="https://help.elevenlabs.io/hc/article_attachments/31114260772241" alt="" />

 

Another possible cause of your audio being spoken with an English accent is if you are generating audio in another language, but using a model that only supports English (Flash v2 or Turbo v2).  This can be resolved by switching to one of our multilingual models (Multilingual v2 or Flash v2.5).
