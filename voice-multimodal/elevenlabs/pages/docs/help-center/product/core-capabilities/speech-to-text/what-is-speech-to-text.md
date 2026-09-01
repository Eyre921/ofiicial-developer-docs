---
title: "What is Speech to Text?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/speech-to-text/what-is-speech-to-text.md
path: docs/help-center/product/core-capabilities/speech-to-text/what-is-speech-to-text
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What is Speech to Text?

Speech to Text converts spoken audio into written text. At ElevenLabs, our Speech to Text model is **Scribe**. It allows you to accurately transcribe speech in over 90 languages, making it easy to turn audio into readable, searchable text.

#### **Key features of Scribe**

* Industry-leading accuracy, with 98% accuracy in major languages such as English, French, Italian, Portuguese, Spanish, and German.
* Precise word-level timestamps, so you can see exactly when each word is spoken.
* Smart speaker diarization, which automatically identifies and separates different speakers.
* Dynamic audio tagging to detect non-speech sounds.
* Support for up to 32 speakers while maintaining high accuracy.

## **What’s new in Scribe v2**

Scribe v2 builds on the core model with additional capabilities designed for more demanding use cases.

* **Keyterm prompting**. You can provide up to 100 words or phrases to guide the model
  toward correctly transcribing important terms. Use of keyterm prompting increases the cost by 20%.
* **Entity detection**. You can choose specific categories of information to detect in
  the transcript, such as credit card numbers, names, or medical conditions. Entity detection is
  only available via API, and increases the cost by 30%
* **Smart multi-language support**. You can submit audio containing multiple languages,
  and Scribe v2 will automatically detect and transcribe each one correctly.
* **Improved stability**. Scribe v2 handles pauses, changes in tone, and long silences
  without breaking or losing accuracy.

  \


#### **Which version should you use?**

We recommend **Scribe v2** when high-accuracy transcription is required. It's available through our [website](https://elevenlabs.io/app/speech-to-text) and [API](/docs/api-reference/speech-to-text/convert). When using Speech to Text via our website, Scribe v2 is the default model. 

For real-time use cases, we recommend **Scribe v2 Realtime**, available through [ElevenAgents](https://elevenlabs.io/app/agents) and via [API](/docs/api-reference/speech-to-text/convert). 

For more details, see our [Speech to Text documentation.](/docs/capabilities/speech-to-text)
