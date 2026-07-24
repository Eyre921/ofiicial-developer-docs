---
title: "Migrating from v3"
source: https://trigger.dev/docs/migrating-from-v3
path: docs/migrating-from-v3
---

What's new in v4, how to migrate, and breaking changes.

<Warning>
  **Trigger.dev v3 has been retired**

  Trigger.dev v3 is end of life. v4 is stable, fully supported, and recommended for all users.

  * On Trigger.dev Cloud, v3 has been shut down: v3 triggers and deploys no longer run.
  * If you self-host, 4.5.0 is the last version we officially support for running v3. Stay on 4.5.0 or upgrade to v4; 4.5.1 and later reject v3 triggers, batch triggers, and deploys with an upgrade message.

  **What you need to do:** Migrate to v4. The migration takes about 2 minutes; follow the steps below. If you have questions or need help, [contact us](https://trigger.dev/contact) or reach out in our [Discord](https://trigger.dev/discord).
</Warning>

## What's new in v4?

| Feature                                                              | Description                                                                                                                                                                                                |
| :------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Wait for token](/docs/wait-for-token)                                    | Create and wait for tokens to be completed, enabling approval workflows and waiting for arbitrary external conditions.                                                                                     |
| Wait idempotency                                                     | Skip waits if the same idempotency key is used again when using [wait for](/docs/wait-for#wait-idempotency), [wait until](/docs/wait-until#wait-idempotency), or [wait for token](/docs/wait-for-token#wait-idempotency). |
| [Priority](/docs/runs/priority)                                           | Specify a priority when triggering a task.                                                                                                                                                                 |
| [Global lifecycle hooks](/docs/tasks/overview#global-lifecycle-hooks)     | Register global lifecycle hooks that are executed for all runs, regardless of the task.                                                                                                                    |
| [onWait and onResume](/docs/tasks/overview#onwait-and-onresume-functions) | Run code when a run is paused or resumed because of a wait.                                                                                                                                                |
| [onComplete](/docs/tasks/overview#oncomplete-function)                    | Run code when a run completes, regardless of whether it succeeded or failed.                                                                                                                               |
| [onCancel](/docs/tasks/overview#oncancel-function)                        | Run code when a run is cancelled.                                                                                                                                                                          |
| [Hidden tasks](/docs/hidden-tasks)                                        | Create tasks that are not exported from your trigger files but can still be executed.                                                                                                                      |
| [Middleware & locals](#middleware-and-locals)                        | The middleware system runs at the top level, executing before and after all lifecycle hooks. The locals API allows sharing data between middleware and hooks.                                              |
| [useWaitToken](/docs/realtime/react-hooks/use-wait-token)                 | Use the useWaitToken hook to complete a wait token from a React component.                                                                                                                                 |
| [Task-backed AI tools](/docs/tasks/schemaTask#task-backed-ai-tools)       | Use `schemaTask` with AI SDK `tool()` and `ai.toolExecute()` (legacy `ai.tool` is deprecated).                                                                                                             |

## Node.js support

Trigger.dev runs your tasks on specific Node.js versions:

* Node.js `21.7.3` (default)
* Node.js `22.16.0` (`node-22`)
* Node.js `24.18.0` (`node-24`)
* Node.js `26.4.0` (`node-26`)
* Bun `1.3.3` (`bun`)

You can change the runtime by setting the `runtime` field in your `trigger.config.ts` file.

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  // "node", "node-22", "node-24", "node-26" or "bun"
  runtime: "node-24",
  project: "<your-project-ref>",
});
```

## How to migrate to v4

First read the deprecations and breaking changes sections below.

We recommend the following steps to migrate to v4:

1. Install the v4 package.
2. Run the `trigger dev` CLI command and test your tasks locally, fixing any breaking changes.
3. Deploy to the staging environment and test your tasks in staging, fixing any breaking changes. (this step is optional, but highly recommended)
4. Once you've verified that v4 is working as expected, you should deploy your application backend with the updated v4 package.
5. Once you've deployed your application backend, you should deploy your tasks to the production environment.

Note that between steps 4 and 5, runs triggered with the v4 package will continue using v3, and only new runs triggered after step 5 is complete will use v4.

<Warning>
  Once v4 is activated in your environment, there will be a period of time where old runs will
  continue to execute using v3, while new runs will use v4. Because these engines use completely
  different underlying queues and concurrency models, it's possible you may have up to double the
  amount of concurrently executing runs. Once the runs drain from the old run engine, the
  concurrency will return to normal.
</Warning>

<Note>
  When migrating from v3 to v4, our infrastructure IPs may change. If you use IP allowlisting (e.g. for databases or APIs), [update your allowlists](https://trigger.dev/changelog/static-ips) with the current static IPs before or immediately after switching to v4 to avoid connectivity issues or downtime.
</Note>

## Migrate using AI

Use the prompt in the accordion below to help you migrate your v3 tasks to v4. The prompt gives good results when using Claude 4 Sonnet. You’ll need a relatively large token limit.

<Accordion title="Copy paste this prompt in full" icon="sparkles">
  ```md theme={"theme":"css-variables"}

  I would like you to help me migrate my v3 task code to v4. Here are the important differences:

  We've deprecated the `@trigger.dev/sdk/v3` import path and moved to a new path:

  // This is the old path
  import { task } from "@trigger.dev/sdk/v3";

  // This is the new path, use this instead
  import { task } from "@trigger.dev/sdk";

  We've renamed the `handleError` hook to `catchError`. Use this instead of `handleError`.

  `init` was previously used to initialize data used in the run function. This is the old version:

  import { task } from "@trigger.dev/sdk";

  const myTask = task({
    init: async () => {
      return {
        myClient: new MyClient(),
      };
    },
    run: async (payload: any, { ctx, init }) => {
      const client = init.myClient;
      await client.doSomething();
    },
  });

  This is the new version using middleware and locals:

  import { task, locals, tasks } from "@trigger.dev/sdk";

  // Create a local for your client
  const MyClientLocal = locals.create<MyClient>("myClient");

  // Set up middleware to initialize the client
  tasks.middleware("my-client", async ({ next }) => {
    const client = new MyClient();
    locals.set(MyClientLocal, client);
    await next();
  });

  // Helper function to get the client
  function getMyClient() {
    return locals.getOrThrow(MyClientLocal);
  }

  const myTask = task({
    run: async (payload: any, { ctx }) => {
      const client = getMyClient();
      await client.doSomething();
    },
  });

  We’ve deprecated the `toolTask` function. Use `schemaTask` plus AI SDK `tool()` with `execute: ai.toolExecute(task)` (the `ai.tool()` wrapper is deprecated). This is the old version:

  import { toolTask, schemaTask } from "@trigger.dev/sdk";
  import { z } from "zod";
  import { generateText } from "ai";

  const myToolTask = toolTask({
    id: "my-tool-task",
    run: async (payload: any, { ctx }) => {},
  });

  export const myAiTask = schemaTask({
    id: "my-ai-task",
    schema: z.object({
      text: z.string(),
    }),
    run: async (payload, { ctx }) => {
      const { text } = await generateText({
        prompt: payload.text,
        model: openai("gpt-4o"),
        tools: {
          myToolTask,
        },
      });
    },
  });

  This is the new version:

  import { schemaTask } from "@trigger.dev/sdk";
  import { ai } from "@trigger.dev/sdk/ai";
  import { z } from "zod";
  import { generateText, tool } from "ai";
  import { openai } from "@ai-sdk/openai";

  // Convert toolTask to schemaTask with a schema
  const myToolTask = schemaTask({
    id: "my-tool-task",
    schema: z.object({
      // Add appropriate schema for your tool's payload
      input: z.string(),
    }),
    run: async (payload, { ctx }) => {},
  });

  const myTool = tool({
    description: myToolTask.description ?? "",
    inputSchema: myToolTask.schema!,
    execute: ai.toolExecute(myToolTask),
  });

  export const myAiTask = schemaTask({
    id: "my-ai-task",
    schema: z.object({
      text: z.string(),
    }),
    run: async (payload, { ctx }) => {
      const { text } = await generateText({
        prompt: payload.text,
        model: openai("gpt-4o"),
        tools: {
          myTool,
        },
      });
    },
  });

  We've made several breaking changes that require code updates:

  **Queue changes**: Queues must now be defined ahead of time using the `queue` function. You can no longer create queues "on-demand" when triggering tasks. This is the old version:


  // Old v3 way - creating queue on-demand
  await myTask.trigger({ foo: "bar" }, { queue: { name: "my-queue", concurrencyLimit: 10 } });


  This is the new version:


  // New v4 way - define queue first
  import { queue, task } from "@trigger.dev/sdk";

  const myQueue = queue({
    name: "my-queue",
    concurrencyLimit: 10,
  });

  export const myTask = task({
    id: "my-task",
    queue: myQueue, // Set queue on task
    run: async (payload: any, { ctx }) => {},
  });

  // Now trigger without queue options
  await myTask.trigger({ foo: "bar" });

  // Or specify queue by name
  await myTask.trigger({ foo: "bar" }, { queue: "my-queue" });


  **Lifecycle hooks**: Function signatures have changed to use a single object parameter instead of separate parameters. Prefer `onStartAttempt` over the deprecated `onStart` when you need code to run before each attempt. This is the old version:


  // Old v3 way
  export const myTask = task({
    id: "my-task",
    onStart: (payload, { ctx }) => {},
    onSuccess: (payload, output, { ctx }) => {},
    onFailure: (payload, error, { ctx }) => {},
    catchError: (payload, { ctx, error, retry }) => {},
    run: async (payload, { ctx }) => {},
  });


  This is the new version:


  // New v4 way - single object parameter for hooks
  export const myTask = task({
    id: "my-task",
    onStartAttempt: ({ payload, ctx }) => {},  // prefer over deprecated onStart
    onSuccess: ({ payload, ctx, task, output }) => {},
    onFailure: ({ payload, ctx, task, error }) => {},
    catchError: ({ payload, ctx, task, error, retry, retryAt, retryDelayInMs }) => {},
    run: async (payload, { ctx }) => {}, // run function unchanged
  });


  **BatchTrigger changes**: The `batchTrigger` function no longer returns runs directly. This is the old version:


  // Old v3 way
  const batchHandle = await tasks.batchTrigger([
    [myTask, { foo: "bar" }],
    [myOtherTask, { baz: "qux" }],
  ]);

  console.log(batchHandle.runs); // Direct access


  This is the new version:


  // New v4 way
  const batchHandle = await tasks.batchTrigger([
    [myTask, { foo: "bar" }],
    [myOtherTask, { baz: "qux" }],
  ]);

  const batch = await batch.retrieve(batchHandle.batchId); // Use batch.retrieve()
  console.log(batch.runs);


  **triggerAndWait / batchTriggerAndWait**: In v4 these return a Result object, not the raw output. Use `if (result.ok) { ... result.output }` or call `.unwrap()` to get the output (throws if the run failed). Do not wrap `triggerAndWait` or `batchTriggerAndWait` in `Promise.all` — this is not supported.


  **Context (ctx) changes**: `ctx.attempt.id` and `ctx.attempt.status` have been removed; use `ctx.attempt.number` where needed. `ctx.task.exportName` has been removed.


  Can you help me convert the following code from v3 to v4? Please include the full converted code in the answer, do not truncate it anywhere.

  ```
</Accordion>

## Installation

To opt-in to using v4, you will need to update your dependencies to the latest version:

<CodeGroup>
  ```bash npx theme={"theme":"css-variables"}
  npx trigger.dev@latest update
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest update
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest update
  ```
</CodeGroup>

This command should update all of your `@trigger.dev/*` packages to a `4.x` version.

## Deprecations

We've deprecated the following APIs:

### @trigger.dev/sdk/v3

We've deprecated the `@trigger.dev/sdk/v3` import path and moved to a new path:

```ts theme={"theme":"css-variables"}
// This still works, but will be removed in a future version
import { task } from "@trigger.dev/sdk/v3";

// This is the new path
import { task } from "@trigger.dev/sdk";
```

### `handleError` and `init`

We've renamed the `handleError` hook to `catchError` to better reflect that it can catch and react to errors. `handleError` will be removed in a future version.

`init` was previously used to initialize data used in the run function:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

const myTask = task({
  init: async () => {
    return {
      myClient: new MyClient(),
    };
  },
  run: async (payload: any, { ctx, init }) => {
    const client = init.myClient;
    await client.doSomething();
  },
});
```

This has now been deprecated in favor of the `locals` API and middleware. See the [Improved middleware and locals](/docs/tasks/overview#middleware-and-locals-functions) section for more details.

### toolTask

We've deprecated the `toolTask` function, which created both a Trigger.dev task and a tool compatible with the Vercel [AI SDK](https://vercel.com/docs/ai-sdk):

```ts theme={"theme":"css-variables"}
import { toolTask, schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";
import { generateText } from "ai";

const myToolTask = toolTask({
  id: "my-tool-task",
  run: async (payload: any, { ctx }) => {},
});

export const myAiTask = schemaTask({
  id: "my-ai-task",
  schema: z.object({
    text: z.string(),
  }),
  run: async (payload, { ctx }) => {
    const { text } = await generateText({
      prompt: payload.text,
      model: openai("gpt-4o"),
      tools: {
        myToolTask,
      },
    });
  },
});
```

We've replaced the `toolTask` function with `schemaTask` plus AI SDK `tool()` and `ai.toolExecute()` (the older `ai.tool()` wrapper is deprecated). See [Task-backed AI tools](/docs/tasks/schemaTask#task-backed-ai-tools).

## Breaking changes

### Queue changes

Previously, it was possible to specify a queue name of a queue that did not exist, along with a concurrency limit. The queue would then be created "on-demand" with the specified concurrency limit. If the queue did exist, the concurrency limit of the queue would be updated to the specified value:

```ts theme={"theme":"css-variables"}
await myTask.trigger({ foo: "bar" }, { queue: { name: "my-queue", concurrencyLimit: 10 } });
```

This is no longer possible, and queues must now be defined ahead of time using the `queue` function:

```ts theme={"theme":"css-variables"}
import { queue } from "@trigger.dev/sdk";

const myQueue = queue({
  name: "my-queue",
  concurrencyLimit: 10,
});
```

Now when you trigger a task, you can only specify the queue by name:

```ts theme={"theme":"css-variables"}
await myTask.trigger({ foo: "bar" }, { queue: "my-queue" });
```

Or you can set the queue on the task:

```ts theme={"theme":"css-variables"}
import { queue, task } from "@trigger.dev/sdk";

const myQueue = queue({
  name: "my-queue",
  concurrencyLimit: 10,
});

export const myTask = task({
  id: "my-task",
  queue: myQueue,
  run: async (payload: any, { ctx }) => {},
});

// You can optionally specify the queue directly on the task
export const myTask2 = task({
  id: "my-task-2",
  queue: {
    name: "my-queue-2",
    concurrencyLimit: 50,
  },
  run: async (payload: any, { ctx }) => {},
});
```

Now you can trigger these tasks without having to specify the queue name in the trigger options:

```ts theme={"theme":"css-variables"}
await myTask.trigger({ foo: "bar" }); // Will use the queue defined on the task
await myTask2.trigger({ foo: "bar" }); // Will use the queue defined on the task
```

If you're using `concurrencyKey` you can specify the `queue` and `concurrencyKey` like this:

```ts theme={"theme":"css-variables"}
const handle = await generatePullRequest.trigger(data, {
  queue: "paid-users",
  concurrencyKey: data.userId,
});
```

For each unique value of `concurrencyKey`, a new queue will be created using the `concurrencyLimit` from the queue. This allows you to have a queue per user.

### Lifecycle hooks

We've changed the function signatures of the lifecycle hooks to be more consistent and easier to use, by unifying all the parameters into a single object that can be destructured.

Previously, hooks received a payload as the first argument and then an additional object as the second argument:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  onStart: ({ payload, ctx }) => {},
  run: async (payload, { ctx }) => {},
});
```

Now, all the parameters are passed in a single object:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  onStart: ({ payload, ctx }) => {},
  // The run function still uses separate parameters
  run: async (payload, { ctx }) => {},
});
```

This is true for all the lifecycle hooks:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  onStart: ({ payload, ctx, task }) => {},
  onSuccess: ({ payload, ctx, task, output }) => {},
  onFailure: ({ payload, ctx, task, error }) => {},
  onWait: ({ payload, ctx, task, wait }) => {},
  onResume: ({ payload, ctx, task, wait }) => {},
  onComplete: ({ payload, ctx, task, result }) => {},
  catchError: ({ payload, ctx, task, error, retry, retryAt, retryDelayInMs }) => {},
  run: async (payload, { ctx }) => {},
});
```

### Context changes

We've made a few small changes to the `ctx` object:

* `ctx.attempt.id` and `ctx.attempt.status` have been removed. `ctx.attempt.number` is still available.
* `ctx.task.exportName` has been removed (since we no longer require tasks to be exported to be triggered).

### BatchTrigger changes

The `batchTrigger` function no longer returns a `runs` list directly. In v3, you could access the runs directly from the batch handle:

```ts theme={"theme":"css-variables"}
// In v3
const batchHandle = await tasks.batchTrigger([
  [myTask, { foo: "bar" }],
  [myOtherTask, { baz: "qux" }],
]);

// You could access runs directly
console.log(batchHandle.runs);
```

In v4, you now need to use the `batch.retrieve()` method to get the batch with its runs:

```ts theme={"theme":"css-variables"}
// In v4
const batchHandle = await tasks.batchTrigger([
  [myTask, { foo: "bar" }],
  [myOtherTask, { baz: "qux" }],
]);

// Now you need to retrieve the batch to get the runs
const batch = await batch.retrieve(batchHandle.batchId);
console.log(batch.runs);
```

### OpenTelemetry

We are now using newer versions of the OpenTelemetry packages. This means that if you're using custom exporters you may need to update the packages:

| Package                                   | Previous Version | New Version | Change Type  |
| ----------------------------------------- | ---------------- | ----------- | ------------ |
| `@opentelemetry/api-logs`                 | 0.52.1           | 0.203.0     | Major update |
| `@opentelemetry/exporter-logs-otlp-http`  | 0.52.1           | 0.203.0     | Major update |
| `@opentelemetry/exporter-trace-otlp-http` | 0.52.1           | 0.203.0     | Major update |
| `@opentelemetry/instrumentation`          | 0.52.1           | 0.203.0     | Major update |
