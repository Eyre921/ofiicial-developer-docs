---
title: "Retrieve Database Instance"
source: https://docs.turso.tech/api-reference/databases/retrieve-instance
path: api-reference/databases/retrieve-instance
---

GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName}
Return the individual database instance by name.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName} \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const instance = await turso.databases.retrieveInstance(
    "my-db",
    "instanceName",
  );
  ```
</RequestExample>
