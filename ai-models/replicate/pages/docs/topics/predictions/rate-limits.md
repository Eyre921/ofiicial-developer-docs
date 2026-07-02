---
title: "Rate limits"
source: https://replicate.com/docs/topics/predictions/rate-limits.md
path: docs/topics/predictions/rate-limits
---

We limit the number of API requests that can be made to Replicate:

*   You can [create predictions](/docs/reference/http#create-a-prediction) at 600 requests per minute.
*   All other endpoints you can call at 3000 requests per minute.

[](#throttling)Throttling
-------------------------

You can make short bursts of requests above the default rate limits before being throttled.

As you approach running out of credit, we apply stronger rate limits. We do this to stop you from accidentally overspending and going into arrears, and to give you some time to increase your balance when it’s running low before getting shut off entirely. To avoid this, set up [credit auto-reload](/docs/topics/billing/prepaid-credit) to keep your credit balance above $20.

If you have been granted credit and don’t have a payment method on file, you’ll also be rate limited to 1 request per second with a maximum of 6 requests per minute.

[](#api-response)API response
-----------------------------

If you hit a limit, you will receive a response with status `429` with a body like:

```json
{"detail":"Request was throttled. Your rate limit resets in ~30s."}
```

[](#higher-limits)Higher limits
-------------------------------

If you want higher limits, [contact us](https://replicate.com/support).
