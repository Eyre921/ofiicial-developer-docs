---
title: "Get character usage metrics"
source: https://elevenlabs.io/docs/api-reference/usage/get.md
path: docs/api-reference/usage/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get character usage metrics

GET https://api.elevenlabs.io/v1/usage/character-stats

(Deprecated) This endpoint is deprecated. Use /v1/workspace/analytics/query/usage-by-product-over-time instead, which exposes the bucket size as `interval_seconds` (an integer in seconds) rather than `aggregation_interval`. Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type "voice" will return the usage of each voice for each interval along the time axis.

Reference: https://elevenlabs.io/docs/api-reference/usage/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/usage/character-stats:
    get:
      operationId: get
      summary: Get character usage metrics
      description: >-
        (Deprecated) This endpoint is deprecated. Use
        /v1/workspace/analytics/query/usage-by-product-over-time instead, which
        exposes the bucket size as `interval_seconds` (an integer in seconds)
        rather than `aggregation_interval`. Returns the usage metrics for the
        current user or the entire workspace they are part of. The response
        provides a time axis based on the specified aggregation interval
        (default: day), with usage values for each interval along that axis.
        Usage is broken down by the selected breakdown type. For example,
        breakdown type "voice" will return the usage of each voice for each
        interval along the time axis.
      tags:
        - subpackage_usage
      parameters:
        - name: start_unix
          in: query
          description: >-
            UTC Unix timestamp for the start of the usage window, in
            milliseconds. To include the first day of the window, the timestamp
            should be at 00:00:00 of that day.
          required: true
          schema:
            type: integer
        - name: end_unix
          in: query
          description: >-
            UTC Unix timestamp for the end of the usage window, in milliseconds.
            To include the last day of the window, the timestamp should be at
            23:59:59 of that day.
          required: true
          schema:
            type: integer
        - name: include_workspace_metrics
          in: query
          description: Whether or not to include the statistics of the entire workspace.
          required: false
          schema:
            type: boolean
            default: false
        - name: breakdown_type
          in: query
          description: >-
            How to break down the information. Cannot be "user" if
            include_workspace_metrics is False.
          required: false
          schema:
            $ref: '#/components/schemas/BreakdownTypes'
        - name: aggregation_interval
          in: query
          description: >-
            How to aggregate usage data over time. Can be "hour", "day", "week",
            "month", or "cumulative".
          required: false
          schema:
            $ref: '#/components/schemas/UsageAggregationInterval'
        - name: aggregation_bucket_size
          in: query
          description: >-
            Aggregation bucket size in seconds. Overrides the aggregation
            interval.
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: metric
          in: query
          description: Which metric to aggregate.
          required: false
          schema:
            $ref: '#/components/schemas/MetricType'
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsageCharactersResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    BreakdownTypes:
      type: string
      enum:
        - none
        - voice
        - voice_multiplier
        - user
        - groups
        - api_keys
        - all_api_keys
        - product_type
        - model
        - resource
        - request_queue
        - region
        - subresource_id
        - reporting_workspace_id
        - has_api_key
        - request_source
      description: >-
        How to break down the information. Cannot be "user" or "api_key" if
        include_workspace_metrics is False.
      title: BreakdownTypes
    UsageAggregationInterval:
      type: string
      enum:
        - hour
        - day
        - week
        - month
        - cumulative
      description: The time interval over which to aggregate the usage data.
      title: UsageAggregationInterval
    MetricType:
      type: string
      enum:
        - credits
        - tts_characters
        - minutes_used
        - request_count
        - ttfb_avg
        - ttfb_p95
        - fiat_units_spent
        - concurrency
        - concurrency_average
      title: MetricType
    UsageCharactersResponseModel:
      type: object
      properties:
        time:
          type: array
          items:
            type: integer
          description: The time axis with unix timestamps for each day.
        usage:
          type: object
          additionalProperties:
            type: array
            items:
              type: number
              format: double
          description: The usage of each breakdown type along the time axis.
      required:
        - time
        - usage
      title: UsageCharactersResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
