---
title: "Send conversation feedback"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/create.md
path: docs/eleven-agents/api-reference/conversations/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Send conversation feedback

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/feedback
Content-Type: application/json

Send the feedback for the given conversation

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_id` (string, required) — The id of the conversation you're taking the action on.

### Body (application/json)

- `feedback` (enum, optional) — Either 'like' or 'dislike' to indicate the feedback for the conversation.
  - Allowed values: `like`, `dislike`

## Response

### 200

Successful Response

- `any`

## Examples

**Request**

```json
{
  "feedback": "like"
}
```

**Response**

```json
{
  "key": "value"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.feedback.create("21m00Tcm4TlvDq8ikWAM", {
        feedback: "like",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.feedback.create(
    conversation_id="21m00Tcm4TlvDq8ikWAM",
    feedback="like",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/feedback"

	payload := strings.NewReader("{\n  \"feedback\": \"like\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/feedback")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"feedback\": \"like\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/feedback")
  .header("Content-Type", "application/json")
  .body("{\n  \"feedback\": \"like\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/feedback', [
  'body' => '{
  "feedback": "like"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/feedback");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"feedback\": \"like\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["feedback": "like"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/feedback")! as URL,
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
