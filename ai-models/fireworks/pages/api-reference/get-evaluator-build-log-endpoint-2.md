---
title: "Get Evaluator Build Log Endpoint"
source: https://docs.fireworks.ai/api-reference/get-evaluator-build-log-endpoint
path: api-reference/get-evaluator-build-log-endpoint
---

get /v1/accounts/{account_id}/evaluators/{evaluator_id}:getBuildLogEndpoint
Returns a signed URL to download the evaluator's build logs. Useful for
debugging `BUILD_FAILED` state.
