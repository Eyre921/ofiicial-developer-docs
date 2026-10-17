---
title: "Get SIP messages for a conversation"
source: https://elevenlabs.io/docs/api-reference/conversations/get-sip-messages.md
path: docs/api-reference/conversations/get-sip-messages
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get SIP messages for a conversation

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/sip-messages

Get SIP messages associated with a conversation's phone call

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-sip-messages

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_id` (string, required) — The id of the conversation you're taking the action on.

### Query parameters

- `page_size` (integer, optional, default: 20)
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `sip_messages` (list of SIPLogMessage, required)
- `next_cursor` (string, optional, nullable)
- `has_more` (boolean, optional, default: false)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### SIPLogMessage

- `call_id` (string, required)
- `phone_numbers` (list of string, required)
- `local_address` (string, required)
- `remote_address` (string, required)
- `transport` (string, required)
- `raw_message` (string, required)
- `error_message` (string, required)
- `direction` (enum, required)
  - Allowed values: `in`, `out`
- `created_at_unix_micro` (integer, required)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

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
      "call_id": "a3f8c2d1-7b4e-4f9a-b6e2-1c5d8e3f0a2b@192.168.1.100",
      "phone_numbers": [
        "+14155552671",
        "+14155559823"
      ],
      "local_address": "192.168.1.100:5060",
      "remote_address": "203.0.113.45:5060",
      "transport": "UDP",
      "raw_message": "INVITE sip:+14155559823@203.0.113.45 SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.1.100:5060;branch=z9hG4bK776asdhds\r\nFrom: <sip:+14155552671@192.168.1.100>;tag=1928301774\r\nTo: <sip:+14155559823@203.0.113.45>\r\nCall-ID: a3f8c2d1-7b4e-4f9a-b6e2-1c5d8e3f0a2b@192.168.1.100\r\nCSeq: 314159 INVITE\r\nContent-Type: application/sdp\r\nContent-Length: 0\r\n",
      "error_message": "",
      "direction": "in",
      "created_at_unix_micro": 1711900800000000
    }
  ],
  "next_cursor": "eyJjcmVhdGVkX2F0IjoxNzExOTAwODAwMDAwMDAwfQ==",
  "has_more": false
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/sip-messages")! as URL,
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
