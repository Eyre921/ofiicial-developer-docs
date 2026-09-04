---
title: "List all users"
source: https://developers.notion.com/reference/get-users
path: reference/get-users
---

get /v1/users
Returns a paginated list of [Users](/reference/user) for the workspace. The response may contain fewer than `page_size` of results.

Guests are not included in the response.
If you already know a guest's ID, [Retrieve a user](/reference/get-user) can return that guest when they belong to the connected workspace.

See [Pagination](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

The API does not guarantee a particular sort order for returned users.

<Note>
  [Personal access tokens](/guides/get-started/personal-access-tokens) cannot list workspace users. Use [Retrieve token's bot user](/reference/get-self) to retrieve the PAT creator, or [Retrieve a user](/reference/get-user) with that user's ID.
</Note>

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  The API does not currently support filtering users by their email and/or name.
</Info>

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have user information capabilities. Attempting to call this API without user information capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>
