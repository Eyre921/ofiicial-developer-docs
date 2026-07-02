---
title: "Caching overview"
source: https://docs.netlify.com/build/caching/caching-overview.md
path: build/caching/caching-overview
---

---
title: "Caching overview"
description: "Customize cache key variations and set Cache-Control headers to control the granularity and freshness of your cache. Purge the cache by site or cache tag."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Netlify's global caching infrastructure is built to provide stellar performance without any stale pages or broken assets for your visitors.

## Default caching behavior

Static asset responses on Netlify are cached on Netlify's global edge nodes and [automatically invalidated](#automatic-invalidation-with-atomic-deploys) whenever a deploy changes the content. Static asset responses can only change with new deploys. So, unless there is a new deploy or [manual purge](#on-demand-invalidation), we treat static asset responses as fresh for up to one year and ignore any attempts to set cache control headers with a shorter `max-age`.

However, responses coming from [Netlify Functions](/build/functions/overview), [Edge Functions](/build/edge-functions/overview), and [proxies](/manage/routing/redirects/rewrites-proxies) are not cached by default. Because these responses are dynamic, they may change without a new deploy and we don't want to risk serving stale content. If you would like to cache responses from functions, edge functions, or proxies, you can [add cache control headers](#supported-cache-control-headers) to customize the caching.

