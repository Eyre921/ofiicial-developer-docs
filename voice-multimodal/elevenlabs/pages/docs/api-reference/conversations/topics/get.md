---
title: "Get agent conversation topics"
source: https://elevenlabs.io/docs/api-reference/conversations/topics/get.md
path: docs/api-reference/conversations/topics/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get agent conversation topics

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/topics

Returns the latest topic discovery run results for a given agent.

Reference: https://elevenlabs.io/docs/api-reference/conversations/topics/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — ID of the agent

### Query parameters

- `page_size` (integer, optional, nullable) — Number of top-level topic groups to return.
- `sort_by` (enum, optional) — Topic table column to sort by.
  - Allowed values: `conversations`, `sentiment`, `success_rate`
- `sort_direction` (enum, optional) — Direction to sort topics.
  - Allowed values: `asc`, `desc`
- `from_unix_secs` (integer, optional, nullable) — Start of the window to view topics for. When set with to_unix_secs, per-day topics in the range are aggregated together.
- `to_unix_secs` (integer, optional, nullable) — End of the window to view topics for.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `topics` (list of object, required)
  - `topic_id` (string, required)
  - `label` (string, required)
  - `description` (string, required)
  - `conversation_count` (integer, required)
  - `parent_topic_id` (string, optional, nullable)
  - `x_2d` (double, optional, nullable)
  - `y_2d` (double, optional, nullable)
  - `metrics` (object, optional, nullable)
    - `conversation_count` (integer, optional, default: 0)
    - `sentiment` (object, optional, nullable)
      - `sentiment` (object, optional)
        - `count` (integer, optional, default: 0)
        - `sum` (double, optional, default: 0)
        - `min` (double, optional, nullable)
        - `max` (double, optional, nullable)
      - `frustration` (object, optional)
        - `count` (integer, optional, default: 0)
        - `sum` (double, optional, default: 0)
        - `min` (double, optional, nullable)
        - `max` (double, optional, nullable)
      - `positive_count` (integer, optional, default: 0)
      - `neutral_count` (integer, optional, default: 0)
      - `negative_count` (integer, optional, default: 0)
    - `evaluation_criteria` (list of object, optional)
      - `criteria_id` (string, required)
      - `success_count` (integer, optional, default: 0)
      - `failure_count` (integer, optional, default: 0)
      - `unknown_count` (integer, optional, default: 0)
- `window_start_unix_secs` (integer, required)
- `window_end_unix_secs` (integer, required)
- `has_more` (boolean, optional, default: false)
- `next_cursor` (string, optional, nullable)

## Examples

**Response**

```json
{
  "topics": [
    {
      "topic_id": "string",
      "label": "string",
      "description": "string",
      "conversation_count": 1,
      "parent_topic_id": "string",
      "x_2d": 1.1,
      "y_2d": 1.1,
      "metrics": {
        "conversation_count": 0,
        "sentiment": {
          "sentiment": {
            "count": 0,
            "sum": 0,
            "min": 1.1,
            "max": 1.1
          },
          "frustration": {
            "count": 0,
            "sum": 0,
            "min": 1.1,
            "max": 1.1
          },
          "positive_count": 0,
          "neutral_count": 0,
          "negative_count": 0
        },
        "evaluation_criteria": [
          {
            "criteria_id": "string",
            "success_count": 0,
            "failure_count": 0,
            "unknown_count": 0
          }
        ]
      }
    }
  ],
  "window_start_unix_secs": 1,
  "window_end_unix_secs": 1,
  "has_more": false,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.topics.get("agent_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.topics.get(
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")! as URL,
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
