---
title: "Node.js setup guide"
source: https://trigger.dev/docs/guides/frameworks/nodejs
path: docs/guides/frameworks/nodejs
---

This guide will show you how to setup Trigger.dev in your existing Node.js project, test an example task, and view the run.

## Prerequisites

* Setup a project in Node.js
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
