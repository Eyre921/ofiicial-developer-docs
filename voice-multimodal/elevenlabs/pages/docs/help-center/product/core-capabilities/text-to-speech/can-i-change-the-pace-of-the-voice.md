---
title: "Can I change the pace of the voice?"
source: https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/can-i-change-the-pace-of-the-voice.md
path: docs/help-center/product/core-capabilities/text-to-speech/can-i-change-the-pace-of-the-voice
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Can I change the pace of the voice?

Voice speed control is available for Text to Speech via Speech Synthesis, Studio, ElevenAgents and our API.

You can control the speed of the voice using the Speed setting.

Possible values range from 0.7 to 1.2. Values below 1 will slow the speech down, and values above 1 will speed it up. Extreme values may affect the quality of the generated speech.

This setting is available for all voices and all models. You can find it in the voice settings.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a1130594e85e35a2a3073530577fd85e902b7886cbf442a18b4422d9084dfcec/assets/images/help-center/product/core-capabilities/text-to-speech/can-i-change-the-pace-of-the-voice.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260914T220121Z&X-Amz-Expires=604800&X-Amz-Signature=9bd4ca2b2eb0bd50e3c1f429f994d2b9ac23bbb3532cd683fe6ad73b375f550c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For information on how to control speech when using the API, please see our [API reference.](/docs/api-reference/text-to-speech/convert#request.body.voice_settings.speed)
