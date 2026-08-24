---
title: "Get ticket"
source: https://elevenlabs.io/docs/api-reference/triage-tickets/get-agent-conversation-ticket-route.md
path: docs/api-reference/triage-tickets/get-agent-conversation-ticket-route
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get ticket

GET https://api.elevenlabs.io/v1/convai/triage-tickets/{agentqa_ticket_id}

Get an agent conversation ticket by ID.

Reference: https://elevenlabs.io/docs/api-reference/triage-tickets/get-agent-conversation-ticket-route

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
- `issue_type` (enum, required, nullable)
  - Allowed values: `knowledge_gap`, `product_feedback`, `tool_issue`, `missing_tool`, `unnecessary_escalation`
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
    await client.getAgentConversationTicketRoute("agentqa_ticket_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.get_agent_conversation_ticket_route(
    agentqa_ticket_id="agentqa_ticket_id",
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
