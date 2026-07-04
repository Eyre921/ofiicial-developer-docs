---
title: "Get secret"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get.md
path: docs/eleven-agents/api-reference/workspace/secrets/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secret

GET https://api.elevenlabs.io/v1/convai/secrets/{secret_id}

Get a workspace secret by ID

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get

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
        - secrets
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
                $ref: '#/components/schemas/type_:ConvAiWorkspaceStoredSecretConfig'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:DependentAvailableToolIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableToolIdentifierAccessLevel
    type_:ConvAiStoredSecretDependenciesToolsItem:
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
                #/components/schemas/type_:DependentAvailableToolIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
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
      discriminator:
        propertyName: type
      title: ConvAiStoredSecretDependenciesToolsItem
    type_:DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableAgentIdentifierAccessLevel
    type_:ConvAiStoredSecretDependenciesAgentsItem:
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
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
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
      discriminator:
        propertyName: type
      title: ConvAiStoredSecretDependenciesAgentsItem
    type_:TelephonyProvider:
      type: string
      enum:
        - twilio
        - sip_trunk
        - exotel
      title: TelephonyProvider
    type_:DependentPhoneNumberIdentifier:
      type: object
      properties:
        phone_number_id:
          type: string
        phone_number:
          type: string
        label:
          type: string
        provider:
          $ref: '#/components/schemas/type_:TelephonyProvider'
      required:
        - phone_number_id
        - phone_number
        - label
        - provider
      title: DependentPhoneNumberIdentifier
    type_:DependentAvailableMcpServerIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableMcpServerIdentifierAccessLevel
    type_:ConvAiStoredSecretDependenciesMcpServersItem:
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
                #/components/schemas/type_:DependentAvailableMcpServerIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
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
      discriminator:
        propertyName: type
      title: ConvAiStoredSecretDependenciesMcpServersItem
    type_:SecretDependencyType:
      type: string
      enum:
        - conversation_initiation_webhook
      title: SecretDependencyType
    type_:ConvAiStoredSecretDependencies:
      type: object
      properties:
        tools:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConvAiStoredSecretDependenciesToolsItem'
        tools_has_more:
          type: boolean
          default: false
          description: Whether there are more tool dependents beyond the returned preview
        agents:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConvAiStoredSecretDependenciesAgentsItem
        agents_has_more:
          type: boolean
          default: false
          description: Whether there are more agent dependents beyond the returned preview
        phone_numbers:
          type: array
          items:
            $ref: '#/components/schemas/type_:DependentPhoneNumberIdentifier'
        phone_numbers_has_more:
          type: boolean
          default: false
          description: >-
            Whether there are more phone number dependents beyond the returned
            preview
        mcp_servers:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConvAiStoredSecretDependenciesMcpServersItem
        others:
          type: array
          items:
            $ref: '#/components/schemas/type_:SecretDependencyType'
      required:
        - tools
        - agents
        - others
      title: ConvAiStoredSecretDependencies
    type_:ConvAiWorkspaceStoredSecretConfig:
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
          $ref: '#/components/schemas/type_:ConvAiStoredSecretDependencies'
      required:
        - type
        - secret_id
        - name
        - used_by
      title: ConvAiWorkspaceStoredSecretConfig
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Response**

```json
{
  "type": "stored",
  "secret_id": "secret_id",
  "name": "name",
  "used_by": {
    "tools": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1,
        "id": "id",
        "name": "name"
      }
    ],
    "agents": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1,
        "id": "id",
        "name": "name"
      }
    ],
    "others": [
      "conversation_initiation_webhook"
    ],
    "tools_has_more": true,
    "agents_has_more": true,
    "phone_numbers": [
      {
        "phone_number_id": "phone_number_id",
        "phone_number": "phone_number",
        "label": "label",
        "provider": "twilio"
      }
    ],
    "phone_numbers_has_more": true,
    "mcp_servers": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1,
        "id": "id",
        "name": "name"
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
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
