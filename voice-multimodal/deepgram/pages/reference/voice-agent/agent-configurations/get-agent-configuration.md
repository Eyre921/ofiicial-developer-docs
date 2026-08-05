---
title: "Get Agent Configuration"
source: https://developers.deepgram.com/reference/voice-agent/agent-configurations/get-agent-configuration.md
path: reference/voice-agent/agent-configurations/get-agent-configuration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get Agent Configuration

GET https://api.deepgram.com/v1/projects/{project_id}/agents/{agent_id}

Returns the specified agent configuration in its uninterpolated form

Reference: https://developers.deepgram.com/reference/voice-agent/agent-configurations/get-agent-configuration

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/agents/{agent_id}:
    get:
      operationId: get
      summary: Get an Agent Configuration
      description: Returns the specified agent configuration in its uninterpolated form
      tags:
        - configurations
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: agent_id
          in: path
          description: The unique identifier of the agent configuration
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
          description: An agent configuration
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentConfigurationV1'
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
    AgentConfigurationV1Config:
      type: object
      properties: {}
      description: The agent configuration object
      title: AgentConfigurationV1Config
    AgentConfigurationV1:
      type: object
      properties:
        agent_id:
          type: string
          description: The unique identifier of the agent configuration
        config:
          $ref: '#/components/schemas/AgentConfigurationV1Config'
          description: The agent configuration object
        metadata:
          type: object
          additionalProperties:
            type: string
          description: >-
            A map of arbitrary key-value pairs for labeling or organizing the
            agent configuration
        created_at:
          type: string
          format: date-time
          description: Timestamp when the configuration was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the configuration was last updated
      required:
        - agent_id
        - config
      description: A reusable agent configuration
      title: AgentConfigurationV1
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
  "agent_id": "string",
  "config": {},
  "metadata": {},
  "created_at": "2024-01-15T09:30:00Z",
  "updated_at": "2024-01-15T09:30:00Z"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890")! as URL,
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
