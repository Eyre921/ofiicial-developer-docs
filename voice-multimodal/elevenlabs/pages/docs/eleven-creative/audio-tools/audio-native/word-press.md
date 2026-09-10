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

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ce6368db32162ddccd68639525a54eeb477eacf3ecd64f9fac559f7a4bac1e01/assets/images/product-guides/audio-native/audio-native-wordpress-1.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T233105Z&X-Amz-Expires=604800&X-Amz-Signature=fc53edd164cdb8ac5b443bce7c078ab5081505f51bc8b96dc168f95b205a8154&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Pick "Auto Insert" for the insert method and set the location to be "Insert Before Content".

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/301598cd60b04b9df9465b057eeb955518b94dfbf676c9cbfee194fe6653fa90/assets/images/product-guides/audio-native/audio-native-wordpress-2.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T233105Z&X-Amz-Expires=604800&X-Amz-Signature=cede0d3c316b6a5988d698c22283ccb0916bd527acc4bc3778949a4797c6996e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Publish your changes

Finally, publish your changes and navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

![Audio Native](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d28e7eb952db6f03f5c1007f43eea0dcda3dc5413d98ab2a3aa5610d242ed8b8/assets/images/product-guides/audio-native/audio-native-wordpress-3.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260910T233105Z&X-Amz-Expires=604800&X-Amz-Signature=00ef3fdd53bf7a20fb4884837fdf0cf0970d136773f092c7237912f2290567b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
