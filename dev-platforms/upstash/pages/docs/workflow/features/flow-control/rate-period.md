---
title: "Rate and Period"
source: https://upstash.com/docs/workflow/features/flow-control/rate-period
path: docs/workflow/features/flow-control/rate-period
---

The rate specifies the maximum number of requests allowed in a given period (time window).

```typescript Configure Retry Attempt Count
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  flowControl: {
    key: "user-signup",
    rate: 10,
    period: 100,
  }
})
```

**Example**:
If `rate = 2` and `period = 1 minute`, then **a maximum of 2 steps** can be executed per minute.

The first 2 requests within the minute are executed immediately:

  <img />

The 3rd request in the same minute is not executed immediately:

  <img />

Instead of rejecting it, Workflow schedules the request in the next available time window:

  <img />

Note that step executions may take longer than the defined period.
The rate limit only controls how many steps are **started** within each time window,
it does not limit their execution duration.
