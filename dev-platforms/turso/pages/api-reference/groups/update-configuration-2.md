---
title: "Update Group Configuration"
source: https://docs.turso.tech/api-reference/groups/update-configuration
path: api-reference/groups/update-configuration
---

PATCH /v1/organizations/{organizationSlug}/groups/{groupName}/configuration
Update a group configuration belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X PATCH 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/configuration' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "delete_protection": true
    }'
  ```
</RequestExample>
