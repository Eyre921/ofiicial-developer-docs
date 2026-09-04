---
title: "Retrieve Database Stats"
source: https://docs.turso.tech/api-reference/databases/stats
path: api-reference/databases/stats
---

GET /v1/organizations/{organizationSlug}/databases/{databaseName}/stats
Fetch the top queries of a database, including the count of rows read and written.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/stats' \
  -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
