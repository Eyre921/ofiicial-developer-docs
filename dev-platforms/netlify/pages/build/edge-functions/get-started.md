---
title: "Netlify Edge Functions: Get Started"
source: https://docs.netlify.com/build/edge-functions/get-started.md
path: build/edge-functions/get-started
---

---
title: "Get started with Edge Functions"
description: "Get started with Edge Functions by trying out a basic use case."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

This page will help you get started with Edge Functions. It describes how to create, test, deploy, invoke, and monitor your edge functions. 

## Create an edge function

To create an edge function to deploy with your site, write a JavaScript or TypeScript file stored in your [edge functions directory](/build/edge-functions/optional-configuration#edge-functions-directory). The default edge functions directory is `YOUR_BASE_DIRECTORY/netlify/edge-functions`. 

For example, create a function file at `netlify/edge-functions/hello.js`:
    
```js
export default () => new Response("Hello world");

export const config = { path: "/test" };
```

The file includes two parts:
- The default export contains the handler function that runs when you make requests to the edge function. It often contains logic to modify requests and responses.
- The `config` export configures the file as an edge function and provides the path on which the edge function will be invoked. 

In this example, requests to `/test` will trigger the edge function and it will respond with `Hello world`.

### Tip - Beyond the basics

- To have nuanced control over the order in which edge functions run, [configure your edge function paths in `netlify.toml`](/build/edge-functions/declarations#declare-edge-functions-in-netlify-toml) instead of inline in the function file.
- For even faster response times, you can [cache edge function responses](/build/edge-functions/optional-configuration#response-caching).
- In case of an error, you can [customize error handling](/build/edge-functions/optional-configuration#error-handling).
- Avoid using Edge Functions in your site to request assets from the same site using `fetch()`

### Edge functions with `.jsx` or `.tsx`

You also have the option to use `.jsx` and `.tsx` files for your edge functions. This can be helpful if you want your function to handle server-side rendering (SSR) at the network edge. 

For example, this `.tsx` file contains the code to stream React SSR at the edge without a meta-framework:

```tsx
import React from "https://esm.sh/react";
import { renderToReadableStream } from "https://esm.sh/react-dom/server";
import type { Config, Context } from "@netlify/edge-functions";

export default async function handler(req: Request, context: Context) {
  const stream = await renderToReadableStream(
    <html>
      <title>Hello</title>
      <body>
        <h1>Hello {context.geo.country?.name}</h1>
      </body>
    </html>
  );

  return new Response(stream, {
    status: 200,
    headers: { "Content-Type": "text/html" },
  });
}

export const config: Config = {
  path: "/hello",
};
```

### Tip - Looking for type definitions?

For TypeScript, you can import the types for the `Context` and `Config` objects from `@netlify/edge-functions`. The types for the `Request` and `Response` objects are in the global scope.

## Test locally

You can use [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli) to test edge functions locally before deploying them to Netlify. 

 1. Ensure you have the latest version of Netlify CLI installed:

    ``` bash
    npm install netlify-cli -g
    ```

2. Launch [Netlify Dev](/api-and-cli-guides/cli-guides/local-development) to start a development environment that executes edge functions on local requests:
    
    ```bash
    netlify dev
    ```
    
3. Visit [localhost:8888/test](http://localhost:8888/test) to execute the `hello` edge function declared for the `/test` route.

Changes to edge functions are applied on new requests.

1. Edit `hello.js` to change the `Response`:
    
    ```js
    export default () => new Response("Updated hello!");

    export const config = { path: "/test" };
    ```
    
2. Save your updated function file.  
3. Reload [localhost:8888/test](http://localhost:8888/test) and note that the response has changed.

To debug edge functions locally, launch Netlify Dev with the `edge-inspect` or `edge-inspect-brk` flag. For details, visit the [CLI docs](https://cli.netlify.com/commands/dev/). 

By default, the `geo` location used is the location of your local environment. To override this to a default mock location of San Francisco, CA, USA, use the `--geo=mock` flag. To mock a specific country, use `--geo=mock --country=` with a two-letter country code. For more information about the `--geo` flag, visit the [CLI docs](https://cli.netlify.com/commands/dev/).

## Deploy

Use [continuous deployment](/deploy/create-deploys#deploy-with-git) or [Netlify CLI manual deploys](/api-and-cli-guides/cli-guides/get-started-with-cli#manual-deploys) to deploy your edge functions. 

### Note - Use CLI version 12.2.8 or later for manual deploys

Manual deploys of edge functions are supported with Netlify CLI version 12.2.8 or later. Deploys made with older CLI versions will result in deployment errors.

If a project has TypeScript and JavaScript edge functions with the same name, for example, `my-function.ts` and `my-function.js`, the TypeScript function is ignored while the JavaScript function is deployed.

## Invoke

Invoke the deployed production version of your `hello` edge function declared for the `/test` route by accessing `mysitename.netlify.app/test`

Deploys of edge functions are atomic. This means that when a new deploy includes changes to function logic or declarations, the behavior of edge functions in old deploys won't be impacted. Updates to edge functions move to production only when you publish a new production deploy.

## Monitor

To access logs for your production edge functions:

1. In the Netlify UI, for your chosen site, visit 
### NavigationPath Component:

Logs & Metrics > Edge Functions
.

To access logs for other versions of your edge functions: 

1. In the Netlify UI, go to your site's **Deploys** tab.
2. Find the deploy of interest.
3. Follow the **Edge Functions** link in the deploy detail page header.

### Log contents

Netlify provides a log of any console statements output by your edge functions. The log for each console statement includes the name of the edge function that generated the output.

#### Date filter

By default, the Edge Function log displays a live tail of the latest activity in **Real-time**. You can also filter to review data from a specific time period, including the **Last hour**, **Last day**, **Last 7 days**, or select **Custom** to input a specific date and time range.

#### Text filter

To make debugging easier, you can filter the logs by edge function name or path. If desired, you can also use [pattern matching](https://www.npmjs.com/package/glob#glob-primer) as part of your query. 

### Log retention

Logs are retained for at least 24 hours of edge function activity, even after a new edge function deployment. This log retention period increases to 7 days for certain [pricing plans](https://www.netlify.com/pricing/?category=developer#features-edge-functions-log-retention). 

### Log Drains

> **Pricing Information:** This feature is available on [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

You can connect your edge function logs to third-party monitoring services for analysis using Netlify's Log Drains feature. Check out our [Log Drains](/manage/monitoring/log-drains) doc for more information. 

