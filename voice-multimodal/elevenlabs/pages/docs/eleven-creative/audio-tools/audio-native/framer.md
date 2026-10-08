---
title: "Audio Native with Framer"
source: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-native/framer.md
path: docs/eleven-creative/audio-tools/audio-native/framer
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio Native with Framer

> **Info**
>
> Follow the steps in the [Audio Native overview](/docs/eleven-creative/audio-tools/audio-native) to
> get started with Audio Native before continuing with this guide.

#### Add Audio Native script to your page

Navigate to your Framer page, sign in and go to your site settings. From the Audio Native embed code, extract the `<script>` tag and paste it in the "End of `<body>` tag" field.

**`Embed script `**

```html title="Embed script "
    <script src="https://elevenlabs.io/player/audioNativeHelper.js" type="text/javascript"></script>
```

![Audio Native](/docs/_fern-img/00efa5ae0c085f442c015ebcf69066cc42c8e20d1c24c907444dd750e159dd4a.webp)

#### Add an Embed Element

On your Framer blog page, add an Embed Element from Utilities.

![Audio Native](/docs/_fern-img/601d4256f5826613e90b5ad75bd92abc7b218944f31cea0a14cfad0677f080ee.webp)

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

![Audio Native](/docs/_fern-img/42ba6037aedc4982495e8ea0ba8f6a23601d1309a6c67f310c8ed326382022b9.webp)

#### Publish your changes

Finally, publish your changes and navigate to the live version of your page. You should see a message to let you know that the Audio Native project is being created. After a few minutes the text in your blog will be converted to an audio article and the embedded audio player will appear.

![Audio Native](/docs/_fern-img/86a311d5bdca2b406a9ee85d7f18a357f7e41dd31545b4b90a92ce04880b1e80.webp)
