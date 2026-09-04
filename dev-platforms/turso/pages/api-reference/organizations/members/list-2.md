---
title: "List Members"
source: https://docs.turso.tech/api-reference/organizations/members/list
path: api-reference/organizations/members/list
---

GET /v1/organizations/{organizationSlug}/members
Returns a list of members part of the organization.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/members \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const members = await turso.organizations.members("mycompany");
  ```
</RequestExample>
