---
title: "Remove Member"
source: https://docs.turso.tech/api-reference/organizations/members/remove
path: api-reference/organizations/members/remove
---

DELETE /v1/organizations/{organizationSlug}/members/{username}
Remove a user from the organization by username.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE https://api.turso.tech/v1/organizations/{organizationSlug}/members/{username} \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const member = await turso.organizations.removeMember("mycompany", "iku");
  ```
</RequestExample>
