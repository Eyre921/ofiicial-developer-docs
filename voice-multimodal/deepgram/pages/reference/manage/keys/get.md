---
title: "Get a Project Key"
source: https://developers.deepgram.com/reference/manage/keys/get.md
path: reference/manage/keys/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get a Project Key

GET https://api.deepgram.com/v1/projects/{project_id}/keys/{key_id}

Retrieves information about a specified API key

Reference: https://developers.deepgram.com/reference/manage/keys/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/keys/{key_id}:
    get:
      operationId: get
      summary: Get a Project Key
      description: Retrieves information about a specified API key
      tags:
        - >-
          subpackage_manage.subpackage_manage/v1.subpackage_manage/v1/projects.subpackage_manage/v1/projects/keys
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: key_id
          in: path
          description: The unique identifier of the API key
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
          description: A specific API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetProjectKeyV1Response'
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
    GetProjectKeyV1ResponseItemMemberApiKey:
      type: object
      properties:
        api_key_id:
          type: string
        comment:
          type: string
        scopes:
          type: array
          items:
            type: string
        tags:
          type: array
          items:
            type: string
        expiration_date:
          type: string
          format: date-time
        created:
          type: string
          format: date-time
      title: GetProjectKeyV1ResponseItemMemberApiKey
    GetProjectKeyV1ResponseItemMember:
      type: object
      properties:
        member_id:
          type: string
        email:
          type: string
        first_name:
          type: string
        last_name:
          type: string
        api_key:
          $ref: '#/components/schemas/GetProjectKeyV1ResponseItemMemberApiKey'
      title: GetProjectKeyV1ResponseItemMember
    GetProjectKeyV1ResponseItem:
      type: object
      properties:
        member:
          $ref: '#/components/schemas/GetProjectKeyV1ResponseItemMember'
      title: GetProjectKeyV1ResponseItem
    GetProjectKeyV1Response:
      type: object
      properties:
        item:
          $ref: '#/components/schemas/GetProjectKeyV1ResponseItem'
      title: GetProjectKeyV1Response
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
  "item": {
    "member": {
      "member_id": "1000-2000-3000-4000",
      "email": "john@test.com",
      "first_name": "John",
      "last_name": "Doe",
      "api_key": {
        "api_key_id": "1000-2000-3000-4000",
        "comment": "A comment",
        "scopes": [
          "admin"
        ],
        "tags": [
          "prod",
          "west-region"
        ],
        "expiration_date": "2021-01-01T00:00:00Z",
        "created": "2021-01-01T00:00:00Z"
      }
    }
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys/123456789012345678901234")! as URL,
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
