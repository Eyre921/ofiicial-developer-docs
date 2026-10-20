---
title: "Retrieve your token's bot user"
source: https://developers.notion.com/reference/get-self
path: reference/get-self
---

get /v1/users/me
Retrieves the [User](/reference/user) associated with the token provided in the authorization header.

For [personal access tokens](/guides/get-started/personal-access-tokens), this endpoint returns the token's bot user. Its `bot.owner.user` is the user who created the token.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

> [!NOTE]
>
> **Connection capabilities**
>
> This endpoint works for connections with any content, property, or comment capability. User information capabilities alone don't grant access. They only control what the owner fields in the [user object](/reference/user) show. To include the owner's email address, the connection needs user information with email addresses. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
