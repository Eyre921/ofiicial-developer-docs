---
title: "Writing Async Workloads"
source: https://docs.netlify.com/build/async-workloads/writing-workloads.md
path: build/async-workloads/writing-workloads
---

---
title: "Writing Async Workloads"
description: "Create Async Workloads files in TypeScript and JavaScript. Define how workloads handle retries and errors."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

This page will go deeper into creating Async Workload functions and the different capabilities available with them.

## Installation

Enable the Async Workloads Netlify extension on the team settings. There's no additional, required settings needed after enabling. Once enabled, all sites on the team can build Async Workloads.

Add the `@netlify/async-workloads` module to your project. This will provide the functionality and types for those using Typescript.

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

## Async Workload functions

Start by adding a function file to your project by creating the file in [your functions directory](/build/functions/configuration#directory).

### Tabs Component:

<TabItem label="TypeScript">

```ts
import { asyncWorkloadFn, AsyncWorkloadEvent, AsyncWorkloadConfig } from "@netlify/async-workloads";

export default asyncWorkloadFn((event: AsyncWorkloadEvent) => {

  // logic goes here

});

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: []
};
```
</TabItem>

<TabItem label="JavaScript">

```js
import { asyncWorkloadFn } from "@netlify/async-workloads";

export default asyncWorkloadFn((event) => {

  // logic goes here

});

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: []
};
```
</TabItem>

Async Workload functions are written similarly to serverless functions but the handler is wrapped with the `asyncWorkloadFn` wrapper. This wrapper ensures all of the necessary functionality and types are in place (e.g. ensuring the authentication checks are performed on all workloads automatically).

Async Workloads operates as an event-based architecture so the inputs to the `asyncWorkloadFn` callback will be an event ([`AsyncWorkloadEvent`](/build/async-workloads/writing-workloads#asyncworkloadevent) and the workload will specify the event names that it responds to. When a client sends an event with a name that matches, the workload callback is invoked and the event is passed.

### AsyncWorkloadEvent

`asyncWorkloadFn` is invoked with an event argument of the type `AsyncWorkloadEvent`. On this event we have the following fields and methods:

- `eventName` - name of the event that triggered the workload.
- `eventId` - ID value assigned to this event when triggered.
- `eventData` - data sent as the `data` field in the sent event.
- `attempt` - retry attempt number. This number is `0` on the first invocation of the workload because that isn't a retry attempt.
- `sendEvent(eventName, options)` - an alias to `client.sendEvent()`. Because this method is running within an Async Workload function, it uses the same information (for example, `baseUrl`, `apiKey`, etc.) used to invoke this async workload to establish a client and send events.

- `step` - object that groups all of the step-related functionality. Learn more about [multi-step workloads here](/build/async-workloads/multi-step-workloads).
    - `step.run(stepId, callback)` - used to create a step function for discrete retryable logic. It returns a promise that will resolve to the value returned from the callback function. The returned value should be serializable to JSON. Identifiers must be unique for each step that needs to run within a workload. If a step matches an `id` that has already run, it will have the promise immediately resolve to the same response value. Learn more about [multi-step workloads here](/build/async-workloads/multi-step-workloads).
    - `step.sleep(sleepId, duration)` - used to delay the continuation of logic within a workload. `sleepId` should be unique across all steps and other sleep functions. `duration` can be the relative number of milliseconds to wait, a [ms-compatible string value](https://www.npmjs.com/package/@lukeed/ms), or a UTC milliseconds timestamp value. Relative duration values are relative to the time the workload function was called. Learn more about [workload sleeping here](/build/async-workloads/multi-step-workloads#sleeping).

### AsyncWorkloadConfig

Within the Async Workload function module, an `asyncWorkloadConfig` field must be exported. This is the in code configuration for how the workload should operate. The config must implement the required fields of the `AsyncWorkloadConfig` type defined below.

### Tabs Component:

<TabItem label="TypeScript">

```ts
import type { AsyncWorkloadConfig } from "@netlify/async-workloads";

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: ['event-a', 'event-b'],
};
```
</TabItem>

<TabItem label="JavaScript">

```js
export const asyncWorkloadConfig = {
	events: ['event-a', 'event-b'],
};
```
</TabItem>

The fields and methods that can be defined on `AsyncWorkloadConfig` type are the following:

- `events` (required) - the list of event name strings that this workload function should respond to. The names are case-insensitive.
- `eventFilter` (optional) - a function that will receive the `AsyncWorkloadEvent` event and the router's request context to determine if the event can be handled by this workload. It must return a boolean to determine if the workload should run this function. This is checked on the Async Workload routing layer and will not invoke this function if the event name or this filter does not match or return false.

### Tabs Component:

<TabItem label="TypeScript">

```ts
import type { AsyncWorkloadConfig, AsyncWorkloadEvent } from "@netlify/async-workloads";

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
  events: ['event-a', 'event-b'],
  eventFilter: (event: AsyncWorkloadEvent)=>{
    // only call this workload if this is for an enterprise customer
    return event.eventData.plan === 'enterprise';
  }
};
```
</TabItem>

<TabItem label="JavaScript">

```js
export const asyncWorkloadConfig = {
  events: ['event-a', 'event-b'],
  eventFilter: (event)=>{
    // only call this workload if this is for an enterprise customer
    return event.eventData.plan === 'enterprise';
  }
};
```
</TabItem>

- `maxRetries` (optional) - when the event is to be handled by a workload function, it always attempts to retry failures. The value should be the number of attempts to be made after the initial retry attempt. The default is `4`, which means the total number of attempts for a function is the initial plus four retry attempts, or `5` total attempts.

- `backoffSchedule` (optional) - provide a function that will be passed the attempt number and it should return the number of milliseconds to wait before processing the next value. Return value can be a number or an [ms-compatible string](https://www.npmjs.com/package/@lukeed/ms) of a relative time from now or the absolute UTC milliseconds. The maximum backoff is `1 week`. The backoff schedule will default to `5 seconds` and each attempt after will multiply the last backoff delay by `4`. The schedule default is `5s`, `20s`, `1m20s`, `8m`, and so on for the remaining retries and up to the max backoff time.

### Tabs Component:

<TabItem label="TypeScript">

```ts
import type { AsyncWorkloadConfig } from "@netlify/async-workloads";

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
  events: ['event-a', 'event-b'],
  // a custom backoff schedule
  backoffSchedule: (attempt)=>{
    if(attempt < 2){
      return '5 minutes';
    }
    return '2 hours';
  }
};
```
</TabItem>

<TabItem label="JavaScript">

```js
export const asyncWorkloadConfig = {
  events: ['event-a', 'event-b'],
  backoffSchedule: (attempt)=>{
    if(attempt < 2){
      return '5 minutes';
    }
    return '2 hours';
  }
};
```
</TabItem>

## Retries and errors

Async Workload functions are considered successful if they do not timeout, if they do not throw an error, and if they do not reject a returned promise. If any of those conditions happen, the system looks to the retry process to determine what to do. The retrying process will consider the configured [`maxRetries`](/build/async-workloads/writing-workloads#maxRetries) and the [`backoffSchedule`](/build/async-workloads/writing-workloads#backoffSchedule).

Optionally, developers can override the workflow retry configuration by throwing explicit errors within the workload. These special error types will inform the system on how to handle this condition.

```js
import { asyncWorkloadFn, ErrorDoNotRetry, ErrorRetryAfterDelay } from "@netlify/async-workloads";

export default asyncWorkloadFn(function (event) {

	// error and explicitly prevent retries
  throw new ErrorDoNotRetry('do not retry this error');

	// error and control future retry
  throw new ErrorRetryAfterDelay({message: 'retry this after some time', retryDelay: '10s'});
});
```

- `ErrorDoNotRetry` - should be used when the workload should not be retried even if there are more retry attempts remaining. This event will still go to the failed state.
- `ErrorRetryAfterDelay` - should be used when the workload has a known delay that needs to be abided by. For example, if the workload is using a third-party API and the API provides a rate limit delay, the workload can turn that rate limit delay from the API into the retry delay.
    - `retryDelay` (required) - the number of milliseconds the system should wait relative to now before retrying. The value can be a number or a [ms](https://www.npmjs.com/package/@lukeed/ms) compatible string value or absolute UTC milliseconds of when the workload should be retried.
    - `forceDelayTime` (optional) - by default, the system will choose the delay that's longer between the explicit `retryDelay` and the workload's [backoff schedule](/build/async-workloads/writing-workloads#backoffSchedule). Setting `forceDelayTime` to `true` will always use the passed `retryDelay` time and will override the backoff schedule. Note, the max time must abide by the same max limits of the backoff schedules.

## Type-safe events

For developers using TypeScript, the Async Workloads supports adding types to your events for both the workload functions and the AsyncWorkloadClient.

To create a type-safe event, you can use the `CustomAsyncWorkloadEvent` interface and extend it with your own event properties.

```ts
import type { CustomAsyncWorkloadEvent } from '@netlify/async-workloads';

// individual event types
export interface FooEvent extends CustomAsyncWorkloadEvent {
  eventName: 'foo',
  eventData: {
    propA: string;
    probB: number[]
  }
}

export interface BarEvent extends CustomAsyncWorkloadEvent {
  eventName: 'bar',
  eventData: {
    prop1: boolean;
  }
}

// the collection of all of the site's types
export type AllSiteEvents = FooEvent | BarEvent;
```

Now, we can use these event types within our available clients and workload functions.

```ts

const client = new AsyncWorkloadsClient<AllSiteEvents>();

client.send('foo', {
  data: {
    // throws type error because
    // this field is not on FooEvent or BarEvent
    otherField: true
  }
});

```

Within the type specific workload functions, we can use the events that it operates on exclusively for type safety.

```ts

// Type this event for the FooEvent
export default asyncWorkloadFn<FooEvent>((event)=> {

  // throws type error:
  // Property 'otherField' does not exist on type '{ propA: string; probB: number[]; }
  if(event.eventData?.otherField === true){
    return;
  }
});

export const asyncWorkloadConfig: AsyncWorkloadConfig<FooEvent> = {
  // throws a type error: because FooEvent is named 'foo'
  events: ['bar'],

  // event filter is also typed
  eventFilter: (event) => {
    // throws type error:
    // Property 'otherField' does not exist on type '{ propA: string; probB: number[]; }
    if(event.eventData?.otherField === true){
      return;
    }
  }
}

```

