---
title: "Music"
source: https://elevenlabs.io/docs/eleven-creative/products/music.md
path: docs/eleven-creative/products/music
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Music

## Overview

Eleven Music offers an end-to-end workflow for music creation. Generate songs in any style and at your desired length
using natural language prompts. You can also add an Audio Reference or select a curated or custom
[Music Finetune](/docs/eleven-creative/products/music/finetunes) to guide the sound and stylistic identity of your
generation.

Refine individual sections, lyrics, styles, and song structure with intuitive editing tools. Once complete, download
your track as a high-quality audio file or share it using a customizable visualizer.

## Guide

#### Create a new song

Describe your song using natural language prompts. Refer to our [Prompting
Guide](/docs/overview/capabilities/music/best-practices) for best practices on style and lyrics.

#### Add an Audio Reference (optional)

Upload a short audio track (up to approximately 30 seconds) to guide the style and sound of your Music v2
generation. Every uploaded reference is screened for copyright compliance. Audio Reference influences sound,
production style, instrumentation, tempo, and mood — it does not copy or remix the uploaded audio.

#### Select a Finetune (optional)

Choose a Finetune to shape the stylistic identity of your generation. You can select from:

* **Curated Finetunes** - Pre-trained Finetunes across global genres and styles created by
  ElevenLabs
* **Custom Finetunes** - Finetunes you’ve created using your own original audio

If you don't select a Finetune, the standard music model will be used. Learn more about
[creating custom Finetunes](/docs/eleven-creative/products/music/finetunes).

#### Select settings

Choose the number of **Variants** and the **Duration**. You can select a fixed length (e.g.,
30s, 1m) or **Auto** for a dynamically determined length. For building complex songs, a workflow
we've seen often is to start with a short duration like **30s** and iteratively adding new
sections as you work on the song.

#### Make edits

Refine your track in the editor. You can edit lyrics, add or remove sections, adjust section
durations, apply style keywords, or use direct conversational prompts for granular creative
control. You can even generate completely new variations of the exact same prompt if you want a
different track based on the same prompt in the same music project, or a different base to work
from.

#### Download and share

Click the **Download** button to save your high-fidelity audio file, or use the **Share** button
to generate a link with a customizable visualizer for your track.

## What can I generate with Eleven Music?

Eleven Music is a versatile model that gives you control over many aspects of music creation. You can generate:

#### Full Songs with Vocals

#### Full Songs with Vocals

Create complete tracks with AI-generated lyrics and vocals in multiple languages, including English, Spanish,
German, and Japanese. Music v2 supports more natural vocal performances and more complex delivery patterns,
including fast rap and dense lyrical phrasing. You can provide your own lyrics or ask the model to generate
lyrics based on your prompt.

#### Instrumental Tracks

#### Instrumental Tracks

Generate purely instrumental music across any genre, from cinematic
scores to ambient lo-fi beats. Perfect for background music, film scores, or any project
requiring instrumental accompaniment.

#### Specific Song Structures

#### Specific Song Structures

Use sectional descriptions in your prompt to build songs piece by
piece, defining the Intro, Verse, Chorus, Breakdown, and Outro. This gives you granular control
over your song's composition and flow.

#### Music for Media

#### Music for Media

Design custom soundtracks for videos, advertisements, games, or other media
by describing the scene or mood. For example: "A high-intensity orchestral track for an epic
battle scene" or "Upbeat corporate jingle for a tech startup."

#### Genre-Specific Music

#### Genre-Specific Music

Generate highly specific styles by including detailed prompts, such as
"Traditional Spanish flamenco with palmas, nylon guitar, and Spanish-language vocals" or "1980s
synthwave with analog synthesizers and retro drum machines."

## Editing and Refinement

Once you've generated your initial track, Eleven Music provides powerful editing tools to refine every aspect
of your composition.

#### Adding and Removing Sections

#### Adding and Removing Sections

**Adding a New Section:**

* To insert a section between existing ones, hover over the section in the section view and click the
  **"+ Add Section"** icon that appears. This will add a section after the current section.
* To add a section at the end of your track, scroll to the end of the timeline and click the **"+"** button.
* Drag the new section in the timeline to adjust its duration.

**Removing a Section:**

