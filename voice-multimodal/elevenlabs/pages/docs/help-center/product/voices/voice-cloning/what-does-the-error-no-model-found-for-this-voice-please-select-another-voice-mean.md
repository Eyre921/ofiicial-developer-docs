---
title: "What does the error 'No model found for this voice. Please select another voice' mean?"
source: https://elevenlabs.io/docs/help-center/product/voices/voice-cloning/what-does-the-error-no-model-found-for-this-voice-please-select-another-voice-mean.md
path: docs/help-center/product/voices/voice-cloning/what-does-the-error-no-model-found-for-this-voice-please-select-another-voice-mean
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What does the error 'No model found for this voice. Please select another voice' mean?

You will see this error if you try to use your Professional Voice Clone (PVC) before it has completed the fine-tuning process and is available for use.

When you create a PVC, it needs to go through a number of processes before it becomes available for use.  After you have verified your voice, it will be processed and queued for fine-tuning.   Depending on how many other voices are currently queued for fine-tuning, we estimate that this process will usually take between 3-6, but it can take up to 24 hours.

You can check the progress of your PVC in My Voices by finding the voice in your list of voices, then clicking **View** to see more details.  You can hover over each model to see the current status.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ec34838a2fd40c5105c9196c356045b2963daf2490fd36c19f42bcb8f5359c86/assets/images/help-center/product/voices/voice-cloning/what-does-the-error-no-model-found-for-this-voice-please-select-another-voice-mean.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T100016Z&X-Amz-Expires=604800&X-Amz-Signature=4d5d6e2268c7bb119168d34bf7512f44431ed8765cd785e9523b21d91b30f4bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For more detail on what each status means, please see [What does the status of my Professional Voice Clone mean?](/docs/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean)

When your PVC has completed fine-tuning and is available for use, you will see a pop-up notification, and will also be notified by email.
