---
title: "List Audit Logs"
source: https://docs.turso.tech/api-reference/audit-logs/list
path: api-reference/audit-logs/list
---

GET /v1/organizations/{organizationSlug}/audit-logs
Return the audit logs for the given organization, ordered by the `created_at` field in descending order.

<Warning>Audit Logs are limited to scaler plan and above.</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/audit-logs \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
