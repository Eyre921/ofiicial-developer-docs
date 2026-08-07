---
title: "Create deployment"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/deployments/create.md
path: docs/eleven-agents/api-reference/agents/deployments/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create deployment

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/deployments
Content-Type: application/json

Create a new deployment for an agent

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/deployments/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Body (application/json)

- `deployment_request` (object, required) — Request to create a new deployment
  - `requests` (list of object, required) — List of deployment requests
    - `branch_id` (string, required) — ID of the branch to deploy
    - `deployment_strategy` (object, required)
      - `traffic_percentage` (double, required) — Traffic percentage to deploy
      - `type` ("percentage", optional)

## Response

### 200

Successful Response

- `traffic_percentage_branch_id_map` (map from string to double, optional) — Map of branch IDs to traffic percentages

## Examples

**Request**

```json
{
  "deployment_request": {
    "requests": [
      {
        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        "deployment_strategy": {
          "traffic_percentage": 0.5,
          "type": "percentage"
        }
      }
    ]
  }
}
```

**Response**

```json
{
  "traffic_percentage_branch_id_map": {
    "key": 1.1
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.deployments.create("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        deploymentRequest: {
            requests: [
                {
                    branchId: "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                    deploymentStrategy: {
                        trafficPercentage: 0.5,
                        type: "percentage",
                    },
                },
            ],
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, AgentDeploymentRequest, AgentDeploymentRequestItem, AgentDeploymentPercentageStrategy

client = ElevenLabs()

client.conversational_ai.agents.deployments.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    deployment_request=AgentDeploymentRequest(
        requests=[
            AgentDeploymentRequestItem(
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                deployment_strategy=AgentDeploymentPercentageStrategy(
                    traffic_percentage=0.5,
                    type="percentage",
                ),
            )
        ],
    ),
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments"

	payload := strings.NewReader("{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments")
  .header("Content-Type", "application/json")
  .body("{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments', [
  'body' => '{
  "deployment_request": {
    "requests": [
      {
        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        "deployment_strategy": {
          "traffic_percentage": 0.5,
          "type": "percentage"
        }
      }
    ]
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["deployment_request": ["requests": [
      [
        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        "deployment_strategy": [
          "traffic_percentage": 0.5,
          "type": "percentage"
        ]
      ]
    ]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments")! as URL,
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
