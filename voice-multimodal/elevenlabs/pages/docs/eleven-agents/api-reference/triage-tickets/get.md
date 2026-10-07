---
title: "Get ticket"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/get.md
path: docs/eleven-agents/api-reference/triage-tickets/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get ticket

GET https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}

Get an agent conversation ticket by ID.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agentqa_ticket_id` (string, required)

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

### 422 Triage Tickets Get Request Unprocessable Entity Error

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

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id';
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id")! as URL,
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
