---
title: "Do I use quota on every generation?"
source: https://elevenlabs.io/docs/help-center/account/general/do-i-use-quota-on-every-generation.md
path: docs/help-center/account/general/do-i-use-quota-on-every-generation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Do I use quota on every generation?

When you press 'Generate' on the website, you will be deducted credits since the audio needs to be generated in order for you to hear it.  This includes if you change the text and then regenerate, including in [Studio](/docs/product-guides/products/studio). In Dubbing Studio, you get an allowance of free credits when creating a dubbing project that you can use to regenerate some of the clips. Once these credits are exhausted, you will be charged credits from your monthly quota for any additional generations.



**Free regenerations in Text to Speech and Voice Changer**

In the Text to Speech playground, you're eligible for two free generations in the following circumstances:

* You're generating on the website.
* The prompt (for Text to Speech) or file (for Voice Changer), voice and model remain the same. You can change the voice setting sliders.
* The first generation was made less than two hours ago.
* You haven't refreshed or left the page since generating the original audio.

If this is the case, you will see 'Regenerate speech', and the number of free regenerations remaining will be displayed if you hover over the 'Regenerate speech' button:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bfcf041fb81235ac78fee6e1bee42750811986f999d0f19ac88935daf347268d/assets/images/help-center/account/general/tts-regenerate.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T233424Z&X-Amz-Expires=604800&X-Amz-Signature=0a42f6cafc0f4675d098fd989460ae3100e410436184a12e5a7fdaf199e243e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your free regenerations have been used, the button will return to 'Generate speech', and the number of credits that will be used for the generation will be displayed:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/747483da90dc8cfdaf27d92c62082f4fbc55f94615391463b0122b00dfe20845/assets/images/help-center/account/general/tts-generate.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T233424Z&X-Amz-Expires=604800&X-Amz-Signature=cf0511b367bdf774da1858183c42c23f29242d1cb68fd387fe42a0eb9ab04e97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

This works differently with the v3 model. Each time you click Generate, you’ll get two alternative outputs, but you’re only charged for one. If you click Generate again, you’ll get two new alternatives and you’ll be charged again. In short, you’re charged every time you click Generate, and each click gives you two options.

Free regenerations for Text to Speech and Speech to Speech are only available via the website. They are not available in via the API.



**Free regenerations in Studio**

We also offer two free regenerations in Studio, provided:

* You haven't changed the text.
* You haven't changed the voice.

If the Generate/Regenerate button says **Regenerate**, rather than Generate, then you won't be charged for your next generation. You can hover over the button to see how many free regenerations are remaining.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/725da07a47c79e1d844c0a1994d147b8b57e501d30638a04725b273a3d1a45b8/assets/images/help-center/account/general/studio-regenerate.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T233424Z&X-Amz-Expires=604800&X-Amz-Signature=f36ccb818c528cf27e9c8c19ea6e52bac60e5af4d79400601c4f1b186500e7c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