When cached, different types of responses have different default cache key considerations that determine whether a request reuses an existing cache object or creates a new one.
- values for header names sent with the [standard `Vary` HTTP response header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary) are factored into cache keys for all response types
- query parameters are additionally factored into cache keys by default for the following:
  - responses from [serverless functions](/build/functions/overview) except for [On-demand Builders](/build/configure-builds/on-demand-builders)
  - responses from [edge functions](/build/edge-functions/overview) when [opting into manual caching](/build/edge-functions/optional-configuration#configure-an-edge-function-for-caching)
  - static assets served from a [redirect with a query parameter condition](/manage/routing/redirects/redirect-options#query-parameters)

This default cache key behavior optimizes the cache hit rate for the majority of use cases. You can customize the behavior with [cache key variations](#cache-key-variation) that take different aspects of a request into account.

### Caution - Not compatible with basic-auth

Using basic-auth on any page of your website disables caching for the entire website.

## Cache key variation

Cache keys determine whether a request reuses an existing cache object or creates a new one. Our defaults for creating cache keys optimize the cache hit rate for the majority of use cases. However, your particular use case may have opportunities for further improvement. 

For example, if your site uses an edge function to [localize content](https://edge-functions-examples.netlify.app/example/localized-content) based on user location, you may want to cache responses based on location to balance the cache hit rate with accurate localization. Or, if your site uses a serverless function where the response depends on only one query parameter, you may want to cache responses based on just that one query parameter and ignore the others to increase the cache hit rate.

You can customize how cache key variations are created for your responses by [setting the `Netlify-Vary` response header](#more-resources). This gives you fine-grained control over which parts of a request are taken into consideration for matching cache objects. The `Netlify-Vary` header takes a set of comma-delimited instructions for what parts of the request to vary cache keys on. Possible instructions are as follows:

- **[`query`](#vary-by-query-parameter):** vary by the value of some or all request URL query parameters
- **[`header`](#vary-by-header):** vary by the value of one or more request headers
- **[`language`](#vary-by-language):** vary by the languages from the `Accept-Language` request header
- **[`country`](#vary-by-country):** vary by the country inferred from a GeoIP lookup on the request IP address
- **[`cookie`](#vary-by-cookie):** vary by the value of one or more request cookie keys

### Tip - On-demand Builders don't support cache key variation

On-demand Builders don't support the `Netlify-Vary` header. They use the request's URL path to determine whether to create a new cache object or reuse an existing one. This approach can't be customized.

Different cache objects are created for different matches to the instructions. A single additional cache object is created for all non-matches. For example, consider a response with `Netlify-Vary: query=style|season`.
- All of the following matches are cached under different cache keys:
   - `/shirts?style=casual&season=summer`
   - `/shirts?style=casual&season=winter`
   - `/shirts?style=casual`
- Meanwhile, all of the following non-matches are cached under the same cache key. Requests to these and any other non-matches return the same response:
   - `/shirts`
   - `/shirts?price=low`
   - `/shirts?price=sale&delivery=true`

### Caution

Use the same <code>Netlify-Vary</code> header for all responses from a URL</span>">
Any given URL should return the same `Netlify-Vary` header across all responses. If different resources for the same URL return different `Netlify-Vary` settings, the instructions for the first resource cached for that URL are used and the subsequent instructions are ignored.

If a response includes both the `Netlify-Vary` and `Vary` headers, we respect both when creating cache keys and returning cached responses. In general, you should use `Netlify-Vary` for your custom business logic and `Vary` for content format and encoding negotiation. If you use a service like Cloudflare in front of Netlify, you should use the standard `Vary` header to pass any desired instructions to Cloudflare since `Netlify-Vary` is a Netlify-specific feature for increased customization of cache keys on Netlify.

### Vary by query parameter

You can create cache key variations based on  a specific subset of query parameters included with a request or all request query parameters. The former is helpful when some query parameters do not affect the response or are unique for each request, such as analytics tracking parameters. The latter is helpful when all query parameters affect the response, such as query parameters that display variations of a product listing.

- To create cache key variations for a subset of query parameters, specify one or more keys in a pipe-delimited list. For example:

   ```
   Netlify-Vary: query=item_id|page|per_page
   ```

- To create cache key variations for all query parameters, include the following response header:

   ```
   Netlify-Vary: query
   ```

The query parameter instruction is case-sensitive. However, the order in which parameters are specified on a given request does not affect how they are matched. For example, consider a `/shirts` path with a `Netlify-Vary: query` header to vary on all query parameters. A response for `/shirts?color=red&size=large` is cached under the same key as `/shirts?size=large&color=red` but a different key than `/shirts?Color=Red&Size=Large`.

### Vary by header

You can create cache key variations based on your custom request headers and most [standard request headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Standard_request_fields). This is helpful for custom business logic like caching different responses based on which version of your app a visitor uses. 

### Collapsible Component:

**Standard request header limitations**

The following standard request headers can not be used with `Netlify-Vary` because they either have high cardinality that risks degraded performance or are the basis of other caching features on Netlify.

- `Accept`
- `Accept-Charset`
- `Accept-Datetime`
- `Accept-Encoding`
- `Accept-Language` - use `Vary: Accept-Language` or `Netlify-Vary` with a list of specific languages instead.
- `Cache-Control`
- `Connection`
- `Content-Length`
- `Cookie` - use `Vary: Cookie` or `Netlify-Vary` with a list of specific cookie keys instead.
- `Host`
- `If-Match`
- `If-Modified-Since`
- `If-None-Match`
- `If-Unmodified-Since`
- `Range`
- `Referer`
- `Upgrade`
- `User-Agent`

---

To create cache key variations based on request headers, specify one or more headers in a pipe-delimited list. For example:

```
Netlify-Vary: header=Device-Type|App-Version
```

### Vary by language

You can create cache key variations for one or more individual languages or custom language groups. These are checked against the `Accept-Language` header from the request using [standard browser language identification codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). This can be helpful for caching localized content.

- To create cache key variations based on one or more individual languages, use a pipe-delimited list. For example:

   ```
   Netlify-Vary: language=en|de
   ```

- To group multiple languages together, use `+`. For example:

   ```
   Netlify-Vary: language=en|es+pt|da+nl+de
   ```

The language instruction respects the quality parameter from the `Accept-Language` header. This means, for example, that a request with `Accept-Language: fr-CH, fr;q=0.9, en;q=0.7, de;q=0.8, *;q=0.5` and a response with `Netlify-Vary: language=de+nl|en` use a cache object under the `de+nl` variation.

### Tip

Use the standard <code>Vary</code> header to vary on all languages</span>">
To create cache key variations for all possible individual languages, you can use `Vary: Accept-Language` rather than listing all the options in a `Netlify-Vary: language` instruction.

### Vary by country

You can create cache key variations based on the geographical origin of the request. You can specify individual countries or custom country groups. These are checked against a GeoIP lookup of the request IP address using [ISO 3166-1 two-letter codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). This can be helpful for caching content about products whose availability varies by region. 

- To create cache key variations based on one or more individual countries, use a pipe-delimited list. For example:

   ```
   Netlify-Vary: country=es|de
   ```

- To group multiple countries together, use `+`. For example:

   ```
   Netlify-Vary: country=us|es+pt|dk+nl+de
   ```

### Vary by cookie
    
You can create cache key variations based on a subset of cookie keys. This is helpful for things like cookie-based A/B testing. It's typically bad for cache hit rate to create variations based on the entirety of the `Cookie` header value as this may include authentication details that vary for each user. So, you should instead target specific cookie keys to vary on.

To create cache key variations based on one or more cookie keys, use a pipe-delimited list. For example:

```
Netlify-Vary: cookie=ab_test|is_logged_in
```

The cookie instruction is case-sensitive. However, the order that cookie keys are specified on a given response does not affect how they are matched. For example, consider a path with a `Netlify-Vary: cookie=ab_test|is_logged_in` header. A response with `Cookie: ab_test=new; is_logged_in=no` is cached under the same key as `Cookie: is_logged_in=no; ab_test=new` but a different key than `Cookie: AB_test=New; is_logged_in=NO`.

### Combine variations

You can use any combination of the above instructions to vary your cached content.

To combine multiple instructions, separate them with a comma. For example:

```
Netlify-Vary: query,country=es+de|us
```

This tells Netlify to take both the entire query into account for cached objects, as well as the request's country of origin.

## Supported cache control headers

Netlify supports the [standard caching directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) with the following cache control headers:

- **`Netlify-CDN-Cache-Control`:** targeted field that applies to only Netlify's CDN
- **`CDN-Cache-Control`:** targeted field that applies to all CDNs that support it
- **`Cache-Control`:** general field that can apply to any CDN or a visitor's browser

### Tip - On-demand Builders use time to live

On-demand Builders don't support these cache control headers. They instead support an optional [time to live (TTL)](/build/configure-builds/on-demand-builders#time-to-live-ttl) pattern that allows you to set a fixed duration of time after which a cached builder response is invalidated.

The following directives affect response caching as described below.

- `public`: cache the response.
- `private`: Netlify's cache is a shared cache, so using `private` means we don't cache the response in our network and can't reuse it for multiple clients. However, the response will be cached in the local cache for each client.
- `no-store`: do not cache the response.
- `s-maxage`: store and reuse the cached response in Netlify's shared cache for this many seconds.
- `max-age`: store and reuse the cached response in any cache for this many seconds. If `s-maxage` is also set, Netlify's shared cache will use `s-maxage` instead.
- [`stale-while-revalidate`](#stale-while-revalidate-directive): keep serving a stale object out of the cache for this many seconds while the object is revalidated in the background.
- [`durable`](#durable-directive): for serverless functions only. Use to reduce function invocations and response latency. When a response is generated and cached for one edge node, store the response in Netlify's durable cache so that other edge nodes can reuse it instead of invoking the function again. 

### Stale while revalidate directive

Stale while revalidate is a caching pattern that allows the cache to keep serving a stale object out of the cache while the object is revalidated in the background. This can be impactful for implementing API caching or patterns like incremental static regeneration (ISR).

As an example use case, imagine you have a slow API endpoint that takes 5 seconds to respond. You can wrap it in a function that adds the following cache header:

```
Netlify-CDN-Cache-Control: public, max-age=60, stale-while-revalidate=120
```

Here's what this header does:

- `public` instructs Netlify's edge to cache the first response.
- `max-age=60` instructs the cache to continue serving the cached response for 60 seconds after the initial request. After 60 seconds, the cache is considered stale.
- `stale-while-revalidate=120` instructs the cache how long it can serve stale content. If a request arrives within this specified duration after the content expired, the stale content is served while the cache revalidates the content in the background.

If there's a steady stream of requests, visitors will get recently refreshed results from the API without having to wait 5 seconds for the API response.

Here's a timeline to illustrate how this works:

1. An initial request generates a response that gets cached (consider this to be t = 0).
2. A new request is made 30 seconds later (t = 30). The cache is still fresh, so the edge serves the cached response.
3. Another request is made 100 seconds later (t = 130). The cache is now stale, but the time is within the 120 _additional_ seconds allotted to serve stale content. So, the edge serves the stale cached response while the cache revalidates the content in the background. Time is reset (t = 0) when the revalidated response is cached.
4. Another new request is made 4 minutes later (t = 240). The cache is stale again and the time is outside the allotment for serving stale content (which ended at t = 60 + 120 = 180). The edge waits for a new response to be generated before serving and caching it. Time is reset (t = 0) when the new response is cached.

### Durable directive

By default, when a site visitor makes a request to Netlify for content that is generated by a function, the specific edge node the visitor connects to checks its own local cache. If fresh content is not found in that node's cache, the node invokes the function to generate a new response. This means the function is typically invoked multiple times for the same content.

When you use the `durable` directive for a function's response, that response is not only returned to the edge node that invoked the function but also stored in a shared cache called the _durable cache_. Whenever that content is requested, edge nodes that don't have the response locally cached check the durable cache, and only invoke the function if the response is not found there.

![](/images/caching-durable.png)

You can expect the following benefits when you add the `durable` directive to your serverless functions: 
- **Better response times and more reliable performance for edge cache misses.** Without the durable cache, an edge cache miss for a serverless function always leads to a function invocation. Function invocations have variable performance and increased latency because of factors like warm vs. cold starts, the time it takes the function logic to run, and calls to third-party APIs that have their own latency profile. With the `durable` directive, many of these edge cache misses are backed by a response stored in the durable cache, so an additional function invocation isn't required. This can also mitigate issues related to high-volume function usage with third-party providers, such as rate-limiting.
- **Fewer function invocations, which can lead to a reduced bill.** The durable cache allows edge nodes to share a cached response, so edge nodes don't have to invoke the function individually when they don't already have a cached response. This reduces the number of function invocations, typically by a significant amount, and decreased usage can mean decreased costs. This can also mitigate issues with third-party providers that can occur with a high volume of function usage, such as third-party API quotas being exhausted. Note that while we aim to minimize function invocations, we do not guarantee that there's always only a single function call for each version of a generated page. Multiple requests across different regions in a short time frame might invoke a function multiple times because the cache is eventually consistent. 
 
Here's an example of a serverless function using the `durable` directive:

```ts
import type { Context } from "@netlify/functions";

export default async (req: Request, context: Context) => {
  return new Response("Hello world", {
		headers: {
			'Netlify-CDN-Cache-Control': 'public, durable, max-age=60, stale-while-revalidate=120'
		}
	});
}
```

The durable cache is compatible with all other fine-grained cache controls including cache key variations, stale while revalidate, and on-demand invalidation. This means if you're already using the edge cache to cache function responses, adding the durable cache requires minimal code changes. Using the durable cache doesn't add significant latency to function invocations. This is because we automatically co-locate the durable cache for a site with the site's [functions region](/build/functions/configuration/?fn-language=ts#region) to minimize cross-region hops for a request.

### Caution - Not yet supported on Edge Function responses

The durable cache is currently only compatible with Netlify Function responses.
The `durable` directive has no effect on responses from Netlify Edge Functions.
If you would like to see this feature added, please [tell us more about your use
case](https://www.netlify.com/support/).

### Framework support

Your ability to control caching headers varies by web framework. 

Some web frameworks give developers full control of caching headers. For example, check out our developer guides on how to use our caching primitives with the following frameworks:
- [Astro](https://developers.netlify.com/guides/how-to-do-advanced-caching-and-isr-with-astro/)
- [Remix](https://developers.netlify.com/guides/how-to-do-isr-and-advanced-caching-with-remix/)

However, other frameworks control some or all caching headers on behalf of developers. Note the following framework-specific limitations:

- Next.js
  - On Netlify, cacheable responses on sites using the Next Runtime 5.5.0 or later automatically use
    the durable cache
  - You can override this behavior in your [next config
    file](https://nextjs.org/docs/app/api-reference/next-config-js/headers#cache-control), but note
    that Next.js did not support this before 14.2.10.
- [Nuxt](/build/frameworks/framework-setup-guides/nuxt) v3 apps using the default `netlify` Nitro preset can't set cache control headers on ISR routes.

### Note - Automatic durable cache for Nuxt and more coming soon

We are working on updating our framework support for Nuxt (and other frameworks powered by Nitro,
  such as Analog, SolidStart, and TanStack Start) to automatically use the durable cache.

### Default values

If you don't specify any of the supported cache control headers, we use the following default values.

For static assets:

```
Netlify-CDN-Cache-Control: public, s-maxage=31536000, must-revalidate
Cache-Control: public, max-age=0, must-revalidate
```

For dynamic responses:

```
Cache-Control: public, max-age=0, must-revalidate
```

### Header precedence

If you specify more than one of the supported headers, Netlify will respect the most specific one. Netlify always passes `CDN-Cache-Control` and `Cache-Control` downstream so that other caches can use them. Here are some examples:

- Response includes both `Netlify-CDN-Cache-Control` and `CDN-Cache-Control`
  - Netlify uses the settings from `Netlify-CDN-Cache-Control`
  - `CDN-Cache-Control` will be passed downstream for other caches to use
- Response includes both `CDN-Cache-Control` and `Cache-Control`
  - Netlify uses the settings from `CDN-Cache-Control`
  - Both `CDN-Cache-Control` and `Cache-Control` are passed downstream for other caches to use

## Automatic invalidation with atomic deploys

To support [atomic deploys](/deploy/deploy-overview), all new deploys invalidate the cache for the given [deploy context](/deploy/deploy-overview#deploy-contexts) by default. For example, a new deploy of a Deploy Preview will invalidate the cache for that specific Deploy Preview number while all other Deploy Previews for the site will remain cached as is. This automation means that a cached asset may be invalidated despite the cache control headers indicating that the asset should still be considered fresh. This override guarantees that we never accidentally serve stale content.

Automatic invalidation relies on an internal cache ID that we apply automatically to all objects on our CDN. The ID indicates both the site and the deploy context that an object belongs to.

### Opt out of automatic invalidation

If you want some of your cached responses from functions or proxies to persist across atomic deploys, you can opt them out of automatic invalidation.

As an example use case, imagine a site that proxies to a CMS server that has a weekly release cycle. Any site deploy in between the weekly CMS releases invalidates the whole cache for that deploy context causing Netlify to revalidate all objects. This includes assets cached from the CMS even though they haven't changed. This can affect performance, increase bandwidth spend, and put unnecessary strain on the CMS server. In this scenario, you can opt out of automatic invalidation for responses proxied from the CMS server to avoid these issues.

To opt an object out of automatic cache invalidation, set the `Netlify-Cache-ID` response header with one or more custom cache IDs. To set multiple IDs, use a comma-separated list.

### Tabs Component:

<TabItem label="One ID">

```
Netlify-Cache-ID: cms-proxy
```

</TabItem>

<TabItem label="Multiple IDs">

```
Netlify-Cache-ID: cms-proxy,product,image
```

</TabItem>

The custom cache ID overrides the internal cache ID making it so that automatic invalidation with atomic deploys does not apply to the object. However, any `Cache-Control` directives for an object are still respected so you can control how long the object stays cached.

To support granular [on-demand invalidation](#on-demand-invalidation) of cached objects that are opted out of automatic invalidation, your custom `Netlify-Cache-ID` values are automatically registered as cache tags that you can use to purge the object by tag.

Keep the following in mind when setting `Netlify-Cache-ID`

- cache IDs are case insensitive
- cache ID response headers must contain only UTF-8 encoded characters
- a single cache ID can be up to 1024 characters long
- a single response can have up to 500 cache IDs

#### Best practices

After you've opted out of automatic invalidation, some site updates might not propagate as you expect them to. This is more common when your `Cache-Control` configuration keeps assets fresh for a long time. If this happens, we recommend that you use [on-demand invalidation](#on-demand-invalidation) to purge the cache so that you don't have to wait for revalidation based on the `Cache-Control` directives to take effect. After a manual purge, your changes should propagate fully across our CDN as requests are made to your site.  

Here are some scenarios where it's a best practice to manually purge the cache after making changes:
- Changing a redirect rule that configures a proxy to a page with a `Netlify-Cache-ID` header. The update might not propagate to all routes, since the proxied content stays in the cache. 
- Changing a function that generated a response with a `Netlify-Cache-ID` header. The updated function won't run since the previously generated response stays in the cache.

If you have sensitive content, we recommend that you don't opt out of automatic invalidation for it. This is because we don't want to risk your sensitive content becoming more widely available than it should be. Take the following scenario for example:
- A site with sensitive content is using [Firewall Traffic Rules](/manage/security/secure-access-to-sites/traffic-rules).
- The sensitive content has been opted out of automatic invalidation.
- A new deploy is made that doesn't include the sensitive content. 
- Someone removes the Firewall Traffic Rules thinking the site doesn't need them anymore now that the project no longer contains sensitive content.
- However, the sensitive content remains cached. The cached content is publicly available to everyone until responses are revalidated based on `Cache-Control` directives which could potentially be long-lived.

## On-demand invalidation

If you want to invalidate cached objects while their cache control headers indicate they're still fresh, you can purge the cache by [site](/build/caching/caching-overview#purge-by-site) or [cache tag](/build/caching/caching-overview#purge-by-cache-tag). These granular options for refreshing your cache without redeploying your entire site optimize developer productivity for your team and site performance for your customers. On-demand invalidation across the entire network takes just a few seconds, even if you're purging a tag associated with thousands of cached objects.

You can use the following to invalidate cached objects:
- a [serverless function](/build/functions/get-started) with the `purgeCache` helper
- a direct call to the [`purge` API endpoint](https://open-api.netlify.com/#tag/purge) with a [personal access token](/api-and-cli-guides/api-guides/get-started-with-api#authentication)

You can use either to purge by site or by tag as demonstrated in the examples in the next sections. 

### Collapsible Component:

**Extra step for Lambda-compatible serverless functions**

To purge the cache from a [Lambda-compatible serverless function](/build/functions/lambda-compatibility), you must pass the `purge_api_token` value provided automatically by Netlify. This keeps your Lambda-compatible function secure.

```ts
// purge a cache tag passed by query parameter across all deploys of a site
// no need to specify site ID as it is passed automatically by the purgeCache helper 

import { purgeCache } from "@netlify/functions"

module.exports.handler = async (event, context) => {
  const token = context.clientContext.custom.purge_api_token;

  await purgeCache({
    tags: ["tag1", "tag2"],
    token
  })

  return {
    body: "Purged!",
    statusCode: 202
  }
}
```

---

### Purge by site

Purging by site invalidates all cached assets across all deploys for the site.

As an example use case, imagine a site that uses branch deploys for A/B testing, is backed by a content API, and needs to be automatically refreshed every hour with new content. Purging the cache by site is useful in this scenario because it keeps the content refresh in sync across all branch deploys.

##### Use a function with the `purgeCache` helper to purge by site

When you use a function with the `purgeCache` helper, the site ID is passed automatically so you don't need to specify the site.

``` ts 
// purge all objects across all deploys for this site

export default async () => {

  console.log("Purging everything");

  await purgeCache();

  return new Response("Purged!", { status: 202 })
};
```

##### Use a direct call to the `purge` API to purge by site

To purge by site with a direct API call, specify the site with one of the following
- **`site_id`:** for example, `3970e0fe-8564-4903-9a55-c5f8de49fb8b`
- **`site_slug`:** for example, `mysitename`

You can find these values for your site by visiting the Netlify UI at 
### NavigationPath Component:

Project configuration > General > Project details > Project information
 and checking the **Project ID** or **Project name** (Also known as Site ID in the Netlify API and formerly as Site ID and Site name in the Netlify UI.)

```sh
curl -X POST \ 
	-H "Content-Type: application/json"	\
	-H "Authorization: Bearer <personal_access_token>" \ 
	--data '{"site_id": "3970e0fe-8564-4903-9a55-c5f8de49fb8b"}' \
	'https://api.netlify.com/api/v1/purge'
```

### Purge by cache tag

Purging by cache tag invalidates specified cached assets. You can purge by tag across all deploys of a site or only within a specific deploy context.

As an example use case, imagine a high-traffic e-commerce site where products routinely sell out. You may want to purge promotions for products when they sell out so that customers aren't disappointed when they follow an old cached promotion link only to find that the product isn't currently available. Purging by cache tag is useful in this scenario because it can refresh assets related to the sold-out product without impacting performance for items that are still available. 

To purge by cache tag you must first [add cache tag response headers](#add-cache-tags). Then you can [invalidate tagged objects](#invalidate-tagged-objects).

Keep the following in mind when purging by cache tag
- cache tags are case insensitive
- cache tag response headers must contain only UTF-8 encoded characters
- a single tag can be up to 1024 characters long
- a single response can have up to 500 cache tags

#### Add cache tags

Netlify supports the following cache tag response headers
- **`Netlify-Cache-Tag`:** targeted field that applies to only Netlify's CDN
- **`Cache-Tag`:** general field that can apply to any CDN 

You can specify one or more cache tags for a response. For multiple tags, use a comma-separated list:

### Tabs Component:

<TabItem label="Cache-Tag">

```  
Cache-Tag: tag1,tag2,tag3
```

</TabItem>

<TabItem label="Netlify-Cache-Tag">

```  
Netlify-Cache-Tag: tag1,tag2,tag3
```

</TabItem>

Additionally, if you've [opted out of automatic invalidation](#opt-out-of-automatic-invalidation) for an object, any custom cache IDs you set with the `Netlify-Cache-ID` response header are registered as tags for that cached object. This prevents cached objects from getting stuck on our CDN with no way to purge them.

These 3 response headers work together in the following ways:

- If you specify both `Netlify-Cache-Tag` and `Cache-Tag`, Netlify uses the values from `Netlify-Cache-Tag`. Netlify always passes `Cache-Tag` values downstream so other caches can use them. 
- Setting `Netlify-Cache-Tag` to a value already set for `Netlify-Cache-ID` is redundant and has no extra effect on your site. If however you want to send your custom `Netlify-Cache-ID` tags downstream so other caches can use them, you must set `Cache-Tag` with the same values you've set for `Netlify-Cache-ID`.
- Tags automatically registered based on `Netlify-Cache-ID` values do not contribute to the limit of 500 cache tags per response. They have their own separate limit of 500 cache IDs per response.

Here are some examples:
- Response includes `Netlify-Cache-Tag: cms-proxy` and `Cache-Tag: cms-asset`:
   - Netlify tags the cached object with the value from `Netlify-Cache-Tag`.
   - You can purge the object from Netlify's cache using the `cms-proxy` tag.
   - Attempts to purge the `cms-asset` tag on Netlify's CDN do not affect the cached object.
   - `Cache-Tag: cms-asset` is passed downstream for other caches to use.
   - The cached object is automatically invalidated by new deploys.
- Response includes `Netlify-Cache-ID: product` and `Cache-Tag: image`:
   - Netlify tags the cached object with both `product` and `image`.
   - You can purge the object from Netlify's cache using either tag.
   - `Cache-Tag: image` is passed downstream for other caches to use. However, the `product` tag is not sent downstream.
   - The cached object persists after new deploys until its `Cache-Control` directives indicate it's stale or until you purge it manually.
- Response includes `Netlify-Cache-ID` with 500 values and `Cache-Tag` with 500 different values:
   - Netlify tags the cached object with the values from both headers.
   - You can purge the object from Netlify's cache with any of the 1000 different tags on the object. 

### Tip

Other providers may strip <code>Cache-Tag</code> before it reaches Netlify</span>">
Some providers remove `Cache-Tag` from their responses. If you are proxying to a provider that does this, you should use both `Netlify-Cache-Tag` and `Cache-Tag` so that your cache tags are applied to both Netlify and the proxy.

#### Invalidate tagged objects

As mentioned above, you can use either a function or a direct API call to invalidate cached objects by tag.

##### Use a function with the `purgeCache` helper to purge by cache tag

When you use a function with the `purgeCache` helper, the site ID is passed automatically so you don't need to specify the site.

By default, tag-based purges apply to all of the site's deploys. To target a specific deploy, specify one or more of the following
- **`deployAlias`** (optional)**:** for example, `deploy-preview-11`. On its own, targets the specified alias on the primary domain.
- **`domain`** (optional)**:** for example, `early-access.company.com`. On its own, targets the currently published production deploy on the specified domain. 

``` ts 
// purge a cache tag passed by query parameter
// applies to a specific Deploy Preview of a specific subdomain

export default async (req: Request) => {
  const url = new URL(req.url);
  const cacheTag = url.searchParams.get("tag");
  if (!cacheTag) {
    return;
  }
  const deployAlias = "deploy-preview-11";
  const domain = "early-access.company.com";

  console.log("Purging tag: ", cacheTag);

  await purgeCache({
    tags: [cacheTag],
    deployAlias,
    domain,
  });

  return new Response("Purged!", { status: 202 })
};
```

##### Use a direct call to the `purge` API to purge by cache tag

To purge by cache tag with a direct API call, specify the following
- **`cache_tags`:** for example `news` or `blog,sale`. If you don't specify a
list of `cache_tags`, the entire site will be purged. However, if you specify an empty
list of `cache_tags`, no purge will be applied.
- the site with either of the following:
   - **`site_id`:** for example, `3970e0fe-8564-4903-9a55-c5f8de49fb8b`
   - **`site_slug`:** for example, `mysitename`

   You can find these values for your site by visiting the Netlify UI at 
### NavigationPath Component:

Project configuration > General > Project details > Project information
 and checking the **Project ID** or **Project name** (Also known as Site ID in the Netlify API and formerly as Site ID and Site name in the Netlify UI).

By default, tag-based purges apply to all of the site's deploys. To target a specific deploy, specify one or more of the following
- **`deploy_alias`** (optional)**:** for example, `deploy-preview-11`. On its own, targets the specified alias on the primary domain.
- **`domain`** (optional)**:** for example, `early-access.company.com`. On its own, targets the currently published production deploy on the specified domain. 

``` bash 
# applies to a specific Deploy Preview of a specific subdomain

curl -X POST \ 
	-H "Content-Type: application/json"	\
	-H "Authorization: Bearer <personal_access_token>" \ 
	--data '{"site_slug": "mysitename", "cache_tags": ["news"], "deploy_alias": "deploy-preview-11", "domain": "early-access.company.com"}' \
	'https://api.netlify.com/api/v1/purge'
```

Each cache tag or site can only be purged twice every 5 seconds. If you exceed
this rate limit, you will receive a `429` response code.

## Debug with `Cache-Status`

Netlify sets a `Cache-Status` header on all responses. This header contains information about how different cache layers handled each response and follows [RFC 9211](https://httpwg.org/specs/rfc9211.html).

The `Cache-Status` header is useful for troubleshooting and monitoring. For example, you can use it for the following:

- checking if you received a cached response
- finding out why you received an uncached response
- differentiating cached and uncached responses when measuring performance

To troubleshoot, examine the `Cache-Status` header on your responses and check how our network handled a request.

If you use a frontend monitoring tool to collect performance metrics, we recommend that you record this header so that you can differentiate cached and uncached responses when analyzing your site's performance.

### Example `Cache-Status` values

Here are some examples of common response patterns: 

- **No response found in the cache:**<br />
   `Cache-Status: "Netlify Edge"; fwd=miss`
- **Cached response found and served:**<br />
   `Cache-Status: "Netlify Edge"; hit`
- **Outdated response found and not served:**<br />
   `Cache-Status: "Netlify Edge"; fwd=stale`
- **Outdated response found and served while we refresh in the background because the [stale while revalidate](#stale-while-revalidate-directive) directive was used:**<br />
   `Cache-Status: "Netlify Edge"; hit; fwd=stale`

For serverless functions with the [`durable` directive](#durable-directive), some common response patterns include a `Cache-Status` from the durable cache.

- **No response found in the edge cache or durable cache for requested URI:**<br />
   `Cache-Status: "Netlify Edge"; fwd=miss`<br /> 
   `Cache-Status: "Netlify Durable"; fwd=uri-miss; stored=true; ttl=3600`
- **No response found in the edge cache or durable cache for requested
variation (either due to Vary or Netlify-Vary mismatch):**<br />
   `Cache-Status: "Netlify Edge"; fwd=miss`<br /> 
   `Cache-Status: "Netlify Durable"; fwd=vary-miss; ttl=3600; stored=true`
- **No response found in the edge cache; cached response found in the durable cache and served:**<br />
   `Cache-Status: "Netlify Edge"; fwd=miss`<br />
   `Cache-Status: "Netlify Durable"; hit; ttl=1234`
- **Outdated response found in the edge cache and not served; fresh response found in the durable cache and served:**<br />
   `Cache-Status: "Netlify Edge"; fwd=stale`<br />
   `Cache-Status: "Netlify Durable"; hit; ttl=1234` 
- **No response found in the edge cache; outdated response found in the durable cache and not served:**<br />
   `Cache-Status: "Netlify Edge"; fwd=miss`<br />
   `Cache-Status: "Netlify Durable"; fwd=stale; stored=false; ttl=-600`
- **No response found in the edge cache; outdated response found in the durable cache and served while we refresh in the background because the [stale while revalidate](#stale-while-revalidate-directive) directive was used:**<br />
   `Cache-Status: "Netlify Edge"; fwd=miss`<br />
   `Cache-Status: "Netlify Durable"; hit; ttl=-600; stored=true`

### Troubleshooting tips

- A response might have multiple `Cache-Status` headers if multiple caches were involved in serving the response. For information about Netlify cache behavior, find values that start with `"Netlify Edge"` or `"Netlify Durable"`.
- Each request you make could land on a different instance of the cache that has different content stored. If your site does not receive production traffic that warms the cache and you're not using the [`durable` directive](#durable-directive) for serverless functions, you will likely land on multiple caches that don't have a cached response before getting a cache hit. Try making multiple requests when debugging caching issues to ensure you make repeat requests to the same instance of the cache.

## More resources

Refer to the following resources for how to set caching headers for different types of responses

- **[Get started with functions](/build/functions/get-started):** include caching headers in a function's response object.
- **[Optional configuration for edge functions](/build/edge-functions/optional-configuration#response-caching):** opt in to caching and customize cache behavior for an edge function.
- **[Netlify Image CDN](/build/image-cdn/overview#custom-headers):** set headers on source images to control caching for Netlify Image CDN.
- **[Custom headers](/manage/routing/headers):** set caching headers that are sent downstream for static assets.
