---
title: "Netlify Edge Functions Overview"
source: https://docs.netlify.com/build/edge-functions/overview.md
path: build/edge-functions/overview
---

---
title: "Edge Functions overview"
description: "Edge Functions connect our platform with an open runtime standard at the network edge, allowing fast, personalized web experiences in a dev ecosystem."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Edge Functions connect the Netlify platform and workflow with an open runtime standard at the network edge. This enables you to build fast, personalized web experiences with an ecosystem of development tools.

Using TypeScript and JavaScript, you can modify network requests to localize content, serve relevant ads, authenticate users, personalize content, redirect visitors, and much more. Edge Functions also support a new generation of edge-first web frameworks allowing your entire app to run at the edge, dramatically increasing performance in many cases.

All this dynamic processing happens in a secure runtime based on [Deno](https://deno.land/) directly from the worldwide network edge location closest to each user for fast response times. Plus, you have the option to cache edge function responses for even faster response times. With Netlify, your edge functions are version-controlled, built, and deployed along with the rest of your Netlify site. This eliminates overhead and brings the power of Deploy Previews and rollbacks to your edge functions.

## Use cases

To learn more about what's possible with Edge Functions, explore the following.

Reference examples of common patterns:

- [Transform responses with content includes](https://edge-functions-examples.netlify.app/example/include)
- [Set custom HTTP request headers](https://edge-functions-examples.netlify.app/example/set-request-header)
- [Localize content with geolocation](https://edge-functions-examples.netlify.app/example/localized-content)
- [Rewrite responses from another URL](https://answers.netlify.com/t/new-syntax-for-rewrites-in-edge-functions/88257)
- [A/B tests using cookies](https://edge-functions-examples.netlify.app/example/abtest)
- [Calculate responses with WebAssembly](https://edge-functions-examples.netlify.app/example/wasm)

Framework-specific examples:

- [Astro](https://astro.build/blog/netlify-edge-functions/)
- [Eleventy](https://www.11ty.dev/blog/eleventy-edge/)
- [Hydrogen](https://github.com/netlify/hydrogen-template)
- Next.js: [React Server Components](https://github.com/netlify/next-react-server-components), [Edge Middleware](https://github.com/netlify/next-edge-middleware)
- [Nuxt 3](https://nitro.unjs.io/deploy/providers/netlify)
- [Remix](https://github.com/netlify/remix-edge-template)
- [SvelteKit](https://github.com/sveltejs/kit/tree/master/packages/adapter-netlify)
- [Qwik](https://qwik.builder.io/deployments/netlify-edge/)

## Documentation

To learn how to create your own edge functions, check out the documentation.

- [**Get started**](/build/edge-functions/get-started)**:** basic hello world example that covers testing and debugging locally, deploying, invoking, and monitoring an edge function.
- [**Edge Functions API**](/build/edge-functions/api)**:** introduction to key concepts and a full endpoint reference.
- [**Declarations**](/build/edge-functions/declarations)**:** configuration details and processing order.
- [**Optional configuration**](/build/edge-functions/optional-configuration)**:** options for more control over how your edge functions are built and executed, such as configuring edge functions for caching.
- [**Limits**](/build/edge-functions/limits)**:** operation limits for the runtime environment and feature limitations.
- [**Create an integration**](/build/edge-functions/create-integration)**:** guidance for framework authors making integrations for developers to use.
- [**Usage and billing**](/build/edge-functions/usage-and-billing)**:** how to monitor your invocation usage.

## More Edge Functions resources

- [Full library of reference examples](https://edge-functions-examples.netlify.app/)
- [Netlify blog: Edge Functions posts](https://www.netlify.com/blog/tags/netlify-edge-functions/)
- [Environment variables and edge functions](/build/edge-functions/environment-variables)
- [Use the Netlify Blobs API in an edge function](/build/data-and-storage/netlify-blobs/)

## Feedback

We welcome your feedback on this feature. Visit our [Forums](https://answers.netlify.com/categories) to join the conversation about Edge Functions.

