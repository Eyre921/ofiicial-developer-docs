---
title: "Update ticket"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/update.md
path: docs/api-reference/triage-tickets/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update ticket

PATCH https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}
Content-Type: application/json

Update a ticket's title, comment, status, priority, and/or assignee. Requires editor access to the ticket's agent.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/update

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

This endpoint expects a PatchAgentConversationTicketRequestModel.

- `title` (string, optional, nullable) — If provided, updates the ticket title. Omit to leave unchanged.
- `status` (enum, optional, nullable) — If provided, updates the ticket status. Omit to leave unchanged.
  - Allowed values: `open`, `in_progress`, `resolved`, `cancelled`, `merged`
- `assignee_user_id` (string, optional, nullable) — If provided, updates who is responsible for resolving this ticket. Must be a workspace member with at least viewer access to the agent. Pass null to unassign. Omit to leave unchanged.
- `priority` (enum, optional, nullable) — If provided, updates how urgently the ticket needs attention. Pass null to clear it. Omit to leave unchanged.
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
{}
```

**Response**

```json
{
  "agentqa_ticket_id": "tkt_01h9x2k4m7n3p8q5r6s9t0u1v2",
  "workspace_id": "wsp_3f8a2b1c9d4e5f6a7b8c9d0e1f2",
  "owner_user_id": "usr_7a3b2c1d9e4f5a6b7c8d9e0f1a2",
  "agent_id": "agt_5c4d3e2f1a0b9c8d7e6f5a4b3c2",
  "needs_clustering": false,
  "title": "Agent fails to answer questions about pricing plans",
  "issue_type": "knowledge_gap",
  "labels": [
    "pricing",
    "knowledge-base"
  ],
  "conversation_ids": [
    "conv_1a2b3c4d5e6f7a8b9c0d1e2f3a4b",
    "conv_9z8y7x6w5v4u3t2s1r0q9p8o7n6m"
  ],
  "first_seen_unix_secs": 1718000000,
  "last_seen_unix_secs": 1718345600,
  "qa_comment": "The agent consistently fails to provide accurate pricing information when users ask about enterprise plans.",
  "ticket_comments": [
    {
      "comment": "Confirmed this is a recurring issue across multiple conversations. The knowledge base needs to be updated with the latest pricing tiers.",
      "created_at_unix_secs": 1718100000,
      "owner_user_id": "usr_7a3b2c1d9e4f5a6b7c8d9e0f1a2"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 3,
      "comment": "Agent incorrectly quoted the starter plan price as $29/month instead of $39/month.",
      "created_at_unix_secs": 1718050000,
      "owner_user_id": "usr_7a3b2c1d9e4f5a6b7c8d9e0f1a2"
    }
  ],
  "status": "in_progress",
  "priority": "high",
  "priority_changes": [
    {
      "priority": "medium",
      "changed_by_user_id": "usr_7a3b2c1d9e4f5a6b7c8d9e0f1a2",
      "changed_at_unix_secs": 1718010000
    },
    {
      "priority": "high",
      "changed_by_user_id": "usr_4d5e6f7a8b9c0d1e2f3a4b5c6d7e",
      "changed_at_unix_secs": 1718200000
    }
  ],
  "status_changes": [
    {
      "status": "open",
      "changed_by_user_id": "usr_7a3b2c1d9e4f5a6b7c8d9e0f1a2",
      "changed_at_unix_secs": 1718000000
    },
    {
      "status": "in_progress",
      "changed_by_user_id": "usr_4d5e6f7a8b9c0d1e2f3a4b5c6d7e",
      "changed_at_unix_secs": 1718250000
    }
  ],
  "source": "qa",
  "assignee_user_id": "usr_4d5e6f7a8b9c0d1e2f3a4b5c6d7e",
  "created_at_unix_secs": 1718000000,
  "updated_at_unix_secs": 1718345600,
  "merged_into_ticket_id": null,
  "search_match": {
    "field": "title",
    "snippet": "Agent fails to answer questions about pricing plans",
    "highlight_start": 0,
    "highlight_end": 49,
    "turn_index": null
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id';
const options = {method: 'PATCH', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
