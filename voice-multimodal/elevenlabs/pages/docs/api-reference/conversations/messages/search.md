---
title: "Smart search"
source: https://elevenlabs.io/docs/api-reference/conversations/messages/search.md
path: docs/api-reference/conversations/messages/search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Smart search

GET https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search

Search conversation transcripts by semantic similarity to surface relevant messages based on meaning and intent, rather than exact keyword matches

Reference: https://elevenlabs.io/docs/api-reference/conversations/messages/search

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `text_query` (string, required) — The search query text for semantic similarity matching
- `agent_id` (string, optional, nullable) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `page_size` (integer, optional, default: 20) — Number of results per page. Max 50.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

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
  - `agent_name` (string, optional, nullable)
  - `chunk_highlights` (list of object, optional, nullable)
    - `value` (string, required)
    - `is_hit` (boolean, required)
- `has_more` (boolean, required) — Whether there are more results available
- `meta` (object, optional)
  - `total` (integer, optional, nullable)
  - `page` (integer, optional, nullable)
  - `page_size` (integer, optional, nullable)
- `next_cursor` (string, optional, nullable) — Cursor for the next page of results

## Examples

**Response**

```json
{
  "results": [
    {
      "conversation_id": "string",
      "agent_id": "string",
      "transcript_index": 1,
      "chunk_text": "string",
      "score": 1.1,
      "conversation_start_time_unix_secs": 1,
      "agent_name": "string",
      "chunk_highlights": [
        {
          "value": "string",
          "is_hit": true
        }
      ]
    }
  ],
  "has_more": true,
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 1
  },
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.messages.search({
        textQuery: "Customer asking to cancel and get money back",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.messages.search(
    text_query="Customer asking to cancel and get money back",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?text_query=Customer+asking+to+cancel+and+get+money+back"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?text_query=Customer+asking+to+cancel+and+get+money+back")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?text_query=Customer+asking+to+cancel+and+get+money+back")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?text_query=Customer+asking+to+cancel+and+get+money+back');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?text_query=Customer+asking+to+cancel+and+get+money+back");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?text_query=Customer+asking+to+cancel+and+get+money+back")! as URL,
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
