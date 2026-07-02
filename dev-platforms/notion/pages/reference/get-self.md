---
title: "Retrieve your token's bot user"
source: https://developers.notion.com/reference/get-self
path: reference/get-self
---

get /v1/users/me
Retrieves the [User](/reference/user) associated with the API token provided in the authorization header.

For [personal access tokens](/guides/get-started/personal-access-tokens), this endpoint returns the user who created the token.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Connection capabilities**

  This endpoint is accessible from by connections with any level of capabilities. The [user object](/reference/user) returned will adhere to the limitations of the connection's capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>
