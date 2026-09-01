---
title: "Create conversation ticket"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/create.md
path: docs/api-reference/triage-tickets/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create conversation ticket

POST https://api.elevenlabs.io/v1/convai/triage-tickets
Content-Type: application/json

Raise a ticket about an agent's performance on a conversation, for triage with Architect. Provide an overall comment and/or turn-level comments describing what went wrong.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `conversation_id` (string, required) — Conversation this ticket is about.
- `qa_comment` (string, optional, nullable) — The QA finding covering the whole conversation.
- `turn_comments` (list of object, optional) — Optional turn-level comments on what went wrong.
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
- `issue_type` (enum, required, nullable)
  - Allowed values: `knowledge_gap`, `incorrect_information`, `documentation_gap`, `product_feedback`, `platform_bug`, `tool_issue`, `missing_tool`, `unnecessary_escalation`, `wrong_action`
- `labels` (list of string, required)
- `conversation_ids` (list of string, required)
- `first_seen_unix_secs` (integer, required, nullable)
- `last_seen_unix_secs` (integer, required, nullable)
- `qa_comment` (string, required, nullable)
- `ticket_comments` (list of object, required)
  - `comment` (string, required)
  - `created_at_unix_secs` (integer, required)
  - `owner_user_id` (string, required, nullable)
- `turn_comments` (list of object, required)
  - `turn_index` (integer, required)
  - `comment` (string, required)
  - `created_at_unix_secs` (integer, required)
  - `owner_user_id` (string, required, nullable)
- `status` (enum, required)
  - Allowed values: `open`, `in_progress`, `resolved`, `merged`
- `source` (enum, required)
  - Allowed values: `qa`, `agent`, `manual`
- `assignee_user_id` (string, required, nullable)
- `created_at_unix_secs` (integer, required)
- `updated_at_unix_secs` (integer, required)

## Examples

**Request**

```json
{
  "conversation_id": "string"
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
  "source": "qa",
  "assignee_user_id": "string",
  "created_at_unix_secs": 1,
  "updated_at_unix_secs": 1
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.triageTickets.create({
        conversationId: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.triage_tickets.create(
    conversation_id="string",
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

	url := "https://api.elevenlabs.io/v1/convai/triage-tickets"

	payload := strings.NewReader("{\n  \"conversation_id\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/triage-tickets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"conversation_id\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/triage-tickets")
  .header("Content-Type", "application/json")
  .body("{\n  \"conversation_id\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/triage-tickets', [
  'body' => '{
  "conversation_id": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/triage-tickets");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"conversation_id\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["conversation_id": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/triage-tickets")! as URL,
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
