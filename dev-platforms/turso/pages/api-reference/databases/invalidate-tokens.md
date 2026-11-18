---
title: "Invalidate All Database Auth Tokens"
source: https://docs.turso.tech/api-reference/databases/invalidate-tokens
path: api-reference/databases/invalidate-tokens
---

POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate
Invalidates all database-scoped authorization tokens for the specified database. On AWS, only tokens for this database are invalidated; group tokens and tokens for other databases in the group are not affected.

> [!WARNING]
>
> On AWS, this invalidates only the tokens created for this database. Group tokens and tokens for other databases in the group are not affected.

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
