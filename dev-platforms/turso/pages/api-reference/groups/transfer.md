---
title: "Transfer Group"
source: https://docs.turso.tech/api-reference/groups/transfer
path: api-reference/groups/transfer
---

POST /v1/organizations/{organizationSlug}/groups/{groupName}/transfer
Transfer a group to another organization that you own or a member of.

<Info>
  You can only transfer groups to organizations you own or are an admin.
</Info>

<Warning>
  Existing database URL and tokens will continue to work, but should update your application to use the new URL and token as soon as possible.
</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/transfer' \
  -H 'Authorization: Bearer TOKEN' \
  -d '{
      "organization": "new-organization-slug"
  }'
  ```
</RequestExample>
