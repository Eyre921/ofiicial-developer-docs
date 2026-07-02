---
title: "Netlify Edge Functions API"
source: https://docs.netlify.com/build/edge-functions/api.md
path: build/edge-functions/api
---

---
title: "Edge Functions API"
description: "Use this API reference to write edge function files with JavaScript or TypeScript that export default functions responsible for processing requests."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

This page provides an overview of key concepts as well as a full reference.

## Overview

Use TypeScript or JavaScript to create an edge function file that exports a default function responsible for processing a request.

When the function is invoked, it receives two arguments:

- a [standard `Request` object](https://developer.mozilla.org/en-US/docs/Web/API/Request) representing the incoming HTTP request
- a [Netlify-specific `Context` object](#netlify-specific-context-object)

The expected return value is one of the following:

- a [standard `Response` object](https://developer.mozilla.org/en-US/docs/Web/API/Response) representing the HTTP response to be delivered to the client
- a [standard `URL` object](https://developer.mozilla.org/en-US/docs/Web/API/URL) if you want to rewrite the incoming request to another same-site URL with a 200 status code
- `undefined` if you choose to bypass the current function

### Edge function types

For TypeScript, you can import the types for the `Context` and `Config` objects from `@netlify/edge-functions`. The types for the `Request` and `Response` objects are in the global scope.

```ts
import type { Config, Context } from "@netlify/edge-functions";

export default async (request: Request, context: Context) => {
  // ...
};

export const config: Config = {
  path: "/",
};
```

### Request handling

Edge functions can handle requests in the following ways:

- [return a response](#return-a-response) directly as an endpoint
- [redirect](#return-a-redirect) to any URL
- [rewrite](#return-a-rewrite) to a same-site URL
- [modify a response](#modify-a-response) as middleware

### Tip - Looking for a list of available request headers?

Netlify doesn't add specific headers to edge function requests. To find information about the client request, use the [`context` object](/build/edge-functions/api#netlify-specific-context-object) instead.

#### Return a response

Similar to serverless functions and other endpoints, an edge function can just return a [standard `Response` object](https://developer.mozilla.org/en-US/docs/Web/API/Response). Once the function returns the response, the request chain ends and any redirects declared for that path do not occur.

For example, this edge function [returns the string](https://edge-functions-examples.netlify.app/example/hello) `Hello, World!` as text/html:

```ts
export default async () => {
  return new Response("Hello, World!", {
    headers: { "content-type": "text/html" }
  });
};
```

#### Return a redirect

You can use an edge function to return [an HTTP redirect](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections) to any URL of your choice.

To do this, use the [standard `Response.redirect` function](https://developer.mozilla.org/en-US/docs/Web/API/Response/redirect), as shown in the example below.

```ts
export default async (req: Request, { cookies, geo }: Context) => {
  if (
    geo.city === "Paris" &&
    cookies.get("promo-code") === "15-for-followers"
  ) {
    const url = new URL("/subscriber-sale", req.url);

    return Response.redirect(url);
  }
};
```

#### Return a rewrite

Similar to our [static routing engine](/manage/routing/redirects/rewrites-proxies), an edge function can also return a rewrite, which is a redirect with a 200 status code. This means that the URL in the visitor's address bar remains the same, while Netlify's servers fetch the new location behind the scenes.

To do this, return a [standard `URL` object](https://developer.mozilla.org/en-US/docs/Web/API/URL) with the path you want to rewrite to.

```ts
export default async (request: Request, { cookies, geo }: Context) => {
  if (
    geo.city === "Paris" &&
    cookies.get("promo-code") === "15-for-followers"
  ) {
    return new URL("/subscriber-sale", request.url);
  }
};
```

### Tip - Same-site URLs only

Edge functions can rewrite to only same-site URLs. To fetch content hosted on another Netlify site or an external site, use the [`fetch` Web API](/build/edge-functions/api#supported-web-apis).

#### Modify a response

An edge function can act as middleware that modifies and returns the response of subsequent functions or requests. This kind of edge function calls `context.next()` to continue the request chain and waits for a response to return before finishing execution.

Any edge functions that return `undefined` or use an empty `return;` also continue the request chain.

Once all edge functions for the initial path run, Netlify evaluates any redirect rules declared for that path and then continues the request chain to eventually serve static content or return a response from a serverless function. For more details on the order of events, review our docs on the [declaration processing order](/build/edge-functions/declarations#declaration-processing-order).

For example, this edge function uses `context.next()` to [transform the content](https://edge-functions-examples.netlify.app/example/transform) of the HTTP response to the requested path:

```ts
import type { Context } from "@netlify/edge-functions";

export default async (request: Request, context: Context) => {
  const url = new URL(request.url);

  // Look for the query parameter, and return if we don't find it
  if (url.searchParams.get("method") !== "transform") {
    return;
  }

  const response = await context.next();
  const text = await response.text();

  return new Response(text.toUpperCase(), response);
};
```

If you want to modify and return the content of a path other than the requested one, use `fetch()` to retrieve it.

```ts
export default async (req: Request) => {
  const url = new URL("/welcome", req.url);
  const res = await fetch(url);

  return someTransformationFunction(res);
};

export const config = { path: "/hello" };
```

##### Use conditional request

When using `context.next()` to transform a response, we modify the request to the downstream asset so that [conditional requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests#cache_update) don't apply and you always get a full response back.

If you want full control over the client caching behavior and you'd like to use conditional requests, you should pass the `sendConditionalRequest` to the `context.next()` call.

```ts
export default async (req: Request, { next }: Context) => {
  const res = await next({ sendConditionalRequest: true });

  // If the response is a 304, it's cached in the client and we can return it
  if (res.status === 304) {
    return res;
  }

  // Transform the response however you need
  const text = await res.text();

  return new Response(text.toUpperCase(), res);
};
```

##### Read request body

If you want to read the request body in your edge function, you need to explicitly pass on a new request with an unused body when you call `context.next()` afterwards. For example, `context.next(new Request(...))`. Without this, attempts to read the request body in subsequent edge functions will cause an error because a request body can only be read once.

```ts
export default async (req: Request, context: Context) => {
  const body = await req.json();

  if (!isValid(body.access_token)) {
    return new Response("forbidden", { status: 403 });
  }

  return context.next(new Request(req, { body: JSON.stringify(body) }));
};
```

### Runtime environment

Edge functions run in a [Deno](https://deno.land/) runtime environment that supports many standard Web APIs.

Edge Functions support Node.js built-in modules and Deno modules. Support for npm packages is in beta.

- For Node.js built-in modules, prefix the - For Deno modules, use a URL import. You can do this directly in the edge function code, for example `- For npm packages, install them [using `npm install`](https://docs.npmjs.com/cli/v6/commands/npm-install) or your favorite package manager. Then 
Edge functions have access to environment variables in the runtime environment. If you have the option to set specific scopes for your environment variables, the scope must include **Functions** to be available to edge functions during runtime. Learn more about how to set and use [environment variables with edge functions](/build/edge-functions/environment-variables).

### Import maps

When you import third-party modules in your edge function, it can be cumbersome to repeat the module's full URL in every import statement.

To use module names in your import statements, use an import map file to map module URLs to names. Netlify edge functions support separate import map files instead of import maps defined in `deno.json`. You can place the import map file anywhere in the project directory. For example, this file maps `html-rewriter` to `https://ghuc.cc/worker-tools/html-rewriter/index.ts`:

```json
{
  "imports": {
    "html-rewriter": "https://ghuc.cc/worker-tools/html-rewriter/index.ts"
  }
}
```

To enable the import map, declare it in `netlify.toml`:

```toml
[functions]
  deno_import_map = "./path/to/your/import_map.json"
```

You can now use `html-rewriter` as a shorthand for the module URL.

```ts
import { HTMLRewriter } from "html-rewriter";

export default async (request, context) => {
  return new HTMLRewriter()
    .on("p", {
      element(element) {
        element.tagName = "h1";
      }
    })
    .transform(await context.next());
};
```

## Type definitions

For TypeScript, you can import the types for the `Context` and `Config` objects from `@netlify/edge-functions`. The types for the `Request` and `Response` objects are in the global scope.

## Netlify-specific `Context` object

The `Context` object exposes the following properties:

### `account`
An object containing Netlify team account information. The `id` property in the object holds the unique ID of the team that the site and function belong to.

### `cookies`
A simplified interface for reading and storing cookies:

- **`cookies.get(name)`:** reads a cookie with a given name from the incoming request.
- **`cookies.set(options)`:** sets a cookie on the outgoing response, using the same format as the `options` value in [the `CookieStore.set` web standard](https://developer.mozilla.org/en-US/docs/Web/API/CookieStore/set).
    
- **`cookies.delete(name)`** or **`cookies.delete(options)`:** adds an instruction to the outgoing response for the client to delete a cookie. Following [the `CookieStore.delete` web standard](https://developer.mozilla.org/en-US/docs/Web/API/CookieStore/delete), accepts a string representing the name of the cookie, or an options object.

### Tip - Setting cookies across subdomains requires a custom domain

Since the `netlify.app` domain is used by many customers, it is listed in the Mozilla Foundation's [Public Suffix List](http://publicsuffix.org/), which prevents setting cookies across subdomains.

### `deploy`
An object containing Netlify deploy information with the following property:

- **`context`:** the [context](/deploy/deploy-overview/#deploy-contexts) of the deploy that the function belongs to.
- **`id`:** unique ID of the deploy that the function belongs to.
- **`published`:** a boolean that indicates whether or not the function belongs to the current [published deploy](/deploy/deploy-overview/#definitions).
- **`skewProtectionToken`:** a token that can be used to uniquely identify the deploy in HTTP calls when [skew protection](/deploy/deploy-overview/#skew-protection) is enabled.

### `geo`
An object containing geolocation data for the client with the following properties:

- **`city`:** name of the city.
- **`country`:**
  - **`code`:** ISO 3166 code for the country.
  - **`name`:** name of the country.
- **`latitude`:** latitude of the location.
- **`longitude`:** longitude of the location.
- **`subdivision`:**
  - **`code`:** ISO 3166 code for the country subdivision.
  - **`name`:** name of the country subdivision.
- **`timezone`:** timezone of the location.
- **`postalCode`:** postal (zip) code of the location. We support all regional formats, so the format will vary.

### `ip`
A string containing the client IP address.

### `next(options?)`

Invokes the [next item in the request chain](/build/edge-functions/api#modify-a-response). The method returns a `Promise` containing the `Response` from the origin that your edge function can modify before returning. 

For best performance, you should only use this method if you need access to the response body. In all other cases, you do not need to explicitly call `next`.

The method accepts an optional `options` object with the following property:

- **`sendConditionalRequest`:** set to true if you'd like to use [conditional requests](/build/edge-functions/api#use-conditional-request).

### `next(request, options?)`

Same method as above, except this one explicitly requires a `Request` object. 

This variation allows you to read the request body in your edge function and then pass a new request object with an unread body to the next item in the request chain. Without this, the `next()` call could fail as a request body can only be read once.

### `params`
An object containing the parameters set for the edge function's `path` in the [configuration object](/build/edge-functions/get-started#create-an-edge-function) and the values they receive from the incoming request URL. 

For example, for an edge function configured to run at `/pets/:name`, the `params` value for a request to `/pets/winter` will be `{"name":"winter"}`. 

To access the query string, use `request.url` instead.

### `requestId`
A string containing the Netlify request ID.

For example, `01FDWR77JMF2DA1CHF5YA6H07C`.

### `server`
An object containing server metadata with the following property:
- **`region`:** the region code where the deployment is running; for example, `us-east-1`.

### `site`
An object containing Netlify site metadata with the following properties:

- **`id`:** unique ID for the site; for example, `1d01c0c0-4554-4747-93b8-34ce3448ab95`.
- **`name`:** name of the site, its Netlify subdomain; for example, `petsof`.
- **`url`:** URL representing the main address to your site. It can be either a Netlify subdomain or your own custom domain if you set one; for example, `https://petsof.netlify.app` or `https://www.petsofnetlify.com`.

### `waitUntil`
`context.waitUntil()` is a function that implements the [`ExtendableEvent.waitUntil` standard](https://developer.mozilla.org/en-US/docs/Web/API/ExtendableEvent/waitUntil). It allows you to extend the edge function's execution until the given Promise it completed, **without blocking the response to the client** from being sent.

You can use it to perform any tasks after the response is sent, such as emitting analytics events or dispatching logs.

Usage notes:
- Any asynchronous work performed via `context.waitUntil` is still subject to the [CPU execution time limit](https://docs.netlify.com/build/edge-functions/limits/)

## `Netlify` global object 

This global object exposes the following properties:

### `Netlify.context`
The Netlify-specific [`context` object](#netlify-specific-context-object). 

This property is available within the [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope) of the function handler. If accessed from outside the handler, it returns `null`.

### `Netlify.env`
An object providing access to [environment variables](/build/edge-functions/environment-variables/) with the following properties:

- **`delete(name)`:** in the context of the invocation, deletes an environment variable with a given name.
- **`get(name)`:** returns the string value of an environment variable with a given name; if the environment variable is not defined, `undefined` is returned.
- **`has(name)`:** returns a boolean value containing `true` if an environment variable with a given name exists, and `false` otherwise.
- **`set(name, value)`:** in the context of the invocation, sets an environment variable with a given name and value.
- **`toObject()`:** returns a plain object containing all the environment variables and their values.

## Supported web APIs

Edge Functions support the following Web APIs:

- [`console`](https://developer.mozilla.org/en-US/docs/Web/API/console). When you use `console.log`, the [Edge Functions logs](/build/edge-functions/get-started#monitor) include which edge function generated the log message.
- [`atob`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/atob)
- [`btoa`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/btoa)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
  - `fetch`
  - `Request`
  - `Response`
  - `URL`
  - `File`
  - `Blob`
- [TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder)
- [TextDecoder](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)
- [TextEncoderStream](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoderStream)
- [TextDecoderStream](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoderStream)
- [Performance](https://developer.mozilla.org/en-US/docs/Web/API/Performance)
- [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Crypto)
  - `randomUUID()`
  - `getRandomValues()`
  - [SubtleCrypto](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto)
- [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [Timers](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
  - `setTimeout`
  - `clearTimeout`
  - `setInterval`
- [Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API)
  - `ReadableStream`
  - `WritableStream`
  - `TransformStream`
- [URLPattern API](https://developer.mozilla.org/en-US/docs/Web/API/URLPattern)

