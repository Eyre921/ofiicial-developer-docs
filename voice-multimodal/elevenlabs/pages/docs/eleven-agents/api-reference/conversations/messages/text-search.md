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
            type: string
        - name: visited_agent_ids
          in: query
          description: >-
            Filter conversations where any of these agents participated. Can not
            exceed 50 values.
          required: false
          schema:
            type: string
        - name: visited_agent_branch_ids
          in: query
          description: >-
            Filter conversations where any of these agent branches participated.
            Can not exceed 50 values.
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
        - name: exclude_statuses
          in: query
          description: >-
            Exclude conversations with the given statuses. Useful for hiding
            in-progress / processing conversations from list views.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_conversationalAi/conversations/messages:MessagesTextSearchRequestExcludeStatusesItem
        - name: termination_reasons
          in: query
          description: >-
            Filter conversations by their stored termination_reason
            (metadata.termination_reason). Repeat param to match any of several.
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
        - name: version_id
          in: query
          description: Filter conversations by version ID.
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
    type_conversationalAi/conversations/messages:MessagesTextSearchRequestExcludeStatusesItem:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: MessagesTextSearchRequestExcludeStatusesItem
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

**Response**

```json
{
  "results": [
    {
      "conversation_id": "conversation_id",
      "agent_id": "agent_id",
      "transcript_index": 1,
      "chunk_text": "chunk_text",
      "score": 1.1,
      "conversation_start_time_unix_secs": 1,
      "agent_name": "agent_name",
      "chunk_highlights": [
        {
          "value": "value",
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
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.messages.textSearch({
        agentId: "agent_id",
        branchId: "branch_id",
        callDurationMaxSecs: 1,
        callDurationMinSecs: 1,
        callStartAfterUnix: 1,
        callStartBeforeUnix: 1,
        callSuccessful: "success",
        conversationInitiationSource: "unknown",
        conversationProductType: "agents",
        cursor: "cursor",
        dataCollectionParams: [
            "data_collection_params",
        ],
        evaluationParams: [
            "evaluation_params",
        ],
        excludeStatuses: [
            "initiated",
        ],
        hasFeedbackComment: true,
        mainLanguages: [
            "main_languages",
        ],
        pageSize: 1,
        ratingMax: 1,
        ratingMin: 1,
        sortBy: "search_score",
        summaryMode: "exclude",
        terminationReasons: [
            "termination_reasons",
        ],
        textOnly: true,
        textQuery: "refund policy",
        toolNames: [
            "tool_names",
        ],
        toolNamesErrored: [
            "tool_names_errored",
        ],
        toolNamesSuccessful: [
            "tool_names_successful",
        ],
        topicIds: [
            "topic_ids",
        ],
        userId: "user_id",
        versionId: "version_id",
        visitedAgentBranchIds: [
            "visited_agent_branch_ids",
        ],
        visitedAgentIds: [
            "visited_agent_ids",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.messages.text_search(
    agent_id="agent_id",
    branch_id="branch_id",
    call_duration_max_secs=1,
    call_duration_min_secs=1,
    call_start_after_unix=1,
    call_start_before_unix=1,
    call_successful="success",
    conversation_initiation_source="unknown",
    conversation_product_type="agents",
    cursor="cursor",
    data_collection_params=[
        "data_collection_params"
    ],
    evaluation_params=[
        "evaluation_params"
    ],
    exclude_statuses=[
        "initiated"
    ],
    has_feedback_comment=True,
    main_languages=[
        "main_languages"
    ],
    page_size=1,
    rating_max=1,
    rating_min=1,
    sort_by="search_score",
    summary_mode="exclude",
    termination_reasons=[
        "termination_reasons"
    ],
    text_only=True,
    text_query="refund policy",
    tool_names=[
        "tool_names"
    ],
    tool_names_errored=[
        "tool_names_errored"
    ],
    tool_names_successful=[
        "tool_names_successful"
    ],
    topic_ids=[
        "topic_ids"
    ],
    user_id="user_id",
    version_id="version_id",
    visited_agent_branch_ids=[
        "visited_agent_branch_ids"
    ],
    visited_agent_ids=[
        "visited_agent_ids"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&rating_max=1&rating_min=1&sort_by=search_score&summary_mode=exclude&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&rating_max=1&rating_min=1&sort_by=search_score&summary_mode=exclude&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&rating_max=1&rating_min=1&sort_by=search_score&summary_mode=exclude&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&rating_max=1&rating_min=1&sort_by=search_score&summary_mode=exclude&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&rating_max=1&rating_min=1&sort_by=search_score&summary_mode=exclude&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&rating_max=1&rating_min=1&sort_by=search_score&summary_mode=exclude&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D")! as URL,
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
