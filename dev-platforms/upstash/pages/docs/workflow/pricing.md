---
title: "Pricing"
source: https://upstash.com/docs/workflow/pricing
path: docs/workflow/pricing
---

Upstash Workflow is based on QStash and uses a "pay-as-you-go" pricing model. You only incur costs when your app receives traffic, meaning there's no charge when it's not in use. Click [here](https://upstash.com/pricing/workflow) to view the pricing.

A workflow run consists of several QStash messages, with the total cost determined by the number of messages used.

You can track your current message usage and associated costs in the [Overview tab of the console](https://console.upstash.com/qstash?tab=details).

  <img />

For detailed pricing information based on different plans, visit our [Workflow pricing page](https://upstash.com/pricing/workflow).

### Message Usage per Workflow Run

* [context.run](/docs/workflow/basics/context#context-run), [context.sleep](/docs/workflow/basics/context#context-sleep), [context.sleepUntil](/docs/workflow/basics/context#context-sleepuntil), or [context.waitForEvent](/docs/workflow/basics/context#context-waitforevent) commands generate a single message.
* The [context.call](/docs/workflow/basics/context#context-call) command generates two messages.
* Each step in a [parallel run](/docs/workflow/howto/parallel-runs) costs 1 extra message.
* If the workflow endpoint or URL in [context.call](/docs/workflow/basics/context#context-call) returns an error or is unreachable, the workflow SDK will retry the call (up to 3 times by default). Each retry counts as a new message.

- [Astro](https://upstash.com/docs/workflow/quickstarts/astro.md)
- [Cloudflare Workers](https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md)
- [Express.js](https://upstash.com/docs/workflow/quickstarts/express.md)
- [FastAPI](https://upstash.com/docs/workflow/quickstarts/fastapi.md)
- [Flask](https://upstash.com/docs/workflow/quickstarts/flask.md)
- [Hono](https://upstash.com/docs/workflow/quickstarts/hono.md)
- [Next.js & FastAPI](https://upstash.com/docs/workflow/quickstarts/nextjs-fastapi.md)
- [Next.js & Flask](https://upstash.com/docs/workflow/quickstarts/nextjs-flask.md)
- [Nuxt](https://upstash.com/docs/workflow/quickstarts/nuxt.md)
- [Supported Platforms](https://upstash.com/docs/workflow/quickstarts/platforms.md)
- [SolidJS](https://upstash.com/docs/workflow/quickstarts/solidjs.md)
- [SvelteKit](https://upstash.com/docs/workflow/quickstarts/svelte.md)
- [TanStack Start](https://upstash.com/docs/workflow/quickstarts/tanstack-start.md)
- [Next.js](https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md)
