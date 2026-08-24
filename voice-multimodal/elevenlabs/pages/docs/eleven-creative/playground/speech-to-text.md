---
title: "Speech to Text"
source: https://elevenlabs.io/docs/eleven-creative/playground/speech-to-text.md
path: docs/eleven-creative/playground/speech-to-text
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Speech to Text

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0c8dba5ebba5f9a72541640bb4a9c9fac7bd265df0549f80cb5557c022f85b6f/assets/images/product-guides/speech-to-text/speech-to-text-product-feature.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T100017Z&X-Amz-Expires=604800&X-Amz-Signature=b70f68119fe522fe47ba52155801ccd7fdbcf4a4a7406810d71b5cf7d9ea6a0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Text to Speech product feature" />

## Overview

With speech to text, you can transcribe spoken audio into text with state of the art accuracy. With automatic language detection, you can transcribe audio in a multitude of languages.

## Creating a transcript

#### Upload audio

In the ElevenLabs dashboard, navigate to the Speech to Text page and click the "Transcribe files" button. From the modal, you can upload an audio or video file to transcribe.

![Speech to Text upload](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/596c6fceacbe4659b583db3ba6e2ba0c1f55177cf870654ae5ded693f1ffe43b/assets/images/product-guides/speech-to-text/speech-to-text-modal.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T100017Z&X-Amz-Expires=604800&X-Amz-Signature=64161a6c0bcd29fd6e01765acdcaf8a2afa225c30016b271ceeb39390015c86d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Select options

* Select the primary language of the audio if you know it. You can leave this set to "Detect", and any languages within the audio will be automatically detected.

* Choose whether you wish to tag audio events like laughter or applause using the "Tag audio events" toggle.

* Keyterm prompting allows you to add up to 1000 words or phrases to bias the model towards transcribing them. This is useful for transcribing specific words or sentences that are not common in the audio, such as product names, names, or other specific terms.

When you're ready, click the "Upload files" button to submit.

#### View results

Click on the name of the audio file you uploaded in the center pane to view the results. You can click on a word to start a playback of the audio at that point.

Click the "Export" button in the top right to download the results in a variety of formats.

## Transcript Editor

Once you've created a transcript, you can edit it in our Transcript Editor. Learn more about it [in this guide](/docs/eleven-creative/products/transcripts).

## FAQ

<tbody>
  <tr>
    <td>
      #### Can I upload video files?

      Yes, the tool supports uploading both audio and video files. The maximum file size for either is 3GB.
    </td>
  </tr>

  <tr>
    <td>
      #### Can I rename speakers?

      ### Renaming speakers

      Yes, you can rename speakers by clicking the "edit" button next to the "Speakers" label.
    </td>
  </tr>

  <tr>
    <td>
      #### What is Speech to Text?

      Speech to Text converts spoken audio into written text. At ElevenLabs, our Speech to Text model is <strong>Scribe</strong>. It allows you to accurately transcribe speech in over 90 languages, making it easy to turn audio into readable, searchable text.

      #### <strong>Key features of Scribe</strong>

      * Industry-leading accuracy, with 98% accuracy in major languages such as English, French, Italian, Portuguese, Spanish, and German.
      * Precise word-level timestamps, so you can see exactly when each word is spoken.
      * Smart speaker diarization, which automatically identifies and separates different speakers.
      * Dynamic audio tagging to detect non-speech sounds.
      * Support for up to 32 speakers while maintaining high accuracy.

      ## <strong>What’s new in Scribe v2</strong>

      Scribe v2 builds on the core model with additional capabilities designed for more demanding use cases.

      * <strong>Keyterm prompting</strong>. You can provide up to 100 words or phrases to guide the model
        toward correctly transcribing important terms. Use of keyterm prompting increases the cost by 20%.
      * <strong>Entity detection</strong>. You can choose specific categories of information to detect in
        the transcript, such as credit card numbers, names, or medical conditions. Entity detection is
        only available via API, and increases the cost by 30%
      * <strong>Smart multi-language support</strong>. You can submit audio containing multiple languages,
        and Scribe v2 will automatically detect and transcribe each one correctly.
      * <strong>Improved stability</strong>. Scribe v2 handles pauses, changes in tone, and long silences
        without breaking or losing accuracy.
        <br />

      #### <strong>Which version should you use?</strong>

      We recommend <strong>Scribe v2</strong> when high-accuracy transcription is required. It's available through our [website](https://elevenlabs.io/app/speech-to-text) and [API](/docs/api-reference/speech-to-text/convert). When using Speech to Text via our website, Scribe v2 is the default model. 

      For real-time use cases, we recommend <strong>Scribe v2 Realtime</strong>, available through [ElevenAgents](https://elevenlabs.io/app/agents) and via [API](/docs/api-reference/speech-to-text/convert). 

      For more details, see our [Speech to Text documentation.](/docs/capabilities/speech-to-text)
    </td>
  </tr>

  <tr>
    <td>
      #### Which languages does Speech to Text support?

      Speech to Text supports over 90 languages. 

      For a full breakdown of which languages are supported, please see the [language support section](/docs/capabilities/speech-to-text#breakdown-of-language-support) of our [Speech to Text documentation.](/docs/capabilities/speech-to-text)
    </td>
  </tr>

  <tr>
    <td>
      #### How many Speech to Text requests can I make and can I increase it?

      The concurrency limit (concurrent requests running in parallel) depends on your subscription and whether you're using Speech to Text or Realtime Speech to Text.

      Below are the current concurrency rates for Speech to Text.

      | Plan       | Speech to Text Concurrency Limit | Realtime Speech to Text Concurrency Limit |
      | ---------- | -------------------------------- | ----------------------------------------- |
      | Free       | 8                                | 6                                         |
      | Starter    | 12                               | 9                                         |
      | Creator    | 20                               | 15                                        |
      | Pro        | 40                               | 30                                        |
      | Scale      | 60                               | 45                                        |
      | Business   | 60                               | 45                                        |
      | Enterprise | Elevated                         | Elevated                                  |

      If you require a higher number of concurrent requests, please reach out to our Enterprise Department directly via [this webpage](https://elevenlabs.io/enterprise). We will be happy to discuss a tailor-made plan that meets your specific requirements.
    </td>
  </tr>
</tbody>
