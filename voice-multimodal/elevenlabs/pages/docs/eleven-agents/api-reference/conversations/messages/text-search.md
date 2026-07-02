---
title: "Text search"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/messages/text-search.md
path: docs/eleven-agents/api-reference/conversations/messages/text-search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Text search

GET https://api.elevenlabs.io/v1/convai/conversations/messages/text-search

Search through conversation transcript messages by full-text and fuzzy search

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/messages/text-search

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
        - subpackage_conversationalAi/conversations/messages
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
            type: string
        - name: call_successful
          in: query
          description: The result of the success evaluation
          required: false
          schema:
            $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        - name: call_start_before_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations up to this start
            date.
          required: false
          schema:
            type: integer
        - name: call_start_after_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations after to this
            start date.
          required: false
          schema:
            type: integer
        - name: call_duration_min_secs
          in: query
          description: Minimum call duration in seconds.
          required: false
          schema:
            type: integer
        - name: call_duration_max_secs
          in: query
          description: Maximum call duration in seconds.
          required: false
          schema:
            type: integer
        - name: rating_max
          in: query
          description: Maximum overall rating (1-5).
          required: false
          schema:
            type: integer
        - name: rating_min
          in: query
          description: Minimum overall rating (1-5).
          required: false
          schema:
            type: integer
        - name: has_feedback_comment
          in: query
          description: Filter conversations with user feedback comments.
          required: false
          schema:
            type: boolean
        - name: user_id
          in: query
          description: Filter conversations by the user ID who initiated them.
          required: false
          schema:
            type: string
        - name: evaluation_params
          in: query
          description: >-
            Evaluation filters. Repeat param. Format: criteria_id:result.
            Example: eval=value_framing:success
          required: false
          schema:
            type: string
        - name: data_collection_params
          in: query
          description: >-
            Data collection filters. Repeat param. Format: id:op:value where op
            is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in,
            pipe-delimit values.
          required: false
          schema:
            type: string
        - name: tool_names
          in: query
          description: Filter conversations by tool names used during the call.
          required: false
          schema:
            type: string
        - name: tool_names_successful
          in: query
          description: Filter conversations by tool names that had successful calls.
          required: false
          schema:
            type: string
        - name: tool_names_errored
          in: query
          description: Filter conversations by tool names that had errored calls.
          required: false
          schema:
            type: string
        - name: main_languages
          in: query
          description: Filter conversations by detected main language (language code).
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
        - name: summary_mode
          in: query
          description: Whether to include transcript summaries in the response.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_conversationalAi/conversations/messages:MessagesTextSearchRequestSummaryMode
            default: exclude
        - name: conversation_initiation_source
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_:ConversationInitiationSource'
        - name: text_only
          in: query
          required: false
          schema:
            type: boolean
        - name: conversation_product_type
          in: query
          description: Restrict results to a single conversation product surface.
          required: false
          schema:
            $ref: '#/components/schemas/type_:ConversationProduct'
        - name: branch_id
          in: query
          description: Filter conversations by branch ID.
          required: false
          schema:
            type: string
        - name: topic_ids
          in: query
          description: Filter conversations by topic IDs assigned during topic discovery.
          required: false
          schema:
            type: string
        - name: sort_by
          in: query
          description: >-
            Sort order for search results. 'search_score' sorts by search score,
            'created_at' sorts by conversation start time.
          required: false
          schema:
            $ref: '#/components/schemas/type_:MessageSearchSortBy'
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
    type_:EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    type_conversationalAi/conversations/messages:MessagesTextSearchRequestSummaryMode:
      type: string
      enum:
        - exclude
        - include
      default: exclude
      description: Whether to include transcript summaries in the response.
      title: MessagesTextSearchRequestSummaryMode
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
    type_:ConversationProduct:
      type: string
      enum:
        - agents
        - speech_engine
      description: Which product surface owns this agent document.
      title: ConversationProduct
    type_:MessageSearchSortBy:
      type: string
      enum:
        - search_score
        - created_at
      title: MessageSearchSortBy
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
      "conversation_id": "conv_20240615_123456",
      "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "transcript_index": 5,
      "chunk_text": "I understand your concern about the refund policy. Let me explain how it works.",
      "score": 0.95,
      "conversation_start_time_unix_secs": 1686825600,
      "agent_name": "Customer Support Bot",
      "chunk_highlights": [
        {
          "value": "I understand your concern about the ",
          "is_hit": false
        },
        {
          "value": "refund policy",
          "is_hit": true
        },
        {
          "value": ". Let me explain how it works.",
          "is_hit": false
        }
      ]
    }
  ],
  "has_more": false,
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 1
  },
  "next_cursor": "eyJwYWdlIjoxfQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c",
    });
    await client.conversationalAi.conversations.messages.textSearch({
        agentId: "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        branchId: "branch_987654321",
        callDurationMaxSecs: 3600,
        callDurationMinSecs: 60,
        callStartAfterUnix: 1600000000,
        callStartBeforeUnix: 1700000000,
        callSuccessful: "success",
        conversationInitiationSource: "widget",
        conversationProductType: "agents",
        cursor: "eyJwYWdlIjoxfQ==",
        dataCollectionParams: [
            "region:eq:us-east",
            "device:in:mobile|desktop",
        ],
        evaluationParams: [
            "value_framing:success",
            "tone:failure",
        ],
        hasFeedbackComment: true,
        mainLanguages: [
            "en",
            "es",
        ],
        pageSize: 20,
        ratingMax: 5,
        ratingMin: 3,
        sortBy: "search_score",
        summaryMode: "include",
        textOnly: false,
        textQuery: "refund policy",
        toolNames: [
            "crm_integration",
            "voice_recorder",
        ],
        toolNamesErrored: [
            "voice_recorder",
        ],
        toolNamesSuccessful: [
            "crm_integration",
        ],
        topicIds: [
            "topic_abc123",
            "topic_def456",
        ],
        userId: "user_1234567890",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c",
)

client.conversational_ai.conversations.messages.text_search(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="branch_987654321",
    call_duration_max_secs=3600,
    call_duration_min_secs=60,
    call_start_after_unix=1600000000,
    call_start_before_unix=1700000000,
    call_successful="success",
    conversation_initiation_source="widget",
    conversation_product_type="agents",
    cursor="eyJwYWdlIjoxfQ==",
    data_collection_params=[
        "region:eq:us-east",
        "device:in:mobile|desktop"
    ],
    evaluation_params=[
        "value_framing:success",
        "tone:failure"
    ],
    has_feedback_comment=True,
    main_languages=[
        "en",
        "es"
    ],
    page_size=20,
    rating_max=5,
    rating_min=3,
    sort_by="search_score",
    summary_mode="include",
    text_only=False,
    text_query="refund policy",
    tool_names=[
        "crm_integration",
        "voice_recorder"
    ],
    tool_names_errored=[
        "voice_recorder"
    ],
    tool_names_successful=[
        "crm_integration"
    ],
    topic_ids=[
        "topic_abc123",
        "topic_def456"
    ],
    user_id="user_1234567890",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_987654321&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=widget&conversation_product_type=agents&cursor=eyJwYWdlIjoxfQ%3D%3D&data_collection_params=%5B%22region%3Aeq%3Aus-east%22%2C%22device%3Ain%3Amobile%7Cdesktop%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&has_feedback_comment=true&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&text_only=false&text_query=refund+policy&tool_names=%5B%22crm_integration%22%2C%22voice_recorder%22%5D&tool_names_errored=%5B%22voice_recorder%22%5D&tool_names_successful=%5B%22crm_integration%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&user_id=user_1234567890"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c")
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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_987654321&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=widget&conversation_product_type=agents&cursor=eyJwYWdlIjoxfQ%3D%3D&data_collection_params=%5B%22region%3Aeq%3Aus-east%22%2C%22device%3Ain%3Amobile%7Cdesktop%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&has_feedback_comment=true&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&text_only=false&text_query=refund+policy&tool_names=%5B%22crm_integration%22%2C%22voice_recorder%22%5D&tool_names_errored=%5B%22voice_recorder%22%5D&tool_names_successful=%5B%22crm_integration%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&user_id=user_1234567890")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_987654321&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=widget&conversation_product_type=agents&cursor=eyJwYWdlIjoxfQ%3D%3D&data_collection_params=%5B%22region%3Aeq%3Aus-east%22%2C%22device%3Ain%3Amobile%7Cdesktop%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&has_feedback_comment=true&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&text_only=false&text_query=refund+policy&tool_names=%5B%22crm_integration%22%2C%22voice_recorder%22%5D&tool_names_errored=%5B%22voice_recorder%22%5D&tool_names_successful=%5B%22crm_integration%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&user_id=user_1234567890")
  .header("xi-api-key", "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_987654321&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=widget&conversation_product_type=agents&cursor=eyJwYWdlIjoxfQ%3D%3D&data_collection_params=%5B%22region%3Aeq%3Aus-east%22%2C%22device%3Ain%3Amobile%7Cdesktop%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&has_feedback_comment=true&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&text_only=false&text_query=refund+policy&tool_names=%5B%22crm_integration%22%2C%22voice_recorder%22%5D&tool_names_errored=%5B%22voice_recorder%22%5D&tool_names_successful=%5B%22crm_integration%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&user_id=user_1234567890', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_987654321&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=widget&conversation_product_type=agents&cursor=eyJwYWdlIjoxfQ%3D%3D&data_collection_params=%5B%22region%3Aeq%3Aus-east%22%2C%22device%3Ain%3Amobile%7Cdesktop%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&has_feedback_comment=true&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&text_only=false&text_query=refund+policy&tool_names=%5B%22crm_integration%22%2C%22voice_recorder%22%5D&tool_names_errored=%5B%22voice_recorder%22%5D&tool_names_successful=%5B%22crm_integration%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&user_id=user_1234567890");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_987654321&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=widget&conversation_product_type=agents&cursor=eyJwYWdlIjoxfQ%3D%3D&data_collection_params=%5B%22region%3Aeq%3Aus-east%22%2C%22device%3Ain%3Amobile%7Cdesktop%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&has_feedback_comment=true&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&text_only=false&text_query=refund+policy&tool_names=%5B%22crm_integration%22%2C%22voice_recorder%22%5D&tool_names_errored=%5B%22voice_recorder%22%5D&tool_names_successful=%5B%22crm_integration%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&user_id=user_1234567890")! as URL,
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
