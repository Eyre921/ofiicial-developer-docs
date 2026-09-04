---
title: "Delete Database"
source: https://docs.turso.tech/api-reference/databases/delete
path: api-reference/databases/delete
---

DELETE /v1/organizations/{organizationSlug}/databases/{databaseName}
Delete a database belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const database = await turso.databases.delete("my-db");
  ```
</RequestExample>
