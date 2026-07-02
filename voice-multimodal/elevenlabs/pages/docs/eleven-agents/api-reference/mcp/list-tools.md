---
title: "List MCP server tools"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/list-tools.md
path: docs/eleven-agents/api-reference/mcp/list-tools
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List MCP server tools

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tools

Retrieve all tools available for a specific MCP server configuration.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/list-tools

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tools:
    get:
      operationId: list
      summary: List Mcp Server Tools
      description: Retrieve all tools available for a specific MCP server configuration.
      tags:
        - subpackage_conversationalAi/mcpServers/tools
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/type_:ListMcpToolsResponseModel'
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
    type_:Icon:
      type: object
      properties:
        src:
          type: string
        mimeType:
          type: string
        sizes:
          type: array
          items:
            type: string
      required:
        - src
      description: An icon for display in user interfaces.
      title: Icon
    type_:ToolAnnotations:
      type: object
      properties:
        title:
          type: string
        readOnlyHint:
          type: boolean
        destructiveHint:
          type: boolean
        idempotentHint:
          type: boolean
        openWorldHint:
          type: boolean
      description: |-
        Additional properties describing a Tool to clients.

        NOTE: all properties in ToolAnnotations are **hints**.
        They are not guaranteed to provide a faithful description of
        tool behavior (including descriptive properties like `title`).

        Clients should never make tool use decisions based on ToolAnnotations
        received from untrusted servers.
      title: ToolAnnotations
    type_:ToolExecutionTaskSupport:
      type: string
      enum:
        - forbidden
        - optional
        - required
      title: ToolExecutionTaskSupport
    type_:ToolExecution:
      type: object
      properties:
        taskSupport:
          $ref: '#/components/schemas/type_:ToolExecutionTaskSupport'
      description: Execution-related properties for a tool.
      title: ToolExecution
    type_:Tool:
      type: object
      properties:
        name:
          type: string
        title:
          type: string
        description:
          type: string
        inputSchema:
          type: object
          additionalProperties:
            description: Any type
        outputSchema:
          type: object
          additionalProperties:
            description: Any type
        icons:
          type: array
          items:
            $ref: '#/components/schemas/type_:Icon'
        annotations:
          $ref: '#/components/schemas/type_:ToolAnnotations'
        _meta:
          type: object
          additionalProperties:
            description: Any type
        execution:
          $ref: '#/components/schemas/type_:ToolExecution'
      required:
        - name
        - inputSchema
      description: Definition for a tool the client can call.
      title: Tool
    type_:ListMcpToolsResponseModel:
      type: object
      properties:
        success:
          type: boolean
          description: Indicates if the operation was successful.
        tools:
          type: array
          items:
            $ref: '#/components/schemas/type_:Tool'
          description: A list of tools available on the MCP server.
        error_message:
          type: string
          description: Error message if the operation was not successful.
      required:
        - success
        - tools
      description: Response model for testing tools available on an MCP server.
      title: ListMcpToolsResponseModel
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
      "title": "title",
      "description": "Gets current weather conditions for a location.",
      "outputSchema": {
        "key": "value"
      },
      "icons": [
        {
          "src": "src"
        }
      ],
      "_meta": {
        "key": "value"
      }
    },
    {
      "name": "tool2",
      "inputSchema": {
        "properties": {},
        "type": "object"
      },
      "title": "title",
      "description": "Description of tool2",
      "outputSchema": {
        "key": "value"
      },
      "icons": [
        {
          "src": "src"
        }
      ],
      "_meta": {
        "key": "value"
      }
    }
  ],
  "error_message": "error_message"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.tools.list("mcp_server_id");
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
