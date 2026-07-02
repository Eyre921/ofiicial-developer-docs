---
title: "List tags"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/list.md
path: docs/eleven-agents/api-reference/conversations/tags/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List tags

GET https://api.elevenlabs.io/v1/convai/tags

List conversation tags for the workspace, ordered by most recently created first.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/tags:
    get:
      operationId: list
      summary: List Conversation Tags
      description: >-
        List conversation tags for the workspace, ordered by most recently
        created first.
      tags:
        - subpackage_conversationalAi/conversations/tags
      parameters:
        - name: page_size
          in: query
          description: How many conversation tags to return. Can not exceed 100.
          required: false
          schema:
            type: integer
            default: 100
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
                  #/components/schemas/type_:GetConversationTagsPageResponseModel
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
    type_:ConversationTagResponseModel:
      type: object
      properties:
        tag_id:
          type: string
        workspace_id:
          type: string
        owner_user_id:
          type: string
        title:
          type: string
        description:
          type: string
        created_at_unix_secs:
          type: integer
      required:
        - tag_id
        - workspace_id
        - owner_user_id
        - title
        - created_at_unix_secs
      title: ConversationTagResponseModel
    type_:GetConversationTagsPageResponseModel:
      type: object
      properties:
        conversation_tags:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConversationTagResponseModel'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - conversation_tags
        - has_more
      title: GetConversationTagsPageResponseModel
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
  "conversation_tags": [
    {
      "tag_id": "tag_id",
      "workspace_id": "workspace_id",
      "owner_user_id": "owner_user_id",
      "title": "title",
      "created_at_unix_secs": 1,
      "description": "description"
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.tags.list({
        cursor: "cursor",
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.tags.list(
    cursor="cursor",
    page_size=1,
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

	url := "https://api.elevenlabs.io/v1/convai/tags?cursor=cursor&page_size=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/tags?cursor=cursor&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tags?cursor=cursor&page_size=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tags?cursor=cursor&page_size=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tags?cursor=cursor&page_size=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tags?cursor=cursor&page_size=1")! as URL,
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
