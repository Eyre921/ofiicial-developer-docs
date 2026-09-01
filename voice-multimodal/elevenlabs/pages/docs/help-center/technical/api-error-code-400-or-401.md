---
title: "API - Error Code 400 or 401"
source: https://elevenlabs.io/docs/help-center/technical/api-error-code-400-or-401.md
path: docs/help-center/technical/api-error-code-400-or-401
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# API - Error Code 400 or 401

These error codes can have a number of causes.  The response message will indicate the cause of the error.

###

### max\_character\_limit\_exceeded

The maximum number of characters per request depends on the model.

* Flash v2.5 - up to 40,000 characters (\~40 minutes of audio)
* Turbo v2.5 - up to 40,000 characters (\~40 minutes of audio)
* Flash v2 - up to 30,000 characters (\~30 minutes of audio)
* Turbo v2 - up to 30,000 characters (\~30 minutes of audio)
* Multilingual v1 and v2 - up to 10,000 characters (\~10 minutes of audio)
* English v1 and v2 - up to 10,000 characters (\~10 minutes of audio)

###

### invalid\_api\_key

This means that you have not set your API key correctly.  Please make sure you're using "xi-api-key" exactly, with no typos, when setting your API key.

###

### voice\_not\_found

This means that you have entered the incorrect voice\_id.  Please check that you are using the correct voice\_id for the voice you want to use.  You can check this in My Voices.

###

### quota\_exceeded

You have insufficient quota to complete the request.  You can purchase [Pay As You Go credits](/docs/overview/administration/pay-as-you-go), or on legacy Creator, Pro, Scale and Business plans, you can enable [usage based billing](/docs/help-center/account/general/what-is-usage-based-billing) from your [Subscription](https://elevenlabs.io/app/subscription) page.



Example 400 response detail:

`"detail": &#123;
 "status": "max_character_limit_exceeded",
 "message": "This request's text has 627 characters and exceeds the character limit of 333 characters for non signed in accounts."
&#125;`

Example 401 response detail:

`"detail": &#123;
 "status": "invalid_api_key",
 "message": "Invalid API key"
&#125;`
