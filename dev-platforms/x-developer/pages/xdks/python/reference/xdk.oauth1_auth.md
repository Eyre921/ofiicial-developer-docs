---
title: "oauth1_auth"
source: https://docs.x.com/xdks/python/reference/xdk.oauth1_auth
path: xdks/python/reference/xdk.oauth1_auth
---

Reference for the oauth1_auth Python package in the X API SDK, grouping the client and Pydantic models for the oauth1 auth endpoints of the X API v2.

This module provides OAuth1.0a authentication functionality for secure
authorization flows. Includes request token generation, authorization URL
generation, access token exchange, and OAuth1 signature generation.

### `class xdk.oauth1_auth.OAuth1`

OAuth1 authentication handler for the X API.

#### Parameters

<ParamField type="str" />

<ParamField type="str" />

<ParamField type="str" />

<ParamField type="str or None" />

<ParamField type="str or None" />

### `__init__`

Initialize OAuth1 authentication.

#### Parameters

<ParamField type="str">
  API Key (Consumer Key).
</ParamField>

<ParamField type="str">
  API Secret (Consumer Secret).
</ParamField>

<ParamField type="str">
  Callback URL for OAuth flow.
</ParamField>

<ParamField type="str or None">
  Access Token (if already obtained).
</ParamField>

<ParamField type="str or None">
  Access Token Secret (if already obtained).
</ParamField>

### `build_request_header`

Build OAuth1 authorization header for API requests.

#### Parameters

<ParamField type="str">
  HTTP method (GET, POST, etc.).
</ParamField>

<ParamField type="str">
  Request URL (may include query parameters).
</ParamField>

<ParamField type="str">
  Request body (form-encoded string or empty).
</ParamField>

#### Returns

`str`

### `get_access_token`

Exchange verifier for access token.

#### Parameters

<ParamField type="str">
  OAuth verifier from callback or PIN.
</ParamField>

#### Returns

`OAuth1AccessToken`

### `get_authorization_url`

Get the authorization URL for OAuth1 flow.

#### Parameters

<ParamField type="bool">
  Whether to use “Log in with X” flow.
</ParamField>

#### Returns

`str`

### `get_request_token`

Get request token to start OAuth1 flow.
:returns: Request token with oauth\_token and oauth\_token\_secret.
:rtype: OAuth1RequestToken

#### Returns

`OAuth1RequestToken`

### `start_oauth_flow`

Convenience method to start the OAuth1 flow.

#### Parameters

<ParamField type="bool">
  Whether to use “Log in with X” flow.
</ParamField>

#### Returns

`str`

### `class xdk.oauth1_auth.OAuth1AccessToken`

OAuth1 access token response.

#### Parameters

<ParamField type="str" />

<ParamField type="str" />

### `__init__`

Initialize OAuth1 access token.

#### Parameters

<ParamField type="str">
  The access token.
</ParamField>

<ParamField type="str">
  The access token secret.
</ParamField>

### `class xdk.oauth1_auth.OAuth1RequestToken`

OAuth1 request token response.

#### Parameters

<ParamField type="str" />

<ParamField type="str" />

### `__init__`

Initialize OAuth1 request token.

#### Parameters

<ParamField type="str">
  The OAuth token.
</ParamField>

<ParamField type="str">
  The OAuth token secret.
</ParamField>
