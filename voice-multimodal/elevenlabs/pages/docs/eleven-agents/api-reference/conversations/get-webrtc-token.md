---
title: "Get conversation token"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-webrtc-token.md
path: docs/eleven-agents/api-reference/conversations/get-webrtc-token
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get conversation token

GET https://api.elevenlabs.io/v1/convai/conversation/token

Get a WebRTC session token for real-time communication.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-webrtc-token

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversation/token:
    get:
      operationId: get_webrtc_token
      summary: >-
        Get a webrtc token to start a conversation with an agent that requires
        authorization
      description: Get a WebRTC session token for real-time communication.
      tags:
        - conversations
      parameters:
        - name: agent_id
          in: query
          description: >-
            Agent id (agent_…) or speech engine external id (seng_), resolved to
            the same underlying resource.
          required: true
          schema:
            type: string
        - name: participant_name
          in: query
          description: >-
            Optional custom participant name. If not provided, user ID will be
            used
          required: false
          schema:
            type: string
        - name: branch_id
          in: query
          description: The ID of the branch to use
          required: false
          schema:
            type: string
        - name: environment
          in: query
          description: >-
            The environment to use for resolving environment variables (e.g.
            'production', 'staging'). Defaults to 'production'.
          required: false
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
                $ref: '#/components/schemas/type_:TokenResponseModel'
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
    type_:TokenResponseModel:
      type: object
      properties:
        token:
          type: string
        conversation_id:
          type: string
      required:
        - token
        - conversation_id
      title: TokenResponseModel
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
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb252YW5zYXRpb25fMTIzNDU2IiwiaWF0IjoxNjg3MjM5MjAwLCJleHAiOjE2ODcyNDI4MDB9.4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e7f8g9h0i",
  "conversation_id": "conv_5f8d04a2c9e77b0012345678"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e",
    });
    await client.conversationalAi.conversations.getWebrtcToken({
        agentId: "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        branchId: "branch_5f8d04a2c9e77b0012345678",
        environment: "production",
        participantName: "jane_doe_92",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e",
)

client.conversational_ai.conversations.get_webrtc_token(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="branch_5f8d04a2c9e77b0012345678",
    environment="production",
    participant_name="jane_doe_92",
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

	url := "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_5f8d04a2c9e77b0012345678&environment=production&participant_name=jane_doe_92"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e")
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

url = URI("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_5f8d04a2c9e77b0012345678&environment=production&participant_name=jane_doe_92")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_5f8d04a2c9e77b0012345678&environment=production&participant_name=jane_doe_92")
  .header("xi-api-key", "sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_5f8d04a2c9e77b0012345678&environment=production&participant_name=jane_doe_92', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_5f8d04a2c9e77b0012345678&environment=production&participant_name=jane_doe_92");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk_live_4f8b9c7d2e3a4b5c9d0e1f2a3b4c5d6e",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_5f8d04a2c9e77b0012345678&environment=production&participant_name=jane_doe_92")! as URL,
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
