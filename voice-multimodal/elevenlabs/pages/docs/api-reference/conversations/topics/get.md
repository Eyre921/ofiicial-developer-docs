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
- `sort_by` (enum, optional) — Column to rank topics by. Use conversations for volume, sentiment with sort_direction=asc for the most negative topics, and frustration with sort_direction=desc for the most frustrated ones. Topics with no score are always ranked last.
  - Allowed values: `conversations`, `sentiment`, `success_rate`, `frustration`
- `sort_direction` (enum, optional) — Direction to sort topics.
  - Allowed values: `asc`, `desc`
- `from_unix_secs` (integer, optional, nullable) — Start of the window to view topics for. When set with to_unix_secs, the completed daily topic-discovery runs in the range are aggregated together, so the window scopes the metrics as well as the topic set. Floored to the start of its UTC day because runs cover whole UTC days; aggregated_run_count reports how many runs were summed. Omit both bounds to get the single latest run.
- `to_unix_secs` (integer, optional, nullable) — End of the window to view topics for.
- `include_evaluation_criteria` (boolean, optional, default: true) — Include the per-criteria evaluation breakdown on each topic's metrics. Pass false to drop it: it dominates the payload and the weighted success_rate is returned either way.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `topics` (list of AgentTopicResponseModel, required)
- `window_start_unix_secs` (integer, required)
- `window_end_unix_secs` (integer, required)
- `aggregated_run_count` (integer, optional, default: 0) — Number of daily topic-discovery runs the returned metrics were summed over.
- `has_more` (boolean, optional, default: false)
- `next_cursor` (string, optional, nullable)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AgentTopicResponseModel

- `topic_id` (string, required)
- `label` (string, required)
- `description` (string, required)
- `conversation_count` (integer, required)
- `parent_topic_id` (string, optional, nullable)
- `x_2d` (double, optional, nullable)
- `y_2d` (double, optional, nullable)
- `metrics` (TopicMetricsAggregate, optional, nullable)
- `success_rate` (double, optional, nullable) — Success rate across the topic's evaluation criteria, weighted by scored conversations. Returned regardless of include_evaluation_criteria.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### TopicMetricsAggregate

- `conversation_count` (integer, optional, default: 0)
- `sentiment` (TopicSentimentAggregate, optional, nullable)
- `evaluation_criteria` (list of TopicEvaluationCriteriaAggregate, optional)

### ValidationErrorLocItems

### TopicSentimentAggregate

- `sentiment` (NumericDistributionAggregate, optional)
- `frustration` (NumericDistributionAggregate, optional)
- `positive_count` (integer, optional, default: 0)
- `neutral_count` (integer, optional, default: 0)
- `negative_count` (integer, optional, default: 0)

### TopicEvaluationCriteriaAggregate

- `criteria_id` (string, required)
- `success_count` (integer, optional, default: 0)
- `failure_count` (integer, optional, default: 0)
- `unknown_count` (integer, optional, default: 0)

### NumericDistributionAggregate

- `count` (integer, optional, default: 0)
- `sum` (double, optional, default: 0)
- `min` (double, optional, nullable)
- `max` (double, optional, nullable)

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
      "topic_id": "topic_a1b2c3d4e5f6",
      "label": "Billing & Payment Issues",
      "description": "Users asking about invoice discrepancies, failed payments, subscription charges, and refund requests.",
      "conversation_count": 342,
      "parent_topic_id": null,
      "x_2d": -0.47,
      "y_2d": 0.83,
      "metrics": {
        "conversation_count": 342,
        "sentiment": {
          "sentiment": {
            "count": 318,
            "sum": 142.6,
            "min": -0.92,
            "max": 0.87
          },
          "frustration": {
            "count": 318,
            "sum": 210.4,
            "min": 0.02,
            "max": 0.98
          },
          "positive_count": 89,
          "neutral_count": 124,
          "negative_count": 105
        },
        "evaluation_criteria": [
          {
            "criteria_id": "crit_resolved_issue",
            "success_count": 198,
            "failure_count": 112,
            "unknown_count": 32
          }
        ]
      },
      "success_rate": 0.638
    }
  ],
  "window_start_unix_secs": 1745452800,
  "window_end_unix_secs": 1748044800,
  "aggregated_run_count": 30,
  "has_more": true,
  "next_cursor": "eyJvZmZzZXQiOjEwLCJydW5faWQiOiJydW5fMjAyNTA1MDEifQ=="
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")! as URL,
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
