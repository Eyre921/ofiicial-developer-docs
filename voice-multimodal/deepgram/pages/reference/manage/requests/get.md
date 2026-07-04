---
title: "Get a Project Request"
source: https://developers.deepgram.com/reference/manage/requests/get.md
path: reference/manage/requests/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get a Project Request

GET https://api.deepgram.com/v1/projects/{project_id}/requests/{request_id}

Retrieves a specific request for a specific project

Reference: https://developers.deepgram.com/reference/manage/requests/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/requests/{request_id}:
    get:
      operationId: get
      summary: Get a Project Request
      description: Retrieves a specific request for a specific project
      tags:
        - manage > v1 > projects > requests
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: request_id
          in: path
          description: The unique identifier of the request
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: |
            Use `Authorization: Token <API_KEY>`
            Example: `Authorization: Token 12345abcdef`
          required: true
          schema:
            type: string
      responses:
        '200':
          description: A specific request for a specific project
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetProjectRequestV1Response'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    ProjectRequestResponseResponse:
      type: object
      properties: {}
      description: The response of the request
      title: ProjectRequestResponseResponse
    ProjectRequestResponse:
      type: object
      properties:
        request_id:
          type: string
          description: The unique identifier of the request
        project_uuid:
          type: string
          description: The unique identifier of the project
        created:
          type: string
          format: date-time
          description: The date and time the request was created
        path:
          type: string
          description: The API path of the request
        api_key_id:
          type: string
          description: The unique identifier of the API key
        response:
          $ref: '#/components/schemas/ProjectRequestResponseResponse'
          description: The response of the request
        code:
          type: number
          format: double
          description: The response code of the request
        deployment:
          type: string
          description: The deployment type
        callback:
          type: string
          description: The callback URL for the request
      description: A single request
      title: ProjectRequestResponse
    GetProjectRequestV1Response:
      type: object
      properties:
        request:
          $ref: '#/components/schemas/ProjectRequestResponse'
      title: GetProjectRequestV1Response
    ErrorResponseTextError:
      type: string
      title: ErrorResponseTextError
    ErrorResponseLegacyError:
      type: object
      properties:
        err_code:
          type: string
          description: The error code
        err_msg:
          type: string
          description: The error message
        request_id:
          type: string
          description: The request ID
      title: ErrorResponseLegacyError
    ErrorResponseModernError:
      type: object
      properties:
        category:
          type: string
          description: The category of the error
        message:
          type: string
          description: A message about the error
        details:
          type: string
          description: A description of the error
        request_id:
          type: string
          description: The unique identifier of the request
      title: ErrorResponseModernError
    ErrorResponse:
      oneOf:
        - $ref: '#/components/schemas/ErrorResponseTextError'
        - $ref: '#/components/schemas/ErrorResponseLegacyError'
        - $ref: '#/components/schemas/ErrorResponseModernError'
      title: ErrorResponse
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: |
        Use `Authorization: Token <API_KEY>`
        Example: `Authorization: Token 12345abcdef`

```

## Examples



**Request**

```json
{}
```

**Response**

```json
{
  "request": {
    "request_id": "123e4567-e89b-12d3-a456-426614174000",
    "project_uuid": "987f6543-e21b-45d6-b789-123456789abc",
    "created": "2024-01-15T09:30:00Z",
    "path": "/v1/projects/987f6543-e21b-45d6-b789-123456789abc/requests/123e4567-e89b-12d3-a456-426614174000",
    "api_key_id": "api_4f7a9b2c3d6e8f1a2b3c4d5e",
    "response": {},
    "code": 200,
    "deployment": "production-us-east-1",
    "callback": "https://webhook.example.com/deepgram/callback"
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234';
const options = {
  method: 'GET',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/requests/123456-7890-1234-5678-901234")! as URL,
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
