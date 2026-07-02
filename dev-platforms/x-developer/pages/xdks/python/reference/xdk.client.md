---
title: "Client"
source: https://docs.x.com/xdks/python/reference/xdk.client
path: xdks/python/reference/xdk.client
---

Reference for the client Python package in the X API SDK, grouping the client and Pydantic models for the client endpoints of the X API v2.

This module provides the primary Client class for interacting with the X API.
It coordinates all sub-clients and handles authentication, session management,
and OAuth2 PKCE flows. All functionality is generated from the OpenAPI specification.

## Client

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

\| None = None)

Client for interacting with the X API.

## Constructors

### `__init__`

Initialize the X API client.

#### Parameters

<ParamField type="str">
  The base URL for the X API (defaults to [https://api.x.com](https://api.x.com)).
</ParamField>

<ParamField type="str or None">
  The bearer token for the X API (app-only authentication).
</ParamField>

<ParamField type="str or None">
  The OAuth2 access token for user context (can be used directly as bearer token).
</ParamField>

<ParamField type="str or None">
  The client ID for the X API (required for OAuth2 PKCE flow).
</ParamField>

<ParamField type="str or None">
  The client secret for the X API.
</ParamField>

<ParamField type="str or None">
  The redirect URI for OAuth2 authorization.
</ParamField>

<ParamField type="Dict[str, Any] or None">
  An existing OAuth2 token dictionary (if available). If provided, access\_token will be extracted.
</ParamField>

<ParamField type="str or List[str] or None">
  Space-separated string or list of strings for OAuth2 authorization scopes.
</ParamField>

<ParamField type="str">
  The base URL for OAuth2 authorization (defaults to [https://x.com/i](https://x.com/i)).
</ParamField>

<ParamField type="OAuth1">
  OAuth1 instance for OAuth1.0a authentication.
</ParamField>

#### Parameters

<ParamField type="str" />

<ParamField type="str or None" />

<ParamField type="str or None" />

<ParamField type="str or None" />

<ParamField type="str or None" />

<ParamField type="str or None" />

<ParamField type="Dict[str, Any] or None" />

<ParamField type="str or List[str] or None" />

<ParamField type="str" />

<ParamField type="OAuth1" />

### `exchange_code`

Exchange authorization code for tokens (matches TypeScript API).

#### Parameters

<ParamField type="Any">
  The authorization code from the callback.
</ParamField>

<ParamField type="Any">
  Optional code verifier (uses stored verifier if not provided).
</ParamField>

### `fetch_token`

Fetch token using authorization response URL (legacy method).

#### Parameters

<ParamField type="Any">
  The full callback URL received after authorization.
</ParamField>

### `get_authorization_url`

Get the authorization URL for the OAuth2 PKCE flow.

#### Parameters

<ParamField type="Any">
  Optional state parameter for security.
</ParamField>

### `is_token_expired`

Check if the OAuth2 token is expired.

### `refresh_token`

Refresh the OAuth2 token.
