---
title: "Get Current User"
source: https://docs.turso.tech/api-reference/user/get-current
path: api-reference/user/get-current
---

GET /v1/user
Returns information about the currently authenticated user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/user \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const user = await turso.users.getCurrent();
  ```
</RequestExample>
