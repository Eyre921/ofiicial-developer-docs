---
title: "List tickets"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/list.md
path: docs/api-reference/triage-tickets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List tickets

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/triage-tickets

List an agent's conversation triage tickets, ordered by most recently created first unless sorted by priority. These are tickets about the agent's own performance on a conversation (for triage with Architect), not tickets an agent opens for end users.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required)

### Query parameters

- `page_size` (integer, optional, default: 100) — How many agent conversation tickets to return. Can not exceed 100.
- `conversation_id` (string, optional, nullable) — Filter tickets by conversation id.
- `status` (enum, optional, nullable) — Filter tickets by status.
  - Allowed values: `open`, `in_progress`, `resolved`, `cancelled`, `merged`
- `sources` (list of enum, optional, nullable) — Filter tickets by how they were raised (qa, agent, manual). Repeat the parameter to filter by multiple sources.
  - Allowed values: `qa`, `agent`, `manual`
- `priorities` (list of enum, optional, nullable) — Filter tickets by priority. Repeat the parameter to filter by multiple priorities.
  - Allowed values: `low`, `medium`, `high`, `urgent`
- `sort_by` (enum, optional) — Order by most recently created, or by priority (most urgent first, then most recently created).
  - Allowed values: `created_at`, `priority`
- `owner_user_id` (string, optional, nullable) — Filter tickets by creator. Use 'agent' for agent-raised tickets.
- `assignee_user_id` (string, optional, nullable) — Filter tickets by assignee. Use 'unassigned' for tickets with no assignee.
- `issue_type` (enum, optional, nullable) — Filter clusters by issue type.
  - Allowed values: `knowledge_gap`, `incorrect_information`, `documentation_gap`, `product_feedback`, `platform_bug`, `tool_issue`, `missing_tool`, `unnecessary_escalation`, `wrong_action`
- `label` (string, optional, nullable) — Filter tickets by an exact label.
- `merged_into_ticket_id` (string, optional, nullable) — Filter tickets merged into this ticket.
- `search` (string, optional, nullable) — Case-insensitive free-text search across the ticket's title, description, comments, and turn comments.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `agent_conversation_tickets` (list of AgentConversationTicketResponseModel, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AgentConversationTicketResponseModel

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

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

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

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "agent_conversation_tickets": [
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
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets")! as URL,
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
