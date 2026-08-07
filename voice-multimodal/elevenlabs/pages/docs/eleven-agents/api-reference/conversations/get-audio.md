---
title: "Get conversation audio"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-audio.md
path: docs/eleven-agents/api-reference/conversations/get-audio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get conversation audio

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/audio

Get the audio recording of a particular conversation

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-audio

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_id` (string, required) — The id of the conversation you're taking the action on.

## Response

### 200

Successful Response

- File download.

## Examples

**Request**

```json
{}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "a1b2c3d4e5f67890123456789abcdef0",
    });
    await client.conversationalAi.conversations.audio.get("21m00Tcm4TlvDq8ikWAM");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="a1b2c3d4e5f67890123456789abcdef0",
)

client.conversational_ai.conversations.audio.get(
    conversation_id="21m00Tcm4TlvDq8ikWAM",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/audio"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "a1b2c3d4e5f67890123456789abcdef0")
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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'a1b2c3d4e5f67890123456789abcdef0'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/audio")
  .header("xi-api-key", "a1b2c3d4e5f67890123456789abcdef0")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/audio', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'a1b2c3d4e5f67890123456789abcdef0',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/audio");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "a1b2c3d4e5f67890123456789abcdef0");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "a1b2c3d4e5f67890123456789abcdef0",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/audio")! as URL,
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
