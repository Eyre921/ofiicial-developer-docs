---
title: "List conversations"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/list.md
path: docs/eleven-agents/api-reference/conversations/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List conversations

GET https://api.elevenlabs.io/v1/convai/conversations

Get all conversations of agents that user owns. With option to restrict to a specific agent.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/list

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
        - name: data_collection_ids
          in: query
          description: >-
            Data collection field IDs to include in each conversation summary.
            Repeat param. When omitted, data_collection_results is not returned.
          required: false
          schema:
            type: string
        - name: evaluation_criteria_ids
          in: query
          description: >-
            Evaluation criteria IDs to include in each conversation summary.
            Repeat param. When omitted, evaluation_criteria_results is not
            returned.
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
            $ref: >-
              #/components/schemas/type_conversationalAi/conversations:ConversationsListRequestSummaryMode
            default: exclude
        - name: search
          in: query
          description: Full-text or fuzzy search over transcript messages
          required: false
          schema:
            type: string
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
        - name: parent_conversation_id
          in: query
          description: >-
            Filter conversations by parent conversation ID for subagent
            conversations.
          required: false
          schema:
            type: string
        - name: topic_ids
          in: query
          description: Filter conversations by topic IDs assigned during topic discovery.
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
              #/components/schemas/type_conversationalAi/conversations:ConversationsListRequestExcludeStatusesItem
        - name: tag_ids
          in: query
          description: >-
            Filter conversations by conversation tag IDs assigned via the
            conversation-tags endpoints.
          required: false
          schema:
            type: string
        - name: workflow_node_entered_id
          in: query
          description: Filter conversations to only those that entered the given node.
          required: false
          schema:
            type: string
        - name: termination_reasons
          in: query
          description: >-
            Filter conversations by their stored termination_reason
            (metadata.termination_reason). Repeat param to match any of several.
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
                $ref: '#/components/schemas/type_:GetConversationsPageResponseModel'
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
    type_conversationalAi/conversations:ConversationsListRequestSummaryMode:
      type: string
      enum:
        - exclude
        - include
      default: exclude
      description: Whether to include transcript summaries in the response.
      title: ConversationsListRequestSummaryMode
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
    type_conversationalAi/conversations:ConversationsListRequestExcludeStatusesItem:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: ConversationsListRequestExcludeStatusesItem
    type_:ConversationSummaryResponseModelStatus:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: ConversationSummaryResponseModelStatus
    type_:TelephonyDirection:
      type: string
      enum:
        - inbound
        - outbound
      default: inbound
      title: TelephonyDirection
    type_:ConversationSentimentAnalysisOverallLabel:
      type: string
      enum:
        - positive
        - neutral
        - negative
      title: ConversationSentimentAnalysisOverallLabel
    type_:ConversationSentimentAnalysis:
      type: object
      properties:
        overall_label:
          $ref: '#/components/schemas/type_:ConversationSentimentAnalysisOverallLabel'
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
    type_:EvaluationCriteriaSummaryResult:
      type: object
      properties:
        result:
          $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        score:
          type: integer
        max_score:
          type: integer
      required:
        - result
      title: EvaluationCriteriaSummaryResult
    type_:ConversationSummaryResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type: string
        version_id:
          type: string
        agent_name:
          type: string
        conversation_id:
          type: string
        start_time_unix_secs:
          type: integer
        call_duration_secs:
          type: integer
        message_count:
          type: integer
        status:
          $ref: '#/components/schemas/type_:ConversationSummaryResponseModelStatus'
        termination_reason:
          type: string
          default: ''
        call_successful:
          $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        call_success_score:
          type: number
          format: double
        transcript_summary:
          type: string
        call_summary_title:
          type: string
        main_language:
          type: string
        conversation_initiation_source:
          $ref: '#/components/schemas/type_:ConversationInitiationSource'
        tool_names:
          type: array
          items:
            type: string
        direction:
          $ref: '#/components/schemas/type_:TelephonyDirection'
        rating:
          type: number
          format: double
        sentiment_analysis:
          $ref: '#/components/schemas/type_:ConversationSentimentAnalysis'
        data_collection_results:
          type: object
          additionalProperties:
            description: Any type
        evaluation_criteria_results:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:EvaluationCriteriaSummaryResult'
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
    type_:GetConversationsPageResponseModel:
      type: object
      properties:
        conversations:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConversationSummaryResponseModel'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - conversations
        - has_more
      title: GetConversationsPageResponseModel
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
  "conversations": [
    {
      "agent_id": "agent_id",
      "conversation_id": "conversation_id",
      "start_time_unix_secs": 1,
      "call_duration_secs": 1,
      "message_count": 1,
      "status": "initiated",
      "call_successful": "success",
      "branch_id": "branch_id",
      "version_id": "version_id",
      "agent_name": "agent_name",
      "termination_reason": "termination_reason",
      "call_success_score": 1.1,
      "transcript_summary": "transcript_summary",
      "call_summary_title": "call_summary_title",
      "main_language": "main_language",
      "conversation_initiation_source": "unknown",
      "tool_names": [
        "tool_names"
      ],
      "direction": "inbound",
      "rating": 1.1,
      "sentiment_analysis": {
        "overall_label": "positive",
        "overall_sentiment_score": 1.1,
        "overall_frustration_score": 1.1,
        "min_user_sentiment_score": 1.1,
        "max_user_frustration_score": 1.1,
        "num_scored_user_turns": 1
      },
      "data_collection_results": {
        "key": "value"
      },
      "tag_ids": [
        "tag_ids"
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.list({
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
        dataCollectionIds: [
            "data_collection_ids",
        ],
        dataCollectionParams: [
            "data_collection_params",
        ],
        evaluationCriteriaIds: [
            "evaluation_criteria_ids",
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
        parentConversationId: "parent_conversation_id",
        ratingMax: 1,
        ratingMin: 1,
        search: "search",
        summaryMode: "exclude",
        tagIds: [
            "tag_ids",
        ],
        terminationReasons: [
            "termination_reasons",
        ],
        textOnly: true,
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
        workflowNodeEnteredId: "workflow_node_entered_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.list(
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
    data_collection_ids=[
        "data_collection_ids"
    ],
    data_collection_params=[
        "data_collection_params"
    ],
    evaluation_criteria_ids=[
        "evaluation_criteria_ids"
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
    parent_conversation_id="parent_conversation_id",
    rating_max=1,
    rating_min=1,
    search="search",
    summary_mode="exclude",
    tag_ids=[
        "tag_ids"
    ],
    termination_reasons=[
        "termination_reasons"
    ],
    text_only=True,
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
    workflow_node_entered_id="workflow_node_entered_id",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id")! as URL,
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
