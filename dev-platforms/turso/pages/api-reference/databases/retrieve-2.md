---
title: "Retrieve Database"
source: https://docs.turso.tech/api-reference/databases/retrieve
path: api-reference/databases/retrieve
---

GET /v1/organizations/{organizationSlug}/databases/{databaseName}
Returns a database belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const database = await turso.databases.retrieve("my-db");
  ```
</RequestExample>
