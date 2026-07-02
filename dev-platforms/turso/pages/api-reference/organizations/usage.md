---
title: "Organization Usage"
source: https://docs.turso.tech/api-reference/organizations/usage
path: api-reference/organizations/usage
---

GET /v1/organizations/{organizationSlug}/usage
Fetch current billing cycle usage for an organization.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/usage \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
