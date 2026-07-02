---
title: "Validate API Token"
source: https://docs.turso.tech/api-reference/tokens/validate
path: api-reference/tokens/validate
---

GET /v1/auth/validate
Validates an API token belonging to a user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v1/auth/validate' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.apiTokens.validate("...");
  ```
</RequestExample>
