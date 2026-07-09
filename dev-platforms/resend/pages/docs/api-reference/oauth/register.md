---
title: "Register Client"
source: https://resend.com/docs/api-reference/oauth/register
path: docs/api-reference/oauth/register
---

POST /oauth/register
Dynamically register an OAuth client for the authorization code + PKCE flow (RFC 7591).

Dynamic Client Registration (DCR) lets a client obtain a `client_id` at runtime instead of being pre-registered by Resend. This endpoint is unauthenticated (no API key), but only ever issues **public** clients: Resend does not support confidential clients or client secrets.

<Note>
  This endpoint is rate-limited to 20 registrations per hour per IP address.
  Requests over the limit get a `429` with `{"error": "too_many_requests"}`.
</Note>

## Body Parameters

<ParamField type="string">
  A human-readable name for the client. Maximum 200 characters.
</ParamField>

<ParamField type="string[]">
  URIs the authorization server may redirect to after the user approves the
  request. At least one is required, up to 10, each up to 2048 characters. See
  [Allowed redirect URIs](#allowed-redirect-uris) for the rules.
</ParamField>

<ParamField type="string[]">
  Must include `authorization_code`. `refresh_token` is also supported.
</ParamField>

<ParamField type="string[]">
  Only `code` is supported. The value is validated if present but not stored;
  the response always echoes back `["code"]`.
</ParamField>

<ParamField type="string">
  Space-delimited list of scopes to request, e.g. `"emails:send"`. Must be a
  subset of the [supported scopes](/docs/api-reference/oauth/authorize#scopes). If
  omitted, the client is registered with every supported scope.
</ParamField>

<ParamField type="string">
  Only `none` is supported. Resend clients authenticate at the token endpoint
  with PKCE, not a client secret.
</ParamField>

<ParamField type="string">
  A URL for the client's homepage. Echoed back, not otherwise used.
</ParamField>

<ParamField type="string">
  A URL for the client's logo. Shown on the consent screen.
</ParamField>

### Allowed redirect URIs

* `https://` URIs are unrestricted.
* `http://` is only allowed for loopback addresses (`127.0.0.1`, `localhost`,
  `[::1]`), for native/CLI clients that run a local callback server.
* Private-use URI schemes (e.g. `cursor://`, `vscode://`) are allowed, since the
  OS routes them only to the registered native app.
* `file`, `ftp`, `data`, `javascript`, `blob`, `about`, and `vbscript` schemes
  are rejected, and none of the URIs may include a fragment.

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/oauth/register' \
       -H 'Content-Type: application/json' \
       -d $'{
    "client_name": "Example OAuth Client",
    "redirect_uris": ["http://127.0.0.1/oauth/callback"],
    "grant_types": ["authorization_code", "refresh_token"],
    "response_types": ["code"],
    "token_endpoint_auth_method": "none",
    "scope": "emails:send"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "client_id": "550e8400-e29b-41d4-a716-446655440000",
    "client_id_issued_at": 1750000000,
    "client_name": "Example OAuth Client",
    "redirect_uris": ["http://127.0.0.1/oauth/callback"],
    "grant_types": ["authorization_code", "refresh_token"],
    "response_types": ["code"],
    "token_endpoint_auth_method": "none",
    "scope": "emails:send"
  }
  ```
</ResponseExample>

## Errors

Errors use the standard OAuth shape (`{"error": "...", "error_description": "..."}`) rather than Resend's usual [error format](/docs/api-reference/errors).

| Status | `error`             | When                                                                     |
| ------ | ------------------- | ------------------------------------------------------------------------ |
| `400`  | `invalid_request`   | A required field is missing, malformed, or a redirect URI is disallowed. |
| `400`  | `invalid_scope`     | `scope` includes a value outside the supported scope set.                |
| `429`  | `too_many_requests` | More than 20 registrations from this IP in the last hour.                |
