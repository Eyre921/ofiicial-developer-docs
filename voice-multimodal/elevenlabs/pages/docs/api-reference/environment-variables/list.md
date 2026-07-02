---
title: "List environment variables"
source: https://elevenlabs.io/docs/api-reference/environment-variables/list.md
path: docs/api-reference/environment-variables/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List environment variables

GET https://api.elevenlabs.io/v1/convai/environment-variables

List all environment variables for the workspace with optional filtering

Reference: https://elevenlabs.io/docs/api-reference/environment-variables/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/environment-variables:
    get:
      operationId: list
      summary: List Environment Variables
      description: List all environment variables for the workspace with optional filtering
      tags:
        - subpackage_environmentVariables
      parameters:
        - name: cursor
          in: query
          description: Pagination cursor from previous response
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: Number of items to return (1-100)
          required: false
          schema:
            type: integer
            default: 100
        - name: label
          in: query
          description: Filter by exact label match
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: environment
          in: query
          description: >-
            Filter to only return variables that have this environment. When
            specified, the values dict in the response will only contain this
            environment.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: type
          in: query
          description: Filter by variable type
          required: false
          schema:
            oneOf:
              - $ref: >-
                  #/components/schemas/V1ConvaiEnvironmentVariablesGetParametersTypeSchema
              - type: 'null'
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
                $ref: '#/components/schemas/EnvironmentVariablesListResponse'
        '400':
          description: Invalid environment filter
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
    V1ConvaiEnvironmentVariablesGetParametersTypeSchema:
      type: string
      enum:
        - string
        - secret
        - auth_connection
      description: Filter by variable type
      title: V1ConvaiEnvironmentVariablesGetParametersTypeSchema
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
    EnvironmentVariablesListResponse:
      type: object
      properties:
        environment_variables:
          type: array
          items:
            $ref: '#/components/schemas/EnvironmentVariableResponse'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - environment_variables
        - has_more
      title: EnvironmentVariablesListResponse
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
  "environment_variables": [
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
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.environment_variables.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/environment-variables"

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables")! as URL,
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
