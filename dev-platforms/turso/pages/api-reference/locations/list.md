---
title: "List Locations"
source: https://docs.turso.tech/api-reference/locations/list
path: api-reference/locations/list
---

GET /v1/locations
Returns a list of locations where you can create or replicate databases.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/locations \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const locations = await turso.locations.list();
  ```
</RequestExample>
