---
title: "Get batch call information"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get.md
path: docs/eleven-agents/api-reference/batch-calling/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get batch call information

GET https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}

Get detailed information about a batch call including all recipients.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `batch_id` (string, required)

## Response

### 200

Successful Response

- `id` (string, required)
- `name` (string, required)
- `agent_id` (string, required)
- `created_at_unix` (integer, required)
- `scheduled_time_unix` (integer, required)
- `total_calls_dispatched` (integer, required, default: 0)
- `total_calls_scheduled` (integer, required, default: 0)
- `total_calls_finished` (integer, required, default: 0)
- `last_updated_at_unix` (integer, required)
- `status` (enum, required)
  - Allowed values: `pending`, `in_progress`, `completed`, `failed`, `cancelled`
- `retry_count` (integer, required, default: 0)
- `telephony_call_config` (object, required)
  - `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
  - `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `agent_name` (string, required)
- `recipients` (list of object, required)
  - `id` (string, required)
  - `status` (enum, required)
    - Allowed values: `pending`, `dispatched`, `initiated`, `in_progress`, `completed`, `failed`, `cancelled`, `voicemail`
  - `created_at_unix` (integer, required)
  - `updated_at_unix` (integer, required)
  - `phone_number` (string, optional)
  - `whatsapp_user_id` (string, optional)
  - `conversation_id` (string, optional)
  - `conversation_initiation_client_data` (object, optional)
    - `conversation_config_override` (object, optional)
      - `asr` (object, optional) — Configuration for conversational transcription
        - `keywords` (list of string, optional) — Keywords to boost prediction probability for
      - `turn` (object, optional) — Configuration for turn detection
        - `soft_timeout_config` (object, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
          - `message` (string, optional) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
          - `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
      - `tts` (object, optional) — Configuration for conversational text to speech
        - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
          - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
        - `voice_id` (string, optional) — The voice ID to use for TTS
        - `supported_voices` (list of object, optional) — Additional supported voices for the agent
          - `label` (string, required)
          - `voice_id` (string, required)
          - `description` (string, optional)
          - `language` (string, optional)
          - `model_family` (enum, optional)
            - Allowed values: `turbo`, `flash`, `multilingual`, `v3_conversational`
          - `optimize_streaming_latency` (integer, optional)
          - `stability` (double, optional)
          - `speed` (double, optional)
          - `similarity_boost` (double, optional)
        - `stability` (double, optional) — The stability of generated speech
        - `speed` (double, optional) — The speed of generated speech
        - `similarity_boost` (double, optional) — The similarity boost for generated speech
        - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
          - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
          - `version_id` (string, optional) — The ID of the version of the pronunciation dictionary
      - `conversation` (object, optional) — Configuration for conversational events
        - `text_only` (boolean, optional) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
        - `max_duration_seconds` (integer, optional) — The maximum duration of a conversation in seconds
      - `agent` (object, optional) — Agent specific configuration
        - `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
        - `language` (string, optional) — Language of the agent - used for ASR and TTS
        - `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
        - `prompt` (object, optional) — The prompt for the agent
          - `prompt` (string, optional) — The prompt for the agent
          - `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
            - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
          - `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
          - `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
          - `knowledge_base` (list of object, optional) — A list of knowledge bases to be used by the agent
            - `type` (enum, required) — The type of the knowledge base
            - `name` (string, required) — The name of the knowledge base
            - `id` (string, required) — The ID of the knowledge base
            - `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
    - `custom_llm_extra_body` (map from string to any, optional)
    - `user_id` (string, optional) — ID of the end user participating in this conversation (for agent owner's user identification)
    - `source_info` (object, optional) — Information about the source of conversation initiation
      - `source` (enum, optional, default: unknown) — Source of the conversation initiation
        - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
      - `version` (string, optional) — The SDK version number
    - `branch_id` (string, optional) — ID of the agent branch to use for this conversation
    - `environment` (string, optional) — Environment to use for resolving environment variables
    - `starting_workflow_node_id` (string, optional) — If set, start the workflow at this node id instead of the default entry
    - `procedure_ids` (list of string, optional) — If set, only these procedures are available to the starting agent. Each ID must be attached to that agent; unknown IDs fail conversation start. An empty list disables all of that agent's procedures. Not applied after an agent transfer. Requires enable_procedure_ids_from_client.
    - `dynamic_variables` (map from string to any, optional)
    - `tool_mock_config` (object, optional) — Configuration for which tools to mock and fallback behavior
      - `mocking_strategy` (enum, optional, default: none) — Which tools to mock: 'all' mocks every mockable tool, 'selected' mocks only those in mocked_tool_names/mocked_tool_ids, 'none' disables mocking.
        - Allowed values: `all`, `selected`, `none`
      - `fallback_strategy` (enum, optional, default: raise_error) — Behavior when no mock matches a tool call.
        - Allowed values: `call_real_tool`, `raise_error`
      - `mocked_tool_names` (list of string, optional) — Tool names to mock. Only used when mocking_strategy is 'selected'.
    - `tool_mock_overrides` (map from string to list of object, optional) — Per-tool response mock overrides keyed by resolved tool name, applied ahead of the tool's shared mocks. Used for test-specific mocks.
      - `mock_result` (string, required) — The return value the LLM sees when this mock is active.
      - `parameter_conditions` (list of object, optional) — If the list is empty, the mock will always activate.
        - `eval` (object, required)
          - `type`: `anything`
          - `type`: `exact`
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm`
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex`
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.
- `phone_number_id` (string, optional)
- `phone_provider` (enum, optional)
  - Allowed values: `twilio`, `sip_trunk`, `exotel`
- `whatsapp_params` (object, optional)
  - `whatsapp_call_permission_request_template_name` (string, required)
  - `whatsapp_call_permission_request_template_language_code` (string, required)
  - `whatsapp_phone_number_id` (string, optional)
- `branch_id` (string, optional)
- `environment` (string, optional)
- `timezone` (string, optional)
- `target_concurrency_limit` (integer, optional) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
- `branch_name` (string, optional)

## Examples

**Response**

```json
{
  "id": "id",
  "name": "name",
  "agent_id": "agent_id",
  "created_at_unix": 1,
  "scheduled_time_unix": 1,
  "total_calls_dispatched": 1,
  "total_calls_scheduled": 1,
  "total_calls_finished": 1,
  "last_updated_at_unix": 1,
  "status": "pending",
  "retry_count": 1,
  "telephony_call_config": {
    "ringing_timeout_secs": 1,
    "twilio_call_recording_enabled": true
  },
  "agent_name": "agent_name",
  "recipients": [
    {
      "id": "id",
      "status": "pending",
      "created_at_unix": 1,
      "updated_at_unix": 1,
      "phone_number": "phone_number",
      "whatsapp_user_id": "whatsapp_user_id",
      "conversation_id": "conversation_id",
      "conversation_initiation_client_data": {
        "conversation_config_override": {
          "asr": {
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "soft_timeout_config": {
              "message": "Hhmmmm...yeah."
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "stability": 0.5,
            "speed": 1,
            "similarity_boost": 0.8,
            "pronunciation_dictionary_locators": [
              {
                "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                "version_id": null
              }
            ]
          },
          "conversation": {
            "max_duration_seconds": 600
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "tool_ids": [
                "tool_ids"
              ],
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ]
            }
          }
        }
      }
    }
  ],
  "phone_number_id": "phone_number_id",
  "phone_provider": "twilio",
  "whatsapp_params": {
    "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
    "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
    "whatsapp_phone_number_id": "whatsapp_phone_number_id"
  },
  "branch_id": "branch_id",
  "environment": "environment",
  "timezone": "timezone",
  "target_concurrency_limit": 1,
  "branch_name": "branch_name"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.get("batch_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.get(
    batch_id="batch_id",
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")! as URL,
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
