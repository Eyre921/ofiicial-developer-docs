---
title: "Cancel a Run"
source: https://upstash.com/docs/workflow/howto/cancel
path: docs/workflow/howto/cancel
---

You can cancel a running workflow both programatically and from your Upstash Workflow console.

## Cancelling via console

In your Upstash Workflow console, find the run you'd like to cancel and press the `Cancel Workflow` button on the right side:

  <img />

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
