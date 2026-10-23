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
* A new error group appears, regresses, or is unignored

The first three are created from the **Alerts** page. The fourth — an **Error group** alert — is created from the **Errors** page instead, but appears in the same Alerts table once created. It behaves quite differently from a run failure alert; see [Error group alerts](#error-group-alerts) below.

> [!NOTE]
>
> If you want to be told about **every** run that fails, choose a **run fails** alert. An Error group
> alert will not do this — it deliberately stays quiet once it has alerted on a given error.

## How to setup alerts

**1. Create a new alert**

Click on "Alerts" in the left hand side menu, then click on "New alert" to open the new alert modal.

![Email alerts](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-blank.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=66c28b50c37b92057afb4100948a6636)

**2. Choose your alert method**

Choose to be notified by email, Slack notification or webhook whenever:

* a run fails
* a deployment fails
* a deployment succeeds

  ![Email alerts](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-modal.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=69b2a564572a6b1fb1c5e3ee77d68c4a)

**3. Delete or disable alerts**

Click on the triple dot menu on the right side of the table row and select "Disable" or "Delete".

![Disable and delete alerts](https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/troubleshooting-alerts-disable-delete.png?fit=max\&auto=format\&n=0bD0UfsjaINxS6Tw\&q=85\&s=f3455ed01b0d4c7a66c855a3b7d0cc53)

## Error group alerts

Error group alerts are **issue-based**, not run-based. They are created from the **Errors** page in the dashboard (the "Configure alerts…" button), not from the New alert modal on the Alerts page. Once created they show up in the Alerts table alongside your other alerts, labelled "Error group".

An error group is one distinct error — the same error from many runs is a single group, with a status of **Unresolved**, **Resolved** or **Ignored** that you set from the Errors page.

### When an error group alert fires

The alert only fires when a group's status *changes* in one of these three ways:

| Trigger | Meaning |
| :- | :- |
| New issue | The error has been seen for the first time. |
| Regression | The group was marked **Resolved**, and the error has occurred again since. |
| Unignored | The group was **Ignored**, and the ignore condition you set has been breached. |

### Why it goes quiet

This is the part that surprises people, so it is worth stating plainly:

**An Unresolved error group does not alert.** After an error group alert fires, the group is set to Unresolved, and it stays silent no matter how many more times that error occurs. It will only alert again once you mark it **Resolved** (and it then recurs) or **Ignored** (and the ignore condition is breached).

This is intentional — one persistently broken task should not flood your Slack channel with a message per failed run. But it means an Error group alert is not a substitute for a run failure alert. If a task has been failing in production for days and you have had no notification, check whether the only alert you have configured is an Error group alert whose group is sitting at Unresolved.

### Which alert type should I use?

* **"Tell me about every run that fails"** → a **run fails** alert, from the Alerts page. It fires for every run that fails once its retries are exhausted.
* **"Tell me when something new breaks"** → an **Error group** alert, from the Errors page.

The two are complementary, and many teams want both.

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
      case "alert.error": {
        console.log("[Webhook Internal Test] Error group alert webhook received", { event });
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

**id** `string`

A unique identifier for this webhook event

**created** `datetime`

When this webhook event was created

**webhookVersion** `string`

The version of the webhook payload format

**type** `string`

The type of alert webhook. One of: `alert.run.failed`, `alert.deployment.success`, `alert.deployment.failed`, or `alert.error`

### Run Failed Alert

This webhook is sent when a run fails. The payload is available on the `object` property:

**object.task.id** `string`

Unique identifier for the task

**object.task.filePath** `string`

File path where the task is defined

**object.task.exportName** `string`

Name of the exported task function

**object.task.version** `string`

Version of the task

**object.task.sdkVersion** `string`

Version of the SDK used

**object.task.cliVersion** `string`

Version of the CLI used

**object.run.id** `string`

Unique identifier for the run

**object.run.number** `number`

Run number

**object.run.status** `string`

Current status of the run

**object.run.createdAt** `datetime`

When the run was created

**object.run.startedAt** `datetime`

When the run started executing

**object.run.completedAt** `datetime`

When the run finished executing

**object.run.isTest** `boolean`

Whether this is a test run

**object.run.idempotencyKey** `string`

Idempotency key for the run

**object.run.tags** `string[]`

Associated tags

**object.run.error** `object`

Error information

**object.run.isOutOfMemoryError** `boolean`

Whether the run was an out-of-memory error

**object.run.machine** `string`

Machine preset used for the run

**object.run.dashboardUrl** `string`

URL to view the run in the dashboard

**object.environment.id** `string`

Environment ID

**object.environment.type** `string`

Environment type (`PRODUCTION`, `STAGING`, or `PREVIEW`)

**object.environment.slug** `string`

Environment slug

**object.environment.branchName** `string`

Environment branch name (optional)

**object.organization.id** `string`

Organization ID

**object.organization.slug** `string`

Organization slug

**object.organization.name** `string`

Organization name

**object.project.id** `string`

Project ID

**object.project.ref** `string`

Project reference

**object.project.slug** `string`

Project slug

**object.project.name** `string`

Project name

### Deployment Success Alert

This webhook is sent when a deployment succeeds. The payload is available on the `object` property:

**object.deployment.id** `string`

Deployment ID

**object.deployment.status** `string`

Deployment status

**object.deployment.version** `string`

Deployment version

**object.deployment.shortCode** `string`

Short code identifier

**object.deployment.deployedAt** `datetime`

When the deployment completed

**object.tasks** `array`

Array of deployed tasks with properties: id, filePath, exportName, and triggerSource

**object.environment.id** `string`

Environment ID

**object.environment.type** `string`

Environment type (`PRODUCTION`, `STAGING`, or `PREVIEW`)

**object.environment.slug** `string`

Environment slug

**object.organization.id** `string`

Organization ID

**object.organization.slug** `string`

Organization slug

**object.organization.name** `string`

Organization name

**object.project.id** `string`

Project ID

**object.project.ref** `string`

Project reference

**object.project.slug** `string`

Project slug

**object.project.name** `string`

Project name

**object.git** `object`

Git metadata for the deployment (optional). When present, `branch`, `commitSha`, `commitMessage`, `commitUrl` and `branchUrl` are always set.

**object.git.branch** `string`

Git branch

**object.git.commitSha** `string`

Short commit SHA (first 7 characters)

**object.git.commitMessage** `string`

Commit message (empty string if unavailable)

**object.git.commitUrl** `string`

URL of the commit

**object.git.branchUrl** `string`

URL of the branch

**object.git.pullRequestNumber** `number`

Pull request number (optional)

**object.git.pullRequestTitle** `string`

Pull request title (optional)

**object.git.pullRequestUrl** `string`

Pull request URL (optional)

**object.git.provider** `string`

Git provider (optional)

**object.vercel** `object`

Vercel metadata for the deployment (optional)

**object.vercel.deploymentUrl** `string`

URL of the deployment in the Vercel dashboard

### Deployment Failed Alert

This webhook is sent when a deployment fails. The payload is available on the `object` property:

**object.deployment.id** `string`

Deployment ID

**object.deployment.status** `string`

Deployment status

**object.deployment.version** `string`

Deployment version

**object.deployment.shortCode** `string`

Short code identifier

**object.deployment.failedAt** `datetime`

When the deployment failed

**object.error.name** `string`

Error name

**object.error.message** `string`

Error message

**object.error.stack** `string`

Error stack trace (optional)

**object.error.stderr** `string`

Standard error output (optional)

**object.environment.id** `string`

Environment ID

**object.environment.type** `string`

Environment type (`PRODUCTION`, `STAGING`, or `PREVIEW`)

**object.environment.slug** `string`

Environment slug

**object.organization.id** `string`

Organization ID

**object.organization.slug** `string`

Organization slug

**object.organization.name** `string`

Organization name

**object.project.id** `string`

Project ID

**object.project.ref** `string`

Project reference

**object.project.slug** `string`

Project slug

**object.project.name** `string`

Project name

**object.git** `object`

Git metadata for the deployment (optional). When present, `branch`, `commitSha`, `commitMessage`, `commitUrl` and `branchUrl` are always set.

**object.git.branch** `string`

Git branch

**object.git.commitSha** `string`

Short commit SHA (first 7 characters)

**object.git.commitMessage** `string`

Commit message (empty string if unavailable)

**object.git.commitUrl** `string`

URL of the commit

**object.git.branchUrl** `string`

URL of the branch

**object.git.pullRequestNumber** `number`

Pull request number (optional)

**object.git.pullRequestTitle** `string`

Pull request title (optional)

**object.git.pullRequestUrl** `string`

Pull request URL (optional)

**object.git.provider** `string`

Git provider (optional)

**object.vercel** `object`

Vercel metadata for the deployment (optional)

**object.vercel.deploymentUrl** `string`

URL of the deployment in the Vercel dashboard

### Error Group Alert

This webhook is sent for an [error group alert](#error-group-alerts). The payload is available on the `object` property:

**object.classification** `string`

Why the alert fired. One of: `new_issue`, `regression`, `unignored`

**object.error.fingerprint** `string`

Identifier for the error group

**object.error.type** `string`

Error type

**object.error.message** `string`

Error message

**object.error.stackTrace** `string`

Sample stack trace, if available

**object.error.firstSeen** `string`

When the error was first seen

**object.error.lastSeen** `string`

When the error was last seen

**object.error.occurrenceCount** `number`

Number of occurrences

**object.error.taskIdentifier** `string`

Task the error occurred in

**object.environment.id** `string`

Environment ID

**object.environment.name** `string`

Environment name

**object.organization.id** `string`

Organization ID

**object.organization.slug** `string`

Organization slug

**object.organization.name** `string`

Organization name

**object.project.id** `string`

Project ID

**object.project.ref** `string`

Project reference

**object.project.slug** `string`

Project slug

**object.project.name** `string`

Project name

**object.dashboardUrl** `string`

URL to view the error in the dashboard
