---
title: "Drizzle setup guide"
source: https://trigger.dev/docs/guides/frameworks/drizzle
path: docs/guides/frameworks/drizzle
---

This guide will show you how to set up Drizzle ORM with Trigger.dev

## Overview

This guide will show you how to set up [Drizzle ORM](https://orm.drizzle.team/) with Trigger.dev, test and view an example task run.

## Prerequisites

* An existing Node.js project with a `package.json` file
* Ensure TypeScript is installed
* A [PostgreSQL](https://www.postgresql.org/) database server running locally, or accessible via a connection string
* Drizzle ORM [installed and initialized](https://orm.drizzle.team/docs/get-started) in your project
* A `DATABASE_URL` environment variable set in your `.env` file, pointing to your PostgreSQL database (e.g. `postgresql://user:password@localhost:5432/dbname`)

> [!TIP]
>
> If your Postgres lives in a private AWS VPC (e.g. RDS without a public endpoint), connect it via
> [Private networking](/docs/private-networking/overview) instead of opening it to the public internet
> (Pro and Enterprise plans).

## Initial setup (optional)

Follow these steps if you don't already have Trigger.dev set up in your project.

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

## Creating a task using Drizzle and deploying it to production

**1. The task using Drizzle**

First, create a new task file in your `trigger` folder.

This is a simple task that will add a new user to your database, we will call it `drizzle-add-new-user`.

> [!NOTE]
>
> For this task to work correctly, you will need to have a `users` table schema defined with Drizzle
> that includes `name`, `age` and `email` fields.

```ts /trigger/drizzle-add-new-user.ts theme={"theme":"css-variables"}
import { eq } from "drizzle-orm";
import { task } from "@trigger.dev/sdk";
import { users } from "src/db/schema";
import { drizzle } from "drizzle-orm/node-postgres";

// Initialize Drizzle client
const db = drizzle(process.env.DATABASE_URL!);

export const addNewUser = task({
  id: "drizzle-add-new-user",
  run: async (payload: typeof users.$inferInsert) => {
    // Create new user
    const [user] = await db.insert(users).values(payload).returning();

    return {
      createdUser: user,
      message: "User created and updated successfully",
    };
  },
});
```

**2. Configuring the build**

Next, in your `trigger.config.js` file, add `pg` to the `externals` array. `pg` is a non-blocking PostgreSQL client for Node.js.

It is marked as an external to ensure that it is not bundled into the task's bundle, and instead will be installed and loaded from `node_modules` at runtime.

```js /trigger.config.js theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>", // Your project reference
  // Your other config settings...
  build: {
    externals: ["pg"],
  },
});
```

**3. Deploying your task**

Once the build configuration is added, you can now deploy your task using the Trigger.dev CLI.

```bash npm theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

```bash pnpm theme={"theme":"css-variables"}
pnpm dlx trigger.dev@latest deploy
```

```bash yarn theme={"theme":"css-variables"}
yarn dlx trigger.dev@latest deploy
```

**4. Adding your DATABASE\_URL environment variable to Trigger.dev**

In your Trigger.dev dashboard sidebar click "Environment Variables" , and then the "Add new" button .

![Environment variables page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=af652254781808a35c2bcefd4b61b59f)

You can add values for your local dev environment, staging and prod. in this case we will add the `DATABASE_URL` for the production environment.

![Environment variables
page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=79b5fd91e809cb0c6c9298410922df96)

**5. Running your task**

To test this task, go to the 'test' page in the Trigger.dev dashboard and run the task with the following payload:

```json theme={"theme":"css-variables"}
{
  "name": "<a-name>", // e.g. "John Doe"
  "age": "<an-age>", // e.g. 25
  "email": "<an-email>" // e.g. "john@doe.test"
}
```

Congratulations! You should now see a new completed run, and a new user with the credentials you provided should be added to your database.

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
