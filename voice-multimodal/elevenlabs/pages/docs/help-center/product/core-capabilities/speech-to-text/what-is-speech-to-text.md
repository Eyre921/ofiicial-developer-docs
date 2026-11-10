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

## **What’s new in Scribe v3**

Scribe v3 is our most accurate Speech to Text model. Compared with Scribe v2, it provides:

* **Fewer transcription errors**. On the FLEURS benchmark across 102 languages, Scribe
  v3 makes 27% fewer word errors than Scribe v2.
* **More accurate speaker labels** on audio with multiple speakers.
* **Number formatting**. Through the API, you can choose whether numbers are written as
  digits or as words.
* **Secondary languages**. Through the API, you can list other languages expected in
  the audio to improve accuracy on mixed-language audio.

Scribe v3 keeps the capabilities introduced in Scribe v2:

* **Keyterm prompting**. You can provide up to 100 words or phrases to guide the model
  toward correctly transcribing important terms. Use of keyterm prompting increases the cost by 20%.
* **Entity detection**. You can choose specific categories of information to detect in
  the transcript, such as credit card numbers, names, or medical conditions. Entity detection is
  only available via API, and increases the cost by 30%
* **Smart multi-language support**. You can submit audio containing multiple languages,
  and Scribe will automatically detect and transcribe each one correctly.
* **Improved stability**. Scribe handles pauses, changes in tone, and long silences
  without breaking or losing accuracy.

  \


#### **Which version should you use?**

We recommend **Scribe v3** (`scribe_v3`) when high-accuracy transcription is required. It's available through our [website](https://elevenlabs.io/app/speech-to-text) and [API](/docs/api-reference/speech-to-text/convert). When using Speech to Text via our website, Scribe v3 is the default model. Workspaces in [data residency](/docs/overview/administration/data-residency) environments use Scribe v2.

For medical and clinical audio, use **Scribe v2 Medical** (`scribe_v2_medical`) through the same API. It is billed at the same rate as Scribe v2.

For real-time use cases, we recommend **Scribe v3 Live** (`scribe_v3_live`), available via the [realtime API](/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime). [ElevenAgents](https://elevenlabs.io/app/agents) uses Scribe v2 Realtime by default.

For more details, see our [Speech to Text documentation.](/docs/capabilities/speech-to-text)
