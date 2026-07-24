---
title: "List conversations"
source: https://elevenlabs.io/docs/api-reference/conversations/list.md
path: docs/api-reference/conversations/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List conversations

GET https://api.elevenlabs.io/v1/convai/conversations

Get all conversations of agents that user owns. With option to restrict to a specific agent.

Reference: https://elevenlabs.io/docs/api-reference/conversations/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversations:
    get:
      operationId: list
      summary: List conversations
      description: >-
        Get all conversations of agents that user owns. With option to restrict
        to a specific agent.
      tags:
        - conversations
      parameters:
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
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
        - name: data_collection_ids
          in: query
          description: >-
            Data collection field IDs to include in each conversation summary.
            Repeat param. When omitted, data_collection_results is not returned.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: evaluation_criteria_ids
          in: query
          description: >-
            Evaluation criteria IDs to include in each conversation summary.
            Repeat param. When omitted, evaluation_criteria_results is not
            returned.
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
        - name: page_size
          in: query
          description: >-
            How many conversations to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: summary_mode
          in: query
          description: Whether to include transcript summaries in the response.
          required: false
          schema:
            $ref: '#/components/schemas/V1ConvaiConversationsGetParametersSummaryMode'
            default: exclude
        - name: search
          in: query
          description: Full-text or fuzzy search over transcript messages
          required: false
          schema:
            type:
              - string
              - 'null'
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
                #/components/schemas/V1ConvaiConversationsGetParametersExcludeStatusesSchemaItems
        - name: tag_ids
          in: query
          description: >-
            Filter conversations by conversation tag IDs assigned via the
            conversation-tags endpoints.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: workflow_node_entered_id
          in: query
          description: Filter conversations to only those that entered the given node.
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/GetConversationsPageResponseModel'
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
    V1ConvaiConversationsGetParametersSummaryMode:
      type: string
      enum:
        - exclude
        - include
      default: exclude
      description: Whether to include transcript summaries in the response.
      title: V1ConvaiConversationsGetParametersSummaryMode
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
    ConversationProduct:
      type: string
      enum:
        - agents
        - speech_engine
      description: Which product surface owns this agent document.
      title: ConversationProduct
    V1ConvaiConversationsGetParametersExcludeStatusesSchemaItems:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: V1ConvaiConversationsGetParametersExcludeStatusesSchemaItems
    ConversationSummaryResponseModelStatus:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: ConversationSummaryResponseModelStatus
    TelephonyDirection:
      type: string
      enum:
        - inbound
        - outbound
      default: inbound
      title: TelephonyDirection
    ConversationSentimentAnalysisOverallLabel:
      type: string
      enum:
        - positive
        - neutral
        - negative
      title: ConversationSentimentAnalysisOverallLabel
    ConversationSentimentAnalysis:
      type: object
      properties:
        overall_label:
          $ref: '#/components/schemas/ConversationSentimentAnalysisOverallLabel'
        overall_sentiment_score:
          type: number
          format: double
        overall_frustration_score:
          type: number
          format: double
        min_user_sentiment_score:
          type: number
          format: double
        max_user_frustration_score:
          type: number
          format: double
        num_scored_user_turns:
          type: integer
      required:
        - overall_label
        - overall_sentiment_score
        - overall_frustration_score
        - min_user_sentiment_score
        - max_user_frustration_score
        - num_scored_user_turns
      title: ConversationSentimentAnalysis
    EvaluationCriteriaSummaryResult:
      type: object
      properties:
        result:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        score:
          type:
            - integer
            - 'null'
        max_score:
          type:
            - integer
            - 'null'
      required:
        - result
      title: EvaluationCriteriaSummaryResult
    ConversationSummaryResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        version_id:
          type:
            - string
            - 'null'
        agent_name:
          type:
            - string
            - 'null'
        conversation_id:
          type: string
        start_time_unix_secs:
          type: integer
        call_duration_secs:
          type: integer
        message_count:
          type: integer
        status:
          $ref: '#/components/schemas/ConversationSummaryResponseModelStatus'
        termination_reason:
          type: string
          default: ''
        call_successful:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        call_success_score:
          type:
            - number
            - 'null'
          format: double
        transcript_summary:
          type:
            - string
            - 'null'
        call_summary_title:
          type:
            - string
            - 'null'
        main_language:
          type:
            - string
            - 'null'
        conversation_initiation_source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
        tool_names:
          type:
            - array
            - 'null'
          items:
            type: string
        direction:
          oneOf:
            - $ref: '#/components/schemas/TelephonyDirection'
            - type: 'null'
        rating:
          type:
            - number
            - 'null'
          format: double
        sentiment_analysis:
          oneOf:
            - $ref: '#/components/schemas/ConversationSentimentAnalysis'
            - type: 'null'
        data_collection_results:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
        evaluation_criteria_results:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/EvaluationCriteriaSummaryResult'
        tag_ids:
          type: array
          items:
            type: string
          description: Conversation tag ids assigned to this conversation.
      required:
        - agent_id
        - conversation_id
        - start_time_unix_secs
        - call_duration_secs
        - message_count
        - status
        - call_successful
      title: ConversationSummaryResponseModel
    GetConversationsPageResponseModel:
      type: object
      properties:
        conversations:
          type: array
          items:
            $ref: '#/components/schemas/ConversationSummaryResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - conversations
        - has_more
      title: GetConversationsPageResponseModel
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
  "conversations": [
    {
      "agent_id": "string",
      "conversation_id": "string",
      "start_time_unix_secs": 1,
      "call_duration_secs": 1,
      "message_count": 1,
      "status": "initiated",
      "call_successful": "success",
      "branch_id": "string",
      "version_id": "string",
      "agent_name": "string",
      "termination_reason": "",
      "call_success_score": 1.1,
      "transcript_summary": "string",
      "call_summary_title": "string",
      "main_language": "string",
      "conversation_initiation_source": "unknown",
      "tool_names": [
        "string"
      ],
      "direction": "inbound",
      "rating": 1.1,
      "sentiment_analysis": {
        "overall_label": "positive",
        "overall_sentiment_score": 0,
        "overall_frustration_score": 0.5,
        "min_user_sentiment_score": 0,
        "max_user_frustration_score": 0.5,
        "num_scored_user_turns": 1
      },
      "data_collection_results": {},
      "evaluation_criteria_results": {},
      "tag_ids": [
        "string"
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversations"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations")! as URL,
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
