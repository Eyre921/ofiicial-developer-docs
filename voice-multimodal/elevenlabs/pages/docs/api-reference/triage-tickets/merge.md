---
title: "Merge tickets"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/merge.md
path: docs/api-reference/triage-tickets/merge
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Merge tickets

POST https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}/merge
Content-Type: application/json

Merge other open tickets of the same agent into this pending, in-progress, or resolved one. Their conversations move onto this ticket, its priority is raised to the highest among them, and they are kept with status 'merged'. Requires viewer access to the ticket's agent.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/merge

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

This endpoint expects a MergeAgentConversationTicketsRequestModel.

- `source_ticket_ids` (list of string, required) — Open tickets of the same agent to fold into this one. They are kept with status 'merged', pointing at this ticket.

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
  "source_ticket_ids": [
    "tkt_01h9x2k4m7n3p8q5r6s9t0u1v2",
    "tkt_03j7y5l2n8o4q1r9s3t6u8v0w4"
  ]
}
```

**Response**

```json
{
  "agentqa_ticket_id": "tkt_09a1b2c3d4e5f6g7h8i9j0k1l2",
  "workspace_id": "ws_4f8e2a1b3c7d9e0f1a2b3c4d5e6f",
  "owner_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d",
  "agent_id": "agt_2b4d6f8a0c2e4f6a8b0c2d4e6f8a",
  "needs_clustering": false,
  "title": "Agent fails to retrieve account balance information from knowledge base",
  "issue_type": "knowledge_gap",
  "labels": [
    "billing",
    "knowledge-base"
  ],
  "conversation_ids": [
    "conv_1a2b3c4d5e6f7a8b9c0d1e2f3a4b",
    "conv_5e6f7a8b9c0d1e2f3a4b5c6d7e8f",
    "conv_9c0d1e2f3a4b5c6d7e8f9a0b1c2d"
  ],
  "first_seen_unix_secs": 1717200000,
  "last_seen_unix_secs": 1717372800,
  "qa_comment": "The agent consistently fails to answer questions about account balance retrieval. Knowledge base articles need to be updated with current API endpoints.",
  "ticket_comments": [
    {
      "comment": "Confirmed this issue affects multiple users. Escalating priority to high.",
      "created_at_unix_secs": 1717286400,
      "owner_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 3,
      "comment": "Agent incorrectly states that balance information is unavailable when it should be accessible via the billing tool.",
      "created_at_unix_secs": 1717243200,
      "owner_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d"
    }
  ],
  "status": "in_progress",
  "priority": "high",
  "priority_changes": [
    {
      "priority": "medium",
      "changed_by_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d",
      "changed_at_unix_secs": 1717200000
    },
    {
      "priority": "high",
      "changed_by_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d",
      "changed_at_unix_secs": 1717286400
    }
  ],
  "status_changes": [
    {
      "status": "open",
      "changed_by_user_id": null,
      "changed_at_unix_secs": 1717200000
    },
    {
      "status": "in_progress",
      "changed_by_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d",
      "changed_at_unix_secs": 1717243200
    }
  ],
  "source": "qa",
  "assignee_user_id": "usr_7c3d5e8f1a2b4c6d8e0f2a4b6c8d",
  "created_at_unix_secs": 1717200000,
  "updated_at_unix_secs": 1717372800,
  "merged_into_ticket_id": null,
  "search_match": {
    "field": "title",
    "snippet": "Agent fails to retrieve account balance information from knowledge base",
    "highlight_start": 22,
    "highlight_end": 37,
    "turn_index": null
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge"

payload = { "source_ticket_ids": ["tkt_01h9x2k4m7n3p8q5r6s9t0u1v2", "tkt_03j7y5l2n8o4q1r9s3t6u8v0w4"] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"source_ticket_ids":["tkt_01h9x2k4m7n3p8q5r6s9t0u1v2","tkt_03j7y5l2n8o4q1r9s3t6u8v0w4"]}'
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge"

	payload := strings.NewReader("{\n  \"source_ticket_ids\": [\n    \"tkt_01h9x2k4m7n3p8q5r6s9t0u1v2\",\n    \"tkt_03j7y5l2n8o4q1r9s3t6u8v0w4\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"source_ticket_ids\": [\n    \"tkt_01h9x2k4m7n3p8q5r6s9t0u1v2\",\n    \"tkt_03j7y5l2n8o4q1r9s3t6u8v0w4\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge")
  .header("Content-Type", "application/json")
  .body("{\n  \"source_ticket_ids\": [\n    \"tkt_01h9x2k4m7n3p8q5r6s9t0u1v2\",\n    \"tkt_03j7y5l2n8o4q1r9s3t6u8v0w4\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge', [
  'body' => '{
  "source_ticket_ids": [
    "tkt_01h9x2k4m7n3p8q5r6s9t0u1v2",
    "tkt_03j7y5l2n8o4q1r9s3t6u8v0w4"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"source_ticket_ids\": [\n    \"tkt_01h9x2k4m7n3p8q5r6s9t0u1v2\",\n    \"tkt_03j7y5l2n8o4q1r9s3t6u8v0w4\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["source_ticket_ids": ["tkt_01h9x2k4m7n3p8q5r6s9t0u1v2", "tkt_03j7y5l2n8o4q1r9s3t6u8v0w4"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge")! as URL,
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
