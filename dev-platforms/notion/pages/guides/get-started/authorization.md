---
title: "Authorization"
source: https://developers.notion.com/guides/get-started/authorization
path: guides/get-started/authorization
---

This guide describes the authorization flows for Notion connections and personal access tokens.

## What is authorization?

Authorization is the process of granting a connection or token access to Notion data. [Internal connections](/guides/get-started/internal-connections) use a static API token, [personal access tokens](/guides/get-started/personal-access-tokens) use a user-scoped static API token, and [public connections](/guides/get-started/public-connections) use the [OAuth 2.0](https://oauth.net/2/) protocol.

## Internal connection auth flow set-up

To use an internal connection, start by creating your connection in the <a href={developerConnectionsUrl}>Developer portal</a>.

The internal connection will be associated with the workspace of your choice. You are required to be a workspace owner to create a connection.

<Frame>
  <img />
</Frame>

Once the connection is created, you can update its settings as needed under the `Configuration` tab and retrieve the installation access token in this tab.

The installation access token will be used to authenticate REST API requests. The connection sends the same token in every API request.

<Frame>
  <img />
</Frame>

### Connection permissions

Before a connection can interact with your Notion workspace page(s), the page must be manually shared with the connection. To share a page with a connection, visit the page in your Notion workspace, click the ••• menu at the top right of a page, scroll down to `Add connections`, and use the search bar to find and select the connection from the dropdown list.

Once the connection is shared, you can start making API requests. If the page is not shared, any API requests made will respond with an error.

<Warning>
  **Never share your installation access token**

  Your installation access token is a secret. To keep your connection secure, never store the token in your source code or commit it in version control. Instead, read the token from an environment variable. Use a secret manager or deployment system to set the token in the environment.

  [Learn more: Best Practices for Handling API Keys](/guides/get-started/handling-api-keys)
</Warning>

### Making API requests with an internal connection

Any time your connection interacts with your workspace, include the installation access token in the `Authorization` header with every API request. However, if you are using Notion’s [SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) to interact with the REST API, the token is set once when a client is initialized.

<CodeGroup>
  ```http HTTP theme={null}
  GET /v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75 HTTP/1.1
  Authorization: Bearer {INTEGRATION_TOKEN}
  ```
</CodeGroup>

<CodeGroup>
  ```javascript JavaScript theme={null}
  const { Client } = require("@notionhq/client")

  // Initializing a client
  const notion = new Client({
  	auth: process.env.NOTION_TOKEN,
  })

  const getUsers = async () => {
  	const listUsersResponse = await notion.users.list({})
  }
  ```
</CodeGroup>

<Note>
  If you are not using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js), also set the [`Notion-Version`](/reference/versioning) and [`Content-type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) headers in all of your requests, like so:

  ```json JSON theme={null}
  headers: {
    Authorization: `Bearer ${process.env.NOTION_TOKEN}`,
    "Notion-Version": "2026-03-11",
    "Content-Type": "application/json",
  },
  ```
</Note>

If you receive an error response from the API, check if the connection has been properly [added to the page](https://www.notion.com/help/add-and-manage-connections-with-the-api#manage-connections-in-your-workspace). If this does not solve the problem, refer to our [Status codes](/reference/status-codes) page for more information.

## Personal access token authentication

Personal access tokens (PATs) are created directly by a Notion user in the <a href={developerPortalUrl}>Developer portal</a>. There is no OAuth flow and no page picker. A PAT acts as the user who created it and uses that user's permissions in the selected workspace.

Use a PAT when a script, CLI workflow, Worker, or trusted tool should act as you. Use an internal connection for team-owned workspace automations, or a public connection when other Notion users need to install your app.

PATs use the same `Authorization` header as other Notion API tokens:

<CodeGroup>
  ```http HTTP theme={null}
  GET /v1/users/me HTTP/1.1
  Authorization: Bearer {PERSONAL_ACCESS_TOKEN}
  Notion-Version: 2026-03-11
  ```
</CodeGroup>

See [Personal access tokens](/guides/get-started/personal-access-tokens) for creation steps, workspace admin controls, tier defaults, and security guidance.

## Public connection auth flow set-up

A public connection can be installed in any Notion workspace within its [installation scope](/guides/get-started/public-connections#installation-scope) — either any workspace, or a specific set chosen at creation time.

Since a public connection is not tied to a single workspace with a single installation access token, public connections instead follow the [OAuth 2.0 protocol](https://oauth.net/2/) to authorize a connection to interact with a workspace.

### How to make a public connection

Navigate to the <a href={developerConnectionsUrl}>Developer portal</a> and create a new public connection.

Fill out the form with your connection details, including your redirect URI(s) under the OAuth configuration section and the connection's [installation scope](/guides/get-started/public-connections#installation-scope) — either **Any workspace** or **Selected workspaces only**. This can't be changed after creation.

The redirect URI is the URI your users will be redirected to after authorizing the public connection. To learn more, read [OAuth’s description of redirect URIs](https://www.oauth.com/oauth2-servers/redirect-uris/).

<Note>
  Marketplace listing details (such as descriptions, categories, and images) are managed separately through the **Listings** section. Refer to the [List on the Marketplace](/guides/get-started/marketplace-listing) guide to learn more.
</Note>

### Public connection authorization overview

Once your connection has been made public, you can update your connection code to use the public auth flow.

As an overview, the authorization flow includes the following steps. Each step will be described in more detail below.

<Steps>
  <Step>
    Navigate the user to the connection’s authorization URL. This URL is provided in the <a href={developerConnectionsUrl}>Developer portal</a>.
  </Step>

  <Step>
    After the user selects which workspace pages to share, Notion redirects the user to the connection’s redirect URI and includes a `code` query parameter. The redirect URI is the one you specified in your <a href={developerConnectionsUrl}>Developer portal</a>.
  </Step>

  <Step>
    Make a `POST` request to [create an access token](/reference/create-a-token), which exchanges the temporary `code` for an access token.
  </Step>

  <Step>
    The Notion API responds with an access token and some additional information.
  </Step>

  <Step>
    Store the access token for future API requests. View the [API reference docs](/reference/intro) to learn about available endpoints.
  </Step>
</Steps>

### Step 1 - Navigate the user to the connection’s authorization URL

After creating a public connection in the <a href={developerConnectionsUrl}>Developer portal</a>, access the connection’s secrets in the **Configuration** tab. Similarly to the internal connections, these values should be protected and should never be included in source code or version control.

<Frame>
  <img />
</Frame>

As an example, your `.env` file using these secrets could look like this:

<CodeGroup>
  ```shell Shell theme={null}
  #.env

  OAUTH_CLIENT_ID=<your-client-id>
  OAUTH_CLIENT_SECRET=<your-client-secret>
  NOTION_AUTH_URL=<your-auth-url>
  ```
</CodeGroup>

To start the authorization flow for a public connection, direct the prospective user to the authorization URL. A common pattern is to include a hyperlink in the connection app that interacts with the Notion REST API. For example, an app that lets users create Notion pages in their workspaces should send users to the authorization URL first.

The following example shows an authorization URL made available through a hyperlink:

<CodeGroup>
  ```html HTML theme={null}
  <a href="https://api.notion.com/v1/oauth/authorize?owner=user&client_id=463558a3-725e-4f37-b6d3-0889894f68de&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%2Fnotion%2Fcallback&response_type=code">Add to Notion</a>
  ```
</CodeGroup>

The URL begins with `https://api.notion.com/v1/oauth/authorize` and has the following parameters:

| Parameter       | Description                                                                                                                                                                         | Required |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| `client_id`     | An identifier for your connection, found in the connection settings.                                                                                                                | ✅        |
| `redirect_uri`  | The URL where the user should return after granting access.                                                                                                                         | ✅        |
| `response_type` | Always use `code`.                                                                                                                                                                  | ✅        |
| `owner`         | Always use `user`.                                                                                                                                                                  | ✅        |
| `state`         | If the user was in the middle of an interaction or operation, then this parameter can be used to restore state after the user returns. It can also be used to prevent CSRF attacks. |          |

Once the authorization URL is visited, the user will be shown a prompt that varies depending on whether or not the connection comes with a Notion template option.

#### Prompt for a standard connection with no template option (Default)

In the standard connection permissions flow, a prompt describes the connection [capabilities](/reference/capabilities), presented to the user as what the connection would like to be able to do in the workspace. A user can either select pages to grant the connection access to, or cancel the request.

<Frame>
  <img />
</Frame>

If the user presses **Cancel**, they will be redirected to the redirect URI with and `error` query param added.

```
www.example.com/my-redirect-uri?error=access_denied&state=
```

You can use this `error`query parameter to conditionally update your app’s state as needed.

If the user opts to `Select pages`, then a page picker interface opens. A user can search for and select pages and databases to share with the connection from the page picker.

<Note>
  The page picker only displays pages or databases to which a user has [full access](https://www.notion.com/help/sharing-and-permissions), because a user needs full access to a resource in order to be able to share it with a connection.
</Note>

<Frame>
  <img />
</Frame>

Users can select which pages to give the connection access to, including both private and public pages available to them. Parent pages can be selected to quickly provide access to child pages, as giving access to a parent page will provide access to all available child pages. Users can return to this view at a later time to update access settings if circumstances change.

If the user clicks `Allow access`, they are then redirected to the `redirect_uri` with a temporary authorization `code`. If the user denies access, they are redirected to the `redirect_uri` with an `error` query parameter.

If the user clicks `Allow access` and the rest of the auth flow is not completed, the connection will *not* have access to the pages that were selected.

#### Prompt for a connection with a Notion template option

Public connections offer the option of providing a public Notion page to use as a template during the auth flow.

To add a template to your workspace, complete the following steps:

* Choose a public page in your workspace that you want users to be able to duplicate.
* Navigate to your connection in the <a href={developerConnectionsUrl}>Developer portal</a> and open the **Configuration** tab, then scroll to the Basic information section.
* Scroll to the bottom of your distribution settings and add the URL of the Notion page you selected to the **Notion URL for optional template** input.

<Frame>
  <img />
</Frame>

Once this URL is added, your auth flow prompt appearance will be updated.

Going back to your prompt view, if the connection offers a Notion template option, the first step in the permissions flow will describe the connection [capabilities](/reference/capabilities). This is presented to the user as what the connection would be able to do in the workspace, and it prompts the user to click `Next`.

<Frame>
  <img />
</Frame>

In the next step, a user can either choose to duplicate the template that you provided or to select existing pages to share with the connection.

<Frame>
  <img />
</Frame>

If the user chooses to duplicate the template, then the following happens automatically:

* The connection is added to the user’s workspace.
* The template is duplicated as a new page in the workspace.
* The new page is shared with the connection.

If the user chooses to select pages to share with the connection, then they continue to the page picker interface that’s part of the [prompt for a standard connection](#prompt-for-a-standard-connection-with-no-template-option-default).

<Note>
  After a user authorizes a public connection, only that user is able to interact or share pages and databases with the connection. Unlike internal connections, if multiple members in a workspace want to use a public connection, each prospective user needs to individually follow the auth flow for the connection.
</Note>

**User authorization failures**

User authorization failures can happen. If a user chooses to `Cancel` the request, then a failure is triggered. Build your connection to handle these cases gracefully, as needed.

In some cases, Notion redirects the user to the `redirect_uri` that you set up when you created the public connection, along with an `error` query parameter. Notion uses the common [error codes in the OAuth specification](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1). Use the `error` code to create a helpful prompt for the user when they’re redirected here.

### Step 2 - Notion redirects the user to the connection’s redirect URI and includes a `code` parameter

When you first created the public connection, you specified a redirect URI. If the user follows the prompt to `Allow access` for the connection, then Notion generates a temporary `code` and sends a request to the redirect URI with the following information in the query string:

| Parameter | Description                                                                                                                                      | Required |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| `code`    | A temporary authorization code.                                                                                                                  | ✅        |
| `state`   | The value provided by the connection when the user was [prompted for access](#prompt-for-a-standard-connection-with-no-template-option-default). |          |

To complete the next step, retrieve the `code` query parameter provided in the redirect. The retrieval method varies depending on your app’s tech stack.

In a React component, for example, the query parameters are made available through the `useRouter()` hook:

<CodeGroup>
  ```javascript JavaScript theme={null}
  export default function AuthRedirectPage() {
    const router = useRouter();
    const { code } = router.query;
    ...
  }
  ```
</CodeGroup>

### Step 3 - Send the `code` in a `POST` request to the Notion API

The connection needs to exchange the temporary `code` for an `access_token`.

To set up this step, retrieve the `code` from the redirect URI.

Next, send the `code` as part of a `POST` request to Notion’s token endpoint: [https://api.notion.com/v1/oauth/token](https://api.notion.com/v1/oauth/token).

This endpoint is described in more detail in the API reference docs for [creating a token](/reference/create-a-token).

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the connection’s `CLIENT_ID` and `CLIENT_SECRET`, like so:

```bash theme={null}
CLIENT_ID:CLIENT_SECRET
```

Find both of these values in the <a href={developerConnectionsUrl}>Developer portal</a>.

Note that in [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header.

The body of the request contains the following JSON-encoded fields:

| Field            | Type     | Description                                                                                | Required                                                                                                                                                                                                                                                                                                                           |
| :--------------- | :------- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"grant_type"`   | `string` | Always use `"authorization_code"`.                                                         | ✅                                                                                                                                                                                                                                                                                                                                  |
| `"code"`         | `string` | The temporary authorization code received in the incoming request to the `"redirect_uri"`. | ✅                                                                                                                                                                                                                                                                                                                                  |
| `"redirect_uri"` | `string` | The `"redirect_uri"` that was provided in the Authorization step.                          | ✅/❌\* <br /><br /> \* If the redirect URI was supplied as a query param in the Authorization URL, this field is required. If there are more than one redirect URIs included in your connection settings, this field is required. Otherwise, it is not allowed. Learn more in the [Create a token page](/reference/create-a-token). |

The following is an example request to exchange the authorization code for an access token:

<CodeGroup>
  ```http HTTP theme={null}
  POST /v1/oauth/token HTTP/1.1
  Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET"
  Content-Type: application/json

  {"grant_type":"authorization_code","code":"e202e8c9-0990-40af-855f-ff8f872b1ec6", "redirect_uri":"https://example.com/auth/notion/callback"}
  ```
</CodeGroup>

The Node-equivalent of this example would look something like this:

<CodeGroup>
  ```javascript JavaScript theme={null}
  ...
  const clientId = process.env.OAUTH_CLIENT_ID;
  const clientSecret = process.env.OAUTH_CLIENT_SECRET;
  const redirectUri = process.env.OAUTH_REDIRECT_URI;

  // encode in base 64
  const encoded = btoa(`${clientId}:${clientSecret}`);

  const response = await fetch("https://api.notion.com/v1/oauth/token", {
  	method: "POST",
  	headers: {
  	Accept: "application/json",
  	"Content-Type": "application/json",
  	Authorization: `Basic ${encoded}`,
  },
  	body: JSON.stringify({
  		grant_type: "authorization_code",
  		code: "your-temporary-code",
  		redirect_uri: redirectUri,
  	}),
  });
  ...
  ```
</CodeGroup>

### Step 4 - Notion responds with an `access_token` , `refresh_token`, and additional information

Notion responds to the request with an `access_token`, `refresh_token`, and additional information. The `access_token` will be used to authenticate subsequent Notion REST API requests. The `refresh_token` will be used to refresh the access token, which generates a new `access_token`.

The response contains the following JSON-encoded fields:

| Field                      | Type     | Description                                                                                                                                                                                                                                   | Not null |
| :------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| `"access_token"`           | `string` | An access token used to authorize requests to the Notion API.                                                                                                                                                                                 | ✅        |
| `"refresh_token"`          | `string` | A refresh token used to generate a new access token                                                                                                                                                                                           | ✅        |
| `"bot_id"`                 | `string` | An identifier for this authorization.                                                                                                                                                                                                         | ✅        |
| `"duplicated_template_id"` | `string` | The ID of the new page created in the user’s workspace. The new page is a duplicate of the template that the developer provided with the connection. If the developer didn’t provide a template for the connection, then the value is `null`. |          |
| `"owner"`                  | `object` | An object containing information about who can view and share this connection. A [user object](/reference/user) is returned, representing the user who authorized the connection.                                                             | ✅        |
| `"workspace_icon"`         | `string` | A URL to an image that can be used to display this authorization in the UI.                                                                                                                                                                   |          |
| `"workspace_id"`           | `string` | The ID of the workspace where this authorization took place.                                                                                                                                                                                  | ✅        |
| `"workspace_name"`         | `string` | A human-readable name that can be used to display this authorization in the UI.                                                                                                                                                               |          |

**Token request failures**

If something goes wrong when the connection attempts to exchange the `code` for an `access_token`, then the response contains a JSON-encoded body with an `"error"` field. Notion uses the common [error codes from the OAuth specification](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2).

### Step 5 - The connection stores the `access_token` and `refresh_token` for future requests

Set up a way for your connection to store both the `access_token` and `refresh_token` that it receives. The `access_token` is used to make authorized requests to the Notion API, and the `refresh_token` is used to generate a new `access_token`.

**Tips for storing and using token access**

* Setting up a database is a typical solution for storing access tokens. If you’re using a database, then build relations between an `access_token`, `refresh_token`, and the corresponding Notion resources that your connection accesses with that token. For example, if you store a Notion database or page ID, relate those records with the correct `access_token` that you use to authorize requests to read or write to that database or page, and the `refresh_token` for ongoing token lifecycle support..
* Store all of the information that your connection receives with the `access_token` and `refresh_token`. You never know when your UI or product requirements might change and you’ll need this data. It's really hard (or impossible) to send users to repeat the authorization flow to generate the information again.
* The `bot_id` returned along with your tokens identifies the Notion bot for the authorization. Store the token pair from each successful authorization response. This includes re-authorization of the same connection, where Notion may return a new `access_token` and `refresh_token`.

### Step 6 - Refreshing an access token

Refreshing an access token will generate a new access token and a new refresh token.

Send the `refresh_token` provided from [Step 4](#step-4-notion-responds-with-an-access_token--refresh_token-and-additional-information) as part of a `POST` request to Notion’s token endpoint: [https://api.notion.com/v1/oauth/token](https://api.notion.com/v1/oauth/token).

This endpoint is described in more detail in the API reference docs for [refreshing a token](/reference/refresh-a-token).

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the connection’s `CLIENT_ID` and `CLIENT_SECRET`, like so:

```bash theme={null}
CLIENT_ID:CLIENT_SECRET
```

Find both of these values in the <a href={developerConnectionsUrl}>Developer portal</a>.

Note that in [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header.

The body of the request contains the following JSON-encoded fields:

| Field             | Type     | Description                                               | Required |
| :---------------- | :------- | :-------------------------------------------------------- | :------- |
| `"grant_type"`    | `string` | Always use `"refresh_token"`.                             | ✅        |
| `"refresh_token"` | `string` | The `"refresh_token"` returned in the Authorization step. | ✅        |

The following is an example request to exchange the `refresh_token` for a new access token and new refresh token

<CodeGroup>
  ```http HTTP theme={null}
  POST /v1/oauth/token HTTP/1.1
  Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET"
  Content-Type: application/json

  {"grant_type":"refresh_token","refresh_token":"nrt_4991090011501Ejc6Xn4sHguI7jZIN449mKe9PRhpMfNK"}
  ```
</CodeGroup>

The Node-equivalent of this example would look something like this:

<CodeGroup>
  ```javascript JavaScript theme={null}
  ...
  const clientId = process.env.OAUTH_CLIENT_ID;
  const clientSecret = process.env.OAUTH_CLIENT_SECRET;

  // encode in base 64
  const encoded = btoa(`${clientId}:${clientSecret}`);

  const response = await fetch("https://api.notion.com/v1/oauth/token", {
  	method: "POST",
  	headers: {
  	Accept: "application/json",
  	"Content-Type": "application/json",
  	Authorization: `Basic ${encoded}`,
  },
  	body: JSON.stringify({
  		grant_type: "refresh_token",
  		refresh_token: "your-refresh-token",
  	}),
  });
  ...
  ```
</CodeGroup>
