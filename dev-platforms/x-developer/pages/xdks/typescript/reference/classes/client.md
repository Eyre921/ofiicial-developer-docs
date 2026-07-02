---
title: "Client"
source: https://docs.x.com/xdks/typescript/reference/classes/Client
path: xdks/typescript/reference/classes/client
---

Reference for the main Client class in the X API TypeScript SDK, the entry point exposing specialized clients for every X API v2 endpoint group.

Main client class for the X API

This is the primary entry point for interacting with the X API. It provides
access to all API endpoints through specialized client modules and handles
authentication, request configuration, and error handling.

**`Example`**

```typescript theme={null}
import { Client } from '@xdevplatform/xdk';

const client = new Client({
  bearerToken: 'your-bearer-token'
});

// Get user information
const user = await client.users.getUser('783214');

// Get followers with pagination
const followers = await client.users.getFollowers('783214', {
  maxResults: 10,
  userFields: ['id', 'name', 'username']
});

// Iterate through followers
for await (const follower of followers) {
  console.log(follower.username);
}
```

## Constructors

### constructor

• **new Client**(`config`): [`Client`](/xdks/typescript/reference/classes/Client)

Creates a new X API client instance

#### Parameters

| Name     | Type  | Description                          |
| :------- | :---- | :----------------------------------- |
| `config` | `any` | Configuration options for the client |

#### Returns

[`Client`](/xdks/typescript/reference/classes/Client)

**`Example`**

```typescript theme={null}
// Bearer token authentication
const client = new Client({
  bearerToken: 'your-bearer-token'
});

// OAuth2 authentication
const client = new Client({
  accessToken: 'your-access-token'
});

// OAuth1 authentication
const client = new Client({
  oauth1: oauth1Instance
});
```

[client.ts:401](https://github.com/xdevplatform/xdk-typescript/blob/81aacb165e0802e188f608bdf462b60fc4e713a2/src/client.ts#L401)

## Properties

<ResponseField name="baseUrl" type="string">
  Base URL for API requests
</ResponseField>

<ResponseField name="bearerToken" type="string">
  Bearer token for authentication
</ResponseField>

<ResponseField name="accessToken" type="string">
  OAuth2 access token
</ResponseField>

<ResponseField name="oauth1" type="any">
  OAuth1 instance for authentication
</ResponseField>

<ResponseField name="headers" type="Headers">
  Headers for requests
</ResponseField>

<ResponseField name="timeout" type="number">
  Request timeout in milliseconds
</ResponseField>

<ResponseField name="retry" type="boolean">
  Whether to automatically retry failed requests
</ResponseField>

<ResponseField name="maxRetries" type="number">
  Maximum number of retry attempts
</ResponseField>

<ResponseField name="httpClient" type="HttpClient = httpClient">
  HTTP client for making requests
</ResponseField>

<ResponseField name="general" type="GeneralClient">
  general client
</ResponseField>

<ResponseField name="accountActivity" type="AccountActivityClient">
  account activity client
</ResponseField>

<ResponseField name="communityNotes" type="CommunityNotesClient">
  community notes client
</ResponseField>

<ResponseField name="compliance" type="ComplianceClient">
  compliance client
</ResponseField>

<ResponseField name="connections" type="ConnectionsClient">
  connections client
</ResponseField>

<ResponseField name="users" type="UsersClient">
  users client
</ResponseField>

<ResponseField name="news" type="NewsClient">
  news client
</ResponseField>

<ResponseField name="spaces" type="SpacesClient">
  spaces client
</ResponseField>

<ResponseField name="activity" type="ActivityClient">
  activity client
</ResponseField>

<ResponseField name="usage" type="UsageClient">
  usage client
</ResponseField>

<ResponseField name="trends" type="TrendsClient">
  trends client
</ResponseField>

<ResponseField name="posts" type="PostsClient">
  posts client
</ResponseField>

<ResponseField name="directMessages" type="DirectMessagesClient">
  direct messages client
</ResponseField>

<ResponseField name="communities" type="CommunitiesClient">
  communities client
</ResponseField>

<ResponseField name="media" type="MediaClient">
  media client
</ResponseField>

<ResponseField name="webhooks" type="WebhooksClient">
  webhooks client
</ResponseField>

<ResponseField name="stream" type="StreamClient">
  stream client
</ResponseField>

<ResponseField name="lists" type="ListsClient">
  lists client
</ResponseField>

<ResponseField name="request" type="Promise<T>">
  Make an authenticated request to the X API

  This method handles authentication, request formatting, and error handling
  for all API requests. It automatically adds the appropriate authentication
  headers based on the client configuration.
</ResponseField>

<ResponseField name="isTokenExpired" type="boolean">
  Check if the OAuth2 token is expired
</ResponseField>

<ResponseField name="refreshToken" type="Promise<void>">
  Refresh the OAuth2 token
</ResponseField>

<ResponseField name="isAuthenticated" type="boolean">
  Get the current authentication status
</ResponseField>

<ResponseField name="mapSecuritySchemeToAuthTypes" type="string[]">
  Map OpenAPI security scheme names to internal authentication types
</ResponseField>

<ResponseField name="validateAuthentication" type="void">
  Validate that the required authentication method is available
</ResponseField>

<ResponseField name="getAvailableAuthTypes" type="string[]">
  Get available authentication types
</ResponseField>
