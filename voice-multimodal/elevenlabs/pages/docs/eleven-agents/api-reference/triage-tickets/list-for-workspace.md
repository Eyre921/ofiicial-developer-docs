---
title: "List workspace tickets"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/list-for-workspace.md
path: docs/eleven-agents/api-reference/triage-tickets/list-for-workspace
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List workspace tickets

GET https://api.elevenlabs.io/v1/convai/triage-tickets

List conversation triage tickets across every agent in the workspace, ordered by most recently created first. Use this to build a workspace-wide view (for example, tickets assigned to the caller); for a single agent's tickets, use the per-agent endpoint instead. Tickets for agents the caller cannot access are omitted.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/list-for-workspace

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 100) — How many agent conversation tickets to return. Can not exceed 100.
- `status` (enum, optional) — Filter tickets by status.
  - Allowed values: `open`, `in_progress`, `resolved`, `merged`
- `assignee_user_id` (string, optional) — Filter tickets by assignee. Use 'unassigned' for tickets with no assignee.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `agent_conversation_tickets` (list of object, required)
  - `agentqa_ticket_id` (string, required)
  - `workspace_id` (string, required)
  - `owner_user_id` (string, required)
  - `agent_id` (string, required)
  - `needs_clustering` (boolean, required)
  - `labels` (list of string, required)
  - `conversation_ids` (list of string, required)
  - `ticket_comments` (list of object, required)
    - `comment` (string, required)
    - `created_at_unix_secs` (integer, required)
    - `owner_user_id` (string, optional)
  - `turn_comments` (list of object, required)
    - `turn_index` (integer, required)
    - `comment` (string, required)
    - `created_at_unix_secs` (integer, required)
    - `owner_user_id` (string, optional)
  - `status` (enum, required)
    - Allowed values: `open`, `in_progress`, `resolved`, `merged`
  - `source` (enum, required)
    - Allowed values: `qa`, `agent`, `manual`
  - `created_at_unix_secs` (integer, required)
  - `updated_at_unix_secs` (integer, required)
  - `issue_type` (enum, optional)
    - Allowed values: `knowledge_gap`, `incorrect_information`, `documentation_gap`, `product_feedback`, `platform_bug`, `tool_issue`, `missing_tool`, `unnecessary_escalation`, `wrong_action`
  - `first_seen_unix_secs` (integer, optional)
  - `last_seen_unix_secs` (integer, optional)
  - `qa_comment` (string, optional)
  - `assignee_user_id` (string, optional)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

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
      "source": "qa",
      "created_at_unix_secs": 1,
      "updated_at_unix_secs": 1,
      "issue_type": "knowledge_gap",
      "first_seen_unix_secs": 1,
      "last_seen_unix_secs": 1,
      "qa_comment": "qa_comment",
      "assignee_user_id": "assignee_user_id"
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.triageTickets.listForWorkspace({
        assigneeUserId: "assignee_user_id",
        cursor: "cursor",
        pageSize: 1,
        status: "open",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.triage_tickets.list_for_workspace(
    assignee_user_id="assignee_user_id",
    cursor="cursor",
    page_size=1,
    status="open",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets?assignee_user_id=assignee_user_id&cursor=cursor&page_size=1&status=open"

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets?assignee_user_id=assignee_user_id&cursor=cursor&page_size=1&status=open")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/triage-tickets?assignee_user_id=assignee_user_id&cursor=cursor&page_size=1&status=open")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/triage-tickets?assignee_user_id=assignee_user_id&cursor=cursor&page_size=1&status=open');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets?assignee_user_id=assignee_user_id&cursor=cursor&page_size=1&status=open");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets?assignee_user_id=assignee_user_id&cursor=cursor&page_size=1&status=open")! as URL,
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
