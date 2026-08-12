---
title: "Next.js Middleware on Netlify (Legacy v4)"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/middleware.md
path: build/frameworks/framework-setup-guides/nextjs/legacy-runtime/middleware
---

---
title: "Next.js Middleware on Netlify"
description: "Learn about Next.js advanced middleware and add it to your Next.js 10-13.4 application to enhance access to requests and responses."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

> **Note - Legacy Next.js Runtime:** The information on this page applies to Next.js version 10-13.4 and Netlify Next.js Runtime v4, which is currently in maintenance support.

[Visit our Next.js adapter docs](/build/frameworks/framework-setup-guides/nextjs/overview/) for info on newer versions of Next.js.

Netlify has expanded on Next.js Middleware to give you more options during development. With `@netlify/next`, you get access to enhanced request and response features through an intuitive API.

Netlify's Next.js Advanced Middleware, available in the [`@netlify/next` library](https://www.npmjs.com/package/@netlify/next), gives improved access to requests and responses. This is similar to Netlify Edge Functions, but with some additional Next.js-specific helpers. `@netlify/next` is separate from [Next.js Runtime](/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/overview/#next-js-runtime-v4) and you need to [install it](#install-netlify-next) in your project to use it.

## Next.js Middleware

Next.js 12 introduced Middleware and enabled changing headers, rewriting the request path, or returning a different response entirely. Netlify fully supports Next.js Middleware and runs it either in an Edge Function or at the origin. Edge Functions are highly recommended for Next.js 12.2 or later, as ISR will not work with earlier versions.

### Deploy Next.js Middleware on Netlify

