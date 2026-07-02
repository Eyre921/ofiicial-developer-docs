---
title: "Get tool executions"
source: https://elevenlabs.io/docs/api-reference/tools/get-executions.md
path: docs/api-reference/tools/get-executions
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get tool executions

GET https://api.elevenlabs.io/v1/convai/tools/{tool_id}/executions

Get paginated list of tool executions for a specific tool.

Reference: https://elevenlabs.io/docs/api-reference/tools/get-executions

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/tools/{tool_id}/executions:
    get:
      operationId: get
      summary: Get Tool Executions
      description: Get paginated list of tool executions for a specific tool.
      tags:
        - subpackage_conversationalAi/tools/executions
      parameters:
        - name: tool_id
          in: path
          description: ID of the requested tool.
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: >-
            How many documents to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: is_error
          in: query
          description: Filter by error status. If not provided, returns all executions.
          required: false
          schema:
            type:
              - boolean
              - 'null'
        - name: agent_id
          in: query
          description: Filter by agent ID.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: branch_id
          in: query
          description: Filter by agent branch ID.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: start_time
          in: query
          description: Filter executions from this Unix timestamp (inclusive).
          required: false
          schema:
            type:
              - number
              - 'null'
            format: double
        - name: end_time
          in: query
          description: Filter executions until this Unix timestamp (inclusive).
          required: false
          schema:
            type:
              - number
              - 'null'
            format: double
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
                $ref: '#/components/schemas/GetToolExecutionsPageResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    ConversationHistoryTranscriptToolCallWebhookDetails:
      type: object
      properties:
        method:
          type: string
        url:
          type: string
        headers:
          type: object
          additionalProperties:
            type: string
        path_params:
          type: object
          additionalProperties:
            type: string
        query_params:
          type: object
          additionalProperties:
            type: string
        body:
          type:
            - string
            - 'null'
      required:
        - method
        - url
      title: ConversationHistoryTranscriptToolCallWebhookDetails
    ToolExecutionResponseModelToolCallDetails:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - api_integration_webhook
              description: 'Discriminator value: api_integration_webhook'
            integration_id:
              type: string
              default: ''
            credential_id:
              type: string
              default: ''
            integration_connection_id:
              type: string
              default: ''
            webhook_details:
              $ref: >-
                #/components/schemas/ConversationHistoryTranscriptToolCallWebhookDetails
          required:
            - type
            - integration_id
            - credential_id
            - integration_connection_id
            - webhook_details
          description: >-
            ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetails
            variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - client
              description: 'Discriminator value: client'
            parameters:
              type: string
          required:
            - type
            - parameters
          description: ConversationHistoryTranscriptToolCallClientDetails variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - mcp
              description: 'Discriminator value: mcp'
            mcp_server_id:
              type: string
            mcp_server_name:
              type: string
            integration_type:
              type: string
            parameters:
              type: object
              additionalProperties:
                type: string
            approval_policy:
              type: string
            requires_approval:
              type: boolean
              default: false
            mcp_tool_name:
              type: string
              default: ''
            mcp_tool_description:
              type: string
              default: ''
          required:
            - type
            - mcp_server_id
            - mcp_server_name
            - integration_type
            - approval_policy
          description: ConversationHistoryTranscriptToolCallMCPDetails variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
              description: 'Discriminator value: webhook'
            method:
              type: string
            url:
              type: string
            headers:
              type: object
              additionalProperties:
                type: string
            path_params:
              type: object
              additionalProperties:
                type: string
            query_params:
              type: object
              additionalProperties:
                type: string
            body:
              type:
                - string
                - 'null'
          required:
            - type
            - method
            - url
          description: ConversationHistoryTranscriptToolCallWebhookDetails variant
      discriminator:
        propertyName: type
      title: ToolExecutionResponseModelToolCallDetails
    ToolExecutionResponseModel:
      type: object
      properties:
        tool_id:
          type: string
          description: The ID of the tool that was executed
        tool_request_id:
          type: string
          description: The request/call ID associated with this tool execution
        conversation_id:
          type: string
          description: The ID of the conversation where the tool was executed
        agent_id:
          type: string
          description: The ID of the agent that ran the tool
        branch_id:
          type:
            - string
            - 'null'
          description: The branch ID if the agent has branches
        timestamp:
          type: number
          format: double
          description: Unix timestamp when the tool was executed
        latency_secs:
          type: number
          format: double
          description: How long the tool execution took
        is_error:
          type: boolean
          default: false
          description: Whether the tool execution failed
        request_payload:
          type:
            - string
            - 'null'
          description: LLM-extracted parameters sent to the tool (JSON string)
        response_payload:
          type:
            - string
            - 'null'
          description: Response returned by the tool
        error_message:
          type:
            - string
            - 'null'
          description: Error message if the tool execution failed
        error_type:
          type:
            - string
            - 'null'
          description: >-
            Error category (internal, customer_config, customer_auth,
            external_server, external_client, client_timeout, unknown)
        id:
          type: string
        tool_call_details:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionResponseModelToolCallDetails'
            - type: 'null'
      required:
        - tool_id
        - tool_request_id
        - conversation_id
        - agent_id
        - timestamp
        - latency_secs
        - id
      title: ToolExecutionResponseModel
    GetToolExecutionsPageResponseModel:
      type: object
      properties:
        executions:
          type: array
          items:
            $ref: '#/components/schemas/ToolExecutionResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - executions
        - has_more
      title: GetToolExecutionsPageResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
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
  "executions": [
    {
      "tool_id": "tool_9f8b7c6d5e4a3b2c1d0e",
      "tool_request_id": "req_1234567890abcdef",
      "conversation_id": "conv_abcdef1234567890",
      "agent_id": "agent_0011223344556677",
      "timestamp": 1685606400,
      "latency_secs": 2.35,
      "id": "exec_0987654321fedcba",
      "branch_id": "branch_main",
      "is_error": false,
      "request_payload": "{\"query\":\"Get weather forecast for New York\"}",
      "response_payload": "{\"forecast\":\"Sunny with a high of 75°F\"}",
      "error_message": null,
      "error_type": null,
      "tool_call_details": {
        "type": "webhook",
        "method": "POST",
        "url": "https://api.weatherprovider.com/v1/forecast",
        "body": "{\"date\":\"2024-06-01\"}",
        "headers": {
          "Authorization": "Bearer abcdef1234567890",
          "Content-Type": "application/json"
        },
        "path_params": {
          "location": "New York"
        },
        "query_params": {
          "units": "imperial"
        }
      }
    }
  ],
  "has_more": true,
  "next_cursor": "cursor_abcdef123456"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tools.executions.get("tool_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tools.executions.get(
    tool_id="tool_id",
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

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id/executions"

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

url = URI("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools/tool_id/executions', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id/executions")! as URL,
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
