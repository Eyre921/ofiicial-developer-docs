---
title: "Sound effects"
source: https://elevenlabs.io/docs/eleven-creative/playground/sound-effects.md
path: docs/eleven-creative/playground/sound-effects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Sound effects

## Overview

**Sound effects** enhance the realism and immersion of your audio projects. With ElevenLabs, you can generate sound effects from text and integrate them into your voiceovers and projects.

## Guide

#### Navigate to Sound Effects

Head over to [Sound Effects](https://elevenlabs.io/app/sound-effects). You can find it under
**Playground** in the sidebar.

#### Describe the sound effect

In the text box, type a description of the sound effect you want (e.g., "person walking on
grass").

#### Adjust settings

![Sound effects
settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3b14346a7ee375acc01d11b4ebb0ec0127a4a65bfab8e708d77ae5e639e64f38/assets/images/product-guides/sound-effects/sound-effects-settings.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T222742Z&X-Amz-Expires=604800&X-Amz-Signature=ad2e9f6851aaba3032a8c2f2a52f9306e6531b27c49f48b5584d66752c5d723e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<ul>
  <li>
    Set the duration for the sound, or choose auto to let the AI decide. The maximum length is
    30 seconds.
  </li>

  <li>
    Turn <strong>Looping</strong> on to create a seamless loop. The ending will blend into the
    beginning without a noticeable gap.
  </li>

  <li>
    Adjust the prompt influence setting to control how closely the output should match the
    prompt. By default, this is set to 30%.
  </li>
</ul>

#### Generate sound

Click the arrow to generate. Four sound effects will be created each time.

#### Review and regenerate

Go to your **History** tab to access the generated sound effects. Click the **download** icon
and choose MP3 (44.1kHz) or WAV (48kHz). You can also click the **star** icon to save to your
favorites, so you can access it again from your **Favorites** tab. If needed, adjust the prompt
or settings and regenerate.

**Exercise**: Create a sound effect using the following prompt: Old-school funky brass stabs from
a vinyl sample, stem, 88 bpm in F# minor.

## Explore the library

![Sound effects explore](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d8d7c3cca84e6acb0dfc419aed291be764794f299b2c7c478a9efc3f8f6e25ef/assets/images/product-guides/sound-effects/sound-effects-explore.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T222742Z&X-Amz-Expires=604800&X-Amz-Signature=fefb82f5402889f2f15dd26aa626d8c1824c28282f0db6a241a0355c3a416278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Browse community-made sound effects in the **Explore** tab.

For more on prompting and how sound effects work, visit our [overview page](/docs/overview/capabilities/sound-effects).

## FAQ

<tbody>
  <tr>
    <td>
      #### What is Sound Effects?

      Our sound effects generator allows you to generate any sound imaginable by inputting a prompt.  Create anything from blockbuster sound design for films, to everyday sounds for your video game.

      To get started, visit [Sound Effects](https://elevenlabs.io/app/sound-effects) or select 'Sound Effects' in the sidebar on the left while logged into your account. 

      Enter your prompt in the text box.  There is a maximum length of 450 characters for your prompt.  

      You can use the settings to control the duration of the sound effect, and how strictly the AI follows your prompt.  If you don't specify the length of the clip, the AI will decide the audio length.

      Each time you select <strong>Generate</strong>, the AI will generate full variations of the prompt you've given.

      You can create looping sound effects if you need longer durations. Looping sound effects can be played on repeat without a perceptible start or end point.

      For more details, please see our full [overview of Sound Effects.](/docs/overview/capabilities/sound-effects)
    </td>
  </tr>

  <tr>
    <td>
      #### How much does it cost to generate sound effects?

      The cost for generating sound effects varies based on the settings you choose, and whether you are using the website or API platform. The settings affect how many sound effects are produced and the duration of each sound effect.

      <strong>
        For Website Users:
      </strong>

      * Each generation produces 4 sound effects.
      * By default, the AI decides the duration of the sound effect, costing 200 credits per generation.
      * If you set the duration yourself, the cost is 40 credits per second of sound effect duration, with a maximum duration of 30 seconds.

      <strong>
        For API Users:
      </strong>

      * Each generation produces 1 sound effect.
      * By default, the AI decides the duration of the sound effect, costing 100 credits per generation.
      * If you set the duration yourself, the cost is 11 credits per second of sound effect duration, with a maximum duration of 30 seconds.

      The cost is not influenced by the text input you use.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I prompt for sound effects?

      The prompt is the piece of text or instruction that tells the AI what kind of output is expected.  The AI understands natural language as well as audio terminology.

      <strong>
        Simple Prompts
      </strong>

      These are simple prompts that try to get the AI to generate a single sound effect.  Some examples would be "person walking on grass" or "glass breaking".  These types of prompts will generate a single type of sound effect with a few variations.

      You can improve these prompts by adding a little more detail, for example, “high-quality, professionally recorded footsteps on grass, sound effects foley.” It can require some experimentation to find a good balance between being descriptive and keeping it brief enough to have AI understand the prompt.

       

      <strong>
        Complex Prompts
      </strong>

      Complex prompts include multiple sound effects, or a sequence of sound effects happening in a specific order, for example, "A man walks through a hallway and then falls down some stairs".  While the AI does understand these prompts, for the best results, we would recommend generating individual sound effects and then combining them in an audio editor of your choice.

       

      For more details on how to prompt for sound effects, along with examples and audio terminology that might be useful for writing prompts, please see our full [overview of Sound Effects.](/docs/capabilities/sound-effects)
    </td>
  </tr>
</tbody>
