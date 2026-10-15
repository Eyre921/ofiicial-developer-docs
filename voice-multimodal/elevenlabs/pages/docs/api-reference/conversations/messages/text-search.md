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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `text_query` (string, required) — The search query text for full-text and fuzzy matching
- `agent_id` (string, optional, nullable) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `visited_agent_ids` (list of string, optional, nullable) — Filter conversations where any of these agents participated. Can not exceed 50 values.
- `visited_agent_branch_ids` (list of string, optional, nullable) — Filter conversations where any of these agent branches participated. Can not exceed 50 values.
- `triggered_procedure_ids` (list of string, optional, nullable) — Filter conversations where any of these procedures were triggered. Can not exceed 50 values.
- `call_successful` (enum, optional, nullable) — The result of the success evaluation
  - Allowed values: `success`, `failure`, `unknown`, `error`
- `call_start_before_unix` (integer, optional, nullable) — Unix timestamp (in seconds) to filter conversations up to this start date.
- `call_start_after_unix` (integer, optional, nullable) — Unix timestamp (in seconds) to filter conversations after to this start date.
- `call_duration_min_secs` (integer, optional, nullable) — Minimum call duration in seconds.
- `call_duration_max_secs` (integer, optional, nullable) — Maximum call duration in seconds.
- `rating_max` (integer, optional, nullable) — Maximum overall rating (1-5).
- `rating_min` (integer, optional, nullable) — Minimum overall rating (1-5).
- `has_feedback_comment` (boolean, optional, nullable) — Filter conversations with user feedback comments.
- `user_id` (string, optional, nullable) — Filter conversations by the user ID who initiated them.
- `evaluation_params` (list of string, optional, nullable) — Evaluation filters. Repeat param. Format: criteria_id:result where result is one of success|failure|unknown. Example: eval=value_framing:success
- `data_collection_params` (list of string, optional, nullable) — Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in. For in, pipe-delimit values. An empty value matches conversations where the field was not collected (id:eq:), and neq with an empty value matches where it was (id:neq:). eq is exact equality. gt|gte|lt|lte require a numeric value.
- `dynamic_variable_params` (list of string, optional, nullable) — Dynamic variable filters. Repeat param. Format: name:op:value where op is one of eq|neq|gt|gte|lt|lte|in. For in, pipe-delimit values. An empty value matches conversations where the variable was not set (name:eq:), and neq with an empty value matches where it was (name:neq:). eq is exact equality. gt|gte|lt|lte require a numeric value. Names containing ':' cannot be expressed.
- `tool_names` (list of string, optional, nullable) — Filter conversations by tool names used during the call.
- `tool_names_successful` (list of string, optional, nullable) — Filter conversations by tool names that had successful calls.
- `tool_names_errored` (list of string, optional, nullable) — Filter conversations by tool names that had errored calls.
- `include_invalid_tool_calls` (boolean, optional, default: false) — Also match tool calls that never ran.
- `main_languages` (list of string, optional, nullable) — Filter conversations by detected main language (language code).
- `exclude_statuses` (list of enum, optional, nullable) — Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `termination_reasons` (list of string, optional, nullable) — Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.
- `page_size` (integer, optional, default: 20) — Number of results per page. Max 50.
- `summary_mode` (enum, optional, default: exclude) — Whether to include transcript summaries in the response.
  - Allowed values: `exclude`, `include`
