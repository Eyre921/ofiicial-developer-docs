---
title: "Bulk Cancel Workflow Runs"
source: https://upstash.com/docs/workflow/api-reference/runs/bulk-cancel-workflow-runs
path: docs/workflow/api-reference/runs/bulk-cancel-workflow-runs
---

> Cancel all matching workflow runs.

`DELETE /v2/workflows/runs`

<Warning>If you provide a list of workflow run IDs in the request body, only those specific workflow runs will be canceled. If you include the workflow URL parameter, all workflow runs matching the URL filter will be canceled. If the request body is empty, all workflow runs will be canceled.</Warning>

This operation scans all your workflow runs and attempts to cancel them.
If a specific workflow run cannot be canceled, it will return an error message.
Therefore, some workflow runs may not be cancelled at the end.
In such cases, you can run the bulk cancel operation multiple times.

For multi-value filters, a workflow run matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
