---
title: "Dubbing"
source: https://elevenlabs.io/docs/eleven-creative/products/dubbing.md
path: docs/eleven-creative/products/dubbing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dubbing

## Overview

**Dubbing** allows you to translate content across 90+ languages in seconds with voice translation, speaker detection, and audio dubbing.

Automatic dubbing or video translation is a process for translating and replacing the original audio of a video with a new language, while preserving the unique characteristics of the original speakers' voices.

![Dubbing new project](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3605e288454d9cce3c8a9ad9c097cbffa2aaf858564e55f3432065590cd293e7/assets/images/product-guides/dubbing/dubbing-new-project.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260918%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260918T113100Z&X-Amz-Expires=604800&X-Amz-Signature=c9de4a6175348176a0b91967d2d4c18bc085eb34a6b548b68e25716318276558&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Guide

Go to [Dubbing](https://elevenlabs.io/app/dubbing) in your navigation menu.

Upload your video or audio file, or select the **Paste URL** tab to dub a video from YouTube,
TikTok, etc.

Choose the language, or languages, you want to dub into.

Click **Speaker similarity** to adjust how closely your dubbed voice mimics the original
speaker.

Click the generate button to submit your dub. You will be shown the cost and asked to confirm
your request.

Once your dub is ready, you'll be able to download it from your list of dubs.

For Dubbing v2, transcript editing and audio regeneration via the API are available on Enterprise
plans only.

## Cloning strength

Cloning strength is the configurable setting in Automatic Dubbing on the Dubbing v2 Alpha model, on a scale of 0 to 10. In the app, click **Speaker similarity** to adjust it. The default value of 7 works well for most content. Higher values prioritize voice similarity to the original speaker, which can sound less natural across languages with very different phonetic characteristics. A higher setting can also carry over more of the original accent into the dubbed output. Lower values give the model more freedom for natural delivery in the target language at the cost of resemblance to the original voice.

## FAQ

<tbody>
  <tr>
    <td>
      #### What is Dubbing?

      ElevenLabs was founded on the idea of creating amazing dubbing; a tool that would allow you to create a perfect dub in any language you desire, using the original voice of the actors and preserving the original performance, making all content more accessible.

      To get started, go to [Dubbing](https://elevenlabs.io/app/dubbing) and upload your audio or video file, or paste a URL to dub a video from YouTube, TikTok or elsewhere online **.**

      Select the language or languages you want to dub into in the **Choose languages** selector. You'll be charged for each language you select here. See [How much does Dubbing cost?](/docs/help-center/product/dubbing/how-much-does-dubbing-cost) for a full breakdown.

      By default, you'll use our latest Dubbing model, v2. Dubs created using the v2 model are automatic. There is no in-app option to edit the content. Transcript editing and audio regeneration via the API are available on Enterprise plans only.

      When using Dubbing v2 via the website, there's a 2 GB and 180 minutes limit for the uploaded file, and you need to stay below both.

      If you want a more in-depth explanation and guide on what Dubbing is and how to use it, we highly recommend reading the full documentation [here](/docs/product-guides/products/dubbing/dubbing-studio).



      If you want to create a Dubbing Studio project so you can edit your dubs, choose **Dubbing v1** as the model, then select **Dubbing project**.

      **Note:** Dubbing Studio is in maintenance mode and receives critical bug fixes only.
    </td>
  </tr>

  <tr>
    <td>
      #### On what plans can I use Dubbing?

      Dubbing is available on all our plans, including the free plan. Dubs generated on free plans are automatically watermarked, with no option to remove this. Watermarking is not available on our paid subscriptions.

      For Dubbing v2, transcript editing and audio regeneration via the API are available on Enterprise plans only.
    </td>
  </tr>

  <tr>
    <td>
      #### Can I edit and regenerate Dubbing v2 via the API?

      For Dubbing v2, transcript editing and audio regeneration via the API are available on Enterprise plans only.

      Creating and downloading dubs with the API is available on all plans. To edit the source transcript or translations and regenerate the audio, you need an Enterprise workspace. See [Refine and regenerate a dub](/docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate).
    </td>
  </tr>

  <tr>
    <td>
      #### How much does Dubbing cost?

      Dubbing is charged per minute of source media, for each language you dub into. The exact rate depends on the dubbing model you’re using — see the [pricing page](https://elevenlabs.io/pricing) for details. In the app, the total cost is shown for you to confirm before a dub starts.

      A dubbing project created with the [Dubbing API](/docs/eleven-api/guides/cookbooks/dubbing) has a minimum charge of one language. Creating a project charges you for one language’s dub up front, based on the duration of the source, and that charge prepays your first language target:

      * The charge is applied when you create the project, while its source is being prepared — not when you add the first language.
      * The first language you add (or the one you queue with `target_language` when creating the project) uses this prepaid charge rather than adding to it.
      * Each additional language you add is charged separately when you queue it.

      ## Handling failures

      * If a project fails to prepare — for example, its source cannot be transcribed — the creation charge is refunded.
      * If an additional language fails to generate, its charge is refunded.
      * The first language is prepaid by the project’s creation charge. If it fails to generate, the creation charge is not refunded, but the prepayment is not lost: it stays available, so retrying that language on the same project incurs no additional charge.
      * Deleting a project or language does not refund a dub that is already running.
    </td>
  </tr>

  <tr>
    <td>
      #### Which file formats are supported by Dubbing?

      Dubbing Studio can output in the following formats:

      * MP4 (Video)
      * AAC (Audio)
      * AAF (Timeline data)
      * SRT (Captions)
      * WAV (Audio - separate tracks for each speaker, downloaded as zip file)

      Dubbing v2 returns a single lossless audio file.

      You can upload audio and video files in the following formats for Dubbing:

      * AAC
      * AIFF
      * AVI
      * FLAC
      * M4A
      * M4V
      * MKV
      * MOV
      * MP3
      * MP4
      * MPEG
      * MPG
      * OGA
      * OGG
      * OPUS
      * WAV
      * WEBA
      * WEBM
      * WMV
      * 3GPP
    </td>
  </tr>

  <tr>
    <td>
      #### Do you offer lip sync?

      At the moment, ElevenLabs does not offer lip syncing as part of Dubbing. Lip sync is available in Image & Video, Flows, and Studio via third party models.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I access Dubbing Studio?

      By default, when you create a new dub, our latest Dubbing v2 model will be used. Dubs created using the v2 model are automatic. There is no in-app option to edit the content. Transcript editing and audio regeneration via the API are available on Enterprise plans only.

      If you want to use Dubbing Studio, choose **Dubbing v1** as the model, then select **Dubbing project**.

      It's not possible to convert an existing automatic dub to a Dubbing project.

      The new dubbing project will appear at the top of your list of dubbing projects, and will go through various stages while generating.

      Once it has completed processing, click the three dots icon and select **Edit** to open your dubbing project.

      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/88ae8853b135c164e1b969cc7ffdf4a427ec9e6ca56a50a646fceb54a0210656/assets/images/help-center/product/dubbing/how-do-i-access-dubbing-studio-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260918%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260918T113100Z&X-Amz-Expires=604800&X-Amz-Signature=80bbd26a7316181a9125fc792cc9ba640aa6062f17f8986b613ba056c40aa643&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      For more information about Dubbing Studio, please see our [overview.](/docs/product-guides/products/dubbing/dubbing-studio)
    </td>
  </tr>

  <tr>
    <td>
      #### What happens to my dubs if I downgrade my subscription?

      If you downgrade your tier or cancel your subscription altogether, you will not be able to use the paid features anymore, such as Instant Voice Cloning and Professional Voice Cloning. However, at the time of writing this, we do not delete any of your data, and it will still be there when you feel ready to upgrade again.
    </td>
  </tr>

  <tr>
    <td>
      #### What is the difference between a track clone and a clip clone in the Dubbing Studio?

      Dubbing Studio is in maintenance mode and receives critical bug fixes only.

      A track clone refers to a voice clone that is derived from the entire track in a dubbing project. This means that the voice clone will be made from a combination of all of the clips on that track. This is the default behavior and is good for creating voice clones that have a bit of the characteristics of all the clips combined and usually give the AI enough data to create a proper clone. However, if the voice changes quite drastically throughout, it might create a voice that is a bit more unstable.

      On the other hand, a clip clone refers to a voice clone that is derived from a specific clip on a track. This allows you to create different voice clones from specific clips and assign that same voice to other clips where you want the tonality or performance. This can be great if you feel like a specific track has exactly the performance you want and want to apply this to other clips too, or perhaps, you want to apply this to the whole track.

      One helpful tip mentioned in the content is to find a clip that you like, where you feel the voice is good, right-click to create a clone from that clip, and then assign that clone to the whole track to achieve a consistent voice throughout. This is just one tip and may not work for all circumstances, but it can work very well in some cases.
    </td>
  </tr>

  <tr>
    <td>
      #### Why can't I download my dubs?

      If you can't download dubbed audio or video, try a different browser and turn off ad blockers and pop-up blockers.

      This issue is most often reported with the Brave browser, but it can also occur in others. In most cases, switching browsers or disabling blockers resolves the problem.
    </td>
  </tr>

  <tr>
    <td>
      #### Why can't I see the edit button next to my dub?

      By default, when you create a new dub, our latest Dubbing v2 model will be used. Dubs created using the v2 model are automatic. There is no in-app edit button for Dubbing v2.

      The edit button is only available when using Dubbing Studio, which is only available for our legacy v1 Dubbing model. To use Dubbing Studio, choose **Dubbing v1** as the model, then select **Dubbing project**.

      For Dubbing v2, you can edit transcripts and regenerate audio via the API on Enterprise plans only.

      **Note:** Dubbing Studio is in maintenance mode and receives critical bug fixes only.
    </td>
  </tr>
</tbody>
