---
title: "Revoke API Token"
source: https://docs.turso.tech/api-reference/tokens/revoke
path: api-reference/tokens/revoke
---

DELETE /v1/auth/api-tokens/{tokenName}
Revokes the provided API token belonging to a user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/auth/api-tokens/{tokenName}' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.apiTokens.revoke("my-token");
  ```
</RequestExample>
