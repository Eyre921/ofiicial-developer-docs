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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.
- `agent_id` (string, optional, nullable) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `visited_agent_ids` (list of string, optional, nullable) — Filter conversations where any of these agents participated. Can not exceed 50 values.
- `visited_agent_branch_ids` (list of string, optional, nullable) — Filter conversations where any of these agent branches participated. Can not exceed 50 values.
- `call_successful` (enum, optional, nullable) — The result of the success evaluation
  - Allowed values: `success`, `failure`, `unknown`
- `call_start_before_unix` (integer, optional, nullable) — Unix timestamp (in seconds) to filter conversations up to this start date.
- `call_start_after_unix` (integer, optional, nullable) — Unix timestamp (in seconds) to filter conversations after to this start date.
- `call_duration_min_secs` (integer, optional, nullable) — Minimum call duration in seconds.
- `call_duration_max_secs` (integer, optional, nullable) — Maximum call duration in seconds.
- `rating_max` (integer, optional, nullable) — Maximum overall rating (1-5).
- `rating_min` (integer, optional, nullable) — Minimum overall rating (1-5).
- `has_feedback_comment` (boolean, optional, nullable) — Filter conversations with user feedback comments.
- `user_id` (string, optional, nullable) — Filter conversations by the user ID who initiated them.
- `evaluation_params` (list of string, optional, nullable) — Evaluation filters. Repeat param. Format: criteria_id:result. Example: eval=value_framing:success
- `data_collection_params` (list of string, optional, nullable) — Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in, pipe-delimit values.
- `data_collection_ids` (list of string, optional, nullable) — Data collection field IDs to include in each conversation summary. Repeat param. When omitted, data_collection_results is not returned.
- `evaluation_criteria_ids` (list of string, optional, nullable) — Evaluation criteria IDs to include in each conversation summary. Repeat param. When omitted, evaluation_criteria_results is not returned.
- `tool_names` (list of string, optional, nullable) — Filter conversations by tool names used during the call.
- `tool_names_successful` (list of string, optional, nullable) — Filter conversations by tool names that had successful calls.
- `tool_names_errored` (list of string, optional, nullable) — Filter conversations by tool names that had errored calls.
- `main_languages` (list of string, optional, nullable) — Filter conversations by detected main language (language code).
- `page_size` (integer, optional, default: 30) — How many conversations to return at maximum. Can not exceed 100, defaults to 30.
- `summary_mode` (enum, optional, default: exclude) — Whether to include transcript summaries in the response.
  - Allowed values: `exclude`, `include`
- `search` (string, optional, nullable, deprecated) — Full-text or fuzzy search over transcript messages
- `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Enum representing the possible sources for conversation initiation.
  - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `text_only` (boolean, optional, nullable)
- `conversation_product_type` (enum, optional, nullable) — Restrict results to a single conversation product surface.
  - Allowed values: `agents`, `speech_engine`
- `branch_id` (string, optional, nullable) — Filter conversations by branch ID.
- `version_id` (string, optional, nullable) — Filter conversations by version ID.
- `parent_conversation_id` (string, optional, nullable) — Filter conversations by parent conversation ID for subagent conversations.
- `topic_ids` (list of string, optional, nullable) — Filter conversations by topic IDs assigned during topic discovery.
- `exclude_statuses` (list of enum, optional, nullable) — Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `tag_ids` (list of string, optional, nullable) — Filter conversations by conversation tag IDs assigned via the conversation-tags endpoints.
- `workflow_node_entered_id` (string, optional, nullable) — Filter conversations to only those that entered the given node.
- `termination_reasons` (list of string, optional, nullable) — Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.
- `guardrail_types` (list of enum, optional, nullable) — Filter to conversations where a guardrail of any of these types triggered (metadata.triggered_guardrails.guardrail_type). Repeat param to match any of several.
  - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
- `custom_guardrail_names` (list of string, optional, nullable) — Filter to conversations where a custom guardrail with any of these names triggered (metadata.triggered_guardrails.guardrail_name). Only custom guardrails carry a name. Repeat param to match any of several.

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
  - `branch_id` (string, optional, nullable)
  - `version_id` (string, optional, nullable)
  - `agent_name` (string, optional, nullable)
  - `termination_reason` (string, optional, default: )
  - `call_success_score` (double, optional, nullable)
  - `transcript_summary` (string, optional, nullable)
  - `call_summary_title` (string, optional, nullable)
  - `main_language` (string, optional, nullable)
  - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Enum representing the possible sources for conversation initiation.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `tool_names` (list of string, optional, nullable)
  - `direction` (enum, optional, nullable, default: inbound)
    - Allowed values: `inbound`, `outbound`
  - `rating` (double, optional, nullable)
  - `sentiment_analysis` (object, optional, nullable)
    - `overall_label` (enum, required)
      - Allowed values: `positive`, `neutral`, `negative`
    - `overall_sentiment_score` (double, required)
    - `overall_frustration_score` (double, required)
    - `min_user_sentiment_score` (double, required)
    - `max_user_frustration_score` (double, required)
    - `num_scored_user_turns` (integer, required)
  - `data_collection_results` (map from string to any, optional, nullable)
  - `evaluation_criteria_results` (map from string to object, optional, nullable)
    - `result` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `score` (integer, optional, nullable)
    - `max_score` (integer, optional, nullable)
  - `tag_ids` (list of string, optional) — Conversation tag ids assigned to this conversation.
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

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
