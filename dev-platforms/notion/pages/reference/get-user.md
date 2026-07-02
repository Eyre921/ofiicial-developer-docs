---
title: "Retrieve a user"
source: https://developers.notion.com/reference/get-user
path: reference/get-user
---

get /v1/users/{user_id}
Retrieves a [User](/reference/user) using the ID specified.

The requested user must belong to the workspace connected to the integration. This endpoint can return workspace members, guests, and bots in that workspace.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have user information capabilities. Attempting to call this API without user information capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>
