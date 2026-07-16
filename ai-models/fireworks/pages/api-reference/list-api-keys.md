---
title: "List API Keys"
source: https://docs.fireworks.ai/api-reference/list-api-keys
path: api-reference/list-api-keys
---

get /v1/accounts/{account_id}/users/{user_id}/apiKeys

List API keys for the user named in `user_id`. Admins can pass `-` as `user_id` to list keys for all users and service accounts in the account (equivalent to [`firectl api-key list --all-users`](/tools-sdks/firectl/commands/api-key-list)).

```bash theme={null}
curl -s "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/users/-/apiKeys" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}"
```
