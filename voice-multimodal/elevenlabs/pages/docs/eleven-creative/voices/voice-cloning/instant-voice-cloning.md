---
title: "Instant Voice Cloning"
source: https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning.md
path: docs/eleven-creative/voices/voice-cloning/instant-voice-cloning
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Instant Voice Cloning

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5771a77cc729af95301635acf8de5519cfb53f40a3f5d38e6af591a880907521/assets/images/product-guides/voices/voice-cloning/voice-cloning-product-feature.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T231944Z&X-Amz-Expires=604800&X-Amz-Signature=ef6b0896670da69d018f74786adb21496d1b198cda461daca16e961b389a5ef6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Voice cloning product feature" />

## Creating an Instant Voice Clone

When cloning a voice, it's important to consider what the AI has been trained on: which languages and what type of dataset. Read more about each individual model and their strengths on the [Models page](/docs/overview/models).

## Guide

If you are unsure about what is permissible from a legal standpoint, please consult the [Terms of
Service](https://elevenlabs.io/terms-of-use) and our [AI Safety
information](https://elevenlabs.io/safety) for more information.

### Navigate to the Instant Voice Cloning page

In the ElevenLabs dashboard, select the **Voices** section on the left, then click the **plus** icon.

From the modal, select **Instant Voice Clone**.

### Upload or record your audio

Follow the on-screen instructions to upload or record your audio.

### Confirm voice details

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b3b4b3b8361ca372638c9c315e69588dcc44520bfaa00a3455720d963894d8ed/assets/images/product-guides/voices/voice-cloning/voice-cloning-ivc-modal.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T231944Z&X-Amz-Expires=604800&X-Amz-Signature=b2f6a0483e14a18deaa7c1f05ee24d5f31e7801eb4fb2c187e6e49eb7d1fca94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Voice cloning IVC modal" />

Name and label your voice clone, confirm that you have the right and consent to clone the voice, then click **Save voice**.

### Use your voice clone

Under the **Voices** section in the dashboard, click the **My Voices** then click **Use voice** to begin using it.

## Best practices

#### Record at least 1 minute of audio

#### Record at least 1 minute of audio

Avoid recording more than 3 minutes, this will yield little improvement and can, in some cases, even be detrimental to the clone.

How the audio was recorded is more important than the total length (total runtime) of the samples. The number of samples you use doesn't matter; it is the total combined length (total runtime) that is the important part.

Approximately 1-2 minutes of clear audio without any reverb, artifacts, or background noise of any kind is recommended. When we speak of "audio or recording quality," we do not mean the codec, such as MP3 or WAV; we mean how the audio was captured. However, regarding audio codecs, using MP3 at 128 kbps and above is advised. Higher bitrates don't have a significant impact on the quality of the clone.

#### Keep the audio consistent

#### Keep the audio consistent

The AI will attempt to mimic everything it hears in the audio. This includes the speed of the person talking, the inflections, the accent, tonality, breathing pattern and strength, as well as noise and mouth clicks. Even noise and artefacts which can confuse it are factored in.

Ensure that the voice maintains a consistent tone throughout, with a consistent performance. Also, make sure that the audio quality of the voice remains consistent across all the samples. Even if you only use a single sample, ensure that it remains consistent throughout the full sample. Feeding the AI audio that is very dynamic, meaning wide fluctuations in pitch and volume, will yield less predictable results.

#### Replicate your performance

#### Replicate your performance

Another important thing to keep in mind is that the AI will try to replicate the performance of the voice you provide. If you talk in a slow, monotone voice without much emotion, that is what the AI will mimic. On the other hand, if you talk quickly with much emotion, that is what the AI will try to replicate.

It is crucial that the voice remains consistent throughout all the samples, not only in tone but also in performance. If there is too much variance, it might confuse the AI, leading to more varied output between generations.

#### Find a good balance for the volume

#### Find a good balance for the volume

Find a good balance for the volume so the audio is neither too quiet nor too loud. The ideal would be between -23 dB and -18 dB RMS with a true peak of -3 dB.

## FAQ

<tbody>
  <tr>
    <td>
      #### What is the difference between Instant Voice Cloning and Professional Voice Cloning?

      [Professional Voice Cloning](/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning), unlike [Instant Voice Cloning](/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning) which lets you quickly clone voices with less than 2 minutes of audio, allows you to train a more realistic model of your voice. This is achieved by training a dedicated model on a large set of voice data to produce a model that’s virtually indistinguishable from your original voice.

      Since Professional Voice Clones require fine-tuning and training, it will take some time before you can use your voice clone. Giving an estimate is challenging as it depends on the number of people in the queue before you and a few other factors, but usually fine-tuning will take 3-6 hours.

      You will receive an email notification once your Professional Voice Clone is ready.
    </td>
  </tr>

  <tr>
    <td>
      #### How many voice samples should I upload for Instant Voice Cloning?

      Cloning with instant voice cloning can be a bit complicated, and we do have some general guidelines. However, they are just that: guidelines. We don't have any set rules when it comes to number of samples or length. We've seen users use samples of only 30 seconds and get excellent results, while we've also seen some users use 10 minutes of audio and have worse results. But we do have a few things that you should consider.

      * Audio quality is the most important aspect to consider when using instant voice cloning.
      * The number of samples is irrelevant; what's important is the total run time. Having more than 2-3 minutes of audio will yield little improvement and can, in some cases, even be detrimental to the stability of the clone.
    </td>
  </tr>

  <tr>
    <td>
      #### What files do you accept for voice cloning?

      For Instant Voice Cloning and Professional Voice Cloning, we accept a range of file types. We strongly recommend MP3 at 192kbps or above.

      **Recommended format**

      * MP3, 192kbps or higher

      **Recommended length**

      * Instant Voice Cloning: 1–2 minutes of good audio
      * Professional Voice Cloning: 30–180 minutes of good audio

      Uncompressed formats such as WAV usually do not improve clone quality, and they can cause problems with the upload process. Focus on recording quality instead: use a clean recording with no background noise, room reverb, or multiple speakers, at a consistent volume and tone, without long gaps of silence.

      For more information, see [Instant Voice Cloning (IVC)](/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning) and [Professional Voice Cloning (PVC)](/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning).
    </td>
  </tr>

  <tr>
    <td>
      #### Are there any restrictions on what voices I can upload for voice cloning?

      At ElevenLabs, we’re fully committed both to respecting intellectual property rights and to implementing safeguards against the potential misuse of our technology:

      * We only partner with clients who adhere to our [Terms of Service](https://elevenlabs.io/terms-of-use) and [Prohibited Use Policy](https://elevenlabs.io/use-policy), which prohibit malicious use of our technology towards any purpose which can be deemed illegal or harmful;
      * We seek to support voice owners and their licensors in claiming their rights and all known infringements will be reviewed and actioned;
      * All audio generated by our models can be instantly traced back to the user responsible for the generation.

      The technology we’re developing is new and clear regulation is yet to be introduced. Part of our goal as an AI research lab is to spread awareness about the existence of this technology, its potential, as well as its limitations.
    </td>
  </tr>

  <tr>
    <td>
      #### Are there any tips to get good-quality cloned voices?

      For a full guide, we highly recommend you read our documentation about [Instant Voice Cloning](/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning) and [Professional Voice Cloning](/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning).

      The bottom line is: good consistent input = good consistent output.

      Length

      * Instant Voice Cloning: 1 - 2 minutes of good audio
      * Professional Voice Cloning: 30 - 180 minutes of good audio

      Use the best and clearest audio clips that you can find. There should only be one speaker without background noise of interference and their voice should be loud and clear.

      Instead of using many clips of different quality just to increase the length, prioritize clips where the microphone quality is obviously very high and where the quality and tone is consistent throughout, rather than focusing on increasing the total runtime.

      Ensure that most of the dialogue in your clips aligns with the speaker's speaking style and intonation that you prefer the most. You don't want too many chunks of dialogue where the speaker deviates from the desired speech patterns you want to hear.

      If necessary, use a noise remover to reduce any background noise.

      You can find more information in our documentation [here](/docs/product-guides/voices/voice-cloning).
    </td>
  </tr>

  <tr>
    <td>
      #### Can I clone my voice in a language other than English?

      Yes. You can clone your voice in any language supported by Flash v2.5 and Multilingual v2. See the full list of supported languages [here](/docs/help-center/other/what-languages-do-you-support).

      You can also clone a voice speaking a language the AI does not support. The clone may capture the speaker’s tone, but it will not be able to speak that language, and results can be unpredictable. We do not recommend this.
    </td>
  </tr>

  <tr>
    <td>
      #### Can I export my voice clones?

      You cannot download or export your voice clones as standalone files. Voice clones stay in your ElevenLabs account.

      You can still use your ElevenLabs voices outside the ElevenLabs website. With your [API key](https://elevenlabs.io/app/settings/api-keys), third-party services can call the ElevenLabs API and generate speech with the voices in your account.

      If you want to recreate a clone later, keep the original audio samples you used to create it. Each clone will sound slightly different, even when you use the same audio.
    </td>
  </tr>

  <tr>
    <td>
      #### Why does my voice or accent not sound correct after cloning?

      ElevenLabs offers two cloning options:

      * **Instant Voice Cloning:** Fast results from about 1–3 minutes of audio. Works well for most voices, but may struggle with uncommon accents or unique voices.
      * **Professional Voice Cloning:** Higher fidelity, using 30 minutes to about 3 hours of audio. Fine-tuning usually takes 3–6 hours, and can take longer if many voices are queued.

      If Instant Voice Cloning does not capture your voice or accent well, try Professional Voice Cloning.

      You cannot change the accent or tone of a clone after it is created. To improve the result, change the audio samples you use. Small changes to the samples can make a large difference.
    </td>
  </tr>

  <tr>
    <td>
      #### What does the error 'No model found for this voice. Please select another voice' mean?

      You will see this error if you try to use your Professional Voice Clone (PVC) before it has completed the fine-tuning process and is available for use.

      When you create a PVC, it needs to go through a number of processes before it becomes available for use.  After you have verified your voice, it will be processed and queued for fine-tuning.   Depending on how many other voices are currently queued for fine-tuning, we estimate that this process will usually take between 3-6, but it can take up to 24 hours.

      You can check the progress of your PVC in My Voices by finding the voice in your list of voices, then clicking <strong>View</strong> to see more details.  You can hover over each model to see the current status.  

      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ec34838a2fd40c5105c9196c356045b2963daf2490fd36c19f42bcb8f5359c86/assets/images/help-center/product/voices/voice-cloning/what-does-the-error-no-model-found-for-this-voice-please-select-another-voice-mean.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T231944Z&X-Amz-Expires=604800&X-Amz-Signature=b59bfcf5059573c6e86e70db4b6e420a15f1ee6487db58698d62001fb62683e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

      For more detail on what each status means, please see [What does the status of my Professional Voice Clone mean?](/docs/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean)

      When your PVC has completed fine-tuning and is available for use, you will see a pop-up notification, and will also be notified by email.
    </td>
  </tr>
</tbody>
