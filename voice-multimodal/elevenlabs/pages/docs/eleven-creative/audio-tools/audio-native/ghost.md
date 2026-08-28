---
title: "Audio Native with Ghost"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native/ghost.md
path: docs/eleven-creative/audio-tools/audio-native/ghost
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native with Ghost

Follow the steps in the [Audio Native overview](/docs/eleven-creative/audio-tools/audio-native) to
get started with Audio Native before continuing with this guide.

#### Add HTML to your blog post

Navigate to your Ghost blog, sign in and open the settings page for the blog post you wish to narrate.

#### Add the embed code to your blog post

Click the "+" symbol on the left and select "HTML" from the menu.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5a2bae6de46f35e49eeaef8ad92323d9717e5af5b00ad05a7670a30ec8f4696c/assets/images/product-guides/audio-native/audio-native-ghost-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T100016Z&X-Amz-Expires=604800&X-Amz-Signature=42812a0a471b2abbdfd1b4d274a35dd0f660c8ec47af408e1d6d61a115454e89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

Paste the Audio Native embed code into the HTML box and press enter.

```html title="Embed code snippet"
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
    <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
```

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2783aa5f50f84ce712957ccb1504381e4248b49b5ca408173c583a40bd38d58e/assets/images/product-guides/audio-native/audio-native-ghost-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T100016Z&X-Amz-Expires=604800&X-Amz-Signature=8a6c30e3384f7c85ac9fe6460d2172b4e456822a84f0e793bbcdeb8074518c71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

#### Update the blog post

Click the "Update" button in the top right corner of the editor, which should now be highlighted in green text.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1625ff60cbf3c92760d918a298ed65fe6f0911c345efbf9999185cf4fab95014/assets/images/product-guides/audio-native/audio-native-ghost-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T100016Z&X-Amz-Expires=604800&X-Amz-Signature=0dd1bf7e161853458b867a87744771eb6e3ef1e45be158174e74047327f936cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

#### Navigate to the live version of the blog post

Finally, navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/20730d8df4528041314d44667d0f9418af10636144af722c1cfa2e7fe48b6107/assets/images/product-guides/audio-native/audio-native-ghost-4.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T100016Z&X-Amz-Expires=604800&X-Amz-Signature=b374843ad81562093a4133eca1e50169358df583e4cc3a8d38010d7b5696dc1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />
