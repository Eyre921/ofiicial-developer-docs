---
title: "Retry attention item"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/attention/retry.md
path: docs/eleven-agents/api-reference/campaigns/attention/retry
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Retry attention item

POST https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/{attention_id}/retry

Place the calls a retryable attention item holds back, once its cause is fixed. Resumes the campaign.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/attention/retry

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `attention_id` (string, required)

## Response

### 200

Successful Response

- `attention_id` (string, required)
- `campaign_id` (string, required)
- `reason` (string, required) — The cause, such as `agent_unavailable` or `phone_number_unavailable`.
- `detail` (string, required) — What went wrong and how to fix it.
- `status` (enum, required)
  - Allowed values: `open`, `resolved`, `retrying`
- `retryable` (boolean, required) — Whether a retry places the calls the item holds back. Items that can't be retried are closed by resolving them.
- `created_at_unix` (integer, required)
- `updated_at_unix` (integer, required)
- `resolution` (string, optional) — The note recorded on resolving the item.

## Errors

### 422 Attention Retry Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

- string
- integer

## Examples

**Response**

```json
{
  "attention_id": "attention_id",
  "campaign_id": "campaign_id",
  "reason": "reason",
  "detail": "detail",
  "status": "open",
  "retryable": true,
  "created_at_unix": 1,
  "updated_at_unix": 1,
  "resolution": "resolution"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry"

response = requests.post(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry';
const options = {method: 'POST'};

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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/retry")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

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
