---
title: "List Project Requests"
source: https://developers.deepgram.com/reference/manage/requests/list.md
path: reference/manage/requests/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Requests

GET https://api.deepgram.com/v1/projects/{project_id}/requests

Generates a list of requests for a specific project

Reference: https://developers.deepgram.com/reference/manage/requests/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/requests:
    get:
      operationId: list
      summary: List Project Requests
      description: Generates a list of requests for a specific project
      tags:
        - requests
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: start
          in: query
          description: >-
            Start date of the requested date range. Formats accepted are
            YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM
          required: false
          schema:
            type: string
            format: date-time
        - name: end
          in: query
          description: >-
            End date of the requested date range. Formats accepted are
            YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM
          required: false
          schema:
            type: string
            format: date-time
        - name: limit
          in: query
          description: Number of results to return per page. Default 10. Range [1,1000]
          required: false
          schema:
            type: number
            format: double
            default: 10
        - name: page
          in: query
          description: >-
            Navigate and return the results to retrieve specific portions of
            information of the response
          required: false
          schema:
            type: number
            format: double
        - name: accessor
          in: query
          description: Filter for requests where a specific accessor was used
          required: false
          schema:
            type: string
        - name: request_id
          in: query
          description: Filter for a specific request id
          required: false
          schema:
            type: string
        - name: deployment
          in: query
          description: Filter for requests where a specific deployment was used
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1ProjectsProjectIdRequestsGetParametersDeployment
        - name: endpoint
          in: query
          description: Filter for requests where a specific endpoint was used
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1ProjectsProjectIdRequestsGetParametersEndpoint
        - name: method
          in: query
          description: Filter for requests where a specific method was used
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1ProjectsProjectIdRequestsGetParametersMethod
        - name: status
          in: query
          description: >-
            Filter for requests that succeeded (status code < 300) or failed
            (status code >=400)
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1ProjectsProjectIdRequestsGetParametersStatus
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
          description: A list of requests for a specific project
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListProjectRequestsV1Response'
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
    V1ProjectsProjectIdRequestsGetParametersDeployment:
      type: string
      enum:
        - hosted
        - beta
        - self-hosted
      description: Deployment type for the requests
      title: V1ProjectsProjectIdRequestsGetParametersDeployment
    V1ProjectsProjectIdRequestsGetParametersEndpoint:
      type: string
      enum:
        - listen
        - read
        - speak
        - agent
      title: V1ProjectsProjectIdRequestsGetParametersEndpoint
    V1ProjectsProjectIdRequestsGetParametersMethod:
      type: string
      enum:
        - sync
        - async
        - streaming
      description: Method type for the request
      title: V1ProjectsProjectIdRequestsGetParametersMethod
    V1ProjectsProjectIdRequestsGetParametersStatus:
      type: string
      enum:
        - succeeded
        - failed
      title: V1ProjectsProjectIdRequestsGetParametersStatus
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
    ListProjectRequestsV1Response:
      type: object
      properties:
        page:
          type: number
          format: double
          description: The page number of the paginated response
        limit:
          type: number
          format: double
          description: The number of results per page
        requests:
          type: array
          items:
            $ref: '#/components/schemas/ProjectRequestResponse'
      title: ListProjectRequestsV1Response
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
  "page": 0,
  "limit": 10,
  "requests": [
    {
      "request_id": "a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d",
      "project_uuid": "12345678-90ab-cdef-1234-567890abcdef",
      "created": "2024-01-15T09:48:20.000Z",
      "path": "/v1/listen?",
      "api_key_id": "b1e2c3d4-5678-90ab-cdef-1234567890ab",
      "response": {
        "code": 200,
        "completed": "2024-01-15T09:48:21.000Z",
        "deployment": "hosted:us",
        "details": {
          "channels": 1,
          "config": {},
          "duration": 30,
          "features": [],
          "metadata": {},
          "method": "sync",
          "models": [
            "1a2b3c4d-5e6f-4a8b-9c0d-1e2f3a4b5c6d"
          ],
          "streams": 1,
          "tags": [],
          "tier": "base",
          "total_audio": 30,
          "usd": 0.0075
        },
        "token_details": []
      },
      "callback": null
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests';
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

	url := "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests"

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

url = URI("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests")! as URL,
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
