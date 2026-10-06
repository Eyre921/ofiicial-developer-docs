---
title: "Enterprise-managed authorization"
source: https://developers.notion.com/guides/mcp/enterprise-managed-authorization
path: guides/mcp/enterprise-managed-authorization
---

Reference for getting Notion MCP access tokens with an identity provider's ID-JAG instead of the browser OAuth flow.

Notion MCP accepts an **ID-JAG** (Identity Assertion JWT Authorization Grant) at its token endpoint. An ID-JAG is a short-lived JWT that your company's identity provider (IdP) signs for one user and one MCP client. Your MCP client trades it for a Notion MCP access token without opening a browser or showing a consent screen.

This page lists what Notion checks and what it returns. It's for developers of MCP clients and identity providers. The protocol itself is defined in two specs, and this page doesn't restate them:

* [Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) (IETF draft)
* [MCP enterprise-managed authorization extension](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/stable/enterprise-managed-authorization.mdx)

For the interactive OAuth flow, see [Build an MCP client](/guides/mcp/build-mcp-client).

## Requirements

Enterprise-managed authorization is part of the Enterprise plan. The workspace must use SAML SSO.

An admin turns on **Enterprise-managed connections** in Notion's settings and enters the identity provider issuer URL. That URL must be a plain `https` URL with no query string, fragment, or credentials. It must also be on the host of the IdP that runs the workspace's SAML SSO. Each issuer is bound to exactly one workspace.

Notion checks this binding every time it issues a token and every time a token is used. If an admin turns the setting off, removes SAML SSO, moves to a different IdP, or the workspace leaves the Enterprise plan, existing tokens stop working.

## Token endpoint

| Item | Value |
| - | - |
| Authorization server metadata | `https://mcp.notion.com/.well-known/oauth-authorization-server` |
| Token endpoint | `https://mcp.notion.com/token` |
| Grant type | `urn:ietf:params:oauth:grant-type:jwt-bearer` |
| Grant profile | `urn:ietf:params:oauth:grant-profile:id-jag` |
| MCP resource | `https://mcp.notion.com/mcp` |

The metadata document lists the grant type in `grant_types_supported` and the grant profile in `authorization_grant_profiles_supported`.

