---
title: "Create manual ticket"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/create-manual.md
path: docs/api-reference/triage-tickets/create-manual
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create manual ticket

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/triage-tickets
Content-Type: application/json

Manually raise a follow-up ticket against an agent, not tied to any conversation (for example a task like 'add the KB about X'). Without a title, one is derived from the comment. Requires viewer access to the agent.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/create-manual

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required)

### Body (application/json)

This endpoint expects a CreateManualTicketRequestModel.

- `qa_comment` (string, required) — What the ticket is about, e.g. a follow-up task for the agent.
- `title` (string, optional, nullable) — One-line headline shown in the triage list. Defaults to one derived from qa_comment.
- `priority` (enum, optional, nullable) — How urgently the ticket needs attention.
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
{
  "qa_comment": "Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request."
}
```

**Response**

```json
{
  "agentqa_ticket_id": "tkt_3f8a2b1c9d4e5f6a7b8c9d0e",
  "workspace_id": "ws_a1b2c3d4e5f6g7h8i9j0k1l2",
  "owner_user_id": "usr_9k8j7h6g5f4e3d2c1b0a9z8y",
  "agent_id": "agt_c4d5e6f7a8b9c0d1e2f3a4b5",
  "needs_clustering": false,
  "title": "Add KB article on refund policy and return request process",
  "issue_type": "knowledge_gap",
  "labels": [
    "knowledge-base"
  ],
  "conversation_ids": [
    "conv_1a2b3c4d5e6f7g8h9i0j1k2l"
  ],
  "first_seen_unix_secs": 1718000000,
  "last_seen_unix_secs": 1718003600,
  "qa_comment": "Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request.",
  "ticket_comments": [
    {
      "comment": "This has been flagged multiple times in recent conversations. Prioritizing for next sprint.",
      "created_at_unix_secs": 1718004200,
      "owner_user_id": "usr_9k8j7h6g5f4e3d2c1b0a9z8y"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 3,
      "comment": "Agent failed to provide refund policy details here.",
      "created_at_unix_secs": 1718001800,
      "owner_user_id": "usr_9k8j7h6g5f4e3d2c1b0a9z8y"
    }
  ],
  "status": "open",
  "priority": "medium",
  "priority_changes": [
    {
      "priority": "medium",
      "changed_by_user_id": "usr_9k8j7h6g5f4e3d2c1b0a9z8y",
      "changed_at_unix_secs": 1718004500
    }
  ],
  "status_changes": [
    {
      "status": "open",
      "changed_by_user_id": "usr_9k8j7h6g5f4e3d2c1b0a9z8y",
      "changed_at_unix_secs": 1718000100
    }
  ],
  "source": "manual",
  "assignee_user_id": "usr_2m3n4o5p6q7r8s9t0u1v2w3x",
  "created_at_unix_secs": 1718000100,
  "updated_at_unix_secs": 1718004500,
  "merged_into_ticket_id": null,
  "search_match": {
    "field": "title",
    "snippet": "Add KB article on refund policy and return request process",
    "highlight_start": 10,
    "highlight_end": 22,
    "turn_index": null
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets"

payload = { "qa_comment": "Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request." }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"qa_comment":"Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request."}'
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets"

	payload := strings.NewReader("{\n  \"qa_comment\": \"Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"qa_comment\": \"Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets")
  .header("Content-Type", "application/json")
  .body("{\n  \"qa_comment\": \"Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets', [
  'body' => '{
  "qa_comment": "Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"qa_comment\": \"Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["qa_comment": "Add a knowledge base article covering our refund policy and the steps users need to follow to initiate a return request."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets")! as URL,
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
