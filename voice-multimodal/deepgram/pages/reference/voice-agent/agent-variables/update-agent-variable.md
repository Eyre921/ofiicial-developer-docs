---
title: "Update Agent Variable"
source: https://developers.deepgram.com/reference/voice-agent/agent-variables/update-agent-variable.md
path: reference/voice-agent/agent-variables/update-agent-variable
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Update Agent Variable

PATCH https://api.deepgram.com/v1/projects/{project_id}/agent-variables/{variable_id}
Content-Type: application/json

Updates the value of an existing template variable

Reference: https://developers.deepgram.com/reference/voice-agent/agent-variables/update-agent-variable

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/agent-variables/{variable_id}:
    patch:
      operationId: update
      summary: Update an Agent Variable
      description: Updates the value of an existing template variable
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
          description: Agent variable updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentVariableV1'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        description: Updated value for the agent variable
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateAgentVariableV1Request'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    UpdateAgentVariableV1Request:
      type: object
      properties:
        value:
          description: The new value to substitute
      required:
        - value
      description: Request body for updating an agent variable
      title: UpdateAgentVariableV1Request
    AgentVariableV1:
      type: object
      properties:
        variable_id:
          type: string
          description: The unique identifier of the variable
        key:
          type: string
          description: The variable name, following the DG_<VARIABLE_NAME> format
        value:
          description: The value to substitute. Can be any valid JSON type
        created_at:
          type: string
          format: date-time
          description: Timestamp when the variable was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the variable was last updated
      required:
        - variable_id
        - key
        - value
      description: A template variable for agent configurations
      title: AgentVariableV1
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
"Welcome to the Deepgram transcription service!"
```

**Response**

```json
{
  "variable_id": "v1a2b3c4-d5e6-7890-abcd-ef1234567890",
  "key": "welcome_message",
  "value": "Welcome to the Deepgram transcription service!",
  "created_at": "2024-01-15T09:30:00Z",
  "updated_at": "2024-01-15T09:30:00Z"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890"

payload = "Welcome to the Deepgram transcription service!"
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890';
const options = {
  method: 'PATCH',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '"Welcome to the Deepgram transcription service!"'
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

	payload := strings.NewReader("\"Welcome to the Deepgram transcription service!\"")

	req, _ := http.NewRequest("PATCH", url, payload)

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

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "\"Welcome to the Deepgram transcription service!\""

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("\"Welcome to the Deepgram transcription service!\"")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890', [
  'body' => '"Welcome to the Deepgram transcription service!"',
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
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "\"Welcome to the Deepgram transcription service!\"", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = "Welcome to the Deepgram transcription service!" as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
