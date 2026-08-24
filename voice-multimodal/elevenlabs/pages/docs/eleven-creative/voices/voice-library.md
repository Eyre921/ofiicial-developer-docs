---
title: "Voice Library"
source: https://elevenlabs.io/docs/eleven-creative/voices/voice-library.md
path: docs/eleven-creative/voices/voice-library
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voice Library

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6279d167562a3c4d9e6b93263ec8dfe4f969f713a0543a7bdf68ae2140c2f3ae/assets/images/product-guides/voices/voices-voice-library.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T233210Z&X-Amz-Expires=604800&X-Amz-Signature=4552f77ee22ff1cb068bcbf33e7df63b61300a751a874fbdc6bd4cc1bddbab23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Voice Library" />

## Overview

The [Voice Library](https://elevenlabs.io/app/voice-library) is a marketplace where our community can share Professional Voice Clones and earn rewards when others use them. Currently, only Professional Voice Clones can be shared. Instant Voice Clones and voices created with Voice Design are not shareable.

To access the Voice Library, click **Voices** in the sidebar and select **Explore**.

Voice Library voices are not available via the API to free tier users.

### Finding voices

You can browse the Voice Library in several ways:

#### Handpicked Collections

Our Handpicked Collections highlight top voices across use cases, genres, and languages. These collections are updated regularly to include new standout voices.

#### Search

Use the search bar to find voices by name, keyword, or voice ID. You can also search by uploading or dragging and dropping an audio file. This will help you find the original voice, if available, along with similar voices.

#### Sort options

You can sort voices by:

* Trending: voices ranked by popularity
* Latest: newly added voices
* Most users
* Character usage

#### Filters

Use filters to refine your search:

#### Language

##### Language

The language filter returns voices that have been trained on a specific language. While all voices can be used with any supported language, voices tagged with a specific language will perform best in that language. Some voices have been assessed as performing well in multiple languages, and these voices will also be returned when you search for a specific language.

#### Accent

##### Accent

When you select a language, the Accent filter will also become available, allowing you to filter for specific accents.

#### Category

##### Category

Filter voices by their suggested use case:

* Conversational
* Narration
* Characters
* Social Media
* Educational
* Advertisement
* Entertainment

#### Gender

##### Gender

* Male
* Female
* Neutral

#### Age

##### Age

* Young
* Middle Aged
* Old

#### Notice period

##### Notice period

Some voices have a notice period. This is how long you'll continue to have access to the voice if the voice owner decides to remove it from the Voice Library. If the voice's owner stops sharing their voice, you'll receive advance notice through email and in-app notifications. These notifications specify when the voice will become unavailable and recommend similar voices from the Voice Library. If the owner of a voice without a notice period decides to stop sharing their voice, you'll lose access to the voice immediately.

This filter allows you to only return voices that have a notice period, and search for voices with a specific notice period. The maximum notice period is 2 years.

#### Live Moderation enabled

##### Live Moderation enabled

Some voices have Live Moderation enabled. This is indicated with a label with a shield icon. When you generate using a voice with Live Moderation enabled, we use tools to check whether the text being generated belongs to a number of prohibited categories. This may introduce extra latency when using the voice.

This filter allows you to exclude voices that have Live Moderation enabled.

#### Quality

##### Quality

Filter voices by their quality level:

* **Any**: All voices regardless of quality assessment
* **Studio Quality**: Voices that have been recorded with proper equipment, mixed well, and tested to be free from most audio problems such as reverb/echo, distortion, or other artifacts. These voices exhibit an overall professional-sounding tone and are reviewed by our QA testers.

### Using voices from the Voice Library

You can use voices from the Voice Library directly without saving them to My Voices. When you use a voice, the notice period will be saved for your account, allowing you to continue using voices you've used previously during an active notice period, even if you haven't saved them to My Voices.

#### Save to My Voices (optional)

While not required, you can save voices to My Voices for easy access or to use at a later date. To do this, click the **+** button.

Voices saved from the Voice Library do not use custom voice slots. Custom voice slots are only
used for voices you create with [Voice Design](/docs/eleven-creative/voices/voice-design) or
[Voice Cloning](/docs/eleven-creative/voices/voice-cloning).

Voices you've added to My Voices will become available for selection in all voice selection menus. You can also use a voice directly from My Voices by clicking the **T** button, which will open Text to Speech with the voice selected.

### My Voices

You can find all the voices you've created yourself, as well as voices you've saved from the Voice Library, in **My Voices**.

You will see the following information about each voice:

* the language it was trained on.
* the category, for example, "Narration".
* how long the notice period is, if the voice has one.

The voice type is indicated by an icon:

* Yellow tick: Professional Voice Clone.
* Black tick: Studio Quality Professional Voice Clone.
* Lightning icon: Instant Voice Clone.
* No icon: voice created with Voice Design.

#### More actions

Click **More actions** (three dots) to:

* Copy voice ID: copies the voice ID to your clipboard.
* Edit voice: allows you to change the name and description of the voice. These changes are only visible to you.
* Share voice: generates a link which you can share with others. When they use the link, the voice will be added to My Voices for their account.
* View history: view your previous Text to Speech generations using this voice.
* Delete voice: deleting voices is permanent and you will be asked to confirm the deletion.

#### Collections

To help organize voices you've saved, you can create your own collections and add voices to them.

To create a new collection go to My voices, click **Collections** and select **Create collection**. Give your new collection a name, and choose from the available icons.

To add individual voices to a collection, click **More actions** (three dots) and select **Add to collection**. You can choose to add the voice to an existing collection, or create a new one.

#### Select multiple voices

You can **Shift + Click** to select multiple voices at once.

#### Drag and drop voices

Both individual voices and multiple voice selections can also be dragged **Collections** and added to an existing collection, or deleted by dragging to the **trash can** icon.

### Sharing a Professional Voice Clone:

In [My Voices](https://elevenlabs.io/app/voice-lab) find your voice and click **More actions**
(three dots), then select **Share voice**.

In the pop-up, enable the **Sharing** toggle.

For private sharing, copy the sharing link. This will allow other users to save your voice to their account.

You can restrict access to specific users by adding emails to the **Allowlist**. If this is left blank, all users with the link will be able to access your voice.

To share publicly, enable **Publish to the Voice Library**. This doesn’t make your voice automatically discoverable.

![Voice sharing overview](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/60fd4b21d2e8bba5e749edb24ec545d5990907ac6da7cbc0967bf08f7c2e0ef9/assets/images/product-guides/voices/voice-sharing.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T233210Z&X-Amz-Expires=604800&X-Amz-Signature=fd0fe0e40372a6bd89862015f9ea1e2bd0b9fbf6eb81d31d26599416310a3ca0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Before proceeding with the sharing process, you'll have a number of options including setting a notice period and enabling Live Moderation. Please see the [Voice Library Addendum](https://elevenlabs.io/vla) to our [Terms of Service](https://elevenlabs.io/terms-of-use) for more information about these options.

You also have the option to select a custom voice preview. Any generations you've made of 70-150 characters will be available to select. If you don't see any options in the selection menu, there are no eligible generations available.

![Voice sharing options](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/95a98e53782fae49fb01c403fe998b87944b247495f2ef257512652b7588d52d/assets/images/product-guides/voices/voice-sharing-options.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260824%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260824T233210Z&X-Amz-Expires=604800&X-Amz-Signature=b94bf6ef98a3298ca41ab8c397623e654139628a755faec196c22073b97d7601&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Enter a name and description for your voice.
Make sure the name you give your voice follows our **naming guidelines**:

#### Naming guidelines

#### Naming guidelines

* The naming pattern should be a name followed by **key voice traits** or a **voice persona**, separated by a hyphen (-).

* The name must be 40 characters or fewer.

* Your name should NOT include the following:

  * Names of public individuals or entities (company names, band names, influencers or famous people, etc).
  * Social handles (Twitter, Instagram, you name it, etc).
  * ALL CAPS WORDS.
  * Emojis and any other non-letter characters.
  * Explicit or harmful words.
  * The word "voice".

* Some examples of names following our guidelines:

  * Serena - Calm, Friendly, Warm
  * Olivia - Upbeat podcast host
  * Jasper - Deep, Encouraging, Serious
  * Maya - Terror narrator
  * Nelson - Scary villain
  * Harmony - High-energy, High-pitch

#### Description guidelines

#### Description guidelines

* The description helps users decide if your voice is right for their project. Be specific about the use cases your voice is best suited for.

* Include as much detail as possible about your voice's key attributes — tone, style, emotion, pacing, and any unique qualities that set it apart.

* Do not list unrelated use cases to increase visibility. Voices with misleading or spammy descriptions will not be approved.

* Example of a good description:

  > Serena offers a warm, meditative tone with a naturally slow and steady pace. Her voice carries a "smile" that feels both friendly and reassuring, making her perfect for content where the listener needs to feel safe or relaxed.
  >
  > **Best use cases:** Meditation apps, sleep stories, wellness tutorials, and empathetic customer service IVR systems.
  >
  > **Key qualities:** Soft-spoken, breathy, and consistently calm.

Set labels (language, accent, gender, age, use case, tone, and style) to help others find your
voice.

Review and accept the [Voice Library Addendum](https://elevenlabs.io/vla) to our [Terms of
Service](https://elevenlabs.io/terms-of-use) and provide the required consents and confirmations.
Please do this carefully and ensure you fully understand our service before sharing. If you have
any questions at this stage, you can reach out to us at [legal@elevenlabs.io](mailto:legal@elevenlabs.io).

After submission, your voice will be reviewed by our team. If minor adjustments are needed, we may make these for you. Your request to share your voice may be declined if it doesn't meet our guidelines, and repeated uploads that consistently violate our guidelines may lead to restrictions on uploading and sharing voices.

We currently do not have an estimate for the review time, as it depends on the queue.

## FAQ

<tbody>
  <tr>
    <td>
      #### What is the Voice Library?

      The [Voice Library](https://elevenlabs.io/app/voice-library) is a marketplace where our community can share Professional Voice Clones and earn rewards when others use them. Currently, only Professional Voice Clones can be shared. Instant Voice Clones and voices created with Voice Design are not shareable.

      To access the Voice Library, click <strong>Voices</strong> in the sidebar and select <strong>Explore</strong>.

      <img src="https://help.elevenlabs.io/hc/article_attachments/35970436663057" alt="" />

      You can browse the Voice Library in several ways:

      * Our Handpicked Collections highlight top voices across use cases, genres, and languages. These collections are updated regularly to include new standout voices.
      * Use the search bar to find voices by name, keyword, or voice ID. You can also search by uploading or dragging and dropping an audio file. This will help you find the original voice, if available, along with similar voices.
      * Use the filters to search by language and accent, gender, age and category. You can also use filters to search for voices with specific notice periods, that don't have Live Moderation enabled, or to exclude voices with a custom rate.

      You can play a sample for each voice by clicking it. If a voice has multiple previews for different languages, you can select the language you want to preview in the player at the bottom of the page.

      You can use a voice directly from the Voice Library by using the <strong>Use voice</strong> button. This will open Text to Speech with the voice preselected. Once you use a voice, the notice period, if any, is saved for your account. This means that you will be able to continue using it for the duration of the notice period if it's removed from the Voice Library in the future. 

      To save a voice to your account so you can easily access it in the future, you can click the <strong>+</strong> button. Voices you’ve added to My Voices will become available for selection in all voice selection menus. You can also use a voice directly from My Voices by clicking the <strong>T</strong> button, which will open Text to Speech with the voice selected.

      For more information, please visit our [guide to the Voice Library.](/docs/product-guides/voices/voice-library/)
    </td>
  </tr>

  <tr>
    <td>
      #### Why can't I use some voices from the Voice Library?

      Some voices in the Voice Library are only available to users with a paid subscription. This is either because the voice’s owner has chosen to restrict usage, or the voice has a credit multiplier in place. If you’re on the free plan and you try to use one of these voices, you’ll see the message: “This voice is not available for free users.” These voices will become available if you upgrade to a paid subscription.

      When you use a voice with a credit multiplier, the credit usage will be adjusted accordingly. For example, if a voice has a 2x multiplier, generating audio will cost twice as many credits as a voice on the standard rate.

      For more details on custom rates and credit multipliers, you can refer to this article: [What are custom rates and credit multipliers?](/docs/help-center/product/voices/voice-library/what-are-custom-rates-and-credit-multipliers)
    </td>
  </tr>

  <tr>
    <td>
      #### Can I share an AI-generated voice in the Voice Library?

      No. We only allow the sharing of professional cloned voices verified by a human. Instant Voice Clones, synthetic voices created using [Voice Design](/docs/product/voices/voice-lab/voice-design), AI-generated or AI-enhanced voices cannot be shared in the Voice Library.

      Users attempting to share voices generated with ElevenLabs or other AI tools into the library might be prohibited from sharing any voices in the future or suspended from the platform.

      Engaging in fraudulent, predatory or abusive practices (like evading product guardrails including voice verification (e.g., CAPTCHA) is against our [Prohibited Use Policy](https://elevenlabs.io/use-policy) and might lead to a permanent ban of the user’s account.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I delete a voice I've shared with the Voice Library?

      To remove a voice that you have shared with the Voice Library, you first need to stop sharing the voice.  To do this, find the voice in the list of voices in [My Voices](https://elevenlabs.io/app/voice-lab), click <strong>More actions</strong> (three dots) then select <strong>Edit in Library</strong> to access the sharing settings.

      Click the <strong>Publish to the Voice Library</strong> toggle to stop sharing your voice with the Voice Library.

      If you did not agree a notice period when you shared the voice, you can delete the voice after you have disabled sharing. 

      To do this, click <strong>More actions</strong> (three dots) then select <strong>Delete voice</strong>. Deleting a voice cannot be undone and you will be asked to confirm the deletion.

      If you did agree a notice period, you will need to wait for this to expire before you can remove your voice. During the notice period, your voice can be used by anyone who had already saved it to My Voices, but it will no longer be visible in the Voice Library. 

      Once you have activated the notice period, you will see a clock icon which you can hover over for confirmation.  Please be aware that if you share your voice with the Voice Library again in the future this will reset your notice period.
    </td>
  </tr>

  <tr>
    <td>
      #### Can Children’s or Child-Like Voices Be Added to the Voice Library?

      No, children’s voices or voices that sound child-like cannot be added to the Library. This policy applies to voices of minors as well as adult voices designed to mimic or sound like children.

      We made this decision to align with our [Prohibited Use Policy](https://elevenlabs.io/use-policy), which prioritizes safeguarding against any potential misuse of voices that could pose risks to children. Voices resembling children could be misused in harmful or exploitative ways, and this restriction helps ensure that our platform remains a safe and responsible space for creators and users alike.

      For more information, please refer to our [Prohibited Use Policy.](https://elevenlabs.io/use-policy)

      If you have further questions or need clarification, please contact support by emailing us at [team@elevenlabs.io](mailto:team@elevenlabs.io).
    </td>
  </tr>

  <tr>
    <td>
      #### How can I identify the voice used to generate audio?

      You can use audio or video files to search the [Voice Library](https://elevenlabs.io/app/voice-library) for similar voices. The original voice used will be shown if it exists in the Voice Library, otherwise you will get suggestions for similar voices.

      To do this, either drag and drop an audio or video file anywhere on the [Voice Library](https://elevenlabs.io/app/voice-library) page, or click the upload icon to select a file to upload.

      <img src="https://help.elevenlabs.io/hc/article_attachments/40421117743121" alt="" />

      For the best results, please upload speech only, without background music or noise.  You can use our [Voice Isolator](https://elevenlabs.io/app/voice-isolator) to clean up the audio if required. 

      Long clips are not required for the AI to find a match.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I add a custom preview for my shared voice?

      You can generate a custom preview for your Professional Voice Clone, and choose this to be the preview for your voice in the [Voice Library](https://elevenlabs.io/app/voice-library). You can change the custom preview at any time from the sharing settings for your voice.

      First, you will need to have generated some suitable audio from a text prompt between 70 and 150 characters long.

      If you don't already have any eligible generations, find your voice in [My Voices](https://elevenlabs.io/app/voice-lab), and use the <strong>T</strong> button to open [Text to Speech](https://elevenlabs.io/app/speech-synthesis/text-to-speech) with your voice selected. Enter text of your choice between 70-150 characters and click <strong>Generate speech.</strong> You can generate the audio using any of our models, including v3. 

      When you have a generation you're happy with, return to [My Voices.](https://elevenlabs.io/app/voice-lab) Find your voice in the list, click <strong>More actions</strong> (three dots) then select <strong>Share voice</strong> to access the sharing settings.

      In the <strong>Publish to the Voice Library</strong> settings, use the drop down selection for <strong>Custom voice preview</strong> to select your recently generated text. This will then be applied as the preview for your voice. Only audio that meets the criteria (length of 70-150 characters) will appear in the list.

       

      <img src="https://help.elevenlabs.io/hc/article_attachments/35971482008209" alt="" />
    </td>
  </tr>

  <tr>
    <td>
      #### What are custom rates and credit multipliers?

      Some voices in the Voice Library have a credit multiplier in place. This is because the voice's owner set a custom rate for financial rewards when they shared their Professional Voice Clone with the Voice Library. Custom rates are a legacy feature that is no longer available for newly shared voices.

      When you use a voice with a custom rate to generate audio, this will have a credit multiplier in effect, meaning that it will cost more credits to generate with this voice.

      If a voice has a credit multiplier in place, this will be displayed as a tag in the Voice Library:

      <img src="https://help.elevenlabs.io/hc/article_attachments/35970940876689" alt="" />

      In Speech Synthesis, you will see a notification that the voice has a credit multiplier in place:<br />

      <img src="https://help.elevenlabs.io/hc/article_attachments/30603895331089" alt="" />

      The credit multiplier that applies for generating audio is based on the custom rate chosen by the voice owner as well as the subscription plan of the user of the voice.
    </td>
  </tr>

  <tr>
    <td>
      #### What is a notice period?

      The notice period in the [Voice Library](https://elevenlabs.io/app/voice-library) is designed to give users advance warning if the owner of a voice they’ve saved, or used previously, decides to stop sharing their voice. This ensures a smooth transition for users who rely on that voice.

      When a voice actor shares their voice to the Voice Library, they can set a notice period. If no notice period is set, their voice will be removed immediately if they decide to stop sharing it, and anyone who has saved the voice will immediately lose access.

      The minimum notice period is 30 days, and the maximum is 2 years. Voice owners receive increased financial rewards for selecting a longer notice period.

      If a voice actor sets a notice period, users who have previously used or saved the voice will receive both email and in-app notifications when the voice owner decides to stop sharing their voice. The voice will be immediately removed from the Voice Library but will remain available for the duration of the notice period for users who saved or used it previously.

      If a voice is deleted during an active notice period, it cannot be saved again because it is no longer available in the Voice Library.

      Once a notice period is active, users can see in the app when the voice will be disabled. For API users, you can see this when fetching the voice using the [Get Voice endpoint](/docs/api-reference/voices/get) by looking for `disable_at_unix` in the response. If the voice has not had its notice period active, this key will not exist or it will say `null`.

      For larger operations, you can also set up a webhook notification for voice removal, ensuring you are informed as soon as a voice is removed. This can be very useful if you need to be informed as soon as the voice is removed, for example if you need to notify your customers.

      <img src="https://help.elevenlabs.io/hc/article_attachments/33538657366545" alt="" />

      You can set this up on your [webhooks settings page](https://elevenlabs.io/app/settings/webhooks) for your account.
    </td>
  </tr>

  <tr>
    <td>
      #### What is Live Moderation?

      When users choose to share their Professional Voice Clone with the Voice Library, they can enable Live Moderation.  When this is enabled, we use tools to check whether requests to use that voice contain text that belongs to a number of prohibited categories. 

      Please note that using a voice model with Live Moderation enabled may result in extra latency.

      For full details, please see the [Voice Library Addendum](https://elevenlabs.io/vla).
    </td>
  </tr>

  <tr>
    <td>
      #### What voices are popular on TikTok, YouTube, and social media?

      If you’ve seen a clip using AI voices on TikTok, YouTube, Instagram, X, or other social platforms, there’s a good chance it was created with ElevenLabs.

      Some of our most popular voices online today include:

      <strong>
        Male voices
      </strong>

      * Brian
      * Liam
      * Adam

      <strong>
        Female voices
      </strong>

      * Jessica
      * Matilda
      * Sarah

      These are just a few of the many voices creators use every day across social media. You can explore our Voice Library to find one that fits your style, or create your own using [Voice Design](/docs/product-guides/voices/voice-design), [Voice Remixing](/docs/capabilities/voice-remixing), [Instant Voice Cloning](/docs/product-guides/voices/voice-cloning/instant-voice-cloning), or [Professional Voice Cloning](/docs/product-guides/voices/voice-cloning/professional-voice-cloning).

      Sign up for a free account to get started: [elevenlabs.io](https://elevenlabs.io)
    </td>
  </tr>
</tbody>
