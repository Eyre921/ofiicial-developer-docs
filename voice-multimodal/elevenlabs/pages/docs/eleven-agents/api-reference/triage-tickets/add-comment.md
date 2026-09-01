---
title: "Add comment"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/add-comment.md
path: docs/eleven-agents/api-reference/triage-tickets/add-comment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add comment

POST https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}/comments
Content-Type: application/json

Append a comment discussing how to resolve the ticket. Requires viewer access to the ticket's agent.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/triage-tickets/add-comment

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

- `comment` (string, required) — A comment discussing how to resolve the ticket.

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

## Examples

**Request**

```json
{
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
  "source": "qa",
  "created_at_unix_secs": 1,
  "updated_at_unix_secs": 1,
  "issue_type": "knowledge_gap",
  "first_seen_unix_secs": 1,
  "last_seen_unix_secs": 1,
  "qa_comment": "qa_comment",
  "assignee_user_id": "assignee_user_id"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.triageTickets.addComment("agentqa_ticket_id", {
        comment: "comment",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.triage_tickets.add_comment(
    agentqa_ticket_id="agentqa_ticket_id",
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/comments"

	payload := strings.NewReader("{\n  \"comment\": \"comment\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/comments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"comment\": \"comment\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/comments")
  .header("Content-Type", "application/json")
  .body("{\n  \"comment\": \"comment\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/comments', [
  'body' => '{
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/comments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"comment\": \"comment\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["comment": "comment"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets/agentqa_ticket_id/comments")! as URL,
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
