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
- `evaluation_params` (list of string, optional, nullable) — Evaluation filters. Repeat param. Format: criteria_id:result. Example: eval=value_framing:success
- `data_collection_params` (list of string, optional, nullable) — Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in, pipe-delimit values.
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

- `results` (list of object, required)
  - `conversation_id` (string, required)
  - `agent_id` (string, required)
  - `transcript_index` (integer, required)
  - `chunk_text` (string, required)
  - `score` (double, required)
  - `conversation_start_time_unix_secs` (integer, required)
  - `agent_name` (string, optional, nullable)
  - `chunk_highlights` (list of object, optional, nullable)
    - `value` (string, required)
    - `is_hit` (boolean, required)
- `has_more` (boolean, required) — Whether there are more results available
- `meta` (object, optional)
  - `total` (integer, optional, nullable)
  - `page` (integer, optional, nullable)
  - `page_size` (integer, optional, nullable)
- `next_cursor` (string, optional, nullable) — Cursor for the next page of results

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
