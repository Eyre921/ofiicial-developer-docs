---
title: "Audio Native"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native.md
path: docs/eleven-creative/audio-tools/audio-native
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/46d22deceeb0c48519f5c98400269b282f6919dc7d8e97baec7e2ca4a215dc8c/assets/images/product-guides/audio-native/audio-native-product-feature.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=51914112a1d2d8459298b89b294ba6a2457c088558c9de290bd9381ac55b1038&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

      For more details, please see our [Audio Native overview.](/docs/creative-platform/audio-tools/audio-native)
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

      **Open the Studio project**\
      Go to the [Audio Native page](https://elevenlabs.io/app/audio-native), click the three dots next to the page you'd like to update, and select **Edit Audio**. This will open the corresponding Studio project.\


      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/55eda284239de43d8010769153064cb7dade1c95de41a7913b377ef450a52a1a/assets/images/help-center/product/distribution-publishing/audio-native/how-to-update-an-audio-native-player.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=21be6386e1e72eff65040e59bad23157b76fa411d3abea6018f7707d18c6e5f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      **Make your changes**\
      Update your project as needed, such as changing the voice or editing the script.

      **Export the project as MP3**\
      Go to **Export** and export the project.\


      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d3116f4d112d3fe033649676abf81212662976589ab131fe56ad96a50c8c7438/assets/images/help-center/product/distribution-publishing/audio-native/how-to-update-an-audio-native-player-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=80840a39eab0e49a82ac6eaea0daafe31df9180ce1924d42fe5263f9b332d74d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      \
      *Note: This step is required for updating Audio Native, even if you don't need the MP3 file.*

      **Publish the updated version**\
      Once the MP3 export is complete, go to **Export > Publish > Audio Native**.

      **Select the updated version**\
      Click **Published version** and select the newly exported version of your audio to update the embedded player.\


      ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/52cb3fe992bb7540153b7d431aab9f44359c713056c1d35e72b5abfd2cdde2a5/assets/images/help-center/product/distribution-publishing/audio-native/how-to-update-an-audio-native-player-3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=3b31f8122df6dfd013f40a8b0f2220eb758b127dad50dae01515a78cc4f35e8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      Your Audio Native player will now reflect the latest version of your project.



      ### **Updating the Player Title and Author**

      To change the title or author shown in the Audio Native player:

      * Go to the corresponding Studio project editor

      * Click the hamburger menu (☰) and select Project Settings\


        ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ef987276cce601b07bab9390e06adeb9d1b106f7ed78e8efa330a5a8b2181989/assets/images/help-center/product/distribution-publishing/audio-native/how-to-update-an-audio-native-player-4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=0fdee8b3ccb03a0fe4819e40fe9e37442d446415028b7a3f2178570c3e0d8a29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      * Go to the Export tab\


        ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/87b69fe08f2e63aa905ba3e00035de251f94d43ebee8c9bb7592517538994781/assets/images/help-center/product/distribution-publishing/audio-native/how-to-update-an-audio-native-player-5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=abdc92c3aae3682ecdd78b86b17127b797e818d16fa0da2cf70388bcf88955a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      * Edit the Title and Author fields\


        ![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/77ed6d1a7724b2a6585a92216c4e1247fd115df74886ea5880fcd764a4608d1b/assets/images/help-center/product/distribution-publishing/audio-native/how-to-update-an-audio-native-player-6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T071047Z&X-Amz-Expires=604800&X-Amz-Signature=2321df2fe47820893089904e73e61d6c1de5330211be49b681e45245b8000bb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

      These changes will be reflected automatically in the embedded player.
    </td>
  </tr>
</tbody>
