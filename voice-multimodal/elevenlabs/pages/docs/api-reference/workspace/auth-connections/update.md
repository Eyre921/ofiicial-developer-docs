---
title: "Update Workspace Auth Connection"
source: https://elevenlabs.io/docs/api-reference/workspace/auth-connections/update.md
path: docs/api-reference/workspace/auth-connections/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Workspace Auth Connection

PATCH https://api.elevenlabs.io/v1/workspace/auth-connections/{auth_connection_id}
Content-Type: application/json

Update an auth connection

Reference: https://elevenlabs.io/docs/api-reference/workspace/auth-connections/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/auth-connections/{auth_connection_id}:
    patch:
      operationId: update
      summary: Update Workspace Auth Connection
      description: Update an auth connection
      tags:
        - authConnections
      parameters:
        - name: auth_connection_id
          in: path
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/workspace_auth_connections_update_Response_200
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/workspace_auth_connections_update_Request'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    UpdateOAuth2ClientCredsRequest:
      type: object
      properties:
        auth_type:
          type: string
          enum:
            - oauth2_client_credentials
          default: oauth2_client_credentials
        provider:
          type:
            - string
            - 'null'
        client_id:
          type:
            - string
            - 'null'
        scopes:
          type:
            - array
            - 'null'
          items:
            type: string
        extra_params:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        basic_auth_in_header:
          type:
            - boolean
            - 'null'
        client_secret:
          type:
            - string
            - 'null'
        custom_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
      title: UpdateOAuth2ClientCredsRequest
    UpdateBasicAuthRequest:
      type: object
      properties:
        auth_type:
          type: string
          enum:
            - basic_auth
          default: basic_auth
        provider:
          type:
            - string
            - 'null'
        username:
          type:
            - string
            - 'null'
        password:
          type:
            - string
            - 'null'
      title: UpdateBasicAuthRequest
    UpdateBearerAuthRequest:
      type: object
      properties:
        auth_type:
          type: string
          enum:
            - bearer_auth
          default: bearer_auth
        provider:
          type:
            - string
            - 'null'
        token:
          type:
            - string
            - 'null'
      title: UpdateBearerAuthRequest
    UpdateOAuth2JwtRequestAlgorithm:
      type: string
      enum:
        - HS256
        - HS384
        - HS512
        - RS256
        - RS384
        - RS512
      title: UpdateOAuth2JwtRequestAlgorithm
    UpdateOAuth2JwtRequestTokenResponseField:
      type: string
      enum:
        - access_token
        - id_token
      title: UpdateOAuth2JwtRequestTokenResponseField
    UpdateOAuth2JWTRequest:
      type: object
      properties:
        auth_type:
          type: string
          enum:
            - oauth2_jwt
          default: oauth2_jwt
        provider:
          type:
            - string
            - 'null'
        algorithm:
          oneOf:
            - $ref: '#/components/schemas/UpdateOAuth2JwtRequestAlgorithm'
            - type: 'null'
        key_id:
          type:
            - string
            - 'null'
        issuer:
          type:
            - string
            - 'null'
        audience:
          type:
            - string
            - 'null'
        subject:
          type:
            - string
            - 'null'
        expiration_seconds:
          type:
            - integer
            - 'null'
        extra_params:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
        scopes:
          type:
            - array
            - 'null'
          items:
            type: string
        token_response_field:
          oneOf:
            - $ref: '#/components/schemas/UpdateOAuth2JwtRequestTokenResponseField'
            - type: 'null'
        secret_key:
          type:
            - string
            - 'null'
      title: UpdateOAuth2JWTRequest
    workspace_auth_connections_update_Request:
      oneOf:
        - $ref: '#/components/schemas/UpdateOAuth2ClientCredsRequest'
        - $ref: '#/components/schemas/UpdateBasicAuthRequest'
        - $ref: '#/components/schemas/UpdateBearerAuthRequest'
        - $ref: '#/components/schemas/UpdateOAuth2JWTRequest'
      description: Updated auth connection fields
      title: workspace_auth_connections_update_Request
    GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel
    AuthConnectionDependenciesToolsItems:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
          description: DependentAvailableToolIdentifier variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            id:
              type: string
          required:
            - type
            - id
          description: |-
            A model that represents an tool dependent on a knowledge base/tools
            to which the user has no direct access.
      discriminator:
        propertyName: type
      title: AuthConnectionDependenciesToolsItems
    DependentAvailableMcpServerIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableMcpServerIdentifierAccessLevel
    AuthConnectionDependenciesMcpServersItems:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              default: available
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/DependentAvailableMcpServerIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
          description: DependentAvailableMCPServerIdentifier variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              default: unknown
            id:
              type: string
          required:
            - type
            - id
          description: DependentUnknownMCPServerIdentifier variant
      discriminator:
        propertyName: type
      title: AuthConnectionDependenciesMcpServersItems
    DependentIntegrationConnectionIdentifier:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
      required:
        - id
        - name
      description: >-
        Identifier for an integration connection that depends on an auth
        connection
      title: DependentIntegrationConnectionIdentifier
    AuthConnectionDependencies:
      type: object
      properties:
        tools:
          type: array
          items:
            $ref: '#/components/schemas/AuthConnectionDependenciesToolsItems'
          default: []
        mcp_servers:
          type: array
          items:
            $ref: '#/components/schemas/AuthConnectionDependenciesMcpServersItems'
          default: []
        integration_connections:
          type: array
          items:
            $ref: '#/components/schemas/DependentIntegrationConnectionIdentifier'
          default: []
      description: Dependencies that use an auth connection
      title: AuthConnectionDependencies
    AuthConnectionStatus:
      type: string
      enum:
        - active
        - refresh_failed
        - revoked
        - credential_invalid
      default: active
      description: |-
        Single status field shared by every auth type's stored credential.

        OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth
        token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the
        tool execution path when an upstream response matches a credential's
        ``failure_signatures`` entry (Bearer, Basic auth, etc.).
      title: AuthConnectionStatus
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingOauth2JwtAlgorithm:
      type: string
      enum:
        - HS256
        - HS384
        - HS512
        - RS256
        - RS384
        - RS512
      default: HS256
      description: JWT signing algorithm
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingOauth2JwtAlgorithm
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingOauth2JwtTokenResponseField:
      type: string
      enum:
        - access_token
        - id_token
      default: access_token
      description: Token field to extract from the token endpoint response.
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingOauth2JwtTokenResponseField
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingPrivateKeyJwtAlgorithm:
      type: string
      enum:
        - HS256
        - HS384
        - HS512
        - RS256
        - RS384
        - RS512
      default: HS256
      description: JWT signing algorithm
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingPrivateKeyJwtAlgorithm
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2AuthCodeScopeSeparator:
      type: string
      enum:
        - ' '
        - ','
      default: ' '
      description: Separator for scopes
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2AuthCodeScopeSeparator
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2CustomAppScopeSeparator:
      type: string
      enum:
        - ' '
        - ','
      default: ' '
      description: Separator for scopes
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2CustomAppScopeSeparator
    workspace_auth_connections_update_Response_200:
      oneOf:
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - oauth2_client_credentials
              description: 'Discriminator value: oauth2_client_credentials'
            name:
              type: string
            provider:
              type: string
            client_id:
              type: string
            token_url:
              type: string
            scopes:
              type: array
              items:
                type: string
              default: []
            extra_params:
              type: object
              additionalProperties:
                type: string
              default: {}
            basic_auth_in_header:
              type: boolean
              default: false
              description: >-
                If True, send client credentials in Authorization header as
                Basic Auth instead of request body
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
            custom_headers:
              type: object
              additionalProperties:
                type: string
              description: Custom headers configured for OAuth2 token requests
          required:
            - auth_type
            - name
            - provider
            - client_id
            - token_url
            - id
          description: Response model for oauth2 client creds
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - basic_auth
              description: 'Discriminator value: basic_auth'
            name:
              type: string
            provider:
              type: string
            username:
              type: string
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - username
            - id
          description: Response model for basic auth
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - bearer_auth
              description: 'Discriminator value: bearer_auth'
            name:
              type: string
            provider:
              type: string
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - id
          description: Response model for bearer auth
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - oauth2_jwt
              description: 'Discriminator value: oauth2_jwt'
            name:
              type: string
            provider:
              type: string
            algorithm:
              $ref: >-
                #/components/schemas/V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingOauth2JwtAlgorithm
              default: HS256
              description: JWT signing algorithm
            key_id:
              type:
                - string
                - 'null'
              description: Key ID (kid) for JWT header - useful for key rotation
            issuer:
              type: string
              description: JWT issuer (iss claim)
            audience:
              type: string
              description: JWT audience (aud claim)
            subject:
              type: string
              description: JWT subject (sub claim)
            expiration_seconds:
              type: integer
              default: 3600
              description: Token expiration time in seconds
            extra_params:
              type: object
              additionalProperties:
                type: string
              description: Additional custom claims to include in the JWT
            token_url:
              type: string
              description: Token endpoint URL for exchanging JWT for access token
            scopes:
              type: array
              items:
                type: string
              description: OAuth2 scopes to request when exchanging JWT for access token
            token_response_field:
              $ref: >-
                #/components/schemas/V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingOauth2JwtTokenResponseField
              default: access_token
              description: Token field to extract from the token endpoint response.
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - issuer
            - audience
            - subject
            - token_url
            - id
          description: Response model for OAuth2 JWT auth connections
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - private_key_jwt
              description: 'Discriminator value: private_key_jwt'
            name:
              type: string
            provider:
              type: string
            algorithm:
              $ref: >-
                #/components/schemas/V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingPrivateKeyJwtAlgorithm
              default: HS256
              description: JWT signing algorithm
            key_id:
              type:
                - string
                - 'null'
              description: Key ID (kid) for JWT header - useful for key rotation
            issuer:
              type: string
              description: JWT issuer (iss claim)
            audience:
              type: string
              description: JWT audience (aud claim)
            subject:
              type: string
              description: JWT subject (sub claim)
            expiration_seconds:
              type: integer
              default: 3600
              description: Token expiration time in seconds
            extra_params:
              type: object
              additionalProperties:
                type: string
              description: Additional custom claims to include in the JWT
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - issuer
            - audience
            - subject
            - id
          description: Response model for Private Key JWT auth connections
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - mtls
              description: 'Discriminator value: mtls'
            name:
              type: string
            provider:
              type: string
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - id
          description: Response model for mTLS auth connections.
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - custom_header_auth
              description: 'Discriminator value: custom_header_auth'
            name:
              type: string
            provider:
              type: string
            header_name:
              type: string
              description: >-
                The name of the header to use for authentication (e.g.,
                'x-api-key')
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - header_name
            - id
          description: Response model for Custom Header Auth auth connections
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - api_integration_oauth2_auth_code
              description: 'Discriminator value: api_integration_oauth2_auth_code'
            name:
              type: string
            provider:
              type: string
            token_url:
              type: string
            scopes:
              type: array
              items:
                type: string
            scope_separator:
              $ref: >-
                #/components/schemas/V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2AuthCodeScopeSeparator
              default: ' '
              description: Separator for scopes
            expires_at:
              type: string
              description: ISO 8601 timestamp of when the access token expires
            integration_id:
              type: string
            credential_id:
              type: string
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - token_url
            - expires_at
            - integration_id
            - credential_id
            - id
          description: >-
            Response model for integration-managed OAuth2 Auth Code auth
            connections
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - api_integration_oauth2_custom_app
              description: 'Discriminator value: api_integration_oauth2_custom_app'
            name:
              type: string
            provider:
              type: string
            token_url:
              type: string
            scopes:
              type: array
              items:
                type: string
            scope_separator:
              $ref: >-
                #/components/schemas/V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2CustomAppScopeSeparator
              default: ' '
              description: Separator for scopes
            expires_at:
              type: string
              description: ISO 8601 timestamp of when the access token expires
            integration_id:
              type: string
            credential_id:
              type: string
            client_id:
              type: string
              description: >-
                OAuth client ID (rendered from template if credential uses
                templated credentials, None for legacy connections)
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - token_url
            - expires_at
            - integration_id
            - credential_id
            - client_id
            - id
          description: Response model for user-owned OAuth2 Custom App auth connections
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - whatsapp_auth
              description: 'Discriminator value: whatsapp_auth'
            name:
              type: string
            provider:
              type: string
              enum:
                - whatsapp
              default: whatsapp
            phone_number_id:
              type: string
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - phone_number_id
            - id
          description: WhatsAppAuthResponse variant
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - slack_bot_auth
              description: 'Discriminator value: slack_bot_auth'
            name:
              type: string
            provider:
              type: string
              enum:
                - Slack
              default: Slack
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - id
          description: Response model for the internal Slack BYO bot auth connection.
        - type: object
          properties:
            auth_type:
              type: string
              enum:
                - url_secret
              description: 'Discriminator value: url_secret'
            name:
              type: string
            provider:
              type: string
            id:
              type: string
            used_by:
              oneOf:
                - $ref: '#/components/schemas/AuthConnectionDependencies'
                - type: 'null'
            status:
              $ref: '#/components/schemas/AuthConnectionStatus'
              default: active
            status_detail:
              type:
                - string
                - 'null'
            status_updated_at:
              type:
                - string
                - 'null'
          required:
            - auth_type
            - name
            - provider
            - id
          description: UrlSecretAuthResponse variant
      discriminator:
        propertyName: auth_type
      description: The type of auth connection config
      title: workspace_auth_connections_update_Response_200
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



**Request**

```json
{}
```

**Response**

```json
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
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.authConnections.update("auth_connection_id", );
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.auth_connections.update(
    auth_connection_id="auth_connection_id",
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/auth-connections/auth_connection_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Content-Type", "application/json")

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

url = URI("https://api.elevenlabs.io/v1/workspace/auth-connections/auth_connection_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/workspace/auth-connections/auth_connection_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/workspace/auth-connections/auth_connection_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/auth-connections/auth_connection_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/auth-connections/auth_connection_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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
