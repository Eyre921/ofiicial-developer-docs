---
title: "Text search"
source: https://elevenlabs.io/docs/api-reference/conversations/messages/text-search.md
path: docs/api-reference/conversations/messages/text-search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Text search

GET https://api.elevenlabs.io/v1/convai/conversations/messages/text-search

Search through conversation transcript messages by full-text and fuzzy search

Reference: https://elevenlabs.io/docs/api-reference/conversations/messages/text-search

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversations/messages/text-search:
    get:
      operationId: text_search
      summary: Text Search Conversation Messages
      description: >-
        Search through conversation transcript messages by full-text and fuzzy
        search
      tags:
        - messages
      parameters:
        - name: text_query
          in: query
          description: The search query text for full-text and fuzzy matching
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
            type:
              - string
              - 'null'
        - name: visited_agent_ids
          in: query
          description: >-
            Filter conversations where any of these agents participated. Can not
            exceed 50 values.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: visited_agent_branch_ids
          in: query
          description: >-
            Filter conversations where any of these agent branches participated.
            Can not exceed 50 values.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: call_successful
          in: query
          description: The result of the success evaluation
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/EvaluationSuccessResult'
              - type: 'null'
        - name: call_start_before_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations up to this start
            date.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: call_start_after_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations after to this
            start date.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: call_duration_min_secs
          in: query
          description: Minimum call duration in seconds.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: call_duration_max_secs
          in: query
          description: Maximum call duration in seconds.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: rating_max
          in: query
          description: Maximum overall rating (1-5).
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: rating_min
          in: query
          description: Minimum overall rating (1-5).
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: has_feedback_comment
          in: query
          description: Filter conversations with user feedback comments.
          required: false
          schema:
            type:
              - boolean
              - 'null'
        - name: user_id
          in: query
          description: Filter conversations by the user ID who initiated them.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: evaluation_params
          in: query
          description: >-
            Evaluation filters. Repeat param. Format: criteria_id:result.
            Example: eval=value_framing:success
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: data_collection_params
          in: query
          description: >-
            Data collection filters. Repeat param. Format: id:op:value where op
            is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in,
            pipe-delimit values.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: tool_names
          in: query
          description: Filter conversations by tool names used during the call.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: tool_names_successful
          in: query
          description: Filter conversations by tool names that had successful calls.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: tool_names_errored
          in: query
          description: Filter conversations by tool names that had errored calls.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: main_languages
          in: query
          description: Filter conversations by detected main language (language code).
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: exclude_statuses
          in: query
          description: >-
            Exclude conversations with the given statuses. Useful for hiding
            in-progress / processing conversations from list views.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              $ref: >-
                #/components/schemas/V1ConvaiConversationsMessagesTextSearchGetParametersExcludeStatusesSchemaItems
        - name: termination_reasons
          in: query
          description: >-
            Filter conversations by their stored termination_reason
            (metadata.termination_reason). Repeat param to match any of several.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: page_size
          in: query
          description: Number of results per page. Max 50.
          required: false
          schema:
            type: integer
            default: 20
        - name: summary_mode
          in: query
          description: Whether to include transcript summaries in the response.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1ConvaiConversationsMessagesTextSearchGetParametersSummaryMode
            default: exclude
        - name: conversation_initiation_source
          in: query
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/ConversationInitiationSource'
              - type: 'null'
        - name: text_only
          in: query
          required: false
          schema:
            type:
              - boolean
              - 'null'
        - name: conversation_product_type
          in: query
          description: Restrict results to a single conversation product surface.
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/ConversationProduct'
              - type: 'null'
        - name: branch_id
          in: query
          description: Filter conversations by branch ID.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: version_id
          in: query
          description: Filter conversations by version ID.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: topic_ids
          in: query
          description: Filter conversations by topic IDs assigned during topic discovery.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: sort_by
          in: query
          description: >-
            Sort order for search results. 'search_score' sorts by search score,
            'created_at' sorts by conversation start time.
          required: false
          schema:
            $ref: '#/components/schemas/MessageSearchSortBy'
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/MessagesSearchResponse'
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
    EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    V1ConvaiConversationsMessagesTextSearchGetParametersExcludeStatusesSchemaItems:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: >-
        V1ConvaiConversationsMessagesTextSearchGetParametersExcludeStatusesSchemaItems
    V1ConvaiConversationsMessagesTextSearchGetParametersSummaryMode:
      type: string
      enum:
        - exclude
        - include
      default: exclude
      description: Whether to include transcript summaries in the response.
      title: V1ConvaiConversationsMessagesTextSearchGetParametersSummaryMode
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
        - audiocodes
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
    ConversationProduct:
      type: string
      enum:
        - agents
        - speech_engine
      description: Which product surface owns this agent document.
      title: ConversationProduct
    MessageSearchSortBy:
      type: string
      enum:
        - search_score
        - created_at
      title: MessageSearchSortBy
    ListResponseMeta:
      type: object
      properties:
        total:
          type:
            - integer
            - 'null'
        page:
          type:
            - integer
            - 'null'
        page_size:
          type:
            - integer
            - 'null'
      title: ListResponseMeta
    SearchHighlightSegment:
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
    MessagesSearchResult:
      type: object
      properties:
        conversation_id:
          type: string
        agent_id:
          type: string
        agent_name:
          type:
            - string
            - 'null'
        transcript_index:
          type: integer
        chunk_text:
          type: string
        chunk_highlights:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SearchHighlightSegment'
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
    MessagesSearchResponse:
      type: object
      properties:
        meta:
          $ref: '#/components/schemas/ListResponseMeta'
        results:
          type: array
          items:
            $ref: '#/components/schemas/MessagesSearchResult'
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for the next page of results
        has_more:
          type: boolean
          description: Whether there are more results available
      required:
        - results
        - has_more
      title: MessagesSearchResponse
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
  "results": [
    {
      "conversation_id": "string",
      "agent_id": "string",
      "transcript_index": 1,
      "chunk_text": "string",
      "score": 1.1,
      "conversation_start_time_unix_secs": 1,
      "agent_name": "string",
      "chunk_highlights": [
        {
          "value": "string",
          "is_hit": true
        }
      ]
    }
  ],
  "has_more": true,
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 1
  },
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.messages.textSearch({
        textQuery: "refund policy",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.messages.text_search(
    text_query="refund policy",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?text_query=refund+policy"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?text_query=refund+policy")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?text_query=refund+policy")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?text_query=refund+policy');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?text_query=refund+policy");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?text_query=refund+policy")! as URL,
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
