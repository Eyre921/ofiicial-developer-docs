---
title: "Get started with Functions"
source: https://docs.netlify.com/build/functions/get-started.md
path: build/functions/get-started
---

---
title: "Get started with functions"
description: "Create your first Netlify function in TypeScript or JavaScript, with options for using AI agents and testing locally."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

This page walks you through creating your first Netlify function. For the conceptual overview of how functions work, see [Functions overview](/build/functions/overview).

## Facet Switcher

Select your function language:

### Available Tabs:

#### TypeScript Tab

<div class="legacy-anchor" id="project-preparation">

#### JavaScript Tab

## Prepare project

Optionally add the `@netlify/functions` module to your project. It's not required for JavaScript functions, but it provides helper exports if you ever opt in.

```bash
npm install @netlify/functions
```

## Create your first function

Create a JavaScript file in [your functions directory](/build/functions/configuration#directory) - by default that's `netlify/functions/`. You can put the file directly in that folder or in a subdirectory; if you use a subdirectory, the entry file must be named `index` or match the subdirectory name.

For example, any of these would create a function called `hello`:

- `netlify/functions/hello.mjs`
- `netlify/functions/hello/hello.mjs`
- `netlify/functions/hello/index.mjs`

### Tip - Use the `.mjs` extension

Naming your file with the `.mjs` extension lets you use modern [ES module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) syntax. For more on file extensions and module formats, see [Configuration → Module format](/build/functions/configuration#module-format).

A function file has a default export with a handler that receives a web platform [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and a Netlify-specific [`context`](/build/functions/api#context-object), and returns a web platform [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response).

```js title="netlify/functions/hello.mjs"
export default async (req, context) => {
  return new Response("Hello, world!")
}

export const config = {
  path: "/hello",
}
```

Once deployed, the function is available at `https://<YOUR DOMAIN>/hello`. For additional routing configuration options, see [Configuration → Routing](/build/functions/configuration#routing).

## Building with an AI agent

If you'd rather describe what your function should do than write the code yourself, an AI coding agent can scaffold the function for you. You can use a local agent like Claude Code or Codex against your project, or use Netlify's [Agent Runners](/build/build-with-ai/agent-runners/overview), which run AI coding agents directly on your Netlify project and commit the changes for you.

A prompt as simple as the following will produce a working function:

```
Add a Netlify function at `/api/joke` that returns a random programming joke as JSON.
```

For more, see the [Agent Runners overview](/build/build-with-ai/agent-runners/overview) and [example prompts](/build/build-with-ai/agent-runners/prompt-examples-for-agent-runners).

## Test locally

Most modern frameworks include native support for Netlify Functions in their dev server, so you can run and test your function locally without any extra tooling.

If you're using a Vite-based framework, like [Astro](/build/frameworks/framework-setup-guides/astro/#local-development), [Nuxt](/build/frameworks/framework-setup-guides/nuxt/#local-development), [TanStack Start](/build/frameworks/framework-setup-guides/tanstack-start/#local-development), or [React Router](/build/frameworks/framework-setup-guides/react-router/#local-development), make sure your project has [`@netlify/vite-plugin`](/build/frameworks/framework-setup-guides/vite#vite-plugin) installed:

```bash
npm install @netlify/vite-plugin
```

Then run your framework's dev server. The plugin emulates the Netlify platform inside the dev server, so functions, edge functions, blobs, environment variables, and other primitives behave the same locally as in production.

If you're on Next.js, use the [Netlify CLI](/api-and-cli-guides/cli-guides/local-development/) instead. The CLI starts a framework server (if one is detected) and handles redirects, proxy rules, environment variables, and Netlify Functions through a simulated Netlify production environment. The CLI is also a good fallback for any other framework that isn't covered by the Vite plugin.

## Next steps

Push your function source files to your Git provider for continuous deployment where Netlify's build system automatically detects, builds, and deploys your functions. You can also deploy manually with the [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli) or [API](/api-and-cli-guides/api-guides/get-started-with-api).

Monitor function [logs](/build/functions/logs/) and [metrics](/manage/monitoring/function-metrics/) in the Netlify UI to observe and help troubleshoot your deployed functions. 

Netlify function logs are found in the Netlify UI. You can also stream Netlify function logs to the console with the [Netlify CLI](https://cli.netlify.com/commands/logs/#logsfunction).

#### Go Tab

## Use the Lambda-compatible API for Go

To write functions in Go, use the [Lambda-compatible functions API](/build/functions/lambda-compatibility/?fn-language=go).


