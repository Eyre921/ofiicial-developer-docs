---
title: "Think Models"
source: https://developers.deepgram.com/reference/voice-agent/think-models.md
path: reference/voice-agent/think-models
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Think Models

GET https://agent.deepgram.com/v1/agent/settings/think/models

Retrieves the available think models that can be used for AI agent processing

Reference: https://developers.deepgram.com/reference/voice-agent/think-models

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/agent/settings/think/models:
    get:
      operationId: list
      summary: List Agent Think Models
      description: >-
        Retrieves the available think models that can be used for AI agent
        processing
      tags:
        - models
      responses:
        '200':
          description: List of available think models
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentThinkModelsV1Response'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://agent.deepgram.com
    description: Production
components:
  schemas:
    AgentThinkModelsV1ResponseModelsItemsOneOf0Id:
      type: string
      enum:
        - gpt-5
        - gpt-5-mini
        - gpt-5-nano
        - gpt-4.1
        - gpt-4.1-mini
        - gpt-4.1-nano
        - gpt-4o
        - gpt-4o-mini
      description: The unique identifier of the OpenAI model
      title: AgentThinkModelsV1ResponseModelsItemsOneOf0Id
    AgentThinkModelsV1ResponseModelsItems0:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItemsOneOf0Id'
          description: The unique identifier of the OpenAI model
        name:
          type: string
          description: The display name of the model
        provider:
          description: The provider of the model
      required:
        - id
        - name
        - provider
      description: OpenAI models
      title: AgentThinkModelsV1ResponseModelsItems0
    AgentThinkModelsV1ResponseModelsItemsOneOf1Id:
      type: string
      enum:
        - claude-3-5-haiku-latest
        - claude-sonnet-4-20250514
      description: The unique identifier of the Anthropic model
      title: AgentThinkModelsV1ResponseModelsItemsOneOf1Id
    AgentThinkModelsV1ResponseModelsItems1:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItemsOneOf1Id'
          description: The unique identifier of the Anthropic model
        name:
          type: string
          description: The display name of the model
        provider:
          description: The provider of the model
      required:
        - id
        - name
        - provider
      description: Anthropic models
      title: AgentThinkModelsV1ResponseModelsItems1
    AgentThinkModelsV1ResponseModelsItemsOneOf2Id:
      type: string
      enum:
        - gemini-2.5-flash
        - gemini-2.0-flash
        - gemini-2.0-flash-lite
      description: The unique identifier of the Google model
      title: AgentThinkModelsV1ResponseModelsItemsOneOf2Id
    AgentThinkModelsV1ResponseModelsItems2:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItemsOneOf2Id'
          description: The unique identifier of the Google model
        name:
          type: string
          description: The display name of the model
        provider:
          description: The provider of the model
      required:
        - id
        - name
        - provider
      description: Google models
      title: AgentThinkModelsV1ResponseModelsItems2
    AgentThinkModelsV1ResponseModelsItemsOneOf3Id:
      type: string
      enum:
        - openai/gpt-oss-20b
      description: The unique identifier of the Groq model
      title: AgentThinkModelsV1ResponseModelsItemsOneOf3Id
    AgentThinkModelsV1ResponseModelsItems3:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItemsOneOf3Id'
          description: The unique identifier of the Groq model
        name:
          type: string
          description: The display name of the model
        provider:
          description: The provider of the model
      required:
        - id
        - name
        - provider
      description: Groq models
      title: AgentThinkModelsV1ResponseModelsItems3
    AgentThinkModelsV1ResponseModelsItems4:
      type: object
      properties:
        id:
          type: string
          description: >-
            The unique identifier of the AWS Bedrock model (any model string
            accepted for BYO LLMs)
        name:
          type: string
          description: The display name of the model
        provider:
          description: The provider of the model
      required:
        - id
        - name
        - provider
      description: AWS Bedrock models (custom models accepted)
      title: AgentThinkModelsV1ResponseModelsItems4
    AgentThinkModelsV1ResponseModelsItems:
      oneOf:
        - $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItems0'
        - $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItems1'
        - $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItems2'
        - $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItems3'
        - $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItems4'
      title: AgentThinkModelsV1ResponseModelsItems
    AgentThinkModelsV1Response:
      type: object
      properties:
        models:
          type: array
          items:
            $ref: '#/components/schemas/AgentThinkModelsV1ResponseModelsItems'
      required:
        - models
      title: AgentThinkModelsV1Response
    ErrorResponseTextError:
      type: string
      title: ErrorResponseTextError
    ErrorResponseLegacyError:
      type: object
      properties:
        err_code:
          type: string
          description: The error code
        err_msg:
          type: string
          description: The error message
        request_id:
          type: string
          description: The request ID
      title: ErrorResponseLegacyError
    ErrorResponseModernError:
      type: object
      properties:
        category:
          type: string
          description: The category of the error
        message:
          type: string
          description: A message about the error
        details:
          type: string
          description: A description of the error
        request_id:
          type: string
          description: The unique identifier of the request
      title: ErrorResponseModernError
    ErrorResponse:
      oneOf:
        - $ref: '#/components/schemas/ErrorResponseTextError'
        - $ref: '#/components/schemas/ErrorResponseLegacyError'
        - $ref: '#/components/schemas/ErrorResponseModernError'
      title: ErrorResponse

```

## Examples



**Response**

```json
{
  "models": [
    {
      "id": "gpt-5",
      "name": "GPT-5",
      "provider": "open_ai"
    }
  ]
}
```

**SDK Code**

```python List supported models
import requests

url = "https://agent.deepgram.com/v1/agent/settings/think/models"
response = requests.get(url)

print(response.json())

```

```typescript List supported models
const res = await fetch(
  "https://agent.deepgram.com/v1/agent/settings/think/models",
);
const data = await res.json();
console.log(data);

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://agent.deepgram.com/v1/agent/settings/think/models"

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

url = URI("https://agent.deepgram.com/v1/agent/settings/think/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://agent.deepgram.com/v1/agent/settings/think/models")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://agent.deepgram.com/v1/agent/settings/think/models');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://agent.deepgram.com/v1/agent/settings/think/models");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://agent.deepgram.com/v1/agent/settings/think/models")! as URL,
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
