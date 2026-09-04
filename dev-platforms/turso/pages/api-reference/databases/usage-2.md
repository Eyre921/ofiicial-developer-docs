---
title: "Retrieve Database Usage"
source: https://docs.turso.tech/api-reference/databases/usage
path: api-reference/databases/usage
---

GET /v1/organizations/{organizationSlug}/databases/{databaseName}/usage
Fetch activity usage for a database in a given time period.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/usage?from=2023-01-01T00:00:00Z&to=2023-02-01T00:00:00Z' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const usageStatsWithDate = await turso.databases.usage("my-db");

  const usageStatsWithDate = await turso.databases.usage("my-db", {
    from: new Date("2023-01-01"),
    to: new Date("2023-02-01"),
  });

  const usageStatsWithString = await turso.databases.usage("my-db", {
    from: "2023-01-01T00:00:00Z",
    to: "2023-02-01T00:00:00Z",
  });
  ```
</RequestExample>
