---
title: "List Project Models"
source: https://developers.deepgram.com/reference/manage/projects/models/list.md
path: reference/manage/projects/models/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Models

GET https://api.deepgram.com/v1/projects/{project_id}/models

Returns metadata on all the latest models that a specific project has access to, including non-public models

Reference: https://developers.deepgram.com/reference/manage/projects/models/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/models:
    get:
      operationId: list
      summary: List Project Models
      description: >-
        Returns metadata on all the latest models that a specific project has
        access to, including non-public models
      tags:
        - >-
          subpackage_manage.subpackage_manage/v1.subpackage_manage/v1/projects.subpackage_manage/v1/projects/models
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: include_outdated
          in: query
          description: returns non-latest versions of models
          required: false
          schema:
            type: boolean
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
          description: A list of models
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListModelsV1Response'
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
    ListModelsV1ResponseSttModels:
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
        batch:
          type: boolean
        streaming:
          type: boolean
        formatted_output:
          type: boolean
      title: ListModelsV1ResponseSttModels
    ListModelsV1ResponseTtsModelsMetadata:
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
      title: ListModelsV1ResponseTtsModelsMetadata
    ListModelsV1ResponseTtsModels:
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
          $ref: '#/components/schemas/ListModelsV1ResponseTtsModelsMetadata'
      title: ListModelsV1ResponseTtsModels
    ListModelsV1Response:
      type: object
      properties:
        stt:
          type: array
          items:
            $ref: '#/components/schemas/ListModelsV1ResponseSttModels'
        tts:
          type: array
          items:
            $ref: '#/components/schemas/ListModelsV1ResponseTtsModels'
      title: ListModelsV1Response
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
  "stt": [
    {
      "name": "nova-3",
      "canonical_name": "nova-3",
      "architecture": "base",
      "languages": [
        "en",
        "en-us"
      ],
      "version": "2021-11-10.1",
      "uuid": "6b28e919-8427-4f32-9847-492e2efd7daf",
      "batch": true,
      "streaming": true,
      "formatted_output": true
    }
  ],
  "tts": [
    {
      "name": "zeus",
      "canonical_name": "aura-2-zeus-en",
      "architecture": "aura-2",
      "languages": [
        "en",
        "en-US"
      ],
      "version": "2025-04-07.0",
      "uuid": "2baf189d-91ac-481d-b6d1-750888667b31",
      "metadata": {
        "accent": "American",
        "age": "Adult",
        "color": "#C58DFF",
        "image": "https://static.deepgram.com/examples/avatars/zeus.jpg",
        "sample": "https://static.deepgram.com/examples/Aura-2-zeus.wav",
        "tags": [
          "masculine",
          "deep",
          "trustworthy",
          "smooth"
        ],
        "use_cases": [
          "IVR"
        ]
      }
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models")! as URL,
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