* Hover over the section you wish to remove in the song structure view.
* Click the delete icon (X) that appears in the corner of the section block.

#### Editing Lyrics and Prompts

#### Editing Lyrics and Prompts

To change the lyrics or instrumental prompts of any existing section:

* Click inside the text box for that section (e.g., Intro, Main Theme).
* Type your new lyrics or edit the existing prompt.
* Use bracketed descriptions like "\[energetic guitar solo]" or "\[drum fill]" for instrumental parts.

#### Style Control

#### Style Control

For advanced control over specific musical elements:

* Hover over the section you want to edit and click **"Edit styles of this section"**.
* In the "Section styles" window, you can:
  * **Include styles:** Add specific musical characteristics like "gradual filter cutoff",
    "hi-hats fade out", or "long delay feedback on vocals."
  * **Exclude styles:** Prevent certain elements like "abrupt ending" or "new elements."
* Click **Save** to apply these style rules to that specific section.

#### Direct Prompting

#### Direct Prompting

Use the conversation interface at the bottom of the editor to make specific changes with natural language:

* Type direct instructions like "Make the chorus more energetic" or "Add a guitar solo after the second verse."
* This allows for creative editing beyond the structured tools.

#### Regenerating Changes

#### Regenerating Changes

After making any edits—whether adding, deleting, or modifying sections—your changes are staged but not yet applied to the audio.

* Your edits will **not** take effect until you click the **Generate** button.
* Once you click **Generate**, the model creates a new version of the song incorporating all your changes.
* Feel free to experiment with different combinations of lyrics, styles, and structures between generations.

## Best Practices for Prompting

The key to great results is a descriptive and detailed prompt. The more information you provide, the closer the output will be to your vision.

#### Be Specific with Genre and Style

#### Be Specific with Genre and Style

Instead of generic terms like "rock music," try detailed descriptions:

* "Energetic 1980s synth-pop with a driving drum machine beat and male vocals"
* "Melancholic indie folk with fingerpicked acoustic guitar and ethereal female harmonies"
* "Heavy metal with palm-muted riffs, double bass drums, and aggressive vocals"

#### Layer Multiple Descriptors

#### Layer Multiple Descriptors

Combine mood, instrumentation, tempo, and use case for better results:

* "A slow, melancholic piano melody over ambient synth textures, suitable for a tragic film scene"
* "Upbeat corporate jingle with bright synthesizers, punchy drums, and an optimistic melody"
* "Dark, atmospheric electronic track with deep bass, glitchy percussion, and haunting vocal samples"

#### Define Instrumentation

#### Define Instrumentation

Call out specific instruments you want to hear:

* "Upbeat funk track with a prominent slap bass line, funky rhythm guitar, and a horn section"
* "Classical string quartet with violin, viola, and cello"
* "Jazz ensemble with piano, upright bass, brushed drums, and tenor saxophone"

#### Use Include/Exclude Styles

#### Use Include/Exclude Styles

Refine your output by explicitly including or excluding certain elements at the track or section level:

* **Include:** "acoustic," "four-on-the-floor kick", "reverb-heavy vocals", "analog warmth"
* **Exclude:** "repetitive structure", "electronic elements", "abrupt ending", "distorted vocals"

#### Build Section by Section

#### Build Section by Section

For maximum control, start with a short generation (e.g., 30 seconds for an Intro)
and build your song piece by piece.

1. Generate the **Intro** and refine until satisfied.
2. Click **"+ Add Section"** to add the next part.
3. Specify the style and content for the new section (e.g., Verse, Chorus, Bridge).
4. Use the conversation interface for specific instructions on each part.
5. Build your track progressively, ensuring each section flows naturally.

#### Iterate and Refine

#### Iterate and Refine

Don't start over if the first generation isn't perfect. Small changes can have a big impact.

* Adjust your prompt and regenerate specific sections.
* Use the editing tools to fine-tune individual parts.
* Experiment with different style combinations.

## Use Cases & Commercial Use

Created in collaboration with artists, labels, and publishers, Eleven Music is, under certain subscriptions and conditions,
**cleared for broad commercial use**. This model allows users to move beyond stock music libraries and create bespoke audio
tailored to their specific needs.

