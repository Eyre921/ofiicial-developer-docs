---
title: "Get Flow Control Key"
source: https://upstash.com/docs/workflow/api-reference/flow-control/get-flow-control-key-1
path: docs/workflow/api-reference/flow-control/get-flow-control-key-1
---

/workflow/openapi.yaml get /v2/keys/rotate
Get details of a specific Flow Control key.

Flow Control keys are used to manage concurrency and rate limiting for workflow steps.
This endpoint returns the current waitlist size for the specified flow control key,
which indicates how many workflow steps are currently waiting due to flow control constraints.