- `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Enum representing the possible sources for conversation initiation.
  - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `text_only` (boolean, optional, nullable)
- `conversation_product_type` (enum, optional, nullable) — Restrict results to a single conversation product surface.
  - Allowed values: `agents`, `speech_engine`
- `branch_id` (string, optional, nullable) — Filter conversations by branch ID.
- `version_id` (string, optional, nullable) — Filter conversations by version ID.
- `topic_ids` (list of string, optional, nullable) — Filter conversations by topic IDs assigned during topic discovery.
- `sort_by` (enum, optional) — Sort order for search results. 'search_score' sorts by search score, 'created_at' sorts by conversation start time.
  - Allowed values: `search_score`, `created_at`
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `results` (list of MessagesSearchResult, required)
- `has_more` (boolean, required) — Whether there are more results available
- `meta` (ListResponseMeta, optional)
- `next_cursor` (string, optional, nullable) — Cursor for the next page of results

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### MessagesSearchResult

transcript_index: index of the message in the conversation transcript chunk_text: text of the transcript; transcript messages if very long could have several chunks. chunk_highlights: chunk_text split into matched/unmatched segments for highlighting. Only populated for keyword/text search, not semantic search. score: similarity score of the message to the search query

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `transcript_index` (integer, required)
- `chunk_text` (string, required)
- `score` (double, required)
- `conversation_start_time_unix_secs` (integer, required)
- `agent_name` (string, optional, nullable)
- `chunk_highlights` (list of SearchHighlightSegment, optional, nullable)

### ListResponseMeta

- `total` (integer, optional, nullable)
- `page` (integer, optional, nullable)
- `page_size` (integer, optional, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### SearchHighlightSegment

- `value` (string, required)
- `is_hit` (boolean, required)

### ValidationErrorLocItems

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
      "conversation_id": "conv_9f8e7d6c5b4a3210fedcba9876543210",
      "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "transcript_index": 12,
      "chunk_text": "I understand your concern about the refund policy. Let me explain how it works.",
      "score": 0.95,
      "conversation_start_time_unix_secs": 1689004800,
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
  "next_cursor": "eyJwYWdlIjoyLCJpZCI6Ijc4OTAxMiJ9"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search"

querystring = {"agent_id":"agent_3701k3ttaq12ewp8b7qv5rfyszkz","branch_id":"branch_1234abcd5678efgh","call_duration_max_secs":"3600","call_duration_min_secs":"60","call_start_after_unix":"1600000000","call_start_before_unix":"1700000000","call_successful":"success","conversation_initiation_source":"twilio","conversation_product_type":"agents","cursor":"eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9","data_collection_params":"[\"location:eq:US\",\"device:neq:mobile\",\"duration:gte:120\"]","dynamic_variable_params":"[\"customer_type:eq:premium\",\"issue_severity:lt:3\"]","evaluation_params":"[\"value_framing:success\",\"tone:failure\"]","exclude_statuses":"[\"in-progress\",\"processing\"]","has_feedback_comment":"true","include_invalid_tool_calls":"false","main_languages":"[\"en\",\"es\"]","page_size":"20","rating_max":"5","rating_min":"3","sort_by":"search_score","summary_mode":"include","termination_reasons":"[\"customer_hangup\",\"agent_disconnect\"]","text_only":"true","text_query":"refund policy","tool_names":"[\"sentiment_analysis\",\"call_transcription\"]","tool_names_errored":"[\"call_transcription\"]","tool_names_successful":"[\"sentiment_analysis\"]","topic_ids":"[\"topic_abc123\",\"topic_def456\"]","triggered_procedure_ids":"[\"proc_1234567890abcdef\"]","user_id":"user_abc123xyz789","version_id":"v1.2.3","visited_agent_branch_ids":"[\"branch_9f8e7d6c5b4a3210fedcba9876543210\"]","visited_agent_ids":"[\"agent_3701k3ttaq12ewp8b7qv5rfyszkz\",\"agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b\"]"}

payload = {}
headers = {
    "xi-api-key": "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D';
const options = {
  method: 'GET',
  headers: {
    'xi-api-key': 'sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c',
    'Content-Type': 'application/json'
  },
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D")
  .header("xi-api-key", "sk_live_4f3b2a1c9d8e7f6a5b4c3d2e1f0a9b8c")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D', [
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/text-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_1234abcd5678efgh&call_duration_max_secs=3600&call_duration_min_secs=60&call_start_after_unix=1600000000&call_start_before_unix=1700000000&call_successful=success&conversation_initiation_source=twilio&conversation_product_type=agents&cursor=eyJwYWdlIjoxLCJpZCI6IjEyMzQ1NiJ9&data_collection_params=%5B%22location%3Aeq%3AUS%22%2C%22device%3Aneq%3Amobile%22%2C%22duration%3Agte%3A120%22%5D&dynamic_variable_params=%5B%22customer_type%3Aeq%3Apremium%22%2C%22issue_severity%3Alt%3A3%22%5D&evaluation_params=%5B%22value_framing%3Asuccess%22%2C%22tone%3Afailure%22%5D&exclude_statuses=%5B%22in-progress%22%2C%22processing%22%5D&has_feedback_comment=true&include_invalid_tool_calls=false&main_languages=%5B%22en%22%2C%22es%22%5D&page_size=20&rating_max=5&rating_min=3&sort_by=search_score&summary_mode=include&termination_reasons=%5B%22customer_hangup%22%2C%22agent_disconnect%22%5D&text_only=true&text_query=refund+policy&tool_names=%5B%22sentiment_analysis%22%2C%22call_transcription%22%5D&tool_names_errored=%5B%22call_transcription%22%5D&tool_names_successful=%5B%22sentiment_analysis%22%5D&topic_ids=%5B%22topic_abc123%22%2C%22topic_def456%22%5D&triggered_procedure_ids=%5B%22proc_1234567890abcdef%22%5D&user_id=user_abc123xyz789&version_id=v1.2.3&visited_agent_branch_ids=%5B%22branch_9f8e7d6c5b4a3210fedcba9876543210%22%5D&visited_agent_ids=%5B%22agent_3701k3ttaq12ewp8b7qv5rfyszkz%22%2C%22agent_48f9d2b7c1a34e6f9a2b7c3d4e5f6a7b%22%5D")! as URL,
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
