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
            type:
              - integer
              - 'null'
        - name: to_unix_secs
          in: query
          description: End of the window to view topics for.
          required: false
          schema:
            type:
              - integer
              - 'null'
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
                $ref: '#/components/schemas/GetAgentTopicsResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    NumericDistributionAggregate:
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
          type:
            - number
            - 'null'
          format: double
        max:
          type:
            - number
            - 'null'
          format: double
      title: NumericDistributionAggregate
    TopicSentimentAggregate:
      type: object
      properties:
        sentiment:
          $ref: '#/components/schemas/NumericDistributionAggregate'
        frustration:
          $ref: '#/components/schemas/NumericDistributionAggregate'
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
    TopicEvaluationCriteriaAggregate:
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
    TopicMetricsAggregate:
      type: object
      properties:
        conversation_count:
          type: integer
          default: 0
        sentiment:
          oneOf:
            - $ref: '#/components/schemas/TopicSentimentAggregate'
            - type: 'null'
        evaluation_criteria:
          type: array
          items:
            $ref: '#/components/schemas/TopicEvaluationCriteriaAggregate'
      title: TopicMetricsAggregate
    AgentTopicResponseModel:
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
          type:
            - string
            - 'null'
        x_2d:
          type:
            - number
            - 'null'
          format: double
        y_2d:
          type:
            - number
            - 'null'
          format: double
        metrics:
          oneOf:
            - $ref: '#/components/schemas/TopicMetricsAggregate'
            - type: 'null'
      required:
        - topic_id
        - label
        - description
        - conversation_count
      title: AgentTopicResponseModel
    GetAgentTopicsResponseModel:
      type: object
      properties:
        topics:
          type: array
          items:
            $ref: '#/components/schemas/AgentTopicResponseModel'
        window_start_unix_secs:
          type: integer
        window_end_unix_secs:
          type: integer
      required:
        - topics
        - window_start_unix_secs
        - window_end_unix_secs
      title: GetAgentTopicsResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
  "window_end_unix_secs": 1
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
