---
title: "Validate Evaluator Upload"
source: https://docs.fireworks.ai/api-reference/validate-evaluator-upload
path: api-reference/validate-evaluator-upload
---

post /v1/accounts/{account_id}/evaluators/{evaluator_id}:validateUpload
Triggers server-side validation of the uploaded source code (**step 5** in
the [Create Evaluator](/api-reference/create-evaluator) workflow). The server
extracts and processes the archive, then builds the evaluator environment.
Poll [Get Evaluator](/api-reference/get-evaluator) to monitor progress.
