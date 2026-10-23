---
title: "Context"
source: https://trigger.dev/docs/context
path: docs/context
---

Get the context of a task run.

Context (`ctx`) is a way to get information about a run.

> [!NOTE]
>
> The context object does not change whilst your code is executing. This means values like
> `ctx.run.durationMs` will be fixed at the moment the `run()` function is called.

```typescript Context example theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const parentTask = task({
  id: "parent-task",
  run: async (payload: { message: string }, { ctx }) => {
    if (ctx.environment.type === "DEVELOPMENT") {
      return;
    }
  },
});
```

## Context properties

**task** `object`

**properties**

**exportName** `string`

The exported function name of the task e.g. `myTask` if you defined it like this: `export
            const myTask = task(...)`.

**id** `string`

The ID of the task.

**filePath** `string`

The file path of the task.

**attempt** `object`

**properties**

**id** `string`

The ID of the execution attempt.

**number** `number`

The attempt number.

**startedAt** `date`

The start time of the attempt.

**backgroundWorkerId** `string`

The ID of the background worker.

**backgroundWorkerTaskId** `string`

The ID of the background worker task.

**status** `string`

The current status of the attempt.

**run** `object`

**properties**

**id** `string`

The ID of the task run.

**context** `any`

The context of the task run.

**tags** `array`

An array of [tags](/docs/tags) associated with the task run.

**isTest** `boolean`

Whether this is a [test run](/docs/run-tests).

**isReplay** `boolean`

Whether this run is a [replay](/docs/replaying) of a previous run.

**createdAt** `date`

The creation time of the task run.

**startedAt** `date`

The start time of the task run.

**idempotencyKey** `string`

An optional [idempotency key](/docs/idempotency) for the task run.

**maxAttempts** `number`

The [maximum number of attempts](/docs/triggering#maxattempts) allowed for this task run.

**durationMs** `number`

The duration of the task run in milliseconds when the `run()` function is called. For live
values use the [usage SDK functions](/docs/run-usage).

**costInCents** `number`

The cost of the task run in cents when the `run()` function is called. For live values use the
[usage SDK functions](/docs/run-usage).

**baseCostInCents** `number`

The base cost of the task run in cents when the `run()` function is called. For live values
use the [usage SDK functions](/docs/run-usage).

**version** `string`

The [version](/docs/versioning) of the task run.

**maxDuration** `number`

The [maximum allowed duration](/docs/runs/max-duration) for the task run.

**queue** `object`

**properties**

**id** `string`

The ID of the queue.

**name** `string`

The name of the queue.

**environment** `object`

**properties**

**id** `string`

The ID of the environment.

**slug** `string`

The slug of the environment.

**type** `string`

The type of the environment (PRODUCTION, STAGING, DEVELOPMENT, or PREVIEW).

**branchName** `string`

If the environment is `PREVIEW` then this will be the branch name.

**git** `object`

**properties**

**commitAuthorName** `string`

The name of the commit author.

**commitMessage** `string`

The message of the commit.

**commitRef** `string`

The ref of the commit.

**commitSha** `string`

The SHA of the commit.

**dirty** `boolean`

Whether the commit is dirty, i.e. there are uncommitted changes.

**remoteUrl** `string`

The remote URL of the repository.

**pullRequestNumber** `number`

The number of the pull request.

**pullRequestTitle** `string`

The title of the pull request.

**pullRequestState** `string`

The state of the pull request (open, closed, or merged).

**organization** `object`

**properties**

**id** `string`

The ID of the organization.

**slug** `string`

The slug of the organization.

**name** `string`

The name of the organization.

**project** `object`

**properties**

**id** `string`

The ID of the project.

**ref** `string`

The reference of the project.

**slug** `string`

The slug of the project.

**name** `string`

The name of the project.

**batch** `object`

Optional information about the batch, if applicable.

**properties**

**id** `string`

The ID of the batch.

**machine** `object`

Optional information about the machine preset used for execution.

**properties**

**name** `string`

The name of the machine preset.

**cpu** `number`

The CPU allocation for the machine.

**memory** `number`

The memory allocation for the machine.

**centsPerMs** `number`

The cost in cents per millisecond for this machine preset.
