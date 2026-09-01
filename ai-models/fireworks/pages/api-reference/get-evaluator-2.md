---
title: "Get Evaluator"
source: https://docs.fireworks.ai/api-reference/get-evaluator
path: api-reference/get-evaluator
---

get /v1/accounts/{account_id}/evaluators/{evaluator_id}
Retrieves an evaluator by name. Use this to monitor build progress after
creation (**step 6** in the [Create Evaluator](/api-reference/create-evaluator) workflow).

Possible states:

- `BUILDING` - Environment is being prepared
- `ACTIVE` - Evaluator is ready to use
- `BUILD_FAILED` - Check build logs via [Get Evaluator Build Log Endpoint](/api-reference/get-evaluator-build-log-endpoint)
