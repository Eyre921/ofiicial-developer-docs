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

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5a2bae6de46f35e49eeaef8ad92323d9717e5af5b00ad05a7670a30ec8f4696c/assets/images/product-guides/audio-native/audio-native-ghost-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T233146Z&X-Amz-Expires=604800&X-Amz-Signature=86782a839490f49763a813a34e0b56bfcec74cd593f03e03271ee27f38cef8b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2783aa5f50f84ce712957ccb1504381e4248b49b5ca408173c583a40bd38d58e/assets/images/product-guides/audio-native/audio-native-ghost-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T233146Z&X-Amz-Expires=604800&X-Amz-Signature=ee1a725ddab22d5c4e7112b77883cdbdd7a284d938333047dbb3dd0b3234dbb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update the blog post

Click the "Update" button in the top right corner of the editor, which should now be highlighted in green text.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1625ff60cbf3c92760d918a298ed65fe6f0911c345efbf9999185cf4fab95014/assets/images/product-guides/audio-native/audio-native-ghost-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T233146Z&X-Amz-Expires=604800&X-Amz-Signature=5949f60d3bca6de9f3a477a994a657b11cb480940cd4f13f18f238a7f1228160&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Navigate to the live version of the blog post

Finally, navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/20730d8df4528041314d44667d0f9418af10636144af722c1cfa2e7fe48b6107/assets/images/product-guides/audio-native/audio-native-ghost-4.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T233146Z&X-Amz-Expires=604800&X-Amz-Signature=b2aca596e51c3b0c6c413e2cd48d7389453b2b780e11693f7e877b4142db72ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
