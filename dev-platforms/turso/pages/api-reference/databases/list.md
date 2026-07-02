---
title: "List Databases"
source: https://docs.turso.tech/api-reference/databases/list
path: api-reference/databases/list
---

GET /v1/organizations/{organizationSlug}/databases
Returns a list of databases belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/databases \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const databases = await turso.databases.list();
  ```
</RequestExample>
