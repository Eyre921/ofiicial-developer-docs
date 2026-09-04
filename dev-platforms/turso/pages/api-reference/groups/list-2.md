---
title: "List Groups"
source: https://docs.turso.tech/api-reference/groups/list
path: api-reference/groups/list
---

GET /v1/organizations/{organizationSlug}/groups
Returns a list of groups belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/groups \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const groups = await turso.groups.list();
  ```
</RequestExample>
