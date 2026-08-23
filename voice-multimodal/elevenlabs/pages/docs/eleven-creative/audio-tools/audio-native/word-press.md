---
title: "Audio Native with WordPress"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native/word-press.md
path: docs/eleven-creative/audio-tools/audio-native/word-press
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native with WordPress

Follow the steps in the [Audio Native overview](/docs/eleven-creative/audio-tools/audio-native) to
get started with Audio Native before continuing with this guide.

#### Install the WPCode plugin

Install the [WPCode plugin](https://wpcode.com/) into your WordPress website to embed HTML code.

#### Create a new code snippet

In the WordPress admin console, click on "Code Snippets". Add the Audio Native embed code to the new code snippet.

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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ce6368db32162ddccd68639525a54eeb477eacf3ecd64f9fac559f7a4bac1e01/assets/images/product-guides/audio-native/audio-native-wordpress-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T093153Z&X-Amz-Expires=604800&X-Amz-Signature=154cc50649619016b92b55c70b11425b569e16be278e3cfe066dc6e72fb6111a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

Pick "Auto Insert" for the insert method and set the location to be "Insert Before Content".

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/301598cd60b04b9df9465b057eeb955518b94dfbf676c9cbfee194fe6653fa90/assets/images/product-guides/audio-native/audio-native-wordpress-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T093153Z&X-Amz-Expires=604800&X-Amz-Signature=fcb269c15ba3a79e51726e7d08ad9335e9fd738ba9ccab1c0858b20e8b8b4584&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />

#### Publish your changes

Finally, publish your changes and navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d28e7eb952db6f03f5c1007f43eea0dcda3dc5413d98ab2a3aa5610d242ed8b8/assets/images/product-guides/audio-native/audio-native-wordpress-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260823T093153Z&X-Amz-Expires=604800&X-Amz-Signature=206be6c19d291fff8131153c0d0f71539f97b86e45196c3194a3307918a6bbd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Audio Native" />
