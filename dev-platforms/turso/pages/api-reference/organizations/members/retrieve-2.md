---
title: "Retrieve Member"
source: https://docs.turso.tech/api-reference/organizations/members/retrieve
path: api-reference/organizations/members/retrieve
---

GET /v1/organizations/{organizationSlug}/members/{username}
Retrieve details of a specific member in the organization.

<RequestExample>
  ```bash theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/members/{username} \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
