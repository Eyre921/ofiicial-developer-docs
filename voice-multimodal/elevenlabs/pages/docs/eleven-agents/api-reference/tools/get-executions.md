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

- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `is_error` (boolean, optional) — Filter by error status. If not provided, returns all executions.
- `agent_id` (string, optional) — Filter by agent ID.
- `branch_id` (string, optional) — Filter by agent branch ID.
- `start_time` (double, optional) — Filter executions from this Unix timestamp (inclusive).
- `end_time` (double, optional) — Filter executions until this Unix timestamp (inclusive).

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
  - `branch_id` (string, optional) — The branch ID if the agent has branches
  - `is_error` (boolean, optional, default: false) — Whether the tool execution failed
  - `request_payload` (string, optional) — LLM-extracted parameters sent to the tool (JSON string)
  - `response_payload` (string, optional) — Response returned by the tool
  - `error_message` (string, optional) — Error message if the tool execution failed
  - `error_type` (string, optional) — Error category (internal, customer_config, customer_auth, external_server, external_client, client_timeout, unknown)
  - `tool_call_details` (object, optional)
    - `type`: `api_integration_webhook`
      - `credential_id` (string, required, default: )
      - `integration_connection_id` (string, required, default: )
      - `integration_id` (string, required, default: )
      - `webhook_details` (object, required)
        - `method` (string, required)
        - `url` (string, required)
        - `type` ("webhook", optional)
        - `headers` (map from string to string, optional)
        - `path_params` (map from string to string, optional)
        - `query_params` (map from string to string, optional)
        - `body` (string, optional)
    - `type`: `client`
      - `parameters` (string, required)
    - `type`: `mcp`
      - `approval_policy` (string, required)
      - `integration_type` (string, required)
      - `mcp_server_id` (string, required)
      - `mcp_server_name` (string, required)
      - `mcp_tool_description` (string, optional, default: )
      - `mcp_tool_name` (string, optional, default: )
      - `parameters` (map from string to string, optional)
      - `requires_approval` (boolean, optional, default: false)
    - `type`: `webhook`
      - `method` (string, required)
      - `url` (string, required)
      - `body` (string, optional)
      - `headers` (map from string to string, optional)
      - `path_params` (map from string to string, optional)
      - `query_params` (map from string to string, optional)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

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
