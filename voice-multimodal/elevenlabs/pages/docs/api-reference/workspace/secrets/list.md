---
title: "Get secrets"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/list.md
path: docs/api-reference/workspace/secrets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secrets

GET https://api.elevenlabs.io/v1/convai/secrets

Get all workspace secrets for the user

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/secrets:
    get:
      operationId: list
      summary: Get Convai Workspace Secrets
      description: Get all workspace secrets for the user
      tags:
        - subpackage_conversationalAi/secrets
      parameters:
        - name: page_size
          in: query
          description: >-
            How many documents to return at maximum. Can not exceed 100. If not
            provided, returns all secrets.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: dependency_limit
          in: query
          description: >-
            Maximum number of dependent resources (tools, agents, phone numbers)
            to return per secret. Can not exceed 100.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: search
          in: query
          description: >-
            If specified, returns only secrets whose names start with this
            string.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/GetWorkspaceSecretsResponseModel'
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
    GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel
    ConvAiStoredSecretDependenciesToolsItems:
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
      title: ConvAiStoredSecretDependenciesToolsItems
    V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
    ConvAiStoredSecretDependenciesAgentsItems:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
          description: DependentAvailableAgentIdentifier variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
          description: |-
            A model that represents an agent dependent on a knowledge base/tools
            to which the user has no direct access.
      discriminator:
        propertyName: type
      title: ConvAiStoredSecretDependenciesAgentsItems
    TelephonyProvider:
      type: string
      enum:
        - twilio
        - sip_trunk
        - exotel
      title: TelephonyProvider
    DependentPhoneNumberIdentifier:
      type: object
      properties:
        phone_number_id:
          type: string
        phone_number:
          type: string
        label:
          type: string
        provider:
          $ref: '#/components/schemas/TelephonyProvider'
      required:
        - phone_number_id
        - phone_number
        - label
        - provider
      title: DependentPhoneNumberIdentifier
    DependentAvailableMcpServerIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableMcpServerIdentifierAccessLevel
    ConvAiStoredSecretDependenciesMcpServersItems:
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
      title: ConvAiStoredSecretDependenciesMcpServersItems
    SecretDependencyType:
      type: string
      enum:
        - conversation_initiation_webhook
      title: SecretDependencyType
    ConvAIStoredSecretDependencies:
      type: object
      properties:
        tools:
          type: array
          items:
            $ref: '#/components/schemas/ConvAiStoredSecretDependenciesToolsItems'
        tools_has_more:
          type: boolean
          default: false
          description: Whether there are more tool dependents beyond the returned preview
        agents:
          type: array
          items:
            $ref: '#/components/schemas/ConvAiStoredSecretDependenciesAgentsItems'
        agents_has_more:
          type: boolean
          default: false
          description: Whether there are more agent dependents beyond the returned preview
        phone_numbers:
          type: array
          items:
            $ref: '#/components/schemas/DependentPhoneNumberIdentifier'
        phone_numbers_has_more:
          type: boolean
          default: false
          description: >-
            Whether there are more phone number dependents beyond the returned
            preview
        mcp_servers:
          type: array
          items:
            $ref: '#/components/schemas/ConvAiStoredSecretDependenciesMcpServersItems'
        others:
          type: array
          items:
            $ref: '#/components/schemas/SecretDependencyType'
      required:
        - tools
        - agents
        - others
      title: ConvAIStoredSecretDependencies
    ConvAIWorkspaceStoredSecretConfig:
      type: object
      properties:
        type:
          type: string
          enum:
            - stored
        secret_id:
          type: string
        name:
          type: string
        used_by:
          $ref: '#/components/schemas/ConvAIStoredSecretDependencies'
      required:
        - type
        - secret_id
        - name
        - used_by
      title: ConvAIWorkspaceStoredSecretConfig
    GetWorkspaceSecretsResponseModel:
      type: object
      properties:
        secrets:
          type: array
          items:
            $ref: '#/components/schemas/ConvAIWorkspaceStoredSecretConfig'
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for fetching the next page of secrets
      required:
        - secrets
      title: GetWorkspaceSecretsResponseModel
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
  "secrets": [
    {
      "type": "string",
      "secret_id": "string",
      "name": "string",
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
        "agents": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "string",
            "name": "string",
            "referenced_resource_ids": [
              "string"
            ]
          }
        ],
        "others": [
          "conversation_initiation_webhook"
        ],
        "tools_has_more": false,
        "agents_has_more": false,
        "phone_numbers": [
          {
            "phone_number_id": "string",
            "phone_number": "string",
            "label": "string",
            "provider": "twilio"
          }
        ],
        "phone_numbers_has_more": false,
        "mcp_servers": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "string",
            "name": "string"
          }
        ]
      }
    }
  ],
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets")! as URL,
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
