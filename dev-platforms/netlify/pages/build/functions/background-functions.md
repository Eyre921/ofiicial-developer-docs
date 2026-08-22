---
title: "Background Functions"
source: https://docs.netlify.com/build/functions/background-functions.md
path: build/functions/background-functions
---

---
title: "Background Functions overview"
description: "Use Background Functions for long-running serverless functions that handle tasks like batch processing, scraping, and more."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

> **Pricing Information:** This feature is available on [Credit-based plans, including Free, Personal, and Pro](https://www.netlify.com/pricing/?category=developer) and on [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans. [Learn more.](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-legacy-plans/legacy-pricing-plans/)

Netlify's Background Functions provide an option for serverless functions that run for up to 15 minutes and don't need to complete before a visitor can take next steps on your site. For tasks like batch processing, scraping, and slower API workflow execution, they may be a better fit than synchronous functions.

## How background functions work

Background functions are longer-running functions that are processed as background tasks using asynchronous invocation.

When a function is invoked asynchronously, there is an initial `202` success response that indicates that the function was successfully invoked. The function will run separately in the background until it completes or it reaches the 15 minute execution limit. If function invocation returns an error, a retry happens after one minute. If it fails again, another retry happens two minutes later.

When a background function is successfully executed, you generally pass the result to a destination other than the originating client.

Like all Netlify Functions, background functions are version-controlled, built, and deployed along with the rest of your Netlify site. Background functions are deployed with the [default values](/build/functions/configuration#default-values), and you can [configure](/build/functions/configuration) and [monitor](/build/functions/logs) them along with your other functions.

Background functions don't support response streaming because they don't return responses.

## Create background functions

To enable background mode on a function, set `background: true` in the function's [config](/build/functions/api#config-object). For example:

```typescript title="netlify/functions/process.mts"

export default async (req: Request) => {
  // Long-running work. The client has already received a 202 response.
}

export const config: Config = {
  background: true,
  path: "/process",
}
```

Background function syntax is otherwise identical to synchronous function syntax - a default export that receives a web platform [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and a [Netlify-specific `Context`](/build/functions/api#context-object) object. The difference is that the client receives an empty `202` response immediately, so you generally pass the invocation result to a destination other than the originating client.

You can also configure background mode through `netlify.toml`:

```toml
[functions.process]
  background = true
```

### Legacy filename convention

Before `config.background` was introduced, background mode was enabled by naming the function file with a `-background` suffix.

This convention is still fully supported and continues to work, but new functions should prefer the `config.background` property described above - keeping configuration alongside the rest of your function's settings is easier to read, easier to toggle, and easier for AI coding agents to discover.

For example, the following file would deploy as a background function called `hello-background`:

```typescript title="netlify/functions/hello-background.mts"

export default async (req: Request, context: Context) => {
  // Long-running work. The client has already received a 202 response.
}

export const config: Config = {
  path: "/process",
}
```

The suffix also works on subdirectory-based functions (`netlify/functions/hello-background/index.mts`).

## More Background Functions resources

- [Netlify Blog: What are Background Functions?](https://www.netlify.com/blog/2021/01/07/what-are-background-functions/)
- [Netlify Blog: Background and Scheduled API Routes for Next.js](https://www.netlify.com/blog/new-background-scheduled-api-routes-nextjs/)

