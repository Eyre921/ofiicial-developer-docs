---
title: "Get link"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-link.md
path: docs/eleven-agents/api-reference/agents/get-link
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get link

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/link

Get the current link used to share the agent with others

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-link

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/link:
    get:
      operationId: get
      summary: Get Shareable Agent Link
      description: Get the current link used to share the agent with others
      tags:
        - link
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
                $ref: '#/components/schemas/type_:GetAgentLinkResponseModel'
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
    type_:ConversationTokenPurpose:
      type: string
      enum:
        - signed_url
        - shareable_link
      title: ConversationTokenPurpose
    type_:ConversationTokenResponseModel:
      type: object
      properties:
        agent_id:
          type: string
          description: The ID of the agent
        conversation_token:
          type: string
          description: The token for the agent
        expiration_time_unix_secs:
          type: integer
          description: The expiration time of the token in unix seconds
        conversation_id:
          type: string
          description: The ID of the conversation
        purpose:
          $ref: '#/components/schemas/type_:ConversationTokenPurpose'
          description: The purpose of the token
        token_requester_user_id:
          type: string
          description: The user ID of the entity who requested the token
      required:
        - agent_id
        - conversation_token
        - purpose
      title: ConversationTokenResponseModel
    type_:GetAgentLinkResponseModel:
      type: object
      properties:
        agent_id:
          type: string
          description: The ID of the agent
        token:
          $ref: '#/components/schemas/type_:ConversationTokenResponseModel'
          description: The token data for the agent
      required:
        - agent_id
      title: GetAgentLinkResponseModel
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

**Response**

```json
{
  "agent_id": "J3Pbu5gP6NNKBscdCdwB",
  "token": {
    "agent_id": "agent_id",
    "conversation_token": "conversation_token",
    "purpose": "signed_url",
    "expiration_time_unix_secs": 1,
    "conversation_id": "conversation_id",
    "token_requester_user_id": "token_requester_user_id"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.link.get("agent_3701k3ttaq12ewp8b7qv5rfyszkz");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.link.get(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/link"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/link")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/link")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/link');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/link");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/link")! as URL,
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
