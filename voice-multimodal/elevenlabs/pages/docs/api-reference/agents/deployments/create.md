---
title: "Create deployment"
source: https://elevenlabs.io/docs/api-reference/agents/deployments/create.md
path: docs/api-reference/agents/deployments/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create deployment

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/deployments
Content-Type: application/json

Create a new deployment for an agent

Reference: https://elevenlabs.io/docs/api-reference/agents/deployments/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/deployments:
    post:
      operationId: create
      summary: Create Or Update Deployments
      description: Create a new deployment for an agent
      tags:
        - subpackage_conversationalAi/agents/deployments
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/AgentDeploymentResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_or_update_deployments_v1_convai_agents__agent_id__deployments_post
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
    AgentDeploymentPercentageStrategy:
      type: object
      properties:
        type:
          type: string
          enum:
            - percentage
          default: percentage
        traffic_percentage:
          type: number
          format: double
          description: Traffic percentage to deploy
      required:
        - traffic_percentage
      title: AgentDeploymentPercentageStrategy
    AgentDeploymentRequestItem:
      type: object
      properties:
        branch_id:
          type: string
          description: ID of the branch to deploy
        deployment_strategy:
          $ref: '#/components/schemas/AgentDeploymentPercentageStrategy'
      required:
        - branch_id
        - deployment_strategy
      title: AgentDeploymentRequestItem
    AgentDeploymentRequest:
      type: object
      properties:
        requests:
          type: array
          items:
            $ref: '#/components/schemas/AgentDeploymentRequestItem'
          description: List of deployment requests
      required:
        - requests
      title: AgentDeploymentRequest
    Body_Create_or_update_deployments_v1_convai_agents__agent_id__deployments_post:
      type: object
      properties:
        deployment_request:
          $ref: '#/components/schemas/AgentDeploymentRequest'
          description: Request to create a new deployment
      required:
        - deployment_request
      title: >-
        Body_Create_or_update_deployments_v1_convai_agents__agent_id__deployments_post
    AgentDeploymentResponse:
      type: object
      properties:
        traffic_percentage_branch_id_map:
          type: object
          additionalProperties:
            type: number
            format: double
          description: Map of branch IDs to traffic percentages
      title: AgentDeploymentResponse
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
    "agtbrch_8901k4t9z5defmb8vh3e9361y7nj": 0.5
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.deployments.create("agent_id", {
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
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")
  .header("Content-Type", "application/json")
  .body("{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments', [
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")! as URL,
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
