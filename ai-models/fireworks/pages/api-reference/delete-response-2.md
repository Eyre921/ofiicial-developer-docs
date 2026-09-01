---
title: "Delete Response"
source: https://docs.fireworks.ai/api-reference/delete-response
path: api-reference/delete-response
---

delete /v1/responses/{response_id}
Deletes a model response by its ID. Once deleted, the response data will be gone immediately and permanently.

The response cannot be recovered and any conversations that reference this response ID will no longer be able to access it.
