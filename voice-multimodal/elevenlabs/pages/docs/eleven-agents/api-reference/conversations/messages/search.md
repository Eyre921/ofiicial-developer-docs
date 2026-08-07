---
title: "Smart search"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/messages/search.md
path: docs/eleven-agents/api-reference/conversations/messages/search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Smart search

GET https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search

Search conversation transcripts by semantic similarity to surface relevant messages based on meaning and intent, rather than exact keyword matches

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/messages/search

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `text_query` (string, required) — The search query text for semantic similarity matching
- `agent_id` (string, optional) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `page_size` (integer, optional, default: 20) — Number of results per page. Max 50.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `results` (list of object, required)
  - `conversation_id` (string, required)
  - `agent_id` (string, required)
  - `transcript_index` (integer, required)
  - `chunk_text` (string, required)
  - `score` (double, required)
  - `conversation_start_time_unix_secs` (integer, required)
  - `agent_name` (string, optional)
  - `chunk_highlights` (list of object, optional)
    - `value` (string, required)
    - `is_hit` (boolean, required)
- `has_more` (boolean, required) — Whether there are more results available
- `meta` (object, optional)
  - `total` (integer, optional)
  - `page` (integer, optional)
  - `page_size` (integer, optional)
- `next_cursor` (string, optional) — Cursor for the next page of results

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "results": [
    {
      "conversation_id": "conv_9f8b7a6c5d4e3f2a1b0c",
      "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "transcript_index": 5,
      "chunk_text": "I understand you want to cancel your order and request a refund. Let me check the details for you.",
      "score": 0.92,
      "conversation_start_time_unix_secs": 1685000000,
      "agent_name": "Support Agent John",
      "chunk_highlights": null
    }
  ],
  "has_more": false,
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 10
  },
  "next_cursor": "cursor_abcdef1234567890"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "sk_live_1234567890abcdef",
    });
    await client.conversationalAi.conversations.messages.search({
        agentId: "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        cursor: "cursor",
        pageSize: 10,
        textQuery: "Customer requesting refund for a cancelled order",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="sk_live_1234567890abcdef",
)

client.conversational_ai.conversations.messages.search(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    cursor="cursor",
    page_size=10,
    text_query="Customer requesting refund for a cancelled order",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk_live_1234567890abcdef")
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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk_live_1234567890abcdef'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order")
  .header("xi-api-key", "sk_live_1234567890abcdef")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk_live_1234567890abcdef',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk_live_1234567890abcdef");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk_live_1234567890abcdef",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&cursor=cursor&page_size=10&text_query=Customer+requesting+refund+for+a+cancelled+order")! as URL,
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
