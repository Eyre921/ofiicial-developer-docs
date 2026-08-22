---
title: "Netlify Functions Overview"
source: https://docs.netlify.com/build/functions/overview.md
path: build/functions/overview
---

---
title: "Functions overview"
description: "Use serverless functions to run on-demand, server-side code without having to run a dedicated server."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

With Netlify Functions, you can build full-stack applications without having to manage servers. Whether you're experimenting with your first application or handling millions of requests, Netlify gives you the infrastructure that automatically scales as you grow.

Your functions are version-controlled, built, and deployed along with the rest of your Netlify site, giving you the power of [Deploy Previews](/deploy/deploy-types/deploy-previews/) and [instant rollbacks](/deploy/manage-deploys/manage-deploys-overview/#rollbacks).

Seamless integrations with [Database](/build/data-and-storage/netlify-database/), [Blobs](/build/data-and-storage/netlify-blobs/), [Caching](/build/caching/caching-overview/), and [AI Gateway](/build/ai-gateway/overview/) give you a powerful foundation to build any full-stack application on Netlify.

## How functions work

A function is a file in your project that contains server-side code for responding to an event.

When the event happens, Netlify hands your code the event payload, runs it in an ephemeral runtime environment, and acts on whatever it returns. The infrastructure automatically scales according to the volume of traffic to your site, so that the performance stays consistent no matter the load.

For web requests, the function returns a response that is delivered to the client. For other types of events, the function's return value can influence what happens next on the platform - for example, an identity handler can mutate a user record or reject a sign-up.

### Web requests

The most common event is a web request to your site. Your function receives a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and a [`Context`](/build/functions/api#context-object), and returns a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) that is delivered back to the client.

You can use the `config` object to [configure different aspects of your function](/build/functions/configuration), such as the URL paths that the function runs on or the HTTP method it responds to.

### Tabs Component:

<TabItem label="Basic">

```ts title="netlify/functions/hello.mts"

export default async (req: Request, context: Context) => {
  return new Response("Hello, world!")
}

export const config: Config = {
  path: "/hello",
}
```

</TabItem>
<TabItem label="Database">

```ts title="netlify/functions/users.mts"

const db = getDatabase()

export default async (req: Request) => {
  const users = await db.sql`SELECT id, email FROM users LIMIT 10`

  return Response.json({ users })
}

export const config: Config = {
  path: "/users",
}
```

</TabItem>
<TabItem label="Blobs">

```ts title="netlify/functions/upload.mts"

export default async (req: Request) => {
  const uploads = getStore("uploads")
  const key = crypto.randomUUID()

  await uploads.set(key, await req.blob())

  return Response.json({ key })
}

export const config: Config = {
  method: "POST",
  path: "/upload",
}
```

</TabItem>
<TabItem label="AI Gateway">

```ts title="netlify/functions/haiku.mts"

const client = new OpenAI()

export default async (req: Request, context: Context) => {
  const response = await client.responses.create({
    model: "gpt-5-mini",
    input: [{ role: "user", content: `Write a haiku about ${context.params.topic}.` }],
  })

  return Response.json({ haiku: response.output_text })
}

export const config: Config = {
  path: "/haiku/:topic",
}
```

</TabItem>

Alternatively, you can author your function as a [Fetchable module](https://fetchable.org/) for interoperability with JavaScript frameworks and runtimes that share this convention. Fetchable is a small emerging standard, primarily used today by platform and framework authors, that defines a uniform shape for fetch-style handlers. To use it, export an object with a `fetch` method instead of a bare default function:

### Tabs Component:

<TabItem label="Basic">

```ts title="netlify/functions/hello.mts"

export default {
  fetch: (req, context) => {
    return new Response("Hello, world!")
  },

  config: {
    path: "/hello",
  },
} satisfies NetlifyFunction
```

</TabItem>
<TabItem label="Database">

```ts title="netlify/functions/users.mts"

const db = getDatabase()

export default {
  fetch: async (req) => {
    const users = await db.sql`SELECT id, email FROM users LIMIT 10`

    return Response.json({ users })
  },

  config: {
    path: "/users",
  },
} satisfies NetlifyFunction
```

</TabItem>
<TabItem label="Blobs">

```ts title="netlify/functions/upload.mts"

export default {
  fetch: async (req) => {
    const uploads = getStore("uploads")
    const key = crypto.randomUUID()

    await uploads.set(key, await req.blob())

    return Response.json({ key })
  },

  config: {
    method: "POST",
    path: "/upload",
  },
} satisfies NetlifyFunction
```

</TabItem>
<TabItem label="AI Gateway">

```ts title="netlify/functions/haiku.mts"

const client = new OpenAI()

export default {
  fetch: async (req, context) => {
    const response = await client.responses.create({
      model: "gpt-5-mini",
      input: [{ role: "user", content: `Write a haiku about ${context.params.topic}.` }],
    })

    return Response.json({ haiku: response.output_text })
  },

  config: {
    path: "/haiku/:topic",
  },
} satisfies NetlifyFunction
```

</TabItem>

### Platform events

A function can also subscribe to platform events on your Netlify project, like a deploy completing, a form submission, or a user signup. To subscribe to one or more events, export an object whose properties are named event handlers, including a `fetch` handler for web requests if you want it.

```ts title="netlify/functions/on-deploy.mts"

export default {
  // Responds to web requests, same as a bare default export.
  fetch(req: Request, context: Context) {
    return new Response("Hello, world!")
  },

  // Runs after every successful deploy.
  deploySucceeded(event: DeploySucceededEvent) {
    console.log(`Deploy ${event.deploy.id} has shipped! 🚀`)
  },
}
```

Refer to [Get started with functions](/build/functions/get-started) for the full walkthrough or [Trigger functions on events](/build/functions/trigger-on-events) for the list of supported events.

## Manage your functions

Functions deployed from Netlify are immutable. This means that an update to a function on your production branch won't change the version that was deployed in a branch deploy, or in a Deploy Preview. You can access all versions of your functions in the Netlify web interface, under the **Functions** tab.

By default, the list displays all of the functions, including background functions, in the current [published deploy](/deploy/deploy-overview#definitions). To find functions on another deploy, you can use the search field at the top of the list. You can start typing to jump to a particular branch, or find a Deploy Preview by number.

## More Functions resources

- [Get started with functions](/build/functions/get-started)
- [API reference](/build/functions/api)
- [Configuration for functions](/build/functions/configuration)
- [Trigger functions on events](/build/functions/trigger-on-events)
- [Use Identity in functions](/manage/security/secure-access-to-sites/identity/use-identity-in-functions)
- [Background Functions overview](/build/functions/background-functions)
- [Scheduled Functions overview](/build/functions/scheduled-functions)
- [Environment variables and functions](/build/functions/environment-variables)
- [Function logs](/build/functions/logs)
- [Functions usage and billing](/build/functions/usage-and-billing)
- Function metrics in [Observability](/manage/monitoring/observability/overview) (credit-based plans) or [Function Metrics](/manage/monitoring/function-metrics) (legacy plans)
- Visit our [Forums](https://answers.netlify.com/categories) to join the conversation about Functions

