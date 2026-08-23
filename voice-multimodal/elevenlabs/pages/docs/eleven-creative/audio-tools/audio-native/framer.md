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

```html title="Embed script "
    <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
```

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/00efa5ae0c085f442c015ebcf69066cc42c8e20d1c24c907444dd750e159dd4a/assets/images/product-guides/audio-native/audio-native-framer-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T233206Z&X-Amz-Expires=604800&X-Amz-Signature=479f4822618500bad4cc3604d8542996f466be99b29834384b6f56c482b8c3d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

#### Add an Embed Element

On your Framer blog page, add an Embed Element from Utilities.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/601d4256f5826613e90b5ad75bd92abc7b218944f31cea0a14cfad0677f080ee/assets/images/product-guides/audio-native/audio-native-framer-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T233206Z&X-Amz-Expires=604800&X-Amz-Signature=c26852dc34b4daa3952f15f2b8784930d840a759a67a8feb5fa4717f9ed05cad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

In the config for the Embed Element, switch the type to HTML and paste the `<div>` snippet from the Audio Native embed code into the HTML box.

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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/42ba6037aedc4982495e8ea0ba8f6a23601d1309a6c67f310c8ed326382022b9/assets/images/product-guides/audio-native/audio-native-framer-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T233206Z&X-Amz-Expires=604800&X-Amz-Signature=e2679f551b057d95696ed98de51d6a85a04041230d8667eb7b3c7448ca510c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

#### Publish your changes

Finally, publish your changes and navigate to the live version of your page. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/86a311d5bdca2b406a9ee85d7f18a357f7e41dd31545b4b90a92ce04880b1e80/assets/images/product-guides/audio-native/audio-native-framer-4.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T233206Z&X-Amz-Expires=604800&X-Amz-Signature=c826a42ad1f30c9fa7c41f9b4efd2414a5aebdd6aaddbd27bf8ddd703bd7080d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />
