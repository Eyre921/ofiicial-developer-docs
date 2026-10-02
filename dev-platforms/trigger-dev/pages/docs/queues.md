---
title: "Queues"
source: https://trigger.dev/docs/queues
path: docs/queues
---

Control the order your runs execute in.

When you trigger a task, it isn't executed immediately. Instead, the task [run](/docs/runs) is placed into a queue for execution. Runs in a queue are started in the order they were triggered, first in, first out, unless you give a run a [priority](#priority) at trigger time.

By default, each task gets its own queue, so triggering the same task ten times executes those runs in trigger order. How many of them execute *at once* is a separate question, governed by [concurrency](/docs/concurrency) — your environment's concurrency limit, plus any limits you set on the task.

## Sharing a queue between tasks

Declare a queue with `queue()` and set it on several tasks to interleave their runs in one queue. Runs from every task on the queue start in the order they were triggered, whichever task they belong to:

```ts /trigger/emails.ts theme={"theme":"css-variables"}
import { queue, task } from "@trigger.dev/sdk";

const emailQueue = queue({ name: "emails" });

export const sendWelcomeEmail = task({
  id: "send-welcome-email",
  queue: emailQueue,
  run: async (payload) => {
    //...
  },
});

export const sendDigestEmail = task({
  id: "send-digest-email",
  queue: emailQueue,
  run: async (payload) => {
    //...
  },
});
```

