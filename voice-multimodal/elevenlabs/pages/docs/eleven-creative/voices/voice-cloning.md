---
title: "Voice Cloning"
source: https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning.md
path: docs/eleven-creative/voices/voice-cloning
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voice Cloning

## Overview

When cloning a voice, there are two main options: Instant Voice Cloning and Professional Voice Cloning. Instant Voice Cloning is a quick and easy way to clone your voice, while Professional Voice Cloning is a more accurate and customizable option.

## Instant Voice Cloning

![Instant voice
cloning](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5f7bbacc7f5bae472e8fd61503496c5137675c1c0ab00b785829d1049ca1fe28/assets/images/product-guides/voices/voice-cloning/voice-cloning-ivc-modal.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T113140Z&X-Amz-Expires=604800&X-Amz-Signature=fab7f2627a40354edbd3499b77873c229e0168a6adb3776961f6b2f53ce0bfdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Instant Voice Cloning allows you to create voice clones from shorter samples near instantaneously. Creating an Instant Voice Clone (IVC) does not train or create a custom AI model. Instead, it relies on prior knowledge from training data to make an educated guess rather than training on the exact voice.

This works extremely well for a lot of voices. However, the biggest limitation with IVCs is if you are trying to clone a very unique voice, or a voice with an accent that the AI might not have experienced extensively during training. In such cases, using Professional Voice Cloning to create a custom model with explicit training might be the best option.

## Professional Voice Cloning

![Professional voice
cloning](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/84134ac62c71531ac93d090030d9651bf428dc90802c17b33ad924973b6560c2/assets/images/product-guides/voices/voice-cloning/voice-pvc-creation.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T113140Z&X-Amz-Expires=604800&X-Amz-Signature=5f8de29c5a7c3c464e5c611448dbe6e374ad0a1a5e113e24bcd86473bb60cf82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Professional Voice Cloning is a feature that's available on our Creator plan or above. Professional Voice Cloning allows you to train a more realistic model of your voice by training a dedicated model on a larger set of voice data, producing a model that's virtually indistinguishable from the original voice.

Since the custom models require fine-tuning and training, it takes more time to train PVCs compared to IVCs. Generally fine-tuning takes 3-6 hours to complete, but it can sometimes take a bit longer, depending on the number of other PVCs queued for fine-tuning.

## Beginner's guide to audio recording

If you're new to audio recording, here are some tips to help you get started.

### Recording location

When recording audio, choose a suitable location and set up to minimize room echo/reverb.
So, we want to "deaden" the room as much as possible. This is precisely what a vocal booth that is acoustically treated made for, and if you do not have a vocal booth readily available, you can experiment with some ideas for a DIY vocal booth, "blanket fort", or closet.

Here are a few YouTube examples of DIY acoustics ideas:

* [I made a vocal booth for \$0.00!](https://www.youtube.com/watch?v=j4wJMDUuHSM)
* [How to Record GOOD Vocals in a BAD Room](https://www.youtube.com/watch?v=TsxdHtu-OpU)
* [The 5 BEST Vocal Home Recording TIPS!](https://www.youtube.com/watch?v=K96mw2QBz34)

### Microphone, pop-filter, and audio interface

A good microphone is crucial. Microphones can range from \$100 to \$10,000, but a professional XLR microphone costing \$150 to \$300 is sufficient for most voiceover work.

For an affordable yet high-quality setup for voiceover work, consider a **Focusrite** interface paired with an **Audio-Technica AT2020** or **Rode NT1 microphone**. This setup, costing between \$300 to \$500, offers high-quality recording suitable for professional use, with minimal self-noise for clean results.

Please ensure that you have a proper **pop-filter** in front of the microphone when recording to avoid plosives as well as breaths and air hitting the diaphragm/microphone directly, as it will sound poor and will also cause issues with the cloning process.

### Digital Audio Workstation (DAW)

There are many different recording solutions out there that all accomplish the same thing: recording audio. However, they are not all created equally. As long as they can record WAV files at 44.1kHz or 48kHz with a bitrate of at least 24 bits, they should be fine. You don't need any fancy post-processing, plugins, denoisers, or anything because we want to keep audio recording simple.

If you want a recommendation, we would suggest something like **REAPER**, which is a fantastic DAW with a tremendous amount of flexibility. It is the industry standard for a lot of audio work. Another good free option is **Audacity**.

Maintain optimal recording levels (not too loud or too quiet) to avoid digital distortion and excessive noise. Aim for peaks of -6 dB to -3 dB and an average loudness of -18 dB for voiceover work, ensuring clarity while minimizing the noise floor. Monitor closely and adjust levels as needed for the best results based on the project and recording environment.

### Positioning

One helpful guideline to follow is to maintain a distance of about two fists away from the microphone, which is approximately 20cm (7-8 in), with a pop filter placed between you and the microphone. Some people prefer to position the pop filter all the way back so that they can press it up right against it. This helps them maintain a consistent distance from the microphone more easily.

Another common technique to avoid directly breathing into the microphone or causing plosive sounds is to speak at an angle. Speaking at an angle ensures that exhaled air is less likely to hit the microphone directly and, instead, passes by it.

### Performance

The performance you give is one of the most crucial aspects of this entire recording session. The AI will try to clone everything about your voice to the best of its ability, which is very high. This means that it will attempt to replicate your cadence, tonality, performance style, the length of your pauses, whether you stutter, take deep breaths, sound breathy, or use a lot of "uhms" and "ahs" – it can even replicate those. Therefore, what we want in the audio file is precisely the performance and voice that we want to clone, nothing less and nothing more. That is also why it's quite important to find a script that you can read that fits the tonality we are aiming for.

When recording for AI, it is very important to be consistent. if you are recording a voice either keep it very animated throughout or keep it very subdued throughout you can't mix and match or the AI can become unstable because it doesn't know what part of the voice to clone. same if you're doing an accent keep the same accent throughout the recording. Consistency is key to a proper clone!

## FAQ

<tbody>
  <tr>
    <td>
      #### What is the difference between Instant Voice Cloning (IVC) and Professional Voice Cloning (PVC)?

      [Professional Voice Cloning (PVC)](/docs/voices/voice-lab/professional-voice-cloning), unlike [Instant Voice Cloning (IVC)](/docs/voices/voice-lab/instant-voice-cloning) which lets you quickly clone voices with less than 2 minutes of audio, allows you to train a more realistic model of your voice. This is achieved by training a dedicated model on a large set of voice data to produce a model that’s virtually indistinguishable from your original voice.<br /><br />Since Professional Voice Clones require fine-tuning and training, it will take some time before you can use your voice clone. Giving an estimate is challenging as it depends on the number of people in the queue before you and a few other factors, but usually fine-tuning will take 3-6 hours. <br /><br />You will receive an email notification once your Professional Voice Clone is ready.
    </td>
  </tr>

  <tr>
    <td>
      #### What files do you accept for voice cloning?

      Recommended:

      * MP3 192kbps+

      Length:

      * 1-2 minutes of good audio for Instant Voice Cloning
      * 30min - 180min of good audio for Professional Voice Cloning

      For both Instant Voice Cloning and Professional Voice Cloning, we accept a plethora of file types, but we strongly recommend using MP3 with a bitrate of 192kbps or above. Using an uncompressed format such as WAV will yield little to no improvement. It is instead recommended to focus on the quality of the actual recording to ensure it is recorded professionally without any background noise, room reverb, multiple speakers, at a consistent volume with a consistent tone, no extremely long gaps of silence, and so on.

      For more information regarding cloning, we highly recommend that you read our documentation for [Instant Voice Cloning (IVC)](/docs/voices/voice-lab/instant-voice-cloning) and [Professional Voice Cloning (PVC)](/docs/voices/voice-lab/professional-voice-cloning).
    </td>
  </tr>

  <tr>
    <td>
      #### Why does my voice or accent not sound correct after cloning?

      Currently, we offer two choices for cloning:

      1. <strong>Instant Voice Cloning (IVC):</strong> IVC is less resource-intensive and provides instant
         results that you can use immediately. This method is swift, requiring only about 1 to 3 minutes
         of audio input for a high-quality clone, and is often ideal for most general uses but might have
         trouble with unique voices or accents.

      2. <strong>Professional Voice Cloning (PVC):</strong> PVC demands significantly more resources and
         you are required to provide the AI with a substantial amount of data (between a minimum of 30
         minutes and closer to 3 hours for optimal results). This process involves fine-tuning the model
         using the provided dataset to create a customized model.  The estimated training time is roughly
         2-6 hours, but the process may take longer depending on how many other voices are queued for
         fine-tuning.

      If you have a rather unique voice with a less common accent, instant voice cloning might not provide a perfect replication of your voice. Then the only way to achieve something like that might be through professional voice cloning. Instant voice cloning is generally very accurate, but under certain circumstances, such as those mentioned above, you might have to resort to professional voice cloning to obtain the most perfect clone.

      Unfortunately, there is no way to influence the accent or tone of the clone after the clone has already been created; the only way to influence it is to change the actual samples you use for cloning. Just small changes to the samples can make a big difference.
    </td>
  </tr>

  <tr>
    <td>
      #### Are there any restrictions on what voices I can upload for voice cloning?

      At Eleven, we’re fully committed both to respecting intellectual property rights and to implementing safeguards against the potential misuse of our technology:

      * We only partner with clients who adhere to our Terms of Service and Prohibited Use Policy which prohibit malicious use of our technology towards any purpose which can be deemed illegal or harmful;
      * We seek to support voice owners and their licensors in claiming their rights and all known infringements will be reviewed and actioned;
      * All audio generated by our models can be instantly traced back to the user responsible for the generation.

      The technology we’re developing is new and clear regulation is yet to be introduced. Part of our goal as an AI research lab is to spread awareness about the existence of this technology, its potential, as well as its limitations.
    </td>
  </tr>

  <tr>
    <td>
      #### Can I export my voice clones?

      No, you cannot export your voice clones, and they are only usable on [ElevenLabs](https://elevenlabs.io/) and not anywhere else.

      If you want to save the voice clone to be able to clone it again later, you will have to save the samples that you used to create the cloned voice. Please be aware that each clone will be slightly different, even if the same audio is used.
    </td>
  </tr>

  <tr>
    <td>
      #### Are there any tips to get good-quality cloned voices?

      For a full guide, we highly recommend you read our documentation about [Instant Voice Cloning (IVC)](/docs/voices/voice-lab/instant-voice-cloning) and [Professional Voice Cloning (PVC)](/docs/voices/voice-lab/professional-voice-cloning).

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

      Yes, you can clone your voice speaking any language that is supported by the Flash v2.5 and Turbo v2.5 model. You can find the full list of languages [here](/docs/help-center/other/what-languages-do-you-support).

      You can even clone a voice speaking a language that the AI is not compatible with, but the results might be very unpredictable, as the AI has never heard that language before. However, it will try its best to clone the voice tonality of the speaker, but it will not be able to speak that language. We would not recommend doing this.
    </td>
  </tr>

  <tr>
    <td>
      #### Can I create a Professional Voice Clone of someone else's voice?

      No. You can only create a Professional Voice Clone of your own voice. Even with their consent, you cannot clone someone else’s voice. All Professional Voice Clones require a verification process to confirm that the voice belongs to you.

      If someone wants to share their voice with you, they can create and verify a Professional Voice Clone on their own account, then share it with you privately using a sharing link. Learn more in our article: [How do I share a voice?](/docs/help-center/product/voice-customization/my-voices/how-do-i-share-a-voice)
    </td>
  </tr>

  <tr>
    <td>
      #### How can I delete my unverified Professional Voice Clone (PVC)?

      Unfortunately, this is not possible. As mentioned during the setup process of your Professional Voice Clone (PVC), once you advance to the verification stage, you are locked in until you've verified your voice.

      If you need help with your Professional Voice Clone, please reach out to support [here](https://help.elevenlabs.io/hc/en-us/requests/new).
    </td>
  </tr>

  <tr>
    <td>
      #### How do I add or upgrade the models used to train my Professional Voice Clone?

      All Professional Voice Clones (PVCs) will automatically train on the Flash v2.5, Turbo v2.5 and Multilingual v2 models. PVCs trained on English audio will also automatically train on the Flash v2 and Turbo v2 models.

      If you have an existing PVC, you now have the option to fine-tune on additional models. In the future, if new models are released that support fine-tuning, you will receive a notification. This is shown by an exclamation icon, which will appear to the right of your voice in the voice list in [My Voices.](https://elevenlabs.io/app/voice-lab) Hovering over this icon will display the notification.

       

      <img src="https://help.elevenlabs.io/hc/article_attachments/35963711553297" alt="" />

       

      To start the fine-tuning process, hover over the name of your voice in the list in [My Voices,](https://elevenlabs.io/app/voice-lab) and you will see all available models. Models that the voice has already been fine-tuned on will be displayed with a tick icon, and models that are available for fine-tuning will be displayed with a plus icon. To begin fine tuning, just click on the model. 

      <img src="https://help.elevenlabs.io/hc/article_attachments/35963711556625" alt="" />

      While the voice is fine-tuning, you can hover over the model name to see the progress. Please note that due to voice caching, you may need to refresh the page to see the latest progress. Once the fine-training has been completed, you will be notified both in-app and by email.
    </td>
  </tr>

  <tr>
    <td>
      #### How many Professional Voice Clones (PVCs) can I have?

      Professional Voice Clone (PVC) slots vary by subscription tier:

      <br />

      <strong>
        Base PVC Slots
      </strong>

      * Free and Starter plan: No PVC slots available
      * Creator, Pro, and legacy Scale plan: 1 PVC slot
      * Scale and legacy Business plan: 3 PVC slots
      * Business plan: 10 PVC slots
      * Enterprise plan: Custom number of PVC slots

      <br />

      <strong>
        Additional PVC Slots
      </strong>

      You can earn additional PVC slots through our quality review process:

      * If your existing PVC gets marked as Studio Quality through our manual review process, you'll automatically receive an additional PVC slot
      * This can happen multiple times if multiple voices get marked as Studio Quality
      * You cannot submit more PVC voices unless you either:

        Get extra slots through the Studio Quality review process

        Upgrade to a Business/Enterprise plan

      <strong>
        Important Notes
      </strong>

      * Professional Voice Clones can only be used to clone your own voice
      * If you downgrade below the Creator tier, your PVC will stay in your library but you won't be able to use it until you upgrade to Creator or above
      * The total number of custom voices you can have (including PVCs) depends on your subscription tier
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
      #### My professional voice clone failed or is delayed, what can I do?

      After you've verified your voice, it will need to fine-tune on our models before you will be able to use it. While this is happening, you can check the status of your voice in [My Voices](https://elevenlabs.io/app/voice-lab) by hovering over the name of your voice. This will show you all the available models for your voice. To check the status for each model, hover over the model's name. 

      If something went wrong, then you may see the following status:

      **We are sorry the training run experienced issues and has been retried. No further action is required.** This means that something went wrong. but your voice has been automatically queued to
      retry the fine-tuning process. Your voice should successfully complete the fine-tuning process on
      the next try, but if you experience multiple failures, this might be an issue with the dataset that
      the AI cannot resolve.

      You can try to resolve this by deleting the voice and uploading the data again, starting from the beginning. This has been shown to help some users.

      If this doesn't resolve the issue, you may need to review your training audio and potentially use different training audio.

      You can always [contact Support](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937) if you're experiencing failures during the fine-tuning process.
    </td>
  </tr>

  <tr>
    <td>
      #### What can I do if I failed to verify my Professional Voice Clone (PVC)?

      If you fail all your verification attempts during the creation of your professional voice clone, you can wait 24 hours, after which time you will be able to retry the process.

      You can also reach out to [support](https://help.elevenlabs.io/hc/en-us/requests/new) so they can look into it for you. If everything looks correct, they will remove the failed verification attempts so you can retry the process from the start.

      Here are some recommendations to help you successfully verify your Professional Voice Clone:

      * Make sure that your web browser is allowed to use your microphone and that you are not muted.
      * Ensure that the recorded audio from your computer microphone sounds similar to the audio uploaded for cloning, without any background noise or other external audio interference.
      * Try to speak in a similar style to the audio you used to train the voice.
      * Read each verification line only once, then press <strong>Stop</strong> to stop recording. Reading the line more than once can cause the verification process to fail.
    </td>
  </tr>

  <tr>
    <td>
      #### What does the error 'No model found for this voice. Please select another voice' mean?

      You will see this error if you try to use your Professional Voice Clone (PVC) before it has completed the fine-tuning process and is available for use.

      When you create a PVC, it needs to go through a number of processes before it becomes available for use.  After you have verified your voice, it will be processed and queued for fine-tuning.   Depending on how many other voices are currently queued for fine-tuning, we estimate that this process will usually take between 3-6, but it can take up to 24 hours.

      You can check the progress of your PVC in My Voices by finding the voice in your list of voices, then clicking <strong>View</strong> to see more details.  You can hover over each model to see the current status.  

      <img src="https://help.elevenlabs.io/hc/article_attachments/28006635136785" alt="" />

      For more detail on what each status means, please see [What does the status of my Professional Voice Clone mean?](/docs/help-center/product/voice-customization/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean)

      When your PVC has completed fine-tuning and is available for use, you will see a pop-up notification, and will also be notified by email.
    </td>
  </tr>

  <tr>
    <td>
      #### What does the status of my Professional Voice Clone mean?

      Your Professional Voice Clone will go through a few different stages while it is processing. These stages are reflected in the status shown for your Professional Voice Clone in [My Voices](https://elevenlabs.io/app/voice-lab).

      To view the current status, find your voice in the list and look at the icons displayed to the right.

       

      <strong>Draft:</strong> This status means that your voice is incomplete. Generally this is either
      because you haven't completed creating the voice, or you haven't verified the voice yet.

      <img src="https://help.elevenlabs.io/hc/article_attachments/35965215258641" alt="" />

      To go through the verification process, click the tick icon.

      <img src="https://help.elevenlabs.io/hc/article_attachments/35965215262097" alt="" />

      To go back to the voice creation process, click <strong>More actions</strong> (three dots) and select <strong>Edit voice</strong>.

       

      Once you've verified your voice, it will need to fine-tune on our models before you can use it. You can track this process by hovering over the name of your voice in [My Voices](https://elevenlabs.io/app/voice-lab). You'll see all available models listed here, with an icon to indicate the status for each model. 

      <img src="https://help.elevenlabs.io/hc/article_attachments/35965182407569" alt="" />

       

      Hover over the name of the model for more information, and you will see one of the following:

      <strong>The training run has been scheduled</strong>: This means that your voice is waiting for a
      slot to open up so it can be trained. The length of time that your voice will be queued will depend
      on how many other voices are also in the queue.

      <strong>Creating dataset</strong> and <strong>Running fine-tuning</strong>: Once a slot opens up, it
      will begin the fine-tuning process. This can take between 6-24 hours. You'll see how far through
      each step in the training process your voice is, indicated by a percentage.

      <strong>
        We are sorry the training run experienced issues and has been retried. No further action is
        required
      </strong>

      : This means that something went wrong. but your voice has been automatically queued to retry the
      fine-tuning process. Your voice should successfully complete the fine-tuning process on the next
      try, but if you experience multiple failures, please [contact
      Support. ](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937)

      <strong>Voice is ready to be used with the model</strong>: This means that the fine-tuning process
      for this model has been completed, and you can now use your voice with this model.

      <strong>Click to start fine-tuning</strong>: Some models do not train automatically, and you will
      need to click the model name to begin fine-training. If additional models have become available for
      your voice to fine-tune on, you'll see an exclamation icon next to your voice. 

      <img src="https://help.elevenlabs.io/hc/article_attachments/35965182410513" alt="" />

      To begin the fine-tuning process, just hover over your voice's name and click the name of the model.
    </td>
  </tr>

  <tr>
    <td>
      #### What languages are supported with Professional Voice Cloning (PVC)?

      We support Professional Voice Cloning for all languages supported by the Flash v2.5 and Turbo v2.5 model.

      Currently, these are the languages we support with professional voice cloning:

      * 🇺🇸 English (USA)
      * 🇬🇧 English (UK)
      * 🇦🇺 English (Australia)
      * 🇨🇦 English (Canada)
      * 🇯🇵 Japanese
      * 🇨🇳 Chinese
      * 🇩🇪 German
      * 🇮🇳 Hindi
      * 🇫🇷 French (France)
      * 🇨🇦 French (Canada)
      * 🇰🇷 Korean
      * 🇧🇷 Portuguese (Brazil)
      * 🇵🇹 Portuguese (Portugal)
      * 🇮🇹 Italian
      * 🇪🇸 Spanish (Spain)
      * 🇲🇽 Spanish (Mexico)
      * 🇮🇩 Indonesian
      * 🇳🇱 Dutch
      * 🇹🇷 Turkish
      * 🇵🇭 Filipino
      * 🇵🇱 Polish
      * 🇸🇪 Swedish
      * 🇧🇬 Bulgarian
      * 🇷🇴 Romanian
      * 🇸🇦 Arabic (Saudi Arabia)
      * 🇦🇪 Arabic (UAE)
      * 🇨🇿 Czech
      * 🇬🇷 Greek
      * 🇫🇮 Finnish
      * 🇭🇷 Croatian
      * 🇲🇾 Malay
      * 🇸🇰 Slovak
      * 🇩🇰 Danish
      * 🇮🇳 Tamil
      * 🇺🇦 Ukrainian
      * 🇷🇺 Russian
      * 🇭🇺 Hungarian
      * 🇳🇴 Norwegian
      * 🇻🇳 Vietnamese
    </td>
  </tr>

  <tr>
    <td>
      #### When will my professional voice clone (PVC) be ready?

      Professional Voice Cloning involves training (fine-tuning) the model on large sets of a particular speaker’s voice to create a custom model.

      Once you've uploaded your samples and verified your voice, your Professional Voice Clone will be added to the queue. The estimated training time is roughly 2-6 hours. This is dependent on a few factors, so it is hard to give an exact estimate. Unfortunately, it can sometimes take longer.

      You can check the current status of your voice in [My Voices.](https://elevenlabs.io/app/voice-lab) For more information, please see [What does the status of my Professional Voice Clone mean?](/docs/help-center/product/voice-customization/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean)

      When your PVC has completed the fine-tuning process, you will receive notifications in-app and by email letting you know that your voice is now ready for use.
    </td>
  </tr>
</tbody>
