---
title: "OAuth2PKCEAuth"
source: https://docs.x.com/xdks/python/reference/xdk.oauth2_auth
path: xdks/python/reference/xdk.oauth2_auth
---

Reference for the oauth2_auth Python package in the X API SDK, grouping the client and Pydantic models for the oauth2 auth endpoints of the X API v2.

This module provides OAuth2 PKCE (Proof Key for Code Exchange) authentication
functionality for secure authorization flows. Includes code verifier generation,
token management, and automatic token refresh capabilities.

### `class xdk.oauth2_auth.OAuth2PKCEAuth`

OAuth2 PKCE authentication for the X API.

#### Parameters

<ParamField type="str" />

<ParamField type="str" />

<ParamField type="str or None" />

<ParamField type="str or None" />

<ParamField type="str or None" />

<ParamField type="Dict[str, Any] or None" />

<ParamField type="str or List[str] or None" />

### `__init__`

Initialize the OAuth2 PKCE authentication.

#### Parameters

<ParamField type="str">
  The base URL for the X API token endpoint (defaults to [https://api.x.com](https://api.x.com)).
</ParamField>

<ParamField type="str">
  The base URL for OAuth2 authorization (defaults to [https://x.com/i](https://x.com/i)).
</ParamField>

<ParamField type="str or None">
  The client ID for the X API.
</ParamField>

<ParamField type="str or None">
  The client secret for the X API.
</ParamField>

<ParamField type="str or None">
  The redirect URI for OAuth2 authorization.
</ParamField>

<ParamField type="Dict[str, Any] or None">
  An existing OAuth2 token dictionary (if available).
</ParamField>

<ParamField type="str or List[str] or None">
  Space-separated string or list of strings for OAuth2 authorization scopes.
</ParamField>

### `exchange_code`

Exchange authorization code for tokens (matches TypeScript API).

#### Parameters

<ParamField type="str">
  The authorization code from the callback.
</ParamField>

<ParamField type="str or None">
  Optional code verifier (uses stored verifier if not provided).
</ParamField>

#### Returns

`Dictstr, Any`

### `fetch_token`

Fetch token using authorization response URL (legacy method, uses exchange\_code internally).

#### Parameters

<ParamField type="str">
  The full callback URL received after authorization
</ParamField>

#### Returns

`Dictstr, Any`

### `get_authorization_url`

Get the authorization URL for the OAuth2 PKCE flow.

#### Parameters

<ParamField type="str or None">
  Optional state parameter for security.
</ParamField>

#### Returns

`str`

### `get_code_challenge`

Get the current code challenge (for PKCE).
:returns: The current code challenge, or None if not set.
:rtype: Optional\[str]

#### Returns

`str | None`

### `get_code_verifier`

Get the current code verifier (for PKCE).
:returns: The current code verifier, or None if not set.
:rtype: Optional\[str]

#### Returns

`str | None`

### `is_token_expired`

Check if the token is expired.
:returns: True if the token is expired, False otherwise.
:rtype: bool

#### Returns

`bool`

### `refresh_token`

Refresh the access token.
:returns: The refreshed token dictionary
:rtype: Dict\[str, Any]

#### Returns

`Dictstr, Any`

### `set_pkce_parameters`

Manually set PKCE parameters.

#### Parameters

<ParamField type="str">
  The code verifier to use.
</ParamField>

<ParamField type="str or None">
  Optional code challenge (will be generated if not provided).
</ParamField>
