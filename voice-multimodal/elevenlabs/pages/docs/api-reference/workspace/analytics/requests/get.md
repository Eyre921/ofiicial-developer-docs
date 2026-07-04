---
title: "List Api Requests"
source: https://elevenlabs.io/docs/api-reference/workspace/analytics/requests/get.md
path: docs/api-reference/workspace/analytics/requests/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Api Requests

POST https://api.elevenlabs.io/v1/workspace/analytics/requests
Content-Type: application/json

Returns a list of API requests. Supports filtering by time range, column filters, and search terms. At least one of start_time or end_time must be provided. An optional sort parameter controls timestamp ordering. Results are ordered by timestamp. Descending if end_time is used, ascending if start_time is used. The response is a tabular structure with columns, column_types, column_units, and rows.

Reference: https://elevenlabs.io/docs/api-reference/workspace/analytics/requests/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/analytics/requests:
    post:
      operationId: get
      summary: List Api Requests
      description: >-
        Returns a list of API requests. Supports filtering by time range, column
        filters, and search terms. At least one of start_time or end_time must
        be provided. An optional sort parameter controls timestamp ordering.
        Results are ordered by timestamp. Descending if end_time is used,
        ascending if start_time is used. The response is a tabular structure
        with columns, column_types, column_units, and rows.
      tags:
        - requests
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
                #/components/schemas/Body_List_API_requests_v1_workspace_analytics_requests_post
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
    BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort:
      type: string
      enum:
        - asc
        - desc
      description: >-
        Optional timestamp sort direction. If omitted, defaults to desc when
        end_time is provided, otherwise asc.
      title: BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort
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
    Body_List_API_requests_v1_workspace_analytics_requests_post:
      type: object
      properties:
        start_time:
          type:
            - integer
            - 'null'
          description: Start of the time range as a Unix timestamp in milliseconds.
        end_time:
          type:
            - integer
            - 'null'
          description: End of the time range as a Unix timestamp in milliseconds.
        limit:
          type: integer
          default: 100
        sort:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyListApiRequestsV1WorkspaceAnalyticsRequestsPostSort
            - type: 'null'
          description: >-
            Optional timestamp sort direction. If omitted, defaults to desc when
            end_time is provided, otherwise asc.
        filters:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ColumnFilter'
        search:
          type:
            - string
            - 'null'
      title: Body_List_API_requests_v1_workspace_analytics_requests_post
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
      "2024-06-01T12:00:00Z",
      "/v1/text-to-speech",
      "250",
      "true"
    ],
    [
      "req_abcdef1234567890",
      "2024-06-01T12:05:00Z",
      "/v1/voice/list",
      "180",
      "true"
    ]
  ],
  "column_units": [
    "",
    "ms",
    "",
    "ms",
    ""
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
