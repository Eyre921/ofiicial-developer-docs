---
title: "Upstash Workflow Pricing"
source: https://upstash.com/docs/workflow/pricing
path: docs/workflow/pricing
---

Upstash Workflow is based on QStash and uses a "pay-as-you-go" pricing model. You only incur costs when your app receives traffic, meaning there's no charge when it's not in use. Click [here](https://upstash.com/pricing/workflow) to view the pricing.

A workflow run consists of several QStash messages, with the total cost determined by the number of messages used.

You can track your current message usage and associated costs in the [Overview tab of the console](https://console.upstash.com/qstash?tab=details).

  <img alt="Workflow message cost diagram" />

For detailed pricing information based on different plans, visit our [Workflow pricing page](https://upstash.com/pricing/workflow).

### Message Usage per Workflow Run

* [context.run](/docs/workflow/steps/run), [context.sleep](/docs/workflow/steps/sleep), [context.sleepUntil](/docs/workflow/steps/sleepUntil), or [context.waitForEvent](/docs/workflow/steps/waitForEvent) commands generate a single message.
* The [context.call](/docs/workflow/steps/call) command generates two messages.
* Each step in a [parallel run](/docs/workflow/howto/parallel-runs) costs 1 extra message.
* If the workflow endpoint or URL in [context.call](/docs/workflow/steps/call) returns an error or is unreachable, the workflow SDK will retry the call (up to 3 times by default). Each retry counts as a new message.

- [Upstash Workflow with Astro](https://upstash.com/docs/workflow/quickstarts/astro.md)
- [Upstash Workflow with Cloudflare Workers](https://upstash.com/docs/workflow/quickstarts/cloudflare-workers.md)
- [Upstash Workflow with Express.js](https://upstash.com/docs/workflow/quickstarts/express.md)
- [Upstash Workflow with FastAPI](https://upstash.com/docs/workflow/quickstarts/fastapi.md)
- [Upstash Workflow with Flask](https://upstash.com/docs/workflow/quickstarts/flask.md)
- [Upstash Workflow with Hono](https://upstash.com/docs/workflow/quickstarts/hono.md)
- [Upstash Workflow with Next.js and FastAPI](https://upstash.com/docs/workflow/quickstarts/nextjs-fastapi.md)
- [Upstash Workflow with Next.js and Flask](https://upstash.com/docs/workflow/quickstarts/nextjs-flask.md)
- [Upstash Workflow with Nuxt](https://upstash.com/docs/workflow/quickstarts/nuxt.md)
- [Upstash Workflow Supported Platforms](https://upstash.com/docs/workflow/quickstarts/platforms.md)
- [Upstash Workflow with SolidJS](https://upstash.com/docs/workflow/quickstarts/solidjs.md)
- [Upstash Workflow with SvelteKit](https://upstash.com/docs/workflow/quickstarts/svelte.md)
- [Upstash Workflow with TanStack Start](https://upstash.com/docs/workflow/quickstarts/tanstack-start.md)
- [Upstash Workflow with Next.js](https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md)
