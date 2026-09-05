---
title: "What is a notice period?"
source: https://elevenlabs.io/docs/help-center/product/voices/voice-library/what-is-a-notice-period.md
path: docs/help-center/product/voices/voice-library/what-is-a-notice-period
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What is a notice period?

The notice period in the [Voice Library](https://elevenlabs.io/app/voice-library) is designed to give users advance warning if the owner of a voice they’ve saved, or used previously, decides to stop sharing their voice. This ensures a smooth transition for users who rely on that voice.

When a voice actor shares their voice to the Voice Library, they can set a notice period. If no notice period is set, their voice will be removed immediately if they decide to stop sharing it, and anyone who has saved the voice will immediately lose access.

The minimum notice period is 30 days, and the maximum is 2 years. Voice owners receive increased financial rewards for selecting a longer notice period.

If a voice actor sets a notice period, users who have previously used or saved the voice will receive both email and in-app notifications when the voice owner decides to stop sharing their voice. The voice will be immediately removed from the Voice Library but will remain available for the duration of the notice period for users who saved or used it previously.

If a voice is deleted during an active notice period, it cannot be saved again because it is no longer available in the Voice Library.

Once a notice period is active, users can see in the app when the voice will be disabled. For API users, you can see this when fetching the voice using the [Get Voice endpoint](/docs/api-reference/voices/get) by looking for `disable_at_unix` in the response. If the voice has not had its notice period active, this key will not exist or it will say `null`.

For larger operations, you can also set up a webhook notification for voice removal, ensuring you are informed as soon as a voice is removed. This can be very useful if you need to be informed as soon as the voice is removed, for example if you need to notify your customers.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ef4914131e291b23f5894a85b274e6a6a106b77e603e330beff26c4ce2593aa1/assets/images/help-center/product/voices/voice-library/what-is-a-notice-period.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113409Z&X-Amz-Expires=604800&X-Amz-Signature=bac24bc7b02dd18b77c159b3af27bfb4863b6e284cc0d922eba1cc4d57160b19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

You can set this up on your [webhooks settings page](https://elevenlabs.io/app/settings/webhooks) for your account.
