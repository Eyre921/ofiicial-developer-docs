---
title: "List users"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/users/list.md
path: docs/eleven-agents/api-reference/users/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List users

GET https://api.elevenlabs.io/v1/convai/users

Get distinct users from conversations with pagination.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/users/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/users:
    get:
      operationId: list
      summary: Get Conversation Users
      description: Get distinct users from conversations with pagination.
      tags:
        - subpackage_conversationalAi/users
      parameters:
        - name: agent_id
          in: query
          description: >-
            Agent id (agent_…) or speech engine external id (seng_), resolved to
            the same underlying resource.
          required: false
          schema:
            type: string
        - name: branch_id
          in: query
          description: Filter conversations by branch ID.
          required: false
          schema:
            type: string
        - name: call_start_before_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations up to this start
            date.
          required: false
          schema:
            type: integer
        - name: call_start_after_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations after to this
            start date.
          required: false
          schema:
            type: integer
        - name: search
          in: query
          description: Search/filter by user ID (exact match).
          required: false
          schema:
            type: string
        - name: page_size
          in: query
          description: How many users to return at maximum. Defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: sort_by
          in: query
          description: >-
            The field to sort the results by. Defaults to
            last_contact_unix_secs.
          required: false
          schema:
            $ref: '#/components/schemas/type_:UsersSortBy'
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
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
                $ref: >-
                  #/components/schemas/type_:GetConversationUsersPageResponseModel
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
    type_:UsersSortBy:
      type: string
      enum:
        - last_contact_unix_secs
        - conversation_count
      title: UsersSortBy
    type_:SentimentAggregate:
      type: object
      properties:
        scored_conversation_count:
          type: integer
        positive_count:
          type: integer
        neutral_count:
          type: integer
        negative_count:
          type: integer
        average_sentiment_score:
          type: number
          format: double
        average_frustration_score:
          type: number
          format: double
      required:
        - scored_conversation_count
        - positive_count
        - neutral_count
        - negative_count
      title: SentimentAggregate
    type_:FrustratedConversationRefOverallLabel:
      type: string
      enum:
        - positive
        - neutral
        - negative
      title: FrustratedConversationRefOverallLabel
    type_:FrustratedConversationRef:
      type: object
      properties:
        conversation_id:
          type: string
        agent_id:
          type: string
        start_time_unix_secs:
          type: integer
        overall_label:
          $ref: '#/components/schemas/type_:FrustratedConversationRefOverallLabel'
        overall_sentiment_score:
          type: number
          format: double
        overall_frustration_score:
          type: number
          format: double
      required:
        - conversation_id
        - agent_id
        - start_time_unix_secs
        - overall_label
        - overall_sentiment_score
        - overall_frustration_score
      title: FrustratedConversationRef
    type_:ConversationUserResponseModel:
      type: object
      properties:
        user_id:
          type: string
        last_contact_unix_secs:
          type: integer
        first_contact_unix_secs:
          type: integer
        conversation_count:
          type: integer
        last_contact_agent_id:
          type: string
        last_contact_conversation_id:
          type: string
        last_contact_agent_name:
          type: string
        sentiment:
          $ref: '#/components/schemas/type_:SentimentAggregate'
        most_frustrated_conversations:
          type: array
          items:
            $ref: '#/components/schemas/type_:FrustratedConversationRef'
      required:
        - user_id
        - last_contact_unix_secs
        - first_contact_unix_secs
        - conversation_count
        - last_contact_conversation_id
        - sentiment
      title: ConversationUserResponseModel
    type_:GetConversationUsersPageResponseModel:
      type: object
      properties:
        users:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConversationUserResponseModel'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - users
        - has_more
      title: GetConversationUsersPageResponseModel
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
  "users": [
    {
      "user_id": "user_9f8b7c6d5e4a3b2c1d0e",
      "last_contact_unix_secs": 1685606400,
      "first_contact_unix_secs": 1672531200,
      "conversation_count": 42,
      "last_contact_conversation_id": "conv_5a3f9d8e7b6c4d2f1e0a",
      "sentiment": {
        "scored_conversation_count": 40,
        "positive_count": 25,
        "neutral_count": 10,
        "negative_count": 5,
        "average_sentiment_score": 0.75,
        "average_frustration_score": 0.2
      },
      "last_contact_agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "last_contact_agent_name": "SupportBot Alpha",
      "most_frustrated_conversations": [
        {
          "conversation_id": "conv_1a2b3c4d5e6f7g8h9i0j",
          "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
          "start_time_unix_secs": 1683024000,
          "overall_label": "negative",
          "overall_sentiment_score": -0.6,
          "overall_frustration_score": 0.9
        }
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "cursor_eyJwYWdlIjoxfQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.users.list({
        agentId: "agent_id",
        branchId: "branch_id",
        callStartAfterUnix: 1,
        callStartBeforeUnix: 1,
        cursor: "cursor",
        pageSize: 1,
        search: "search",
        sortBy: "last_contact_unix_secs",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.users.list(
    agent_id="agent_id",
    branch_id="branch_id",
    call_start_after_unix=1,
    call_start_before_unix=1,
    cursor="cursor",
    page_size=1,
    search="search",
    sort_by="last_contact_unix_secs",
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

	url := "https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs"

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

url = URI("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs")! as URL,
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
