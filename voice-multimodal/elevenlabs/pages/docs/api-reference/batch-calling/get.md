---
title: "Get batch call information"
source: https://elevenlabs.io/docs/api-reference/batch-calling/get.md
path: docs/api-reference/batch-calling/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get batch call information

GET https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}

Get detailed information about a batch call including all recipients.

Reference: https://elevenlabs.io/docs/api-reference/batch-calling/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/batch-calling/{batch_id}:
    get:
      operationId: get
      summary: Get A Batch Call By Id.
      description: Get detailed information about a batch call including all recipients.
      tags:
        - batchCalls
      parameters:
        - name: batch_id
          in: path
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
                $ref: '#/components/schemas/BatchCallDetailedResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    TelephonyProvider:
      type: string
      enum:
        - twilio
        - sip_trunk
        - exotel
      title: TelephonyProvider
    BatchCallWhatsAppParams:
      type: object
      properties:
        whatsapp_phone_number_id:
          type:
            - string
            - 'null'
        whatsapp_call_permission_request_template_name:
          type: string
        whatsapp_call_permission_request_template_language_code:
          type: string
      required:
        - whatsapp_call_permission_request_template_name
        - whatsapp_call_permission_request_template_language_code
      title: BatchCallWhatsAppParams
    BatchCallStatus:
      type: string
      enum:
        - pending
        - in_progress
        - completed
        - failed
        - cancelled
      title: BatchCallStatus
    TelephonyCallConfig:
      type: object
      properties:
        ringing_timeout_secs:
          type: integer
          default: 60
          description: >-
            How long to ring the recipient before giving up, in seconds. Note
            that this will also be limited by the provider's own constraints.
      title: TelephonyCallConfig
    BatchCallRecipientStatus:
      type: string
      enum:
        - pending
        - dispatched
        - initiated
        - in_progress
        - completed
        - failed
        - cancelled
        - voicemail
      title: BatchCallRecipientStatus
    ASRConversationalConfigOverride:
      type: object
      properties:
        keywords:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: ASRConversationalConfigOverride
    SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type:
            - string
            - 'null'
          description: >-
            Message to show when the first soft timeout is reached while waiting
            for LLM response. Supports dynamic variables (e.g.,
            {{system__time}}, {{custom_variable}}).
      title: SoftTimeoutConfigOverride
    TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigOverride'
            - type: 'null'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfigOverride
    TTSConversationalConfigOverride:
      type: object
      properties:
        voice_id:
          type:
            - string
            - 'null'
          description: The voice ID to use for TTS
        stability:
          type:
            - number
            - 'null'
          format: double
          description: The stability of generated speech
        speed:
          type:
            - number
            - 'null'
          format: double
          description: The speed of generated speech
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
          description: The similarity boost for generated speech
      title: TTSConversationalConfigOverride
    ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
      title: ConversationConfigOverride
    LLM:
      type: string
      enum:
        - gpt-4o-mini
        - gpt-4o
        - gpt-4
        - gpt-4-turbo
        - gpt-4.1
        - gpt-4.1-mini
        - gpt-4.1-nano
        - gpt-5
        - gpt-5.1
        - gpt-5.2
        - gpt-5.2-chat-latest
        - gpt-5.4
        - gpt-5.4-mini
        - gpt-5.4-nano
        - gpt-5.5
        - gpt-5-mini
        - gpt-5-nano
        - gpt-3.5-turbo
        - gemini-1.5-pro
        - gemini-1.5-flash
        - gemini-2.0-flash
        - gemini-2.0-flash-lite
        - gemini-2.5-flash-lite
        - gemini-2.5-flash
        - gemini-3-pro-preview
        - gemini-3-flash-preview
        - gemini-3.1-pro-preview
        - gemini-3.1-flash-lite-preview
        - gemini-3.1-flash-lite
        - gemini-3.5-flash
        - claude-sonnet-4-5
        - claude-opus-4-7
        - claude-sonnet-4-6
        - claude-sonnet-4
        - claude-haiku-4-5
        - claude-3-7-sonnet
        - claude-3-5-sonnet
        - claude-3-5-sonnet-v1
        - claude-3-haiku
        - grok-beta
        - custom-llm
        - qwen3-4b
        - qwen3-30b-a3b
        - qwen36-35b-a3b
        - qwen35-397b-a17b
        - gpt-oss-20b
        - gpt-oss-120b
        - glm-45-air-fp8
        - gemini-2.5-flash-preview-09-2025
        - gemini-2.5-flash-lite-preview-09-2025
        - gemini-2.5-flash-preview-05-20
        - gemini-2.5-flash-preview-04-17
        - gemini-2.5-flash-lite-preview-06-17
        - gemini-2.0-flash-lite-001
        - gemini-2.0-flash-001
        - gemini-1.5-flash-002
        - gemini-1.5-flash-001
        - gemini-1.5-pro-002
        - gemini-1.5-pro-001
        - claude-sonnet-4@20250514
        - claude-sonnet-4-5@20250929
        - claude-haiku-4-5@20251001
        - claude-3-7-sonnet@20250219
        - claude-3-5-sonnet@20240620
        - claude-3-5-sonnet-v2@20241022
        - claude-3-haiku@20240307
        - gpt-5-2025-08-07
        - gpt-5.1-2025-11-13
        - gpt-5.2-2025-12-11
        - gpt-5.4-2026-03-05
        - gpt-5.4-mini-2026-03-17
        - gpt-5.4-nano-2026-03-17
        - gpt-5.5-2026-04-23
        - gpt-5-mini-2025-08-07
        - gpt-5-nano-2025-08-07
        - gpt-4.1-2025-04-14
        - gpt-4.1-mini-2025-04-14
        - gpt-4.1-nano-2025-04-14
        - gpt-4o-mini-2024-07-18
        - gpt-4o-2024-11-20
        - gpt-4o-2024-08-06
        - gpt-4o-2024-05-13
        - gpt-4-0613
        - gpt-4-0314
        - gpt-4-turbo-2024-04-09
        - gpt-3.5-turbo-0125
        - gpt-3.5-turbo-1106
        - watt-tool-8b
        - watt-tool-70b
      default: gemini-2.5-flash
      title: LLM
    KnowledgeBaseDocumentType:
      type: string
      enum:
        - file
        - url
        - text
        - folder
      title: KnowledgeBaseDocumentType
    DocumentUsageModeEnum:
      type: string
      enum:
        - prompt
        - auto
      default: auto
      title: DocumentUsageModeEnum
    KnowledgeBaseLocator:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/KnowledgeBaseDocumentType'
          description: The type of the knowledge base
        name:
          type: string
          description: The name of the knowledge base
        id:
          type: string
          description: The ID of the knowledge base
        usage_mode:
          $ref: '#/components/schemas/DocumentUsageModeEnum'
          default: auto
          description: The usage mode of the knowledge base
      required:
        - type
        - name
        - id
      title: KnowledgeBaseLocator
    PromptAgentAPIModelOverride-Output:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
          description: The prompt for the agent
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
          description: >-
            The LLM to query with the prompt and the chat history. If using data
            residency, the LLM must be supported in the data residency
            environment
        tool_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of IDs of tools used by the agent
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of Native MCP server ids to be used by the agent
        knowledge_base:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
          description: A list of knowledge bases to be used by the agent
      title: PromptAgentAPIModelOverride-Output
    AgentConfigOverride-Output:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type:
            - string
            - 'null'
          description: Language of the agent - used for ASR and TTS
        max_conversation_duration_message:
          type:
            - string
            - 'null'
          description: >-
            If non-empty, the message the agent will send when max conversation
            duration is reached.
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride-Output'
            - type: 'null'
          description: The prompt for the agent
      title: AgentConfigOverride-Output
    ConversationConfigClientOverride-Output:
      type: object
      properties:
        asr:
          oneOf:
            - $ref: '#/components/schemas/ASRConversationalConfigOverride'
            - type: 'null'
          description: Configuration for conversational transcription
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigOverride'
            - type: 'null'
          description: Configuration for turn detection
        tts:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalConfigOverride'
            - type: 'null'
          description: Configuration for conversational text to speech
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigOverride'
            - type: 'null'
          description: Configuration for conversational events
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigOverride-Output'
            - type: 'null'
          description: Agent specific configuration
      title: ConversationConfigClientOverride-Output
    ConversationInitiationSource:
      type: string
      enum:
        - unknown
        - android_sdk
        - node_js_sdk
        - react_native_sdk
        - react_sdk
        - js_sdk
        - python_sdk
        - widget
        - sip_trunk
        - twilio
        - exotel
        - genesys
        - swift_sdk
        - whatsapp
        - twilio_sms
        - flutter_sdk
        - zendesk_integration
        - slack_integration
        - telegram_integration
        - intercom_integration
        - freshdesk_integration
        - template_preview
        - genesys_bot_connector
      default: unknown
      description: Enum representing the possible sources for conversation initiation.
      title: ConversationInitiationSource
    ConversationInitiationSourceInfo:
      type: object
      properties:
        source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
          description: Source of the conversation initiation
        version:
          type:
            - string
            - 'null'
          description: The SDK version number
      description: Information about the source of conversation initiation
      title: ConversationInitiationSourceInfo
    MockingStrategy:
      type: string
      enum:
        - all
        - selected
        - none
      default: none
      title: MockingStrategy
    MockNoMatchBehavior:
      type: string
      enum:
        - call_real_tool
        - raise_error
      default: raise_error
      title: MockNoMatchBehavior
    OrchestratorToolMockBehaviorConfig:
      type: object
      properties:
        mocking_strategy:
          $ref: '#/components/schemas/MockingStrategy'
          default: none
          description: >-
            Which tools to mock: 'all' mocks every mockable tool, 'selected'
            mocks only those in mocked_tool_names/mocked_tool_ids, 'none'
            disables mocking.
        fallback_strategy:
          $ref: '#/components/schemas/MockNoMatchBehavior'
          default: raise_error
          description: Behavior when no mock matches a tool call.
        mocked_tool_names:
          type: array
          items:
            type: string
          description: Tool names to mock. Only used when mocking_strategy is 'selected'.
      description: 'Orchestrator-side config: tools are identified by resolved names.'
      title: OrchestratorToolMockBehaviorConfig
    ConversationInitiationClientDataInternal:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Output'
        custom_llm_extra_body:
          type: object
          additionalProperties:
            description: Any type
        user_id:
          type:
            - string
            - 'null'
          description: >-
            ID of the end user participating in this conversation (for agent
            owner's user identification)
        source_info:
          $ref: '#/components/schemas/ConversationInitiationSourceInfo'
        branch_id:
          type:
            - string
            - 'null'
          description: ID of the agent branch to use for this conversation
        environment:
          type:
            - string
            - 'null'
          description: Environment to use for resolving environment variables
        starting_workflow_node_id:
          type:
            - string
            - 'null'
          description: >-
            If set, start the workflow at this node id instead of the default
            entry
        dynamic_variables:
          type: object
          additionalProperties:
            description: Any type
        tool_mock_config:
          $ref: '#/components/schemas/OrchestratorToolMockBehaviorConfig'
          description: Configuration for which tools to mock and fallback behavior
      title: ConversationInitiationClientDataInternal
    OutboundCallRecipientResponseModel:
      type: object
      properties:
        id:
          type: string
        phone_number:
          type:
            - string
            - 'null'
        whatsapp_user_id:
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/BatchCallRecipientStatus'
        created_at_unix:
          type: integer
        updated_at_unix:
          type: integer
        conversation_id:
          type:
            - string
            - 'null'
        conversation_initiation_client_data:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataInternal'
            - type: 'null'
      required:
        - id
        - status
        - created_at_unix
        - updated_at_unix
        - conversation_id
      title: OutboundCallRecipientResponseModel
    BatchCallDetailedResponse:
      type: object
      properties:
        id:
          type: string
        phone_number_id:
          type:
            - string
            - 'null'
        phone_provider:
          oneOf:
            - $ref: '#/components/schemas/TelephonyProvider'
            - type: 'null'
        whatsapp_params:
          oneOf:
            - $ref: '#/components/schemas/BatchCallWhatsAppParams'
            - type: 'null'
        name:
          type: string
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        environment:
          type:
            - string
            - 'null'
        created_at_unix:
          type: integer
        scheduled_time_unix:
          type: integer
        timezone:
          type:
            - string
            - 'null'
        total_calls_dispatched:
          type: integer
          default: 0
        total_calls_scheduled:
          type: integer
          default: 0
        total_calls_finished:
          type: integer
          default: 0
        last_updated_at_unix:
          type: integer
        status:
          $ref: '#/components/schemas/BatchCallStatus'
        retry_count:
          type: integer
          default: 0
        telephony_call_config:
          $ref: '#/components/schemas/TelephonyCallConfig'
        target_concurrency_limit:
          type:
            - integer
            - 'null'
          description: >-
            Maximum number of simultaneous calls for this batch. When set,
            dispatch is governed by this limit rather than workspace/agent
            capacity percentages.
        agent_name:
          type: string
        branch_name:
          type:
            - string
            - 'null'
        recipients:
          type: array
          items:
            $ref: '#/components/schemas/OutboundCallRecipientResponseModel'
      required:
        - id
        - phone_number_id
        - phone_provider
        - whatsapp_params
        - name
        - agent_id
        - branch_id
        - environment
        - created_at_unix
        - scheduled_time_unix
        - timezone
        - total_calls_dispatched
        - total_calls_scheduled
        - total_calls_finished
        - last_updated_at_unix
        - status
        - retry_count
        - telephony_call_config
        - target_concurrency_limit
        - agent_name
        - branch_name
        - recipients
      description: Detailed response model for a batch call including all recipients.
      title: BatchCallDetailedResponse
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



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
    "ringing_timeout_secs": 60
  },
  "target_concurrency_limit": 1,
  "agent_name": "string",
  "branch_name": "string",
  "recipients": [
    {
      "id": "string",
      "status": "pending",
      "created_at_unix": 1,
      "updated_at_unix": 1,
      "conversation_id": "string",
      "phone_number": "string",
      "whatsapp_user_id": "string",
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
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "stability": 0.5,
            "speed": 1,
            "similarity_boost": 0.8
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "tool_ids": [],
              "knowledge_base": []
            }
          }
        },
        "custom_llm_extra_body": {},
        "user_id": "string",
        "source_info": {
          "source": "unknown",
          "version": "string"
        },
        "branch_id": "string",
        "environment": "string",
        "starting_workflow_node_id": "string",
        "dynamic_variables": {},
        "tool_mock_config": {
          "mocking_strategy": "none",
          "fallback_strategy": "raise_error",
          "mocked_tool_names": [
            "string"
          ]
        }
      }
    }
  ]
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
