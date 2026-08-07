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
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `sip_messages` (list of object, required)
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
- `next_cursor` (string, optional)
- `has_more` (boolean, optional, default: false)

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
