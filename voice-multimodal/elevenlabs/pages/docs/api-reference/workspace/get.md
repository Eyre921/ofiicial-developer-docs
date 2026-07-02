---
title: "Get settings"
source: https://elevenlabs.io/docs/api-reference/workspace/get.md
path: docs/api-reference/workspace/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get settings

GET https://api.elevenlabs.io/v1/convai/settings

Retrieve Convai settings for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/get

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
                $ref: '#/components/schemas/GetConvAISettingsResponseModel'
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
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAISecretLocator
    ConversationInitiationClientDataWebhookRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
      title: ConversationInitiationClientDataWebhookRequestHeaders
    ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
          description: The URL to send the webhook to
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationInitiationClientDataWebhookRequestHeaders
          description: The headers to send with the webhook request
      required:
        - url
        - request_headers
      title: ConversationInitiationClientDataWebhook
    WebhookEventType:
      type: string
      enum:
        - transcript
        - audio
        - call_initiation_failure
        - unredacted_transcript
        - unredacted_audio
      title: WebhookEventType
    WebhookTranscriptFormat:
      type: string
      enum:
        - json
        - opentelemetry
      default: json
      title: WebhookTranscriptFormat
    ConvAIWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type:
            - string
            - 'null'
        events:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEventType'
          description: >-
            List of event types to send via webhook. Options: transcript, audio,
            call_initiation_failure, unredacted_transcript, unredacted_audio.
        transcript_format:
          $ref: '#/components/schemas/WebhookTranscriptFormat'
          default: json
          description: Format for transcript webhooks.
        send_audio:
          type:
            - boolean
            - 'null'
          description: >-
            DEPRECATED: Use 'events' field instead. Whether to send audio data
            with post-call webhooks for ConvAI conversations
      title: ConvAIWebhooks
    LivekitStackType:
      type: string
      enum:
        - standard
        - static
      default: standard
      title: LivekitStackType
    GetConvAISettingsResponseModel:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationClientDataWebhook'
            - type: 'null'
        webhooks:
          $ref: '#/components/schemas/ConvAIWebhooks'
        can_use_mcp_servers:
          type: boolean
          default: false
          description: Whether the workspace can use MCP servers
        rag_retention_period_days:
          type: integer
          default: 10
        conversation_embedding_retention_days:
          type:
            - integer
            - 'null'
          description: >-
            Days to retain conversation embeddings. None means use the system
            default (30 days).
        default_livekit_stack:
          $ref: '#/components/schemas/LivekitStackType'
          default: standard
      title: GetConvAISettingsResponseModel
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
  "conversation_initiation_client_data_webhook": {
    "url": "https://example.com/webhook",
    "request_headers": {
      "Content-Type": "application/json"
    }
  },
  "webhooks": {
    "post_call_webhook_id": "string",
    "events": [
      "transcript"
    ],
    "transcript_format": "json",
    "send_audio": true
  },
  "can_use_mcp_servers": false,
  "rag_retention_period_days": 10,
  "conversation_embedding_retention_days": 1,
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/settings"

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

url = URI("https://api.elevenlabs.io/v1/convai/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/settings")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings")! as URL,
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
