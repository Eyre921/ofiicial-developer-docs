---
title: "Get tool executions"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-executions.md
path: docs/eleven-agents/api-reference/tools/get-executions
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get tool executions

GET https://api.elevenlabs.io/v1/convai/tools/{tool_id}/executions

Get paginated list of tool executions for a specific tool.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-executions

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
            type: string
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
            type: boolean
        - name: agent_id
          in: query
          description: Filter by agent ID.
          required: false
          schema:
            type: string
        - name: branch_id
          in: query
          description: Filter by agent branch ID.
          required: false
          schema:
            type: string
        - name: start_time
          in: query
          description: Filter executions from this Unix timestamp (inclusive).
          required: false
          schema:
            type: number
            format: double
        - name: end_time
          in: query
          description: Filter executions until this Unix timestamp (inclusive).
          required: false
          schema:
            type: number
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
                $ref: '#/components/schemas/type_:GetToolExecutionsPageResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:ConversationHistoryTranscriptToolCallWebhookDetails:
      type: object
      properties:
        type:
          type: string
          enum:
            - webhook
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
          type: string
      required:
        - method
        - url
      title: ConversationHistoryTranscriptToolCallWebhookDetails
    type_:ToolExecutionResponseModelToolCallDetails:
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
                #/components/schemas/type_:ConversationHistoryTranscriptToolCallWebhookDetails
          required:
            - type
            - integration_id
            - credential_id
            - integration_connection_id
            - webhook_details
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
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
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
              type: string
          required:
            - type
            - method
            - url
      discriminator:
        propertyName: type
      title: ToolExecutionResponseModelToolCallDetails
    type_:ToolExecutionResponseModel:
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
          type: string
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
          type: string
          description: LLM-extracted parameters sent to the tool (JSON string)
        response_payload:
          type: string
          description: Response returned by the tool
        error_message:
          type: string
          description: Error message if the tool execution failed
        error_type:
          type: string
          description: >-
            Error category (internal, customer_config, customer_auth,
            external_server, external_client, client_timeout, unknown)
        id:
          type: string
        tool_call_details:
          $ref: '#/components/schemas/type_:ToolExecutionResponseModelToolCallDetails'
      required:
        - tool_id
        - tool_request_id
        - conversation_id
        - agent_id
        - timestamp
        - latency_secs
        - id
      title: ToolExecutionResponseModel
    type_:GetToolExecutionsPageResponseModel:
      type: object
      properties:
        executions:
          type: array
          items:
            $ref: '#/components/schemas/type_:ToolExecutionResponseModel'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - executions
        - has_more
      title: GetToolExecutionsPageResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Response**

```json
{
  "executions": [
    {
      "tool_id": "tool_id",
      "tool_request_id": "tool_request_id",
      "conversation_id": "conversation_id",
      "agent_id": "agent_id",
      "timestamp": 1.1,
      "latency_secs": 1.1,
      "id": "id",
      "branch_id": "branch_id",
      "is_error": true,
      "request_payload": "request_payload",
      "response_payload": "response_payload",
      "error_message": "error_message",
      "error_type": "error_type",
      "tool_call_details": {
        "type": "api_integration_webhook",
        "credential_id": "credential_id",
        "integration_connection_id": "integration_connection_id",
        "integration_id": "integration_id",
        "webhook_details": {
          "method": "method",
          "url": "url"
        }
      }
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tools.executions.get("tool_id", {
        agentId: "agent_id",
        branchId: "branch_id",
        cursor: "cursor",
        endTime: 1.1,
        isError: true,
        pageSize: 1,
        startTime: 1.1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tools.executions.get(
    tool_id="tool_id",
    agent_id="agent_id",
    branch_id="branch_id",
    cursor="cursor",
    end_time=1.1,
    is_error=True,
    page_size=1,
    start_time=1.1,
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id/executions?agent_id=agent_id&branch_id=branch_id&cursor=cursor&end_time=1.1&is_error=true&page_size=1&start_time=1.1"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions?agent_id=agent_id&branch_id=branch_id&cursor=cursor&end_time=1.1&is_error=true&page_size=1&start_time=1.1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions?agent_id=agent_id&branch_id=branch_id&cursor=cursor&end_time=1.1&is_error=true&page_size=1&start_time=1.1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools/tool_id/executions?agent_id=agent_id&branch_id=branch_id&cursor=cursor&end_time=1.1&is_error=true&page_size=1&start_time=1.1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions?agent_id=agent_id&branch_id=branch_id&cursor=cursor&end_time=1.1&is_error=true&page_size=1&start_time=1.1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id/executions?agent_id=agent_id&branch_id=branch_id&cursor=cursor&end_time=1.1&is_error=true&page_size=1&start_time=1.1")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
