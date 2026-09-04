---
title: "Retrieve Database Configuration"
source: https://docs.turso.tech/api-reference/databases/configuration
path: api-reference/databases/configuration
---

GET /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration
Retrieve an individual database configuration belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/configuration' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
