---
title: "Audio Native with Webflow"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native/webflow.md
path: docs/eleven-creative/audio-tools/audio-native/webflow
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native with Webflow

> **Info**
>
> Follow the steps in the [Audio Native overview](/docs/eleven-creative/audio-tools/audio-native) to
> get started with Audio Native before continuing with this guide.

#### Add HTML to your blog post

Navigate to your Webflow blog, sign in and open the editor for the blog post you wish to narrate.

#### Add the embed code to your blog post

Click the "+" symbol in the top left and select "Code Embed" from the Elements menu.

![Audio Native](/docs/_fern-img/463029e96318cf16fa0b207019206a4e8e7b1bf44ab4203ca9811037bc2c22a4.webp)

Paste the Audio Native embed code into the HTML box and click "Save & Close".

**`Embed code snippet`**

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

![Audio Native](/docs/_fern-img/cdfc41cfbb4ba58fecc2173ab4b247037c34a7e0beb35cfd55a492a8ca2b74bf.webp)

#### Re-position the code embed

In the Navigator, place the code embed where you want it to appear on the page.

![Audio Native](/docs/_fern-img/43b6853dad99b80ed8c88d1f7a5400c96bad1cf7455213e6bc6c025031685c44.webp)

#### Publish your changes

Finally, publish your changes and navigate to the live version of the blog post. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

![Audio Native](/docs/_fern-img/4ec1a4eac0888c6b7f5df5e5669581b5b2a38967295eb2a5bc8fc7acc409b840.webp)
