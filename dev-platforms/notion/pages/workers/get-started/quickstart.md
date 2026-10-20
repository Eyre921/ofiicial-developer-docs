---
title: "Quickstart"
source: https://developers.notion.com/workers/get-started/quickstart
path: workers/get-started/quickstart
---

Create and deploy your first worker in minutes.

Get up and running with Workers in a few steps.

## Prerequisites

> **Node.js**
>
> Version 22 or higher

> **npm**
>
> Version 10 or higher

## Create your first worker

**1. Install the CLI**

```bash theme={null}
curl -fsSL https://ntn.dev | bash
```

**2. Initialize a new project**

Scaffold a new worker project and enter the directory:

```bash theme={null}
ntn workers new my-worker
cd my-worker
```

**3. Deploy to Notion**

Connect to your Notion workspace and deploy:

```bash theme={null}
ntn workers deploy
```

Follow the prompts to authenticate with your Notion workspace.

**4. Share the worker (optional)**

To let other workspace members use this worker, share it from the [Developer portal](https://www.notion.so/developers/workers). **Can connect** lets members connect the worker to agents, and **Full access** lets them manage, edit, and deploy it. See [sharing workers](/workers/guides/sharing-workers) for more details.

**5. Run the sample tool**

Execute the included sample tool:

```bash theme={null}
ntn workers exec sayHello -d '{"name": "World"}'
```

## What's in a worker?

The scaffolded project lives in `src/index.ts` and exports a single `Worker` instance:

```typescript src/index.ts theme={null}
import { Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

worker.tool("sayHello", {
  title: "Say Hello",
  description: "Returns a friendly greeting",
  schema: {
    type: "object",
    properties: {
      name: { type: "string" },
    },
    required: ["name"],
    additionalProperties: false,
  },
  execute: ({ name }) => `Hello, ${name}!`,
});
```

## Next steps

> **[Syncs](/workers/guides/syncs)**
>
> Sync external data into Notion databases.

> **[Agent tools](/workers/guides/tools)**
>
> Build custom tools for Notion AI.

> **[Webhooks](/workers/guides/webhooks)**
>
> Receive HTTP events from external services.

> **[OAuth](/workers/guides/oauth)**
>
> Connect to third-party APIs.
