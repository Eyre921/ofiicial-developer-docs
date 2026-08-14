---
title: "Get conversation summary"
source: https://elevenlabs.io/docs/api-reference/conversations/get-summary.md
path: docs/api-reference/conversations/get-summary
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get conversation summary

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/summary

Get a lightweight summary of a conversation: its title, the generated transcript summary, whether the call was successful, and — only when the conversation is short — the plain chat messages. Tool calls, tool results, and contextual updates are omitted so the response stays small. Use this instead of the full conversation endpoint when you only need the gist (e.g. an agent reading many conversations); use GET /v1/convai/conversations/\{conversation\_id} when you need the full transcript with tool calls and contextual updates.

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-summary

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

- `max_messages` (integer, optional, default: 40) — Maximum number of chat message turns to include inline. When the conversation has more than this, the messages are omitted and messages_omitted is set.

## Response

### 200

Successful Response

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `message_count` (integer, required) — Number of plain chat message turns in the conversation.
- `note` (string, required) — Guidance telling the agent how to get the full transcript.
- `call_summary_title` (string, optional, nullable) — Short generated title for the conversation.
- `transcript_summary` (string, optional, nullable) — Generated natural-language summary of the call.
- `call_successful` (enum, optional, nullable)
  - Allowed values: `success`, `failure`, `unknown`
- `messages` (list of object, optional, nullable) — The plain chat messages (role and text only). Included only when message_count does not exceed the requested max_messages; otherwise null and messages_omitted is true.
  - `role` (enum, required)
    - Allowed values: `user`, `agent`
  - `message` (string, required)
- `messages_omitted` (boolean, optional, default: false) — True when the chat messages were omitted because the conversation was too long. Fetch the full transcript for the messages.

## Examples

**Response**

```json
{
  "conversation_id": "string",
  "agent_id": "string",
  "status": "initiated",
  "message_count": 1,
  "note": "string",
  "call_summary_title": "string",
  "transcript_summary": "string",
  "call_successful": "success",
  "messages": [
    {
      "role": "user",
      "message": "string"
    }
  ],
  "messages_omitted": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.getSummary("conversation_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.get_summary(
    conversation_id="conversation_id",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/summary"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/summary")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/summary")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/summary');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/summary");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/summary")! as URL,
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