For specific details on supported usage per tier, please refer to our [Music
Terms](https://elevenlabs.io/music-terms).

## Export and Quality

When you're satisfied with your composition, use the **Download** button to export your track.

#### Export Formats

#### Export Formats

Generated audio is provided in MP3 format with professional-grade quality (44.1kHz, 128-192kbps).
Other audio formats will be supported soon.

#### Quality Settings

#### Quality Settings

Export quality varies by subscription tier:

* **Free, Starter, and Creator:** Standard quality exports.
* **Pro, Scale, Business, and Enterprise:** High-fidelity, studio-grade exports.
  All exports maintain the full dynamic range and frequency response of the original generation.

#### Sharing

#### Sharing

Use the **Share** button to:

* Generate a shareable link to your song.
* Customize the visualizer that accompanies your track.
* Share your creations with collaborators or audiences.

## Music v2

Music v2 is the default model in the Eleven Music interface. It offers improved prompt adherence, composition, prompt understanding, multilingual output, and vocal delivery over Music v1.

Music v2 capabilities include:

* Audio Reference for guiding a generation with a short uploaded track
* Long-form, section-by-section composition
* Mid-track genre transitions
* Fast rap and complex vocal delivery
* Improved inpainting
* Sound effects embedded inside tracks

Audio Reference is available on all Music v2 plans, including Free. Every uploaded reference track is screened for copyright compliance.

## Availability & API Access

Eleven Music is available today for all users on the ElevenLabs website. The intuitive interface makes it easy to create professional-quality music without technical expertise.

**API Access:** The Music API is available for paid subscribers.

Visit our [Music Product Page](https://elevenlabs.io/music) for the latest information and to
start creating.

## FAQ

<tbody>
  <tr>
    <td>
      #### How long can my generated songs be?

      You can create everything from short clips to full-length tracks. For maximum control, you can
      start with a short duration like **30s** to create an initial section, then iteratively use the
      **"+ Add Section"** button to build out your song piece by piece, extending it to your desired
      length.

      The minimum duration of a song is 3 seconds and the maximum is 10 minutes.
    </td>
  </tr>

  <tr>
    <td>
      #### What languages are supported for vocals?

      Eleven Music supports vocals in multiple languages including English, Spanish, German, and
      Japanese. The model can generate lyrics in these languages, or you can provide your own lyrics for
      the AI to sing.
    </td>
  </tr>

  <tr>
    <td>
      #### What is Eleven Music?

      Eleven Music is our AI model for generating high-fidelity, studio-grade music from natural language prompts.

      Eleven Music offers:

      * <strong>Complete Music Tracks</strong> from a single text prompt
      * <strong>Granular Control</strong> of genre, mood, style, structure, and instrumentation
      * <strong>Vocals & Lyrics</strong> across multiple languages, including English, Spanish, German,
        and Japanese, with Music v2 supporting more natural vocal performances and complex delivery
        patterns such as fast rap
      * <strong>Audio Reference</strong> to guide Music v2 generations with a short uploaded track
      * <strong>Post-Generation Editing</strong> to adjust sections and lyrics of those sections via the
        UI
      * <strong>Studio-Ready Exports</strong> in MP3 for professional workflows

      ### Use Cases & Commercial Use

      Created in collaboration with artists, labels, publishers, and artists, Eleven Music is <strong>cleared for broad commercial use</strong>.

      This model allows users to move beyond stock music libraries and create bespoke audio. For specific details on supported usage per tier, please refer to our [Music Terms](https://elevenlabs.io/music-terms).

      ### Availability & API Access

      Eleven Music is available today for all users on the ElevenLabs website.

      API access is available for all users on paid subscription plans. See our [API documentation](/docs/cookbooks/music/quickstart) for more information. 

      Visit the following resources for more information:

      * [Eleven Music Product Page](/docs/product-guides/products/music)
      * [Eleven Music Prompting Guide](/docs/overview/capabilities/music/best-practices)
      * [Eleven Music Usage Terms](https://elevenlabs.io/music-terms)
    </td>
  </tr>

  <tr>
    <td>
      #### What can I generate with Eleven Music?

      Eleven Music is a versatile model that gives you control over many aspects of audio creation. You can generate:

      * <strong>Full Songs with Vocals:</strong> Create complete tracks with AI-generated lyrics and
        vocals in a variety of languages. Music v2 supports more natural vocal performances and more
        complex delivery patterns, including fast rap and dense lyrical phrasing.
      * <strong>Instrumental Tracks:</strong> Generate purely instrumental music across any genre, from
        cinematic scores to ambient lo-fi beats.
      * <strong>Specific Song Structures:</strong> Use sectional generation to build a song piece by
        piece, defining the Intro, Verse, Chorus, Breakdown, and Outro.
      * <strong>Music for Media:</strong> Design custom soundtracks for videos, ads, or games by
        describing the scene or mood (e.g., "A high-intensity orchestral track for an epic battle scene").
      * <strong>Genre-Specific Music:</strong> Generate highly specific styles by including detailed
        prompts, such as "Traditional Spanish flamenco with palmas, nylon guitar, and Spanish-language
        vocals."
    </td>
  </tr>

  <tr>
    <td>
      #### How much does Eleven Music cost?

      The cost of Eleven Music depends on the length of your track and how many variants you're generating. You can see how much each generation will cost before you click <strong>Generate</strong> by hovering over the number of <strong>credits remaining</strong> for your account. 

      For a breakdown of how many minutes of Music each of our subscription plans can generate with the included credit quota, see the Music table on our [Pricing page. ](https://elevenlabs.io/pricing)
    </td>
  </tr>

  <tr>
    <td>
      #### Are there any best practices for prompting Eleven Music?

      The key to great results is a descriptive and detailed prompt. The model understands nuance, so the more information you provide, the closer the output will be to your vision. Here are some best practices:

      * <strong>Be Specific with Genre and Style:</strong> Instead of `rock music`, try `energetic 1980s
        synth-pop with a driving drum machine beat and male vocals`.
      * <strong>Layer Multiple Descriptors:</strong> Combine mood, instrumentation, tempo, and use case.
      * Example: `A slow, melancholic piano melody over ambient synth textures, suitable for a tragic film scene`.
      * <strong>Define Instrumentation:</strong> Call out the specific instruments you want to hear.
      * Example: `Upbeat funk track with a prominent slap bass line, funky rhythm guitar, and a horn section`.
      * <strong>Use the "Include/Exclude Styles" Feature:</strong> Refine your output by explicitly
        including or excluding certain tags like acoustic, repetitive structure, or four-on-the-floor
        kick.
      * <strong>Build Section by Section:</strong> To have the most control when creating a full song,
        generate the Intro first. Once you're happy with that first section, you can click the "+" sign
        and specify the style for the next part. Then, use the "Continue the conversation..." prompt box
        to generate the Main Groove or Chorus, building your track piece by piece.
      * <strong>Iterate and Refine:</strong> If the first generation isn't perfect, don't start over!
        Adjust your prompt and regenerate. Small changes can have a big impact.

      For a complete list of tips and examples, please see our official [Prompting Guide](/docs/overview/capabilities/music/best-practices).
    </td>
  </tr>

  <tr>
    <td>
      #### How can I edit my track, add or remove sections, or change the style of a specific part in Eleven Music?

      Eleven Music gives you granular control to edit your song composition without having to start over. You can easily add new parts, edit lyrics, delete sections, and even fine-tune the musical style of each individual section.

      Here’s a step-by-step guide to editing your track:

      <strong>
        1\. Adding a New Section
      </strong>

      To add a new part to your song (like a bridge, a solo, or a second verse):

      * To add a new section, there are two ways to achieve this:

      * In the song structure, find the section you want the new section to follow. On the left-hand side of that section, you'll see a "+" symbol that will say "Add section below" when you hover over.<br />

        <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6c23aeecbe607b133b6940ae30a60ba168772a8c351f68cfa42cec1f8705c95c/assets/images/help-center/product/core-capabilities/music/how-can-i-edit-my-track-add-or-remove-sections-or-change-the-style-of-a-specific-part-in-eleven-music.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260826T200253Z&X-Amz-Expires=604800&X-Amz-Signature=1a42a6ae3c39a77512443588e030f7b0e744d71151b26baf397419e6cac856d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

      * In the timeline, scroll to the end of your song structure and click the "+" sign, which will add a new empty section at the end.<br />

        <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/071d9a8998758844dd15d1c512c5bbd3d335950c7b4ca784604182042eb14c80/assets/images/help-center/product/core-capabilities/music/how-can-i-edit-my-track-add-or-remove-sections-or-change-the-style-of-a-specific-part-in-eleven-music-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260826T200253Z&X-Amz-Expires=604800&X-Amz-Signature=afa939d5328da4cbae7492a81f71d8868fdd325ddab2f00cf64f7201658adcb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

      * Once you've added this new empty section, you can drag it to extend the duration, add lyrics, or a descriptive prompt (e.g., "\[energetic guitar solo]").

      <strong>
        2\. Editing Lyrics or Prompts
      </strong>

      To change the lyrics or the instrumental prompt of any existing section:

      * Simply click inside the text box for that section (e.g., Main Groove 1, Breakdown).
      * Type your new lyrics or edit the existing prompt.

      <strong>
        3\. Modifying the Style of a Section
      </strong>

      For more advanced control, you can define specific musical elements to include or exclude from a section.

      * Hover over the section you want to edit and click the <strong>"Edit styles of this section"</strong> link.<br />

        <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c9086f7935759344e852854e10af5a38b27760359897a7c315824c1c6e2ef124/assets/images/help-center/product/core-capabilities/music/how-can-i-edit-my-track-add-or-remove-sections-or-change-the-style-of-a-specific-part-in-eleven-music-3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260826T200253Z&X-Amz-Expires=604800&X-Amz-Signature=60252422c01297c581a1f2039e2c056e91e8d963bb92e2c6146135d85198d0cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

      * A "Section styles" window will pop up. Here you can:

      * <strong>Include styles:</strong> Add specific musical characteristics or production details. For
        example: gradual filter cutoff, hi-hats fade out, long delay feedback on vocalise.

      * <strong>Exclude styles:</strong> Prevent certain elements from appearing. For example: abrupt
        ending, new elements.

      * Click <strong>Save</strong> to apply these style rules to that specific section.

      <strong>
        4\. Deleting a Section
      </strong>

      If you want to remove a part of your song entirely:

      * Hover over the section you wish to remove in the timeline.<br />

        <img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c8506897c18519729967118d2d2f1136f302023a890685b8aba786d1034c8943/assets/images/help-center/product/core-capabilities/music/how-can-i-edit-my-track-add-or-remove-sections-or-change-the-style-of-a-specific-part-in-eleven-music-4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260826T200253Z&X-Amz-Expires=604800&X-Amz-Signature=94285bef3b84eac7a68c711a605d3cdf3aa1a5e91b86db0c76d0240452d36dab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

      * Click the delete icon, the "X", in the upper left corner of the section.

      * The section will be removed from the structure, and a notification like "Outro deleted" will briefly appear.

      <strong>
        5\. Generating Your Changes
      </strong>

      After you have made any edits—whether adding, deleting, or modifying a section—you will see a notice at the bottom that says <strong>"Song composition has changed."</strong>

      * Your edits will <strong>not</strong> take effect until you click the <strong>Generate</strong> button.
      * Once you click <strong>Generate</strong>, the model will create a new version of your track that incorporates all of your changes.

      Feel free to experiment with different combinations of lyrics, styles, and structures to craft your perfect track
    </td>
  </tr>

  <tr>
    <td>
      #### What is Audio Reference?

      Audio Reference lets you upload a short audio track to guide the style and sound of a new Music v2 generation. The uploaded track is used as creative guidance alongside your text prompt.

      You can upload a reference track of up to approximately 30 seconds in commonly used audio formats. Every uploaded reference is screened for copyright compliance before it can be used.

      Audio Reference influences characteristics such as the overall sound, production style, instrumentation, tempo, and mood of the generated track. It does not copy or remix the uploaded audio, and the result remains a newly generated composition.

      Audio Reference is available with Music v2 on all paid subscriptions.
    </td>
  </tr>

  <tr>
    <td>
      #### Can Audio Reference remix a song or change its genre?

      Audio Reference is not a remixing or genre-transfer tool. It guides characteristics such as sound, mood, instrumentation, and production style.

      Results may be less reliable when the requested output is substantially different from the uploaded reference — for example, when using a jazz reference to request a rap track.

      Audio Reference is intended to guide a generation toward a similar style and sound. It is not designed for genre transformation.
    </td>
  </tr>
</tbody>
