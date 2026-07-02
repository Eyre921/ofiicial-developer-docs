---
title: "Get settings"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/get.md
path: docs/eleven-agents/api-reference/workspace/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get settings

GET https://api.elevenlabs.io/v1/convai/settings

Retrieve Convai settings for the workspace

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/settings:
    get:
      operationId: get
      summary: Get Convai Settings
      description: Retrieve Convai settings for the workspace
      tags:
        - subpackage_conversationalAi/settings
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
                $ref: '#/components/schemas/type_:GetConvAiSettingsResponseModel'
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
    type_:ConvAiSecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAiSecretLocator
    type_:ConversationInitiationClientDataWebhookRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
      title: ConversationInitiationClientDataWebhookRequestHeadersValue
    type_:ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
          description: The URL to send the webhook to
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ConversationInitiationClientDataWebhookRequestHeadersValue
          description: The headers to send with the webhook request
      required:
        - url
        - request_headers
      title: ConversationInitiationClientDataWebhook
    type_:WebhookEventType:
      type: string
      enum:
        - transcript
        - audio
        - call_initiation_failure
        - unredacted_transcript
        - unredacted_audio
      title: WebhookEventType
    type_:WebhookTranscriptFormat:
      type: string
      enum:
        - json
        - opentelemetry
      default: json
      title: WebhookTranscriptFormat
    type_:ConvAiWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type: string
        events:
          type: array
          items:
            $ref: '#/components/schemas/type_:WebhookEventType'
          description: >-
            List of event types to send via webhook. Options: transcript, audio,
            call_initiation_failure, unredacted_transcript, unredacted_audio.
        transcript_format:
          $ref: '#/components/schemas/type_:WebhookTranscriptFormat'
          description: Format for transcript webhooks.
        send_audio:
          type: boolean
          description: >-
            DEPRECATED: Use 'events' field instead. Whether to send audio data
            with post-call webhooks for ConvAI conversations
      title: ConvAiWebhooks
    type_:LivekitStackType:
      type: string
      enum:
        - standard
        - static
      default: standard
      title: LivekitStackType
    type_:GetConvAiSettingsResponseModel:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          $ref: '#/components/schemas/type_:ConversationInitiationClientDataWebhook'
        webhooks:
          $ref: '#/components/schemas/type_:ConvAiWebhooks'
        can_use_mcp_servers:
          type: boolean
          default: false
          description: Whether the workspace can use MCP servers
        rag_retention_period_days:
          type: integer
          default: 10
        conversation_embedding_retention_days:
          type: integer
          description: >-
            Days to retain conversation embeddings. None means use the system
            default (30 days).
        default_livekit_stack:
          $ref: '#/components/schemas/type_:LivekitStackType'
      title: GetConvAiSettingsResponseModel
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
{}
```

**Response**

```json
{
  "conversation_initiation_client_data_webhook": {
    "url": "https://hooks.exampleworkspace.com/convai/initiate",
    "request_headers": {
      "Authorization": {
        "secret_id": "secret_12345abcdef"
      },
      "Content-Type": "application/json"
    }
  },
  "webhooks": {
    "post_call_webhook_id": "webhook_98765xyz",
    "events": [
      "transcript",
      "audio",
      "call_initiation_failure"
    ],
    "transcript_format": "json",
    "send_audio": false
  },
  "can_use_mcp_servers": true,
  "rag_retention_period_days": 14,
  "conversation_embedding_retention_days": 30,
  "default_livekit_stack": "standard"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.settings.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.settings.get()

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

	url := "https://api.elevenlabs.io/v1/convai/settings"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/settings")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
