---
title: "Update Database Configuration"
source: https://docs.turso.tech/api-reference/databases/update-configuration
path: api-reference/databases/update-configuration
---

PATCH /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration
Update a database configuration belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X PATCH 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/configuration' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "size_limit": "500mb",
        "delete_protection": true,
        "block_reads": false,
        "block_writes": false,
        "allowed_ips": ["203.0.113.7", "10.0.0.0/8"],
        "allowed_aws_vpc_ids": ["vpce-0fe6c8807461bba49"]
    }'
  ```
</RequestExample>
