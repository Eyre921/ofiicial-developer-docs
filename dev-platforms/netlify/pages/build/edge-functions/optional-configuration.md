---
title: "Edge Functions Configuration"
source: https://docs.netlify.com/build/edge-functions/optional-configuration.md
path: build/edge-functions/optional-configuration
---

---
title: "Optional configuration for edge functions"
description: "Learn about optional configuration settings you can use for more control over how your edge functions are built and executed, such as response caching."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

This document describes optional configuration settings you can use for more control over how your edge functions are built and executed.

## Edge functions directory

The default edge functions directory is `YOUR_BASE_DIRECTORY/netlify/edge-functions`. 

You can specify a custom edge functions directory with the `edge_functions` key in `netlify.toml`. For example, to use the `my-custom-directory` directory, add the following to the `build` section in `netlify.toml`:

```toml
[build]
  edge_functions = "my-custom-directory"
```

The path is an absolute path relative to the site's [base directory](/build/configure-builds/overview#definitions-1) in your repository. To help keep your site secure, make sure your edge functions directory is outside of your [publish directory](/build/configure-builds/overview#definitions-1) so that your source files aren't deployed as part of your site.

## Response caching

You have the option to cache edge function responses for even faster response times. When the edge function gets a request and a cached response is available, we will serve the response directly from the edge cache. This bypasses the edge function invocation altogether and serves the response from as close to the user as possible for fast response times.

### When to use caching

If an edge function is [used as an endpoint](/build/edge-functions/api#return-a-response) to return a response directly and that response can be reused for different requests from multiple clients, we recommend that you configure the edge function for caching to further optimize performance.

If, however, the edge function is [used as middleware](/build/edge-functions/api#modify-a-response) to inform routing or transform requests / responses, we recommend that you do not configure the edge function for caching. This guarantees that the edge function will be invoked for every single request and can generate unique responses for different requests.

Here are some example use cases and recommendations:
- **Server-side rendering should use caching.** Imagine an edge function tasked with server-side-rendering a page and producing the HTML output. Since the output is the same for all requests, the initial response can be reused for future requests.
- **Personalization should not use caching.** Imagine an edge function that rearranges the order of items on a products page based on a set of preferences captured in a cookie. Since the outcome is unique to the specific client that is making the request, the logic for reading the cookie and rearranging the items needs to be invoked for every single request. 

### Configure an edge function for caching

There are two parts to configuring an edge function for caching:
- [Opt in to caching](#opt-in-to-caching) by setting the `cache` property to `manual`
- [Customize cache behavior](#customize-cache-behavior) by specifying HTTP headers

If you do one part but not the other, your edge function responses will not be cached. They will use the default behavior and every request to the edge function will invoke the function for a fresh response.

Keep the [Edge Functions feature limitations](/build/edge-functions/limits#feature-limitations) in mind when configuring caching.

#### Opt in to caching

You can set the `cache` property to `manual` inline in the function code, or in `netlify.toml`.

For inline configuration, use the `config` object in your edge function file.

```ts
import type { Config } from "@netlify/edge-functions"

export default async () => new Response("Hello, world!")

export const config: Config = {
  cache: "manual",
  path: "/hello"
}
```

For file-based configuration, use the `edge_functions` property in `netlify.toml`.

```toml
[[edge_functions]]
  cache = "manual"
  path = "/hello"
  function = "hello-world"
```

#### Customize cache behavior

You must specify caching headers inline in the function code.

```ts
import type { Context, Config } from "@netlify/edge-functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello world", {
		headers: {
			'cache-control': 'public, s-maxage=3600'
		}
	});
}
```

### Supported headers

We support the following HTTP headers for edge functions configured for caching:

- **[`Cache-Control`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)**, **`CDN-Cache-Control`**, and **`Netlify-CDN-Cache-Control`:** visit our [caching](/build/caching/caching-overview) doc to learn more about how Netlify handles these headers, including their order of precedence and supported directives.
- **[`Expires`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires):** store and reuse the cached response until this date/time. Overridden by `max-age` and `s-maxage`.
- **[`Vary`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary)** and **`Netlify-Vary`:** visit our [caching](/build/caching/caching-overview) doc to learn more about how Netlify handles these headers, including supported instructions and guidance on when to use which option.

By default, [cached responses respect atomic deploys](/build/caching/caching-overview#automatic-invalidation-with-atomic-deploys). This means that `s-maxage`, `max-age`, and `Expires` are voided by a new deploy in an identical [deploy context](/deploy/deploy-overview#deploy-contexts) (such as the same Deploy Preview number, or the same branch deploy). 

For example, imagine an edge function in published production deploy `A` that is configured for caching with `"cache-control": "public, s-maxage=3600"`. If deploy `B` becomes the new published production deploy five minutes later, we discard any responses previously cached. Even though the previously cached responses are configured to be stored and reused for one hour, they are discarded since they belong to a different deploy.

## Error handling

Because edge function failures can have different consequences in different contexts, you can customize what happens after an edge function errors. By default, when an edge function errors, we stop the request chain and serve a [generic error page](https://edge-functions-examples.netlify.app/error).

![Error page with error message and next steps for site visitors and site owners.](/images/edge-functions-error.png)

Alternatively, you can choose to serve a rewrite to a specific custom path or have the request chain continue.

### When to customize error handling

If an edge function is responsible for critical business logic, errors should block access (_fail closed_). Depending on your audience and content, the default error page may suffice or you may want to rewrite to a custom path.

If, however, the edge function is used for progressive enhancement, errors should allow access (_fail open_). In these cases letting the request proceed to serve baseline essential content is a better user experience than stopping the request and serving an error page.

Here are some example use cases for edge functions and recommendations for error handling:

- **Authentication on an internal site should serve the default generic error page.** If the edge function errors and the user cannot be authenticated, stopping the request chain and serving an error page protects your gated content. In the case of an internal site, the default error page is helpful to your engineering team because it provides a link to the edge function logs for troubleshooting.

- **Authentication on a customer-facing site should rewrite to a custom path.** If the edge function errors and the user cannot be authenticated, stopping the request chain and serving a custom error page protects your gated content. In the case of a customer-facing site, rewriting to a custom path allows you to provide a branded error message with more specific guidance to your site visitors to keep them engaged and get them unblocked.

- **Localization that is nice to have but not business-critical should be bypassed.** If the edge function errors and content can't be translated based on the user's location, it's okay to let the request proceed and serve untranslated content. In this case, though the user experience isn't ideal, the user can still engage with your content by using an external translation tool to read unlocalized text.

### Configure error handling for an edge function

To customize error handling, use the `onError` property inline in the function code. Supported values are:
- **`fail`:** serve a generic error page. This is the default if `onError` is not specified.
- **`/YOUR_CUSTOM_PATH`:** rewrite to the specified same-site path. Must start with `/`. The path is served without invoking any edge functions that may be declared for that path.
- **`bypass`:** skip the erroring edge function and continue the request chain.

### Tabs Component:

<TabItem label="fail">
```ts
import { Config } from "@netlify/edge-functions"

export default async () => {
  throw new Error("error");
};

export const config: Config = {
  path: "/hello",
  onError: "fail"
}
```
</TabItem>

<TabItem label="path">
```ts
import { Config } from "@netlify/edge-functions"

export default async () => {
  throw new Error("error");
};

export const config: Config = {
  path: "/hello",
  onError: "/unavailable"
}
```
</TabItem>

<TabItem label="bypass">
```ts
import { Config } from "@netlify/edge-functions"

export default async () => {
  throw new Error("error");
};

export const config: Config = {
  path: "/hello",
  onError: "bypass"
}
```
</TabItem>

