---
title: "Restore Group"
source: https://docs.turso.tech/api-reference/groups/restore
path: api-reference/groups/restore
---

POST /v3/organizations/{organizationId}/groups/{groupId}/restore
Restore a group deleted within the last five days, along with the member databases that were deleted with it. Requires a paid plan, an admin or owner of the organization, and recovery enabled for the organization. If some databases fail to restore, the group still becomes active: retry the failed database UUIDs individually with Restore Database.

<Note>
  Unlike the v1 endpoints, this endpoint identifies the organization and group by
  **UUID** — use the `id` field from
  [Retrieve Organization](/api-reference/organizations/retrieve) and the `uuid`
  field from [List Deleted Groups](/api-reference/groups/list-deleted).
</Note>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v3/organizations/{organizationId}/groups/{groupId}/restore' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
