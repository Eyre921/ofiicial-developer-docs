---
title: "Async Workloads Lifecycle"
source: https://docs.netlify.com/build/async-workloads/lifecycle.md
path: build/async-workloads/lifecycle
---

---
title: "Lifecycle of Async Workloads"
description: "The lifecycle of Async Workloads to handle asynchronous, durable, event-based workflows, while ensuring system resilience and scalability."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

As an asynchronous, durable, and event-based architecture, the lifecycle of Async Workloads has more considerations than a single client/server transaction. This page will cover the lifecycle of Async Workloads. Generally, this isn't information you need to use Async Workloads effectively but it can be important for some application design considerations.

## Guarantees

The default nature of Async Workloads is that events are immediately processed or they are enqueued if they are scheduled for the future. The queue strategy is "first in, first out " (FIFO) - meaning it will pick up scheduled work based on the order it is enqueued.

[Priorities](/build/async-workloads/sending-events#prioritized-events) can be assigned to the event upon sending it. The default priority for all events is `0` and an event can be assigned a value between `-50` and `+50`, where the higher the number is, the higher the priority. In the event that two events are scheduled for the same time, the higher priority event will be sent first.

You can decide to use FIFO, explicit priorities, or mix them. If you need more than one Async Workload system to have different queue strategies, we recommend creating separate Netlify sites with Async Workloads that have different strategies applied to them.

Event data and states are persisted so that the events will automatically continue processing after unexpected issues are resolved.

When it comes to throughput for non-scheduled events, the Netlify serverless platform does not put a hard limit on the number of events that can be processed concurrently. It can scale to handle thousands of events concurrently.

The throughput for scheduled events has autoscaling capable of handling tens of thousands of events routing concurrently. There is no hard limit, the system will attempt to handle as many events as possible for each [scheduler interval](/build/async-workloads/optional-configuration#scheduler-polling-interval).

## Retries

Retries are the attempts to call a specific workload function again after it was unsuccessful with the initial attempt.

The default number of retries is `4`. In total, with the initial attempt plus the number of retries, the total number of attempts for a workload is `5` by default. The max retries and backoff schedule can be [configured](/build/async-workloads/writing-workloads#maxRetries) per workload.

**When do retries happen?** If a workload function throws an error, has a timeout, or rejects a returned promise. A retry will be attempted if there are remaining retries attempts and the thrown error was not a [ErrorDoNotRetry](/build/async-workloads/writing-workloads#ErrorDoNotRetry) type.

## Failures

When a workload function fails to process an event that it subscribes to and all retry attempts have also failed, it will be moved into the dead-letter state. This event will stay there for a retention period and then be deleted. During this retention period, a team can inspect, modify, and/or retry these events.

The default retention period for dead letters is 30 days after it was enqueued. After 30 days, the events will be automatically deleted.

You can inspect the events in the project's 
### NavigationPath Component:

Blobs
 store under `async-workloads-state-dead-lettered/*`

To retry these events, use the [management API](/build/async-workloads/lifecycle#management-apis) to target the events you want to re-trigger.

## Management APIs

In addition to the functions and state that Async Workloads adds to your site for the internal logic, it also provides an API for your systems to have programmatic access to managing events. The API comes in the form of JSON endpoints and as Async Workload events. These internal events can be sent by your system and Async Workloads will process them.

When using the API endpoints, the `AWL_API_KEY` must be sent in an `Authorization` header.

### Deleting Events

Kicks off an internal Async Workload to delete events by the criteria provided.

The API accepts `eventIds` and/or `states` to filter which events to delete.
 - `eventIds` is an array of event IDs to delete.
 - `states` is an array of states; events with matching states will be deleted.

### Tabs Component:

<TabItem label="Fetch API">
```js
fetch('SITE_ORIGIN/.netlify/functions/async-workloads-api/events', {
  headers: {
    'Authorization': 'Bearer AWL_API_KEY'
  }
  method: 'DELETE',
  body: JSON.stringify({ eventIds: [], states: [] })
})
```
</TabItem>

<TabItem label="curl">
```bash
curl --header "Authorization: Bearer AWL_API_KEY" \
  --request 'DELETE' \
  --data '{ "eventIds": [], "states": [] }' \
  'SITE_ORIGIN/.netlify/functions/async-workloads-api/events'
```
</TabItem>

<TabItem label="Internal Event">
```js
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient();
await client.send('awl:delete-events', {
	data: {
		eventIds: [],
    states: []
	}
});
```
</TabItem>

Available states to filter by:
  - `processing` - events that are currently being processed by a workload function
  - `pending` - events that are about to be processed by a workload function
  - `delayed` - events that are scheduled to be processed by a workload function in the near future
  - `hibernating` - events that are scheduled to be processed by a workload function in the future (24 hours or more from now)
  - `dead-lettered` - events that have failed to process and have been moved to the dead-letter state

### Retrying Failed Events

Kicks off an internal Async Workload to retry events that are failed/dead-lettered by the criteria provided.

The API accepts `eventIds` or `eventNames` to be passed to filter which events to retry.
 - `eventIds` is an array of event IDs to retry.
 - `eventNames` is an array of event names to retry.

If neither `eventIds` or `eventNames` are provided, then all failed events will be retried.

### Tabs Component:

<TabItem label="Fetch API">
```js
fetch('SITE_ORIGIN/.netlify/functions/async-workloads-api/failed-events', {
  headers: {
    'Authorization': 'Bearer AWL_API_KEY'
  }
  method: 'POST',
  body: JSON.stringify({ eventIds: [] })
})
```
</TabItem>

<TabItem label="curl">
```bash
curl --header "Authorization: Bearer AWL_API_KEY" \
  --request 'POST' \
  --data '{ "eventIds": [] }' \
  'SITE_ORIGIN/.netlify/functions/async-workloads-api/failed-events'
```
</TabItem>

<TabItem label="Internal Event">
```js
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient();
await client.send('awl:retry-failed-events', {
	data: {
		eventIds: [],
    eventNames: [],
	}
});
```
</TabItem>

## Local and branch lifecycle

In production deploy contexts, the Async Workload schedule runs continuously based on the scheduler interval. In non-production deploy contexts (dev, branch deploys, etc.), the Async Workload scheduler runs only on "stateful" actions (for example, processing or retrying events). This prevents unnecessary compute usage on environments that do not serve production traffic. Once triggered, the scheduler runs briefly and exits. This behavior cannot be disabled.

## Event data storage

Event data, persisted results, etc. are stored exclusively as [Blobs](/build/data-and-storage/netlify-blobs/) on the site that hosts the Async Workloads. The data stored there is allowed to be sensitive data. To keep your data secure, Netlify encrypts blobs at rest and in transit. This data can only be accessed through your own site. You are responsible for making sure the code you use to access blobs or Async Workload data doesn't allow data to leak.

