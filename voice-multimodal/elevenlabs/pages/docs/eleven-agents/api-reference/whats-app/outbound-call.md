---
title: "Outbound call via WhatsApp"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/outbound-call.md
path: docs/eleven-agents/api-reference/whats-app/outbound-call
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Outbound call via WhatsApp

POST https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call
Content-Type: application/json

Make an outbound call via WhatsApp

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/outbound-call

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/whatsapp/outbound-call:
    post:
      operationId: outbound_call
      summary: Make An Outbound Call Via Whatsapp
      description: Make an outbound call via WhatsApp
      tags:
        - whatsapp
      parameters:
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
                $ref: '#/components/schemas/type_:WhatsAppOutboundCallResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                whatsapp_phone_number_id:
                  type: string
                whatsapp_user_id:
                  type: string
                whatsapp_call_permission_request_template_name:
                  type: string
                whatsapp_call_permission_request_template_language_code:
                  type: string
                agent_id:
                  type: string
                conversation_initiation_client_data:
                  $ref: >-
                    #/components/schemas/type_:ConversationInitiationClientDataRequestInput
              required:
                - whatsapp_phone_number_id
                - whatsapp_user_id
                - whatsapp_call_permission_request_template_name
                - whatsapp_call_permission_request_template_language_code
                - agent_id
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
    type_:AsrConversationalConfigOverride:
      type: object
      properties:
        keywords:
          type: array
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: AsrConversationalConfigOverride
    type_:SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type: string
          description: >-
            Message to show when the first soft timeout is reached while waiting
            for LLM response. Supports dynamic variables (e.g.,
            {{system__time}}, {{custom_variable}}).
      title: SoftTimeoutConfigOverride
    type_:TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          $ref: '#/components/schemas/type_:SoftTimeoutConfigOverride'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfigOverride
    type_:TtsConversationalConfigOverride:
      type: object
      properties:
        voice_id:
          type: string
          description: The voice ID to use for TTS
        stability:
          type: number
          format: double
          description: The stability of generated speech
        speed:
          type: number
          format: double
          description: The speed of generated speech
        similarity_boost:
          type: number
          format: double
          description: The similarity boost for generated speech
      title: TtsConversationalConfigOverride
    type_:ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type: boolean
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
      title: ConversationConfigOverride
    type_:Llm:
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
      title: Llm
    type_:KnowledgeBaseDocumentType:
      type: string
      enum:
        - file
        - url
        - text
        - folder
      title: KnowledgeBaseDocumentType
    type_:DocumentUsageModeEnum:
      type: string
      enum:
        - prompt
        - auto
      default: auto
      title: DocumentUsageModeEnum
    type_:KnowledgeBaseLocator:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:KnowledgeBaseDocumentType'
          description: The type of the knowledge base
        name:
          type: string
          description: The name of the knowledge base
        id:
          type: string
          description: The ID of the knowledge base
        usage_mode:
          $ref: '#/components/schemas/type_:DocumentUsageModeEnum'
          description: The usage mode of the knowledge base
      required:
        - type
        - name
        - id
      title: KnowledgeBaseLocator
    type_:PromptAgentApiModelOverrideInput:
      type: object
      properties:
        prompt:
          type: string
          description: The prompt for the agent
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            The LLM to query with the prompt and the chat history. If using data
            residency, the LLM must be supported in the data residency
            environment
        tool_ids:
          type: array
          items:
            type: string
          description: A list of IDs of tools used by the agent
        native_mcp_server_ids:
          type: array
          items:
            type: string
          description: A list of Native MCP server ids to be used by the agent
        knowledge_base:
          type: array
          items:
            $ref: '#/components/schemas/type_:KnowledgeBaseLocator'
          description: A list of knowledge bases to be used by the agent
      title: PromptAgentApiModelOverrideInput
    type_:AgentConfigOverrideInput:
      type: object
      properties:
        first_message:
          type: string
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type: string
          description: Language of the agent - used for ASR and TTS
        max_conversation_duration_message:
          type: string
          description: >-
            If non-empty, the message the agent will send when max conversation
            duration is reached.
        prompt:
          $ref: '#/components/schemas/type_:PromptAgentApiModelOverrideInput'
          description: The prompt for the agent
      title: AgentConfigOverrideInput
    type_:ConversationConfigClientOverrideInput:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/type_:AsrConversationalConfigOverride'
          description: Configuration for conversational transcription
        turn:
          $ref: '#/components/schemas/type_:TurnConfigOverride'
          description: Configuration for turn detection
        tts:
          $ref: '#/components/schemas/type_:TtsConversationalConfigOverride'
          description: Configuration for conversational text to speech
        conversation:
          $ref: '#/components/schemas/type_:ConversationConfigOverride'
          description: Configuration for conversational events
        agent:
          $ref: '#/components/schemas/type_:AgentConfigOverrideInput'
          description: Agent specific configuration
      title: ConversationConfigClientOverrideInput
    type_:ConversationInitiationSource:
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
    type_:ConversationInitiationSourceInfo:
      type: object
      properties:
        source:
          $ref: '#/components/schemas/type_:ConversationInitiationSource'
          description: Source of the conversation initiation
        version:
          type: string
          description: The SDK version number
      description: Information about the source of conversation initiation
      title: ConversationInitiationSourceInfo
    type_:ConversationInitiationClientDataRequestInput:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/type_:ConversationConfigClientOverrideInput'
        custom_llm_extra_body:
          type: object
          additionalProperties:
            description: Any type
        user_id:
          type: string
          description: >-
            ID of the end user participating in this conversation (for agent
            owner's user identification)
        source_info:
          $ref: '#/components/schemas/type_:ConversationInitiationSourceInfo'
        branch_id:
          type: string
          description: ID of the agent branch to use for this conversation
        environment:
          type: string
          description: Environment to use for resolving environment variables
        starting_workflow_node_id:
          type: string
          description: >-
            If set, start the workflow at this node id instead of the default
            entry
        dynamic_variables:
          type: object
          additionalProperties:
            description: Any type
      title: ConversationInitiationClientDataRequestInput
    type_:WhatsAppOutboundCallResponse:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
        conversation_id:
          type: string
      required:
        - success
        - message
      title: WhatsAppOutboundCallResponse
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

**Request**

```json
{
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
  "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
  "agent_id": "agent_id"
}
```

**Response**

```json
{
  "success": true,
  "message": "message",
  "conversation_id": "conversation_id"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsapp.outboundCall({
        whatsappPhoneNumberId: "whatsapp_phone_number_id",
        whatsappUserId: "whatsapp_user_id",
        whatsappCallPermissionRequestTemplateName: "whatsapp_call_permission_request_template_name",
        whatsappCallPermissionRequestTemplateLanguageCode: "whatsapp_call_permission_request_template_language_code",
        agentId: "agent_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp.outbound_call(
    whatsapp_phone_number_id="whatsapp_phone_number_id",
    whatsapp_user_id="whatsapp_user_id",
    whatsapp_call_permission_request_template_name="whatsapp_call_permission_request_template_name",
    whatsapp_call_permission_request_template_language_code="whatsapp_call_permission_request_template_language_code",
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call"

	payload := strings.NewReader("{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call")
  .header("Content-Type", "application/json")
  .body("{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call', [
  'body' => '{
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
  "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
  "agent_id": "agent_id"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"whatsapp_phone_number_id\": \"whatsapp_phone_number_id\",\n  \"whatsapp_user_id\": \"whatsapp_user_id\",\n  \"whatsapp_call_permission_request_template_name\": \"whatsapp_call_permission_request_template_name\",\n  \"whatsapp_call_permission_request_template_language_code\": \"whatsapp_call_permission_request_template_language_code\",\n  \"agent_id\": \"agent_id\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "whatsapp_phone_number_id": "whatsapp_phone_number_id",
  "whatsapp_user_id": "whatsapp_user_id",
  "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
  "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
  "agent_id": "agent_id"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp/outbound-call")! as URL,
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
