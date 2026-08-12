---
title: "Cache API"
source: https://docs.netlify.com/build/caching/cache-api.md
path: build/caching/cache-api
---

---
title: "Cache API"
description: "Improve the performance of your application by caching web requests made from Functions and Edge Functions."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Store responses from web requests made from [Functions](/build/functions/overview) and [Edge Functions](/build/edge-functions/overview), making your application more performant, resilient and cost-efficient.

The Cache API is a great companion to Netlify's [fine-gained cache controls](/build/caching/caching-overview), giving you the power to cache entire routes as well as their individual components.

Built entirely on web standards, it works seamless with any web framework - or without one.

## Overview

The Cache API is a programmatic interface for reading and writing HTTP responses to a cache using the standard [CacheStorage](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage) and [Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache) JavaScript APIs.

Just like [Functions](/build/functions/get-started) and [Edge Functions](/build/edge-functions/api), the Cache API operates on [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects and has first-class support for the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

You can use the Cache API to cache any resource on the web, whether it's hosted on Netlify or any other provider.

## Features

The Cache API uses standard [cache control headers](/build/caching/caching-overview#supported-cache-control-headers) to determine the cache behavior for a response. This includes how long it can be cached for, how it's matched against a request and how it can be invalidated.

- Responses are automatically invalidated once their expiration time (defined by the `max-age` or `s-maxage` directives) has elapsed
- Responses can be manually invalidated by calling the [`delete()` method](#cachedelete) or by purging any [cache tags](/build/caching/caching-overview#purge-by-cache-tag) set on the response
- Responses stored with the Cache API are not replicated across regions, meaning that any functions and edge functions running on a given region all share the same cache data, but that data isn't shared with any functions or edge functions running on a different region
- Responses stored with the Cache API are automatically invalidated when your site is redeployed
- Requests to the Cache API are automatically routed to the closest region for optimal performance

## API reference

The Cache API offers the following methods, a subset of the standard [CacheStorage](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage) and [Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache) APIs.

### `caches.match`

Retrieves a response from any of the `Cache` instances, if found.

```ts
const response = await caches.match(request);
```

#### Parameters

- **`request`:** the request for which you are attempting to find responses in the caches; this can be a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object or a URL string

#### Return value

A `Promise` that resolves to the [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) associated with the first matching request in any of the caches. If no match is found, the `Promise` resolves to `undefined`.

### `caches.open`

Opens a named cache instance where you can store and retrieve responses.

The name parameter defines a namespace for a specific set of cached responses. You should use something meaningful for your application context.

Keep in mind that responses aren't shared between caches, so using multiple names can fragment your cache and reduce your hit ratio.

```ts
const cache = await caches.open("my-cache");
```

#### Parameters

- **`name`:** name of the cache

#### Return value

A `Promise` that resolves with a [Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache) instance.

### `cache.add`

Takes a URL, retrieves it, and adds the resulting response object to the given cache.

This is an instance method of a `Cache` object that must be created with [`caches.open()`](#cachesopen).

```ts
const cache = await caches.open("my-cache");

await cache.add(request);
```

#### Parameters

- **`request`:** a request for the resource you want to add to the cache; this can be a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object or a URL string

#### Return value

A `Promise` that resolves with `undefined`.

### `cache.addAll`

Takes an array of URLs, retrieves them, and adds the resulting response objects to the given cache.

This is an instance method of a `Cache` object that must be created with [`caches.open()`](#cachesopen).

```ts
const cache = await caches.open("my-cache");

const responses = await cache.addAll(requests);
```

#### Parameters

- **`request`:** an array of requests for the resource you want to add to the cache; these can be a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object or a URL string

#### Return value

A `Promise` that resolves with `undefined`.

### `cache.delete`

Finds a response that matches the given request and deletes it from the cache.

This is an instance method of a `Cache` object that must be created with [`caches.open()`](#cachesopen).

```ts
const cache = await caches.open("my-cache");

await cache.delete(request);
```

#### Parameters

- **`request`:** the request you are looking to delete from the cache; this can be a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object or a URL

#### Return value

A `Promise` that resolves with `true`.

### `cache.match`

Retrieves a response from the cache, if found.

This is an instance method of a `Cache` object that must be created with [`caches.open()`](#cachesopen).

```ts
const cache = await caches.open("my-cache");

const response = await cache.match(request);
```

#### Parameters

- **`request`:** the request for which you are attempting to find responses in the cache; this can be a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object or a URL string

#### Return value

A `Promise` that resolves to the [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) associated with the first matching request in the cache. If no match is found, the `Promise` resolves to `undefined`.

### `cache.put`

Adds a response to the cache.

This is an instance method of a `Cache` object that must be created with [`caches.open()`](#cachesopen).

```ts
const cache = await caches.open("my-cache");

await cache.put(request, response);
```

#### Parameters

- **`request`:** the request to be added to the cache; this can be a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object or a URL string
- **`response`:** the [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) you want to match up to the request

#### Return value

A `Promise` that resolves with `undefined`.

## Utility methods

The `@netlify/cache` module offers a set of utility methods that you can use on top of the base API to perform common tasks more easily. To use them, start by adding the module to your project using the [package manager of your choice](/build/configure-builds/manage-dependencies#javascript-dependencies):

```
npm install @netlify/cache
```

### `cacheHeaders`

Returns a object with a set of headers that represent the cache settings supplied.

```ts
cacheHeaders(cacheSettings);
```

The resulting headers are designed to make the most of [Netlify's caching primitives](/build/caching/caching-overview/), and some of them are specific to the Netlify platform. If you're looking to leverage only generic cache headers, consider using [the `cdn-cache-control` module](https://www.npmjs.com/package/cdn-cache-control) instead.

#### Parameters

- **`cacheSettings`:** an object with the different cache settings to be set, with support for the following properties:
  - `durable`: A boolean indicating whether to persist the response in the [durable cache](/build/caching/caching-overview#durable-directive)
  - `overrideDeployRevalidation`: Opts out of [automatic invalidation with atomic deploys](/build/caching/caching-overview#opt-out-of-automatic-invalidation) by specifying one or more cache tags that can be used for [on-demand invalidation](/build/caching/caching-overview#on-demand-invalidation)
  - `swr`: The value for [the `stale-while-revalidate` directive](/build/caching/caching-overview#stale-while-revalidate-directive), representing the amount of time (in seconds) after the response has expired during which it can still be served while it's revalidated in the background
  - `tags`: List of [cache tags](/build/caching/caching-overview#purge-by-cache-tag) to add to the response
  - `ttl`: The value for the `s-maxage` directive, representing the maximum amount of time (in seconds) that Netlify will cache the response
  - `vary`: An object containing the parts of the request [to vary on](/build/caching/caching-overview#cache-key-variation), with support for one or more of the following properties:
    - `cookie`: List of cookies to vary on
    - `country`: List of countries to vary on, with nested arrays representing _or_ conditions
    - `header`: List of headers to vary on
    - `language`: List of languages to vary on, with nested arrays representing [language combinations](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)
    - `query`: List of URL query parameters to vary on or `true` to vary on all query parameters

#### Return value

An object mapping header names to their values.

#### Example

This example shows how you might use the `cacheHeaders` utility method to return a response that will be cached for up to two days, with a set of cache tags and specific varying conditions.

```ts
import { cacheHeaders, DAY } from "@netlify/cache";
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  const headers = {
    "x-custom-header": "some value",
    ...cacheHeaders({
      ttl: 2 * DAY, // Two days
      tags: ["product", "sale"],
      vary: {
        cookie: ["ab_test_name", "ab_test_bucket"],
        query: ["item_id", "page"]
      }
    })
  }

  return new Response("I will be cached", { headers });
};

export const config: Config = {
  path: "/cacheheaders-example"
};
```

### `fetchWithCache`

Returns a response for the given request if it's found in the cache. If not, a new request is made and the response is added to the cache.

It's a drop-in replacement for the [standard `fetch` method](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch) with an additional optional parameter for configuring the cache settings of the response that is added to the cache. These options override any conflicting cache settings that the response may define.

```ts
fetchWithCache(resource);
fetchWithCache(resource, cacheSettings);
fetchWithCache(resource, options);
fetchWithCache(resource, options, cacheSettings);
```

#### Parameters

- **`response`:** the resource that you wish to fetch; this can be either a string, a [`URL` object](https://developer.mozilla.org/en-US/docs/Web/API/URL) or a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request)
- **`options`:** a standard [`RequestInit` object](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit) containing any custom settings that you want to apply to the request
- **`cacheSettings`:** an object with the different cache settings to be set, with support for the following properties:
  - `durable`: A boolean indicating whether to persist the response in the [durable cache](/build/caching/caching-overview#durable-directive)
  - `overrideDeployRevalidation`: Opts out of [automatic invalidation with atomic deploys](/build/caching/caching-overview#opt-out-of-automatic-invalidation) by specifying one or more cache tags that can be used for [on-demand invalidation](/build/caching/caching-overview#on-demand-invalidation)
  - `swr`: The value for [the `stale-while-revalidate` directive](/build/caching/caching-overview#stale-while-revalidate-directive), representing the amount of time (in seconds) after the response has expired during which it can still be served while it's revalidated in the background
  - `tags`: List of [cache tags](/build/caching/caching-overview#purge-by-cache-tag) to add to the response
  - `ttl`: The value for the `s-maxage` directive, representing the maximum amount of time (in seconds) that Netlify will cache the response
  - `vary`: An object containing the parts of the request [to vary on](/build/caching/caching-overview#cache-key-variation), with support for one or more of the following properties:
    - `cookie`: List of cookies to vary on
    - `country`: List of countries to vary on, with nested arrays representing _or_ conditions
    - `header`: List of headers to vary on
    - `language`: List of languages to vary on, with nested arrays representing [language combinations](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)
    - `query`: List of URL query parameters to vary on or `true` to vary on all query parameters

### Note - Stale while revalidate support

When using the `swr` option, `fetchWithCache` automatically handles background revalidation on the client. If a cached response is stale but still within the `stale-while-revalidate` window, the stale response is returned immediately and a background request is made to fetch a fresh response and update the cache.

#### Return value

A `Promise` that resolves to a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object.

#### Example

This example shows how you might use the `fetchWithCache` utility method to either retrieve a response from the cache or fetch it from the network. When the response is fetched from the network, it is then added to the cache with a set of options.

```ts
import { fetchWithCache, DAY } from "@netlify/cache";
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  const response = await fetchWithCache("https://example.com/expensive-api", {
    ttl: 2 * DAY, // Two days
    tags: ["product", "sale"],
    vary: {
      cookie: ["ab_test_name", "ab_test_bucket"],
      query: ["item_id", "page"]
    }
  });

  return response;
};

export const config: Config = {
  path: "/fetchwithcache-example"
};
```

### `getCacheStatus`

Extracts information from the `Cache-Status` header about how the response has interacted with the different components of Netlify's global caching infrastructure.

The returned value makes it straightforward to differentiate cached and uncached responses, which is especially useful when measuring performance.

```ts
getCacheStatus(cacheStatusHeader);
getCacheStatus(headers);
getCacheStatus(response);
```

#### Parameters

- **`cacheStatusHeader`:** a string containing the values of the `Cache-Status` header you want to inspect
- **`headers`:** a [`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers) object containing the `Cache-Status` header you want to inspect
- **`response`:** the [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object containing the `Cache-Status` header you want to inspect

#### Return value

An object containing the following properties:

- **`hit`**: a boolean indicating whether the response has been served from a Netlify cache
- **`caches`**: an object with granular information about the different Netlify caches:
  - **`durable`**: an object describing how the response has interacted with the [durable cache](/build/caching/caching-overview#durable-directive):
    - **`hit`**: a boolean indicating whether the response has been served by the durable cache
    - **`stale`**: a boolean indicating whether the response matched a stale entry in the cache (i.e. older than the specified age settings)
    - **`stored`**: a boolean indicating whether the response has just been stored in the durable cache
    - **`ttl`**: the number of seconds left before the response's expiration date; a negative number represents how long ago the response has expired
  - **`edge`**: an object describing how the response has interacted with the [edge cache](/build/caching/caching-overview):
    - **`hit`**: a boolean indicating whether the response has been served by the edge cache
    - **`stale`**: a boolean indicating whether the response matched a stale entry in the cache (i.e. older than the specified age settings)

#### Example

This example shows how you might use the `getCacheStatus` utility method to determine whether a response was retrieved from the cache, including information about which of Netlify's caching layers has served the response.

```ts
import { fetchWithCache, getCacheStatus } from "@netlify/cache";
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  const response = await fetchWithCache("https://example.com/expensive-api");
  const { hit, edge, durable } = getCacheStatus(response);

  if (hit) {
    console.log("Served from the cache:")
    console.log(`- Edge cache: ${edge?.hit ? "hit" : "miss"}`);
    console.log(`- Durable cache: ${durable?.hit ? "hit" : "miss"}`);
  } else {
    console.log("Served from the network:")
    console.log(`- Edge cache: ${edge?.stale ? "stale" : "not found"}`);
    console.log(`- Durable cache: ${durable?.stale ? "stale" : "not found"}`);
  }

  return response;
};

export const config: Config = {
  path: "/getcachestatus-example"
};
```

### `needsRevalidation`

Checks whether a cached response includes a signal indicating that the client should perform a background revalidation. This happens when a response is served from the Cache API with the [`stale-while-revalidate` directive](/build/caching/caching-overview#stale-while-revalidate-directive): the stale response is returned immediately, but the client is responsible for fetching a fresh response and writing it back to the cache with [`cache.put()`](#cacheput).

```ts
needsRevalidation(response);
```

#### Parameters

- **`response`:** the [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object to check for a revalidation signal

#### Return value

A `boolean` indicating whether the response requires background revalidation.

#### Example

This example shows how you might use the `needsRevalidation` utility method to manually handle stale-while-revalidate when using the Cache API directly.

```ts
import { needsRevalidation, cacheHeaders, MINUTE, HOUR } from "@netlify/cache";
import type { Config, Context } from "@netlify/functions";

const cache = await caches.open("my-cache");

export default async (req: Request, context: Context) => {
  const request = new Request("https://example.com/expensive-api");
  const cached = await cache.match(request);

  if (cached) {
    if (needsRevalidation(cached)) {
      // The response is stale but within the SWR window. Revalidate
      // in the background and write the fresh response to the cache.
      context.waitUntil(
        fetch(request).then((fresh) => {
          const response = new Response(fresh.body, {
            headers: {
              ...Object.fromEntries(fresh.headers),
              ...cacheHeaders({ ttl: MINUTE, swr: HOUR }),
            },
          });
          return cache.put(request, response);
        })
      );
    }

    return cached;
  }

  const fresh = await fetch(request);
  const response = new Response(fresh.body, {
    headers: {
      ...Object.fromEntries(fresh.headers),
      ...cacheHeaders({ ttl: MINUTE, swr: HOUR }),
    },
  });

  context.waitUntil(cache.put(request, response.clone()));

  return response;
};

export const config: Config = {
  path: "/needsrevalidation-example",
};
```

### Note

fetchWithCache</code>">
If you use [`fetchWithCache`](#fetchwithcache) with the `swr` option, background revalidation is handled automatically. You only need `needsRevalidation` when directly calling `cache.match` and `cache.put`.

## Usage with frameworks

The Cache API has been designed to work seamlessly with any web framework that deploys to Netlify. For the best development experience possible, that are a few important things to note.

The [CacheStorage API](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage) is exposed through the `caches` global variable, as defined by the spec. The API isn't part of Node.js though, which means this variable usually isn't available in Node.js environments.

On Netlify, we expose it automatically in the Netlify Functions and Netlify Edge Functions runtimes, both on live sites and locally with [Netlify Dev](/api-and-cli-guides/cli-guides/local-development/).

However, some frameworks have a setup where functions are not used in local development; or you might choose to run your framework's own development command and not use the Netlify CLI altogether. In those cases, the `caches` global will not be set and trying to access it will cause an error.

To get around that, you can 
```ts
import { caches } from "@netlify/cache";

const cache = await caches.open("my-cache");

await cache.set("https://example.com", new Response("Hello"));
```

Using this import does not change the functionality in any way, and does not require any further code changes. It's only required for local development in certain setups.

We're working with framework maintainers to make this global variable part of their local development servers, at which point you'll be able to completely remove the import.

## Limits

There is a limit to how many Cache API operations you can perform on a single serverless function or edge function invocation:

- Maximum number of cache lookups per invocation: 100
- Maximum number of cache insertions or deletions per invocation: 20

If you exceed any of these limits, any subsequent cache lookups will not return any response and any insertions or deletions will not actually modify the state of the cache.

When multiple edge functions run for a given request, these limits are shared by all the edge functions.

The limits are not shared between serverless functions and edge functions, which means that each group of functions will have their own quota.

## Notes and limitations

Keep the following limitations in mind when working with the Cache API:

- When a stale response is served within the [`stale-while-revalidate` directive](/build/caching/caching-overview#stale-while-revalidate-directive) window, the client is responsible for performing background revalidation - [`fetchWithCache`](#fetchwithcache) handles this automatically, or you can use [`needsRevalidation`](#needsrevalidation) to detect the signal and revalidate manually
- The Cache API is available in the [local development environment](/api-and-cli-guides/cli-guides/local-development) when using version 20.0.3 or above of the Netlify CLI; note that no cached responses are actually persisted anywhere, which means that lookups will not return a response and insertions or deletions will not mutate any state
- As per the [standard Cache API specification](https://w3c.github.io/ServiceWorker/#dom-cache-put), it is not possible to cache [partial responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/206), responses with a `Vary` header set to `*`, or responses for a request with a method other than `GET`

While the Netlify Cache API tries to follow the standard [CacheStorage](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage) and [Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache) APIs as closely as possible, there are some implementation differences associated with operating a cache on a globally-distributed infrastructure instead of the browser:

- The [`keys()`](https://developer.mozilla.org/en-US/docs/Web/API/Cache/keys) method is not implemented and there is currently no way to list the contents of the cache
- While [reads](#cachematch) and [writes](#cacheput) are strongly consistent, [deletions](#cachedelete) are eventually consistent, so reading an entry after deleting it may still yield the cached response for a short period of time while the deletion is propagated across the network

## Examples

Let's imagine a function that takes some input via a URL query parameter and uses it to make an HTTP request to an external API.

This fictional API is slow and expensive, so it's in our best interest to call it only when absolutely necessary. The following example shows how you might do this with the Cache API.

### Tabs Component:

<TabItem label="Original">
```ts
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  const request = new Request("https://example.com/expensive-api");

  // Call the external API. This will happen on every request.
  const response = await fetch(request);

  return response;
};

export const config: Config = {
  path: "/cache-api-example"
};

```
</TabItem>

<TabItem label="Cache API">
```ts
import type { Config, Context } from "@netlify/functions";

const cache = await caches.open("my-cache");

export default async (req: Request, context: Context) => {
  const request = new Request("https://example.com/expensive-api");

  // Look for the response in the cache.
  const cached = await cache.match(request);

  if (cached) {
    return cached;
  }

  // It's not in the cache, so let's fetch it.
  const fresh = await fetch(request);

  // Store it in the cache for future invocations. The response must be cloned
  // so that we can simultaneously stream it to the client and to the cache.
  if (response.ok) {
    cache.put(request, fresh.clone()).catch(error => {
      console.error("Failed to add to the cache:", error);
    });
  }

  return fresh;
};

export const config: Config = {
  path: "/cache-api-example"
};
```

</TabItem>

<TabItem label="Cache API + fetchWithCache">
```ts
import { fetchWithCache } from "@netlify/cache";
import type { Config, Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  const request = new Request("https://example.com/expensive-api");

  // Get the response from the cache if it's there. If not, fetch it
  // and store in the cache. This is a convenience method, equivalent
  // to the logic in the "Cache API" tab.
  const response = await fetchWithCache(request);

  return response;
};

export const config: Config = {
  path: "/cache-api-example"
};

```

</TabItem>

## Troubleshooting

### Outside handler scope

While you can [open a cache instance](#cachesopen) anywhere in your function code, you can only [read](#cachematch), [write](#cacheput) or [delete](#cachedelete) entries from the cache within the scope of your request handler.

Attempting to perform any of those operations in another scope (such as the global scope) will throw an error.

```ts
import type { Config, Context } from "@netlify/functions";

// ✅ This works.
const cache = await caches.open("my-cache");

// ❌ This will throw an error.
const cached = await cache.match("https://example.com");

export default async (req: Request, context: Context) => {
  // ✅ This works.
  const cached = await cache.match("https://example.com");

  if (cached) {
    return cached;
  }

  return new Response("Not in the cache", { status: 404 });
};

export const config: Config = {
  path: "/cache-api-example"
};
```

### Missing cache headers or directives

Responses must have [a cache control header](/build/caching/caching-overview#supported-cache-control-headers) with caching directives.

If you are not in control of the server or you don't want to change the response headers it returns, consider using the [`fetchWithCache`](#fetchwithcache) utility method to modify the response headers before the response is added to the Cache API.

### Unsupported `Netlify-Vary` directives

Responses must not use unsupported directives of the `Netlify-Vary` header.

Please refer to the [cache key variation documentation](/build/caching/caching-overview#cache-key-variation) for the full list of supported directives, and the values they accept.

### Unsupported `Cache-Control` directives

Responses must not set cache control headers with the `private`, `no-cache` or `no-store` directives, as these directives indicate that the response cannot be stored in a public cache without validating it with the origin server before each reuse.

Refer to the [`Cache-Control` directives documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control#directives) for more information on the different cache control directives.

Consider removing these directives from your response. If you are not in control of the server or you don't want to change the response headers it returns, consider using the [`fetchWithCache`](#fetchwithcache) utility method to modify the response headers before the response is added to the Cache API.

### Invalid maximum age

Responses must have a cache control header with a `max-age` or `s-maxage` directive of at least 1 second.

Consider updating the cache control headers to include this directive with a supported value. If you are not in control of the server or you don't want to change the response headers it returns, consider using the [`fetchWithCache`](#fetchwithcache) utility method to modify the response headers before the response is added to the Cache API.

### Missing status code

Responses must specify a status code. Please ensure you're passing a valid [`Response` object](https://developer.mozilla.org/en-US/docs/Web/API/Response) to the Cache API.

### Invalid status code

Responses must have a status code between 200 and 299.

Consider checking the status of the response before storing it with the Cache API.

```ts
const response = await fetch("https://example.com");

if (response.ok) {
  await cache.put(request, response);
}
```

### Internal error

There was an internal error that prevented your Cache API operation to be completed.

Please use [our support page](https://www.netlify.com/support/) to report your problem.
