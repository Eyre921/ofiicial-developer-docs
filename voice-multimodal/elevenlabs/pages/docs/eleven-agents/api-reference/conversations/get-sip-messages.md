---
title: "Get SIP messages for a conversation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-sip-messages.md
path: docs/eleven-agents/api-reference/conversations/get-sip-messages
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get SIP messages for a conversation

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/sip-messages

Get SIP messages associated with a conversation's phone call

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-sip-messages

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversations/{conversation_id}/sip-messages:
    get:
      operationId: get_sip_messages
      summary: Get Sip Messages For A Conversation
      description: Get SIP messages associated with a conversation's phone call
      tags:
        - subpackage_conversationalAi/conversations
      parameters:
        - name: conversation_id
          in: path
          description: The id of the conversation you're taking the action on.
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          required: false
          schema:
            type: integer
            default: 20
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
                $ref: '#/components/schemas/type_:GetSipLogMessagesResponse'
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
    type_:SipLogMessageDirection:
      type: string
      enum:
        - in
        - out
      title: SipLogMessageDirection
    type_:SipLogMessage:
      type: object
      properties:
        call_id:
          type: string
        phone_numbers:
          type: array
          items:
            type: string
        local_address:
          type: string
        remote_address:
          type: string
        transport:
          type: string
        raw_message:
          type: string
        error_message:
          type: string
        direction:
          $ref: '#/components/schemas/type_:SipLogMessageDirection'
        created_at_unix_micro:
          type: integer
      required:
        - call_id
        - phone_numbers
        - local_address
        - remote_address
        - transport
        - raw_message
        - error_message
        - direction
        - created_at_unix_micro
      title: SipLogMessage
    type_:GetSipLogMessagesResponse:
      type: object
      properties:
        sip_messages:
          type: array
          items:
            $ref: '#/components/schemas/type_:SipLogMessage'
        next_cursor:
          type: string
        has_more:
          type: boolean
          default: false
      required:
        - sip_messages
      title: GetSipLogMessagesResponse
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
  "sip_messages": [
    {
      "call_id": "call_id",
      "phone_numbers": [
        "phone_numbers"
      ],
      "local_address": "local_address",
      "remote_address": "remote_address",
      "transport": "transport",
      "raw_message": "raw_message",
      "error_message": "error_message",
      "direction": "in",
      "created_at_unix_micro": 1
    }
  ],
  "next_cursor": "next_cursor",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.getSipMessages("21m00Tcm4TlvDq8ikWAM", {
        cursor: "cursor",
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.get_sip_messages(
    conversation_id="21m00Tcm4TlvDq8ikWAM",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages?cursor=cursor&page_size=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages?cursor=cursor&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages?cursor=cursor&page_size=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages?cursor=cursor&page_size=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages?cursor=cursor&page_size=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages?cursor=cursor&page_size=1")! as URL,
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
