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
    "string"
  ]
}
```

**Response**

```json
{
  "agentqa_ticket_id": "string",
  "workspace_id": "string",
  "owner_user_id": "string",
  "agent_id": "string",
  "needs_clustering": true,
  "title": "string",
  "issue_type": "knowledge_gap",
  "labels": [
    "string"
  ],
  "conversation_ids": [
    "string"
  ],
  "first_seen_unix_secs": 1,
  "last_seen_unix_secs": 1,
  "qa_comment": "string",
  "ticket_comments": [
    {
      "comment": "string",
      "created_at_unix_secs": 1,
      "owner_user_id": "string"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 1,
      "comment": "string",
      "created_at_unix_secs": 1,
      "owner_user_id": "string"
    }
  ],
  "status": "open",
  "priority": "low",
  "priority_changes": [
    {
      "priority": "low",
      "changed_by_user_id": "string",
      "changed_at_unix_secs": 1
    }
  ],
  "source": "qa",
  "assignee_user_id": "string",
  "created_at_unix_secs": 1,
  "updated_at_unix_secs": 1,
  "merged_into_ticket_id": "string",
  "search_match": {
    "field": "title",
    "snippet": "string",
    "highlight_start": 1,
    "highlight_end": 1,
    "turn_index": 1
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.triageTickets.merge("agentqa_ticket_id", {
        sourceTicketIds: [
            "string",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.triage_tickets.merge(
    agentqa_ticket_id="agentqa_ticket_id",
    source_ticket_ids=[
        "string"
    ],
)

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

	payload := strings.NewReader("{\n  \"source_ticket_ids\": [\n    \"string\"\n  ]\n}")

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
request.body = "{\n  \"source_ticket_ids\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge")
  .header("Content-Type", "application/json")
  .body("{\n  \"source_ticket_ids\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/merge', [
  'body' => '{
  "source_ticket_ids": [
    "string"
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
request.AddParameter("application/json", "{\n  \"source_ticket_ids\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["source_ticket_ids": ["string"]] as [String : Any]

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
