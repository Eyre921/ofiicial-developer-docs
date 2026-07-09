---
title: "Get Workspace Usage"
source: https://elevenlabs.io/docs/api-reference/workspace/usage/get-usage-by-product-over-time.md
path: docs/api-reference/workspace/usage/get-usage-by-product-over-time
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Workspace Usage

POST https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time
Content-Type: application/json

Returns credit usage broken down by product type over time. The response is a tabular structure with columns, column_types, column_units, and rows.

Reference: https://elevenlabs.io/docs/api-reference/workspace/usage/get-usage-by-product-over-time

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/analytics/query/usage-by-product-over-time:
    post:
      operationId: get_usage_by_product_over_time
      summary: Get Workspace Usage
      description: >-
        Returns credit usage broken down by product type over time. The response
        is a tabular structure with columns, column_types, column_units, and
        rows.
      tags:
        - usage
      parameters:
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
                $ref: '#/components/schemas/WorkspaceAnalyticsQueryResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Get_Workspace_Usage_v1_workspace_analytics_query_usage_by_product_over_time_post
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
    BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItems:
      type: string
      enum:
        - product_type
        - model
        - voice_id
        - user_id
        - fiat_currency
        - fiat_charge_type
        - region
        - reporting_workspace_id
        - request_source
        - resource_id
        - subresource_id
        - request_queue_type
        - voice_multiplier
        - hashed_xi_api_key
        - billing_group_id
      title: >-
        BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItems
    ColumnFilterOperation:
      type: string
      enum:
        - in
        - not_in
        - le
        - ge
        - lt
        - gt
        - eq
        - neq
      title: ColumnFilterOperation
    ColumnFilterValuesItems:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: string
          format: date-time
        - type: boolean
      title: ColumnFilterValuesItems
    ColumnFilter:
      type: object
      properties:
        column:
          type: string
        operation:
          $ref: '#/components/schemas/ColumnFilterOperation'
        values:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/ColumnFilterValuesItems'
              - type: 'null'
      required:
        - column
        - operation
        - values
      title: ColumnFilter
    Body_Get_Workspace_Usage_v1_workspace_analytics_query_usage_by_product_over_time_post:
      type: object
      properties:
        start_time:
          type: integer
          description: >-
            Start of the time range as a Unix timestamp in milliseconds. Must be
            at least 2020-01-01.
        end_time:
          type: integer
          description: >-
            End of the time range as a Unix timestamp in milliseconds. Must be
            at least 2020-01-01.
        interval_seconds:
          type: integer
          default: 60
          description: >-
            Bucket size in seconds. Each row in the response covers this many
            seconds of the selected time range. For example, pass 3600 for
            hourly buckets or 86400 for daily buckets. Whether `time_zone`
            shifts bucket boundaries depends on this value: whole-day multiples
            (e.g. 86400) align to local midnight; whole-hour multiples up to 24
            hours (e.g. 3600, 14400) align to local hour boundaries from
            midnight; sub-hour values and other sizes remain UTC-anchored
            regardless of `time_zone`.
        group_by:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/BodyGetWorkspaceUsageV1WorkspaceAnalyticsQueryUsageByProductOverTimePostGroupByItems
        filters:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ColumnFilter'
        time_zone:
          type: string
          default: UTC
          description: >-
            IANA time zone identifier (e.g. 'America/New_York', 'Europe/London',
            'UTC') used to align bucket boundaries for eligible
            `interval_seconds` values. Whole-day multiples start at local
            midnight; whole-hour multiples up to 24 hours align to local hour
            boundaries from midnight. Sub-hour intervals and other bucket sizes
            remain UTC-anchored regardless of this setting. Defaults to UTC.
      required:
        - start_time
        - end_time
      title: >-
        Body_Get_Workspace_Usage_v1_workspace_analytics_query_usage_by_product_over_time_post
    WorkspaceAnalyticsQueryResponseModelColumnTypesItems:
      type: string
      enum:
        - String
        - Float
        - DateTime
        - Int
        - Bool
        - JSON
        - Map
        - Array
      title: WorkspaceAnalyticsQueryResponseModelColumnTypesItems
    WorkspaceAnalyticsQueryResponseModelRowsItemsItems:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
        - type: string
          format: date-time
      title: WorkspaceAnalyticsQueryResponseModelRowsItemsItems
    ColumnUnit:
      type: string
      enum:
        - ms
        - s
        - min
        - duration
        - credits
        - usd
        - eur
        - inr
        - pln
        - ratio
        - rating
      title: ColumnUnit
    WorkspaceAnalyticsQueryResponseModel:
      type: object
      properties:
        columns:
          type: array
          items:
            type: string
        column_types:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspaceAnalyticsQueryResponseModelColumnTypesItems
        rows:
          type: array
          items:
            type: array
            items:
              oneOf:
                - $ref: >-
                    #/components/schemas/WorkspaceAnalyticsQueryResponseModelRowsItemsItems
                - type: 'null'
        column_units:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/ColumnUnit'
              - type: 'null'
      required:
        - columns
        - column_types
        - rows
        - column_units
      title: WorkspaceAnalyticsQueryResponseModel
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



**Request**

```json
{
  "start_time": 1680307200000,
  "end_time": 1680393600000
}
```

**Response**

```json
{
  "columns": [
    "timestamp",
    "product_type",
    "credits_used"
  ],
  "column_types": [
    "DateTime",
    "String",
    "Float"
  ],
  "rows": [
    [
      "2024-04-01T00:00:00Z",
      "text_to_speech",
      "125.5"
    ],
    [
      "2024-04-01T01:00:00Z",
      "voice_cloning",
      "75.25"
    ],
    [
      "2024-04-01T02:00:00Z",
      "text_to_speech",
      "98.75"
    ]
  ],
  "column_units": [
    "s",
    "",
    "credits"
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.usage.getUsageByProductOverTime({
        startTime: 1680307200000,
        endTime: 1680393600000,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.usage.get_usage_by_product_over_time(
    start_time=1680307200000,
    end_time=1680393600000,
)

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

	url := "https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time"

	payload := strings.NewReader("{\n  \"start_time\": 1680307200000,\n  \"end_time\": 1680393600000\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"start_time\": 1680307200000,\n  \"end_time\": 1680393600000\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time")
  .header("Content-Type", "application/json")
  .body("{\n  \"start_time\": 1680307200000,\n  \"end_time\": 1680393600000\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time', [
  'body' => '{
  "start_time": 1680307200000,
  "end_time": 1680393600000
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"start_time\": 1680307200000,\n  \"end_time\": 1680393600000\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "start_time": 1680307200000,
  "end_time": 1680393600000
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time")! as URL,
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
