---
title: "Voiceover studio"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/voiceover-studio.md
path: docs/eleven-creative/audio-tools/voiceover-studio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voiceover studio

Voiceover Studio will be sunset on **May 15, 2026**. For all new projects, use [ElevenCreative
Studio](/docs/eleven-creative/products/studio). You can also open Studio directly at
[elevenlabs.io/app/studio](https://elevenlabs.io/app/studio).

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/051b3139b84d462fcaa5bcf11d7ca2e7be093fa226ac08e7d827c447ee97ae4a/assets/images/product-guides/voiceover-studio/voiceover-studio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T100017Z&X-Amz-Expires=604800&X-Amz-Signature=04f704668e04387918bf722b6e5590e91bb5fbfcc500879eaff01a2c895b3e4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Voiceover studio" />

## Overview

Voiceover Studio combines the audio timeline with our Sound Effects feature, giving you the ability to write a dialogue between any number of speakers, choose those speakers, and intertwine your own creative sound effects anywhere you like.

## Guide

#### Navigate to the Voiceover studio

In the ElevenLabs dashboard, click on the "Voiceover Studio" option in the sidebar under "Audio
Tools".

#### Create a new voiceover

Click the "Create a new voiceover" button to begin. You can optionally upload video or audio to
create a voiceover from.

#### Modify the voiceover with the timeline

On the bottom half of your screen, use the timeline to add and edit voiceover clips plus add
sound effects.

#### Export your voiceover

Once you're happy with your voiceover, click the "Export" button in the bottom right, choose the
format you want and either view or download your voiceover.

## FAQ

<tbody>
  <tr>
    <td>
      #### How does the timeline work?

      ### Timeline

      The timeline is a linear representation of your Voiceover project. Each row represents a track, and on the far left section you have the track information for voiceover or SFX tracks. In the middle, you can create the clips that represent when a voice is speaking or a SFX is playing. On the right-hand side, you have the settings for the currently selected clip.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I add tracks?

      ### Adding Tracks

      To add a track, click the "Add Track" button in the bottom left of the timeline. You can choose to add a voiceover track or an SFX track.

      There are three types of tracks you can add in the studio: Voiceover tracks, SFX tracks and uploaded audio.

      * **Voiceover Tracks:** Voiceover tracks create new Speakers. You can click and add clips on the timeline wherever you like. After creating a clip, start writing your desired text on the speaker cards above and click "Generate". Similar to Dubbing Studio, you will also see a little cogwheel on each Speaker track - simply click on it to adjust the voice settings or replace any speaker with a voice directly from your Voices - including your own Professional Voice Clone if you have created one.

      * **SFX Tracks:** Add a SFX track, then click anywhere on that track to create a SFX clip. Similar to our independent SFX feature, simply start writing your prompt in the Speaker card above and click "Generate" to create your new SFX audio. You can lengthen or shorten SFX clips and move them freely around your timeline to fit your project - make sure to press the "stale" button if you do so.

      * **Uploaded Audio:** Add an audio track including background music or sound effects. It's best to avoid uploading audio with speakers, as any speakers in this track will not be detected, so you won't be able to translate or correct them.
    </td>
  </tr>

  <tr>
    <td>
      #### How does this differ from Dubbing Studio?

      ### Key Differences from Dubbing Studio

      If you chose not to upload a video when you created your Voiceover project, then the entire timeline is yours to work with and there are no time constraints. This differs from Dubbing Studio as it gives you a lot more freedom to create what you want and adjust the timing more easily.

      When you Add a Voiceover Track, you will instantly be able to create clips on your timeline. Once you create a Voiceover clip, begin by writing in the Speaker Card above. After generating that audio, you will notice your clip on the timeline will automatically adjust its length based on the text prompt - this is called "Dynamic Generation". This option is also available in Dubbing Studio by right-clicking specific clips, but because syncing is more important with dubbed videos, the default generation type there is "Fixed Generation," meaning the clips' lengths are not affected.
    </td>
  </tr>

  <tr>
    <td>
      #### How are credits deducted with Voiceover Studio?

      ### Credit Costs

      Voiceover Studio does not deduct credits to create your initial project. Credits are deducted every time material is generated. Similar to Speech-Synthesis, credit costs for Voiceover Clips are based on the length of the text prompt. SFX clips will deduct 80 credits per generation.

      If you choose to Dub (translate) your Voiceover Project into different languages, this will also cost additional credits depending on how much material needs to be generated. The cost is 1 credit per character for the translation, plus the cost of generating the new audio for the additional languages.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I upload a script?

      ### Uploading Scripts

      With Voiceover Studio, you have the option to upload a script for your project as a CSV file. You can either include speaker name and line, or speaker name, line, start time and end time. To upload a script, click on the cog icon in the top right hand corner of the page and select "Import Script".

      Scripts should be provided in the following format:

      ```
      speaker,line
      ```

      Example input:

      ```
      speaker,line
      Joe,"Hey!"
      Maria,"Oh, hi Joe! It's been a while."
      ```

      You can also provide start and end times for each line in the following format:

      ```
      speaker,line,start_time,end_time
      ```

      Example input:

      ```
      speaker,line,start_time,end_time
      Joe,"Hey!",0.1,1.5
      Maria,"Oh, hi Joe! It's been a while.",1.6,2.0
      ```

      Once your script has imported, make sure to assign voices to each speaker before you generate the audio. To do this, click the cog icon in the information for each track, on the left.

      If you don't specify start and end times for your clips, Voiceover Studio will estimate how long each clip will be, and distribute them along your timeline.
    </td>
  </tr>

  <tr>
    <td>
      #### What's the difference between Dynamic Duration and Fixed Duration?

      ### Dynamic Duration

      By default, Voiceover Studio uses Dynamic Duration, which means that the length of the clip will vary depending on the text input and the voice used. This ensures that the audio sounds as natural as possible, but it means that the length of the clip might change after the audio has been generated. You can easily reposition your clips along the timeline once they have been generated to get a natural sounding flow. If you click "Generate Stale Audio", or use the generate button on the clip, the audio will be generated using Dynamic Duration.

      This also applies if you do specify the start and end time for your clips. The clips will generate based on the start time you specify, but if you use the default Dynamic Duration, the end time is likely to change once you generate the audio.

      ### Fixed Duration

      If you need the clip to remain the length specified, you can choose to generate with Fixed Duration instead. To do this, you need to right click on the clip and select "Generate Audio Fixed Duration". This will adjust the length of the generated audio to fit the specified length of the clip. This could lead to the audio sounding unnaturally quick or slow, depending on the length of your clip.

      If you want to generate multiple clips at once, you can use shift + click to select multiple clips for a speaker at once, then right click on one of them to select "Generate Audio Fixed Duration" for all selected clips.
    </td>
  </tr>

  <tr>
    <td>
      #### What is Voiceover Studio?

      Similar to Dubbing Studio, Voiceover Studio gives users an opportunity to create their own interactive content, but with a little more freedom. Voiceover Studio combines the audio timeline with our Sound Effects feature, giving you the ability to write a dialogue between any number of speakers, choose those speakers, and intertwine your own creative sound effects anywhere you like.

      To begin, you first have the option to upload a video or to create your Voiceover from scratch. After that, it’s as simple as pressing “Create Studio” - you can name your Voiceover before or after it’s created.

      Once inside, you'll see your audio timeline.  This is a linear representation of your Voiceover project. Each row represents a track, and there are two types of track you can add: Voiceover tracks and SFX tracks.

      Once you've added tracks, you can then add clips, which will be represented by speaker cards.

      For a more in-depth explanation and guide on what Voiceover Studio is and how to use it, we recommend reading our full [overview of Voiceover Studio.](/docs/product-guides/audio-tools/voiceover-studio)

      Voiceover Studio is available on the Creator plan and above.
    </td>
  </tr>

  <tr>
    <td>
      #### How much does Voiceover Studio cost?

      Creating a Voiceover project does not deduct any quota.  Once you've created your project, quota will be deducted every time material is generated.  Similar to Speech Synthesis, quota costs for voiceover clips are based on the length of the text prompt.  SFX clips will deduct 100 quota per generation.

      If you choose to Dub (translate) your Voiceover project into different languages, this will also cost additional quota depending on how much material needs to be generated.
    </td>
  </tr>
</tbody>
