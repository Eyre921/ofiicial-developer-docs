---
title: "client.getWaiters"
source: https://upstash.com/docs/workflow/basics/client/waiters
path: docs/workflow/basics/client/waiters
---

The `getWaiters` method retrieves all waiters that are currently listening for a given event.

A **waiter** represents a workflow run that is paused at a `context.waitForEvent` step and is waiting for the specified `eventId`.

## Arguments

<ParamField body="eventId" type="string" required>
    The identifier of the event to look up.
</ParamField>

## Response

Returns a list of `Waiter` objects describing workflows that are waiting on the given event.

<ResponseField name="Waiter" type="object">
  <Expandable>
   	<ResponseField name="url" type="string" required>
      URL to call upon notify
    </ResponseField>
   	<ResponseField name="deadline" type="number" required>
      Unix timestamp for when the wait will time out
    </ResponseField>
   	<ResponseField name="headers" type="Record<string, string[]>" required>
      Headers sent in case of notify
    </ResponseField>
   	<ResponseField name="timeoutUrl" type="string">
      URL to call upon timeout
    </ResponseField>
   	<ResponseField name="timeoutBody" type="unknown">
      Body used in timeout request
    </ResponseField>
   	<ResponseField name="timeoutHeaders" type="Record<string, string[]>">
      Headers sent in case of time out
    </ResponseField>
  </Expandable>
</ResponseField>

## Usage

```javascript
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" });

const result = await client.getWaiters({
  eventId: "my-event-id",
});
```
