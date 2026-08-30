---
title: "Why does my voice change accent or language?"
source: https://elevenlabs.io/docs/help-center/troubleshooting/why-does-my-voice-change-accent-or-language.md
path: docs/help-center/troubleshooting/why-does-my-voice-change-accent-or-language
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Why does my voice change accent or language?

The accent used when generating audio comes from the voice that you use. For the best results, we recommend using a voice that has been trained on audio in the language you're generating in. You can use any voice to produce audio in any of the languages we support, but if you use a voice that is not native to the language, it might retain its native accent, or drift between different accents. 

You can either create your own cloned voice, or you can find voices in the Voice Library. You can use the language and accent filters to find suitable voices. You need to select the language before the accent filter will become available.

 

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a20116d23eec58c7eb81720fddd62551a68a4325a9267e09b8c447c3e7ac16c2/assets/images/help-center/troubleshooting/why-does-my-voice-change-accent-or-language.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260830T071001Z&X-Amz-Expires=604800&X-Amz-Signature=6f7a6ccb4eccd20e92ebea1e551f9267479774341960404f38bc6df4166a4242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

 

Another possible cause of your audio being spoken with an English accent is if you are generating audio in another language, but using a model that only supports English (Flash v2 or Turbo v2).  This can be resolved by switching to one of our multilingual models (Multilingual v2 or Flash v2.5).
