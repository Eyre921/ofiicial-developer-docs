---
title: "List attention items"
source: https://elevenlabs.io/docs/api-reference/campaigns/attention/list.md
path: docs/api-reference/campaigns/attention/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List attention items

GET https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention

List problems in the workspace's outbound campaigns that need you to act, such as an agent or phone number that can no longer be used, newest first. A campaign with an open item holds back the calls it affects.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/attention/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `campaign_id` (string, optional, nullable) — Only this campaign's items.
- `include_resolved` (boolean, optional, default: false) — Include items that are already resolved.
- `page_size` (integer, optional, default: 100) — How many items to return at most.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `attention` (list of AttentionView, required)
- `next_cursor` (string, required, nullable)
- `has_more` (boolean, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AttentionView

- `attention_id` (string, required)
- `campaign_id` (string, required)
- `reason` (string, required) — The cause, such as `agent_unavailable` or `phone_number_unavailable`.
- `detail` (string, required) — What went wrong and how to fix it.
- `status` (enum, required)
  - Allowed values: `open`, `resolved`, `retrying`
- `retryable` (boolean, required) — Whether a retry places the calls the item holds back. Items that can't be retried are closed by resolving them.
- `resolution` (string, required, nullable) — The note recorded on resolving the item.
- `created_at_unix` (integer, required)
- `updated_at_unix` (integer, required)

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
  "attention": [
    {
      "attention_id": "string",
      "campaign_id": "string",
      "reason": "string",
      "detail": "string",
      "status": "open",
      "retryable": true,
      "resolution": "string",
      "created_at_unix": 1,
      "updated_at_unix": 1
    }
  ],
  "next_cursor": "string",
  "has_more": true
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention';
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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention"

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention")! as URL,
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
