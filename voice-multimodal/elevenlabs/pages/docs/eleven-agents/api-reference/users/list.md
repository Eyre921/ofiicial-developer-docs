---
title: "List users"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/users/list.md
path: docs/eleven-agents/api-reference/users/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List users

GET https://api.elevenlabs.io/v1/convai/users

Get distinct users from conversations with pagination.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/users/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, optional) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `branch_id` (string, optional) — Filter conversations by branch ID.
- `call_start_before_unix` (integer, optional) — Unix timestamp (in seconds) to filter conversations up to this start date.
- `call_start_after_unix` (integer, optional) — Unix timestamp (in seconds) to filter conversations after to this start date.
- `search` (string, optional) — Search/filter by user ID (exact match).
- `page_size` (integer, optional, default: 30) — How many users to return at maximum. Defaults to 30.
- `sort_by` (enum, optional) — The field to sort the results by. Defaults to last_contact_unix_secs.
  - Allowed values: `last_contact_unix_secs`, `conversation_count`, `average_sentiment_score`
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `users` (list of object, required)
  - `user_id` (string, required)
  - `last_contact_unix_secs` (integer, required)
  - `first_contact_unix_secs` (integer, required)
  - `conversation_count` (integer, required)
  - `last_contact_conversation_id` (string, required)
  - `sentiment` (object, required)
    - `scored_conversation_count` (integer, required)
    - `positive_count` (integer, required)
    - `neutral_count` (integer, required)
    - `negative_count` (integer, required)
    - `recent_scored_conversation_count` (integer, required)
    - `recent_positive_count` (integer, required)
    - `recent_neutral_count` (integer, required)
    - `recent_negative_count` (integer, required)
    - `average_sentiment_score` (double, optional)
    - `average_frustration_score` (double, optional)
    - `recent_average_sentiment_score` (double, optional)
    - `recent_average_frustration_score` (double, optional)
  - `last_contact_agent_id` (string, optional)
  - `last_contact_agent_name` (string, optional)
  - `most_frustrated_conversations` (list of object, optional)
    - `conversation_id` (string, required)
    - `agent_id` (string, required)
    - `start_time_unix_secs` (integer, required)
    - `overall_label` (enum, required)
      - Allowed values: `positive`, `neutral`, `negative`
    - `overall_sentiment_score` (double, required)
    - `overall_frustration_score` (double, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "users": [
    {
      "user_id": "user_9f8b7c6d5e4a3b2c1d0e",
      "last_contact_unix_secs": 1685404800,
      "first_contact_unix_secs": 1677628800,
      "conversation_count": 42,
      "last_contact_conversation_id": "conv_5a3f9b8c7d6e4f2a1b0c",
      "sentiment": {
        "scored_conversation_count": 40,
        "positive_count": 25,
        "neutral_count": 10,
        "negative_count": 5,
        "recent_scored_conversation_count": 10,
        "recent_positive_count": 6,
        "recent_neutral_count": 3,
        "recent_negative_count": 1,
        "average_sentiment_score": 0.75,
        "average_frustration_score": 0.2,
        "recent_average_sentiment_score": 0.8,
        "recent_average_frustration_score": 0.15
      },
      "last_contact_agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "last_contact_agent_name": "SupportBot Alpha",
      "most_frustrated_conversations": [
        {
          "conversation_id": "conv_7e4d3c2b1a0f9e8d7c6b",
          "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
          "start_time_unix_secs": 1685318400,
          "overall_label": "negative",
          "overall_sentiment_score": -0.6,
          "overall_frustration_score": 0.9
        }
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "cursor_eyJwYWdlIjoxfQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.users.list({
        agentId: "agent_id",
        branchId: "branch_id",
        callStartAfterUnix: 1,
        callStartBeforeUnix: 1,
        cursor: "cursor",
        pageSize: 1,
        search: "search",
        sortBy: "last_contact_unix_secs",
        sortDirection: "asc",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.users.list(
    agent_id="agent_id",
    branch_id="branch_id",
    call_start_after_unix=1,
    call_start_before_unix=1,
    cursor="cursor",
    page_size=1,
    search="search",
    sort_by="last_contact_unix_secs",
    sort_direction="asc",
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

	url := "https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
