---
title: "What are Notion Workers?"
source: https://developers.notion.com/workers/get-started/overview
path: workers/get-started/overview
---

Learn what Notion Workers are, what you can build with them, and how they fit into Notion.

Notion Workers are small Node/TypeScript programs that extend Notion. You write code, deploy it with the [Notion CLI](/cli/get-started/overview), and Notion hosts and runs it for you. No servers to manage.

With Workers, you can:

* **Sync external data** into [Notion databases](/guides/data-apis/working-with-databases) on a schedule.
* **Give Notion AI new tools** that your [Custom Agents](https://www.notion.com/help/custom-agents) can call.
* **Receive webhooks** from external services like GitHub, Stripe, or Zendesk.

Workers are designed to be built with AI coding agents. Scaffold a project, describe what you want, and deploy.

## What you can build

> **[Sync data](/workers/guides/syncs)**
>
> Pull data from Salesforce, Stripe, GitHub, or any API into Notion databases — kept in sync automatically.

> **[Agent tools](/workers/guides/tools)**
>
> Give Notion Custom Agents functions like "create a Jira ticket" or "look up a customer in our CRM."

> **[Webhooks](/workers/guides/webhooks)**
>
> Receive HTTP events from GitHub pushes, Stripe payments, or any service that sends webhooks.

## How it works

A worker is a single TypeScript file that exports a `Worker` instance. You register **capabilities** on it (syncs, tools, webhooks) and deploy with `ntn workers deploy`:

```typescript src/index.ts theme={null}
import { Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

// Register capabilities on the worker
worker.tool("sayHello", { /* ... */ });
worker.sync("customersSync", { /* ... */ });
worker.webhook("onGithubPush", { /* ... */ });
```

Once deployed, Notion takes over:

* **Syncs** run on a schedule (default every 30 minutes) and write results to Notion databases.
* **Tools** appear in Notion Custom Agents and are called by Custom Agents on demand.
* **Webhooks** receive HTTP events from external services and run your handler asynchronously.

Your code runs in a sandboxed Node.js environment. You can make HTTP requests to external APIs, [use secrets](/workers/guides/secrets) stored via the CLI, and authenticate with third-party services through [OAuth](/workers/guides/oauth).

| Concept | What it does |
| :- | :- |
| **Worker** | The container for your code. One worker per project. |
| **Capability** | Something the worker can do, i.e. a sync, tool, or webhook. A worker can have one or more capabilities. |
| **Database** | A Notion database managed by a sync. You define its schema in code. |
| **Pacer** | Rate-limits outbound API calls so you don't hit third-party quotas. |
| **OAuth** | Handles authorization flows for services like GitHub and Google. |
| **Secrets** | Environment variables stored securely and injected at runtime. |

## Typical workflow

**1. Scaffold a project**

```bash theme={null}
ntn workers new my-worker
cd my-worker
```

This creates a new directory with a `src/index.ts` starter file, TypeScript config, and dependencies.

**2. Write your capabilities**

Add syncs, tools, or webhooks to `src/index.ts`. Use an AI coding agent to help. The template includes prompts and skills, like the `/sync` skill.

**3. Deploy**

```bash theme={null}
ntn workers deploy
```

The CLI bundles your code, uploads it to Notion, and starts running your capabilities.

**4. Iterate**

Edit your code and redeploy.

## Next steps

> **[Quickstart](/workers/get-started/quickstart)**
>
> Create and deploy your first worker in less than five minutes.

> **[CLI reference](/cli/get-started/overview)**
>
> Install and configure the Notion CLI.

> **[Limits](/workers/reference/limits)**
>
> Rate limits for runs, webhooks, and sync database writes.
