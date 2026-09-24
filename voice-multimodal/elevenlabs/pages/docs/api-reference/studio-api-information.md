---
title: "ElevenCreative Studio API"
source: https://elevenlabs.io/docs/api-reference/studio-api-information.md
path: docs/api-reference/studio-api-information
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenCreative Studio API

> **Note**
>
> The ElevenCreative Studio API is only available upon request. To get access, [contact sales](https://elevenlabs.io/contact-sales).

## FAQ

<tbody>
  <tr>
    <td>
      #### What is Studio?

      ElevenCreative Studio is a workspace for creating audio and video projects. Studio 4.0 combines a prompt-first workflow with timeline editing, generated media, sharing, and comments.

      ![ElevenCreative Studio project editor](https://files.buildwithfern.com/visual-editor-images/elevenlabs.io/docs/2026-09-22T09:10:38.702Z/docs/eleven-creative/products/studio/Studio1.webp)

      ## Audio projects

      Use Audio projects to create long-form narration, podcasts, and audiobooks. Upload a script or document, assign voices, and arrange narration, music, and sound effects on the timeline.

      The Audio project editor includes:

      * A contextual sidebar for voice, model, playback, and generation settings.
      * A Chapters sidebar for organizing long-form content.
      * Generation history and paragraph locking.
      * Actor Mode for guiding speech delivery with a recording.
      * MP3 and WAV export options.

      ## Video projects

      Use Video projects to combine video, images, speech, music, sound effects, text, and captions. Start with a prompt, an Inspiration, an upload, or a blank project.

      The Video project editor includes:

      * A **Library** for project and workspace assets.
      * A **Script** panel for narration and pronunciation rules.
      * A **Captions** panel for transcript and style controls.
      * A multi-track timeline for arranging media.
      * Aspect ratios for widescreen, vertical, portrait, and square video.
      * Studio Agent for planning and editing video projects.

      ## Sharing and export

      Share a project to collect comments from teammates. Select **Export** to render the current chapter or project as audio or video.

      For detailed instructions, see the [ElevenCreative Studio guide](/docs/product-guides/products/studio).
    </td>
  </tr>

  <tr>
    <td>
      #### On what plans can I use Studio?

      Our professional end-to-end solution for long-form content, called Studio, is available on all our plans, including our free plan.

      The exception being the **Create a podcast (GenFM)** feature, which requires a paid subscription to access.

      You can find more information about all our subscription plans on our [Pricing page.](https://elevenlabs.io/pricing)
    </td>
  </tr>

  <tr>
    <td>
      #### How do I add chapters to a Studio project?

      The **Chapters** sidebar is available in Audio projects. When you import a document that contains chapters, Studio detects them automatically.

      Select the **Chapters** tab to open the sidebar.

      ![Chapters sidebar in a Studio Audio project](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6f636820458f31c4388e8e6f5ce5433fba73340fc4e8712f0ec818f5966365d9/assets/images/product-guides/studio/studio-chapters.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T113307Z&X-Amz-Expires=604800&X-Amz-Signature=dd223d724c60f22dd29ccb72d6d99f063bb90272692d80fe615ea263bf3126d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      Select **+** to add a chapter. Use **Chapter actions** to rename or remove a chapter. Drag chapters to reorder them.
    </td>
  </tr>

  <tr>
    <td>
      #### Does it cost credits to regenerate in Studio?

      We offer up to two free regenerations in Studio, provided you haven't changed the text that you're regenerating, or assigned a different voice, or changed the voice settings.

      To regenerate, either click on the paragraph to regenerate the whole paragraph, or select one or more words that you want to regenerate. For the best results, we recommend regenerating a complete phrase or sentence.

      If the selection is eligible for a free regeneration, you will see that the Generate/Regenerate button in the toolbar says **Regenerate**, and if you hover over it, you will see a notification letting you know how many free regenerations are remaining.

      ![Generate and Regenerate controls in Studio](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/648aadb17d5d4c3bb29a3d1e568f37ad4139f941e092e7fce740c7f34821374c/assets/images/product-guides/studio/studio_generate.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T113307Z&X-Amz-Expires=604800&X-Amz-Signature=15d8aa648328f80d1d5d9ffc956c91da038197c649df8ed0096b994b59b942cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      If your selection isn't eligible for a free regeneration, the button will say **Generate**, and you will be charged for the generation.
    </td>
  </tr>

  <tr>
    <td>
      #### How can I create a voiceover for my video using Studio?

      Create a new video project from the Studio home page. Enter a prompt, select an Inspiration, or select **+ New blank project** > **Video project (New)**.

      Use the **Library** panel to add the video and voiceover:

      Select **Create +**.

      Select **Upload** to add an existing video, or select **Video** to generate one.

      Select **Speech** to generate the voiceover.

      Drag the video and speech clips from the Library to the timeline.

      Adjust the clips on the timeline to align the voiceover with the video.

      ![Library panel in a Studio video project](https://files.buildwithfern.com/visual-editor-images/elevenlabs.io/docs/2026-09-22T08:55:34.233Z/docs/eleven-creative/products/studio/Contextual_Sidebar_Video_project.webp)

      Use the **Script** panel to edit the narration or change its voice and model. Changes to the text or voice require regeneration.

      To add captions, open the **Captions** panel and select the voiceover track as the caption source. Edit the transcript and caption style as required.

      Select **Export** to render and download the finished video.
    </td>
  </tr>
</tbody>