Your MCP client needs a client ID before it can call the token endpoint. Register with [dynamic client registration](https://datatracker.ietf.org/doc/html/rfc7591) at `https://mcp.notion.com/register`, or use a client ID metadata document. The registration must include at least one redirect URI, even though this grant never redirects. Notion uses it to match the connection to the same client settings as an interactive connection. Without one, the exchange fails.

Public clients (`token_endpoint_auth_method` of `none`) are allowed, and they send `client_id` in the form body. Confidential clients use the method they registered. With `client_secret_basic`, send the client ID and secret in an HTTP Basic `Authorization` header, and leave both out of the form body. With `client_secret_post`, send `client_id` and `client_secret` in the form body.

### Request

Send a form-encoded `POST` to the token endpoint.

| Parameter | Required | Value |
| - | - | - |
| `grant_type` | Yes | `urn:ietf:params:oauth:grant-type:jwt-bearer` |
| `assertion` | Yes | The ID-JAG as a compact JWT, 16 KB or smaller. |
| `client_id` | `none` and `client_secret_post` | The client ID from registration. |
| `client_secret` | `client_secret_post` | The client secret from registration. |
| `scope` | No | Space-separated OAuth scopes. Notion MCP doesn't need any, so you can leave it out. If the ID-JAG has a `scope` claim, Notion drops any requested scope that isn't in it. |

```bash theme={null}
curl https://mcp.notion.com/token \
  --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer" \
  --data-urlencode "client_id=$NOTION_MCP_CLIENT_ID" \
  --data-urlencode "assertion=$ID_JAG"
```

### Response

A successful exchange returns JSON:

```json theme={null}
{
  "access_token": "...",
  "token_type": "bearer",
  "expires_in": 28800,
  "scope": "",
  "resource": "https://mcp.notion.com/mcp"
}
```

There's no `refresh_token`. When the access token expires, get a new ID-JAG from the IdP and exchange it again. Use `expires_in` to schedule that. Don't assume a fixed value: the default is 8 hours, but Notion can change it.

Treat the access token as a secret. Don't put it in browser page source, client bundles, logs, or public repositories.

## ID-JAG header

| Field | Requirement |
| - | - |
| `typ` | Must be exactly `oauth-id-jag+jwt`. |
| `alg` | Must be `RS256` or `ES256`. Notion rejects other algorithms, including `none`. |
| `kid` | Recommended. If present, it must match a key in the IdP's JWKS. If absent, the JWKS must have exactly one key that fits. |

## ID-JAG claims

| Claim | Required | Requirement |
| - | - | - |
| `iss` | Yes | Exactly the issuer URL the admin configured, character for character, including any trailing slash. |
| `sub` | Yes | The user's stable ID at the IdP. |
| `aud` | Yes | `https://mcp.notion.com`. A string, or an array with exactly one value. |
| `client_id` | Yes | The same client ID the MCP client uses at the token endpoint. |
| `jti` | Yes | A unique ID for this assertion. |
| `exp` | Yes | Expiry time, as an integer number of seconds since the Unix epoch. |
| `iat` | Yes | Issue time, as an integer number of seconds since the Unix epoch. |
| `nbf` | No | Not-before time, as an integer. |
| `resource` | No | If present, it must be exactly `https://mcp.notion.com/mcp`. If absent, Notion uses `https://mcp.notion.com/mcp`. Other values can fail at the token endpoint, or return a token that `/mcp` rejects. |
| `email` | First exchange | The user's email. See [How Notion finds the user](#how-notion-finds-the-user). |
| `scope` | No | Space-separated OAuth scopes. |
| `cnf` | Must be absent | Notion doesn't support sender-constrained (DPoP) tokens. |
| `authorization_details` | Must be absent | Notion doesn't support rich authorization requests. |

All required string claims must be non-empty strings.

### Lifetime and clock skew

Notion allows 60 seconds of clock skew. With that allowance:

* `iat` can be at most 60 seconds in the future.
* `nbf`, if present, can be at most 60 seconds in the future.
* `exp` minus `iat` can be at most 360 seconds (a 300-second limit plus skew). Give ID-JAGs a lifetime of 5 minutes or less.
* The assertion must not have expired when Notion issues the token. An assertion that expires during the exchange fails with `Assertion has expired`.

### Replay

Treat each ID-JAG as single-use. Notion records each `iss` and `jti` pair until at least the assertion's `exp`, and rejects a later exchange with the same pair. This check is best-effort: two exchanges of the same assertion sent at the same moment, or through different regions before the record propagates, can both succeed. Don't rely on it as your only replay defense. Have the IdP use a new `jti` for every assertion, and have the client get a new ID-JAG for every exchange, including retries.

## Signing keys

Notion finds the IdP's signing keys with OpenID Connect discovery. It doesn't accept a JWKS URL in configuration.

1. Notion fetches `<issuer>/.well-known/openid-configuration`. It appends the path to the issuer, so an issuer with a path, like `https://example.okta.com/oauth2/default`, works. Redirects aren't followed.
2. Notion reads `jwks_uri` from that document. The `jwks_uri` must have the same origin as the issuer.
3. Notion fetches the JWKS. It must be JSON with a `keys` array, 64 KB or smaller.

Each fetch times out after 10 seconds. Notion sends `User-Agent: notion-hosted-mcp` on both fetches. If your IdP sits behind a firewall or bot filter that blocks requests by user agent, allow that value.

Notion caches the discovery result for 10 minutes and the JWKS for 5 minutes. When an ID-JAG has a `kid` that isn't in the cached JWKS, Notion refetches the JWKS once, at most every 30 seconds per issuer. Publish a new key in the JWKS before you start signing with it.

For `RS256`, the key must be an RSA key. For `ES256`, it must be an EC key on the P-256 curve. If the key has `use`, `key_ops`, or `alg`, they must allow signature verification with the ID-JAG's `alg`.

## How Notion finds the user

Notion maps the ID-JAG to a user in the workspace bound to the issuer.

On the first exchange for an `iss` and `sub` pair, Notion looks up the Notion account with the email in the `email` claim. If it finds one, Notion links that `iss` and `sub` pair to the account. After that, `sub` is what counts. Later exchanges find the user by `iss` and `sub`, even if the email changes or is left out.

The exchange fails if any of these is true:

* The `iss` and `sub` pair has no link yet and the ID-JAG has no `email` claim.
* No Notion account has that email.
* The email belongs to an account already linked to a different `sub` from the same issuer.
* The user isn't a member of the bound workspace.
* An admin has denied the user's enterprise-managed access. Admins can do this with the [update enterprise-managed access endpoint](/reference/admin/update-mcp-client-connection-enterprise-managed-access).

## What the token can do

The access token works with the Notion MCP server at `https://mcp.notion.com/mcp`. Send it as a bearer token in the `Authorization` header. It acts as the mapped user in the bound workspace, and it can reach the same content as a connection that the user authorized through the browser flow. The connection shows up in the workspace's list of MCP client connections, marked as enterprise-managed.

Notion checks the issuer binding and the user's access on every request. If either no longer allows the user, the token stops working before it expires.

The first connection for a user records an MCP server connected event. Changes to enterprise-managed settings and to member access are recorded too. See [Audit log events](/compliance/audit-log-events) and [SIEM events](/compliance/siem-events).

## Errors

Error responses use the OAuth format: a JSON body with `error` and `error_description`.

| Status | `error` | `error_description` | Meaning |
| - | - | - | - |
| 400 | `invalid_request` | `assertion is required` | The `assertion` parameter is missing or empty. |
| 400 | `invalid_request` | `Invalid scope parameter format` | The `scope` parameter isn't valid OAuth scope syntax. |
| 400 | `invalid_target` | `Invalid resource` | The `resource` claim isn't a valid URI or isn't `https://mcp.notion.com/mcp`. |
| 400 | `invalid_grant` | `Invalid assertion` | The ID-JAG failed a format, issuer, signature, claim, or replay check. |
| 400 | `invalid_grant` | `Assertion was not authorized` | The ID-JAG was valid, but Notion didn't issue a token for it. |
| 400 | `invalid_grant` | `Assertion has expired` | The ID-JAG expired while Notion processed it. |
| 401 | `invalid_client` | `Client not found` | The client ID isn't registered. |

`Invalid assertion` means the ID-JAG itself failed a check. `Assertion was not authorized` means the ID-JAG passed those checks, but Notion refused it. Common reasons are that Notion couldn't map it to a workspace member, the user's access is denied, the ID-JAG has a `cnf` or `authorization_details` claim, `aud` is an array with more than one value, or the client has no redirect URI.

Notion keeps these messages generic on purpose. A more specific message would let anyone with a forged or stolen assertion learn which issuers are configured and which users exist. Notion doesn't say which check failed, and a request that names an untrusted issuer gets the same response as one with a bad signature.

### Common causes of `invalid_grant`

These failures all return `Invalid assertion`. Check the item in the right column.

| Failed check | What to check |
| - | - |
| Malformed or too large | The assertion is a compact JWT with three non-empty parts and is 16 KB or smaller. |
| Wrong `typ` | The header `typ` is `oauth-id-jag+jwt`. |
| Wrong `alg` | The header `alg` is `RS256` or `ES256`. |
| Issuer not trusted | `iss` exactly matches the configured issuer URL, enterprise-managed connections are on, the workspace is on the Enterprise plan, and the issuer is on the SAML SSO IdP's host. Discovery failures also land here: `<issuer>/.well-known/openid-configuration` must return 200 without a redirect, with a `jwks_uri` on the issuer's origin. |
| JWKS fetch failed | `jwks_uri` returns 200 with a JSON `keys` array of 64 KB or less, and doesn't block the `notion-hosted-mcp` user agent. |
| No matching key | The header `kid` is in the JWKS, and the key type fits `alg`: RSA for `RS256`, EC P-256 for `ES256`. Without a `kid`, the JWKS has only one matching key. |
| Signature failed | The IdP signed the assertion with the private key for the JWKS key that matches `kid`. |
| Missing or invalid claim | `iss`, `sub`, `aud`, `client_id`, and `jti` are non-empty strings. `exp`, `iat`, and `nbf` are integers. `scope` is valid scope syntax. |
| Audience mismatch | `aud` is `https://mcp.notion.com`. |
| Client ID mismatch | `client_id` equals the client ID sent to the token endpoint. |
| Expired | `exp` is in the future. Check the IdP's clock. |
| Issued or valid in the future | `iat` and `nbf` are no more than 60 seconds ahead of Notion's clock. |
| Lifetime too long | `exp` minus `iat` is 360 seconds or less. |
| Replayed | `jti` is new for every assertion, and the client gets a new ID-JAG for each exchange. |
