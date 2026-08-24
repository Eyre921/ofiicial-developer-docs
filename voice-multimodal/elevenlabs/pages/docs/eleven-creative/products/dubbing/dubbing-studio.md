---
title: "Dubbing Studio"
source: https://elevenlabs.io/docs/eleven-creative/products/dubbing/dubbing-studio.md
path: docs/eleven-creative/products/dubbing/dubbing-studio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dubbing Studio

Dubbing Studio is in maintenance mode. It continues to receive critical bug fixes only, and no new
feature work is planned. Existing Dubbing Studio customers keep uninterrupted access.

## Create a Dubbing Studio project

1. Check the 'Create Dubbing Studio' box when creating a dub.

![Create Dubbing Studio Project](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c334b44ee4e91578c7be68c2bec87f88500b32ee3d79238c8719a1b102744941/assets/images/product-guides/dubbing/dubbing-studio-create.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=682969e0c9e5e1a0bcbe24c7e6127283e9cda2a42e93b7202088500e82517880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

2. Click on **Create Dub**. Once the Dubbing Studio project is created, you will be able to open it.

## Core Concepts

#### Speaker Cards

## Speaker Cards

![Dubbing Studio Speaker Cards](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c6be1de4bd0554d29e1e8c64623d047724294b0ba4afac818c4a067f5d423465/assets/images/product-guides/dubbing/dubbing-studio-edits.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=99797e42dc6406c6b66e5ba330ca2559230ed45c134187e26a0aa3e0308fee57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Speaker cards show the original transcription and translation (if you add one) of dialogue from the source video. You can click 'Transcribe Audio' to retranscribe
the original speech, or click the arrow to re-translate an existing transcription.

### Edit Transcripts and Translations

Both transcriptions and translations can be edited freely - just click inside a speaker card and start typing to edit the text.

### Speaker Identification

You can see the name of each speaker in the top left of the speaker card. To change the name of a speaker or reassign a clip to a different speaker,
you'll need to use the Timeline.

#### Timeline

## Timeline

The timeline contains many important elements of Dubbing Studio, covered in more detail in different sections below:

### Basic navigation

There are 3 main ways to navigate the timeline:

1. Click and drag the cursor
2. Horizontally scroll
3. Input a specific timecode on the right side of the timeline

### Adjust clips and regenerate audio

1. Drag the handles on the left or right side of a clip to adjust its length.
2. Click the refresh icon to regenerate the audio for that clip.

![Dubbing Studio Adjust and Regenerate](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3320cc4f5d628066da8d168fcfe0d1586d8a57e618a786fd5e5839ae487642f0/assets/images/product-guides/dubbing/dubbing-studio-adjust-regenerate.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=10523bb1559b2acef1bfac59f079d077b3799ce38b669914d98db777dd597008&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

##### Dynamic vs. Fixed Generations

NOTE: By default, all regenerations in Dubbing Studio are <i>Fixed Generations</i>, which means that the system will keep the duration of the clip fixed regardless
of how much text it contains. This can lead to speech speeding up or slowing down significantly if you adjust the length of a clip without changing the text, or if you add/remove
a large number of words to a clip.

Consider a clip with the phrase 'I'm doing well.' If that clip were set to last 10 seconds and the audio were generated using Fixed Generations, the speech would sound
slow and drawn out.

Alternatively, you can use <i>Dynamic Generations</i> by right clicking a segment and selecting it from the options. This will attempt to adjust the
length of the clip to the length of the text and make the audio sound more natural.

But be careful – using Dynamic Generations could affect sync and timing in your videos. If, for example, you select Dynamic Generation for a clip with many words in it,
and there is not enough room before the next clip for it to properly expand, the audio may not generate properly.

![Dubbing Studio Dynamic Generation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/25222c5ca2adb6d17899d1949bd07b4c4b3249f59da4f08d77b9525a572e8721/assets/images/product-guides/dubbing/dubbing-studio-dynamic.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=36fe1d1103ac7aa18cc99e76497018d874b780db34cda0ca3d414405d2145fc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

##### Stale Audio

Stale audio refers to audio that needs to be regenerated for one of many reasons (clip length changes, settings changes, transcription/translation changes, etc). You can regenerate stale
clips individually or click 'Generate Stale Audio' to bulk generate all stale audio clips.

##### Clip History

You can right click a clip and select 'Clip History' to view previous generations and select the one that sounds best.

### Split and Merge clips

1. To split a clip, move the cursor to a specific timecode and click 'Split'.
2. To merge two clips, drag the ends of the clips together and click 'Merge.'

![Dubbing Studio Merge](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/44afe6659b3ea14d9baa16e735725759ced84469ed8d66a5a708f33950363a8f/assets/images/product-guides/dubbing/dubbing-studio-split-merge.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=e6e05ed55b2372a251d3f7ee0932b0d667b532e21e5bcd2b8f80cc33903afd74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

As you split and merge clips, the speaker cards above the timeline will update to reflect these changes.

### Reassign clips to different speakers

To reassign a clips to a different speaker, click the segment and drag it to another track.

![Dubbing Studio Reassign Clips](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/93fc997eba2a8a3e7ec831731cae6a20d3c55df45e5818b9629bb1dcf4d3b519/assets/images/product-guides/dubbing/dubbing-studio-reassign.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=bb47c111d7b6b3d9dc01851938204200e7b7b3c729d1849559c65bf18f1c1fca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Add additional audio tracks

Use the action buttons at the bottom of the timeline to add new audio tracks

![Dubbing Studio Add Tracks](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6144bb02bb8a9da95cd4fbf76d9df479b2174e83fb8569bdeaf9b14743d19cdf/assets/images/product-guides/dubbing/dubbing-studio-add-tracks.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=ed5b669fbf44ea58d5484765626d477c519c54d7beaa9e06b60d4e92fc3b27cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Voice Settings

## Voice Settings

### Voice Selection

To select the voice that will be used to generate audio on a specific speaker track, click the settings cog icon on the left side of the timeline near the speaker name.

There are 3 main types of voices to choose from in Dubbing Studio:

1. Clip clone - this creates a unique voice clone for each clip based on the source audio for that clip
2. Track clone - this creates a single voice clone for the whole track based on all source audio for a given speaker
3. Other voices - you can also choose from thousands of voices available in our Voice Library, each with detailed metadata and tags to help you choose the right one

You can also create, save, and reuse a voice from a specific clip by right clicking the clip and selecting 'Create Voice from Selection.'

### Setting Track vs. Clip Level Settings

You can set voice settings at two levels:

1. Track Level - changes will apply across all clips in the track, which can help with stability and consistency.

2. Clip Level - changes will only apply to a specific clip. To set clip-level settings, use the panel on the right side of the timeline.
   Disable the 'inherit track settings' toggle and configure your desired settings.

![Dubbing Studio Voice
Settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b4d2221711308a019b150e06634b62a9d9161ac9f51662d0aa3aaeb95e623b81/assets/images/product-guides/dubbing/dubbing-studio-clip-settings.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T203357Z&X-Amz-Expires=604800&X-Amz-Signature=de7ed27ada1f3c8bf5e4bfdda8b16efce0ea64027f0ba7152b7f4f3c6d91b417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Exports

## Exports

Click 'Export' in the bottom right of Dubbing Studio to open the export menu.

Dubbing Studio currently supports the following export formats:

* AAC (audio)
* MP3 (audio)
* WAV (audio)
* .zip of audio tracks
* .zip of audio clips
* AAF (timeline data)
* SRT (subtitles/captions)
* CSV (speaker, start\_time, end\_time, transcription, translation)

<b>Make sure you select the correct language</b> when exporting.

## Additional Features

* **Voiceover Tracks:** Voiceover tracks create new Speakers. You can click and add clips on the timeline wherever you like. After creating a clip, start writing your desired text on the speaker cards above. You'll first need to translate that text, then you can press "Generate". You can also use our voice changer tool by clicking on the microphone icon on the right side of the screen to use your own voice and then change it into the selected voice.
* **SFX Tracks:** Add a SFX track, then click anywhere on that track to create a SFX clip. Similar to our independent SFX feature, simply start writing your prompt in the Speaker card above and click "Generate" to create your new SFX audio. You can lengthen or shorten SFX clips and move them freely around your timeline to fit your project - make sure to press the "stale" button if you do so.
* **Upload Audio:** This option allows you to upload a non voiced track such as sfx, music or background track. Please keep in mind that if voices are present in this track, they won't be detected so it will not be possible to translate or correct them.

## Manual Dub

In cases where you already have an accurate dubbing script prepared and want to ensure your Dubbing Studio project sticks to your
exact clips and speaker assignment, you can use the <b>Manual Dub</b> option during creation.

To create a Manual Dub, you'll need:

1. Video file
2. Background audio file
3. Foreground audio file
4. CSV where each row contains a speaker, start\_time, end\_time, transcription, and translation field

The CSV file must strictly follow the predefined format in order to be processed correctly. Please see below for samples in the three supported timecodes:

* seconds
* hours:minutes:seconds:frame
* hours:minutes:seconds,milliseconds

### Example CSV files

```csv seconds
speaker,start_time,end_time,transcription,translation
Adam,"0.10000","1.15000","Hello, how are you?","Hola, ¿cómo estás?"
Adam,"1.50000","3.50000","I'm fine, thank you.","Estoy bien, gracias."

```

```csv hours:minutes:seconds:frame
speaker,start_time,end_time,transcription,translation
Adam,"0:00:01:01","0:00:05:01","Hello, how are you?","Hola, ¿cómo estás?"
Adam,"0:00:06:01","0:00:10:01","I'm fine, thank you.","Estoy bien, gracias."

```

```csv hours:minutes:seconds,milliseconds
speaker,start_time,end_time,transcription,translation
Adam,"0:00:01,000","0:00:05,000","Hello, how are you?","Hola, ¿cómo estás?"
Adam,"0:00:06,000","0:00:10,000","I'm fine, thank you.","Estoy bien, gracias."

```

| speaker | start\_time | end\_time   | transcription                     | translation                                  |
| ------- | ----------- | ----------- | --------------------------------- | -------------------------------------------- |
| Joe     | 0:00:00.000 | 0:00:02.000 | Hey!                              | Hallo!                                       |
| Maria   | 0:00:02.000 | 0:00:06.000 | Oh, hi, Joe. It has been a while. | Oh, hallo, Joe. Es ist schon eine Weile her. |
| Joe     | 0:00:06.000 | 0:00:11.000 | Yeah, I know. Been busy.          | Ja, ich weiß. War beschäftigt.               |
| Maria   | 0:00:11.000 | 0:00:17.000 | Yeah? What have you been up to?   | Ja? Was hast du gemacht?                     |
| Joe     | 0:00:17.000 | 0:00:23.000 | Traveling mostly.                 | Hauptsächlich gereist.                       |
| Maria   | 0:00:23.000 | 0:00:30.000 | Oh, anywhere I would know?        | Oh, irgendwo, das ich kenne?                 |
| Joe     | 0:00:30.000 | 0:00:36.000 | Spain.                            | Spanien.                                     |

## FAQ

<tbody>
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
      #### How do I access Dubbing Studio?

      By default, when you create a new dub, our latest Dubbing v2 model will be used. Dubs created using the v2 model are completely automatic without any option to edit the content.

      If you want to use Dubbing Studio, you can do this by selecting <strong>Use legacy v1 Dubbing model</strong> in the <strong>Advanced</strong> options when you create your dub, then check the <strong>Create Dubbing project</strong> option. 

      <img src="https://help.elevenlabs.io/hc/article_attachments/38961100866449" alt="" />

      It's not possible to convert an existing automatic dub to a Dubbing project.

      The new dubbing project will appear at the top of your list of dubbing projects, and will go through various stages while generating.

      Once it has completed processing, click the three dots icon and select <strong>Edit</strong> to open your dubbing project.

      <img src="https://help.elevenlabs.io/hc/article_attachments/47309511976593" alt="" />

      For more information about Dubbing Studio, please see our [overview.](/docs/product-guides/products/dubbing/dubbing-studio)
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

  <tr>
    <td>
      #### Why can't I download my dubs?

      If you can't download dubbed audio or video, try a different browser and turn off ad blockers and pop-up blockers.

      This issue is most often reported with the Brave browser, but it can also occur in others. In most cases, switching browsers or disabling blockers resolves the problem.
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
      #### Do you offer lip sync?

      At the moment, ElevenLabs does not offer lip syncing as part of Dubbing. Lip sync is available in Image & Video, Flows, and Studio via third party models.
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
      #### On what plans can I use Dubbing?

      Dubbing is available on all our plans, including the free plan. Dubs generated on free plans are automatically watermarked, with no option to remove this. Watermarking is not available on our paid subscriptions.
    </td>
  </tr>

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
</tbody>
