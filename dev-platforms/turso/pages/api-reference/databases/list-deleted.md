---
title: "List Deleted Databases"
source: https://docs.turso.tech/api-reference/databases/list-deleted
path: api-reference/databases/list-deleted
---

GET /v3/organizations/{organizationId}/databases
Returns databases deleted within the last five days, which can still be restored. Requires a paid plan. Available even while recovery is disabled for the organization.

<Note>
  Unlike the v1 endpoints, this endpoint identifies the organization by its
  **UUID** — the `id` field from
  [Retrieve Organization](/api-reference/organizations/retrieve).
</Note>

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v3/organizations/{organizationId}/databases?deleted=true' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
