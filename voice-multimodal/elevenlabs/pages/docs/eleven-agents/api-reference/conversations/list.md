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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.
- `agent_id` (string, optional) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `visited_agent_ids` (string, optional) — Filter conversations where any of these agents participated. Can not exceed 50 values.
- `visited_agent_branch_ids` (string, optional) — Filter conversations where any of these agent branches participated. Can not exceed 50 values.
- `call_successful` (enum, optional) — The result of the success evaluation
  - Allowed values: `success`, `failure`, `unknown`
- `call_start_before_unix` (integer, optional) — Unix timestamp (in seconds) to filter conversations up to this start date.
- `call_start_after_unix` (integer, optional) — Unix timestamp (in seconds) to filter conversations after to this start date.
- `call_duration_min_secs` (integer, optional) — Minimum call duration in seconds.
- `call_duration_max_secs` (integer, optional) — Maximum call duration in seconds.
- `rating_max` (integer, optional) — Maximum overall rating (1-5).
- `rating_min` (integer, optional) — Minimum overall rating (1-5).
- `has_feedback_comment` (boolean, optional) — Filter conversations with user feedback comments.
- `user_id` (string, optional) — Filter conversations by the user ID who initiated them.
- `evaluation_params` (string, optional) — Evaluation filters. Repeat param. Format: criteria_id:result. Example: eval=value_framing:success
- `data_collection_params` (string, optional) — Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in, pipe-delimit values.
- `data_collection_ids` (string, optional) — Data collection field IDs to include in each conversation summary. Repeat param. When omitted, data_collection_results is not returned.
- `evaluation_criteria_ids` (string, optional) — Evaluation criteria IDs to include in each conversation summary. Repeat param. When omitted, evaluation_criteria_results is not returned.
- `tool_names` (string, optional) — Filter conversations by tool names used during the call.
- `tool_names_successful` (string, optional) — Filter conversations by tool names that had successful calls.
- `tool_names_errored` (string, optional) — Filter conversations by tool names that had errored calls.
- `main_languages` (string, optional) — Filter conversations by detected main language (language code).
- `page_size` (integer, optional, default: 30) — How many conversations to return at maximum. Can not exceed 100, defaults to 30.
- `summary_mode` (enum, optional, default: exclude) — Whether to include transcript summaries in the response.
  - Allowed values: `exclude`, `include`
- `search` (string, optional, deprecated) — Full-text or fuzzy search over transcript messages
- `conversation_initiation_source` (enum, optional, default: unknown) — Enum representing the possible sources for conversation initiation.
  - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `text_only` (boolean, optional)
- `conversation_product_type` (enum, optional) — Restrict results to a single conversation product surface.
  - Allowed values: `agents`, `speech_engine`
- `branch_id` (string, optional) — Filter conversations by branch ID.
- `version_id` (string, optional) — Filter conversations by version ID.
- `parent_conversation_id` (string, optional) — Filter conversations by parent conversation ID for subagent conversations.
- `topic_ids` (string, optional) — Filter conversations by topic IDs assigned during topic discovery.
- `exclude_statuses` (enum, optional) — Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `tag_ids` (string, optional) — Filter conversations by conversation tag IDs assigned via the conversation-tags endpoints.
- `workflow_node_entered_id` (string, optional) — Filter conversations to only those that entered the given node.
- `termination_reasons` (string, optional) — Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.
- `guardrail_types` (enum, optional) — Filter to conversations where a guardrail of any of these types triggered (metadata.triggered_guardrails.guardrail_type). Repeat param to match any of several.
  - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
- `custom_guardrail_names` (string, optional) — Filter to conversations where a custom guardrail with any of these names triggered (metadata.triggered_guardrails.guardrail_name). Only custom guardrails carry a name. Repeat param to match any of several.

## Response

### 200

Successful Response

