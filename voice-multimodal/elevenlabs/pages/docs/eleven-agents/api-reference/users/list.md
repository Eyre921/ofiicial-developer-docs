---
title: "List users"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/users/list.md
path: docs/eleven-agents/api-reference/users/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List users

GET https://api.elevenlabs.io/v1/convai/users

Get distinct users from conversations with pagination.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/users/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, optional) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `branch_id` (string, optional) — Filter conversations by branch ID.
- `call_start_before_unix` (integer, optional) — Unix timestamp (in seconds) to filter conversations up to this start date.
- `call_start_after_unix` (integer, optional) — Unix timestamp (in seconds) to filter conversations after to this start date.
- `search` (string, optional) — Search/filter by user ID (exact match).
- `page_size` (integer, optional, default: 30) — How many users to return at maximum. Defaults to 30.
- `sort_by` (enum, optional) — The field to sort the results by. Defaults to last_contact_unix_secs.
  - Allowed values: `last_contact_unix_secs`, `conversation_count`, `average_sentiment_score`
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `users` (list of ConversationUserResponseModel, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Errors

### 422 Users List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ConversationUserResponseModel

- `user_id` (string, required)
- `last_contact_unix_secs` (integer, required)
- `first_contact_unix_secs` (integer, required)
- `conversation_count` (integer, required)
- `last_contact_conversation_id` (string, required)
- `sentiment` (SentimentAggregate, required)
- `last_contact_agent_id` (string, optional)
- `last_contact_agent_name` (string, optional)
- `most_frustrated_conversations` (list of FrustratedConversationRef, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### SentimentAggregate

- `scored_conversation_count` (integer, required)
- `positive_count` (integer, required)
- `neutral_count` (integer, required)
- `negative_count` (integer, required)
- `recent_scored_conversation_count` (integer, required)
- `recent_positive_count` (integer, required)
- `recent_neutral_count` (integer, required)
- `recent_negative_count` (integer, required)
- `average_sentiment_score` (double, optional)
- `average_frustration_score` (double, optional)
- `recent_average_sentiment_score` (double, optional)
- `recent_average_frustration_score` (double, optional)

### FrustratedConversationRef

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `start_time_unix_secs` (integer, required)
- `overall_label` (enum, required)
  - Allowed values: `positive`, `neutral`, `negative`
- `overall_sentiment_score` (double, required)
- `overall_frustration_score` (double, required)

### ValidationErrorLocItem

## Examples

**Response**

```json
{
  "users": [
    {
      "user_id": "user_id",
      "last_contact_unix_secs": 1,
      "first_contact_unix_secs": 1,
      "conversation_count": 1,
      "last_contact_conversation_id": "last_contact_conversation_id",
      "sentiment": {
        "scored_conversation_count": 1,
        "positive_count": 1,
        "neutral_count": 1,
        "negative_count": 1,
        "recent_scored_conversation_count": 1,
        "recent_positive_count": 1,
        "recent_neutral_count": 1,
        "recent_negative_count": 1,
        "average_sentiment_score": null,
        "average_frustration_score": null,
        "recent_average_sentiment_score": null,
        "recent_average_frustration_score": null
      },
      "last_contact_agent_id": "last_contact_agent_id",
      "last_contact_agent_name": "last_contact_agent_name",
      "most_frustrated_conversations": [
        {
          "conversation_id": "conversation_id",
          "agent_id": "agent_id",
          "start_time_unix_secs": 1,
          "overall_label": "positive",
          "overall_sentiment_score": 1.1,
          "overall_frustration_score": 1.1
        }
      ]
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/users"

querystring = {"agent_id":"agent_id","branch_id":"branch_id","call_start_after_unix":"1","call_start_before_unix":"1","cursor":"cursor","page_size":"1","search":"search","sort_by":"last_contact_unix_secs","sort_direction":"asc"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc"

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

url = URI("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/users?agent_id=agent_id&branch_id=branch_id&call_start_after_unix=1&call_start_before_unix=1&cursor=cursor&page_size=1&search=search&sort_by=last_contact_unix_secs&sort_direction=asc")! as URL,
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
