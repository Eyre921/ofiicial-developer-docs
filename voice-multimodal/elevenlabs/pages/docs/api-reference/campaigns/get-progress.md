---
title: "Get campaign progress"
source: https://elevenlabs.io/docs/api-reference/campaigns/get-progress.md
path: docs/api-reference/campaigns/get-progress
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get campaign progress

GET https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/{campaign_id}/progress

Get where an outbound campaign's leads and calls stand, and when its next call is due.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/get-progress

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `campaign_id` (string, required)

## Response

### 200

Successful Response

- `leads` (LeadsProgress, required)
- `conversations` (ConversationProgress, required)
- `next_call_time_unix` (integer, required, nullable) — When the next call is due; unset when none is scheduled.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### LeadsProgress

- `total` (integer, required)
- `uncalled` (integer, required) — Unfinished leads whose first call hasn't been placed yet.
- `leads_needing_attention` (integer, required) — Unfinished leads whose next call an attention item holds back.
- `active` (integer, required) — Other unfinished leads: a call under way, awaiting analysis or a follow-up.
- `finished` (integer, required) — Leads that won't be called again.
- `finished_by_disposition` (map from string to integer, required) — Finished leads by why they finished. Missing keys mean none.

### ConversationProgress

- `scheduled` (integer, required) — Calls due to be placed that haven't started.
- `scheduled_by_type` (map from string to integer, required) — Scheduled calls by call type. Missing keys mean none.
- `awaiting_permission` (integer, required) — WhatsApp calls waiting on the contact to grant call permission.
- `in_progress` (integer, required) — Calls under way.
- `awaiting_analysis` (integer, required) — Ended calls whose analysis the campaign is waiting on.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

- string
- integer

## Examples

**Response**

```json
{
  "leads": {
    "total": 1,
    "uncalled": 1,
    "leads_needing_attention": 1,
    "active": 1,
    "finished": 1,
    "finished_by_disposition": {}
  },
  "conversations": {
    "scheduled": 1,
    "scheduled_by_type": {},
    "awaiting_permission": 1,
    "in_progress": 1,
    "awaiting_analysis": 1
  },
  "next_call_time_unix": 1
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress';
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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress"

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/progress")! as URL,
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
