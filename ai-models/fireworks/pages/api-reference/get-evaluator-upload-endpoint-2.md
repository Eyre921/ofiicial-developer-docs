---
title: "Get Evaluator Upload Endpoint"
source: https://docs.fireworks.ai/api-reference/get-evaluator-upload-endpoint
path: api-reference/get-evaluator-upload-endpoint
---

post /v1/accounts/{account_id}/evaluators/{evaluator_id}:getUploadEndpoint
Returns signed URLs for uploading evaluator source code (**step 3** in the
[Create Evaluator](/api-reference/create-evaluator) workflow). After receiving
the signed URL, upload your `.tar.gz` archive using HTTP `PUT` with
`Content-Type: application/octet-stream` header.
