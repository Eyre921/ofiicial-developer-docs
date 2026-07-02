---
title: "Get secret"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get.md
path: docs/api-reference/workspace/secrets/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secret

GET https://api.elevenlabs.io/v1/convai/secrets/{secret_id}

Get a workspace secret by ID

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/secrets/{secret_id}:
    get:
      operationId: get
      summary: Get Convai Workspace Secret
      description: Get a workspace secret by ID
      tags:
        - subpackage_conversationalAi/secrets
      parameters:
        - name: secret_id
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
                $ref: '#/components/schemas/ConvAIWorkspaceStoredSecretConfig'
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
  "type": "stored",
  "secret_id": "sec_9f8b7c6d5e4a3b2c1d0e",
  "name": "DatabaseCredentials",
  "used_by": {
    "tools": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1685000000,
        "id": "tool_123abc456def",
        "name": "DataSyncTool"
      }
    ],
    "agents": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1685100000,
        "id": "agent_987zyx654wvu",
        "name": "CustomerSupportAgent",
        "referenced_resource_ids": [
          "res_789xyz123uvw"
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
        "phone_number_id": "pn_5551234567",
        "phone_number": "+15551234567",
        "label": "Support Line",
        "provider": "twilio"
      }
    ],
    "phone_numbers_has_more": false,
    "mcp_servers": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1685200000,
        "id": "mcp_321fed654cba",
        "name": "PrimaryMCPServer"
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
    await client.conversationalAi.secrets.get("secret_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.get(
    secret_id="secret_id",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
