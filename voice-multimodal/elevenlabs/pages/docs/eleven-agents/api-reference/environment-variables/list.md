---
title: "List environment variables"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list.md
path: docs/eleven-agents/api-reference/environment-variables/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List environment variables

GET https://api.elevenlabs.io/v1/convai/environment-variables

List all environment variables for the workspace with optional filtering

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list

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
            type: string
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
            type: string
        - name: environment
          in: query
          description: >-
            Filter to only return variables that have this environment. When
            specified, the values dict in the response will only contain this
            environment.
          required: false
          schema:
            type: string
        - name: type
          in: query
          description: Filter by variable type
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_environmentVariables:EnvironmentVariablesListRequestType
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
                $ref: '#/components/schemas/type_:EnvironmentVariablesListResponse'
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
    type_environmentVariables:EnvironmentVariablesListRequestType:
      type: string
      enum:
        - string
        - secret
        - auth_connection
      title: EnvironmentVariablesListRequestType
    type_:EnvironmentVariableResponseType:
      type: string
      enum:
        - string
        - secret
        - auth_connection
      title: EnvironmentVariableResponseType
    type_:EnvironmentVariableSecretValue:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      title: EnvironmentVariableSecretValue
    type_:EnvironmentVariableAuthConnectionValue:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
      title: EnvironmentVariableAuthConnectionValue
    type_:EnvironmentVariableResponseValues:
      oneOf:
        - type: object
          additionalProperties:
            type: string
        - type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:EnvironmentVariableSecretValue'
        - type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:EnvironmentVariableAuthConnectionValue'
      title: EnvironmentVariableResponseValues
    type_:EnvironmentVariableResponse:
      type: object
      properties:
        label:
          type: string
        created_at_unix_secs:
          type: integer
        updated_at_unix_secs:
          type: integer
        created_by_user_id:
          type: string
        type:
          $ref: '#/components/schemas/type_:EnvironmentVariableResponseType'
        id:
          type: string
        workspace_id:
          type: string
        values:
          $ref: '#/components/schemas/type_:EnvironmentVariableResponseValues'
      required:
        - label
        - created_at_unix_secs
        - updated_at_unix_secs
        - type
        - id
        - workspace_id
        - values
      title: EnvironmentVariableResponse
    type_:EnvironmentVariablesListResponse:
      type: object
      properties:
        environment_variables:
          type: array
          items:
            $ref: '#/components/schemas/type_:EnvironmentVariableResponse'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - environment_variables
        - has_more
      title: EnvironmentVariablesListResponse
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
  "environment_variables": [
    {
      "label": "API_ENDPOINT",
      "created_at_unix_secs": 1685000000,
      "updated_at_unix_secs": 1687600000,
      "type": "string",
      "id": "envvar_123abc456def",
      "workspace_id": "workspace_789xyz123",
      "values": {
        "production": "https://api.production.example.com",
        "staging": "https://api.staging.example.com"
      },
      "created_by_user_id": "user_987654321"
    }
  ],
  "has_more": false,
  "next_cursor": "cursor_abcdef123456"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.list({
        cursor: "cursor",
        environment: "environment",
        label: "label",
        pageSize: 1,
        type: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.environment_variables.list(
    cursor="cursor",
    environment="environment",
    label="label",
    page_size=1,
    type="string",
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

	url := "https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string"

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")! as URL,
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
