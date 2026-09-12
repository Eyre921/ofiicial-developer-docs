---
title: "Audio Native with Framer"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native/framer.md
path: docs/eleven-creative/audio-tools/audio-native/framer
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native with Framer

Follow the steps in the [Audio Native overview](/docs/eleven-creative/audio-tools/audio-native) to
get started with Audio Native before continuing with this guide.

#### Add Audio Native script to your page

Navigate to your Framer page, sign in and go to your site settings. From the Audio Native embed code, extract the `<script>` tag and paste it in the "End of `<body>` tag" field.

**`Embed script `**

```html title="Embed script "
    <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
```

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/00efa5ae0c085f442c015ebcf69066cc42c8e20d1c24c907444dd750e159dd4a/assets/images/product-guides/audio-native/audio-native-framer-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260912%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260912T093502Z&X-Amz-Expires=604800&X-Amz-Signature=cd4b05984a62b8492619c512358f0cd1c1b1ce34c2ee7515c64ce572ab017e0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add an Embed Element

On your Framer blog page, add an Embed Element from Utilities.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/601d4256f5826613e90b5ad75bd92abc7b218944f31cea0a14cfad0677f080ee/assets/images/product-guides/audio-native/audio-native-framer-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260912%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260912T093502Z&X-Amz-Expires=604800&X-Amz-Signature=c0bec538b031d266b22bd1d50fe71e17ebf17c1e51f858c8374726bfae2c4c5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

In the config for the Embed Element, switch the type to HTML and paste the `<div>` snippet from the Audio Native embed code into the HTML box.

**`Embed div`**

```html title="Embed div"
    <div
        id="elevenlabs-audionative-widget"
        data-height="90"
        data-width="100%"
        data-frameborder="no"
        data-scrolling="no"
        data-publicuserid="public-user-id"
        data-playerurl="https://elevenlabs.io/player/index.html"
        data-projectid="project-id"
    >
        Loading the <a href="https://elevenlabs.io/text-to-speech" target="_blank" rel="noopener">Elevenlabs Text to Speech</a> AudioNative Player...
    </div>
```

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/42ba6037aedc4982495e8ea0ba8f6a23601d1309a6c67f310c8ed326382022b9/assets/images/product-guides/audio-native/audio-native-framer-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260912%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260912T093502Z&X-Amz-Expires=604800&X-Amz-Signature=7c709354b0012a8f5bb2965535e080cedddffb211a94e4836dd0f11714874c39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Publish your changes

Finally, publish your changes and navigate to the live version of your page. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/86a311d5bdca2b406a9ee85d7f18a357f7e41dd31545b4b90a92ce04880b1e80/assets/images/product-guides/audio-native/audio-native-framer-4.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260912%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260912T093502Z&X-Amz-Expires=604800&X-Amz-Signature=3a51362cc69d768596840339423d267cb5a9fe2d5c6ba67e8bb0edf6b1a0c9c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
