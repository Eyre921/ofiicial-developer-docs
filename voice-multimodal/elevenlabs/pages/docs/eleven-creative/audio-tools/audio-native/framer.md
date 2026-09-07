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

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/00efa5ae0c085f442c015ebcf69066cc42c8e20d1c24c907444dd750e159dd4a/assets/images/product-guides/audio-native/audio-native-framer-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233113Z&X-Amz-Expires=604800&X-Amz-Signature=a9605747794bfba1fa642f228eeabb1b38009d200f3cfa1b8c7de624a5e01b9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add an Embed Element

On your Framer blog page, add an Embed Element from Utilities.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/601d4256f5826613e90b5ad75bd92abc7b218944f31cea0a14cfad0677f080ee/assets/images/product-guides/audio-native/audio-native-framer-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233113Z&X-Amz-Expires=604800&X-Amz-Signature=edce2d40c18df86cce6af56b88914186d7a9962246c1466e5f52dd3d717cbe32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/42ba6037aedc4982495e8ea0ba8f6a23601d1309a6c67f310c8ed326382022b9/assets/images/product-guides/audio-native/audio-native-framer-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233113Z&X-Amz-Expires=604800&X-Amz-Signature=106e79d6e5354d2c0a7ff9afd3f97fe2880e92e485b42a34e5b3be723b044d45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Publish your changes

Finally, publish your changes and navigate to the live version of your page. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/86a311d5bdca2b406a9ee85d7f18a357f7e41dd31545b4b90a92ce04880b1e80/assets/images/product-guides/audio-native/audio-native-framer-4.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233113Z&X-Amz-Expires=604800&X-Amz-Signature=d105845a376e87f7075584cff887666fba21188636ab143770a109726e2e7270&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
