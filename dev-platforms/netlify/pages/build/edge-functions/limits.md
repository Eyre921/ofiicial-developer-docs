---
title: "Edge Functions Limits"
source: https://docs.netlify.com/build/edge-functions/limits.md
path: build/edge-functions/limits
---

---
title: "Edge Functions limits"
description: "Keep these limitations in mind when working with Edge Functions, which connect our platform with an open runtime standard at the network edge."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Keep the following limitations in mind when working with Edge Functions.

## Operation limits

Edge functions have limits for their size and the amount of memory and execution time they can use:

- **Code size limit:** 20 MB after compression

  This is the maximum edge function bundle size supported.
- **Memory per set of deployed edge functions:** 512 MB
- **CPU execution time per request:** 50 ms
   
   This tracks all time spent running your scripts. Execution time does not include time spent waiting for resources or responses.
- **Response header timeout:** 40 s

## Invocation limits

The number of invocations allowed per month varies by team plan. Check your usage & billing dashboard for more information or you can reach out to [Support](https://www.netlify.com/support/).

Cached responses from edge functions [configured for caching](/build/edge-functions/optional-configuration#response-caching) do not count toward edge function invocations.

## Feature limitations

- If a site has [Netlify's Split Testing](/manage/monitoring/split-testing/) enabled, requests to that site will not execute edge functions.
- If a site is using [Netlify's Custom Headers](/manage/routing/headers), including [basic authentication headers](/manage/routing/headers#basic-authentication-headers), they will not apply to edge functions.
- If a site has [prerendering](/build/post-processing/prerendering/) enabled, it will not apply to paths where the response is served from an edge function.
- Unexpected collisions may occur if a site has multiple framework plugins generating edge functions as part of the build.
- Edge functions can only [rewrite requests](/build/edge-functions/api#return-a-rewrite) to same-site URLs. To fetch content hosted on another Netlify site or an external site, use the [`fetch` Web API](/build/edge-functions/api#supported-web-apis).
- Edge functions [configured for caching](/build/edge-functions/optional-configuration#response-caching) always shadow static files that actually exist within the site. If an edge function configured for caching is declared to run on `/*` and there's a `cat.png` static file, a request to `/cat.png` serves the edge function rather than the static file.
- There is no local caching for edge functions. Any HTTP headers for cache configuration in an edge function are ignored in local testing.
- Netlify Edge Functions is not currently supported as part of our HIPAA-compliant hosting offering. For more information, visit our [Trust Center](https://trust-center.netlify-corp.com) and download our reference architecture for HIPAA-compliant composable sites on Netlify.

### Tip - Learn more about the edge function processing order and caveats

Along with the above limitations, we recommend you review our docs on the [declaration processing order](/build/edge-functions/declarations#declaration-processing-order) and [caveats](/build/edge-functions/declarations#processing-order-caveats) to consider when you create edge functions.


