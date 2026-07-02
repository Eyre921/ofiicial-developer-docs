---
title: "Retrieve Group"
source: https://docs.turso.tech/api-reference/groups/retrieve
path: api-reference/groups/retrieve
---

GET /v1/organizations/{organizationSlug}/groups/{groupName}
Returns a group belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const group = await turso.groups.retrieve("default");
  ```
</RequestExample>
