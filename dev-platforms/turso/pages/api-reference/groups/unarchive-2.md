---
title: "Unarchive Group"
source: https://docs.turso.tech/api-reference/groups/unarchive
path: api-reference/groups/unarchive
---

POST /v1/organizations/{organizationSlug}/groups/{groupName}/unarchive
Unarchive a group that has been archived due to inactivity.

<Info>
  Databases get archived after 10 days of inactivity for users on a free plan. You can unarchive inactive groups using the API.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/unarchive' \
  -H 'Authorization: Bearer TOKEN' \
  ```
</RequestExample>
