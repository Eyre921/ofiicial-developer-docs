---
title: "Create a token"
source: https://developers.notion.com/reference/create-a-token
path: reference/create-a-token
---

post /v1/oauth/token
Creates an access token that a third-party service can use to authenticate with Notion.

<Info>
  For step-by-step instructions on how to use this endpoint to create a public connection, check out the [Authorization guide](/guides/get-started/authorization#public-connection-auth-flow-set-up).
</Info>

<Warning>
  **Redirect URI requirements for public connections**

  The `redirect_uri` is a *required* field in the request body for this endpoint if:

  * the `redirect_uri` query parameter was set in the [Authorization URL](/guides/get-started/authorization#step-1-navigate-the-user-to-the-connections-authorization-url) provided to users, *or*;
  * there are more than one `redirect_uri`s included in the <a href={developerConnectionsUrl}>connection's settings</a> under **OAuth Domain & URIs**.

  In most cases, the `redirect_uri` field is required.

  This field is not allowed in the request body if:

  * there is one `redirect_uri` included in the <a href={developerConnectionsUrl}>connection's settings</a> under **OAuth Domain & URIs**, *and* the `redirect_uri` query parameter was not included in the Authorization URL.

  Learn more in the public connection section of the [Authorization Guide](/guides/get-started/authorization#public-connection-auth-flow-set-up).

  *Note: Each Public API endpoint can return several possible error codes. To see a full description of each type of error code, see the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation.*
</Warning>
