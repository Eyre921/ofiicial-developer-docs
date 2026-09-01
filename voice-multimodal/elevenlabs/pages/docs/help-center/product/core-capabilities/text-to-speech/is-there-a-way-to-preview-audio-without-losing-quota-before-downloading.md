---
title: "Is there a way to preview audio without losing quota before downloading?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/is-there-a-way-to-preview-audio-without-losing-quota-before-downloading.md
path: docs/help-center/product/core-capabilities/text-to-speech/is-there-a-way-to-preview-audio-without-losing-quota-before-downloading
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Is there a way to preview audio without losing quota before downloading?

Unfortunately, at this time, we do not offer download-based deduction as an alternative to generation-based deduction. There is currently no way to preview generations without deducting quota.

When you press 'Generate' on the website, you will be deducted credits since the servers need to spin up and the audio needs to be generated. There's no way to test or preview a voice using your own text without using credits.

We do permit two free regenerations in Text to Speech via the website in the following circumstances:

* The prompt (for Text to Speech) or file (for Voice Changer), voice and model remain the same. You can change the voice setting sliders.
* The first generation was made less than two hours ago.
* You haven't refreshed the page since generating the original audio.

If this is the case, you will see 'Regenerate speech', and the number of free regenerations remaining will be displayed if you hover over the 'Regenerate speech' button:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9b75422ebf4bee357d8eb5384d30e03a3c4c5102f422cb87c22ff09c1bfe1c8d/assets/images/help-center/product/core-capabilities/text-to-speech/is-there-a-way-to-preview-audio-without-losing-quota-before-downloading.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T100017Z&X-Amz-Expires=604800&X-Amz-Signature=c208dbc3e92e9e1df96ddd326f51da5f90d6c7fd80ecad390b85795729ebe5cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your free regenerations have been used, the button will return to 'Generate speech', and the number of credits that will be used for the generation will be displayed:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/72b5058ea9066fbad31cf1a38453ba35947cc7486eb06ded307d1ae13c1011d4/assets/images/help-center/product/core-capabilities/text-to-speech/is-there-a-way-to-preview-audio-without-losing-quota-before-downloading-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T100017Z&X-Amz-Expires=604800&X-Amz-Signature=e585c65e208bf501d496883dc5ab92bf5fd4f5c29ec74d0aaaee774ad9ede6d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Free regenerations are only available in Text to Speech via the website. They are not available via the API.

We are looking into whether there's a way for us to facilitate previews at this quality without raising prices or costs. We are also exploring ways to make the AI more controllable, so you don't have to preview and instead get the desired result, hopefully on the first try.
