---
title: "Invalidate All Database Auth Tokens"
source: https://docs.turso.tech/api-reference/databases/invalidate-tokens
path: api-reference/databases/invalidate-tokens
---

POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate
Invalidates all authorization tokens for the specified database.

<Warning>
  A short downtime is required to complete the changes.
</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.databases.rotateTokens("my-db");
  ```
</RequestExample>
