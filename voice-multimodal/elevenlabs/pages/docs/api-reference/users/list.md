---
title: "List users"
source: https://elevenlabs.io/docs/api-reference/users/list.md
path: docs/api-reference/users/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List users

GET https://api.elevenlabs.io/v1/convai/users

Get distinct users from conversations with pagination.

Reference: https://elevenlabs.io/docs/api-reference/users/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, optional, nullable) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `branch_id` (string, optional, nullable) — Filter conversations by branch ID.
- `call_start_before_unix` (integer, optional, nullable) — Unix timestamp (in seconds) to filter conversations up to this start date.
- `call_start_after_unix` (integer, optional, nullable) — Unix timestamp (in seconds) to filter conversations after to this start date.
- `search` (string, optional, nullable) — Search/filter by user ID (exact match).
- `page_size` (integer, optional, default: 30) — How many users to return at maximum. Defaults to 30.
- `sort_by` (enum, optional) — The field to sort the results by. Defaults to last_contact_unix_secs.
  - Allowed values: `last_contact_unix_secs`, `conversation_count`, `average_sentiment_score`
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `users` (list of object, required)
  - `user_id` (string, required)
  - `last_contact_unix_secs` (integer, required)
  - `first_contact_unix_secs` (integer, required)
  - `conversation_count` (integer, required)
  - `last_contact_conversation_id` (string, required)
  - `sentiment` (object, required)
    - `scored_conversation_count` (integer, required)
    - `positive_count` (integer, required)
    - `neutral_count` (integer, required)
    - `negative_count` (integer, required)
    - `average_sentiment_score` (double, required, nullable)
    - `average_frustration_score` (double, required, nullable)
    - `recent_scored_conversation_count` (integer, required)
    - `recent_positive_count` (integer, required)
    - `recent_neutral_count` (integer, required)
    - `recent_negative_count` (integer, required)
    - `recent_average_sentiment_score` (double, required, nullable)
    - `recent_average_frustration_score` (double, required, nullable)
  - `last_contact_agent_id` (string, optional, nullable)
  - `last_contact_agent_name` (string, optional, nullable)
  - `most_frustrated_conversations` (list of object, optional)
    - `conversation_id` (string, required)
    - `agent_id` (string, required)
    - `start_time_unix_secs` (integer, required)
    - `overall_label` (enum, required)
      - Allowed values: `positive`, `neutral`, `negative`
    - `overall_sentiment_score` (double, required)
    - `overall_frustration_score` (double, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Examples

**Response**

```json
{
  "users": [
    {
      "user_id": "string",
      "last_contact_unix_secs": 1,
      "first_contact_unix_secs": 1,
      "conversation_count": 1,
      "last_contact_conversation_id": "string",
      "sentiment": {
        "scored_conversation_count": 1,
        "positive_count": 1,
        "neutral_count": 1,
        "negative_count": 1,
        "average_sentiment_score": 1.1,
        "average_frustration_score": 1.1,
        "recent_scored_conversation_count": 1,
        "recent_positive_count": 1,
        "recent_neutral_count": 1,
        "recent_negative_count": 1,
        "recent_average_sentiment_score": 1.1,
        "recent_average_frustration_score": 1.1
      },
      "last_contact_agent_id": "string",
      "last_contact_agent_name": "string",
      "most_frustrated_conversations": [
        {
          "conversation_id": "string",
          "agent_id": "string",
          "start_time_unix_secs": 1,
          "overall_label": "positive",
          "overall_sentiment_score": 1.1,
          "overall_frustration_score": 1.1
        }
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.users.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.users.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/users"

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

url = URI("https://api.elevenlabs.io/v1/convai/users")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/users")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/users');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/users");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/users")! as URL,
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
