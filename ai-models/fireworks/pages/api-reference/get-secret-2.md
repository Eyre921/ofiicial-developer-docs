---
title: "Get Secret"
source: https://docs.fireworks.ai/api-reference/get-secret
path: api-reference/get-secret
---

get /v1/accounts/{account_id}/secrets/{secret_id}
Retrieves a secret by name. Note that the `value` field is not returned in the response for security reasons. Only the `name` and `key_name` fields are included.
