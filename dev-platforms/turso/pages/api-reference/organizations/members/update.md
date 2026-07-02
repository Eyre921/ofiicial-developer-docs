---
title: "Update Member Role"
source: https://docs.turso.tech/api-reference/organizations/members/update
path: api-reference/organizations/members/update
---

PATCH /v1/organizations/{organizationSlug}/members/{username}
Update the role of an organization member. Only organization admins or owners can perform this action.

<RequestExample>
  ```bash theme={null}
  curl -L -X PATCH https://api.turso.tech/v1/organizations/{organizationSlug}/members/{username} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
      "role": "member"
    }'
  ```
</RequestExample>
