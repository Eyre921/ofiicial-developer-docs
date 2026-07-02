---
title: "Create Agent Configuration"
source: https://developers.deepgram.com/reference/voice-agent/agent-configurations/create-agent-configuration.md
path: reference/voice-agent/agent-configurations/create-agent-configuration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Create Agent Configuration

POST https://api.deepgram.com/v1/projects/{project_id}/agents
Content-Type: application/json

Creates a new reusable agent configuration. The `config` field must be a valid JSON string representing the `agent` block of a Settings message. The returned `agent_id` can be passed in place of the full `agent` object in future Settings messages.

Reference: https://developers.deepgram.com/reference/voice-agent/agent-configurations/create-agent-configuration

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/agents:
    post:
      operationId: create
      summary: Create an Agent Configuration
      description: >-
        Creates a new reusable agent configuration. The `config` field must be a
        valid JSON string representing the `agent` block of a Settings message.
        The returned `agent_id` can be passed in place of the full `agent`
        object in future Settings messages.
      tags:
        - subpackage_voiceAgent.subpackage_voiceAgent/configurations
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
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
          description: Agent configuration created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAgentConfigurationV1Response'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        description: Agent configuration details
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAgentConfigurationV1Request'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    CreateAgentConfigurationV1Request:
      type: object
      properties:
        config:
          type: string
          description: >-
            A valid JSON string representing the agent block of a Settings
            message
        metadata:
          type: object
          additionalProperties:
            type: string
          description: >-
            A map of arbitrary key-value pairs for labeling or organizing the
            agent configuration
        api_version:
          type: integer
          default: 1
          description: API version. Defaults to 1
      required:
        - config
      description: Request body for creating an agent configuration
      title: CreateAgentConfigurationV1Request
    CreateAgentConfigurationV1ResponseConfig:
      type: object
      properties: {}
      description: The parsed agent configuration object
      title: CreateAgentConfigurationV1ResponseConfig
    CreateAgentConfigurationV1Response:
      type: object
      properties:
        agent_id:
          type: string
          description: The unique identifier of the newly created agent configuration
        config:
          $ref: '#/components/schemas/CreateAgentConfigurationV1ResponseConfig'
          description: The parsed agent configuration object
        metadata:
          type: object
          additionalProperties:
            type: string
          description: Metadata associated with the agent configuration
      required:
        - agent_id
        - config
      title: CreateAgentConfigurationV1Response
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
{
  "config": "{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}"
}
```

**Response**

```json
{
  "agent_id": "agent_9f8b7c6d5e4a3b2c1d0e",
  "config": {},
  "metadata": {}
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents"

payload = { "config": "{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"config":"{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}"}'
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents"

	payload := strings.NewReader("{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents', [
  'body' => '{
  "config": "{\\"language\\":\\"en-US\\",\\"model\\":\\"general\\",\\"punctuate\\":true,\\"profanity_filter\\":false}"
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["config": "{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
