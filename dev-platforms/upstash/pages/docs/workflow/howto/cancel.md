---
title: "Cancel a Run"
source: https://upstash.com/docs/workflow/howto/cancel
path: docs/workflow/howto/cancel
---

You can cancel a running workflow both programatically and from your Upstash Workflow console.

## Cancelling via console

In your Upstash Workflow console, find the run you'd like to cancel and press the `Cancel Workflow` button on the right side:

  <img alt="Cancel a workflow run in the Upstash Console" />

## Cancelling in bulk

To cancel many runs at once, filter the `Logs` tab down to the runs you want
and pick **Cancel** from the **Bulk actions** menu. QStash cancels every running
workflow that matches the filters in the background.

The **History** button next to the menu lists each bulk cancellation with its
state, the filters used and the number of runs cancelled, so you can follow an
operation while it runs or look it up later by its action ID. The same is
available through the [bulk cancel workflow runs](/docs/workflow/api-reference/runs/bulk-cancel-workflow-runs)
endpoint with `"async": true`, and the
[bulk actions](/docs/workflow/api-reference/bulk-actions/list-bulk-actions) endpoints.

  <img alt="Bulk action history panel in the Upstash Console" />

## Cancelling programatically

<Note>
  This feature is not yet available in
  [workflow-py](https://github.com/upstash/workflow-py). See our
  [Roadmap](/docs/workflow/roadmap) for feature parity plans and
  [Changelog](/docs/workflow/changelog) for updates.
</Note>

```javascript
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.cancel({ ids: "<WORKFLOW_RUN_ID>" });
```

And replace `<WORKFLOW_RUN_ID>` with your actual run ID. See [the documentation of `client.cancel` method for more information about other ways of canceling workflows](/docs/workflow/basics/client/cancel).

You can also use the [Upstash Workflow REST API](/docs/workflow/api-reference/runs/cancel-workflow-run) to cancel a run programatically.
