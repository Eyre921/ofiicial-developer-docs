---
title: "Replaying"
source: https://trigger.dev/docs/replaying
path: docs/replaying
---

A replay is a copy of a run with the same payload but against the latest version in that environment. This is useful if something went wrong and you want to try again with the latest version of your code.

### Replaying from the UI

**From a run**

**1. Click the Replay button in the top right**

![Select a task, then in the bottom right
click "Replay"](https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-action.png?fit=max\&auto=format\&n=5SxX7bFjJKRsidSL\&q=85\&s=64e19da4dca5b249adee459a1eeb62e1)

**2. Confirm replay settings**

You can edit the payload  (if available) and choose the environment  to replay the run in.

![Select a task, then in the bottom right
click "Replay"](https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-run-modal.png?fit=max\&auto=format\&n=5SxX7bFjJKRsidSL\&q=85\&s=9891cc5d05792c57d3e58a06171113f4)

**Runs list**

**1. Click the action button on a run**

![On the runs page, press the triple dot button](https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list.png?fit=max\&auto=format\&n=5SxX7bFjJKRsidSL\&q=85\&s=a9dc0c82c7053753ab620237be1fc63d)

**2. Click replay**

![Click replay](https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/replay-runs-list-popover.png?fit=max\&auto=format\&n=5SxX7bFjJKRsidSL\&q=85\&s=41ea417523f3a85b6dfbe0946911ee98)

### Detecting replays in your task

You can check if a run is a replay using the [context](/docs/context) object:

```ts theme={"theme":"css-variables"}
export const myTask = task({
  id: "my-task",
  run: async (payload, { ctx }) => {
    if (ctx.run.isReplay) {
      // This run is a replay of a previous run
    }
  },
});
```

### Replaying using the SDK

You can replay a run using the SDK:

```ts Your backend code theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

const replayedRun = await runs.replay(run.id);
// { id: "run_cmv6ixfn30008ct9kegazjolu" }
```

The new run reuses the original run's payload, metadata, tags, queue, concurrency key, and machine. Pass options to override any of them for the new run:

```ts Your backend code theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

const replayedRun = await runs.replay(run.id, {
  payload: { userId: "user_456" },
  metadata: { source: "replay" },
  tags: ["replayed"],
  machine: "large-1x",
  delay: "10m",
});
```

The options use the same names as [`trigger()` options](/docs/triggering): `payload`, `metadata`, `tags`, `queue`, `concurrencyKey`, `machine`, `version`, `region`, `delay`, `ttl`, `idempotencyKey`, `idempotencyKeyTTL`, `maxAttempts`, `maxDuration`, and `priority`. If you leave out `payload`, `metadata`, `tags`, `queue`, `concurrencyKey`, or `machine`, the new run uses the original run's value. The other options fall back to the task's current defaults, and without `version` the replay runs on the current version. The replay always runs in the same environment as the original run.

A `queue` must already exist in the environment, and a `version` must be a version deployed to it. Otherwise the replay fails with an error and no run is created.

A replay starts a new run, so the API key or token you replay with needs permission to trigger the task as well as write access to the run.

The SDK serializes a `payload` override the same way `trigger()` does, so values like `Date`, `BigInt`, `Map` and `Set` reach the task with their types.

When you call `trigger()` or `batchTrigger()` on a task you receive back a run handle which has an `id` property. You can use that `id` to replay the run.

You can also access the run id from inside a run. You could write this to your database and then replay it later.

```ts theme={"theme":"css-variables"}
export const simpleChildTask = task({
  id: "simple-child-task",
  run: async (payload, { ctx }) => {
    // the run ID (and other useful info) is in ctx
    const runId = ctx.run.id;
  },
});
```

### Bulk replaying

See [Bulk actions](/docs/bulk-actions) for more information.
