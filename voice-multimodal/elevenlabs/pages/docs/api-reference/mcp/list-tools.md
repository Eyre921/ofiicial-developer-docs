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
- `tools` (list of object, required) — A list of tools available on the MCP server.
  - `name` (string, required)
  - `inputSchema` (map from string to any, required)
  - `title` (string, optional, nullable)
  - `description` (string, optional, nullable)
  - `outputSchema` (map from string to any, optional, nullable)
  - `icons` (list of object, optional, nullable)
    - `src` (string, required)
    - `mimeType` (string, optional, nullable)
    - `sizes` (list of string, optional, nullable)
  - `annotations` (object, optional, nullable) — Additional properties describing a Tool to clients. NOTE: all properties in ToolAnnotations are **hints**. They are not guaranteed to provide a faithful description of tool behavior (including descriptive properties like `title`). Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers.
    - `title` (string, optional, nullable)
    - `readOnlyHint` (boolean, optional, nullable)
    - `destructiveHint` (boolean, optional, nullable)
    - `idempotentHint` (boolean, optional, nullable)
    - `openWorldHint` (boolean, optional, nullable)
  - `_meta` (map from string to any, optional, nullable)
  - `execution` (object, optional, nullable) — Execution-related properties for a tool.
    - `taskSupport` (enum, optional, nullable)
      - Allowed values: `forbidden`, `optional`, `required`
- `error_message` (string, optional, nullable) — Error message if the operation was not successful.

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
  ]
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
