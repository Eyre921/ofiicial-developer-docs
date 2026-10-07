---
title: "List tickets"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/list.md
path: docs/eleven-agents/api-reference/triage-tickets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List tickets

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/triage-tickets

List an agent's conversation triage tickets, ordered by most recently created first unless sorted by priority. These are tickets about the agent's own performance on a conversation (for triage with Architect), not tickets an agent opens for end users.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/list

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
- `conversation_id` (string, optional) — Filter tickets by conversation id.
- `status` (enum, optional) — Filter tickets by status.
  - Allowed values: `open`, `in_progress`, `resolved`, `cancelled`, `merged`
- `sources` (enum, optional) — Filter tickets by how they were raised (qa, agent, manual). Repeat the parameter to filter by multiple sources.
  - Allowed values: `qa`, `agent`, `manual`
- `priorities` (enum, optional) — Filter tickets by priority. Repeat the parameter to filter by multiple priorities.
  - Allowed values: `low`, `medium`, `high`, `urgent`
- `sort_by` (enum, optional) — Order by most recently created, or by priority (most urgent first, then most recently created).
  - Allowed values: `created_at`, `priority`
- `owner_user_id` (string, optional) — Filter tickets by creator. Use 'agent' for agent-raised tickets.
- `assignee_user_id` (string, optional) — Filter tickets by assignee. Use 'unassigned' for tickets with no assignee.
- `issue_type` (enum, optional) — Filter clusters by issue type.
  - Allowed values: `knowledge_gap`, `incorrect_information`, `documentation_gap`, `product_feedback`, `platform_bug`, `tool_issue`, `missing_tool`, `unnecessary_escalation`, `wrong_action`
- `label` (string, optional) — Filter tickets by an exact label.
- `merged_into_ticket_id` (string, optional) — Filter tickets merged into this ticket.
- `search` (string, optional) — Case-insensitive free-text search across the ticket's title, description, comments, and turn comments.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `agent_conversation_tickets` (list of AgentConversationTicketResponseModel, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Errors

### 422 Triage Tickets List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AgentConversationTicketResponseModel

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

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

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

### ValidationErrorLocItem

## Examples

**Response**

```json
{
  "agent_conversation_tickets": [
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
          "owner_user_id": null
        }
      ],
      "turn_comments": [
        {
          "turn_index": 1,
          "comment": "comment",
          "created_at_unix_secs": 1,
          "owner_user_id": null
        }
      ],
      "status": "open",
      "priority_changes": [
        {
          "changed_by_user_id": "changed_by_user_id",
          "changed_at_unix_secs": 1,
          "priority": null
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
        "highlight_end": 1
      }
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets"

querystring = {"assignee_user_id":"assignee_user_id","conversation_id":"conversation_id","cursor":"cursor","issue_type":"knowledge_gap","label":"label","merged_into_ticket_id":"merged_into_ticket_id","owner_user_id":"owner_user_id","page_size":"1","priorities":"[\"low\"]","search":"search","sort_by":"created_at","sources":"[\"qa\"]","status":"open"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open';
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/triage-tickets?assignee_user_id=assignee_user_id&conversation_id=conversation_id&cursor=cursor&issue_type=knowledge_gap&label=label&merged_into_ticket_id=merged_into_ticket_id&owner_user_id=owner_user_id&page_size=1&priorities=%5B%22low%22%5D&search=search&sort_by=created_at&sources=%5B%22qa%22%5D&status=open")! as URL,
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
