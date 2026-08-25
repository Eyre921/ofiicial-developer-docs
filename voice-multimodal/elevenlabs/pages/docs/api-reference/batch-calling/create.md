---
title: "Submit batch calling job"
source: https://elevenlabs.io/docs/api-reference/batch-calling/create.md
path: docs/api-reference/batch-calling/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Submit batch calling job

POST https://api.elevenlabs.io/v1/convai/batch-calling/submit
Content-Type: application/json

Submit a batch call request to schedule calls for multiple recipients.

Reference: https://elevenlabs.io/docs/api-reference/batch-calling/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `call_name` (string, required)
- `agent_id` (string, required)
- `recipients` (list of object, required)
  - `id` (string, optional, nullable)
  - `phone_number` (string, optional, nullable)
  - `whatsapp_user_id` (string, optional, nullable)
  - `conversation_initiation_client_data` (object, optional, nullable)
    - `conversation_config_override` (object, optional)
      - `asr` (object, optional, nullable) — Configuration for conversational transcription
        - `keywords` (list of string, optional, nullable) — Keywords to boost prediction probability for
      - `turn` (object, optional, nullable) — Configuration for turn detection
        - `soft_timeout_config` (object, optional, nullable) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
          - `message` (string, optional, nullable) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
          - `additional_soft_timeout_messages` (list of string, optional, nullable) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
      - `tts` (object, optional, nullable) — Configuration for conversational text to speech
        - `model_id` (enum, optional, nullable, default: eleven_flash_v2) — The model to use for TTS
          - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
        - `voice_id` (string, optional, nullable) — The voice ID to use for TTS
        - `supported_voices` (list of object, optional, nullable) — Additional supported voices for the agent
          - `label` (string, required)
          - `voice_id` (string, required)
          - `description` (string, optional, nullable)
          - `language` (string, optional, nullable)
          - `model_family` (enum, optional, nullable)
            - Allowed values: `turbo`, `flash`, `multilingual`, `v3_conversational`
          - `optimize_streaming_latency` (enum, optional, nullable)
            - Allowed values: `0`, `1`, `2`, `3`, `4`
          - `stability` (double, optional, nullable)
          - `speed` (double, optional, nullable)
          - `similarity_boost` (double, optional, nullable)
        - `stability` (double, optional, nullable) — The stability of generated speech
        - `speed` (double, optional, nullable) — The speed of generated speech
        - `similarity_boost` (double, optional, nullable) — The similarity boost for generated speech
        - `pronunciation_dictionary_locators` (list of object, optional, nullable) — The pronunciation dictionary locators
          - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
          - `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary
      - `conversation` (object, optional, nullable) — Configuration for conversational events
        - `text_only` (boolean, optional, nullable) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
        - `max_duration_seconds` (integer, optional, nullable) — The maximum duration of a conversation in seconds
      - `agent` (object, optional, nullable) — Agent specific configuration
        - `first_message` (string, optional, nullable) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
        - `language` (string, optional, nullable) — Language of the agent - used for ASR and TTS
        - `max_conversation_duration_message` (string, optional, nullable) — If non-empty, the message the agent will send when max conversation duration is reached.
        - `prompt` (object, optional, nullable) — The prompt for the agent
          - `prompt` (string, optional, nullable) — The prompt for the agent
          - `llm` (enum, optional, nullable) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
            - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
          - `tool_ids` (list of string, optional, nullable) — A list of IDs of tools used by the agent
          - `native_mcp_server_ids` (list of string, optional, nullable) — A list of Native MCP server ids to be used by the agent
          - `knowledge_base` (list of object, optional, nullable) — A list of knowledge bases to be used by the agent
            - `type` (enum, required) — The type of the knowledge base
            - `name` (string, required) — The name of the knowledge base
            - `id` (string, required) — The ID of the knowledge base
            - `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
    - `custom_llm_extra_body` (map from string to any, optional)
    - `user_id` (string, optional, nullable) — ID of the end user participating in this conversation (for agent owner's user identification)
    - `source_info` (object, optional) — Information about the source of conversation initiation
      - `source` (enum, optional, nullable, default: unknown) — Source of the conversation initiation
        - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
      - `version` (string, optional, nullable) — The SDK version number
    - `branch_id` (string, optional, nullable) — ID of the agent branch to use for this conversation
    - `environment` (string, optional, nullable) — Environment to use for resolving environment variables
    - `starting_workflow_node_id` (string, optional, nullable) — If set, start the workflow at this node id instead of the default entry
    - `procedure_ids` (list of string, optional, nullable) — If set, only these procedures are available to the starting agent. Each ID must be attached to that agent; unknown IDs fail conversation start. An empty list disables all of that agent's procedures. Not applied after an agent transfer. Requires enable_procedure_ids_from_client.
    - `dynamic_variables` (map from string to any, optional)
- `scheduled_time_unix` (integer, optional, nullable)
- `agent_phone_number_id` (string, optional, nullable)
- `whatsapp_params` (object, optional, nullable)
  - `whatsapp_call_permission_request_template_name` (string, required)
  - `whatsapp_call_permission_request_template_language_code` (string, required)
  - `whatsapp_phone_number_id` (string, optional, nullable)
- `timezone` (string, optional, nullable)
- `branch_id` (string, optional, nullable)
- `environment` (string, optional, nullable)
- `telephony_call_config` (object, optional)
  - `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
  - `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `target_concurrency_limit` (integer, optional, nullable) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.

## Response

### 200

Successful Response

- `id` (string, required)
- `phone_number_id` (string, required, nullable)
- `phone_provider` (enum, required, nullable)
  - Allowed values: `twilio`, `sip_trunk`, `exotel`
- `whatsapp_params` (object, required, nullable)
  - `whatsapp_call_permission_request_template_name` (string, required)
  - `whatsapp_call_permission_request_template_language_code` (string, required)
  - `whatsapp_phone_number_id` (string, optional, nullable)
- `name` (string, required)
- `agent_id` (string, required)
- `branch_id` (string, required, nullable)
- `environment` (string, required, nullable)
- `created_at_unix` (integer, required)
- `scheduled_time_unix` (integer, required)
- `timezone` (string, required, nullable)
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
- `target_concurrency_limit` (integer, required, nullable) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
- `agent_name` (string, required)
- `branch_name` (string, required, nullable)

## Examples

**Request**

```json
{
  "call_name": "string",
  "agent_id": "string",
  "recipients": [
    {}
  ]
}
```

**Response**

```json
{
  "id": "string",
  "phone_number_id": "string",
  "phone_provider": "twilio",
  "whatsapp_params": {
    "whatsapp_call_permission_request_template_name": "string",
    "whatsapp_call_permission_request_template_language_code": "string",
    "whatsapp_phone_number_id": "string"
  },
  "name": "string",
  "agent_id": "string",
  "branch_id": "string",
  "environment": "string",
  "created_at_unix": 1,
  "scheduled_time_unix": 1,
  "timezone": "string",
  "total_calls_dispatched": 0,
  "total_calls_scheduled": 0,
  "total_calls_finished": 0,
  "last_updated_at_unix": 1,
  "status": "pending",
  "retry_count": 0,
  "telephony_call_config": {
    "ringing_timeout_secs": 60,
    "twilio_call_recording_enabled": false
  },
  "target_concurrency_limit": 1,
  "agent_name": "string",
  "branch_name": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.create({
        callName: "string",
        agentId: "string",
        recipients: [
            {},
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, OutboundCallRecipient

client = ElevenLabs()

client.conversational_ai.batch_calls.create(
    call_name="string",
    agent_id="string",
    recipients=[
        OutboundCallRecipient()
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/submit"

	payload := strings.NewReader("{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/submit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/batch-calling/submit")
  .header("Content-Type", "application/json")
  .body("{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/batch-calling/submit', [
  'body' => '{
  "call_name": "string",
  "agent_id": "string",
  "recipients": [
    {}
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/submit");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "call_name": "string",
  "agent_id": "string",
  "recipients": [[]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/submit")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
