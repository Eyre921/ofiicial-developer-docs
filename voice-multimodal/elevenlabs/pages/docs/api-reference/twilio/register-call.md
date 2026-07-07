---
title: "Register call"
source: https://elevenlabs.io/docs/api-reference/twilio/register-call.md
path: docs/api-reference/twilio/register-call
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Register call

POST https://api.elevenlabs.io/v1/convai/twilio/register-call
Content-Type: application/json

Register a Twilio call and return TwiML to connect the call

Reference: https://elevenlabs.io/docs/api-reference/twilio/register-call

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/twilio/register-call:
    post:
      operationId: register_call
      summary: Register A Twilio Call And Return Twiml
      description: Register a Twilio call and return TwiML to connect the call
      tags:
        - twilio
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
                type: object
                properties: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Register_a_Twilio_call_and_return_TwiML_v1_convai_twilio_register_call_post
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
    TelephonyDirection:
      type: string
      enum:
        - inbound
        - outbound
      default: inbound
      title: TelephonyDirection
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
    PromptAgentAPIModelOverride-Input:
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
      title: PromptAgentAPIModelOverride-Input
    AgentConfigOverride-Input:
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
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride-Input'
            - type: 'null'
          description: The prompt for the agent
      title: AgentConfigOverride-Input
    ConversationConfigClientOverride-Input:
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
            - $ref: '#/components/schemas/AgentConfigOverride-Input'
            - type: 'null'
          description: Agent specific configuration
      title: ConversationConfigClientOverride-Input
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
        - salesforce_integration
        - template_preview
        - genesys_bot_connector
        - subagent_tool
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
    ConversationInitiationClientDataRequest-Input:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Input'
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
      title: ConversationInitiationClientDataRequest-Input
    Body_Register_a_Twilio_call_and_return_TwiML_v1_convai_twilio_register_call_post:
      type: object
      properties:
        agent_id:
          type: string
        from_number:
          type: string
        to_number:
          type: string
        direction:
          $ref: '#/components/schemas/TelephonyDirection'
          default: inbound
        conversation_initiation_client_data:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationInitiationClientDataRequest-Input
            - type: 'null'
      required:
        - agent_id
        - from_number
        - to_number
      title: >-
        Body_Register_a_Twilio_call_and_return_TwiML_v1_convai_twilio_register_call_post
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



**Request**

```json
{
  "agent_id": "string",
  "from_number": "string",
  "to_number": "string"
}
```

**Response**

```json
"string"
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.twilio.registerCall({
        agentId: "string",
        fromNumber: "string",
        toNumber: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.twilio.register_call(
    agent_id="string",
    from_number="string",
    to_number="string",
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

	url := "https://api.elevenlabs.io/v1/convai/twilio/register-call"

	payload := strings.NewReader("{\n  \"agent_id\": \"string\",\n  \"from_number\": \"string\",\n  \"to_number\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/twilio/register-call")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"agent_id\": \"string\",\n  \"from_number\": \"string\",\n  \"to_number\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/twilio/register-call")
  .header("Content-Type", "application/json")
  .body("{\n  \"agent_id\": \"string\",\n  \"from_number\": \"string\",\n  \"to_number\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/twilio/register-call', [
  'body' => '{
  "agent_id": "string",
  "from_number": "string",
  "to_number": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/twilio/register-call");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"agent_id\": \"string\",\n  \"from_number\": \"string\",\n  \"to_number\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "agent_id": "string",
  "from_number": "string",
  "to_number": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/twilio/register-call")! as URL,
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
