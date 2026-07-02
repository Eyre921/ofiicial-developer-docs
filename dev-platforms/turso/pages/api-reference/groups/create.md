---
title: "Create Group"
source: https://docs.turso.tech/api-reference/groups/create
path: api-reference/groups/create
---

POST /v1/organizations/{organizationSlug}/groups
Creates a new group for the organization or user.

<Warning>
  Creating more than one group is limited to Scaler, Pro and Enterprise plans.
</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups' \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "new-group",
      "location": "lhr"
  }'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const group = await turso.groups.create("new-group", {
    location: "lhr",
    extensions: ["vector", "uuid"], // 'all'
  });
  ```
</RequestExample>
