---
title: "Edge Function Declarations"
source: https://docs.netlify.com/build/edge-functions/declarations.md
path: build/edge-functions/declarations
---

---
title: "Edge Functions declarations"
description: "Create declarations to configure edge functions to run on specific URL patterns as edge functions aren't auto-assigned a URL route to use as an endpoint."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Unlike regular functions, edge functions aren't automatically assigned a URL route for you to use as a function endpoint. Instead, you configure your edge functions to run on specific URL patterns.

You can configure the edge function path [inline in the function code](#declare-edge-functions-inline) or [in `netlify.toml`](#declare-edge-functions-in-netlify-toml).

## Declare edge functions inline

To configure the edge function path in the same file as the function code, export a `config` object with the following properties:

- **`path`:** [`URLPattern`](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API#pattern_syntax) expression on which paths to run the edge function. Must start with `/`, for example `path = "/*"`.
- **`excludedPath`:** optional `URLPattern` exclusion to limit the routes matched by `path`. Must also start with `/`, for example `excludedPath = "/*.css"`. Accepts a single string or an array of strings.
- **`pattern`:** alternative to the `path` property that allows for regex path matching.
- **`excludedPattern`:** optional regex exclusion to limit the routes matched by `pattern`. Accepts a single regex or an array of regex.
- **`method`:** optional HTTP methods that should run the edge function. Accepts a string or an array of strings.
- **`header`:** optional conditions on HTTP headers that must be met for the edge function to run. Accepts an [object with conditions](#match-by-headers).
- **`onError`:** optional setting to control how this function [handles errors](/build/edge-functions/optional-configuration#error-handling).
- **`cache`:** optional setting to opt in to [response caching](/build/edge-functions/optional-configuration#response-caching).

```ts
import type { Config } from "@netlify/edge-functions";

export default async () => new Response("Hello, world!");

export const config: Config = {
  path: "/test",
};
```

### Match by path

The `path` property can be a string if you want the edge function to run on a single path or an array of strings if you want to configure multiple paths.

In both cases, you can use [`URLPattern` expressions](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API#pattern_syntax) to match multiple paths.

```ts
import type { Config } from "@netlify/edge-functions";

export default async () => new Response("Hello, world!");

export const config: Config = {
  path: ["/", "/products/*"],
};
```

To limit the paths matched, use `excludedPath`.

```ts
import type { Config } from "@netlify/edge-functions"

export default async () => new Response("Hello, world!")

export const config: Config = {
  path: "/*",
  excludedPath: ["/*.css", "/*.js"]
}
```

This example shows an edge function that runs on all requests except for requests to CSS or JS files.

Values for `path` and `excludedPath` must start with `/`, for example `path: "/*"`.

### Match by headers

The `header` property accepts an object specifying a set of conditions that must be observed on the HTTP headers present in the request.

Each key represents the name of an HTTP header, and the values can be one of the following:

- `true`: Matches the edge function only if the header is present in the request
- `false`: Matches the edge function only if the header is not present in the request
- A string: Matches the edge function only if the header value matches the [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) represented in the string

For example, the following edge function will only run if the request contains a `x-required` header. But if it also contains a `x-forbidden` header, the edge function will not run.

```ts
import type { Config } from "@netlify/edge-functions";

export default async () => new Response("Hello, world!");

export const config: Config = {
  header: {
    "x-required": true,
    "x-forbidden": false
  },
  path: "/*",
};
```

Header names are case-insensitive. For example, both `x-required` and `X-Required` will match any variation of that header name.

In the example below, the edge function will only run if the `user-agent` header contains the strings `iPhone` or `Android`.

```ts
import type { Config } from "@netlify/edge-functions";

export default async () => new Response("Hello, world!");

export const config: Config = {
  header: {
    "user-agent": "(iPhone|Android)"
  },
  path: "/*",
};
```

### Tip - Matching by user-agent categories

Netlify provides a custom request header (`netlify-agent-category`) which maps any `user-agent` header value to a specific category of clients. [Learn more.](/build/user-agent-categories)

When a request contains multiple values with the same name, the string used for matching is the comma-separated list of all the values. This lets you choose whether to match on all the values or on a subset of them.

For example, the following edge function will run if the `accept-language` header contains at least `de` and `en`.

```ts
import type { Config } from "@netlify/edge-functions";

export default async () => new Response("Hello world / Hallo welt");

export const config: Config = {
  header: {
    // Changing to "^en$" lets you strictly match on a single value.
    "accept-language": "^(?=.*\bde\b)(?=.*\ben\b).*$"
  },
  path: "/*",
};
```

## Declare edge functions in `netlify.toml`

If you would like to declare multiple edge functions to run on the same path and customize the order they run in, configure edge function paths in `netlify.toml` instead of inline in the function file. You can use the following properties to configure `edge_functions` in `netlify.toml`:

- **`function`:** name of the edge function you're configuring. 
- **`path`:** [`URLPattern`](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API#pattern_syntax) expression on which paths to run the edge function. Must start with `/`, for example `path = "/*"`.
- **`excludedPath`:** optional `URLPattern` exclusion to limit the routes matched by `path`. Must also start with `/`, for example `excludedPath = "/*.css"`. Accepts a single string or an array of strings. 
- **`pattern`:** alternative to the `path` property that allows for regex path matching.
- **`excludedPattern`:** optional regex exclusion to limit the routes matched by `pattern`. Accepts a single regex or an array of regex.
- **`header`:** optional conditions on HTTP headers that must be met for the edge function to run. Accepts an [object with conditions](#match-by-headers-1).
- **`cache`:** optional setting to opt in to [response caching](/build/edge-functions/optional-configuration#response-caching).

Each edge function declaration associates one or more site paths or patterns with one function to execute on requests that match the paths or patterns. A single request can execute a chain of edge functions from a series of declarations. A single edge function can be associated with multiple paths across various declarations. Edge functions run in order of declaration in the file, from top to bottom, with the exception that edge functions [configured for caching](/build/edge-functions/optional-configuration#response-caching) always run after those that are not.

```toml
[[edge_functions]]
  path = "/admin"
  function = "auth"

[[edge_functions]]
  path = "/admin"
  function = "injector"
  cache = "manual"

[[edge_functions]]
  path = "/blog/*"
  function = "auth"

[[edge_functions]]
  path = "/blog/*"
  function = "rewriter"

[[edge_functions]]
  pattern = "/products/(.*)"
  excludedPattern = "/products/things/(.*)"
  function = "highlight"

[[edge_functions]]
  path = "/*"
  excludedPath = "/img/*"
  function = "common"
```

This example shows how both paths and functions can be configured across multiple declarations. 

- A request for `/admin` would invoke the `auth` function first, then `common`, and finally `injector`. Because it is configured for caching, the `injector` function runs after the other functions even though it is declared between them.
- The `auth` function runs for the `/admin` path and any child paths of `/blog`.

### Match by headers

The `header` property accepts an object specifying a set of conditions that must be observed on the HTTP headers present in the request.

Each key represents the name of an HTTP header, and the values can be one of the following:

- `true`: Matches the edge function only if the header is present in the request
- `false`: Matches the edge function only if the header is not present in the request
- A string: Matches the edge function only if the header value matches the [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) represented in the string

For example, the following declaration makes the edge function run if the request contains a `x-required` header, but not if it also contains a `x-forbidden` header.

```toml
[[edge_functions]]
  path = "/*"
  excludedPath = "/img/*"
  function = "common"

  [edge_functions.header]
  x-forbidden = false
  x-required = true
```

Header names are case-insensitive. For example, both `x-required` and `X-Required` will match any variation of that header name.

In the example below, the edge function will only run if the `user-agent` header contains the strings `iPhone` or `Android`.

```toml
[[edge_functions]]
  path = "/*"
  excludedPath = "/img/*"
  function = "common"

  [edge_functions.header]
  user-agent = "(iPhone|Android)"
```

When a request contains multiple values with the same name, the string used for matching is the comma-separated list of all the values. This lets you choose whether to match on all the values or on a subset of them.

For example, the following edge function will run if the `accept-language` header contains at least `de` and `en`.

```ts
[[edge_functions]]
  path = "/*"
  excludedPath = "/img/*"
  function = "common"

  [edge_functions.header]
  # Changing to "^en$" lets you strictly match on a single value.
  accept-language = "^(?=.*\bde\b)(?=.*\ben\b).*$"
```

## Declaration processing order

In general, edge functions are processed in the following order:
- edge functions [declared in a configuration file](#declare-edge-functions-in-netlify-toml) run before those [declared inline](#declare-edge-functions-inline)
- framework-generated edge functions run before user-created edge functions
- edge functions that are not configured for caching run before edge functions that are [configured for caching](/build/edge-functions/optional-configuration#response-caching)

This section outlines the processing order, and [any exceptions](#processing-order-caveats), in more detail.

When a request is made for a path, such as `/admin`, edge functions run in the following order. Netlify loops through this order twice - the first time running edge functions that are not configured for caching and the second time running edge functions that are configured for caching.
1. Edge functions your framework generates and declares for the path in a configuration file. 
2. Edge functions you declare for the path in `netlify.toml`. If you declare multiple edge functions for the same path, they run in order of declaration in the file, from top to bottom. 
    
    Note that if you declare the same edge function both in `netlify.toml` and inline, Netlify merges the configurations and treats them as inline declarations (refer to step 4). The inline configuration takes precedence for any duplicate fields. 
3. Edge functions your framework and enabled integrations generate and declare for the path with inline configuration.
4. Edge functions you declare for the path with inline configuration. If you use inline configuration to declare multiple edge functions for the same path, they run in alphabetical order by function file name. 

Once all edge functions for the path run, Netlify moves on to evaluate any redirect rules - unless the last [edge function returns a response](#processing-order-caveats) and ends the request chain. A redirect might request a new path that also requires edge functions and the above steps will repeat for that new path. 

The request chain continues until it eventually serves static content or returns a request from a serverless function. Learn more about [request handling](/build/edge-functions/api#request-handling) with edge functions.

### Tip

Use <code>netlify.toml</code> to be explicit about edge function order</span>">
If you want to customize the order in which multiple edge functions run on a given path, we recommend that you [add the declarations to `netlify.toml`](#declare-edge-functions-in-netlify-toml) instead of using inline declarations.

### Processing order caveats

Keep the following caveats in mind as you write and configure your edge functions as these items can interrupt or change the expected order of events:

- If the edge function for a path [returns a response](/build/edge-functions/api#return-a-response) and terminates the request, redirects for that path do not occur.
- If you declare an edge function for the target path of a [static routing rewrite](/manage/routing/redirects/rewrites-proxies), the page at the target path will be served but the edge function will not execute for rewritten requests.
- If the edge function uses `fetch()` for internal requests or `URL()` for internal rewrites, the command will start a new request chain and Netlify will run any edge functions that match that path first. If you want to request a specific static asset or serverless function with the same internal path, and not re-run the same edge functions, use `context.next()` instead.
- If an edge function fails, what happens next depends on its [error handling](/build/edge-functions/optional-configuration#error-handling) configuration.

Along with considering these caveats, we recommend you also review the [edge functions feature limitations](/build/edge-functions/limits#feature-limitations).

