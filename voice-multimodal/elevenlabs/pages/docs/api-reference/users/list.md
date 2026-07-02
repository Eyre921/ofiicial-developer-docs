---
title: "List users"
source: https://elevenlabs.io/docs/api-reference/users/list.md
path: docs/api-reference/users/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List users

GET https://api.elevenlabs.io/v1/convai/users

Get distinct users from conversations with pagination.

Reference: https://elevenlabs.io/docs/api-reference/users/list

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
            type:
              - string
              - 'null'
        - name: branch_id
          in: query
          description: Filter conversations by branch ID.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: call_start_before_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations up to this start
            date.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: call_start_after_unix
          in: query
          description: >-
            Unix timestamp (in seconds) to filter conversations after to this
            start date.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: search
          in: query
          description: Search/filter by user ID (exact match).
          required: false
          schema:
            type:
              - string
              - 'null'
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
            $ref: '#/components/schemas/UsersSortBy'
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
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
                $ref: '#/components/schemas/GetConversationUsersPageResponseModel'
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
    UsersSortBy:
      type: string
      enum:
        - last_contact_unix_secs
        - conversation_count
      title: UsersSortBy
    SentimentAggregate:
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
          type:
            - number
            - 'null'
          format: double
        average_frustration_score:
          type:
            - number
            - 'null'
          format: double
      required:
        - scored_conversation_count
        - positive_count
        - neutral_count
        - negative_count
        - average_sentiment_score
        - average_frustration_score
      title: SentimentAggregate
    FrustratedConversationRefOverallLabel:
      type: string
      enum:
        - positive
        - neutral
        - negative
      title: FrustratedConversationRefOverallLabel
    FrustratedConversationRef:
      type: object
      properties:
        conversation_id:
          type: string
        agent_id:
          type: string
        start_time_unix_secs:
          type: integer
        overall_label:
          $ref: '#/components/schemas/FrustratedConversationRefOverallLabel'
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
    ConversationUserResponseModel:
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
          type:
            - string
            - 'null'
        last_contact_conversation_id:
          type: string
        last_contact_agent_name:
          type:
            - string
            - 'null'
        sentiment:
          $ref: '#/components/schemas/SentimentAggregate'
        most_frustrated_conversations:
          type: array
          items:
            $ref: '#/components/schemas/FrustratedConversationRef'
      required:
        - user_id
        - last_contact_unix_secs
        - first_contact_unix_secs
        - conversation_count
        - last_contact_conversation_id
        - sentiment
      title: ConversationUserResponseModel
    GetConversationUsersPageResponseModel:
      type: object
      properties:
        users:
          type: array
          items:
            $ref: '#/components/schemas/ConversationUserResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - users
        - has_more
      title: GetConversationUsersPageResponseModel
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
  "users": [
    {
      "user_id": "string",
      "last_contact_unix_secs": 1,
      "first_contact_unix_secs": 1,
      "conversation_count": 1,
      "last_contact_conversation_id": "string",
      "sentiment": {
        "scored_conversation_count": 1,
        "positive_count": 1,
        "neutral_count": 1,
        "negative_count": 1,
        "average_sentiment_score": 1.1,
        "average_frustration_score": 1.1
      },
      "last_contact_agent_id": "string",
      "last_contact_agent_name": "string",
      "most_frustrated_conversations": [
        {
          "conversation_id": "string",
          "agent_id": "string",
          "start_time_unix_secs": 1,
          "overall_label": "positive",
          "overall_sentiment_score": 1.1,
          "overall_frustration_score": 1.1
        }
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.users.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.users.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/users"

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

url = URI("https://api.elevenlabs.io/v1/convai/users")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/users")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/users');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/users");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/users")! as URL,
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
