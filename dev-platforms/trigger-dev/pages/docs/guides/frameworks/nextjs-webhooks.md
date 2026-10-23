---
title: "Triggering tasks with webhooks in Next.js"
source: https://trigger.dev/docs/guides/frameworks/nextjs-webhooks
path: docs/guides/frameworks/nextjs-webhooks
---

Learn how to trigger a task from a webhook in a Next.js app.

## Prerequisites

* [A Next.js project, set up with Trigger.dev](/docs/guides/frameworks/nextjs)
* [cURL](https://curl.se/) installed on your local machine. This will be used to send a POST request to your webhook handler.

## GitHub repo

> **[View the project on GitHub](https://github.com/triggerdotdev/examples/tree/main/nextjs-webhooks/my-app)**
>
> Click here to view the full code for this project in our examples repository on GitHub. You can
> fork it and use it as a starting point for your own project.

## Adding the webhook handler

The webhook handler in this guide will be an API route.

This will be different depending on whether you are using the Next.js pages router or the app router.

### Pages router: creating the webhook handler

Create a new file `pages/api/webhook-handler.ts` or `pages/api/webhook-hander.js`.

In your new file, add the following code:

```ts /pages/api/webhook-handler.ts theme={"theme":"css-variables"}
import { helloWorldTask } from "@/trigger/example";
import { tasks } from "@trigger.dev/sdk";
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  // Parse the webhook payload
  const payload = req.body;

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  res.status(200).json({ message: "OK" });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

### App router: creating the webhook handler

Create a new file in the `app/api/webhook-handler/route.ts` or `app/api/webhook-handler/route.js`.

In your new file, add the following code:

```ts /app/api/webhook-handler/route.ts theme={"theme":"css-variables"}
import type { helloWorldTask } from "@/trigger/example";
import { tasks } from "@trigger.dev/sdk";
import { NextResponse } from "next/server";

export async function POST(req: Request) {
  // Parse the webhook payload
  const payload = await req.json();

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  return NextResponse.json("OK", { status: 200 });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

## Triggering the task locally

Now that you have your webhook handler set up, you can trigger the 'Hello World' task from it. We will do this locally using cURL.

**1. Run your Next.js app and the Trigger.dev dev server**

First, run your Next.js app.

```bash npm theme={"theme":"css-variables"}
npm run dev
```

```bash pnpm theme={"theme":"css-variables"}
pnpm run dev
```

```bash yarn theme={"theme":"css-variables"}
yarn dev
```

Then, open up a second terminal window and start the Trigger.dev dev server:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest dev
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest dev
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest dev
```

**2. Trigger the webhook with some dummy data**

To send a POST request to your webhook handler, open up a terminal window on your local machine and run the following command:

> [!TIP]
>
> If `http://localhost:3000` isn't the URL of your locally running Next.js app, replace the URL in
> the below command with that URL instead.

```bash theme={"theme":"css-variables"}
curl -X POST -H "Content-Type: application/json" -d '{"Name": "John Doe", "Age": "87"}' http://localhost:3000/api/webhook-handler
```

This will send a POST request to your webhook handler, with a JSON payload.

**3. Check the task ran successfully**

After running the command, you should see a successful dev run and a 200 response in your terminals.

If you now go to your [Trigger.dev dashboard](https://cloud.trigger.dev), you should also see a successful run for the 'Hello World' task, with the payload you sent, in this case; `{"name": "John Doe", "age": "87"}`.

## Learn more about Next.js and Trigger.dev

### Walk-through guides from development to deployment

> **[Next.js - setup guide](/docs/guides/frameworks/nextjs)**
>
> Learn how to setup Trigger.dev with Next.js, using either the pages or app router.

> **[Next.js - triggering tasks using webhooks](/docs/guides/frameworks/nextjs-webhooks)**
>
> Learn how to create a webhook handler for incoming webhooks in a Next.js app, and trigger a task from it.

### Task examples

> **[Fal.ai with Realtime in Next.js](/docs/guides/examples/fal-ai-realtime)**
>
> Generate an image from a prompt using Fal.ai and Trigger.dev Realtime.

> **[Generate a cartoon using Fal.ai in Next.js](/docs/guides/examples/fal-ai-image-to-cartoon)**
>
> Convert an image to a cartoon using Fal.ai.

> **[Vercel sync environment variables](/docs/guides/examples/vercel-sync-env-vars)**
>
> Learn how to automatically sync environment variables from your Vercel projects to Trigger.dev.

> **[Vercel AI SDK](/docs/guides/examples/vercel-ai-sdk)**
>
> Learn how to use the Vercel AI SDK, which is a simple way to use AI models from different
> providers, including OpenAI, Anthropic, Amazon Bedrock, Groq, Perplexity etc.
