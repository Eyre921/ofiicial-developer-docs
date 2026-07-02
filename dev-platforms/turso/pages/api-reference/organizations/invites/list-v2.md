---
title: "List Invites"
source: https://docs.turso.tech/api-reference/organizations/invites/list-v2
path: api-reference/organizations/invites/list-v2
---

GET /v2/organizations/{organizationSlug}/invites
Returns a list of pending invites for the organization.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v2/organizations/{organizationSlug}/invites \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "mycompany",
    token: "",
  });

  const invites = await turso.organizations.listInvites();
  ```
</RequestExample>
