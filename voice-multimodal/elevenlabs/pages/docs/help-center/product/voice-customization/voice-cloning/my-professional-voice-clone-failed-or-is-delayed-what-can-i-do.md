---
title: "My professional voice clone failed or is delayed, what can I do?"
source: https://elevenlabs.io/docs/help-center/product/voice-customization/voice-cloning/my-professional-voice-clone-failed-or-is-delayed-what-can-i-do.md
path: docs/help-center/product/voice-customization/voice-cloning/my-professional-voice-clone-failed-or-is-delayed-what-can-i-do
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# My professional voice clone failed or is delayed, what can I do?

After you've verified your voice, it will need to fine-tune on our models before you will be able to use it. While this is happening, you can check the status of your voice in [My Voices](https://elevenlabs.io/app/voice-lab) by hovering over the name of your voice. This will show you all the available models for your voice. To check the status for each model, hover over the model's name. 

If something went wrong, then you may see the following status:

**We are sorry the training run experienced issues and has been retried. No further action is required.** This means that something went wrong. but your voice has been automatically queued to
retry the fine-tuning process. Your voice should successfully complete the fine-tuning process on
the next try, but if you experience multiple failures, this might be an issue with the dataset that
the AI cannot resolve.

You can try to resolve this by deleting the voice and uploading the data again, starting from the beginning. This has been shown to help some users.

If this doesn't resolve the issue, you may need to review your training audio and potentially use different training audio.

You can always [contact Support](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937) if you're experiencing failures during the fine-tuning process.
