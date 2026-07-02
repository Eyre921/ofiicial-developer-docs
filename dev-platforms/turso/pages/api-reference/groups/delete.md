---
title: "Delete Group"
source: https://docs.turso.tech/api-reference/groups/delete
path: api-reference/groups/delete
---

DELETE /v1/organizations/{organizationSlug}/groups/{groupName}
Delete a group belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const group = await turso.groups.delete("new-group");
  ```
</RequestExample>
