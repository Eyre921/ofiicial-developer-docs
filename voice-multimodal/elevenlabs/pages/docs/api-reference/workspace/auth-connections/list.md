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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/auth-connections:
    get:
      operationId: list
      summary: Get Workspace Auth Connections
      description: Get all auth connections for the workspace
      tags:
        - authConnections
      parameters:
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
                $ref: '#/components/schemas/ListAuthConnectionsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2AuthCodeScopeSeparator:
      type: string
      enum:
        - ' '
        - ','
      default: ' '
      description: Separator for scopes
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2AuthCodeScopeSeparator
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
    V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2CustomAppScopeSeparator:
      type: string
      enum:
        - ' '
        - ','
      default: ' '
      description: Separator for scopes
      title: >-
        V1WorkspaceAuthConnectionsAuthConnectionIdPatchResponsesContentApplicationJsonSchemaDiscriminatorMappingApiIntegrationOauth2CustomAppScopeSeparator
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
    ListAuthConnectionsResponseAuthConnectionsItems:
      oneOf:
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
      discriminator:
        propertyName: auth_type
      description: The type of auth connection config
      title: ListAuthConnectionsResponseAuthConnectionsItems
    ListAuthConnectionsResponse:
      type: object
      properties:
        auth_connections:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListAuthConnectionsResponseAuthConnectionsItems
      required:
        - auth_connections
      title: ListAuthConnectionsResponse
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
