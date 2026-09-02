---
title: "ElevenCreative Studio API"
source: https://elevenlabs.io/docs/api-reference/studio-api-information.md
path: docs/api-reference/studio-api-information
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenCreative Studio API

The ElevenCreative Studio API is only available upon request. To get access, [contact sales](https://elevenlabs.io/contact-sales).

## FAQ

<tbody>
  <tr>
    <td>
      #### What is Studio?

      Studio is our production workflow for creating professional audio and video content. It brings together text, visuals, and sound to help you produce narrations, audiobooks, video voiceovers, and more.

      ### Creating Audio Content

      To generate audio, you can upload a full book, document, or script, or even import an entire webpage via URL. Studio supports a wide range of formats, including:

      * EPUB
      * PDF
      * DOCX
      * TXT
      * HTML
      * URL

      Once imported, you can edit and organize text directly in the interface and apply any voice from our Voice Library to bring your content to life. When your project is complete, you can export as either MP3 or WAV.

      ### Creating Video and Voiceover Content

      Studio also allows you to import videos and images to create voiceovers. The timeline includes a video track and caption layer, giving you precise control over timing and synchronization. You can also import music and sound effects on separate tracks for richer productions.

      When your project is ready for review, you can share it using our built-in collaboration tools, which include feedback and commenting features.

      ### Advanced Features

      Studio includes powerful organization and editing tools that make it easy to manage complex projects:

      * Assign different voices and settings to sections or characters.
      * Regenerate individual paragraphs or words to fine-tune delivery.
      * Lock sections once you’re satisfied with the result.
      * Access Generation History to restore and download previous versions.
      * Adjust playback speed between 0.8× and 2.0× for efficient review.

      These controls make Studio ideal for creating everything from table reads and audio dramas to narrated videos and multimedia productions.

      For a full overview and step-by-step guidance, see our [Studio documentation.](/docs/product-guides/products/studio)
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

      When you create a Studio project using the **New audiobook** option and import a document that includes chapters, chapters will be automatically detected.

      To manage chapters in an existing project, go to **Project options** in the top left corner, then select **Manage chapters**. This will open the **Chapters sidebar**.

      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/70c468910efa03c84f4cd309a937cbe537c223c2f1e6598db37eef6bd26e4f0d/assets/images/help-center/product/studio/studio-manage-chapters.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T233314Z&X-Amz-Expires=604800&X-Amz-Signature=f72d8f72aea0d9688a8996ecb3e854213452f5e67efde56fede884adef4ba626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      You can add a new chapter using the **+** button. You can also rename and remove chapters using the **Chapter actions** (three dots) button, and drag and drop the chapters to rearrange them.

      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0a498e857491f4974398d85b788ad49025892cf3aeed63913b03ce6e28d5d0cf/assets/images/help-center/product/studio/studio-chapter-options.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T233314Z&X-Amz-Expires=604800&X-Amz-Signature=50ad4df7d0d0258d38c957cc4f40abe7e44a33e4e56bfba7411ed6e34f70294a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    </td>
  </tr>

  <tr>
    <td>
      #### Does it cost credits to regenerate in Studio?

      We offer up to two free regenerations in Studio, provided you haven't changed the text that you're regenerating, or assigned a different voice, or changed the voice settings.

      To regenerate, either click on the paragraph to regenerate the whole paragraph, or select one or more words that you want to regenerate. For the best results, we recommend regenerating a complete phrase or sentence.

      If the selection is eligible for a free regeneration, you will see that the Generate/Regenerate button in the toolbar says **Regenerate**, and if you hover over it, you will see a notification letting you know how many free regenerations are remaining.

      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f3af89ec341d3d0e493219796067b35ce8d129e6d51edc70178f6a1ea22d4977/assets/images/help-center/product/studio/does-it-cost-credits-to-regenerate-in-studio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T233314Z&X-Amz-Expires=604800&X-Amz-Signature=7fab741894110a2e21b1d77bd4c46925b4d064d35b3111f446afa1e238d8b765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      If your selection isn't eligible for a free regeneration, the button will say **Generate**, and you will be charged for the generation.
    </td>
  </tr>

  <tr>
    <td>
      #### How can I create a voiceover for my video using Studio?

      To create a voiceover for a video, you can either:

      * Start a new project using the **New video voiceover** option, which lets you upload a video file, or
      * Start a blank project using the **New blank project option** > **Video project**.

      You can also add a video to an existing project:

      * To upload a video, use the **Imports** option and either drag and drop your file, or specify the location using the **Upload file** option.
      * To add a video that you've generated using Image & Video, click **Video** in the sidebar. You'll see your previously generated videos and can import using the **+** button.
      * You can also generate a video directly in Studio using the Video prompt, which you can access by clicking **Video** in the sidebar.

      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9bd8a0e0c3d81158b4fe3416484c762c58aead9246a55ee5dd7c7b68400bb0e3/assets/images/help-center/product/studio/how-can-i-create-a-voiceover-for-my-video-using-studio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T233314Z&X-Amz-Expires=604800&X-Amz-Signature=0a242ae5a2d77adf24466a2cb16ca612d800bf3b97a46892e848c43c70b28a03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      You can:

      * **Resize the video view** by dragging the vertical divider between the video and text panes.
      * **Remove the video** by right-clicking it in the timeline and selecting **Delete**.
      * **Export your project** as a full video or audio-only file by clicking **Export**.
    </td>
  </tr>
</tbody>
