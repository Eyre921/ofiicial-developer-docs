---
title: "Overview"
source: https://upstash.com/docs/workflow/basics/client
path: docs/workflow/basics/client
---

The Workflow Client lets you programmatically interact with your workflow runs.
You can use it from the same application that hosts your workflows, or from any external service.

## Initialization

Initialize a new client with your credentials:

```javascript
import { Client } from "@upstash/workflow"

const client = new Client({
  baseUrl: process.env.QSTASH_URL!,
  token: process.env.QSTASH_TOKEN!
})
```

The client is lightweight and stateless. You can safely reuse a single instance across your application.

## Functionality

The client exposes a set of functions to manage workflow runs and inspect their state:

* [client.trigger](/docs/workflow/basics/client/trigger)
* [client.cancel](/docs/workflow/basics/client/cancel)
* [client.notify](/docs/workflow/basics/client/notify)
* [client.logs](/docs/workflow/basics/client/logs)
* [client.getWaiters](/docs/workflow/basics/client/waiters)
* client.dlq
    * [client.dlq.list](/docs/workflow/basics/client/dlq/list)
    * [client.dlq.restart](/docs/workflow/basics/client/dlq/restart)
    * [client.dlq.resume](/docs/workflow/basics/client/dlq/resume)
    * [client.dlq.delete](/docs/workflow/basics/client/dlq/delete)
    * [client.dlq.retryFailureFunction](/docs/workflow/basics/client/dlq/callback)
