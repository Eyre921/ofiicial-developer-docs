---
title: "Get a Project Model"
source: https://developers.deepgram.com/reference/manage/projects/models/get.md
path: reference/manage/projects/models/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get a Project Model

GET https://api.deepgram.com/v1/projects/{project_id}/models/{model_id}

Returns metadata for a specific model

Reference: https://developers.deepgram.com/reference/manage/projects/models/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/models/{model_id}:
    get:
      operationId: get
      summary: Get a Project Model
      description: Returns metadata for a specific model
      tags:
        - models
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: model_id
          in: path
          description: The specific UUID of the model
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
          description: A model object that can be either STT or TTS
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetModelV1Response'
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
    GetModelV1Response0:
      type: object
      properties:
        name:
          type: string
        canonical_name:
          type: string
        architecture:
          type: string
        languages:
          type: array
          items:
            type: string
        version:
          type: string
        uuid:
          type: string
          format: uuid
        batch:
          type: boolean
        streaming:
          type: boolean
        formatted_output:
          type: boolean
      title: GetModelV1Response0
    GetModelV1ResponseOneOf1Metadata:
      type: object
      properties:
        accent:
          type: string
        age:
          type: string
        color:
          type: string
        image:
          type: string
          format: uri
        sample:
          type: string
          format: uri
        tags:
          type: array
          items:
            type: string
        use_cases:
          type: array
          items:
            type: string
      title: GetModelV1ResponseOneOf1Metadata
    GetModelV1Response1:
      type: object
      properties:
        name:
          type: string
        canonical_name:
          type: string
        architecture:
          type: string
        languages:
          type: array
          items:
            type: string
        version:
          type: string
        uuid:
          type: string
          format: uuid
        metadata:
          $ref: '#/components/schemas/GetModelV1ResponseOneOf1Metadata'
      title: GetModelV1Response1
    GetModelV1Response:
      oneOf:
        - $ref: '#/components/schemas/GetModelV1Response0'
        - $ref: '#/components/schemas/GetModelV1Response1'
      title: GetModelV1Response
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



**Response**

```json
{
  "architecture": "polaris",
  "batch": true,
  "canonical_name": "enhanced-general",
  "formatted_output": false,
  "languages": [
    "en",
    "en-us"
  ],
  "name": "general",
  "streaming": true,
  "uuid": "c7226e9e-ae1c-4057-ae2a-a71a6b0dc588",
  "version": "2022-05-18.1"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291';
const options = {method: 'GET', headers: {Authorization: 'Token <apiKey>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Token <apiKey>")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Token <apiKey>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

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
