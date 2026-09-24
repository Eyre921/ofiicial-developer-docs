---
title: "List Deleted Groups"
source: https://docs.turso.tech/api-reference/groups/list-deleted
path: api-reference/groups/list-deleted
---

GET /v3/organizations/{organizationId}/deleted-groups
Returns groups deleted within the last five days, including empty groups, which can still be restored. Requires a paid plan and an organization-level token. Available even while recovery is disabled for the organization.

<Note>
  Unlike the v1 endpoints, this endpoint identifies the organization by its
  **UUID** — the `id` field from
  [Retrieve Organization](/api-reference/organizations/retrieve).
</Note>

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v3/organizations/{organizationId}/deleted-groups' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
