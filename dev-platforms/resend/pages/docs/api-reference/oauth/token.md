---
title: "Token"
source: https://resend.com/docs/api-reference/oauth/token
path: docs/api-reference/oauth/token
---

POST /oauth/token
Exchange an authorization code for tokens, or refresh an access token.

Handles two grants, selected by the `grant_type` body field: `authorization_code` (with mandatory PKCE) and `refresh_token` (with rotation and reuse detection). Accepts both `application/json` and `application/x-www-form-urlencoded`. Prefer form encoding, since that's what most OAuth libraries send by default.

Access tokens are JWTs signed with `ES256`, valid for 900 seconds. Refresh tokens are opaque strings, valid for 60 days from whenever they were last issued, and rotate on every use.

## PKCE

Before starting the [authorization request](/docs/api-reference/oauth/authorize), generate:

* `code_verifier`: a high-entropy random string, 43–128 characters, from the
  unreserved character set (`A-Z`, `a-z`, `0-9`, `-`, `.`, `_`, `~`). Keep it
  client-side only.
* `code_challenge`: the base64url-encoded SHA-256 hash of `code_verifier`,
  sent during authorization.

```javascript theme={"theme":{"light":"github-light","dark":"vesper"}}
import { createHash, randomBytes } from 'node:crypto';

function base64url(input) {
  return Buffer.from(input).toString('base64url');
}

const codeVerifier = base64url(randomBytes(64));
const codeChallenge = base64url(
  createHash('sha256').update(codeVerifier).digest(),
);
```

## Authorization code grant

### Body Parameters

<ParamField type="string">
  Must be `"authorization_code"`.
</ParamField>

<ParamField type="string" />

<ParamField type="string">
  The code from the `/oauth/authorize` callback. Single-use: redeeming it twice
  fails with `invalid_grant`. Expires 10 minutes after it was issued.
</ParamField>

<ParamField type="string">
  Must exactly match the `redirect_uri` used in the authorization request.
</ParamField>

<ParamField type="string">
  The original value that
  [code\_challenge](/docs/api-reference/oauth/authorize#param-code-challenge) was
  derived from.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/oauth/token' \
       -H 'Content-Type: application/x-www-form-urlencoded' \
       -d 'grant_type=authorization_code&client_id=550e8400-e29b-41d4-a716-446655440000&code=AUTHORIZATION_CODE&redirect_uri=http%3A%2F%2F127.0.0.1%3A49152%2Foauth%2Fcallback&code_verifier=CODE_VERIFIER_VALUE'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "access_token": "eyJhbGciOiJFUzI1NiIsImtpZCI6Im9hdXRoX2tleSIsInR5cCI6ImF0K2p3dCJ9...",
    "token_type": "Bearer",
    "expires_in": 900,
    "refresh_token": "JcL7aYfE7S9h3L4qv0o2e1w8m6n5b3x9RkP2tD4uV6Q",
    "scope": "emails:send"
  }
  ```
</ResponseExample>

### Body Parameters

<ParamField type="string">
  Must be `"refresh_token"`.
</ParamField>

<ParamField type="string" />

<ParamField type="string" />

<ParamField type="string">
  Optionally narrow the scope of the new access token. Must be a subset of what
  the grant already has. You can't use this to escalate scope.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/oauth/token' \
       -H 'Content-Type: application/x-www-form-urlencoded' \
       -d 'grant_type=refresh_token&client_id=550e8400-e29b-41d4-a716-446655440000&refresh_token=JcL7aYfE7S9h3L4qv0o2e1w8m6n5b3x9RkP2tD4uV6Q'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "access_token": "eyJhbGciOiJFUzI1NiIsImtpZCI6Im9hdXRoX2tleSIsInR5cCI6ImF0K2p3dCJ9...",
    "token_type": "Bearer",
    "expires_in": 900,
    "refresh_token": "N3wRefreshTokenValue...",
    "scope": "emails:send"
  }
  ```
</ResponseExample>

## Errors

| Status | `error`               | When                                                                                                                                                                                           |
| ------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`  | `invalid_request`     | A required field is missing or malformed.                                                                                                                                                      |
| `400`  | `invalid_scope`       | Refresh requests a scope outside what the grant already has.                                                                                                                                   |
| `400`  | `invalid_grant`       | The code/refresh token is invalid, expired, already used, or reused after rotation (which also revokes the grant). Also returned when PKCE verification fails or `redirect_uri` doesn't match. |
| `401`  | `invalid_client`      | Unknown or disabled `client_id`.                                                                                                                                                               |
| `400`  | `unauthorized_client` | The client isn't registered for the grant type it's using.                                                                                                                                     |
