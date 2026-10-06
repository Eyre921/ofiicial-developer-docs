---
title: "context.notify"
source: https://upstash.com/docs/workflow/steps/notify
path: docs/workflow/steps/notify
---

`context.notify()` notifies workflows that are waiting for a specific event, passing along an optional payload.

It is typically used in combination with [`context.waitForEvent`](/docs/workflow/steps/waitForEvent).

## Arguments

<ParamField body="stepName" type="string">
    A unique identifier for the step.
</ParamField>

<ParamField body="eventId" type="string">
    The identifier of the event to notify.
    Must match the `eventId` used in `context.waitForEvent`.
</ParamField>

<ParamField body="eventData" type="any">
    Data to deliver to the waiting workflow(s).
    This value will be returned in `eventData` from the corresponding `waitForEvent` call.
</ParamField>

<ParamField body="workflowRunId" type="string" optional>
    The workflow run ID to notify. When provided, enables **lookback functionality** - the notification will be stored and delivered even if `notify` is called before `waitForEvent`.

    This solves race conditions where notifications might be sent before a workflow reaches its wait step.
</ParamField>

## Response

`context.notify()` returns an object containing the notified event and the list of workflows that were notified.

<ResponseField name="eventId" type="string">
    The event ID that was notified.
</ResponseField>

<ResponseField name="eventData" type="any">
    The event data sent with the notification.
</ResponseField>

<ResponseField name="notifyResponse" type="NotifyResponse[]">
    A list of `NotifyResponse` objects, one for each workflow that was waiting on the event.
    An empty list means no workflow was waiting.

    <Expandable defaultOpen>
        <ResponseField name="messageId" type="string">
            The ID of the notification message delivered to the workflow.
            This is unique to every notification.
        </ResponseField>

        <ResponseField name="error" type="string">
            Error message if delivering the notification to this waiter failed.
        </ResponseField>

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
    </Expandable>

</ResponseField>

## Usage

### Basic Notification

```javascript
import { serve } from "@upstash/workflow/nextjs";

export const { POST } = serve<{ topic: string }>(async (context) => {
  const payload = context.requestPayload;

  const {
    notifyResponse, // result of notify, which is a list of notified waiters
  } = await context.notify("notify step", "my-event-Id", payload);
});
```

### Notification with Lookback

To prevent race conditions, you can provide a `workflowRunId`. This enables lookback - the notification will be stored and delivered even if sent before the target workflow reaches `waitForEvent`:

```javascript
import { serve } from "@upstash/workflow/nextjs";

export const { POST } = serve<{ orderId: string }>(async (context) => {
  const { orderId } = context.requestPayload;

  // Process payment
  await context.run("process-payment", async () => {
    return processPayment(orderId);
  });

  // Notify a specific workflow run with lookback support
  const {
    notifyResponse,
  } = await context.notify(
    "notify payment complete",
    "payment-processed",
    { orderId, status: "success" },
    "wfr_order_processor_123" // Enables lookback for this workflow run
  );
});
```
