---
title: "Restore Database"
source: https://docs.turso.tech/api-reference/databases/restore
path: api-reference/databases/restore
---

POST /v3/organizations/{organizationId}/databases/{databaseId}/restore
Restore a database deleted within the last five days, exactly as it was at the moment it was deleted. Requires a paid plan, an admin or owner of the organization, and recovery enabled for the organization.

<Note>
  Unlike the v1 endpoints, this endpoint identifies the organization and database
  by **UUID** — use the `id` field from
  [Retrieve Organization](/api-reference/organizations/retrieve) and the `DbId`
  field from [List Deleted Databases](/api-reference/databases/list-deleted).
</Note>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v3/organizations/{organizationId}/databases/{databaseId}/restore' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```bash cURL (new name) theme={null}
  curl -L -X POST 'https://api.turso.tech/v3/organizations/{organizationId}/databases/{databaseId}/restore' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{ "name": "my-restored-database" }'
  ```
</RequestExample>
