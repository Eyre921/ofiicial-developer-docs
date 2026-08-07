---
title: "Get character metrics usage"
source: https://elevenlabs.io/docs/api-reference/legacy/usage/get.md
path: docs/api-reference/legacy/usage/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get character metrics usage

GET https://api.elevenlabs.io/v1/usage/character-stats

(Deprecated) This endpoint is deprecated. Use /v1/workspace/analytics/query/usage-by-product-over-time instead, which exposes the bucket size as `interval_seconds` (an integer in seconds) rather than `aggregation_interval`. Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type "voice" will return the usage of each voice for each interval along the time axis.

Reference: https://elevenlabs.io/docs/api-reference/legacy/usage/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `start_unix` (integer, required) — UTC Unix timestamp for the start of the usage window, in milliseconds. To include the first day of the window, the timestamp should be at 00:00:00 of that day.
- `end_unix` (integer, required) — UTC Unix timestamp for the end of the usage window, in milliseconds. To include the last day of the window, the timestamp should be at 23:59:59 of that day.
- `include_workspace_metrics` (boolean, optional, default: false) — Whether or not to include the statistics of the entire workspace.
- `breakdown_type` (enum, optional) — How to break down the information. Cannot be "user" if include_workspace_metrics is False.
  - Allowed values: `none`, `voice`, `voice_multiplier`, `user`, `groups`, `api_keys`, `all_api_keys`, `product_type`, `model`, `resource`, `request_queue`, `region`, `subresource_id`, `reporting_workspace_id`, `has_api_key`, `request_source`
- `aggregation_interval` (enum, optional) — How to aggregate usage data over time. Can be "hour", "day", "week", "month", or "cumulative".
  - Allowed values: `hour`, `day`, `week`, `month`, `cumulative`
- `aggregation_bucket_size` (integer, optional, nullable) — Aggregation bucket size in seconds. Overrides the aggregation interval.
- `metric` (enum, optional) — Which metric to aggregate.
  - Allowed values: `credits`, `tts_characters`, `minutes_used`, `request_count`, `ttfb_avg`, `ttfb_p95`, `fiat_units_spent`, `concurrency`, `concurrency_average`

## Response

### 200

Successful Response

- `time` (list of integer, required) — The time axis with unix timestamps for each day.
- `usage` (map from string to list of double, required) — The usage of each breakdown type along the time axis.

## Examples

**Response**

```json
{
  "time": [
    1738252091000,
    1739404800000
  ],
  "usage": {
    "All": [
      49,
      1053
    ]
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.usage.get({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.usage.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/usage/character-stats?end_unix=1688165999&start_unix=1685574000"

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

url = URI("https://api.elevenlabs.io/v1/usage/character-stats?end_unix=1688165999&start_unix=1685574000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/usage/character-stats?end_unix=1688165999&start_unix=1685574000")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/usage/character-stats?end_unix=1688165999&start_unix=1685574000');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/usage/character-stats?end_unix=1688165999&start_unix=1685574000");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/usage/character-stats?end_unix=1688165999&start_unix=1685574000")! as URL,
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
