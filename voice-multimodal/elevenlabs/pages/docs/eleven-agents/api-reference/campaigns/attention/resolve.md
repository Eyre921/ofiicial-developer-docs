---
title: "Resolve attention item"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/attention/resolve.md
path: docs/eleven-agents/api-reference/campaigns/attention/resolve
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Resolve attention item

POST https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/{attention_id}/resolve
Content-Type: application/json

Close an attention item that can't be retried, recording how it was handled.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/attention/resolve

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `attention_id` (string, required)

### Body (application/json)

This endpoint expects an object.

- `resolution` (string, required) — How the item was handled.

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

### 422 Attention Resolve Request Unprocessable Entity Error

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

**Request**

```json
{
  "resolution": "resolution"
}
```

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

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve"

payload = { "resolution": "resolution" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"resolution":"resolution"}'
};

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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve"

	payload := strings.NewReader("{\n  \"resolution\": \"resolution\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"resolution\": \"resolution\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve")
  .header("Content-Type", "application/json")
  .body("{\n  \"resolution\": \"resolution\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve', [
  'body' => '{
  "resolution": "resolution"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"resolution\": \"resolution\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["resolution": "resolution"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/attention/attention_id/resolve")! as URL,
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
