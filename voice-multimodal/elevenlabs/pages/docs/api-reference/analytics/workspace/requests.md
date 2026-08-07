---
title: "List API requests"
source: https://elevenlabs.io/docs/api-reference/analytics/workspace/requests.md
path: docs/api-reference/analytics/workspace/requests
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List API requests

POST https://api.elevenlabs.io/v1/workspace/analytics/requests
Content-Type: application/json

Returns a list of API requests. Supports filtering by time range, column filters, and search terms. At least one of start_time or end_time must be provided. An optional sort parameter controls timestamp ordering. Results are ordered by timestamp. Descending if end_time is used, ascending if start_time is used. The response is a tabular structure with columns, column_types, column_units, and rows.

Reference: https://elevenlabs.io/docs/api-reference/analytics/workspace/requests

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `start_time` (integer, optional, nullable) — Start of the time range as a Unix timestamp in milliseconds.
- `end_time` (integer, optional, nullable) — End of the time range as a Unix timestamp in milliseconds.
- `limit` (integer, optional, default: 100)
- `sort` (enum, optional, nullable) — Optional timestamp sort direction. If omitted, defaults to desc when end_time is provided, otherwise asc.
  - Allowed values: `asc`, `desc`
- `filters` (list of object, optional, nullable)
  - `column` (string, required)
  - `operation` (enum, required)
    - Allowed values: `in`, `not_in`, `le`, `ge`, `lt`, `gt`, `eq`, `neq`
  - `values` (list of string or integer or double or string or boolean, required)
- `search` (string, optional, nullable)

## Response

### 200

Successful Response

- `columns` (list of string, required)
- `column_types` (list of enum, required)
  - Allowed values: `String`, `Float`, `DateTime`, `Int`, `Bool`, `JSON`, `Map`, `Array`
- `rows` (list of list of string or integer or double or boolean or string, required)
- `column_units` (list of enum, required)
  - Allowed values: `ms`, `s`, `min`, `duration`, `credits`, `usd`, `eur`, `inr`, `pln`, `ratio`, `rating`

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "columns": [
    "request_id",
    "timestamp",
    "endpoint",
    "response_time_ms",
    "success"
  ],
  "column_types": [
    "String",
    "DateTime",
    "String",
    "Int",
    "Bool"
  ],
  "rows": [
    [
      "req_1234567890abcdef",
      "2024-06-01T12:34:56Z",
      "/v1/text-to-speech",
      "120",
      "true"
    ],
    [
      "req_abcdef1234567890",
      "2024-06-01T12:35:10Z",
      "/v1/voice/list",
      "85",
      "true"
    ]
  ],
  "column_units": [
    "null",
    "null",
    "null",
    "ms",
    "null"
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.analytics.requests.get({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.analytics.requests.get()

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

	url := "https://api.elevenlabs.io/v1/workspace/analytics/requests"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/analytics/requests")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/analytics/requests")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/analytics/requests', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/analytics/requests");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/analytics/requests")! as URL,
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
