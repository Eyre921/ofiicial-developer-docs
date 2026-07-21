---
title: "Is there a way to preview audio without losing quota before downloading?"
source: https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/is-there-a-way-to-preview-audio-without-losing-quota-before-downloading.md
path: docs/help-center/product/speech-synthesis/text-to-speech/is-there-a-way-to-preview-audio-without-losing-quota-before-downloading
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Is there a way to preview audio without losing quota before downloading?

Unfortunately, at this time, we do not offer download-based deduction as an alternative to generation-based deduction. There is currently no way to preview generations without deducting quota.

When you press 'Generate' on the website, you will be deducted credits since the servers need to spin up and the audio needs to be generated.  There's no way to test or preview a voice using your own text without using credits.

We do permit two free regenerations in Speech Synthesis via the website in the following circumstances:

* The prompt (for text-to-speech) or file (for speech-to-speech), voice and model remain the same.  You can change the voice setting sliders.
* The first generation was made less than two hours ago.
* You haven't refreshed the page since generating the original audio.

If this is the case, you will see 'Regenerate speech', and the number of free regenerations remaining will be displayed if you hover over the 'Regenerate speech' button:

<img src="https://help.elevenlabs.io/hc/article_attachments/28015504910609" alt="" />

 

Once your free regenerations have been used, the button will return to 'Generate speech', and the number of credits that will be used for the generation will be displayed:

<img src="https://help.elevenlabs.io/hc/article_attachments/28015488674961" alt="" />

 

Free regenerations are only available in Speech Synthesis via the website.  They are not available via the API.

We are looking into whether there's a way for us to facilitate previews at this quality without raising prices or costs. We are also exploring ways to make the AI more controllable, so you don't have to preview and instead get the desired result, hopefully on the first try.
