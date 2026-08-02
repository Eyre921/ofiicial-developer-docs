---
title: "Audio Native"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native.md
path: docs/eleven-creative/audio-tools/audio-native
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/46d22deceeb0c48519f5c98400269b282f6919dc7d8e97baec7e2ca4a215dc8c/assets/images/product-guides/audio-native/audio-native-product-feature.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260802T233128Z&X-Amz-Expires=604800&X-Amz-Signature=e88023d942c85d0e2903603ef3bcc7d9f9a962fbceeb02c214914b3f5df6fa68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

## Overview

Audio Native is an embedded audio player that automatically voices content of a web page using ElevenLab’s [Text to Speech](/docs/eleven-creative/playground/text-to-speech) service. It can also be used to embed pre-generated content from a project into a web page. All it takes to embed on your site is a small HTML snippet. In addition, Audio Native provides built-in metrics allowing you to precisely track audience engagement via a listener dashboard.

The end result will be a Audio Native player that can narrate the content of a page, or, like in the case below, embed pre-generated content from a project:

## Guide

#### Navigate to Audio Native

In the ElevenLabs dashboard, under "Audio Tools" navigate to ["Audio Native"](https://elevenlabs.io/app/audio-native).

#### Configure player appearance

Customize the player appearance by selecting background and text colors.

#### Configure allowed sites

The URL allowlist is the list of web pages that will be permitted to play your content.

You can choose to add a specific web page (e.g. `https://elevenlabs.io/blog`) or add a whole domain to the allowlist (e.g. `http://elevenlabs.io`). If a player is embedded on a page that is not in the allowlist, it will not work as intended.

#### Get embed code

Once you've finished configuring the player and allowlist, copy the embed code and paste it into your website's source code.

## Technology-specific guides

To integrate Audio Native into your web techology of choice, see the following guides:

#### [React](/docs/eleven-creative/audio-tools/audio-native/react)

#### [Ghost](/docs/eleven-creative/audio-tools/audio-native/ghost)

#### [Squarespace](/docs/eleven-creative/audio-tools/audio-native/squarespace)

#### [Framer](/docs/eleven-creative/audio-tools/audio-native/framer)

#### [Webflow](/docs/eleven-creative/audio-tools/audio-native/webflow)

#### [Wordpress](/docs/eleven-creative/audio-tools/audio-native/word-press)

#### [Wix](/docs/eleven-creative/audio-tools/audio-native/wix)

## Using the API

You can use the [Audio Native API](/docs/api-reference/audio-native/create) to programmatically create an Audio Native player for your existing content.

```python title="Python"
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs(
api_key="YOUR_API_KEY",
)
response = elevenlabs.audio_native.create(
name="name",
)

# Use the snippet in response.html_snippet to embed the player on your website

```

```javascript title="JavaScript"
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient({ apiKey: "YOUR_API_KEY" });
const { html_snippet } = await elevenlabs.audioNative.create({
    name: "my-audio-native-player"
});

// Use the HTML code in html_snippet to embed the player on your website
```

## Settings

#### Voice and model

### Voices

To configure the voice and model that will be used to read the content of the page, navigate to the "Settings" tab and select the voice and model you want to use.

#### Pronunciation dictionaries

### Pronunciation dictionaries

Sometimes you may want to specify the pronunciation of certain words, such as character or brand names, or specify how acronyms should be read. Pronunciation dictionaries allow this functionality by enabling you to upload a lexicon or dictionary file that includes rules about how specified words should be pronounced, either using a phonetic alphabet (phoneme tags) or word substitutions (alias tags).

Whenever one of these words is encountered in a project, the AI will pronounce the word using the specified replacement. When checking for a replacement word in a pronunciation dictionary, the dictionary is checked from start to end and only the first replacement is used.

## FAQ

<tbody>
  <tr>
    <td>
      #### What is Audio Native?

      Audio Native is an embedded audio player that automatically voices content of a web page using ElevenLab’s text-to-speech service. It can also be used to embed pre-generated content from a Studio project into a web page. All it takes to deploy on your site is a brief snippet of html. In addition, Audio Native comes with built-in metrics so you can track audience engagement through a listener dashboard.

      Audio Native is available on the Creator plan and above.

      For more details, please see our <a href="/docs/creative-platform/audio-tools/audio-native">Audio Native overview.</a>
    </td>
  </tr>

  <tr>
    <td>
      #### On what plans is Audio Native available?

      Audio Native is available on the Creator plan and above. 

      For more information, please see our [Audio Native overview.](/docs/product-guides/audio-tools/audio-native)
    </td>
  </tr>

  <tr>
    <td>
      #### How to update an Audio Native player

      Made edits to your website or decided to use a new voice? Here’s how to update your Audio Native player to reflect those changes:

      <strong>Open the Studio project</strong><br />Go to the [Audio Native page](https://elevenlabs.io/app/audio-native), click the three dots next to the page you'd like to update, and select <strong>Edit Audio</strong>. This will open the corresponding Studio project.<br />

      <img src="https://help.elevenlabs.io/hc/article_attachments/34478880523025" alt="" />

      <strong>Make your changes</strong><br />Update your project as needed, such as changing the voice or editing the script.

      <strong>Export the project as MP3</strong><br />Go to <strong>Export</strong> and export the project.<br />

      <img src="https://help.elevenlabs.io/hc/article_attachments/34478880525201" alt="" />

      <br />

      <em>
        Note: This step is required for updating Audio Native, even if you don't need the MP3 file.
      </em>

      <strong>Publish the updated version</strong><br />Once the MP3 export is complete, go to <strong>Export > Publish > Audio Native</strong>.

      <strong>Select the updated version</strong><br />Click <strong>Published version</strong> and select the newly exported version of your audio to update the embedded player.<br />

      <img src="https://help.elevenlabs.io/hc/article_attachments/34478870511121" alt="" />

      Your Audio Native player will now reflect the latest version of your project.

       

      ### <strong>Updating the Player Title and Author</strong>

      To change the title or author shown in the Audio Native player:

      * Go to the corresponding Studio project editor

      * Click the hamburger menu (☰) and select Project Settings<br />

        <img src="https://help.elevenlabs.io/hc/article_attachments/34478870512913" alt="" />

      * Go to the Export tab<br />

        <img src="https://help.elevenlabs.io/hc/article_attachments/34478870513681" alt="" />

      * Edit the Title and Author fields<br />
        <img src="https://help.elevenlabs.io/hc/article_attachments/34478880531601" alt="" />

      These changes will be reflected automatically in the embedded player.
    </td>
  </tr>
</tbody>
