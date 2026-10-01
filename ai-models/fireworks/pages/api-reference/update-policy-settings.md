---
title: "Update Policy Settings"
source: https://docs.fireworks.ai/api-reference/update-policy-settings
path: api-reference/update-policy-settings
---

patch /v1/accounts/{account_id}/policySettings

Updates the account's governance settings. The API key must belong to an account **Admin** on an Enterprise account, either a user or a [service account](/accounts/service-accounts) with the Admin role. Requests with any other key fail with a permission error.

Pass `updateMask` with the proto field names of the settings you are changing, comma-separated. If you omit it, the mask is derived from the fields present in your request body. Settings outside the mask are left unchanged.

| Setting | `updateMask` | Notes |
| :- | :- | :- |
| [Model access policy](/accounts/model-access-policy) | `default_permissions`, `rules` | `rules` replaces the whole list. Every permissions object needs all four booleans. |
| [Data residency](/accounts/data-residency) | `residency` | Accepts `US`. Mask `residency` and omit the field to remove the restriction. |
| [Zero Data Retention policy](/accounts/zero-data-retention) | `zero_data_retention` | Replaces the whole section, so always send `defaultEnforced`. A scope you leave out follows `defaultEnforced`. |
| [Customer-managed encryption keys](/guides/security_compliance/secure_training/cmek) | `cmek_required` | Only Fireworks can change it. |

```bash theme={null}
curl -X PATCH \
  "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/policySettings?updateMask=zero_data_retention" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"zeroDataRetention": {"defaultEnforced": true}}'
```
