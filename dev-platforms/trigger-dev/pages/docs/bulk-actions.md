---
title: "Bulk actions in the dashboard"
source: https://trigger.dev/docs/bulk-actions
path: docs/bulk-actions
---

Replay or cancel multiple runs from the dashboard using filters or selected run IDs.

**Bulk actions let you replay or cancel multiple runs asynchronously from the dashboard.**

Use bulk actions when you need to retry failed runs after deploying a fix, or stop a group of queued or executing runs.

> [!NOTE]
>
> For backend code, see [Bulk actions with the SDK](/docs/runs/bulk-actions).

<video />

## Create a bulk action in the dashboard

**1. Open the bulk action panel**

Open the runs page and click **Bulk action** in the top right.

![Open the bulk action panel from the runs page](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/bulk-action-open-panel.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=e514c6b6e2c85aa8dc9bbb2cc6604f21)

**2. Choose the runs**

Filter the runs table to target a group of runs, or select individual runs from the table.

**3. Configure the action**

Choose **Replay** or **Cancel**, add an optional name, then confirm the action.

![Configure and create a bulk action](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/bulk-action-create.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=defba18d2817528b5cbbfbdac1b01552)

**4. Track progress**

Open the bulk action page to see progress, view affected runs, or replay the action.

![View bulk action progress](https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/bulk-action-page.png?fit=max\&auto=format\&n=uys6iMwf9B_ojh8r\&q=85\&s=a796b724494a8c0cce3883d2befc5b46)

> [!NOTE]
>
> You can only cancel runs that are still cancelable, such as queued or executing runs. Runs that have already reached a final state cannot be canceled.

## Create a bulk action from the SDK

Use `runs.bulk.replay()` or `runs.bulk.cancel()` when you want to create a bulk action from your backend code.

```ts Your backend code theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

const action = await runs.bulk.replay({
  filter: {
    status: "FAILED",
    taskIdentifier: "sync-customer",
    period: "24h",
  },
  name: "Replay failed customer syncs",
});

const completed = await runs.bulk.poll(action.id);
console.log(completed.status, completed.counts);
```

See [Bulk actions with the SDK](/docs/runs/bulk-actions) for canceling, listing, polling, and aborting bulk actions from your backend code.
