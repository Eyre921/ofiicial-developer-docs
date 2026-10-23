---
title: "Triggering tasks from Supabase edge functions"
source: https://trigger.dev/docs/guides/frameworks/supabase-edge-functions-basic
path: docs/guides/frameworks/supabase-edge-functions-basic
---

This guide will show you how to trigger a task from a Supabase edge function, and then view the run in our dashboard.

## Overview

Supabase edge functions allow you to trigger tasks either when an event is sent from a third party (e.g. when a new Stripe payment is processed, when a new user signs up to a service, etc), or when there are any changes or updates to your Supabase database.

This guide shows you how to set up and deploy a simple Supabase edge function example that triggers a task when an edge function URL is accessed.

## Prerequisites

* Ensure you have the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) installed
* Since Supabase CLI version 1.123.4, you must have [Docker Desktop installed](https://supabase.com/docs/guides/functions/deploy#deploy-your-edge-functions) to deploy Edge Functions
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## GitHub repo

> **[View the project on GitHub](https://github.com/triggerdotdev/examples/tree/main/supabase-edge-functions)**
>
> Click here to view the full code for this project in our examples repository on GitHub. You can
> fork it and use it as a starting point for your own project.

## Initial setup

**1. Optional step 1: create a new Supabase project**

> [!NOTE]
>
> If you already have a Supabase project on your local machine you can skip this step.

You can create a new project by running the following command in your terminal using the Supabase CLI:

```bash theme={"theme":"css-variables"}
supabase init
```

> [!NOTE]
>
> If you are using VS Code, ensure to answer 'y' when asked to generate VS Code settings for Deno,
> and install any recommended extensions.

**2. Optional step 2: create a package.json file**

If your project does not already have `package.json` file (e.g. if you are using Deno), create it manually in your project's root folder.

> [!NOTE]
>
> If your project has a `package.json` file you can skip this step.

This is required for the Trigger.dev SDK to work correctly.

```ts package.json theme={"theme":"css-variables"}
{
  "devDependencies": {
    "typescript": "^5.6.2"
  }
}
```

> [!NOTE]
>
> Update your Typescript version to the latest version available.

**3. Run the CLI `init` command**

The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

Run this command in the root of your project to get started:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest init
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest init
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest init
```

It will do a few things:

> [!TIP]
>
> Our [Trigger.dev MCP server](/docs/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.

1. Ask if you want to set up AI tooling: the [Trigger.dev MCP server](/docs/mcp-introduction) and/or Trigger.dev agent skills (shown the first time you run init). If you choose either, you can let your AI assistant finish the setup instead of the CLI.
2. Log you into the CLI if you're not already logged in.
3. Ask you to select your project.
4. Install the required SDK packages.
5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
6. Create a `trigger.config.ts` file in the root of your project.

Install the "Hello World" example task when prompted. We'll use this task to test the setup.

**4. Run the CLI `dev` command**

The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest dev
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest dev
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest dev
```

**5. Perform a test run using the dashboard**

The CLI `dev` command spits out various useful URLs, including a link to the dashboard. Open it, find your Example task on the Tasks page, and press the "Test" button to open its test page.

Most tasks have a "payload" which you enter in the JSON editor, but our example task doesn't need any input. You can also configure run options, pre-populate the form from recent runs, and save run templates.

Press the "Run test" button.

![Test page](https://mintcdn.com/trigger/2gGDaV8FR4pPhx_f/images/test-dashboard.png?fit=max\&auto=format\&n=2gGDaV8FR4pPhx_f\&q=85\&s=9a7c31f3499500be59e62586763e03d1)

**6. View your run**

Congratulations, you should see the run page which will live reload showing you the current state of the run.

![Run page](https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?fit=max\&auto=format\&n=5SxX7bFjJKRsidSL\&q=85\&s=4b0bb5f9b181499cf324cdb8d5d673a8)

If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

![Terminal showing completed run](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=a9284c5228343b72d798c6e36f5acb24)

## Create a new Supabase edge function and deploy it

**1. Create a new Supabase edge function**

We'll call this example `edge-function-trigger`.

In your project, run the following command in the terminal using the Supabase CLI:

```bash theme={"theme":"css-variables"}
supabase functions new edge-function-trigger
```

**2. Update the edge function code**

Replace the placeholder code in your `edge-function-trigger/index.ts` file with the following:

```ts functions/edge-function-trigger/index.ts theme={"theme":"css-variables"}
// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
// Import the Trigger.dev SDK - replace "<your-sdk-version>" with the version of the SDK you are using, e.g. "3.0.0". You can find this in your package.json file.
import { tasks } from "npm:@trigger.dev/sdk@3.0.0";
// Import your task type from your /trigger folder
import type { helloWorldTask } from "../../../src/trigger/example.ts";
//     👆 **type-only** import

Deno.serve(async () => {
  await tasks.trigger<typeof helloWorldTask>(
    // Your task id
    "hello-world",
    // Your task payload
    "Hello from a Supabase Edge Function!"
  );
  return new Response("OK");
});
```

> [!NOTE]
>
> You can only import the `type` from the task.

> [!NOTE]
>
> Tasks in the `trigger` folder use Node, so they must stay in there or they will not run,
> especially if you are using a different runtime like Deno. Also do not add "`npm:`" to imports
> inside your task files, for the same reason.

**3. Deploy your edge function using the Supabase CLI**

You can now deploy your edge function with the following command in your terminal:

```bash theme={"theme":"css-variables"}
supabase functions deploy edge-function-trigger --no-verify-jwt
```

> [!WARNING]
>
> `--no-verify-jwt` removes the JSON Web Tokens requirement from the authorization header. By
> default this should be on, but it is not strictly required for this hello world example.

> [!NOTE]
>
> To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
> our [Supabase Authentication guide](/docs/guides/frameworks/supabase-authentication). It demonstrates
> how to use JWT authentication for user-specific operations or your service role key for
> admin-level access.

Follow the CLI instructions and once complete you should now see your new edge function deployment in your Supabase edge functions dashboard.

There will be a link to the dashboard in your terminal output, or you can find it at this URL:

`https://supabase.com/dashboard/project/<your-project-id>/functions`

> [!NOTE]
>
> Replace `your-project-id` with your actual project ID.

## Create a Trigger.dev API key for Supabase

Open the API Keys page for your Production environment in the Trigger.dev [project dashboard](https://cloud.trigger.dev). Create a named key with **Trigger only** access and copy it. Trigger.dev shows the complete value only once.

Then, in [Supabase](https://supabase.com/dashboard/projects), select your project, navigate to 'Project settings' , click 'Edge functions'  in the configurations menu, and then click the 'Add new secret'  button.

Add `TRIGGER_SECRET_KEY`  with the environment API key you created.

![Add secret key in Supabase](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=70842bf838bc1ea9e1f195c9926bb746)

## Deploy your task and trigger it from your edge function

**1. Deploy your 'Hello World' task**

Next, deploy your `hello-world` task to [Trigger.dev cloud](https://cloud.trigger.dev).

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest deploy
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest deploy
```

**2. Trigger a prod run from your deployed edge function**

To do this all you need to do is simply open the `edge-function-trigger` URL.

`https://supabase.com/dashboard/project/<your-project-id>/functions`

> [!NOTE]
>
> Replace `your-project-id` with your actual project ID.

In your Supabase project, go to your Edge function dashboard, find `edge-function-trigger`, copy the URL, and paste it into a new window in your browser.

Once loaded you should see ‘OK’ on the new screen.

![Edge function URL](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=39bf78f3b0d9fab4d92cc1cda60fbcec)

The task will be triggered when your edge function URL is accessed.

Check your [cloud.trigger.dev](https://cloud.trigger.dev) dashboard and you should see a successful `hello-world` task.

**Congratulations, you have run a simple Hello World task from a Supabase edge function!**

### If you see a runtime error when calling tasks.trigger()

If you see `TypeError: Cannot read properties of undefined (reading 'toString')` when calling `tasks.trigger()` from your edge function, the SDK is hitting a dependency that expects Node-style APIs not available in the Supabase Edge (Deno) runtime. Use the [Tasks API](/docs/management/tasks/trigger) with `fetch` instead of the SDK—that avoids loading the SDK in Deno:

```ts theme={"theme":"css-variables"}
const response = await fetch(
  `https://api.trigger.dev/api/v1/tasks/your-task-id/trigger`,
  {
    method: "POST",
    headers: {
      Authorization: `Bearer ${Deno.env.get("TRIGGER_SECRET_KEY")}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ payload: { your: "payload" } }),
  }
);
```

See [Trigger task via API](/docs/management/tasks/trigger) for full request/response details and optional fields (e.g. `delay`, `idempotencyKey`).

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

> **[Edge function hello world guide](/docs/guides/frameworks/supabase-edge-functions-basic)**
>
> Learn how to trigger a task from a Supabase edge function when a URL is visited.

> **[Database webhooks guide](/docs/guides/frameworks/supabase-edge-functions-database-webhooks)**
>
> Learn how to trigger a task from a Supabase edge function when an event occurs in your database.

> **[Supabase authentication guide](/docs/guides/frameworks/supabase-authentication)**
>
> Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
> keys for admin access.

### Task examples with code you can copy and paste

> **[Supabase database operations](/docs/guides/examples/supabase-database-operations)**
>
> Run basic CRUD operations on a table in a Supabase database using Trigger.dev.

> **[Supabase Storage upload](/docs/guides/examples/supabase-storage-upload)**
>
> Download a video from a URL and upload it to Supabase Storage using S3.
