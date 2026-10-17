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
- `branch_id` (string, optional, nullable) — Filter conversations by branch ID.
- `page_size` (integer, optional, default: 20) — Number of results per page. Max 50.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `results` (list of MessagesSearchResult, required)
- `has_more` (boolean, required) — Whether there are more results available
- `meta` (ListResponseMeta, optional)
- `next_cursor` (string, optional, nullable) — Cursor for the next page of results

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### MessagesSearchResult

transcript_index: index of the message in the conversation transcript chunk_text: text of the transcript; transcript messages if very long could have several chunks. chunk_highlights: chunk_text split into matched/unmatched segments for highlighting. Only populated for keyword/text search, not semantic search. score: similarity score of the message to the search query

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `transcript_index` (integer, required)
- `chunk_text` (string, required)
- `score` (double, required)
- `conversation_start_time_unix_secs` (integer, required)
- `agent_name` (string, optional, nullable)
- `chunk_highlights` (list of SearchHighlightSegment, optional, nullable)

### ListResponseMeta

- `total` (integer, optional, nullable)
- `page` (integer, optional, nullable)
- `page_size` (integer, optional, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### SearchHighlightSegment

- `value` (string, required)
- `is_hit` (boolean, required)

### ValidationErrorLocItems

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
      "conversation_id": "conv_8f3k2mxp9qr1tz5wy6nb4jdce7",
      "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "transcript_index": 5,
      "chunk_text": "I'd like to cancel my subscription and get a full refund for the charges on my account this month.",
      "score": 0.9423,
      "conversation_start_time_unix_secs": 1711900800,
      "agent_name": "Customer Support Agent",
      "chunk_highlights": [
        {
          "value": "I'd like to ",
          "is_hit": false
        },
        {
          "value": "cancel my subscription and get a full refund",
          "is_hit": true
        },
        {
          "value": " for the charges on my account this month.",
          "is_hit": false
        }
      ]
    }
  ],
  "has_more": true,
  "meta": {
    "total": 47,
    "page": 1,
    "page_size": 20
  },
  "next_cursor": "eyJwYWdlIjoyLCJwYWdlX3NpemUiOjIwfQ=="
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search"

querystring = {"agent_id":"agent_3701k3ttaq12ewp8b7qv5rfyszkz","text_query":"Customer asking to cancel and get money back"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back';
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&text_query=Customer+asking+to+cancel+and+get+money+back")! as URL,
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
