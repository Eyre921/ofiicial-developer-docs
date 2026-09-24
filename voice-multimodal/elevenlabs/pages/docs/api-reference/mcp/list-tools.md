---
title: "List MCP server tools"
source: https://elevenlabs.io/docs/api-reference/mcp/list-tools.md
path: docs/api-reference/mcp/list-tools
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List MCP server tools

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tools

Retrieve all tools available for a specific MCP server configuration.

Reference: https://elevenlabs.io/docs/api-reference/mcp/list-tools

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `mcp_server_id` (string, required) — ID of the MCP Server.

### Query parameters

- `environment` (string, optional, default: production) — Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

## Response

### 200

Successful Response

- `success` (boolean, required) — Indicates if the operation was successful.
- `tools` (list of Tool, required) — A list of tools available on the MCP server.
- `tool_approval_statuses` (list of MCPToolApprovalStatus, optional) — Derived approval states for currently discovered tools. Populated only for persisted MCP servers using per-tool approval; otherwise empty.
- `error_message` (string, optional, nullable) — Error message if the operation was not successful.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### Tool

Definition for a tool the client can call.

- `name` (string, required)
- `inputSchema` (map from string to any, required)
- `title` (string, optional, nullable)
- `description` (string, optional, nullable)
- `execution` (ToolExecution, optional, nullable) — Execution-related properties for a tool (2025-11-25 only).
- `outputSchema` (map from string to any, optional, nullable)
- `icons` (list of Icon, optional, nullable)
- `annotations` (ToolAnnotations, optional, nullable) — Additional properties describing a Tool to clients. NOTE: all properties in ToolAnnotations are **hints**. They are not guaranteed to provide a faithful description of tool behavior (including descriptive properties like `title`). Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers.
- `_meta` (map from string to any, optional, nullable)

### MCPToolApprovalStatus

Derived approval state for a currently discovered MCP tool.

- `tool_id` (string, required) — Canonical MCP tool identifier in the form mcp:\<server\_id>:\<tool\_name>
- `state` (enum, required) — Whether a stored approval exists and still matches the live tool definition
  - Allowed values: `up_to_date`, `needs_review`, `not_approved`
- `approval_policy` (enum, optional, nullable, default: requires_approval) — Stored execution policy. Set when the tool has an approval.
  - Allowed values: `auto_approved`, `requires_approval`
- `approved_definition` (MCPApprovedToolDefinition, optional, nullable) — Previously approved definition, included when the tool needs review and a snapshot exists.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ToolExecution

Execution-related properties for a tool (2025-11-25 only).

- `taskSupport` (enum, optional, nullable)
  - Allowed values: `forbidden`, `optional`, `required`

### Icon

An optionally-sized icon for display in a user interface (2025-11-25+).

- `src` (string, required)
- `mimeType` (string, optional, nullable)
- `sizes` (list of string, optional, nullable)
- `theme` (enum, optional, nullable)
  - Allowed values: `light`, `dark`

### ToolAnnotations

Additional properties describing a Tool to clients. NOTE: all properties in ToolAnnotations are **hints**. They are not guaranteed to provide a faithful description of tool behavior (including descriptive properties like `title`). Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers.

- `title` (string, optional, nullable)
- `readOnlyHint` (boolean, optional, nullable)
- `destructiveHint` (boolean, optional, nullable)
- `idempotentHint` (boolean, optional, nullable)
- `openWorldHint` (boolean, optional, nullable)

### MCPApprovedToolDefinition

Snapshot of the MCP tool definition that was approved.

- `description` (string, optional, default: ) — The MCP server-provided tool description at approval time
- `input_schema` (map from string to any, optional) — The MCP server-provided JSON input schema at approval time

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "success": true,
  "tools": [
    {
      "name": "weather_by_zapier_get_current",
      "inputSchema": {
        "properties": {
          "latitude": {
            "description": "Latitude",
            "type": "string"
          },
          "longitude": {
            "description": "Longitude",
            "type": "string"
          }
        },
        "required": [
          "latitude",
          "longitude"
        ],
        "type": "object"
      },
      "description": "Gets current weather conditions for a location."
    },
    {
      "name": "tool2",
      "inputSchema": {
        "properties": {},
        "type": "object"
      },
      "description": "Description of tool2"
    }
  ],
  "tool_approval_statuses": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.tools.list("mcp_server_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tools.list(
    mcp_server_id="mcp_server_id",
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools"

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")! as URL,
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