- `conversations` (list of object, required)
  - `agent_id` (string, required)
  - `conversation_id` (string, required)
  - `start_time_unix_secs` (integer, required)
  - `call_duration_secs` (integer, required)
  - `message_count` (integer, required)
  - `status` (enum, required)
    - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
  - `call_successful` (enum, required)
    - Allowed values: `success`, `failure`, `unknown`
  - `branch_id` (string, optional)
  - `version_id` (string, optional)
  - `agent_name` (string, optional)
  - `termination_reason` (string, optional, default: )
  - `call_success_score` (double, optional)
  - `transcript_summary` (string, optional)
  - `call_summary_title` (string, optional)
  - `main_language` (string, optional)
  - `conversation_initiation_source` (enum, optional, default: unknown) — Enum representing the possible sources for conversation initiation.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `tool_names` (list of string, optional)
  - `direction` (enum, optional, default: inbound)
    - Allowed values: `inbound`, `outbound`
  - `rating` (double, optional)
  - `sentiment_analysis` (object, optional)
    - `overall_label` (enum, required)
      - Allowed values: `positive`, `neutral`, `negative`
    - `overall_sentiment_score` (double, required)
    - `overall_frustration_score` (double, required)
    - `min_user_sentiment_score` (double, required)
    - `max_user_frustration_score` (double, required)
    - `num_scored_user_turns` (integer, required)
  - `data_collection_results` (map from string to any, optional)
  - `evaluation_criteria_results` (map from string to object, optional)
    - `result` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `score` (integer, optional)
    - `max_score` (integer, optional)
  - `tag_ids` (list of string, optional) — Conversation tag ids assigned to this conversation.
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

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
        customGuardrailNames: [
            "custom_guardrail_names",
        ],
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
        guardrailTypes: [
            "custom",
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
    custom_guardrail_names=[
        "custom_guardrail_names"
    ],
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
    guardrail_types=[
        "custom"
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

	url := "https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&custom_guardrail_names=%5B%22custom_guardrail_names%22%5D&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&guardrail_types=%5B%22custom%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&custom_guardrail_names=%5B%22custom_guardrail_names%22%5D&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&guardrail_types=%5B%22custom%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&custom_guardrail_names=%5B%22custom_guardrail_names%22%5D&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&guardrail_types=%5B%22custom%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&custom_guardrail_names=%5B%22custom_guardrail_names%22%5D&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&guardrail_types=%5B%22custom%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&custom_guardrail_names=%5B%22custom_guardrail_names%22%5D&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&guardrail_types=%5B%22custom%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations?agent_id=agent_id&branch_id=branch_id&call_duration_max_secs=1&call_duration_min_secs=1&call_start_after_unix=1&call_start_before_unix=1&call_successful=success&conversation_initiation_source=unknown&conversation_product_type=agents&cursor=cursor&custom_guardrail_names=%5B%22custom_guardrail_names%22%5D&data_collection_ids=%5B%22data_collection_ids%22%5D&data_collection_params=%5B%22data_collection_params%22%5D&evaluation_criteria_ids=%5B%22evaluation_criteria_ids%22%5D&evaluation_params=%5B%22evaluation_params%22%5D&exclude_statuses=%5B%22initiated%22%5D&guardrail_types=%5B%22custom%22%5D&has_feedback_comment=true&main_languages=%5B%22main_languages%22%5D&page_size=1&parent_conversation_id=parent_conversation_id&rating_max=1&rating_min=1&search=search&summary_mode=exclude&tag_ids=%5B%22tag_ids%22%5D&termination_reasons=%5B%22termination_reasons%22%5D&text_only=true&tool_names=%5B%22tool_names%22%5D&tool_names_errored=%5B%22tool_names_errored%22%5D&tool_names_successful=%5B%22tool_names_successful%22%5D&topic_ids=%5B%22topic_ids%22%5D&user_id=user_id&version_id=version_id&visited_agent_branch_ids=%5B%22visited_agent_branch_ids%22%5D&visited_agent_ids=%5B%22visited_agent_ids%22%5D&workflow_node_entered_id=workflow_node_entered_id")! as URL,
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
