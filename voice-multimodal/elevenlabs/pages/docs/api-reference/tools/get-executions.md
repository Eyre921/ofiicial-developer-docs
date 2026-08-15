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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `tool_id` (string, required) — ID of the requested tool.

### Query parameters

- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `is_error` (boolean, optional, nullable) — Filter by error status. If not provided, returns all executions.
- `agent_id` (string, optional, nullable) — Filter by agent ID.
- `branch_id` (string, optional, nullable) — Filter by agent branch ID.
- `start_time` (double, optional, nullable) — Filter executions from this Unix timestamp (inclusive).
- `end_time` (double, optional, nullable) — Filter executions until this Unix timestamp (inclusive).

## Response

### 200

Successful Response

- `executions` (list of object, required)
  - `tool_id` (string, required) — The ID of the tool that was executed
  - `tool_request_id` (string, required) — The request/call ID associated with this tool execution
  - `conversation_id` (string, required) — The ID of the conversation where the tool was executed
  - `agent_id` (string, required) — The ID of the agent that ran the tool
  - `timestamp` (double, required) — Unix timestamp when the tool was executed
  - `latency_secs` (double, required) — How long the tool execution took
  - `id` (string, required)
  - `branch_id` (string, optional, nullable) — The branch ID if the agent has branches
  - `is_error` (boolean, optional, default: false) — Whether the tool execution failed
  - `request_payload` (string, optional, nullable) — LLM-extracted parameters sent to the tool (JSON string)
  - `response_payload` (string, optional, nullable) — Response returned by the tool
  - `error_message` (string, optional, nullable) — Error message if the tool execution failed
  - `error_type` (string, optional, nullable) — Error category (internal, customer_config, customer_auth, external_server, external_client, client_timeout, unknown)
  - `tool_call_details` (object, optional, nullable)
    - `type`: `api_integration_webhook` (ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetails)
      - `credential_id` (string, required, default: )
      - `integration_connection_id` (string, required, default: )
      - `integration_id` (string, required, default: )
      - `webhook_details` (object, required)
        - `method` (string, required)
        - `url` (string, required)
        - `headers` (map from string to string, optional)
        - `path_params` (map from string to string, optional)
        - `query_params` (map from string to string, optional)
        - `body` (string, optional, nullable)
    - `type`: `client` (ConversationHistoryTranscriptToolCallClientDetails)
      - `parameters` (string, required)
    - `type`: `mcp` (ConversationHistoryTranscriptToolCallMCPDetails)
      - `approval_policy` (string, required)
      - `integration_type` (string, required)
      - `mcp_server_id` (string, required)
      - `mcp_server_name` (string, required)
      - `mcp_tool_description` (string, optional, default: )
      - `mcp_tool_name` (string, optional, default: )
      - `parameters` (map from string to string, optional)
      - `requires_approval` (boolean, optional, default: false)
    - `type`: `webhook` (ConversationHistoryTranscriptToolCallWebhookDetails)
      - `method` (string, required)
      - `url` (string, required)
      - `body` (string, optional, nullable)
      - `headers` (map from string to string, optional)
      - `path_params` (map from string to string, optional)
      - `query_params` (map from string to string, optional)
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

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
