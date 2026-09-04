---
title: "List Organizations"
source: https://docs.turso.tech/api-reference/organizations/list
path: api-reference/organizations/list
---

GET /v1/organizations
Returns a list of organizations the authenticated user owns or is a member of.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const organizations = await turso.organizations.list();
  ```
</RequestExample>
