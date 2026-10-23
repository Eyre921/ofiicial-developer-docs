---
title: "Remix setup guide"
source: https://trigger.dev/docs/guides/frameworks/remix
path: docs/guides/frameworks/remix
---

This guide will show you how to setup Trigger.dev in your existing Remix project, test an example task, and view the run.

## Prerequisites

* Setup a project in Remix
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## Initial setup

**1. Run the CLI `init` command**

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

**2. Run the CLI `dev` command**

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

**3. Perform a test run using the dashboard**

The CLI `dev` command spits out various useful URLs, including a link to the dashboard. Open it, find your Example task on the Tasks page, and press the "Test" button to open its test page.

Most tasks have a "payload" which you enter in the JSON editor, but our example task doesn't need any input. You can also configure run options, pre-populate the form from recent runs, and save run templates.

Press the "Run test" button.

![Test page](https://mintcdn.com/trigger/2gGDaV8FR4pPhx_f/images/test-dashboard.png?fit=max\&auto=format\&n=2gGDaV8FR4pPhx_f\&q=85\&s=9a7c31f3499500be59e62586763e03d1)

**4. View your run**

Congratulations, you should see the run page which will live reload showing you the current state of the run.

![Run page](https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?fit=max\&auto=format\&n=5SxX7bFjJKRsidSL\&q=85\&s=4b0bb5f9b181499cf324cdb8d5d673a8)

If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

![Terminal showing completed run](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=a9284c5228343b72d798c6e36f5acb24)

## Create an API key for local development

Open the API Keys page for your Development environment and create a named key with **Trigger only** access. Set the key as `TRIGGER_SECRET_KEY` in your `.env` file so your Remix app can trigger runs.

For more information on authenticating with Trigger.dev, see the [API keys page](/docs/apikeys).

## Triggering your task in Remix

**1. Create an API route**

Create a new file called `api.hello-world.ts` (or `api.hello-world.js`) in the `app/routes` directory like this: `app/routes/api.hello-world.ts`.

**2. Add your task**

Add this code to your `api.hello-world.ts` file which imports your task:

```ts app/routes/api.hello-world.ts theme={"theme":"css-variables"}
import type { helloWorldTask } from "../../src/trigger/example";
import { tasks } from "@trigger.dev/sdk";

export async function loader() {
  const handle = await tasks.trigger<typeof helloWorldTask>("hello-world", "James");

  return new Response(JSON.stringify(handle), {
    headers: { "Content-Type": "application/json" },
  });
}
```

**3. Trigger your task**

Run your Remix app:

```bash npm theme={"theme":"css-variables"}
npm run dev
```

```bash pnpm theme={"theme":"css-variables"}
pnpm run dev
```

```bash yarn theme={"theme":"css-variables"}
yarn dev
```

Run the dev server from Step 2. of the [Initial Setup](/docs/guides/frameworks/remix#initial-setup) section above if it's not already running:

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest dev
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest dev
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest dev
```

Now visit the URL in your browser to trigger the task. Ensure the port number is the same as the one you're running your Remix app on. For example, if you're running your Remix app on port 3000, visit:

```bash theme={"theme":"css-variables"}
http://localhost:3000/api/trigger
```

You should see the CLI log the task run with a link to view the logs in the dashboard.

![Trigger.dev CLI showing a successful run](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/trigger-cli-run-success.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=75168b271620e7206a50b041224a98b0)

Visit the [Trigger.dev dashboard](https://cloud.trigger.dev) to see your run.

## Manually add your environment variables (optional)

If you have any environment variables in your tasks, be sure to add them in the dashboard so deployed code runs successfully. In Node.js, these environment variables are accessed in your code using `process.env.MY_ENV_VAR`.

In the sidebar select the "Environment Variables" page, then press the "Add new"
button. ![Environment variables page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=af652254781808a35c2bcefd4b61b59f)

You can add values for your local dev environment, staging and prod. ![Environment variables
page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=79b5fd91e809cb0c6c9298410922df96)

You can also add environment variables in code by following the steps on the [Environment Variables page](/docs/deploy-environment-variables#in-your-code).

## Deploying your task to Trigger.dev

For this guide, we'll manually deploy your task by running the [CLI deploy command](/docs/cli-deploy-commands) below. Other ways to deploy are listed in the next section.

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest deploy
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest deploy
```

### Other ways to deploy

**GitHub Actions**

Use GitHub Actions to automatically deploy your tasks whenever new code is pushed and when the `trigger` directory has changes in it. Follow [this guide](/docs/github-actions) to set up GitHub Actions.

**Vercel Integration**

Use the official [Vercel integration](/docs/vercel-integration) to deploy your tasks automatically.

## Deploying to Vercel Edge Functions

Before we start, it's important to note that:

* We'll be using a type-only import for the task to ensure compatibility with the edge runtime.
* The `@trigger.dev/sdk` package supports the edge runtime out of the box.

There are a few extra steps to follow to deploy your `/api/hello-world` API endpoint to Vercel Edge Functions.

**1. Update your API route**

Update your API route to use the `runtime: "edge"` option and change it to an `action()` so we can trigger the task from a curl request later on.

```ts app/routes/api.hello-world.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";
import type { helloWorldTask } from "../../src/trigger/example";
//      👆 **type-only** import

// include this at the top of your API route file
export const config = {
  runtime: "edge",
};
export async function action({ request }: { request: Request }) {
  // This is where you'd authenticate the request
  const payload = await request.json();
  const handle = await tasks.trigger<typeof helloWorldTask>("hello-world", payload);
  return new Response(JSON.stringify(handle), {
    headers: { "Content-Type": "application/json" },
  });
}
```

**2. Update the Vercel configuration**

Create or update the `vercel.json` file with the following:

```json vercel.json theme={"theme":"css-variables"}
{
  "buildCommand": "npm run vercel-build",
  "devCommand": "npm run dev",
  "framework": "remix",
  "installCommand": "npm install",
  "outputDirectory": "build/client"
}
```

**3. Update package.json scripts**

Update your `package.json` to include the following scripts:

```json package.json theme={"theme":"css-variables"}
"scripts": {
    "build": "remix vite:build",
    "dev": "remix vite:dev",
    "lint": "eslint --ignore-path .gitignore --cache --cache-location ./node_modules/.cache/eslint .",
    "start": "remix-serve ./build/server/index.js",
    "typecheck": "tsc",
    "vercel-build": "remix vite:build && cp -r ./public ./build/client"
},
```

**4. Deploy to Vercel**

Push your code to a Git repository and create a new project in the Vercel dashboard. Select your repository and follow the prompts to complete the deployment.

**5. Add your Vercel environment variables**

Open the Trigger.dev API Keys page for the environment your Vercel deployment uses. Create a named key with **Trigger only** access, then add it to the Vercel project settings:

```bash theme={"theme":"css-variables"}
TRIGGER_SECRET_KEY=tr_prod_sk_xxxxxxxxxx
```

**6. Deploy your project**

Once you've added the environment variable, deploy your project to Vercel.

> [!NOTE]
>
> Ensure you have also deployed your Trigger.dev task. See [deploy your task
> step](/docs/guides/frameworks/remix#deploying-your-task-to-trigger-dev).

**7. Test your task in production**

After deployment, you can test your task in production by running this curl command:

```bash theme={"theme":"css-variables"}
curl -X POST https://your-app.vercel.app/api/hello-world \
-H "Content-Type: application/json" \
-d '{"name": "James"}'
```

This sends a POST request to your API endpoint with a JSON payload.

### Additional notes

The `vercel-build` script in `package.json` is specific to Remix projects on Vercel, ensuring that static assets are correctly copied to the build output.

The `runtime: "edge"` configuration in the API route allows for better performance on Vercel's Edge Network.

## Realtime updates with React hooks

The `@trigger.dev/react-hooks` package lets you subscribe to task runs from your React components. Show progress bars, stream AI responses, or display run status in real time.

> **[React hooks](/docs/realtime/react-hooks/overview)**
>
> Hooks for subscribing to runs, streaming data, and triggering tasks from the frontend.

> **[Streams](/docs/tasks/streams)**
>
> Pipe continuous data (like AI completions) from your tasks to the client while they run.

## Additional resources for Remix

> **[Remix - triggering tasks using webhooks](/docs/guides/frameworks/remix-webhooks)**
>
> How to create a webhook handler in a Remix app, and trigger a task from it.

## Useful next steps

> **[Tasks overview](/docs/tasks/overview)**
>
> Learn what tasks are and their options

> **[Writing tasks](/docs/writing-tasks-introduction)**
>
> Learn how to write your own tasks

> **[Deploy using the CLI](/docs/cli-deploy-commands)**
>
> Learn how to deploy your task manually using the CLI

> **[Deploy using GitHub actions](/docs/github-actions)**
>
> Learn how to deploy your task using GitHub actions
