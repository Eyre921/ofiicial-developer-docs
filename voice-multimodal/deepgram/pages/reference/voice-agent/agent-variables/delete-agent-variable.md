---
title: "Delete Agent Variable"
source: https://developers.deepgram.com/reference/voice-agent/agent-variables/delete-agent-variable.md
path: reference/voice-agent/agent-variables/delete-agent-variable
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Delete Agent Variable

DELETE https://api.deepgram.com/v1/projects/{project_id}/agent-variables/{variable_id}

Deletes the specified template variable

Reference: https://developers.deepgram.com/reference/voice-agent/agent-variables/delete-agent-variable

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/agent-variables/{variable_id}:
    delete:
      operationId: delete
      summary: Delete an Agent Variable
      description: Deletes the specified template variable
      tags:
        - subpackage_voiceAgent.subpackage_voiceAgent/variables
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: variable_id
          in: path
          description: The unique identifier of the agent variable
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
          description: Agent variable deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteAgentVariableV1Response'
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
    DeleteAgentVariableV1Response:
      type: object
      properties: {}
      description: Confirmation that the agent variable was deleted
      title: DeleteAgentVariableV1Response
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
{}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890';
const options = {
  method: 'DELETE',
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890', [
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

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890");
var request = new RestRequest(Method.DELETE);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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
