---
title: "Replaying"
source: https://trigger.dev/docs/replaying
path: docs/replaying
---

A replay is a copy of a run with the same payload but against the latest version in that environment. This is useful if something went wrong and you want to try again with the latest version of your code.

### Replaying from the UI

<Tabs>
  <Tab title="From a run">
    <Steps>
      <Step title="Click the Replay button in the top right">
        <img
          alt="Select a task, then in the bottom right
click &#x22;Replay&#x22;"
        />
      </Step>

      <Step title="Confirm replay settings">
        You can edit the payload <Icon icon="circle-1" /> (if available) and choose the environment <Icon icon="circle-2" /> to replay the run in.

        <img
          alt="Select a task, then in the bottom right
click &#x22;Replay&#x22;"
        />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Runs list">
    <Steps>
      <Step title="Click the action button on a run">
        <img alt="On the runs page, press the triple dot button" />
      </Step>

      <Step title="Click replay">
        <img alt="Click replay" />
      </Step>
    </Steps>
  </Tab>
</Tabs>

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

```ts theme={"theme":"css-variables"}
const replayedRun = await runs.replay(run.id);
```

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
