---
title: "Get agent conversation topics"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/topics/get.md
path: docs/eleven-agents/api-reference/conversations/topics/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get agent conversation topics

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/topics

Returns the latest topic discovery run results for a given agent.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/topics/get

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

- `page_size` (integer, optional) — Number of top-level topic groups to return.
- `sort_by` (enum, optional) — Column to rank topics by. Use conversations for volume, sentiment with sort_direction=asc for the most negative topics, and frustration with sort_direction=desc for the most frustrated ones. Topics with no score are always ranked last.
  - Allowed values: `conversations`, `sentiment`, `success_rate`, `frustration`
- `sort_direction` (enum, optional) — Direction to sort topics.
  - Allowed values: `asc`, `desc`
- `from_unix_secs` (integer, optional) — Start of the window to view topics for. When set with to_unix_secs, the completed daily topic-discovery runs in the range are aggregated together, so the window scopes the metrics as well as the topic set. Floored to the start of its UTC day because runs cover whole UTC days; aggregated_run_count reports how many runs were summed. Omit both bounds to get the single latest run.
- `to_unix_secs` (integer, optional) — End of the window to view topics for.
- `include_evaluation_criteria` (boolean, optional, default: true) — Include the per-criteria evaluation breakdown on each topic's metrics. Pass false to drop it: it dominates the payload and the weighted success_rate is returned either way.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `topics` (list of object, required)
  - `topic_id` (string, required)
  - `label` (string, required)
  - `description` (string, required)
  - `conversation_count` (integer, required)
  - `parent_topic_id` (string, optional)
  - `x_2d` (double, optional)
  - `y_2d` (double, optional)
  - `metrics` (object, optional)
    - `conversation_count` (integer, optional, default: 0)
    - `sentiment` (object, optional)
      - `sentiment` (object, optional)
        - `count` (integer, optional, default: 0)
        - `sum` (double, optional, default: 0)
        - `min` (double, optional)
        - `max` (double, optional)
      - `frustration` (object, optional)
        - `count` (integer, optional, default: 0)
        - `sum` (double, optional, default: 0)
        - `min` (double, optional)
        - `max` (double, optional)
      - `positive_count` (integer, optional, default: 0)
      - `neutral_count` (integer, optional, default: 0)
      - `negative_count` (integer, optional, default: 0)
    - `evaluation_criteria` (list of object, optional)
      - `criteria_id` (string, required)
      - `success_count` (integer, optional, default: 0)
      - `failure_count` (integer, optional, default: 0)
      - `unknown_count` (integer, optional, default: 0)
  - `success_rate` (double, optional) — Success rate across the topic's evaluation criteria, weighted by scored conversations. Returned regardless of include_evaluation_criteria.
- `window_start_unix_secs` (integer, required)
- `window_end_unix_secs` (integer, required)
- `aggregated_run_count` (integer, optional, default: 0) — Number of daily topic-discovery runs the returned metrics were summed over.
- `has_more` (boolean, optional, default: false)
- `next_cursor` (string, optional)

## Examples

**Response**

```json
{
  "topics": [
    {
      "topic_id": "topic_id",
      "label": "label",
      "description": "description",
      "conversation_count": 1,
      "parent_topic_id": "parent_topic_id",
      "x_2d": 1.1,
      "y_2d": 1.1,
      "success_rate": 1.1
    }
  ],
  "window_start_unix_secs": 1,
  "window_end_unix_secs": 1,
  "aggregated_run_count": 1,
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.topics.get("agent_id", {
        cursor: "cursor",
        fromUnixSecs: 1,
        includeEvaluationCriteria: true,
        pageSize: 1,
        sortBy: "conversations",
        sortDirection: "asc",
        toUnixSecs: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.topics.get(
    agent_id="agent_id",
    cursor="cursor",
    from_unix_secs=1,
    include_evaluation_criteria=True,
    page_size=1,
    sort_by="conversations",
    sort_direction="asc",
    to_unix_secs=1,
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?cursor=cursor&from_unix_secs=1&include_evaluation_criteria=true&page_size=1&sort_by=conversations&sort_direction=asc&to_unix_secs=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?cursor=cursor&from_unix_secs=1&include_evaluation_criteria=true&page_size=1&sort_by=conversations&sort_direction=asc&to_unix_secs=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?cursor=cursor&from_unix_secs=1&include_evaluation_criteria=true&page_size=1&sort_by=conversations&sort_direction=asc&to_unix_secs=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?cursor=cursor&from_unix_secs=1&include_evaluation_criteria=true&page_size=1&sort_by=conversations&sort_direction=asc&to_unix_secs=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?cursor=cursor&from_unix_secs=1&include_evaluation_criteria=true&page_size=1&sort_by=conversations&sort_direction=asc&to_unix_secs=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?cursor=cursor&from_unix_secs=1&include_evaluation_criteria=true&page_size=1&sort_by=conversations&sort_direction=asc&to_unix_secs=1")! as URL,
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
