---
title: "List Database Instances"
source: https://docs.turso.tech/api-reference/databases/list-instances
path: api-reference/databases/list-instances
---

GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances
Returns a list of instances of a database. Instances are the individual primary or replica databases in each region defined by the group.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/instances \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const instances = await turso.databases.listInstances("my-db");
  ```
</RequestExample>
