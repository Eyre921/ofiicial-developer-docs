---
title: "Sending Events"
source: https://docs.netlify.com/build/async-workloads/sending-events.md
path: build/async-workloads/sending-events
---

---
title: "Sending Async Workload events"
description: "Trigger Async Workload functions using the AsyncWorkloadClient or API to process events immediately or to schedule for the future."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Async Workloads brings a durable, event-based architecture to Netlify functions. This means that workloads are centered around subscribing and broadcasting events. Unlike traditional client/server architecture patterns where a single URL corresponds to a specific function or logic, event-based architectures send events that could trigger many functions, and any function could correspond to many different events. This is why Async Workload functions [subscribe to events by name](/build/async-workloads/writing-workloads#config-events) and why events are [sent by name](/build/async-workloads/sending-events#send-eventName).

### AsyncWorkloadsClient

The most common option for sending events is using the `AsyncWorkloadsClient` library.
To use, ensure you have the `@netlify/async-workloads` library installed.

### Tabs Component:

<TabItem label="npm">
```bash
npm install @netlify/async-workloads
```
</TabItem>

<TabItem label="pnpm">
```bash
pnpm add @netlify/async-workloads
```
</TabItem>

<TabItem label="yarn">
```bash
yarn add @netlify/async-workloads
```
</TabItem>

#### Client usage example

To use the client library, it first needs to be instantiated with any settings and then all of the functions will use these settings in the actions they perform.

```ts
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient();

// sending event with no data
await client.send('EVENT_NAME');

// sending event with data
await client.send('EVENT_NAME', { data: { foo: true } });
```

You can also instantiate the client with options.

```ts
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient({
  baseUrl: 'https://example.com',
  apiKey: '5555-555-555-5555',
});
```

Available client options:

- `baseUrl` - the origin for the site that hosts the Async Workload functions. If the site using this library is the same site that runs the Async Workloads, this field should be omitted. Otherwise, the client needs to know where to send requests to and this parameter is required.
- `apiKey` - the API key used to send requests to the Async Workloads routing layer. If the site using this library is the same site that runs the Async Workloads, this field should be omitted. Otherwise, the client needs to know exactly what the API key is to send authorized requests.

#### Basic events

With an instantiated client, specify the event name and any data needed.

```js
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient();

const { eventId, sendStatus } = await client.send('event.first', {
	data: {
		plan: 'pro',
		id: '1234-abc'
	}
});

// this event is invoked without data
await client.send('event.second')
```

Options for `client.send(eventName, options)`:

- `eventName` (required) - the string name of this event being triggered. This is a case-insensitive field.
- `options.data` (optional) - a JSON serializable value that will be passed along to subscribed Async Workload functions.
- `options.delayUntil` (optional) - when this event should attempt to be fired, up to a maximum of one year from the current time. The value can be the absolute milliseconds of the future date (UTC) or the number of milliseconds to wait relative to now, or an [ms-compatible string](https://www.npmjs.com/package/@lukeed/ms), relative to now.
- `options.priority` (optional) - if this event should be processed before or after other events, specifying the priority informs when Async Workloads should process the event relative to others. Higher priority events are processed first when events are triggered at the same time. Allowed values range from `-50` to `+50`, where the default for all is `0`. This only applies to delayed functions, as all non-delayed events are immediately processed.

The result from `client.send(event, options)` is an object with status and identifying details of the workload.
- `eventId` - the unique identifier of this `client.send()` call.
- `sendStatus` - the status of sending the event to the Async Workloads routing layer. This layer will acknowledge that the event was received or it will mark it as failed. The value will be `"succeeded"` or `"failed"`.

#### Scheduling events

To trigger events to run in the future, the `delayUntil` field on the `client.send()` call accepts a few different patterns to suit different needs.

```js
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient();

await client.send('EVENT_NAME', {
  // or you can use '1w', '7 days', 604_800_000
  delayUntil: '1 week'
});

await client.send('EVENT_NAME', {
  // 5 minutes relative to now
  delayUntil: 1000 * 60 * 5
});

await client.send('EVENT_NAME', {
  // exact UTC time of 30m in the future
  delayUntil: Date.now() + (1000 * 60 * 30)
});
```

This is very handy for use cases such as refreshing oAuth tokens, sending notifications relative to a user timezone, and so much more.

#### Prioritized events

When two or more events are scheduled to run at the same time in the future, it's sometimes important to identify which should happen first. This is where the `priority` field comes in.

```js
import { AsyncWorkloadsClient } from '@netlify/async-workloads'

const client = new AsyncWorkloadsClient();

const user = getUser();

await client.send('EVENT_NAME', {
  priority: user.plan === 'enterprise' ? 25 : 0
});
```

In this example, the logic uses the user's plan field to determine if they should be higher in the ordering. If they are an "enterprise" plan user, then we want this event to run with a higher priority. Unless the event has some reason for delaying (like using the `delayUntil` send option), priorities aren't considered. When events are delayed and the Async Workloads scheduler layer is identifying which delayed work to process first, events with higher priority values will be processed before others that are available at the same time with lower priority values.

### Send using the router API

The router layer for Async Workloads is accessible on sites using Async Workloads extension automatically. Under the hood, this is what the `AsyncWorkloadsClient#send()` method uses. This API gives developers the means to trigger Async Workloads from systems that can't use the `AsyncWorkloadsClient`.

Using the API will require the `AWL_API_KEY` value. When installing the Async Workload extension, this value is automatically set as an Environment Variable on the team (if on a plan that allows this). It can be changed or set on the project configuration as well.

Once you have access to the `AWL_API_KEY` use it within the headers to make requests as follows.

### Tabs Component:

<TabItem label="JavaScript">

```js
await fetch('SITE_ORIGIN/.netlify/functions/async-workloads-router?events=EVENT_NAME', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer AWL_API_KEY'
  },
  body: JSON.stringify({
    eventName: 'EVENT_NAME',
    data: { foo: true }
  })
})

```
</TabItem>

<TabItem label="curl">

```bash
curl --header "Content-Type: application/json" \
  --header "Authorization: Bearer AWL_API_KEY" \
  --request 'POST' \
  --data '{"eventName":"EVENT_NAME","data":{"foo":true}}' \
  'SITE_ORIGIN/.netlify/functions/async-workloads-router?events=EVENT_NAME'
```
</TabItem>

This API method accepts a JSON body with a single event or an array of events in the contents. The options for the events are the same as the `options` argument to the [`client.send(eventName, options)`](/build/async-workloads/sending-events#basic-events) with one addition. The `eventName` should be in the `options` object as well. For example, `client.send('event-a', { delayUntil '1 day' })` would have a corresponding API body of `{"eventName": "event-a", "delayUntil": "1 day"}`.

