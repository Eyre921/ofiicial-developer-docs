---
title: "Quick start: add Trigger.dev to your project"
source: https://trigger.dev/docs/quick-start
path: docs/quick-start
---

Set up Trigger.dev in your existing project in under 3 minutes. Install the SDK, create your first background task, and trigger it from your code.

## Set up with AI

Using an AI coding assistant? Copy this prompt and paste it into Claude Code, Cursor, Copilot, Windsurf, or any AI tool. It'll handle the setup for you.

<Accordion title="Copy the setup prompt">
  ```text theme={"theme":"css-variables"}
  Help me add Trigger.dev to this project.

  ## What to do

  1. I need a Trigger.dev account. If I don't have one, point me to https://cloud.trigger.dev to sign up. Wait for me to confirm.
  2. Run `npx trigger.dev@latest init` in the project root.
     - When it asks about the MCP server, recommend I install it (best DX: gives you direct access to Trigger.dev docs, deploys, and run monitoring).
     - Install the "Hello World" example task when prompted.
  3. Run `npx trigger.dev@latest dev` to start the dev server.
  4. Once the dev server is running, test the example task from the Trigger.dev dashboard.
  5. Set TRIGGER_SECRET_KEY in my .env file (or .env.local for Next.js). I can find it on the API Keys page in the dashboard.
  6. Ask me what framework I'm using and show me how to trigger the task from my backend code.

  If I've already run init and want the MCP server, run: npx trigger.dev@latest install-mcp

  ## Critical rules

  - ALWAYS import from `@trigger.dev/sdk`. NEVER import from `@trigger.dev/sdk/v3`.
  - NEVER use `client.defineJob()` — that's the deprecated v2 API.
  - Use type-only imports when triggering from backend code to avoid bundling task code:

    import type { myTask } from "./trigger/example";
    import { tasks } from "@trigger.dev/sdk";

    const handle = await tasks.trigger<typeof myTask>("hello-world", { message: "Hello from my app!" });

  ## When done, point me to

  - Writing tasks: https://trigger.dev/docs/tasks/overview
  - Real-time updates: https://trigger.dev/docs/realtime/overview
  - AI tooling: https://trigger.dev/docs/building-with-ai
  ```
</Accordion>

## Manual setup

<Steps>
  <Step title="Create a Trigger.dev account">
    Sign up at [Trigger.dev Cloud](https://cloud.trigger.dev) (or [self-host](/docs/self-hosting/overview)). The onboarding flow will guide you through creating your first organization and project.
  </Step>

  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/docs/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/docs/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs, including a link to the dashboard. Open it, find your Example task on the Tasks page, and press the "Test" button to open its test page.

    Most tasks have a "payload" which you enter in the JSON editor, but our example task doesn't need any input. You can also configure run options, pre-populate the form from recent runs, and save run templates.

    Press the "Run test" button.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

## Triggering tasks from your app

The test page in the dashboard is great for verifying your task works. To trigger tasks from your own code, you'll need to set the `TRIGGER_SECRET_KEY` environment variable. Grab it from the API Keys page in the dashboard and add it to your `.env` file.

```bash .env theme={"theme":"css-variables"}
TRIGGER_SECRET_KEY=tr_dev_...
```

See [Triggering](/docs/triggering) for the full guide, or jump straight to framework-specific setup for [Next.js](/docs/guides/frameworks/nextjs), [Remix](/docs/guides/frameworks/remix), or [Node.js](/docs/guides/frameworks/nodejs).

## Next steps

<CardGroup>
  <Card title="Building with AI" icon="brain" href="/docs/building-with-ai">
    Build Trigger.dev projects using AI coding assistants
  </Card>

  <Card title="How to trigger your tasks" icon="bolt" href="/docs/triggering">
    Trigger tasks from your backend code
  </Card>

  <Card title="Writing tasks" icon="wand-magic-sparkles" href="/docs/tasks/overview">
    Task options, lifecycle hooks, retries, and queues
  </Card>

  <Card title="Guides and example projects" icon="books" href="/docs/guides/introduction">
    Framework guides and working example repos
  </Card>
</CardGroup>
