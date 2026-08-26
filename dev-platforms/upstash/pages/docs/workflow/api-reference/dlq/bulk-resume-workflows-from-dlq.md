---
title: "Bulk Resume Workflows from DLQ"
source: https://upstash.com/docs/workflow/api-reference/dlq/bulk-resume-workflows-from-dlq
path: docs/workflow/api-reference/dlq/bulk-resume-workflows-from-dlq
---

> When a workflow run fails, it's automatically moved to the DLQ (Dead Letter Queue) where it can be analyzed and resumed. 
  The resume feature allows you to continue a failed workflow run from exactly where it failed, without re-executing successfully completed steps.

  This is particularly useful for long-running workflows where you don't want to lose progress from successful steps when a single step fails.

  When a workflow is resumed, it continues execution from the last failed step. A new workflow run ID is generated,
  but the workflow maintains the state and results from previously completed steps.

  <Note>
    You can make changes to the workflow code as long as these changes come after the failed steps. 
    However, making changes before the failed step will break the code and is not allowed.

    For more details, check out [Handle workflow route code changes](/docs/workflow/howto/changes) page.
  </Note>


`POST /v2/workflows/dlq/resume`

<Info>
  For multi-value filters, a workflow run matches if its value equals any of the given values (OR logic), and multiple filters are combined with AND logic. 
  
  Multiple values can be passed either by repeating the query parameter (`label=label_1&label=label_2`) or as a single comma-separated value (`label=label_1,label_2`).
</Info>
