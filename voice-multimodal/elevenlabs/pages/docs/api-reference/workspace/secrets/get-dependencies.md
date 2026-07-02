---
title: "Get secret dependencies"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies.md
path: docs/api-reference/workspace/secrets/get-dependencies
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secret dependencies

GET https://api.elevenlabs.io/v1/convai/secrets/{secret_id}/dependencies/{resource_type}

Get paginated list of resources that depend on a specific secret, filtered by resource type.

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/secrets/{secret_id}/dependencies/{resource_type}:
    get:
      operationId: get_dependencies
      summary: Get Secret Dependencies By Type
      description: >-
        Get paginated list of resources that depend on a specific secret,
        filtered by resource type.
      tags:
        - subpackage_conversationalAi/secrets
      parameters:
        - name: secret_id
          in: path
          required: true
          schema:
            type: string
        - name: resource_type
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/SecretDependencyResourceType'
        - name: page_size
          in: query
          description: How many dependency items to return per page.
          required: false
          schema:
            type: integer
            default: 20
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
                $ref: '#/components/schemas/GetSecretDependenciesResponseModel'
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
    SecretDependencyResourceType:
      type: string
      enum:
        - tools
        - agents
        - phone_numbers
      title: SecretDependencyResourceType
    GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        GetSecretDependenciesResponseModelDependenciesOneOf0ItemsDiscriminatorMappingAvailableAccessLevel
    GetSecretDependenciesResponseModelDependenciesOneOf0Items:
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
      title: GetSecretDependenciesResponseModelDependenciesOneOf0Items
    GetSecretDependenciesResponseModelDependencies0:
      type: array
      items:
        $ref: >-
          #/components/schemas/GetSecretDependenciesResponseModelDependenciesOneOf0Items
      title: GetSecretDependenciesResponseModelDependencies0
    V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
    GetSecretDependenciesResponseModelDependenciesOneOf1Items:
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
      title: GetSecretDependenciesResponseModelDependenciesOneOf1Items
    GetSecretDependenciesResponseModelDependencies1:
      type: array
      items:
        $ref: >-
          #/components/schemas/GetSecretDependenciesResponseModelDependenciesOneOf1Items
      title: GetSecretDependenciesResponseModelDependencies1
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
    GetSecretDependenciesResponseModelDependencies2:
      type: array
      items:
        $ref: '#/components/schemas/DependentPhoneNumberIdentifier'
      title: GetSecretDependenciesResponseModelDependencies2
    GetSecretDependenciesResponseModelDependencies:
      oneOf:
        - $ref: '#/components/schemas/GetSecretDependenciesResponseModelDependencies0'
        - $ref: '#/components/schemas/GetSecretDependenciesResponseModelDependencies1'
        - $ref: '#/components/schemas/GetSecretDependenciesResponseModelDependencies2'
      title: GetSecretDependenciesResponseModelDependencies
    GetSecretDependenciesResponseModel:
      type: object
      properties:
        dependencies:
          $ref: '#/components/schemas/GetSecretDependenciesResponseModelDependencies'
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for fetching the next page of dependencies
      required:
        - dependencies
      title: GetSecretDependenciesResponseModel
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
  "dependencies": [
    {
      "access_level": "editor",
      "created_at_unix_secs": 1685000000,
      "id": "tool_9f8b7c6d",
      "name": "Data Enrichment API",
      "type": "available"
    }
  ],
  "next_cursor": "eyJwYWdlIjoxLCJpZCI6InRvb2xfOWY4YjdjNmQifQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.getDependencies("tools", "secret_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.get_dependencies(
    resource_type="tools",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")! as URL,
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
