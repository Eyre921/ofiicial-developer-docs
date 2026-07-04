---
title: "List LLMs"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/llm/list.md
path: docs/eleven-agents/api-reference/llm/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List LLMs

GET https://api.elevenlabs.io/v1/convai/llm/list

Returns a list of available LLM models that can be used with agents, including their capabilities and any deprecation status. The response is filtered based on the data residency of the deployment and any compliance requirements (e.g. HIPAA) of the workspace subscription.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/llm/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/llm/list:
    get:
      operationId: list
      summary: List Available Llms
      description: >-
        Returns a list of available LLM models that can be used with agents,
        including their capabilities and any deprecation status. The response is
        filtered based on the data residency of the deployment and any
        compliance requirements (e.g. HIPAA) of the workspace subscription.
      tags:
        - llm
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
                $ref: '#/components/schemas/type_:LlmListResponseModelInput'
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
    type_:LlmReasoningEffort:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
        - xhigh
      title: LlmReasoningEffort
    type_:LlmDeprecationConfigModel:
      type: object
      properties:
        warning_start_days:
          type: integer
          description: >-
            Number of days before the provider deprecation date when warnings
            start being shown.
        fallback_start_days:
          type: integer
          description: >-
            Number of days before the provider deprecation date when traffic
            starts being routed to the replacement model.
        fallback_complete_days:
          type: integer
          description: >-
            Number of days before the provider deprecation date when all traffic
            is routed to the replacement model.
        fallback_start_percentage:
          type: integer
          description: >-
            Percentage of traffic routed to the replacement model when fallback
            begins.
        fallback_complete_percentage:
          type: integer
          description: >-
            Percentage of traffic routed to the replacement model when fallback
            is complete.
      required:
        - warning_start_days
        - fallback_start_days
        - fallback_complete_days
        - fallback_start_percentage
        - fallback_complete_percentage
      title: LlmDeprecationConfigModel
    type_:LlmDeprecationInfoModel:
      type: object
      properties:
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: The identifier of the deprecated LLM model.
        is_deprecated:
          type: boolean
          description: >-
            Whether this model is currently deprecated. True if the model is
            immediately deprecated or within the warning period.
        is_in_warning_period:
          type: boolean
          default: false
          description: >-
            Whether this model is currently in the warning period before
            deprecation.
        is_in_fallback_period:
          type: boolean
          default: false
          description: >-
            Whether traffic is currently being progressively routed to the
            replacement model.
        fallback_percentage:
          type: integer
          default: 0
          description: >-
            Current percentage of traffic being routed to the replacement model
            (0-100).
        provider_deprecation_date:
          type: string
          format: date-time
          description: >-
            The date when the model provider will deprecate this model. Null for
            immediately deprecated models.
        replacement_model:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            The model that replaces this deprecated model. Traffic will be
            automatically routed to this model.
        deprecation_config:
          $ref: '#/components/schemas/type_:LlmDeprecationConfigModel'
          description: >-
            Custom deprecation timing configuration for this model. Null if
            using the default configuration.
      required:
        - llm
        - is_deprecated
      title: LlmDeprecationInfoModel
    type_:RegionalProcessingSurchargeInfo:
      type: object
      properties:
        multiplier:
          type: number
          format: double
          description: >-
            The surcharge multiplier applied to this model's pricing (e.g. 1.1
            for a 10% surcharge).
      required:
        - multiplier
      title: RegionalProcessingSurchargeInfo
    type_:LlmInfoModelInput:
      type: object
      properties:
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: The model identifier.
        is_checkpoint:
          type: boolean
          description: >-
            Whether this is a pinned checkpoint version of a model rather than a
            top-level alias.
        max_tokens_limit:
          type: integer
          description: Maximum number of output tokens the model can generate.
        max_context_limit:
          type: integer
          description: Maximum number of input context tokens the model supports.
        supports_image_input:
          type: boolean
          description: Whether the model supports image file inputs during conversations.
        supports_document_input:
          type: boolean
          description: >-
            Whether the model supports document (PDF) file inputs during
            conversations.
        supports_parallel_tool_calls:
          type: boolean
          description: Whether the model supports calling multiple tools in parallel.
        available_reasoning_efforts:
          type: array
          items:
            $ref: '#/components/schemas/type_:LlmReasoningEffort'
          description: >-
            Available reasoning effort levels for this model. Null if the model
            does not support configurable reasoning.
        deprecation_info:
          $ref: '#/components/schemas/type_:LlmDeprecationInfoModel'
          description: >-
            Deprecation information if this model is deprecated or scheduled for
            deprecation. Null if the model is not affected.
        regional_processing_surcharge:
          $ref: '#/components/schemas/type_:RegionalProcessingSurchargeInfo'
          description: >-
            Regional processing surcharge details if this model has additional
            costs in the current deployment region. Null if no surcharge
            applies.
      required:
        - llm
        - is_checkpoint
        - max_tokens_limit
        - max_context_limit
        - supports_image_input
        - supports_document_input
        - supports_parallel_tool_calls
      title: LlmInfoModelInput
    type_:LlmListResponseModelInput:
      type: object
      properties:
        llms:
          type: array
          items:
            $ref: '#/components/schemas/type_:LlmInfoModelInput'
          description: List of all available LLM models that can be used with agents.
        default_deprecation_config:
          $ref: '#/components/schemas/type_:LlmDeprecationConfigModel'
          description: >-
            The default deprecation timing configuration used for models without
            a custom override.
      required:
        - llms
        - default_deprecation_config
      title: LlmListResponseModelInput
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
  "llms": [
    {
      "llm": "gemini-2.5-flash",
      "is_checkpoint": false,
      "max_tokens_limit": 8192,
      "max_context_limit": 1048576,
      "supports_image_input": true,
      "supports_document_input": true,
      "supports_parallel_tool_calls": true,
      "available_reasoning_efforts": [
        "none"
      ],
      "deprecation_info": {
        "llm": "gpt-4o-mini",
        "is_deprecated": true,
        "is_in_warning_period": true,
        "is_in_fallback_period": false,
        "fallback_percentage": 0,
        "provider_deprecation_date": "2025-06-01T00:00:00Z",
        "replacement_model": "gpt-4o",
        "deprecation_config": {
          "warning_start_days": 30,
          "fallback_start_days": 14,
          "fallback_complete_days": 7,
          "fallback_start_percentage": 25,
          "fallback_complete_percentage": 100
        }
      },
      "regional_processing_surcharge": {
        "multiplier": 1.1
      }
    }
  ],
  "default_deprecation_config": {
    "warning_start_days": 30,
    "fallback_start_days": 14,
    "fallback_complete_days": 7,
    "fallback_start_percentage": 25,
    "fallback_complete_percentage": 100
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.llm.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.llm.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/llm/list"

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

url = URI("https://api.elevenlabs.io/v1/convai/llm/list")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/llm/list")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/llm/list');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/llm/list");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/llm/list")! as URL,
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
