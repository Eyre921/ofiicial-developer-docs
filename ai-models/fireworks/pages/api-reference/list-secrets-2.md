---
title: "List Secrets"
source: https://docs.fireworks.ai/api-reference/list-secrets
path: api-reference/list-secrets
---

get /v1/accounts/{account_id}/secrets
Lists all secrets for an account. Note that the `value` field is not returned in the response for security reasons. Only the `name` and `key_name` fields are included for each secret.
