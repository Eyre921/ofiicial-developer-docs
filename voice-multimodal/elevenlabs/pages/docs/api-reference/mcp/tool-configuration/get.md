---
title: "Get configuration override"
source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/get.md
path: docs/api-reference/mcp/tool-configuration/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get configuration override

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}

Retrieve configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `mcp_server_id` (string, required) — ID of the MCP Server.
- `tool_name` (string, required) — Name of the MCP tool to retrieve config overrides for.

## Response

### 200

Successful Response

- `tool_name` (string, required) — The name of the MCP tool
- `pre_tool_speech` (enum, optional, nullable, default: auto) — If set, overrides the server's pre_tool_speech setting for this tool.
  - Allowed values: `auto`, `force`, `off`
- `interruption_mode` (enum, optional, nullable, default: allow) — If set, overrides the server's interruption_mode setting for this tool.
  - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
- `tool_call_sound` (enum or "off", optional, nullable) — Overrides the server's tool_call_sound setting for this tool. A sound name plays that sound; 'off' overrides to no sound (silence); null means do not override (inherit the server default).
- `tool_call_sound_behavior` (enum, optional, nullable, default: auto) — If set, overrides the server's tool_call_sound_behavior setting for this tool
  - Allowed values: `auto`, `always`
- `execution_mode` (enum, optional, nullable, default: immediate) — If set, overrides the server's execution_mode setting for this tool
  - Allowed values: `immediate`, `post_tool_speech`, `async`
- `response_timeout_secs` (integer, optional, nullable) — If set, overrides the server's response timeout for this MCP tool (seconds).
- `assignments` (list of object, optional) — Dynamic variable assignments for this MCP tool
  - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
  - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
  - `source` ("response", optional, default: response) — The source to extract the value from. Currently only 'response' is supported.
  - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
  - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
- `input_overrides` (map from string to object, optional, nullable) — Mapping of json path to input override configuration
  - `source`: `constant` (ConstantSchemaOverride)
    - `constant_value` (string or integer or double or boolean or list of any or map from string to any, required, nullable) — The constant value to use
  - `source`: `dynamic_variable` (DynamicVariableSchemaOverride)
    - `dynamic_variable` (string, required) — The name of the dynamic variable to use
  - `source`: `llm` (LLMSchemaOverride)
    - `prompt` (string, optional, nullable) — Prompt override for the LLM. If not provided, the original schema description is used.
  - `source`: `omit` (OmitSchemaOverride)
- `response_mocks` (list of object, optional, nullable) — Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.
  - `mock_result` (string, required) — The return value the LLM sees when this mock is active.
  - `parameter_conditions` (list of object, optional) — If the list is empty, the mock will always activate.
    - `eval` (object, required)
      - `type`: `anything` (MatchAnythingParameterEvaluationStrategy)
      - `type`: `exact` (ExactParameterEvaluationStrategy)
        - `expected_value` (string, required) — The exact string value that the parameter must match.
      - `type`: `llm` (LLMParameterEvaluationStrategy)
        - `description` (string, required) — A description of the evaluation strategy to use for the test.
      - `type`: `regex` (RegexParameterEvaluationStrategy)
        - `pattern` (string, required) — A regex pattern to match the agent's response against.
    - `path` (string, required)
  - `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.
- `force_pre_tool_speech` (boolean, optional, nullable, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If set, overrides the server's force_pre_tool_speech setting for this tool.
- `disable_interruptions` (boolean, optional, nullable, deprecated) — DEPRECATED: use `interruption_mode` instead. If set, overrides the server's disable_interruptions setting for this tool.

## Examples

**Response**

```json
{
  "tool_name": "string",
  "pre_tool_speech": "auto",
  "interruption_mode": "allow",
  "tool_call_sound": "typing",
  "tool_call_sound_behavior": "auto",
  "execution_mode": "immediate",
  "response_timeout_secs": 1,
  "assignments": [
    {
      "dynamic_variable": "string",
      "value_path": "string",
      "source": "response",
      "sanitize": false,
      "preserve_native_type": false
    }
  ],
  "input_overrides": {},
  "response_mocks": [
    {
      "mock_result": "string",
      "parameter_conditions": [
        {
          "eval": {
            "description": "string",
            "type": "string"
          },
          "path": "string"
        }
      ],
      "is_error": false
    }
  ],
  "force_pre_tool_speech": true,
  "disable_interruptions": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.toolConfigs.get("mcp_server_id", "tool_name");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tool_configs.get(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name",
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name"

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")! as URL,
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
