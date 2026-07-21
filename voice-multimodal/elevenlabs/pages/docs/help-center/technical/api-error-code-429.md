---
title: "API - Error Code 429"
source: https://elevenlabs.io/docs/help-center/technical/api-error-code-429.md
path: docs/help-center/technical/api-error-code-429
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# API - Error Code 429

API Error Code 429 can have two response messages: `too_many_concurrent_requests` or `system_busy`.

### too\_many\_concurrent\_requests

If you see the response message `too_many_concurrent_requests`, this means that you have exceeded the concurrency limit for your subscription.  

The concurrency limit (concurrent requests running in parallel) depends on the plan you are on. Below are the current rates for each plan, but please note that we will likely revisit them in the future.

> Free: 2<br />Starter: 3<br />Creator: 5<br />Pro: 10<br />Scale: 15<br />Business: 15

ElevenAgents has different concurrency limits. For details, please see [this article.](/docs/help-center/product/conversational-agents/eleven-labs-agents-formerly-conversational-ai/how-many-eleven-agents-requests-can-i-make-and-can-i-increase-it)

### system\_busy

If you see the response message `system_busy`, this means that our services were experiencing high levels of traffic and your request could not be processed.  Generally, if you retry the request, it will succeed.
