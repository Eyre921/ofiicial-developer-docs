---
title: "Alerts"
source: https://trigger.dev/docs/troubleshooting-alerts
path: docs/troubleshooting-alerts
---

Get alerted when runs or deployments fail, or when deployments succeed.

We support receiving alerts for the following events:

* Run fails
* Deployment fails
* Deployment succeeds

## How to setup alerts

<Steps>
  <Step title="Create a new alert">
    Click on "Alerts" in the left hand side menu, then click on "New alert" to open the new alert modal.

    <img alt="Email alerts" />
  </Step>

  <Step title="Choose your alert method">
    Choose to be notified by email, Slack notification or webhook whenever:

    * a run fails
    * a deployment fails
    * a deployment succeeds

      <img alt="Email alerts" />
  </Step>

  <Step title="Delete or disable alerts">
    Click on the triple dot menu on the right side of the table row and select "Disable" or "Delete".

    <img alt="Disable and delete alerts" />
  </Step>
</Steps>

## Alert webhooks

For the alert webhooks you can use the SDK to parse them. Here is an example of how to parse the webhook payload in Remix:

```ts theme={"theme":"css-variables"}
import { ActionFunctionArgs, json } from "@remix-run/server-runtime";
import { webhooks, WebhookError } from "@trigger.dev/sdk";

export async function action({ request }: ActionFunctionArgs) {
  // Make sure this is a POST request
  if (request.method !== "POST") {
    return json({ error: "Method not allowed" }, { status: 405 });
  }

  try {
    // Construct and verify the webhook event
    // This secret can be found on your Alerts page when you create a webhook alert
    const event = await webhooks.constructEvent(request, process.env.ALERT_WEBHOOK_SECRET!);

    // Process the event based on its type
    switch (event.type) {
      case "alert.run.failed": {
        console.log("[Webhook Internal Test] Run failed alert webhook received", { event });
        break;
      }
      case "alert.deployment.success": {
        console.log("[Webhook Internal Test] Deployment success alert webhook received", { event });
        break;
      }
      case "alert.deployment.failed": {
        console.log("[Webhook Internal Test] Deployment failed alert webhook received", { event });
        break;
      }
      default: {
        console.log("[Webhook Internal Test] Unhandled webhook type", { event });
      }
    }

    // Return a success response
    return json({ received: true }, { status: 200 });
  } catch (err) {
    // Handle webhook errors
    if (err instanceof WebhookError) {
      console.error("Webhook error:", { message: err.message });
      return json({ error: err.message }, { status: 400 });
    }

    if (err instanceof Error) {
      console.error("Error processing webhook:", { message: err.message });
      return json({ error: err.message }, { status: 400 });
    }

    // Handle other errors
    console.error("Error processing webhook:", { err });
    return json({ error: "Internal server error" }, { status: 500 });
  }
}
```

### Common properties

When you create a webhook alert, you'll receive different payloads depending on the type of alert. All webhooks share some common properties:

<ParamField type="string">
  A unique identifier for this webhook event
</ParamField>

<ParamField type="datetime">
  When this webhook event was created
</ParamField>

<ParamField type="string">
  The version of the webhook payload format
</ParamField>

<ParamField type="string">
  The type of alert webhook. One of: `alert.run.failed`, `alert.deployment.success`, or `alert.deployment.failed`
</ParamField>

### Run Failed Alert

This webhook is sent when a run fails. The payload is available on the `object` property:

<ParamField type="string">
  Unique identifier for the task
</ParamField>

<ParamField type="string">
  File path where the task is defined
</ParamField>

<ParamField type="string">
  Name of the exported task function
</ParamField>

<ParamField type="string">
  Version of the task
</ParamField>

<ParamField type="string">
  Version of the SDK used
</ParamField>

<ParamField type="string">
  Version of the CLI used
</ParamField>

<ParamField type="string">
  Unique identifier for the run
</ParamField>

<ParamField type="number">
  Run number
</ParamField>

<ParamField type="string">
  Current status of the run
</ParamField>

<ParamField type="datetime">
  When the run was created
</ParamField>

<ParamField type="datetime">
  When the run started executing
</ParamField>

<ParamField type="datetime">
  When the run finished executing
</ParamField>

<ParamField type="boolean">
  Whether this is a test run
</ParamField>

<ParamField type="string">
  Idempotency key for the run
</ParamField>

<ParamField type="string[]">
  Associated tags
</ParamField>

<ParamField type="object">
  Error information
</ParamField>

<ParamField type="boolean">
  Whether the run was an out-of-memory error
</ParamField>

<ParamField type="string">
  Machine preset used for the run
</ParamField>

<ParamField type="string">
  URL to view the run in the dashboard
</ParamField>

<ParamField type="string">
  Environment ID
</ParamField>

<ParamField type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField type="string">
  Environment slug
</ParamField>

<ParamField type="string">
  Organization ID
</ParamField>

<ParamField type="string">
  Organization slug
</ParamField>

<ParamField type="string">
  Organization name
</ParamField>

<ParamField type="string">
  Project ID
</ParamField>

<ParamField type="string">
  Project reference
</ParamField>

<ParamField type="string">
  Project slug
</ParamField>

<ParamField type="string">
  Project name
</ParamField>

### Deployment Success Alert

This webhook is sent when a deployment succeeds. The payload is available on the `object` property:

<ParamField type="string">
  Deployment ID
</ParamField>

<ParamField type="string">
  Deployment status
</ParamField>

<ParamField type="string">
  Deployment version
</ParamField>

<ParamField type="string">
  Short code identifier
</ParamField>

<ParamField type="datetime">
  When the deployment completed
</ParamField>

<ParamField type="array">
  Array of deployed tasks with properties: id, filePath, exportName, and triggerSource
</ParamField>

<ParamField type="string">
  Environment ID
</ParamField>

<ParamField type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField type="string">
  Environment slug
</ParamField>

<ParamField type="string">
  Organization ID
</ParamField>

<ParamField type="string">
  Organization slug
</ParamField>

<ParamField type="string">
  Organization name
</ParamField>

<ParamField type="string">
  Project ID
</ParamField>

<ParamField type="string">
  Project reference
</ParamField>

<ParamField type="string">
  Project slug
</ParamField>

<ParamField type="string">
  Project name
</ParamField>

### Deployment Failed Alert

This webhook is sent when a deployment fails. The payload is available on the `object` property:

<ParamField type="string">
  Deployment ID
</ParamField>

<ParamField type="string">
  Deployment status
</ParamField>

<ParamField type="string">
  Deployment version
</ParamField>

<ParamField type="string">
  Short code identifier
</ParamField>

<ParamField type="datetime">
  When the deployment failed
</ParamField>

<ParamField type="string">
  Error name
</ParamField>

<ParamField type="string">
  Error message
</ParamField>

<ParamField type="string">
  Error stack trace (optional)
</ParamField>

<ParamField type="string">
  Standard error output (optional)
</ParamField>

<ParamField type="string">
  Environment ID
</ParamField>

<ParamField type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField type="string">
  Environment slug
</ParamField>

<ParamField type="string">
  Organization ID
</ParamField>

<ParamField type="string">
  Organization slug
</ParamField>

<ParamField type="string">
  Organization name
</ParamField>

<ParamField type="string">
  Project ID
</ParamField>

<ParamField type="string">
  Project reference
</ParamField>

<ParamField type="string">
  Project slug
</ParamField>

<ParamField type="string">
  Project name
</ParamField>
