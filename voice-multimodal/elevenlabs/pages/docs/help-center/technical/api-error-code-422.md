---
title: "API - Error Code 422"
source: https://elevenlabs.io/docs/help-center/technical/api-error-code-422.md
path: docs/help-center/technical/api-error-code-422
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# API - Error Code 422

### value\_error: Required value is not provided or is not in the correct format

> Check [https://api.elevenlabs.io/docs#/](https://api.elevenlabs.io/docs#/) to see what parameters are required for the endpoint you are using. Ensure you are setting it properly.

### cors error

> A code 422 of type “cors” most commonly seems to occur when you do not use JSON.stringify() on the request body when using fetch() in JavaScript. It might also occur if you call one of the API from a frontend.

With any unsuccessful API response, be sure to check the response body as it will contain error detail in json format.