<Note>
  If what you want to share is a concurrency cap rather than ordering, you don't need a shared
  queue: declare a named limit with `concurrencyLimit()` and each task keeps its own queue while
  drawing from the shared limit. See [sharing a limit between
  tasks](/docs/concurrency#sharing-a-limit-between-tasks).
</Note>

Queue names can use letters, numbers, underscores, hyphens and slashes, up to 128 characters. Names starting with `limit/` are reserved for [concurrency limits](/docs/concurrency) and are rejected at deploy time.

## Setting the queue when you trigger a run

When you trigger a task you can override its queue by name. This is really useful if you sometimes have high priority runs:

```ts /trigger/override-queue.ts theme={"theme":"css-variables"}
import { queue, task } from "@trigger.dev/sdk";

const paidQueue = queue({ name: "paid-users" });

export const generatePullRequest = task({
  id: "generate-pull-request",
  // normally this task is limited to 1 run at a time
  concurrency: { total: 1 },
  run: async (payload) => {
    //todo generate a PR using OpenAI
  },
});
```

Triggering from your backend and overriding the queue:

```ts app/api/push/route.ts theme={"theme":"css-variables"}
import { generatePullRequest } from "~/trigger/override-queue";

export async function POST(request: Request) {
  const data = await request.json();

  if (data.branch === "main") {
    //trigger the task, with the paid users queue
    const handle = await generatePullRequest.trigger(data, {
      // Set the paid users queue
      queue: "paid-users",
    });

    return Response.json(handle);
  } else {
    //triggered with the default queue
    const handle = await generatePullRequest.trigger(data);
    return Response.json(handle);
  }
}
```

## Priority

You can re-order runs within a queue at trigger time by giving them a priority:

You can set a priority when you trigger a run. This allows you to prioritize some of your runs over others, so they are started sooner. This is very useful when:

* You have critical work that needs to start more quickly (and you have long queues).
* You want runs for your premium users to take priority over free users.

The value for priority is a time offset in seconds that determines the order of dequeuing.

<img alt="Priority runs" />

If you specify a priority of `10` the run will dequeue before runs that were triggered with no priority 8 seconds ago, like in this example:

```ts theme={"theme":"css-variables"}
// no priority = 0
await myTask.trigger({ foo: "bar" });

//... imagine 8s pass by

// this run will start before the run above that was triggered 8s ago (with no priority)
await myTask.trigger({ foo: "bar" }, { priority: 10 });
```

If you passed a value of `3600` the run would dequeue before runs that were triggered an hour ago (with no priority).

<Note>
  Setting a high priority will not allow you to beat runs from other organizations. It will only
  affect the order of your own runs.
</Note>

## Archiving queues

Queues are created when you deploy, so renaming a queue or deleting a task leaves its old queue behind. To tidy up the list, open the queue's menu on the Concurrency page in the dashboard and choose **Archive**.

Archiving only hides the queue in the dashboard, and it doesn't affect runs. Archived queues don't count towards the **Allocated** total, even if they have runs. To see them, turn on the **Show archived** toggle; to bring one back, choose **Unarchive** from its menu.

* You can only archive a queue that your current deployment no longer declares.
* You can't archive a queue while it has runs waiting or in progress, or while it's paused or its concurrency limit or [`total` limit](/docs/concurrency) is 0.
* If an archived queue gets new runs, it stays hidden, but a warning above the list names it until it's empty.
* Pausing an archived queue, or setting its concurrency limit or `total` limit to 0 (including by resetting an override), unarchives it.
* If a later deploy declares the queue again, it's unarchived automatically.
* The SDK and API still list archived queues.

<Note>
  Some runs belong to a queue without currently sitting in it, so they don't count as activity:
  delayed runs that haven't reached their start time yet, runs waiting for a deploy of their
  version, runs that are waiting (for example on `wait.for` or a child task) or have been
  checkpointed, and, depending on how the engine is configured, runs with a concurrency key that
  have been handed to a worker but not picked up yet. A queue with only runs like these can be
  archived, and the warning won't name it until one of them is back in the queue or running. These
  runs still execute normally and always show on the Runs page.
</Note>

## Managing queues with the SDK

The SDK provides a `queues` namespace that allows you to manage queues programmatically. You can list, retrieve, pause, resume, and modify concurrency limits for queues.

<Note>
  Import from `@trigger.dev/sdk`:

  ```ts theme={"theme":"css-variables"}
  import { queues } from "@trigger.dev/sdk";
  ```
</Note>

### Listing queues

You can list all queues in your environment with pagination support:

```ts theme={"theme":"css-variables"}
import { queues } from "@trigger.dev/sdk";

// List all queues (returns paginated results)
const allQueues = await queues.list();

// With pagination options
const pagedQueues = await queues.list({
  page: 1,
  perPage: 20,
});
```

### Retrieving a queue

You can retrieve a specific queue by its ID, or by its type and name:

```ts theme={"theme":"css-variables"}
import { queues } from "@trigger.dev/sdk";

// Using queue ID (starts with "queue_")
const queueById = await queues.retrieve("queue_1234");

// Using type and name for a task's default queue
const taskQueue = await queues.retrieve({
  type: "task",
  name: "my-task-id",
});

// Using type and name for a custom queue
const customQueue = await queues.retrieve({
  type: "custom",
  name: "my-custom-queue",
});
```

The queue object contains useful information about the queue state, and its `version` discriminates the shape:

```ts theme={"theme":"css-variables"}
// V1: the queue carries its own concurrency limit and override state
{
  id: "queue_1234",       // Queue ID
  name: "my-task-id",     // Queue name
  type: "task",           // "task" or "custom"
  version: "V1",
  running: 5,             // Currently executing runs
  queued: 10,             // Runs waiting to execute
  paused: false,          // Whether the queue is paused
  concurrencyLimit: 10,   // The queue's own limit
  concurrency: {
    current: 10,          // Effective limit
    base: 10,             // Default limit from code
    override: null,       // Override value (if set)
    overriddenAt: null,   // When override was applied
    overriddenBy: null,   // Who applied the override
  }
}

// V2: the queue is only the line runs wait in. Concurrency is declared with
// the task `concurrency` option and managed through `concurrencyLimits`.
{
  id: "queue_5678",
  name: "my-v2-task-id",
  type: "task",
  version: "V2",
  running: 3,
  queued: 12,
  paused: false,
  concurrencyLimit: null,
}
```

### Pausing and resuming queues

You can pause a queue to prevent new runs from starting. Runs that are currently executing will continue to completion.

```ts theme={"theme":"css-variables"}
import { queues } from "@trigger.dev/sdk";

// Pause a queue using its ID
await queues.pause("queue_1234");

// Or using type and name
await queues.pause({ type: "task", name: "my-task-id" });
await queues.pause({ type: "custom", name: "my-custom-queue" });
```

To resume a paused queue and allow new runs to start:

```ts theme={"theme":"css-variables"}
import { queues } from "@trigger.dev/sdk";

// Resume a queue using its ID
await queues.resume("queue_1234");

// Or using type and name
await queues.resume({ type: "task", name: "my-task-id" });
await queues.resume({ type: "custom", name: "my-custom-queue" });
```

### Overriding concurrency limits

<Warning>
  `queues.overrideConcurrencyLimit` and `queues.resetConcurrencyLimit` are deprecated and only work
  for queues on the legacy model, where the queue carried its own concurrency limit. On the current
  model, declare concurrency with the task `concurrency` option and manage it through
  [`concurrencyLimits`](/docs/concurrency), e.g. `concurrencyLimits.override("task/my-task", { total: 10 })`
  and `concurrencyLimits.reset("task/my-task")`. A legacy limit on a queue used with
  `concurrencyKey` maps to `perKey` rather than `total`, and a limit on a custom queue shared by
  several tasks maps to a named limit declared with `concurrencyLimit()`, again using `perKey`
  when the queue receives keyed runs.
</Warning>

You can temporarily override a queue's concurrency limit. This is useful for scaling up or down based on demand:

```ts theme={"theme":"css-variables"}
import { queues } from "@trigger.dev/sdk";

// Set concurrency limit to 5
await queues.overrideConcurrencyLimit("queue_1234", 5);

// Or using type and name
await queues.overrideConcurrencyLimit({ type: "task", name: "my-task-id" }, 20);
```

To reset the concurrency limit back to the base value defined in your code:

```ts theme={"theme":"css-variables"}
import { queues } from "@trigger.dev/sdk";

// Reset concurrency limit to the base value
await queues.resetConcurrencyLimit("queue_1234");

// Or using type and name
await queues.resetConcurrencyLimit({ type: "task", name: "my-task-id" });
```

Overrides survive deploys: redeploying your code keeps an active override until you reset it.