Next.js Middleware works out of the box with Netlify, and most functions will work unchanged. Visit [the Middleware docs](https://nextjs.org/docs/middleware) for details of how to create Middleware functions.

### Netlify Edge Functions and Middleware

By default, Next.js Middleware on Netlify uses [Edge Functions](/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/overview/#edge-functions) to connect the Netlify platform and workflow with an open runtime standard at the network edge. If you don't want to use Edge Functions for your Middleware, you can [opt out](#opt-out-of-netlify-edge-functions).

Note that the `@netlify/next` library that enables Next.js Advanced Middleware on Netlify requires Edge Functions and is subject to the [limitations](/build/edge-functions/limits/) of Edge Functions.

#### Opt out of Netlify Edge Functions

If you opt out of using Netlify Edge Functions for Middleware, regular serverless functions will handle your requests and responses.

Opting out of Edge Functions exposes you to the limitations of regular serverless functions:

- You can't use Netlify's Next.js Advanced Middleware library `@netlify/next`.
- Regular Netlify Functions don't have access to `request.geo`.
- When the Middleware runs at the origin, it is run _after_ [Netlify rewrites and redirects](/manage/routing/redirects/overview). If a static file is served by the Netlify CDN, then the Middleware is never run, as Middleware only runs when a page is served by Next.js. This means that any pages that match Middleware routes are served from the origin rather than the CDN.

To opt out, [create an environment variable](/build/environment-variables/get-started/#create-environment-variables) named `NEXT_DISABLE_NETLIFY_EDGE` and set it to `true`. If you have the option to set specific [scopes](/build/environment-variables/overview/#scopes) for your environment variables, the scope must include **Builds** to be available during the build process.

## Next.js Advanced Middleware with the `@netlify/next` library

Regular Next.js Middleware doesn't provide access to the actual response. Instead, it allows you to return a `NextResponse` object, which is used by the handler to modify the response headers when they are eventually returned.

Calling `NextResponse.next()` doesn't actually send a request to the origin. It's a placeholder for setting response headers that are applied later. It also doesn't let you modify the request, but instead can return a `rewrite()`. The wrapper uses the returned `rewrite()` to modify the request.

To provide improved access to requests and responses, Netlify created a [library called `@netlify/next`](https://www.npmjs.com/package/@netlify/next). This library works with requests and responses in much the same way that [Netlify Edge Functions](/build/edge-functions/overview/) do, but with some additional Next.js-specific helpers.

### Warning

**`@netlify/next` requires Edge Functions**

`@netlify/next` requires Netlify's [Edge Functions](/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/overview/#edge-functions) and is subject to the [limitations](/build/edge-functions/limits/) of Edge Functions. If you [opt out of Edge Functions](#opt-out-of-netlify-edge-functions), then you can't use `@netlify/next`.

Improved access to requests and responses enables excellent features, and `@netlify/next` has several ready to go:
- HTML rewrites
- Page data transforms
- Request headers
- Access to response body

### HTML rewrites

This feature enables rewriting the HTML of Next.js pages. It includes a simple `replaceText` function but also support for more powerful transforms using the [HTMLRewriter](https://github.com/worker-tools/html-rewriter) stream transformer. This enables personalization of pages at the edge, with no need for SSR. It works with ISR and static pages too.

### Page data transforms

Next.js passes `getStaticProps` and `getServerSideProps` data to a page component and transfers it either as a JSON data file (for internal navigation with `next/link`) or embedded in the page's  HTML in a script tag for server-rendered pages. 

This feature allows users to modify those props on the fly, in a similar way to the HTML rewrites. This means you can be sure that the hydrated page matches the SSR HTML, avoiding hydration errors. It works with both the data in HTML pages and JSON data requests.

### Request headers

Next.js Middleware allows response headers to be modified. This extends that ability to request headers that are sent to the origin. This is particularly helpful for rewrites to external sites. For example, it allows authentication headers to be added to proxied requests, allowing you to proxy a single page from a password-protected site without sharing credentials with the user.

### Access to response body

The other features make it easier to modify responses. But if you need more powerful changes, you can also get full read and write access to the response body as a stream.

## Install `@netlify/next`

`@netlify/next` is not part of the default Next.js Runtime, so you need to install this library in your project. To do so, enter the following in a terminal at the root of your project.

``` bash
npm install @netlify/next
```

## `@netlify/next` API

You can use `@netlify/next` in your Next.js projects through its API, which includes the `MiddlewareRequest` and `MiddlewareResponse` endpoints.

## `MiddlewareRequest` object

The `MiddlewareRequest` object is a more powerful version of the standard `NextRequest` object. You create it by passing `NextRequest` to the constructor:

```typescript

export async function middleware(nextRequest: NextRequest) {
  const request = new MiddlewareRequest(nextRequest);
  // ...
}
```

You can then make changes to the request, such as adding or modifying headers. Or, you can use it to get a `MiddlewareResponse` object that you can then process.

`MiddlewareRequest` has several useful methods you can use to handle your requests.

### `next()` method

Passes the request on to the origin and returns the response.

### `rewrite()` method

Rewrites the request URL and passes it on to the origin. Can be either an internal or external URL.

### `headers` object

A normal request `headers` object, except it is mutable and any changes are used when the request is sent to the origin.

## `MiddlewareResponse` object

This object is returned by `middlewareRequest.next()` or `middlewareRequest.rewrite()` and gives access to the full response. This may either be a static HTML file or SSR HTML.

The following object and methods in this section can help you transform the response. You can change the response headers similarly to a regular `NextResponse`. However, you can also _read_ the response headers coming from the origin.

### `originResponse` object

The [`Response` object](https://developer.mozilla.org/en-US/docs/Web/API/Response/Response) returned from the origin. You should not normally need to access this directly, but should instead use the helper methods below.

### `setPageProp()` method

Sets the value of a single page prop.

#### Syntax

``` typescript
setPageProp(key: string, value: any);
```

##### Parameters

- `key: string`
- `value: any`. While this parameter's type is `any`, you should follow the [guidance for `props`](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#props) in the Next.js documentation.

#### Example

```typescript
  const request = new MiddlewareRequest(req);
  const response = await request.next();
  const message = `This was static but has been transformed in ${request.geo.city}`;

  response.setPageProp("message", message);
```

### `replaceText()` method

Replaces the text content of an element. It can either take a string or a function that is passed the current value and returns the new value. This should be text that was generated from props, and you should use `setPageProp` to change the prop as well.

#### Syntax

``` typescript
replaceText(selector: string, valueOrReplacer: string | ((input: string) => string));
```

##### Parameters

- `selector: string`
- `valueOrReplacer: string | ((input: string) => string))`

#### Example

```typescript
  const request = new MiddlewareRequest(req);
  const response = await request.next();
  const message = `This was static but has been transformed in ${request.geo.city}`;

  response.replaceText("#message", message);
```

### `transformData()` method

Modifies the returned page data. This is like `setPageProp` except you can change the whole page data object.

#### Syntax

``` typescript
transformData(transform: (props: any) => any);
```

##### Parameters

- `transform: (props: any) => any`

#### Example

```typescript
  const request = new MiddlewareRequest(req);
  const response = await request.next();
  const message = `This was static but has been transformed in ${request.geo?.city}`;

  // Transform the response page data
  response.transformData((data) => {
    data.pageProps.message = message;
    data.pageProps.showAd = true;
    return data;
  })
```

### `rewriteHTML()` method

Allows the returned HTML to be written using [HTMLRewriter](https://github.com/worker-tools/html-rewriter).

#### Syntax

``` typescript
rewriteHTML(selector: string, handlers: ElementHandlers);
```

##### Parameters

- `selector: string`
- `handlers: ElementHandlers`

#### Example

```typescript
  const request = new MiddlewareRequest(req);
  const res = await request.next();
  const message = `This was static but has been transformed in ${request.geo?.city}`;

  // Transform the response HTML
  res.rewriteHTML("p[id=message]", {
    text(textChunk) {
      if (textChunk.lastInTextNode) {
        textChunk.replace(message);
      } else {
        textChunk.remove();
      }
    },
  });
```

### Response caveats

Modifying the response can cause React hydration errors if the hydrated page content doesn't match the HTML returned from the server. There are two ways around this. 

Ideally, you can change both the text content and the prop. That would mean the value will still match.

If that's not possible (for example, if the displayed HTML is too complex to generate), then you can use two-pass rendering for the element. This is when you don't render the element in SSR, but instead update the state in `useEffect` and then display it at that point. The logic for this can be encapsulated in a custom hook.

For example:

```typescript

const useHydrated = () => {
  const [hydrated, setHydrated] = React.useState(false);
  React.useEffect(() => {
    setHydrated(true)
  }, []);

  return hydrated;
}

const Page = ({ message, showAd }) => {
  const hydrated = useHydrated();

  return (
    <div>
      {hydrated && showAd ? (
        <div>
          <p>This is an ad that isn't shown by default</p>
          <img src="http://placekitten.com/400/300" />
        </div>
      ) : (
        <p>No ads for me</p>
      )}
    </div>
  );
}

export async function getStaticProps() {
  return {
    props: {
      showAd: false,
    },
  }
}

export default Page;

```

## Modify request headers

Headers on the `MiddlewareRequest` object can be added or modified, and the changed headers will then be passed along to the origin if you call `middlewareRequest.next()` or `middlewareRequest.rewrite()`. 

You can also modify headers on the original `NextRequest` object, and they will be passed along in the same way. This can be used for many things. For example, to add authentication headers to an externally proxied request or attach a bucket name header for A/B testing.

```typescript
const { pathname } = req.nextUrl;
const request = new MiddlewareRequest(req);

if (pathname.startsWith("/api/hello")) {
  // Add a header to the request
  request.headers.set("x-hello", "world");

  return request.next();
}

if (pathname.startsWith("/headers")) {
  // Add a header to the rewritten request
  request.headers.set("x-hello", "world");
  
  return request.rewrite("/api/hello");
}
```

