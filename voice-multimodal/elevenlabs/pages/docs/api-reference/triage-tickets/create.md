---
title: "Create conversation ticket"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/create.md
path: docs/api-reference/triage-tickets/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create conversation ticket

POST https://api.elevenlabs.io/v1/convai/triage-tickets
Content-Type: application/json

Raise a ticket about an agent's performance on a conversation, for triage with Architect. Provide an overall comment and/or turn-level comments describing what went wrong.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

This endpoint expects a CreateAgentConversationTicketRequestModel.

- `conversation_id` (string, required) — Conversation this ticket is about.
- `title` (string, optional, nullable) — One-line headline shown in the triage list. Defaults to one derived from the comments, falling back to the conversation's summary title. Ignored when the comment is added to the conversation's open ticket.
- `qa_comment` (string, optional, nullable) — The issue this ticket is about, covering the whole conversation rather than a single turn.
- `turn_comments` (list of TurnCommentRequestModel, optional) — Optional turn-level comments on what went wrong.
- `priority` (enum, optional, nullable) — How urgently the ticket needs attention. If the conversation already has an open ticket, it is raised to this priority when lower.
  - Allowed values: `low`, `medium`, `high`, `urgent`

## Response

### 200

Successful Response

- `agentqa_ticket_id` (string, required)
- `workspace_id` (string, required)
- `owner_user_id` (string, required)
- `agent_id` (string, required)
- `needs_clustering` (boolean, required)
- `title` (string, required, nullable) — One-line headline for the ticket. None only on tickets created before titles existed.
- `issue_type` (enum, required, nullable)
  - Allowed values: `knowledge_gap`, `incorrect_information`, `documentation_gap`, `product_feedback`, `platform_bug`, `tool_issue`, `missing_tool`, `unnecessary_escalation`, `wrong_action`
- `labels` (list of string, required)
- `conversation_ids` (list of string, required)
- `first_seen_unix_secs` (integer, required, nullable)
- `last_seen_unix_secs` (integer, required, nullable)
- `qa_comment` (string, required, nullable)
- `ticket_comments` (list of TicketCommentResponseModel, required)
- `turn_comments` (list of TurnCommentResponseModel, required)
- `status` (enum, required)
  - Allowed values: `open`, `in_progress`, `resolved`, `cancelled`, `merged`
- `priority` (enum, required, nullable)
  - Allowed values: `low`, `medium`, `high`, `urgent`
- `priority_changes` (list of TicketPriorityChangeResponseModel, required)
- `status_changes` (list of TicketStatusChangeResponseModel, required)
- `source` (enum, required)
  - Allowed values: `qa`, `agent`, `manual`
- `assignee_user_id` (string, required, nullable)
- `created_at_unix_secs` (integer, required)
- `updated_at_unix_secs` (integer, required)
- `merged_into_ticket_id` (string, optional, nullable) — The ticket this one was merged into, set while its status is 'merged'.
- `search_match` (TicketSearchMatchResponseModel, optional, nullable) — Where the list's `search` query matched. Set only on searched lists.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### TurnCommentRequestModel

- `turn_index` (integer, required) — Zero-based index of the transcript turn this comment refers to.
- `comment` (string, required) — What went wrong at this turn.

### TicketCommentResponseModel

- `comment` (string, required)
- `created_at_unix_secs` (integer, required)
- `owner_user_id` (string, required, nullable)

### TurnCommentResponseModel

- `turn_index` (integer, required)
- `comment` (string, required)
- `created_at_unix_secs` (integer, required)
- `owner_user_id` (string, required, nullable)

### TicketPriorityChangeResponseModel

- `priority` (enum, required, nullable)
  - Allowed values: `low`, `medium`, `high`, `urgent`
- `changed_by_user_id` (string, required)
- `changed_at_unix_secs` (integer, required)

### TicketStatusChangeResponseModel

- `status` (enum, required)
  - Allowed values: `open`, `in_progress`, `resolved`, `cancelled`, `merged`
- `changed_by_user_id` (string, required, nullable)
- `changed_at_unix_secs` (integer, required)

### TicketSearchMatchResponseModel

