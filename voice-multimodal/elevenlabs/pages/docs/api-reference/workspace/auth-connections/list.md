---
title: "Get Workspace Auth Connections"
source: https://elevenlabs.io/docs/api-reference/workspace/auth-connections/list.md
path: docs/api-reference/workspace/auth-connections/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Workspace Auth Connections

GET https://api.elevenlabs.io/v1/workspace/auth-connections

Get all auth connections for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/auth-connections/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `auth_connections` (list of object, required)
  - `auth_type`: `api_integration_oauth2_auth_code` (ApiIntegrationOAuth2AuthCodeResponse)
    - `credential_id` (string, required)
    - `expires_at` (string, required) — ISO 8601 timestamp of when the access token expires
    - `id` (string, required)
    - `integration_id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `token_url` (string, required)
    - `scope_separator` (enum, optional, default:  ) — Separator for scopes
      - Allowed values: ` `, `,`
    - `scopes` (list of string, optional)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `api_integration_oauth2_custom_app` (ApiIntegrationOAuth2CustomAppResponse)
    - `client_id` (string, required) — OAuth client ID (rendered from template if credential uses templated credentials, None for legacy connections)
    - `credential_id` (string, required)
    - `expires_at` (string, required) — ISO 8601 timestamp of when the access token expires
    - `id` (string, required)
    - `integration_id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `token_url` (string, required)
    - `scope_separator` (enum, optional, default:  ) — Separator for scopes
      - Allowed values: ` `, `,`
    - `scopes` (list of string, optional)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `basic_auth` (BasicAuthResponse)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `username` (string, required)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `bearer_auth` (BearerAuthResponse)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `custom_header_auth` (CustomHeaderAuthResponse)
    - `header_name` (string, required) — The name of the header to use for authentication (e.g., 'x-api-key')
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `mtls` (MTLSAuthResponse)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `oauth2_client_credentials` (OAuth2ClientCredsResponse)
    - `client_id` (string, required)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `token_url` (string, required)
    - `basic_auth_in_header` (boolean, optional, default: false) — If True, send client credentials in Authorization header as Basic Auth instead of request body
    - `custom_headers` (map from string to string, optional) — Custom headers configured for OAuth2 token requests
    - `extra_params` (map from string to string, optional, default: {})
    - `scopes` (list of string, optional, default: [])
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `oauth2_jwt` (OAuth2JWTResponse)
    - `audience` (string, required) — JWT audience (aud claim)
    - `id` (string, required)
    - `issuer` (string, required) — JWT issuer (iss claim)
    - `name` (string, required)
    - `provider` (string, required)
    - `subject` (string, required) — JWT subject (sub claim)
    - `token_url` (string, required) — Token endpoint URL for exchanging JWT for access token
    - `algorithm` (enum, optional, default: HS256) — JWT signing algorithm
      - Allowed values: `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`
    - `expiration_seconds` (integer, optional, default: 3600) — Token expiration time in seconds
    - `extra_params` (map from string to string, optional) — Additional custom claims to include in the JWT
    - `key_id` (string, optional, nullable) — Key ID (kid) for JWT header - useful for key rotation
    - `scopes` (list of string, optional) — OAuth2 scopes to request when exchanging JWT for access token
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `token_response_field` (enum, optional, default: access_token) — Token field to extract from the token endpoint response.
      - Allowed values: `access_token`, `id_token`
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `private_key_jwt` (PrivateKeyJWTResponse)
    - `audience` (string, required) — JWT audience (aud claim)
    - `id` (string, required)
    - `issuer` (string, required) — JWT issuer (iss claim)
    - `name` (string, required)
    - `provider` (string, required)
    - `subject` (string, required) — JWT subject (sub claim)
    - `algorithm` (enum, optional, default: HS256) — JWT signing algorithm
      - Allowed values: `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`
    - `expiration_seconds` (integer, optional, default: 3600) — Token expiration time in seconds
    - `extra_params` (map from string to string, optional) — Additional custom claims to include in the JWT
    - `key_id` (string, optional, nullable) — Key ID (kid) for JWT header - useful for key rotation
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `refresh_token_auth` (RefreshTokenAuthResponse)
    - `client_id` (string, required)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `token_url` (string, required)
    - `extra_params` (map from string to string, optional, default: {})
    - `scopes` (list of string, optional, default: [])
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `slack_bot_auth` (SlackBotAuthResponse)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` ("Slack", optional, default: Slack)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `url_secret` (UrlSecretAuthResponse)
    - `id` (string, required)
    - `name` (string, required)
    - `provider` (string, required)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)
  - `auth_type`: `whatsapp_auth` (WhatsAppAuthResponse)
    - `id` (string, required)
    - `name` (string, required)
    - `phone_number_id` (string, required)
    - `provider` ("whatsapp", optional, default: whatsapp)
    - `status` (enum, optional, default: active) — Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      - Allowed values: `active`, `refresh_failed`, `revoked`, `credential_invalid`
    - `status_detail` (string, optional, nullable)
    - `status_updated_at` (string, optional, nullable)
    - `used_by` (object, optional, nullable) — Dependencies that use an auth connection
      - `tools` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableToolIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownToolIdentifier)
          - `id` (string, required)
      - `mcp_servers` (list of object, optional, default: [])
        - `type`: `available` (DependentAvailableMCPServerIdentifier)
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
        - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
          - `id` (string, required)
      - `integration_connections` (list of object, optional, default: [])
        - `id` (string, required)
        - `name` (string, required)

## Examples

**Response**

```json
{
  "auth_connections": [
    {
      "auth_type": "oauth2_client_credentials",
      "client_id": "string",
      "id": "string",
      "name": "string",
      "provider": "string",
      "token_url": "string",
      "basic_auth_in_header": false,
      "custom_headers": {},
      "extra_params": {},
      "scopes": [
        "string"
      ],
      "status": "active",
      "status_detail": "string",
      "status_updated_at": "string",
      "used_by": {
        "tools": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "string",
            "name": "string"
          }
        ],
        "mcp_servers": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "string",
            "name": "string"
          }
        ],
        "integration_connections": [
          {
            "id": "string",
            "name": "string"
          }
        ]
      }
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.authConnections.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.auth_connections.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/auth-connections"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/workspace/auth-connections")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/auth-connections")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/auth-connections');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/auth-connections");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/auth-connections")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
