---
title: "List Invoices"
source: https://docs.turso.tech/api-reference/organizations/invoices
path: api-reference/organizations/invoices
---

GET /v1/organizations/{organizationSlug}/invoices
Returns a list of invoices for the organization.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/invoices \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
