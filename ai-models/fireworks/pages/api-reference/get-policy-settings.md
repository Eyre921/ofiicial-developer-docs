---
title: "Get Policy Settings"
source: https://docs.fireworks.ai/api-reference/get-policy-settings
path: api-reference/get-policy-settings
---

get /v1/accounts/{account_id}/policySettings

Returns the account's governance settings in one object:

| Field | Setting |
| :- | :- |
| `defaultPermissions`, `rules` | [Model access policy](/accounts/model-access-policy) |
| `residency` | [Data residency](/accounts/data-residency) |
| `zeroDataRetention` | [Zero Data Retention policy](/accounts/zero-data-retention) |
| `cmekRequired` | [Customer-managed encryption keys](/guides/security_compliance/secure_training/cmek) |

Any account member can read the policy settings.

```bash theme={null}
curl -s "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/policySettings" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}"
```

An absent `residency` means serving is unrestricted, and an absent `zeroDataRetention` means the policy is off. An account that has never saved policy settings can return `404`, which also means no policy is set.
