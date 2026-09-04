---
title: "Invalidate All Group Auth Tokens"
source: https://docs.turso.tech/api-reference/groups/invalidate-tokens
path: api-reference/groups/invalidate-tokens
---

POST /v1/organizations/{organizationSlug}/groups/{groupName}/auth/rotate
Invalidates all authorization tokens for the specified group.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/auth/rotate' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.groups.invalidateTokens("default");
  ```
</RequestExample>
