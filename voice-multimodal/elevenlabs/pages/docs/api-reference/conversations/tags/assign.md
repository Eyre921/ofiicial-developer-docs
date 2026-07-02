---
title: "Add tag to conversation"
source: https://elevenlabs.io/docs/api-reference/conversations/tags/assign.md
path: docs/api-reference/conversations/tags/assign
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add tag to conversation

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/tags
Content-Type: application/json

Assign one or more conversation tags to a conversation. Tags that are already assigned are ignored. Tags must belong to the same workspace.

Reference: https://elevenlabs.io/docs/api-reference/conversations/tags/assign

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversations/{conversation_id}/tags:
    post:
      operationId: assign
      summary: Assign Conversation Tags
      description: >-
        Assign one or more conversation tags to a conversation. Tags that are
        already assigned are ignored. Tags must belong to the same workspace.
      tags:
        - subpackage_conversationalAi/conversations/tags
      parameters:
        - name: conversation_id
          in: path
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '204':
          description: Successful Response
          content:
            application/json:
              schema:
                type: object
                properties: {}
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
              $ref: '#/components/schemas/AssignConversationTagsRequestModel'
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
    AssignConversationTagsRequestModel:
      type: object
      properties:
        tag_ids:
          type: array
          items:
            type: string
          description: >-
            Tag IDs to add to the conversation. Re-assigning an existing tag is
            a no-op.
      required:
        - tag_ids
      title: AssignConversationTagsRequestModel
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
  "tag_ids": [
    "tag_9f8b7c6d5e4a3b2c1d0e"
  ]
}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.tags.assign("conversation_id", {
        tagIds: [
            "tag_9f8b7c6d5e4a3b2c1d0e",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.tags.assign(
    conversation_id="conversation_id",
    tag_ids=[
        "tag_9f8b7c6d5e4a3b2c1d0e"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/tags"

	payload := strings.NewReader("{\n  \"tag_ids\": [\n    \"tag_9f8b7c6d5e4a3b2c1d0e\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/tags")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tag_ids\": [\n    \"tag_9f8b7c6d5e4a3b2c1d0e\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/tags")
  .header("Content-Type", "application/json")
  .body("{\n  \"tag_ids\": [\n    \"tag_9f8b7c6d5e4a3b2c1d0e\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/tags', [
  'body' => '{
  "tag_ids": [
    "tag_9f8b7c6d5e4a3b2c1d0e"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/tags");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tag_ids\": [\n    \"tag_9f8b7c6d5e4a3b2c1d0e\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tag_ids": ["tag_9f8b7c6d5e4a3b2c1d0e"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/tags")! as URL,
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
