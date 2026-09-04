---
title: "List Plans"
source: https://docs.turso.tech/api-reference/organizations/plans
path: api-reference/organizations/plans
---

GET /v1/organizations/{organizationSlug}/plans
Returns a list of available plans and their quotas.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/plans \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
