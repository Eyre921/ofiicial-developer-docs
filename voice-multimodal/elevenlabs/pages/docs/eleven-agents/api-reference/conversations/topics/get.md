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

- `from_unix_secs` (integer, optional) — Start of the window to view topics for. When set with to_unix_secs, per-day topics in the range are aggregated together.
- `to_unix_secs` (integer, optional) — End of the window to view topics for.

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
- `window_start_unix_secs` (integer, required)
- `window_end_unix_secs` (integer, required)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "topics": [
    {
      "topic_id": "b7f3a9d2-4c8e-4f1a-9d3e-2a5f7b6c9e12",
      "label": "Customer Support Issues",
      "description": "Conversations related to troubleshooting and support requests.",
      "conversation_count": 124,
      "parent_topic_id": null,
      "x_2d": 0.45,
      "y_2d": -0.32
    }
  ],
  "window_start_unix_secs": 1685606400,
  "window_end_unix_secs": 1685692799
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.topics.get("agent_id", {
        fromUnixSecs: 1,
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
    from_unix_secs=1,
    to_unix_secs=1,
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?from_unix_secs=1&to_unix_secs=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?from_unix_secs=1&to_unix_secs=1")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?from_unix_secs=1&to_unix_secs=1")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?from_unix_secs=1&to_unix_secs=1', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?from_unix_secs=1&to_unix_secs=1");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics?from_unix_secs=1&to_unix_secs=1")! as URL,
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
