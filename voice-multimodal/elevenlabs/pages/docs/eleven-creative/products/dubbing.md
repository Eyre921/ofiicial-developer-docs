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

![Dubbing new project](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8c0235c62183be7eabf87a0346600e94e3c5717ecb58f0207715894eb39c9f5e/assets/images/product-guides/dubbing/dubbing-new-project.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T094031Z&X-Amz-Expires=604800&X-Amz-Signature=1ec061783572ac832071870086ea0bc941ee2ea4bbb7120351b5d9fc09eaccd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Guide

Go to [Dubbing](https://elevenlabs.io/app/dubbing) in your navigation menu.

Upload your video or audio file, or select the **Paste URL** tab to dub a video from YouTube,
TikTok, etc.

Choose the language, or languages, you want to dub into.

Click the **Advanced** settings to adjust speaker similarity. This setting controls how closely
your dubbed voice mimics the original speaker.

Click the generate button to submit your dub. You will be shown the cost and asked to confirm
your request.

Once your dub is ready, you'll be able to download it from your list of dubs.

![Dubbing new project advanced
settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9515592460d4e2e6393e657c2743710b201c846ed0894c82343f55bde176b8fd/assets/images/product-guides/dubbing/dubbing-new-advanced.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T094031Z&X-Amz-Expires=604800&X-Amz-Signature=18637234de2d59aa50ca05e9ef47063404b16146666eeedb26c7ddb31a0a3e52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Cloning strength

Cloning strength is the configurable setting in Automatic Dubbing on the Alpha model. The default value of 7 works well for most content.

* This is the advanced Dubbing version, which you can access by checking the **Create a Dubbing Studio project** box. Read more about it in the [Dubbing Studio guide](/docs/creative-platform/products/dubbing/dubbing-studio).

## FAQ

<tbody>
  <tr>
    <td>
      #### What is Dubbing?

      ElevenLabs was founded on the idea of creating amazing dubbing; a tool that would allow you to create a perfect dub in any language you desire, using the original voice of the actors and preserving the original performance, making all content more accessible.

      To get started, go to [Dubbing](https://elevenlabs.io/app/dubbing) and upload your audio or video file, or paste a URL to dub a video from YouTube, TikTok or elsewhere online <strong>.</strong>

      Select the language or languages you want to dub into in the <strong>Choose languages</strong> selector. You'll be charged for each language you select here. 

      By default, you'll use our latest Dubbing model, v2. Dubs created using the v2 model are completely automatic without any option to edit the content.

      When using Dubbing v2 via the website, there's a 2 GB and 180 minutes limit for the uploaded file, and you need to stay below both.

      If you want a more in-depth explanation and guide on what Dubbing is and how to use it, we highly recommend reading the full documentation [here](/docs/product-guides/products/dubbing/dubbing-studio).

       

      If you want to create a Dubbing Studio project, so you can edit your dubs, you can also choose <strong>Use legacy v1 dubbing model</strong> in the <strong>Advanced</strong> options. This will allow you to create a Dubbing Studio project by checking the <strong>Create Dubbing project</strong> option. 

      <strong>Note:</strong> Dubbing Studio is in maintenance mode and receives critical bug fixes only.
    </td>
  </tr>

  <tr>
    <td>
      #### On what plans can I use Dubbing?

      Dubbing is available on all our plans, including the free plan. Dubs generated on free plans are automatically watermarked, with no option to remove this. Watermarking is not available on our paid subscriptions.
    </td>
  </tr>

  <tr>
    <td>
      #### How much does Dubbing cost?

      The cost for dubbing depends on the dubbing model you’re using, the duration of your dub, and the number of languages you’re dubbing into. The total cost will be displayed before you confirm your request.
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

      By default, when you create a new dub, our latest Dubbing v2 model will be used. Dubs created using the v2 model are completely automatic without any option to edit the content.

      If you want to use Dubbing Studio, you can do this by selecting <strong>Use legacy v1 Dubbing model</strong> in the <strong>Advanced</strong> options when you create your dub, then check the <strong>Create Dubbing project</strong> option. 

      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9fc196e5c40348615fff7f381e5945b855702f9b0b0cbeb204c565d17d6211f6/assets/images/help-center/product/dubbing/how-do-i-access-dubbing-studio.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T094031Z&X-Amz-Expires=604800&X-Amz-Signature=843b46412c88bdb3c87725572ddbd55c5dcdd365db5fc89dfd1296acf19ec5ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

      It's not possible to convert an existing automatic dub to a Dubbing project.

      The new dubbing project will appear at the top of your list of dubbing projects, and will go through various stages while generating.

      Once it has completed processing, click the three dots icon and select <strong>Edit</strong> to open your dubbing project.

      <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/88ae8853b135c164e1b969cc7ffdf4a427ec9e6ca56a50a646fceb54a0210656/assets/images/help-center/product/dubbing/how-do-i-access-dubbing-studio-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T094031Z&X-Amz-Expires=604800&X-Amz-Signature=2b6a6eb95eb6fdd2bfb429c10578a8b692cbeb7eb69eca013298d6d64847e5dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

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

      By default, when you create a new dub, our latest Dubbing v2 model will be used. Dubs created using the v2 model are completely automatic without any option to edit the content.

      The edit button is only available when using Dubbing Studio, which is only available for our legacy v1 Dubbing model. To use Dubbing Studio, you will need to select <strong>Use legacy v1 Dubbing model</strong> in the <strong>Advanced</strong> options when you create your dub, then check the <strong>Create Dubbing project</strong> option. 

      <strong>Note:</strong> Dubbing Studio is in maintenance mode and receives critical bug fixes only.
    </td>
  </tr>
</tbody>
