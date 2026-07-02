---
title: "Async Workloads Limits"
source: https://docs.netlify.com/build/async-workloads/limitations.md
path: build/async-workloads/limitations
---

---
title: "Async Workload Limitations"
description: "Details for how to leverage Async Workloads within it's limits."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

This page captures all of the unique limitations of Async Workloads that run on Netlify Functions.

## Payload limitations

The internal router reduces invocations when possible by batching up to 10 requests at once. Given the [6 MB limit](/build/functions/overview#default-deployment-options) for Netlify functions, the data limit for Async Workload event payloads should stay under 500 KB each to allow for overhead with metadata of the system.

We recommend that you use the [claim check design pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check) to avoid sending large payloads in event-driven architectures

## Functions configuration

Async Workloads brings durable, event-driven architecture to Netlify functions. Under the hood, they are still serverless functions and you can set configuration inline in function code. Because the Async Workloads system will handle all event routing, do not set the `path` or `schedule` [inline configuration](/build/functions/get-started/?fn-language=ts#route-requests) for a serverless function. At this time, there is no way to invoke Async Workload functions directly without using the `AsyncWorkloadClient` or the router API. Given this, if you would like to invoke the workload at a specific route, create a separate serverless function or edge function and then add the `client.send()` call to invoke it. This allows for the custom path while also keeping control over the authorization and event routing with Async Workloads.

