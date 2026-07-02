---
title: "Get secrets"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/list.md
path: docs/eleven-agents/api-reference/workspace/secrets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secrets

GET https://api.elevenlabs.io/v1/convai/secrets

Get all workspace secrets for the user

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/list

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
            type: integer
        - name: dependency_limit
          in: query
          description: >-
            Maximum number of dependent resources (tools, agents, phone numbers)
            to return per secret. Can not exceed 100.
          required: false
          schema:
            type: integer
        - name: search
          in: query
          description: >-
            If specified, returns only secrets whose names start with this
            string.
          required: false
          schema:
            type: string
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
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
                $ref: '#/components/schemas/type_:GetWorkspaceSecretsResponseModel'
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
    type_:GetWorkspaceSecretsResponseModel:
      type: object
      properties:
        secrets:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConvAiWorkspaceStoredSecretConfig'
        next_cursor:
          type: string
          description: Cursor for fetching the next page of secrets
      required:
        - secrets
      title: GetWorkspaceSecretsResponseModel
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

**Request**

```json
{}
```

**Response**

```json
{
  "secrets": [
    {
      "type": "stored",
      "secret_id": "sec_9f8b7c6d5e4a3b2c1d0e",
      "name": "PaymentGatewayAPIKey",
      "used_by": {
        "tools": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1685000000,
            "id": "tool_123abc456def",
            "name": "Stripe Integration"
          }
        ],
        "agents": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1685100000,
            "id": "agent_789xyz012uvw",
            "name": "Billing Agent"
          }
        ],
        "others": [
          "conversation_initiation_webhook"
        ]
      }
    }
  ],
  "next_cursor": "cursor_eyJwYWdlIjoxfQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.list({
        cursor: "cursor",
        dependencyLimit: 1,
        pageSize: 1,
        search: "search",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.list(
    cursor="cursor",
    dependency_limit=1,
    page_size=1,
    search="search",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search")! as URL,
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
