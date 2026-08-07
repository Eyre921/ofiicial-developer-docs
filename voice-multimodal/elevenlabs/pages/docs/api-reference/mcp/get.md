---
title: "Get MCP server"
source: https://elevenlabs.io/docs/api-reference/mcp/get.md
path: docs/api-reference/mcp/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get MCP server

GET https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}

Retrieve a specific MCP server configuration from the workspace.

Reference: https://elevenlabs.io/docs/api-reference/mcp/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `mcp_server_id` (string, required) — ID of the MCP Server.

## Response

### 200

Successful Response

- `id` (string, required)
- `config` (object, required)
  - `url` (string or object, required) — The URL of the MCP server, if this contains a secret please store as a workspace secret, otherwise store as a plain string. Must use https
    - ConvAISecretLocator
      - `secret_id` (string, required)
  - `name` (string, required)
  - `approval_policy` (enum, optional, default: require_approval_all) — Defines the MCP server-level approval policy for tool execution.
    - Allowed values: `auto_approve_all`, `require_approval_all`, `require_approval_per_tool`
  - `tool_approval_hashes` (list of object, optional) — List of tool approval hashes for per-tool approval when approval_policy is REQUIRE_APPROVAL_PER_TOOL
    - `tool_name` (string, required) — The name of the MCP tool
    - `tool_hash` (string, required) — SHA256 hash of the tool's parameters and description
    - `approval_policy` (enum, optional, default: requires_approval) — The approval policy for this tool
      - Allowed values: `auto_approved`, `requires_approval`
  - `transport` (enum, optional, default: SSE) — The transport type used to connect to the MCP server
    - Allowed values: `SSE`, `STREAMABLE_HTTP`
  - `secret_token` (object or object, optional, nullable) — The secret token (Authorization header) stored as a workspace secret or in-place secret
    - ConvAISecretLocator
      - `secret_id` (string, required)
    - ConvAIUserSecretDBModel
      - `name` (string, required)
      - `encrypted_value` (string, required)
      - `nonce` (string, required)
      - `id` (string, required)
  - `request_headers` (map from string to string or object or object or object, optional) — The headers included in the request
    - ConvAISecretLocator
      - `secret_id` (string, required)
    - ConvAIDynamicVariable
      - `variable_name` (string, required)
    - ConvAIEnvVarLocator
      - `env_var_label` (string, required)
  - `request_meta` (map from string to string or integer or double or boolean or object or object or object, optional) — Entries sent in the MCP `_meta` field of tools/call requests. Values may be JSON scalars, or references to a workspace secret, dynamic variable, or environment variable resolved per call.
    - ConvAISecretLocator
      - `secret_id` (string, required)
    - ConvAIDynamicVariable
      - `variable_name` (string, required)
    - ConvAIEnvVarLocator
      - `env_var_label` (string, required)
  - `auth_connection` (object or object, optional, nullable) — Optional auth connection to use for authentication with this MCP server
    - AuthConnectionLocator
      - `auth_connection_id` (string, required)
    - EnvironmentAuthConnectionLocator
      - `env_var_label` (string, required)
  - `description` (string, optional, default: )
  - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency. Applies to every tool from this MCP server unless overridden per tool.
    - Allowed values: `auto`, `force`, `off`
  - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it. Applies to every tool from this MCP server unless overridden per tool.
    - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
  - `tool_call_sound` (enum, optional, nullable) — Predefined tool call sound type to play during tool execution for all tools from this MCP server
    - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
  - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play for all tools from this MCP server
    - Allowed values: `auto`, `always`
  - `execution_mode` (enum, optional, default: immediate) — Determines when and how all tools from this MCP server execute: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
    - Allowed values: `immediate`, `post_tool_speech`, `async`
  - `response_timeout_secs` (integer, optional, default: 30) — The maximum time in seconds to wait for each MCP tool call to complete. Must be between 5 and 300 seconds (inclusive).
  - `tool_config_overrides` (list of object, optional) — List of per-tool configuration overrides that override the server-level defaults for specific tools
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
        - `constant_value` (string or integer or double or boolean or list of any or map from string to any, required) — The constant value to use
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
  - `disable_compression` (boolean, optional, default: false) — Whether to disable HTTP compression for this MCP server. Enable this if the server does not support compressed responses.
  - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, all tools from this MCP server will require pre-tool execution speech.
  - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while any tool from this MCP server is running.
- `metadata` (object, required) — The metadata of the MCP Server
  - `created_at` (integer, required)
  - `owner_user_id` (string, optional, nullable)
- `access_info` (object, optional, nullable) — The access information of the MCP Server
  - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
  - `creator_name` (string, required) — Name of the agent's creator
  - `creator_email` (string, required) — Email of the agent's creator
  - `role` (enum, required) — The role of the user making the request
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
    - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
- `dependent_agents` (list of object, optional) — List of agents that depend on this MCP Server.
  - `type`: `available` (DependentAvailableAgentIdentifier)
    - `access_level` (enum, required)
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `created_at_unix_secs` (integer, required)
    - `id` (string, required)
    - `name` (string, required)
    - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
  - `type`: `unknown` (DependentUnknownAgentIdentifier)
    - `id` (string, required)
    - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.

## Examples

**Response**

```json
{
  "id": "string",
  "config": {
    "url": "string",
    "name": "string",
    "approval_policy": "require_approval_all",
    "tool_approval_hashes": [
      {
        "tool_name": "string",
        "tool_hash": "string",
        "approval_policy": "requires_approval"
      }
    ],
    "transport": "SSE",
    "secret_token": {
      "secret_id": "string"
    },
    "request_headers": {},
    "request_meta": {},
    "auth_connection": {
      "auth_connection_id": "string"
    },
    "description": "",
    "pre_tool_speech": "auto",
    "interruption_mode": "allow",
    "tool_call_sound": "typing",
    "tool_call_sound_behavior": "auto",
    "execution_mode": "immediate",
    "response_timeout_secs": 30,
    "tool_config_overrides": [
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
    ],
    "disable_compression": false,
    "force_pre_tool_speech": false,
    "disable_interruptions": false
  },
  "metadata": {
    "created_at": 1,
    "owner_user_id": "string"
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "access_source": "creator"
  },
  "dependent_agents": [
    {
      "type": "available",
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "string",
      "name": "string",
      "referenced_resource_ids": [
        "string"
      ]
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.get("mcp_server_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.get(
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id")! as URL,
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
