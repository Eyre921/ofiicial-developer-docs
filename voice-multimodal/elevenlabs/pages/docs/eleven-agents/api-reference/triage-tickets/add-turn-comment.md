---
title: "Add turn comment"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/add-turn-comment.md
path: docs/eleven-agents/api-reference/triage-tickets/add-turn-comment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add turn comment

POST https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}/turn-comments
Content-Type: application/json

Append a turn-level comment to a ticket. Requires viewer access to the ticket's agent.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/add-turn-comment

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

This endpoint expects an object.

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
- `labels` (list of string, required)
- `conversation_ids` (list of string, required)
- `ticket_comments` (list of TicketCommentResponseModel, required)
- `turn_comments` (list of TurnCommentResponseModel, required)
- `status` (enum, required)
  - Allowed values: `open`, `in_progress`, `resolved`, `cancelled`, `merged`
- `priority_changes` (list of TicketPriorityChangeResponseModel, required)
- `source` (enum, required)
  - Allowed values: `qa`, `agent`, `manual`
- `created_at_unix_secs` (integer, required)
- `updated_at_unix_secs` (integer, required)
- `title` (string, optional) — One-line headline for the ticket. None only on tickets created before titles existed.
- `issue_type` (enum, optional)
  - Allowed values: `knowledge_gap`, `incorrect_information`, `documentation_gap`, `product_feedback`, `platform_bug`, `tool_issue`, `missing_tool`, `unnecessary_escalation`, `wrong_action`
- `first_seen_unix_secs` (integer, optional)
- `last_seen_unix_secs` (integer, optional)
- `qa_comment` (string, optional)
- `priority` (enum, optional)
  - Allowed values: `low`, `medium`, `high`, `urgent`
- `merged_into_ticket_id` (string, optional) — The ticket this one was merged into, set while its status is 'merged'.
- `assignee_user_id` (string, optional)
- `search_match` (TicketSearchMatchResponseModel, optional) — Where the list's `search` query matched. Set only on searched lists.

## Errors

### 422 Triage Tickets Add Turn Comment Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### TicketCommentResponseModel

- `comment` (string, required)
- `created_at_unix_secs` (integer, required)
- `owner_user_id` (string, optional)

### TurnCommentResponseModel

- `turn_index` (integer, required)
- `comment` (string, required)
- `created_at_unix_secs` (integer, required)
- `owner_user_id` (string, optional)

### TicketPriorityChangeResponseModel

- `changed_by_user_id` (string, required)
- `changed_at_unix_secs` (integer, required)
- `priority` (enum, optional)
  - Allowed values: `low`, `medium`, `high`, `urgent`

### TicketSearchMatchResponseModel

- `field` (enum, required) — Which of the ticket's texts matched.
  - Allowed values: `title`, `description`, `comment`, `turn_comment`
- `snippet` (string, required) — Whitespace-collapsed excerpt around the match, with an ellipsis where it was cut.
- `highlight_start` (integer, required) — Offset of the match in `snippet`.
- `highlight_end` (integer, required) — Exclusive end offset of the match in `snippet`.
- `turn_index` (integer, optional) — The commented turn, set when `field` is 'turn_comment'.

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

## Examples

**Request**

```json
{
  "turn_index": 1,
  "comment": "comment"
}
```

**Response**

```json
{
  "agentqa_ticket_id": "agentqa_ticket_id",
  "workspace_id": "workspace_id",
  "owner_user_id": "owner_user_id",
  "agent_id": "agent_id",
  "needs_clustering": true,
  "labels": [
    "labels"
  ],
  "conversation_ids": [
    "conversation_ids"
  ],
  "ticket_comments": [
    {
      "comment": "comment",
      "created_at_unix_secs": 1,
      "owner_user_id": "owner_user_id"
    }
  ],
  "turn_comments": [
    {
      "turn_index": 1,
      "comment": "comment",
      "created_at_unix_secs": 1,
      "owner_user_id": "owner_user_id"
    }
  ],
  "status": "open",
  "priority_changes": [
    {
      "changed_by_user_id": "changed_by_user_id",
      "changed_at_unix_secs": 1,
      "priority": "low"
    }
  ],
  "source": "qa",
  "created_at_unix_secs": 1,
  "updated_at_unix_secs": 1,
  "title": "title",
  "issue_type": "knowledge_gap",
  "first_seen_unix_secs": 1,
  "last_seen_unix_secs": 1,
  "qa_comment": "qa_comment",
  "priority": "low",
  "merged_into_ticket_id": "merged_into_ticket_id",
  "assignee_user_id": "assignee_user_id",
  "search_match": {
    "field": "title",
    "snippet": "snippet",
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
    await client.conversationalAi.triageTickets.addTurnComment("agentqa_ticket_id", {
        turnIndex: 1,
        comment: "comment",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.triage_tickets.add_turn_comment(
    agentqa_ticket_id="agentqa_ticket_id",
    turn_index=1,
    comment="comment",
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments"

	payload := strings.NewReader("{\n  \"turn_index\": 1,\n  \"comment\": \"comment\"\n}")

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
request.body = "{\n  \"turn_index\": 1,\n  \"comment\": \"comment\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments")
  .header("Content-Type", "application/json")
  .body("{\n  \"turn_index\": 1,\n  \"comment\": \"comment\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/turn-comments', [
  'body' => '{
  "turn_index": 1,
  "comment": "comment"
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
request.AddParameter("application/json", "{\n  \"turn_index\": 1,\n  \"comment\": \"comment\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "turn_index": 1,
  "comment": "comment"
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
