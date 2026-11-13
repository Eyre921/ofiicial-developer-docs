---
title: "Build an MCP client for Notion"
source: https://developers.notion.com/guides/mcp/build-mcp-client
path: guides/mcp/build-mcp-client
---

Connect your app or AI assistant to Notion MCP with OAuth 2.0, PKCE, and support for Notion’s tools.

Build an
[MCP client](https://modelcontextprotocol.io/docs/develop/build-client) that
connects to [Notion MCP](/guides/mcp/overview) using OAuth 2.0 with
[PKCE](https://oauth.net/2/pkce/).

## Connection requirements

Notion provides a hosted
[MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction)
server that lets MCP clients work with Notion workspaces. Use Streamable HTTP at `https://mcp.notion.com/mcp`. If your client uses the deprecated `/sse` endpoint, [migrate to Streamable HTTP](/guides/mcp/get-started-with-mcp#migrate-from-the-legacy-sse-endpoint).

Your client must support:

* OAuth 2.0 Authorization Code flow with PKCE
* Streamable HTTP (`/mcp`)
* Token refresh handling
* Secure credential storage

## Prerequisites

> [!NOTE]
>
> This guide uses TypeScript/JavaScript examples, but the concepts apply to any
> programming language. The OAuth 2.0 flow, PKCE implementation, and MCP
> protocol are language-agnostic.

**Required libraries (TypeScript/JavaScript):**

```bash npm theme={null}
npm install @modelcontextprotocol/client@2
```

```bash TypeScript types theme={null}
npm install --save-dev @types/node
```

### Alternative libraries for other languages

> [accordion] Python
>
> * **MCP SDK**: [python-sdk](https://github.com/modelcontextprotocol/python-sdk) (official)
> * **OAuth 2.0**: [`authlib`](https://docs.authlib.org) (recommended) or [`requests-oauthlib`](https://requests-oauthlib.readthedocs.io)
> * **PKCE**: Built into both `authlib` and `requests-oauthlib`

> [accordion] Go
>
> * **MCP SDK**: [go-sdk](https://github.com/modelcontextprotocol/go-sdk) (official)
> * **OAuth 2.0**: [`golang.org/x/oauth2`](https://pkg.go.dev/golang.org/x/oauth2) (official extended package)
> * **PKCE**: Supported via `oauth2.SetAuthURLParam("code_challenge", ...)` and `oauth2.SetAuthURLParam("code_challenge_method", "S256")`

> [accordion] Rust
>
> * **MCP SDK**: [rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) (official)
> * **OAuth 2.0**: [`oauth2`](https://docs.rs/oauth2) crate
> * **PKCE**: Built into `oauth2` crate via `PkceCodeChallenge` and `PkceCodeVerifier`

> [accordion] Java
>
> * **MCP SDK**: Use HTTP client libraries (Apache HttpClient, OkHttp, or Java 11+ `HttpClient`)
> * **OAuth 2.0**: [`Spring Security OAuth2`](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html) (recommended) or [`ScribeJava`](https://github.com/scribejava/scribejava)
> * **PKCE**: Built into Spring Security OAuth2 Client; supported in ScribeJava via `PKCE` configuration

> [accordion] C# / .NET
>
> * **MCP SDK**: Use `HttpClient` with [`System.Net.Http.Json`](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.json)
> * **OAuth 2.0**: [`IdentityModel.OidcClient`](https://github.com/IdentityModel/IdentityModel.OidcClient) or [`Microsoft.Identity.Web`](https://learn.microsoft.com/en-us/azure/active-directory/develop/microsoft-identity-web)
> * **PKCE**: Built into both libraries

> [accordion] Ruby
>
> * **MCP SDK**: Use `Net::HTTP` (standard library) or [`Faraday`](https://lostisland.github.io/faraday/)
> * **OAuth 2.0**: [`oauth2`](https://github.com/oauth-xx/oauth2) gem
> * **PKCE**: Supported via `oauth2` gem with appropriate configuration

### Key references

* [MCP specification, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
  * [Building an MCP client](https://modelcontextprotocol.io/docs/develop/build-client)
* [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) — OAuth 2.0 Authorization Framework
* [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636) — PKCE (Proof Key for Code Exchange)
* [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) — OAuth 2.0 Authorization Server Metadata
* [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728) — OAuth 2.0 Protected Resource Metadata

## Step 1: OAuth discovery

Discover the OAuth issuer and endpoints before redirecting the user. An unauthenticated request to `https://mcp.notion.com/mcp` returns a `401` with a `WWW-Authenticate` header. Its `resource_metadata` URL points to Notion's [protected resource metadata](https://mcp.notion.com/.well-known/oauth-protected-resource/mcp). That document identifies the resource and its authorization server. The [authorization server metadata](https://mcp.notion.com/.well-known/oauth-authorization-server) lists the endpoints and supported authentication methods.

The TypeScript SDK handles metadata discovery and issuer validation. This example is for Notion's hosted endpoint.

```typescript theme={null}
import { discoverOAuthServerInfo, type AuthorizationServerMetadata } from "@modelcontextprotocol/client"

type OAuthMetadata = AuthorizationServerMetadata
const mcpUrl = new URL("https://mcp.notion.com/mcp")

const { resourceMetadata, authorizationServerMetadata: metadata } =
  await discoverOAuthServerInfo(mcpUrl)

if (resourceMetadata?.resource !== mcpUrl.href ||
    metadata?.issuer !== mcpUrl.origin ||
    !metadata.authorization_endpoint ||
    !metadata.code_challenge_methods_supported?.includes("S256")) {
  throw new Error("Could not verify Notion's OAuth configuration")
}
```

## Step 2: Generate PKCE parameters

PKCE (Proof Key for Code Exchange) is mandatory for secure OAuth flows.
Generate a code verifier and challenge:

```typescript TypeScript theme={null}
import { randomBytes, createHash } from "crypto"

function base64URLEncode(str: Buffer): string {
  return str
    .toString("base64")
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=/g, "")
}

function generateCodeVerifier(): string {
  // Generate 32 random bytes = 256 bits
  // Base64 encoding produces ~43 characters
  const bytes = randomBytes(32)
  return base64URLEncode(bytes)
}

function generateCodeChallenge(verifier: string): string {
  const hash = createHash("sha256").update(verifier).digest()
  return base64URLEncode(hash)
}

// Usage
const codeVerifier = generateCodeVerifier()
const codeChallenge = generateCodeChallenge(codeVerifier)

// Store codeVerifier securely - you'll need it for token exchange
```

> [!WARNING]
>
> The `codeVerifier` must be kept secret and never sent to the authorization
> server until the token exchange step. Store it securely (encrypted session,
> secure cookie, or in-memory with short expiry).

## Step 3: Dynamic client registration

Reuse your existing client ID for this issuer. If you distribute a new client, you can publish a Client ID Metadata Document (CIMD) at a public HTTPS URL. Use the document URL as your client ID when the issuer advertises `client_id_metadata_document_supported: true`. Include that exact URL as `client_id` in the document, along with your client name and registered redirect URIs. See [MCP client registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration).

If you have neither an existing registration nor a metadata document, use the advertised `registration_endpoint` for dynamic client registration. Register once and store the result per issuer. This example registers a public client:

```typescript TypeScript theme={null}
type ClientRegistration = {
  client_name: string
  client_uri?: string
  redirect_uris: string[]
  grant_types: string[]
  response_types: string[]
  token_endpoint_auth_method: string
  scope?: string
}

type ClientCredentials = {
  client_id: string
  client_secret?: string
  client_id_issued_at?: number
  client_secret_expires_at?: number
}

async function registerClient(
  metadata: OAuthMetadata,
  redirectUri: string
): Promise<ClientCredentials> {
  if (!metadata.registration_endpoint) {
    throw new Error("Server does not support dynamic client registration")
  }

  const registrationRequest: ClientRegistration = {
    client_name: "Your MCP Client",
    client_uri: "https://example.com",
    redirect_uris: [redirectUri],
    grant_types: ["authorization_code", "refresh_token"],
    response_types: ["code"],
    token_endpoint_auth_method: "none",
  }

  const response = await fetch(metadata.registration_endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(registrationRequest),
  })

  if (!response.ok) {
    const errorBody = await response.text()
    throw new Error(
      `Client registration failed: ${response.status} - ${errorBody}`
    )
  }

  const credentials = await response.json()
  if (typeof credentials.client_id !== "string") throw new Error("Missing client ID")
  return credentials
}
```

## Step 4: Initiate authorization flow

Redirect the user to the authorization endpoint with PKCE parameters. Include the protected resource URL as `resource` in the authorization request and token exchange. This binds the access token to Notion MCP.

```typescript TypeScript theme={null}
function buildAuthorizationUrl(
  metadata: OAuthMetadata,
  clientId: string,
  redirectUri: string,
  codeChallenge: string,
  state: string,
  scopes: string[] = []
): string {
  if (!metadata.authorization_endpoint) throw new Error("Missing authorization endpoint")

  const params = new URLSearchParams({
    response_type: "code",
    resource: mcpUrl.href,
    client_id: clientId,
    redirect_uri: redirectUri,
    scope: scopes.join(" "),
    state: state,
    code_challenge: codeChallenge,
    code_challenge_method: "S256",
    prompt: "consent",
  })

  return `${metadata.authorization_endpoint}?${params.toString()}`
}

function generateState(): string {
  return randomBytes(32).toString("hex")
}

// Usage
const state = generateState()
const authorizationUrl = buildAuthorizationUrl(
  metadata,
  clientId,
  redirectUri,
  codeChallenge,
  state
)

// Store state and codeVerifier in secure session storage
// Redirect user to authorizationUrl
window.location.href = authorizationUrl // Browser redirect
```

> [!WARNING]
>
> **Security best practices:**
>
> * Always use HTTPS for redirect URIs in production
> * Store `state` and `codeVerifier` securely (encrypted session storage)
> * Set a short expiry (10 minutes) for stored values
> * Validate `state` on callback to prevent CSRF attacks

## Step 5: Handle OAuth callback

After user authorizes, they'll be redirected back to your `redirectUri` with an
authorization code:

```typescript TypeScript theme={null}
interface CallbackParams {
  code?: string
  state?: string
  iss?: string
  error?: string
  error_description?: string
}

function parseCallback(url: string): CallbackParams {
  const urlParams = new URLSearchParams(new URL(url).search)

  return {
    code: urlParams.get("code") || undefined,
    state: urlParams.get("state") || undefined,
    iss: urlParams.get("iss") || undefined,
    error: urlParams.get("error") || undefined,
    error_description: urlParams.get("error_description") || undefined,
  }
}

function handleCallback(callbackUrl: string, storedState: string): string {
  const params = parseCallback(callbackUrl)

  if (params.iss !== mcpUrl.origin) {
    throw new Error("Unexpected authorization server")
  }

  if (params.state !== storedState) {
    throw new Error("Invalid state parameter - possible CSRF attack")
  }

  if (params.error) throw new Error(`Authorization failed: ${params.error}`)
  if (!params.code) {
    throw new Error("Missing authorization code")
  }

  return params.code
}
```

## Step 6: Exchange authorization code for tokens

Exchange the authorization code for access and refresh tokens. The examples use the public client from step 3. A confidential client must authenticate with its registered token endpoint method.

```typescript TypeScript theme={null}
type TokenResponse = {
  access_token: string
  token_type: string
  expires_in?: number
  refresh_token?: string
  scope?: string
  // Identity fields, sent only on authorization-code exchanges
  user_id?: string
  workspace_id?: string
  email_domain?: string
  bot_id?: string
  workspace_name?: string | null
  workspace_icon?: string | null
}

async function exchangeCodeForTokens(
  code: string,
  codeVerifier: string,
  metadata: OAuthMetadata,
  clientId: string,
  redirectUri: string
): Promise<TokenResponse> {
  const params = new URLSearchParams({
    grant_type: "authorization_code",
    resource: mcpUrl.href,
    code: code,
    client_id: clientId,
    redirect_uri: redirectUri,
    code_verifier: codeVerifier,
  })

  const response = await fetch(metadata.token_endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      Accept: "application/json",
      "User-Agent": "YourApp-MCP-Client/1.0",
    },
    body: params.toString(),
  })

  if (!response.ok) {
    const errorBody = await response.text()
    throw new Error(
      `Token exchange failed: ${response.status} - ${errorBody}`
    )
  }

  const tokens = await response.json()

  if (!tokens.access_token) {
    throw new Error("Missing access_token in response")
  }

  return tokens
}
```

A successful authorization-code exchange also says who connected. Refresh
responses don't include these fields, so store them from the first exchange.

| Field | Type | Description |
| - | - | - |
| `user_id` | `string` | ID of the Notion user who authorized the connection. |
| `workspace_id` | `string` | ID of the connected workspace. |
| `email_domain` | `string` | Lowercased domain of the user's email address. |
| `bot_id` | `string` | ID of the Notion authorization behind this connection. |
| `workspace_name` | `string` or `null` | Display name of the workspace. |
| `workspace_icon` | `string` or `null` | Icon for the workspace, usually an image URL. |

`user_id` and `workspace_id` come as a pair. If Notion can't resolve them, the
response has none of these fields. `email_domain` is left out when the user has
no email address. `bot_id`, `workspace_name`, and `workspace_icon` are left out
when Notion doesn't have the connection's details, and the two workspace fields
can be `null`. To get the user's name or email address, or to look up identity
later, see [Identify the connected workspace](#identify-the-connected-workspace).

> [!NOTE]
>
> Notion may add fields to the token response over time. Parse it leniently
> and [ignore fields you don't recognize](/reference/versioning#what-we-consider-backwards-compatible).

> [!WARNING]
>
> **Token storage security:**
>
> * **Web applications:** Store tokens server-side only, never in localStorage
>   or cookies
> * **Desktop applications:** Use secure credential storage (Keychain on macOS,
>   Credential Manager on Windows)
> * **Mobile applications:** Use secure keychain/keystore APIs
> * Always encrypt tokens at rest

## Step 7: Connect to MCP server with authentication

Use the v2 TypeScript client and select the July 2026 protocol. The SDK's default mode uses the 2025 handshake. With the version pinned, the SDK calls `server/discover` and adds the July metadata and matching HTTP headers to subsequent requests.

```typescript theme={null}
import { Client, StreamableHTTPClientTransport } from "@modelcontextprotocol/client"

async function createMcpClient(accessToken: string): Promise<Client> {
  const client = new Client(
    { name: "notion-workspace-client", version: "1.0.0" },
    { versionNegotiation: { mode: { pin: "2026-07-28" } } }
  )
  await client.connect(new StreamableHTTPClientTransport(mcpUrl, {
    requestInit: { headers: { Authorization: `Bearer ${accessToken}` } },
  }))
  return client
}
```

### Send a request without an SDK

You can start with `tools/list` immediately. To discover server capabilities first, send `server/discover`. Each POST carries its own version, client capabilities, and bearer token. This request lists the tools visible to the connection. Set `NOTION_MCP_ACCESS_TOKEN` to the access token from step 6 in your local shell.

```bash theme={null}
curl --fail-with-body https://mcp.notion.com/mcp \
  -H "Authorization: Bearer $NOTION_MCP_ACCESS_TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2026-07-28' \
  -H 'Mcp-Method: tools/list' \
  --data '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {
      "_meta": {
        "io.modelcontextprotocol/protocolVersion": "2026-07-28",
        "io.modelcontextprotocol/clientCapabilities": {},
        "io.modelcontextprotocol/clientInfo": {"name": "notion-workspace-client", "version": "1.0.0"}
      }
    }
  }'
```

Read the response as JSON or as a request-scoped event stream, according to its `Content-Type`. Notion returns HTTP 405 for a standalone `GET /mcp`; send the POST directly. For a completed list, read `result.tools` and use the exact names it returns. Honor `result.ttlMs` when caching. A `private` catalog belongs to the authorized connection, and a TTL of zero means fetch the list again. See [list tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#listing-tools).

For `tools/call` and `prompts/get`, also send `Mcp-Name` with the value of `params.name`. For `resources/read`, use `params.uri`. If a tool schema declares `x-mcp-header`, mirror the parameter as the spec directs. Missing or mismatched headers can return HTTP 400. If the server returns `UnsupportedProtocolVersionError`, choose a version both sides support from the error data. See the [Streamable HTTP rules](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http).

### Session ids on the Streamable HTTP endpoint

July 2026 clients send self-contained requests. Skip `initialize`, `notifications/initialized`, and `Mcp-Session-Id`. Use `server/discover` to check advertised capabilities before using optional features.

Clients using a 2025 protocol revision still connect to the same `/mcp` URL. They initialize first and echo any `Mcp-Session-Id` returned by Notion. The SDK handles this when you select the older protocol. See [version negotiation](https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle).

### Identify the connected workspace

Use the [token response fields](#step-6-exchange-authorization-code-for-tokens)
first. They give you `user_id` and `workspace_id` without another request.
For a user-authorized connection, call `notion-get-self` with an empty object to
read the person who connected, including their name and email when available.
If `user.type` is `bot`, the connection acts as a workspace bot and no person
email is available; use `user_id` from the authorization-code token response to
identify the person who authorized the connection.

```typescript TypeScript theme={null}
const result = await client.callTool({
  name: "notion-get-self",
  arguments: {},
})

const [block] = result.content
if (result.isError || block?.type !== "text") {
  throw new Error("Could not read identity from notion-get-self")
}

const { workspace, user } = JSON.parse(block.text)
console.log(workspace.id, workspace.name)
console.log(user.type, user.id, user.name, user.email)
```

The text block contains a JSON object with stable `workspace` and `user`
fields. See [Supported tools](/guides/mcp/mcp-supported-tools) for their shapes.

Older clients can still call `notion-fetch` with the id `self`. That response
puts the same identity under a `self` field. New clients should use
`notion-get-self`.

An MCP access token works only with Notion MCP. Don't send it to the REST API,
for example to `GET /v1/users/me`.

OpenID Connect (OIDC) is the standard OAuth option for receiving identity in
an ID token or from a UserInfo endpoint. It isn't available from Notion MCP
yet. If Notion enables OIDC for your client, request `openid`. Add `profile`
for the user's name and `email` for the user's verified email address. Notion
grants these identity scopes only to clients the Notion team allows. The
consent page tells the user, “See your name and email address.” Notion omits
the email claim when the email isn't verified.

To check whether a token is still active, and who it belongs to, send it to
the `introspection_endpoint` from the
[authorization server metadata](#step-1-oauth-discovery). This endpoint follows
[RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662). Send a `POST` with
a form-encoded `token` parameter, and authenticate with the same method you
use at the token endpoint. Public clients send only `client_id`. A client can
only introspect its own tokens.

```typescript TypeScript theme={null}
type TokenIntrospectionResponse = {
  active: boolean
  client_id?: string
  scope?: string
  token_type?: "bearer"
  exp?: number
  iat?: number
  sub?: string
  aud?: string | string[]
  iss?: string
  user_id?: string
  workspace_id?: string
}

type TokenEndpointAuthMethod =
  | "client_secret_basic"
  | "client_secret_post"
  | "none"

async function introspectToken(
  token: string,
  metadata: OAuthMetadata,
  clientId: string,
  tokenEndpointAuthMethod: TokenEndpointAuthMethod,
  clientSecret: string | undefined
): Promise<TokenIntrospectionResponse> {
  if (!("introspection_endpoint" in metadata) || typeof metadata.introspection_endpoint !== "string") {
    throw new Error("Authorization server does not support token introspection")
  }

  const body = new URLSearchParams({ token })
  const headers = new Headers({
    "Content-Type": "application/x-www-form-urlencoded",
    Accept: "application/json",
  })

  if (tokenEndpointAuthMethod === "client_secret_basic") {
    if (!clientSecret) {
      throw new Error("Client secret is required for client_secret_basic")
    }
    const credentials = `${encodeURIComponent(clientId)}:${encodeURIComponent(clientSecret)}`
    headers.set("Authorization", `Basic ${btoa(credentials)}`)
  } else if (tokenEndpointAuthMethod === "client_secret_post") {
    if (!clientSecret) {
      throw new Error("Client secret is required for client_secret_post")
    }
    body.set("client_id", clientId)
    body.set("client_secret", clientSecret)
  } else {
    body.set("client_id", clientId)
  }

  const response = await fetch(metadata.introspection_endpoint, {
    method: "POST",
    headers,
    body,
  })

  if (!response.ok) {
    const errorBody = await response.text()
    throw new Error(
      `Token introspection failed: ${response.status} - ${errorBody}`
    )
  }

  const tokenInfo: unknown = await response.json()
  if (!isTokenIntrospectionResponse(tokenInfo)) {
    throw new Error("Invalid token introspection response")
  }

  return tokenInfo
}

function isTokenIntrospectionResponse(
  value: unknown
): value is TokenIntrospectionResponse {
  if (
    typeof value !== "object" ||
    value === null ||
    !("active" in value) ||
    typeof value.active !== "boolean"
  ) {
    return false
  }

  return (
    (!("client_id" in value) || typeof value.client_id === "string") &&
    (!("scope" in value) || typeof value.scope === "string") &&
    (!("token_type" in value) || value.token_type === "bearer") &&
    (!("exp" in value) || typeof value.exp === "number") &&
    (!("iat" in value) || typeof value.iat === "number") &&
    (!("sub" in value) || typeof value.sub === "string") &&
    (!("aud" in value) || isStringOrStringArray(value.aud)) &&
    (!("iss" in value) || typeof value.iss === "string") &&
    (!("user_id" in value) || typeof value.user_id === "string") &&
    (!("workspace_id" in value) || typeof value.workspace_id === "string")
  )
}

function isStringOrStringArray(value: unknown): value is string | string[] {
  return (
    typeof value === "string" ||
    (Array.isArray(value) && value.every(item => typeof item === "string"))
  )
}
```

An active token returns `active: true` with `client_id`, `scope`, `iat`, `sub`,
and `iss`, plus `user_id`, `exp`, and `aud` when Notion has them. Access tokens
also return `token_type: "bearer"` and, when Notion has it, `workspace_id`. An expired, revoked, or unknown
token, or a token issued to another client, returns only `{ "active": false }`.

### Check tool availability

You don't need to check tool access before you call tools. Each tool enforces
its own access limits when you call it. Use `notion-search` to search Notion,
and `notion-connector-search`, when the session lists it, to search connected
sources such as Slack and Google Drive. Workspace-owned connections keep the
earlier tool list: use the search tool the connection lists, which can be
`notion-ai-search`. See
[Supported tools](/guides/mcp/mcp-supported-tools) for that case.

If your client wants plan or parameter details up front, call
`notion-get-tool-access` with `{}` once and reuse the map for this connection.

```typescript TypeScript theme={null}
const result = await client.callTool({
  name: "notion-get-tool-access",
  arguments: {},
})

const [block] = result.content
if (result.isError || block?.type !== "text") {
  throw new Error("Could not read tool access from notion-get-tool-access")
}

const { current_tool_access } = JSON.parse(block.text)
console.log(current_tool_access)
// { [toolName]: { status, restricted_parameters?, upgrade_url?, ... } }
```

The map includes only tools the server exposes to this connection. It reports
AI search access under `connector_search`. In workspace-owned connections, it
reports that access under `ai_search` instead, and leaves out `search` when
`ai_search` is `available`, so request both keys there if you narrow it with
`tool_names`.

A user lookup (`query_type: "user"`) on the listed search tool has separate
requirements: it needs user information capabilities, and workspace-owned MCP
connections must also expose `notion-get-users`. AI search access doesn't grant
these permissions.

Read each `restricted_parameters` reason against your requested value. A listed
parameter isn't always forbidden: a restriction on multiple teamspaces still
allows a single teamspace. An `upgrade_required` status means full access needs
an upgrade; it doesn't rule out documented fallback results.
See [Supported tools](/guides/mcp/mcp-supported-tools) for all access statuses,
recovery links, and search behavior.

## Step 8: Handle token refresh

Access tokens expire. Implement automatic refresh with proper error handling:

```typescript TypeScript expandable theme={null}
async function refreshAccessToken(
  refreshToken: string,
  metadata: OAuthMetadata,
  clientId: string
): Promise<TokenResponse> {
  const params = new URLSearchParams({
    grant_type: "refresh_token",
    resource: mcpUrl.href,
    refresh_token: refreshToken,
    client_id: clientId,
  })

  const response = await fetch(metadata.token_endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      Accept: "application/json",
    },
    body: params.toString(),
  })

  if (!response.ok) {
    if (response.headers.get("content-type")?.includes("application/json")) {
      const error = await response.json()
      if (error.error === "invalid_grant") throw new Error("REAUTH_REQUIRED")
      if (error.error === "invalid_client") throw new Error("INVALID_CLIENT")
    }
    throw new Error(`Token refresh failed: HTTP ${response.status}`)
  }

  const tokens = await response.json()

  return tokens
}
```

> [!NOTE]
>
> Many servers rotate refresh tokens for security (RFC 6749 Section 10.4).
> Always store the new `refresh_token` if provided in the response.

## Complete example

With the access token from step 6 and the client from step 7, list the tools available to the user. Follow each page's cursor until the server omits it.

```typescript theme={null}
const accessToken = process.env.NOTION_MCP_ACCESS_TOKEN
if (!accessToken) throw new Error("Set NOTION_MCP_ACCESS_TOKEN first")
const client = await createMcpClient(accessToken)
try {
  let cursor: string | undefined
  do {
    const page = await client.listTools({ cursor })
    for (const tool of page.tools) console.log(tool.name)
    cursor = page.nextCursor
  } while (cursor)
} finally {
  await client.close()
}
```

## Security best practices

1. **Always use HTTPS** — Never use HTTP except for localhost development
2. **Validate state parameter** — Always verify state matches stored value on
   callback
3. **Secure token storage** — Encrypt tokens at rest, never expose to
   client-side code
4. **PKCE is mandatory** — Require advertised S256 support before starting authorization
5. **Token expiry handling** — Check token expiry before each request, refresh
   proactively
6. **Error handling** — Handle `invalid_grant` errors gracefully
   (re-authentication required)
7. **HTTPS verification** — Validate SSL certificates in production
8. **Rate limiting** — Implement rate limiting for token refresh to prevent
   abuse
9. **Scope minimization** — Only request the scopes you actually need
10. **Audit logging** — Log all OAuth operations for security auditing

## Troubleshooting

> [accordion] Invalid state parameter
>
> * Store the state securely and validate on callback
> * Expire after \~10 minutes

> [accordion] Invalid code_verifier
>
> * Use the exact verifier that produced the code_challenge
> * Ensure base64url encoding (no +, /, =)

> [accordion] Discovery fails
>
> * Use RFC 9728 (protected resource) then RFC 8414 (authorization server)
> * Confirm server supports OAuth and your URL is correct

> [accordion] Connection timeout
>
> * Check that the client uses Streamable HTTP and the URL `https://mcp.notion.com/mcp`
> * Check proxy or firewall rules

> [accordion] CORS errors in browser
>
> * Do token exchange server-side; browser should only handle redirects

> [accordion] Token refresh fails with invalid_grant
>
> When refresh returns `{ "error": "invalid_grant" }`, the refresh token is
> invalid, expired, revoked, or superseded by rotation. Do not retry refresh;
> prompt re-authentication.
>
> **Common causes:**
>
> 1. **Rotation on use** — Providers rotate refresh tokens and revoke the old
>    one. **Fix:** Persist the new `refresh_token` atomically with the access
>    token.
> 2. **Expired refresh token** — The grant reached its lifetime. **Fix:** Re-authenticate;
>    monitor early expirations.
> 3. **Client credential mismatch** — `client_id` or `client_secret` differs
>    from initial auth. **Fix:** Keep credentials consistent for the token's
>    lifetime.
> 4. **Explicit revocation or policy event** — User revoked access, password
>    change, or security policy. **Fix:** Show clear reconnect UI.
> 5. **Concurrent refreshes** — Parallel refreshes cause losers to see
>    `invalid_grant`. **Fix:** Use a mutex or distributed lock around refresh.
>
> **Operational guidance:**
>
> * `invalid_grant` → re-authenticate
> * `temporarily_unavailable` or network errors → retry with backoff
> * Refresh 5–10 minutes before expiry to avoid races
> * Cache access tokens with accurate expiry
>
> If your client exchanges an ID-JAG from an identity provider instead of a
> refresh token, `invalid_grant` means Notion rejected the assertion. See
> [Enterprise-managed authorization](/guides/mcp/enterprise-managed-authorization)
> for the claims Notion checks and the common causes.

### Notion MCP OAuth specifics

Notion's remote MCP server is built on
[Cloudflare's `workers-oauth-provider` package](https://github.com/cloudflare/workers-oauth-provider).
Its token lifecycle has a few behaviors worth designing your client around. The
guarantees below are the ones you can rely on; build for them as the strictest
case.

#### Token lifecycle

* **Access tokens** currently last about **eight hours**, but this duration is
  subject to change. Always use the token response's `expires_in` value and
  refresh proactively rather than hard-coding a lifetime.
* Refresh tokens have a maximum lifetime of 180 days from authorization. A grant can end sooner. If a refresh returns `invalid_grant`, prompt the user to authorize again.

For reliable long-lived connections:

* Persist dynamic client registration credentials (`client_id` and
  `client_secret`) durably and reuse them, because re-registering orphans prior
  grants. Alternatively, use a Client ID Metadata Document (CIMD), which Notion
  MCP supports.
* Persist each rotated `refresh_token` atomically and serialize refreshes per
  grant. Never refresh the same grant concurrently from multiple processes.
* Treat `invalid_grant` as terminal: clear the stored tokens and reauthorize
  once. Do not retry-loop.

#### Refresh token rotation

Every refresh rotates the refresh token: the token response returns a new
`refresh_token`, and the one you sent is retired. To keep a connection healthy:

* Persist the new `refresh_token` from each refresh response atomically with the
  new access token, before you issue the next request.
* A grant keeps at most two refresh tokens valid at once — the current one and
  the immediately previous one (a one-step window). If a transient failure
  prevents you from storing a rotated token, you may retry once with the
  previously stored token.

> [!WARNING]
>
> **Reusing a refresh token that has already been rotated away can revoke the
> entire connection.** As a theft-containment measure, replaying a refresh token
> that was rotated out more than a brief grace period earlier is treated as a
> stolen-token signal: the server revokes the whole grant. Every access and
> refresh token for that connection stops working, and the user must
> re-authorize from scratch. To stay clear of it:
>
> * Serialize refreshes per connection with a mutex or distributed lock. Never
>   refresh the same connection from two workers or replicas concurrently —
>   distributed setups that share a connection without a consistent, atomic
>   token store are the most common cause of accidental reuse.
> * Treat `invalid_grant` as terminal for the connection: drop the stored tokens
>   and surface re-authentication. Do **not** retry a refresh that returned
>   `invalid_grant`. A revoked or expired grant cannot recover, and retry loops
>   against it only generate load and never succeed.

#### Handling `invalid_grant`

`invalid_grant` from the token endpoint always means the connection is dead and
the user must reconnect, whether the cause is refresh-token reuse, the grant
lifetime, an explicit revocation, or a credential mismatch. Stop refreshing that
connection, clear its tokens, and prompt re-authorization. See
[Troubleshooting](#troubleshooting) above for the full list of causes and fixes.

## Optional: MCP server discovery via `mcp.json`

> [!NOTE]
>
> The `mcp.json` convention described here is not part of the MCP specification.
> It is an unofficial convention, championed by Notion and Cursor, that MCP
> clients can optionally support to improve the user experience.

MCP clients can discover available MCP servers by checking for a
`/.well-known/mcp.json` file on a website's domain. When a user pastes a link,
the client can detect the MCP server and offer to connect to it.

For example, Notion hosts its discovery file at:

```
https://www.notion.com/.well-known/mcp.json
```

The file contains:

```json theme={null}
{
  "name": "Notion",
  "description": "Connect your Notion workspace to search, update, and trigger workflows across tools.",
  "icon": "https://www.notion.com/images/notion-logo-block-main.svg",
  "endpoint": "https://mcp.notion.com/mcp"
}
```

### Schema

| Field | Type | Description |
| :- | :- | :- |
| `name` | `string` | Human-readable name of the MCP server |
| `description` | `string` | Brief description of what the server provides |
| `icon` | `string` (URL) | URL to the server's icon |
| `endpoint` | `string` (URL) | The MCP server endpoint URL |

### How to use this in your client

For a Notion link, you can offer the user a connection to the endpoint in [Notion's discovery file](https://www.notion.com/.well-known/mcp.json). Verify the endpoint against the Notion server you trust before sending a token. After the user connects, use `server/discover` to read its protocol capabilities.

### Publishing your own `mcp.json`

If you operate an MCP server, you can publish a `mcp.json` file at
`/.well-known/mcp.json` on your domain so that MCP clients can discover your
server automatically.

## Additional resources

* [Notion MCP Server GitHub](https://github.com/makenotion/notion-mcp-server)
* [MCP SDK Documentation](https://ts.sdk.modelcontextprotocol.io/v2/clients/connect)
* [MCP Registry](https://github.com/modelcontextprotocol/registry/tree/main/docs) — the official MCP server registry
