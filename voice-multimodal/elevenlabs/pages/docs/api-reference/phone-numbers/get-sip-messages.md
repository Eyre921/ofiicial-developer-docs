---
title: "Get SIP messages for a phone number"
source: https://elevenlabs.io/docs/api-reference/phone-numbers/get-sip-messages.md
path: docs/api-reference/phone-numbers/get-sip-messages
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get SIP messages for a phone number

GET https://api.elevenlabs.io/v1/convai/phone-numbers/{phone_number_id}/sip-messages

Get SIP messages for a phone number

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/get-sip-messages

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/phone-numbers/{phone_number_id}/sip-messages:
    get:
      operationId: get_sip_messages
      summary: Get Sip Messages For A Phone Number
      description: Get SIP messages for a phone number
      tags:
        - subpackage_conversationalAi/phoneNumbers
      parameters:
        - name: phone_number_id
          in: path
          description: >-
            The phone number ID. This is returned when a phone number is
            imported.
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
                $ref: '#/components/schemas/GetSIPLogMessagesResponse'
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
    SIPLogMessageDirection:
      type: string
      enum:
        - in
        - out
      title: SIPLogMessageDirection
    SIPLogMessage:
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
          $ref: '#/components/schemas/SIPLogMessageDirection'
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
      title: SIPLogMessage
    GetSIPLogMessagesResponse:
      type: object
      properties:
        sip_messages:
          type: array
          items:
            $ref: '#/components/schemas/SIPLogMessage'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
          default: false
      required:
        - sip_messages
      title: GetSIPLogMessagesResponse
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
{}
```

**Response**

```json
{
  "sip_messages": [
    {
      "call_id": "a1b2c3d4e5f67890",
      "phone_numbers": [
        "+14155552671",
        "+14155552672"
      ],
      "local_address": "192.168.1.10:5060",
      "remote_address": "203.0.113.5:5060",
      "transport": "UDP",
      "raw_message": "INVITE sip:+14155552672@domain.com SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.1.10:5060;branch=z9hG4bK776asdhds\r\nFrom: <sip:+14155552671@domain.com>;tag=1928301774\r\nTo: <sip:+14155552672@domain.com>\r\nCall-ID: a1b2c3d4e5f67890@192.168.1.10\r\nCSeq: 1 INVITE\r\nContact: <sip:+14155552671@192.168.1.10:5060>\r\nContent-Length: 0\r\n",
      "error_message": "",
      "direction": "in",
      "created_at_unix_micro": 1687001234567890
    }
  ],
  "next_cursor": "eyJwYWdlIjoxfQ==",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.phoneNumbers.getSipMessages("phone_number_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.phone_numbers.get_sip_messages(
    phone_number_id="phone_number_id",
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id/sip-messages"

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id/sip-messages")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id/sip-messages")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id/sip-messages', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id/sip-messages");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id/sip-messages")! as URL,
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
