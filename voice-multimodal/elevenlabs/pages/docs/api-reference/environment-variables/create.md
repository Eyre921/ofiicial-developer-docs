---
title: "Create environment variable"
source: https://elevenlabs.io/docs/api-reference/environment-variables/create.md
path: docs/api-reference/environment-variables/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create environment variable

POST https://api.elevenlabs.io/v1/convai/environment-variables
Content-Type: application/json

Create a new environment variable for the workspace

Reference: https://elevenlabs.io/docs/api-reference/environment-variables/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/environment-variables:
    post:
      operationId: create
      summary: Create Environment Variable
      description: Create a new environment variable for the workspace
      tags:
        - environmentVariables
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
                $ref: '#/components/schemas/EnvironmentVariableResponse'
        '400':
          description: Invalid parameters
          content:
            application/json:
              schema:
                description: Any type
        '409':
          description: Environment variable with this label already exists
          content:
            application/json:
              schema:
                description: Any type
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
              $ref: '#/components/schemas/environment_variables_create_Request'
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
    EnvironmentVariableSecretValueRequest:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      title: EnvironmentVariableSecretValueRequest
    EnvironmentVariableAuthConnectionValueRequest:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
      title: EnvironmentVariableAuthConnectionValueRequest
    environment_variables_create_Request:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - string
              description: 'Discriminator value: string'
            label:
              type: string
              description: Unique label for the environment variable.
            values:
              type: object
              additionalProperties:
                type: string
              description: Environment-specific values. Must include 'production' key.
          required:
            - type
            - label
            - values
          description: CreateStringEnvironmentVariableRequest variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - secret
              description: 'Discriminator value: secret'
            label:
              type: string
              description: Unique label for the environment variable.
            values:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/EnvironmentVariableSecretValueRequest'
              description: >-
                Environment-specific secret references. Must include
                'production' key.
          required:
            - type
            - label
            - values
          description: CreateSecretEnvironmentVariableRequest variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - auth_connection
              description: 'Discriminator value: auth_connection'
            label:
              type: string
              description: Unique label for the environment variable.
            values:
              type: object
              additionalProperties:
                $ref: >-
                  #/components/schemas/EnvironmentVariableAuthConnectionValueRequest
              description: >-
                Environment-specific auth connection references. Must include
                'production' key.
          required:
            - type
            - label
            - values
          description: CreateAuthConnectionEnvironmentVariableRequest variant
      discriminator:
        propertyName: type
      title: environment_variables_create_Request
    EnvironmentVariableResponseType:
      type: string
      enum:
        - string
        - secret
        - auth_connection
      title: EnvironmentVariableResponseType
    EnvironmentVariableSecretValue:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      title: EnvironmentVariableSecretValue
    EnvironmentVariableResponseValues1:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/EnvironmentVariableSecretValue'
      title: EnvironmentVariableResponseValues1
    EnvironmentVariableAuthConnectionValue:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
      title: EnvironmentVariableAuthConnectionValue
    EnvironmentVariableResponseValues2:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/EnvironmentVariableAuthConnectionValue'
      title: EnvironmentVariableResponseValues2
    EnvironmentVariableResponseValues:
      oneOf:
        - type: object
          additionalProperties:
            type: string
        - $ref: '#/components/schemas/EnvironmentVariableResponseValues1'
        - $ref: '#/components/schemas/EnvironmentVariableResponseValues2'
      title: EnvironmentVariableResponseValues
    EnvironmentVariableResponse:
      type: object
      properties:
        label:
          type: string
        created_at_unix_secs:
          type: integer
        updated_at_unix_secs:
          type: integer
        created_by_user_id:
          type:
            - string
            - 'null'
        type:
          $ref: '#/components/schemas/EnvironmentVariableResponseType'
        id:
          type: string
        workspace_id:
          type: string
        values:
          $ref: '#/components/schemas/EnvironmentVariableResponseValues'
      required:
        - label
        - created_at_unix_secs
        - updated_at_unix_secs
        - type
        - id
        - workspace_id
        - values
      title: EnvironmentVariableResponse
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
{
  "type": "string",
  "label": "string"
}
```

**Response**

```json
{
  "label": "string",
  "created_at_unix_secs": 1,
  "updated_at_unix_secs": 1,
  "type": "string",
  "id": "string",
  "workspace_id": "string",
  "values": {},
  "created_by_user_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.create({
        type: "string",
        label: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs
from elevenlabs.environment_variables import EnvironmentVariablesCreateRequestBody_String

client = ElevenLabs()

client.environment_variables.create(
    request=EnvironmentVariablesCreateRequestBody_String(
        label="string",
        values={},
    ),
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

	url := "https://api.elevenlabs.io/v1/convai/environment-variables"

	payload := strings.NewReader("{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/environment-variables")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/environment-variables', [
  'body' => '{
  "type": "string",
  "label": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "type": "string",
  "label": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
