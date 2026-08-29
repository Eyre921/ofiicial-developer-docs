---
title: "What does the status of my Professional Voice Clone mean?"
source: https://elevenlabs.io/docs/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean.md
path: docs/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What does the status of my Professional Voice Clone mean?

Your Professional Voice Clone will go through a few different stages while it is processing. These stages are reflected in the status shown for your Professional Voice Clone in [My Voices](https://elevenlabs.io/app/voice-lab).

To view the current status, find your voice in the list and look at the icons displayed to the right.

 

<strong>Draft:</strong> This status means that your voice is incomplete. Generally this is either
because you haven't completed creating the voice, or you haven't verified the voice yet.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6d3f8b497dcb56c5ac48f87906f196f49fce5518dbe1f3e700df2f91ebbc1378/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260829%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260829T233330Z&X-Amz-Expires=604800&X-Amz-Signature=3f2ef0e53dc393bdf8ecde3a3b6b9d14cc8c2b539d7732ffd22cfde9ef547e61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

To go through the verification process, click the tick icon.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5e4e259056fdcee35a751b0d7ca2a463019a47469f95cabc9ed359f7f51fc5fe/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260829%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260829T233330Z&X-Amz-Expires=604800&X-Amz-Signature=daeb887d63e5a3caa92f4f251425e3c6dbffad0c67c7671d6a3a9d790a191596&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

To go back to the voice creation process, click <strong>More actions</strong> (three dots) and select <strong>Edit voice</strong>.

 

Once you've verified your voice, it will need to fine-tune on our models before you can use it. You can track this process by hovering over the name of your voice in [My Voices](https://elevenlabs.io/app/voice-lab). You'll see all available models listed here, with an icon to indicate the status for each model. 

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d4820b45f5fb4a89f76d3b5ef5ed2992bbf515eacac039c67596c055f136b67c/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean-3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260829%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260829T233330Z&X-Amz-Expires=604800&X-Amz-Signature=eb9ef8c60563e5dbb215a233539d4317cfe3396b34865b013371cfffcbd2be44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

 

Hover over the name of the model for more information, and you will see one of the following:

<strong>The training run has been scheduled</strong>: This means that your voice is waiting for a
slot to open up so it can be trained. The length of time that your voice will be queued will depend
on how many other voices are also in the queue.

<strong>Creating dataset</strong> and <strong>Running fine-tuning</strong>: Once a slot opens up, it
will begin the fine-tuning process. This can take between 6-24 hours. You'll see how far through
each step in the training process your voice is, indicated by a percentage.

<strong>
  We are sorry the training run experienced issues and has been retried. No further action is
  required
</strong>

This means that something went wrong, but your voice has been automatically queued to retry the
fine-tuning process. Your voice should successfully complete the fine-tuning process on the next
try, but if you experience multiple failures, please contact support by emailing us at
[team@elevenlabs.io](mailto:team@elevenlabs.io).

<strong>Voice is ready to be used with the model</strong>: This means that the fine-tuning process
for this model has been completed, and you can now use your voice with this model.

<strong>Click to start fine-tuning</strong>: Some models do not train automatically, and you will
need to click the model name to begin fine-training. If additional models have become available for
your voice to fine-tune on, you'll see an exclamation icon next to your voice. 

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7fe7278b67a7f9697c1a6190837fb110fd53e64ddb3513b4cc351292a077740e/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean-4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260829%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260829T233330Z&X-Amz-Expires=604800&X-Amz-Signature=9c1f4f5312ddeb18f51a915f511b864832130505e32761720ec1d1ddfc7ceeac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="" />

To begin the fine-tuning process, just hover over your voice's name and click the name of the model.