- `field` (enum, required) — Which of the ticket's texts matched.
  - Allowed values: `title`, `description`, `comment`, `turn_comment`
- `snippet` (string, required) — Whitespace-collapsed excerpt around the match, with an ellipsis where it was cut.
- `highlight_start` (integer, required) — Offset of the match in `snippet`.
- `highlight_end` (integer, required) — Exclusive end offset of the match in `snippet`.
- `turn_index` (integer, optional, nullable) — The commented turn, set when `field` is 'turn_comment'.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{
  "conversation_id": "conv_3f8a2b1c9d4e5f6a7b8c9d0e"
}
```

**Response**

```json
{
  "agentqa_ticket_id": "ticket_7d4e2f1a3b5c8d9e0f1a2b3c",
  "workspace_id": "ws_1a2b3c4d5e6f7a8b9c0d1e2f",
  "owner_user_id": "user_9c8b7a6f5e4d3c2b1a0f9e8d",
  "agent_id": "agent_4f3e2d1c0b9a8f7e6d5c4b3a",
  "needs_clustering": true,
  "title": "Agent provided incorrect refund policy information",
  "issue_type": "knowledge_gap",
  "labels": [
    "refund-policy"
  ],
  "conversation_ids": [
    "conv_3f8a2b1c9d4e5f6a7b8c9d0e"
  ],
  "first_seen_unix_secs": 1718000000,
  "last_seen_unix_secs": 1718003600,
  "qa_comment": "The agent incorrectly stated that refunds take 3-5 business days when the actual policy is 7-10 business days. This caused customer confusion and a follow-up complaint.",
  "ticket_comments": [
    {
      "comment": "Confirmed the agent's knowledge base entry for refund timelines is outdated. Needs to be updated to reflect the current 7-10 business day policy.",
      "created_at_unix_secs": 1718004200,
      "owner_user_id": "user_9c8b7a6f5e4d3c2b1a0f9e8d"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 4,
      "comment": "Agent stated '3-5 business days' for refund processing, which contradicts the current policy of 7-10 business days.",
      "created_at_unix_secs": 1718004200,
      "owner_user_id": "user_9c8b7a6f5e4d3c2b1a0f9e8d"
    }
  ],
  "status": "open",
  "priority": "high",
  "priority_changes": [
    {
      "priority": "high",
      "changed_by_user_id": "user_9c8b7a6f5e4d3c2b1a0f9e8d",
      "changed_at_unix_secs": 1718004500
    }
  ],
  "status_changes": [
    {
      "status": "open",
      "changed_by_user_id": "user_9c8b7a6f5e4d3c2b1a0f9e8d",
      "changed_at_unix_secs": 1718004200
    }
  ],
  "source": "qa",
  "assignee_user_id": "user_2a3b4c5d6e7f8a9b0c1d2e3f",
  "created_at_unix_secs": 1718004200,
  "updated_at_unix_secs": 1718004500,
  "merged_into_ticket_id": null,
  "search_match": {
    "field": "title",
    "snippet": "Agent provided incorrect refund policy information",
    "highlight_start": 25,
    "highlight_end": 38,
    "turn_index": null
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/triage-tickets"

payload = { "conversation_id": "conv_3f8a2b1c9d4e5f6a7b8c9d0e" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/triage-tickets';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"conversation_id":"conv_3f8a2b1c9d4e5f6a7b8c9d0e"}'
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets"

	payload := strings.NewReader("{\n  \"conversation_id\": \"conv_3f8a2b1c9d4e5f6a7b8c9d0e\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"conversation_id\": \"conv_3f8a2b1c9d4e5f6a7b8c9d0e\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets")
  .header("Content-Type", "application/json")
  .body("{\n  \"conversation_id\": \"conv_3f8a2b1c9d4e5f6a7b8c9d0e\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets', [
  'body' => '{
  "conversation_id": "conv_3f8a2b1c9d4e5f6a7b8c9d0e"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"conversation_id\": \"conv_3f8a2b1c9d4e5f6a7b8c9d0e\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["conversation_id": "conv_3f8a2b1c9d4e5f6a7b8c9d0e"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
