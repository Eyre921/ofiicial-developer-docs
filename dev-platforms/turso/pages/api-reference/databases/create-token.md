---
title: "Generate Database Auth Token"
source: https://docs.turso.tech/api-reference/databases/create-token
path: api-reference/databases/create-token
---

POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens
Generates an authorization token for the specified database.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens?expiration=2w&authorization=full-access' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const token = await turso.databases.createToken("my-db", {
    expiration: "2w",
    authorization: "full-access",
  });
  ```
</RequestExample>

<ResponseExample>
  ```json theme={null}
  {
    "jwt": "TOKEN"
  }
  ```
</ResponseExample>
