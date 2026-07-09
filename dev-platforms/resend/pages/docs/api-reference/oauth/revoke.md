---
title: "Revoke Token"
source: https://resend.com/docs/api-reference/oauth/revoke
path: docs/api-reference/oauth/revoke
---

POST /oauth/revoke
Disconnect a client by revoking its refresh token.

RFC 7009 token revocation. Revoking a refresh token revokes the entire grant: every access and refresh token issued under it stops working.

Access tokens can't be revoked individually. Revoke the grant's refresh token instead. Per RFC 7009, this endpoint always returns `200` with an empty body.

## Body Parameters

<ParamField type="string">
  The refresh token to revoke.
</ParamField>

<ParamField type="string" />

<ParamField type="string">
  Optional per RFC 7009. If set to `"access_token"`, the request fails: access
  token revocation isn't supported. Any other value (including
  `"refresh_token"`) is accepted and ignored. Unknown hints don't affect
  behavior.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/oauth/revoke' \
       -H 'Content-Type: application/x-www-form-urlencoded' \
       -d 'client_id=550e8400-e29b-41d4-a716-446655440000&token=JcL7aYfE7S9h3L4qv0o2e1w8m6n5b3x9RkP2tD4uV6Q&token_type_hint=refresh_token'
  ```
</RequestExample>

<ResponseExample>
  ```http Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  HTTP/1.1 200 OK
  ```
</ResponseExample>

## Errors

| Status | `error`           | When                                                                         |
| ------ | ----------------- | ---------------------------------------------------------------------------- |
| `400`  | `invalid_request` | `token` or `client_id` is missing, or `token_type_hint` is `"access_token"`. |
| `401`  | `invalid_client`  | Unknown or disabled `client_id`.                                             |
