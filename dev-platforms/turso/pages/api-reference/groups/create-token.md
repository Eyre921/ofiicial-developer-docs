---
title: "Create Group Auth Token"
source: https://docs.turso.tech/api-reference/groups/create-token
path: api-reference/groups/create-token
---

POST /v1/organizations/{organizationSlug}/groups/{groupName}/auth/tokens
Generates an authorization token for the specified group.

<Info>
  Tokens cannot be retrieved once created, and cannot be revoked individually.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/auth/tokens?expiration=2w&authorization=full-access' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const token = await turso.groups.createToken("default", {
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
