---
title: "List API Tokens"
source: https://docs.turso.tech/api-reference/tokens/list
path: api-reference/tokens/list
---

GET /v1/auth/api-tokens
Returns a list of API tokens belonging to a user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/auth/api-tokens \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const apiTokens = await turso.apiTokens.list();
  ```
</RequestExample>
