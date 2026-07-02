---
title: "Retrieve Group Configuration"
source: https://docs.turso.tech/api-reference/groups/configuration
path: api-reference/groups/configuration
---

GET /v1/organizations/{organizationSlug}/groups/{groupName}/configuration
Retrieve an individual group configuration belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/configuration' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
