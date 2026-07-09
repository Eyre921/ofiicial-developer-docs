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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/topics:
    get:
      operationId: get
      summary: Get Agent Conversation Topics
      description: Returns the latest topic discovery run results for a given agent.
      tags:
        - topics
      parameters:
        - name: agent_id
          in: path
          description: ID of the agent
          required: true
          schema:
            type: string
        - name: from_unix_secs
          in: query
          description: >-
            Start of the window to view topics for. When set with to_unix_secs,
            per-day topics in the range are aggregated together.
          required: false
          schema:
            type: integer
        - name: to_unix_secs
          in: query
          description: End of the window to view topics for.
          required: false
          schema:
            type: integer
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:GetAgentTopicsResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    type_:NumericDistributionAggregate:
      type: object
      properties:
        count:
          type: integer
          default: 0
        sum:
          type: number
          format: double
          default: 0
        min:
          type: number
          format: double
        max:
          type: number
          format: double
      title: NumericDistributionAggregate
    type_:TopicSentimentAggregate:
      type: object
      properties:
        sentiment:
          $ref: '#/components/schemas/type_:NumericDistributionAggregate'
        frustration:
          $ref: '#/components/schemas/type_:NumericDistributionAggregate'
        positive_count:
          type: integer
          default: 0
        neutral_count:
          type: integer
          default: 0
        negative_count:
          type: integer
          default: 0
      title: TopicSentimentAggregate
    type_:TopicEvaluationCriteriaAggregate:
      type: object
      properties:
        criteria_id:
          type: string
        success_count:
          type: integer
          default: 0
        failure_count:
          type: integer
          default: 0
        unknown_count:
          type: integer
          default: 0
      required:
        - criteria_id
      title: TopicEvaluationCriteriaAggregate
    type_:TopicMetricsAggregate:
      type: object
      properties:
        conversation_count:
          type: integer
          default: 0
        sentiment:
          $ref: '#/components/schemas/type_:TopicSentimentAggregate'
        evaluation_criteria:
          type: array
          items:
            $ref: '#/components/schemas/type_:TopicEvaluationCriteriaAggregate'
      title: TopicMetricsAggregate
    type_:AgentTopicResponseModel:
      type: object
      properties:
        topic_id:
          type: string
        label:
          type: string
        description:
          type: string
        conversation_count:
          type: integer
        parent_topic_id:
          type: string
        x_2d:
          type: number
          format: double
        y_2d:
          type: number
          format: double
        metrics:
          $ref: '#/components/schemas/type_:TopicMetricsAggregate'
      required:
        - topic_id
        - label
        - description
        - conversation_count
      title: AgentTopicResponseModel
    type_:GetAgentTopicsResponseModel:
      type: object
      properties:
        topics:
          type: array
          items:
            $ref: '#/components/schemas/type_:AgentTopicResponseModel'
        window_start_unix_secs:
          type: integer
        window_end_unix_secs:
          type: integer
      required:
        - topics
        - window_start_unix_secs
        - window_end_unix_secs
      title: GetAgentTopicsResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

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
