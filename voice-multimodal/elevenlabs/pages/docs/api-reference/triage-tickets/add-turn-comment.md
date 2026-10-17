---
title: "Add turn comment"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/add-turn-comment.md
path: docs/api-reference/triage-tickets/add-turn-comment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add turn comment

POST https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}/turn-comments
Content-Type: application/json

Append a turn-level comment to a ticket. Requires viewer access to the ticket's agent.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/add-turn-comment

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agentqa_ticket_id` (string, required)

### Body (application/json)

This endpoint expects an AddTurnCommentRequestModel.

- `turn_index` (integer, required) — Zero-based index of the transcript turn this comment refers to.
- `comment` (string, required) — What went wrong at this turn.

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
  "turn_index": 3,
  "comment": "The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base."
}
```

**Response**

```json
{
  "agentqa_ticket_id": "tkt_3f8a2b1c9d4e5f6a7b8c9d0e",
  "workspace_id": "ws_7a1b2c3d4e5f6a7b8c9d0e1f",
  "owner_user_id": "usr_a1b2c3d4e5f6a7b8c9d0e1f2",
  "agent_id": "agt_b2c3d4e5f6a7b8c9d0e1f2a3",
  "needs_clustering": false,
  "title": "Agent provides incorrect pricing information for Pro plan",
  "issue_type": "incorrect_information",
  "labels": [
    "pricing",
    "knowledge-base"
  ],
  "conversation_ids": [
    "conv_c3d4e5f6a7b8c9d0e1f2a3b4"
  ],
  "first_seen_unix_secs": 1718000000,
  "last_seen_unix_secs": 1718086400,
  "qa_comment": "This issue has been observed in multiple conversations. The agent consistently quotes the wrong price for the Pro plan.",
  "ticket_comments": [
    {
      "comment": "Confirmed this is a recurring issue across at least 5 conversations this week. Escalating priority.",
      "created_at_unix_secs": 1718050000,
      "owner_user_id": "usr_d4e5f6a7b8c9d0e1f2a3b4c5"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 3,
      "comment": "The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base.",
      "created_at_unix_secs": 1718086400,
      "owner_user_id": "usr_a1b2c3d4e5f6a7b8c9d0e1f2"
    }
  ],
  "status": "in_progress",
  "priority": "high",
  "priority_changes": [
    {
      "priority": "high",
      "changed_by_user_id": "usr_d4e5f6a7b8c9d0e1f2a3b4c5",
      "changed_at_unix_secs": 1718050000
    }
  ],
  "status_changes": [
    {
      "status": "in_progress",
      "changed_by_user_id": "usr_d4e5f6a7b8c9d0e1f2a3b4c5",
      "changed_at_unix_secs": 1718050000
    }
  ],
  "source": "qa",
  "assignee_user_id": "usr_e5f6a7b8c9d0e1f2a3b4c5d6",
  "created_at_unix_secs": 1718000000,
  "updated_at_unix_secs": 1718086400,
  "merged_into_ticket_id": null,
  "search_match": {
    "field": "turn_comment",
    "snippet": "...agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month...",
    "highlight_start": 7,
    "highlight_end": 47,
    "turn_index": 3
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments"

payload = {
    "turn_index": 3,
    "comment": "The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base."
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"turn_index":3,"comment":"The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base."}'
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments"

	payload := strings.NewReader("{\n  \"turn_index\": 3,\n  \"comment\": \"The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"turn_index\": 3,\n  \"comment\": \"The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments")
  .header("Content-Type", "application/json")
  .body("{\n  \"turn_index\": 3,\n  \"comment\": \"The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments', [
  'body' => '{
  "turn_index": 3,
  "comment": "The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"turn_index\": 3,\n  \"comment\": \"The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "turn_index": 3,
  "comment": "The agent provided incorrect pricing information at this turn, stating the Pro plan costs $49/month when it actually costs $99/month. This needs to be corrected in the knowledge base."
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments")! as URL,
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
