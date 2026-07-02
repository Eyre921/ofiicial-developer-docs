---
title: "Netlify On-demand Builders"
source: https://docs.netlify.com/build/configure-builds/on-demand-builders.md
path: build/configure-builds/on-demand-builders
---

---
title: "On-demand Builders"
description: "Use On-demand Builders to build pages for your site when users visit them for the first time, then cache the built pages at the edge for subsequent visits."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

On-demand Builders are serverless functions used to generate web content as needed that's automatically cached on Netlify's Edge CDN. They enable you to build pages for your site when a user visits them for the first time and then cache them at the edge for subsequent visits.

### Tip - Consider serverless functions with the durable cache instead

For better performance and fewer function invocations, consider using [serverless functions with the `durable` directive](/build/caching/caching-overview#durable-directive) instead of On-demand Builders.

Key characteristics of On-demand Builders:

- They are Lambda-compatible serverless functions written [in TypeScript](/build/functions/lambda-compatibility/?fn-language=ts) or [in JavaScript](/build/functions/lambda-compatibility/?fn-language=js).
- They accept GET requests only.
- They don't provide access to HTTP headers or query parameters from incoming requests.
- They are protected from repeated invocations by caching generated pages or assets.
- They use the request's URL path to determine whether to create a new cache object or reuse an existing one. This approach can't be customized with [cache key variations](/build/caching/caching-overview#cache-key-variation).
- They use the [response type](#cached-responses) to determine whether or not to cache the response.
- They support an optional [time to live (TTL)](#time-to-live-ttl) pattern for configuring caching. They don't support [cache control headers](/build/caching/caching-overview).
- They buffer responses. They don't support response streaming.
- A new site deploy invalidates the cached responses associated with builders in the same [deploy context](/deploy/deploy-overview#deploy-contexts), such as the same Deploy Preview number or the same branch deploy.

On-demand Builders were designed to support Incremental Static Regeneration (ISR) for [Next.js sites using Netlify's Next.js Runtime v4](/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/overview).

## Cached responses

Successful responses, redirection responses, and Not Found responses are cached at the edge and served to subsequent requests. That is, any response with a status code of `2xx` (such as `200` or `201`), `301`, `302`, `307`, `308`, or `404` is cached.

If you use [Time to Live (TTL)](#time-to-live-ttl), responses with the above status codes invalidate the cache after the TTL expires.

Responses with any other status codes, such as `500`, are not cached.

## Create On-demand Builders

To get started, follow our docs to create a Lambda-compatible function [in TypeScript](/build/functions/lambda-compatibility/?fn-language=ts) or [in JavaScript](/build/functions/lambda-compatibility/?fn-language=js). Use the synchronous function format, and return a response that can be served as a cached static asset. To convert the function to a builder, use the `builder()` method from the [`@netlify/functions`](https://github.com/netlify/primitives/tree/main/packages/functions) package.

First, add the package to your site dependencies:

```bash
npm install -D @netlify/functions
```

Then, pass your function as a parameter to the `builder()` method and export this method as the `handler` from your function file.

### Tabs Component:

<TabItem label="TypeScript">
```ts
import { builder, type Handler } from "@netlify/functions";

const myHandler: Handler = async (event, context) => {
// logic to generate the required content
};

const handler = builder(myHandler);

export { handler };

````
</TabItem>

<TabItem label="JavaScript">
```js
const { builder } = require("@netlify/functions")

async function handler(event, context) {
  // logic to generate the required content
}

exports.handler = builder(handler);
````

</TabItem>

For example, your builder could return a full HTML page or a processed image file. Here's a "hello world" example:

### Tabs Component:

<TabItem label="TypeScript">
```ts
import { builder, type Handler } from "@netlify/functions";

const myHandler: Handler = async (event, context) => {
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "text/html",
    },
    body: `<!DOCTYPE html> <html> <body> Hello World </body> </html>`,
  };
};
const handler = builder(myHandler);

export { handler };

````
</TabItem>

<TabItem label="JavaScript">
```js
const { builder } = require("@netlify/functions")

async function handler(event, context) {
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "text/html",
    },
    body: `
    <!DOCTYPE html>
      <html>
        <body>
          Hello World
        </body>
    </html>
    `,
  };
}

exports.handler = builder(handler);
````

</TabItem>

On success, this builder returns a `200` status code and an HTML page with a "Hello World" message. This successful response is cached at the edge and served to subsequent requests.

If the initial invocation of a builder fails with a status code that is not one of the [cached response codes](#cached-responses), for example because a third-party API is down and the response status is `500`, the erroring response is served but not cached. The next request will retry the builder to get a successful response.

For a working example of using On-demand builders with code to explore, you can visit this [example site](https://every-color.netlify.app/) and its corresponding [code repository](https://github.com/netlify/example-every-color).

### Time to live (TTL)

On-demand Builders support an optional time to live (TTL) pattern that allows you to set a fixed duration of time after which a cached builder response is invalidated. This allows you to force a refresh of a builder-generated response without a new deploy.

You can set a TTL for your builder by including a `ttl`, in seconds, in your response. `ttl` has a minimum value of 60.

### Tabs Component:

<TabItem label="TypeScript">
```ts
import { builder, type Handler } from "@netlify/functions";

const originalResponse = {
  body: ':thumbsup:',
  statusCode: 200,
  ttl: 3600,
};

const myHandler: Handler = async (event, context) => {
// logic to generate the required content

return originalResponse;
};

const handler = builder(myHandler);

export { handler };

````
</TabItem>

<TabItem label="JavaScript">
```js
const { builder } = require("@netlify/functions")

const originalResponse = {
  body: ':thumbsup:',
  statusCode: 200,
  ttl: 3600,
}

async function handler(event, context) {
  // logic to generate the required content

  return originalResponse
}

exports.handler = builder(handler);
````

</TabItem>

After the TTL has expired, the next request triggers a builder invocation to regenerate the content. The previously cached response is served for 60 seconds after a refresh is triggered. If the refresh is successful and returns with one of the [cached response codes](#cached-responses), the updated response is cached and served until the next successful refresh. If the refresh fails and returns with any other status code, for example because a third-party API is down, the previously cached successful response is served until the next successful refresh.

### Confirm request type

Incoming requests to On-demand Builders include a `x-nf-builder-cache` header that indicates whether the request is an initial request for your content or a background refresh request. This gives you the opportunity to add conditional logic to your builder depending on the request type - for example, you might want to serve a loading page while a user waits for an initial request to complete.

To confirm the type of the incoming request, check the `x-nf-builder-cache` header value in the `headers` property of the `event` object. If the header's value is `miss`, the request is an initial blocking request from the browser that needs to complete before a user can take next steps. If the header's value is `revalidate`, the request is an asynchronous TTL refresh request that runs in the background.

### Environment variables

On-demand Builders have access to environment variables in the runtime environment. If you have the option to set specific scopes for your environment variables, the scope must include **Functions** to be available to On-demand Builders during runtime.

Learn more about how to set and use [environment variables with functions](/build/functions/environment-variables).

## Use On-demand Builders

Similar to other functions, On-demand Builders can be invoked at endpoints relative to the base URL of your site. Builders, however, use a unique `builders` path for invocation:
`/.netlify/builders/FUNCTION_NAME`.

Builder endpoints can be called directly like regular web URLs or can be executed by redirecting traffic from another URL.

For example, consider a news site with a large amount of infrequently visited, archived content. You can use a builder to generate those less-frequented pages on-demand when a user requests them. The request URL might be something like this:

```html
https://myawesomenews.com/.netlify/builders/my-archive-builder/article/199x-news
```

The first call to the builder invokes it and returns the generated page, assuming that's the logic in your function. Subsequent calls return the cached page content until the next deploy or until the [time to live (TTL)](#time-to-live-ttl) has elapsed.

In another example, if you want to replace a static image `src` with a custom-sized image generated using a builder, you can format an `img` tag like this:

```html
<img
  alt="kittens."
  src="/.netlify/builders/my-image-transformer/file/kittens.jpg/width/640"
/>
```

The first builder call processes and returns the image, and subsequent calls return the cached image until the next deploy or until the [TTL](#time-to-live-ttl) has elapsed.

### Customize paths with redirects

In the example above, you might prefer to use a different URL instead of the default builder endpoint. You can do this by redirecting traffic from a URL to the builder using [redirect rules](/manage/routing/redirects/overview) in the `_redirects` file or `netlify.toml` Netlify configuration file.

Here are some examples with [`_redirects` file](/manage/routing/redirects/overview#syntax-for-the-_redirects-file) and [`netlify.toml`](/manage/routing/redirects/overview#syntax-for-the-netlify-configuration-file) syntax.

### Tabs Component:

<TabItem label="_redirects">
```
/images/*  /.netlify/builders/my-image-transformer   200

/archive /.netlify/builders/my-archive-builder 200

````
</TabItem>

<TabItem label="netlify.toml">
```toml
[[redirects]]
  from = "/images/*"
  to = "/.netlify/builders/my-image-transformer"
  status = 200

[[redirects]]
  from = "/archive"
  to = "/.netlify/builders/my-archive-builder"
  status = 200
````

</TabItem>

The original path is passed to the builder as part of the event object. To continue an example from above, a call to `/images/kittens.jpg/width/640` triggers the `my-image-transformer` function with the following values passed to it as part of the `event`:

```js
{
  "path": "/images/kittens.jpg/width/640",
  "httpMethod": "GET"
  ...
}
```

For more information about the `event` parameter and the Lambda-compatible Netlify Functions programming model, refer to our docs on [synchronous function format for TypeScript](/build/functions/lambda-compatibility/?fn-language=ts#synchronous-function-format) or [JavaScript](/build/functions/lambda-compatibility/?fn-language=js#synchronous-function-format-2).

#### Redirect workaround for query parameters

On-demand Builders currently don't process or cache query parameters from redirected paths. In most cases, it's preferable to embed these parameters into the path directly, but in cases where you don't control the path, you can re-shape it with an additional redirect rule to the path resolution. The first rule must have a `3XX` [HTTP status code](/manage/routing/redirects/redirect-options#http-status-codes), as that ensures a new URL for our redirects engine to process the second rule, passing your new path to the builder. Here's an example in `_redirects` syntax:

```
/generated/image url=:url w=:w /img/:url/:w 301!

/img/:url/:w /.netlify/builders/image 200
```

#### Shadowing

Redirect rules leverage [shadowing](/manage/routing/redirects/rewrites-proxies#shadowing), which means that they trigger only if there isn't already an asset at the specified `from` path. This can be useful if your prebuilt assets and content generated by your builder share the same path.

If you prefer to trigger the proxy regardless of the presence of a pre-built asset, you can append `!` to the status code in the `_redirects` file, or add `force = true` in `netlify.toml`.

### Local development

You can build and test logic like any other function using [Netlify Dev](/api-and-cli-guides/cli-guides/local-development). When testing locally, however, caching isn't available.

### Secure On-demand Builders

You can use the same authentication and authorization strategy as the rest of your Netlify site to secure builders. We recommend using JSON Web Tokens (JWT), roles, and redirect rules for managing granular access. Refer to [our docs on role-based access control](/manage/security/secure-access-to-sites/role-based-access-control) to learn more.

### Limits

- The maximum response payload size for a builder is 6 MB.
- Pages or assets generated by On-demand Builders are limited to 10,000 per deploy. For a higher limit, please [contact sales](https://www.netlify.com/contact/). If the limit is reached, additional generated pages or assets will have reduced caching and may be regenerated upon subsequent requests.
- There is a 30 second execution time limit that results in a timeout.

## Usage and billing

Requests to builders that return a previously non-cached response count towards your [Netlify Functions usage](/build/functions/usage-and-billing) for billing purposes. This includes requests per month and run time per month. If a cached response is available and served, no function invocation is made and no usage is incurred against your Netlify Functions allotment.

On-demand Builders execution doesn't count towards build minutes.

