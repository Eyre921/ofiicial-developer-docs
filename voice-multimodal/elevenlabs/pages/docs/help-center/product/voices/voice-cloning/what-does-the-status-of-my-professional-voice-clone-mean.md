---
title: "What does the status of my Professional Voice Clone mean?"
source: https://elevenlabs.io/docs/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean.md
path: docs/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What does the status of my Professional Voice Clone mean?

Your Professional Voice Clone will go through a few different stages while it is processing. These stages are reflected in the status shown for your Professional Voice Clone in [My Voices](https://elevenlabs.io/app/voice-lab).

To view the current status, find your voice in the list and look at the icons displayed to the right.



**Draft:** This status means that your voice is incomplete. Generally this is either
because you haven't completed creating the voice, or you haven't verified the voice yet.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6d3f8b497dcb56c5ac48f87906f196f49fce5518dbe1f3e700df2f91ebbc1378/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233316Z&X-Amz-Expires=604800&X-Amz-Signature=23c5697a53897c667607bc08ae27defc9cc1ab9217074a0c5a8bb26108438567&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To go through the verification process, click the tick icon.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5e4e259056fdcee35a751b0d7ca2a463019a47469f95cabc9ed359f7f51fc5fe/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233316Z&X-Amz-Expires=604800&X-Amz-Signature=c1f9c7accb2ab344cd424d9f27790776ca18b400bd4bef78f01941ce052bb77d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To go back to the voice creation process, click **More actions** (three dots) and select **Edit voice**.



Once you've verified your voice, it will need to fine-tune on our models before you can use it. You can track this process by hovering over the name of your voice in [My Voices](https://elevenlabs.io/app/voice-lab). You'll see all available models listed here, with an icon to indicate the status for each model.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d4820b45f5fb4a89f76d3b5ef5ed2992bbf515eacac039c67596c055f136b67c/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean-3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233316Z&X-Amz-Expires=604800&X-Amz-Signature=f6245cacee8fae5745488b6b9307bae885e73e22c4e9669d7fcea0b52fc9b2bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Hover over the name of the model for more information, and you will see one of the following:

**The training run has been scheduled**: This means that your voice is waiting for a
slot to open up so it can be trained. The length of time that your voice will be queued will depend
on how many other voices are also in the queue.

**Creating dataset** and **Running fine-tuning**: Once a slot opens up, it
will begin the fine-tuning process. This can take between 6-24 hours. You'll see how far through
each step in the training process your voice is, indicated by a percentage.

**We are sorry the training run experienced issues and has been retried. No further action is
required**

This means that something went wrong, but your voice has been automatically queued to retry the
fine-tuning process. Your voice should successfully complete the fine-tuning process on the next
try, but if you experience multiple failures, please contact support by emailing us at
[team@elevenlabs.io](mailto:team@elevenlabs.io).

**Voice is ready to be used with the model**: This means that the fine-tuning process
for this model has been completed, and you can now use your voice with this model.

**Click to start fine-tuning**: Some models do not train automatically, and you will
need to click the model name to begin fine-training. If additional models have become available for
your voice to fine-tune on, you'll see an exclamation icon next to your voice.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7fe7278b67a7f9697c1a6190837fb110fd53e64ddb3513b4cc351292a077740e/assets/images/help-center/product/voices/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean-4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260907T233316Z&X-Amz-Expires=604800&X-Amz-Signature=948c3f92824f4e36249c9778f842a2c70df2372f1af0505d57a84091efc5cf81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To begin the fine-tuning process, just hover over your voice's name and click the name of the model.
