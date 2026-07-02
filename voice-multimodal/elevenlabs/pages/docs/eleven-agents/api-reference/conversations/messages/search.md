---
title: "Smart search"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/messages/search.md
path: docs/eleven-agents/api-reference/conversations/messages/search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Smart search

GET https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search

Search conversation transcripts by semantic similarity to surface relevant messages based on meaning and intent, rather than exact keyword matches

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/messages/search

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversations/messages/smart-search:
    get:
      operationId: search
      summary: Smart Search Conversation Messages
      description: >-
        Search conversation transcripts by semantic similarity to surface
        relevant messages based on meaning and intent, rather than exact keyword
        matches
      tags:
        - subpackage_conversationalAi/conversations/messages
      parameters:
        - name: text_query
          in: query
          description: The search query text for semantic similarity matching
          required: true
          schema:
            type: string
        - name: agent_id
          in: query
          description: >-
            Agent id (agent_…) or speech engine external id (seng_), resolved to
            the same underlying resource.
          required: false
          schema:
            type: string
        - name: page_size
          in: query
          description: Number of results per page. Max 50.
          required: false
          schema:
            type: integer
            default: 20
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
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
                $ref: '#/components/schemas/type_:MessagesSearchResponse'
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
    type_:ListResponseMeta:
      type: object
      properties:
        total:
          type: integer
        page:
          type: integer
        page_size:
          type: integer
      title: ListResponseMeta
    type_:SearchHighlightSegment:
      type: object
      properties:
        value:
          type: string
        is_hit:
          type: boolean
      required:
        - value
        - is_hit
      title: SearchHighlightSegment
    type_:MessagesSearchResult:
      type: object
      properties:
        conversation_id:
          type: string
        agent_id:
          type: string
        agent_name:
          type: string
        transcript_index:
          type: integer
        chunk_text:
          type: string
        chunk_highlights:
          type: array
          items:
            $ref: '#/components/schemas/type_:SearchHighlightSegment'
        score:
          type: number
          format: double
        conversation_start_time_unix_secs:
          type: integer
      required:
        - conversation_id
        - agent_id
        - transcript_index
        - chunk_text
        - score
        - conversation_start_time_unix_secs
      description: >-
        transcript_index: index of the message in the conversation transcript

        chunk_text: text of the transcript; transcript messages if very long
        could have several chunks.

        chunk_highlights: chunk_text split into matched/unmatched segments for
        highlighting.
            Only populated for keyword/text search, not semantic search.
        score: similarity score of the message to the search query
      title: MessagesSearchResult
    type_:MessagesSearchResponse:
      type: object
      properties:
        meta:
          $ref: '#/components/schemas/type_:ListResponseMeta'
        results:
          type: array
          items:
            $ref: '#/components/schemas/type_:MessagesSearchResult'
        next_cursor:
          type: string
          description: Cursor for the next page of results
        has_more:
          type: boolean
          description: Whether there are more results available
      required:
        - results
        - has_more
      title: MessagesSearchResponse
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
  "results": [
    {
      "conversation_id": "conv_9f8b7a6c5d4e3f2a1b0c",
      "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "transcript_index": 5,
      "chunk_text": "I understand you want to cancel your order and request a refund. Let me check the details for you.",
      "score": 0.92,
      "conversation_start_time_unix_secs": 1685000000,
      "agent_name": "Support Agent John",
      "chunk_highlights": null
    }
  ],
  "has_more": false,
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 10
  },
  "next_cursor": "cursor_abcdef1234567890"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "sk_live_1234567890abcdef",
    });
    await client.conversationalAi.conversations.messages.search({
        agentId: "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        cursor: "cursor",
        pageSize: 10,
        textQuery: "Customer requesting refund for a cancelled order",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="sk_live_1234567890abcdef",
)

client.conversational_ai.conversations.messages.search(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    cursor="cursor",
    page_size=10,
    text_query="Customer requesting refund for a cancelled order",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk_live_1234567890abcdef")
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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk_live_1234567890abcdef'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order")
  .header("xi-api-key", "sk_live_1234567890abcdef")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk_live_1234567890abcdef',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk_live_1234567890abcdef");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk_live_1234567890abcdef",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order")! as URL,
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
