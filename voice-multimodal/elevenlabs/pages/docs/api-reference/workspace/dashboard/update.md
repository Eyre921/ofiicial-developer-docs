---
title: "Update Convai Dashboard Settings"
source: https://elevenlabs.io/docs/api-reference/workspace/dashboard/update.md
path: docs/api-reference/workspace/dashboard/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Convai Dashboard Settings

PATCH https://api.elevenlabs.io/v1/convai/settings/dashboard
Content-Type: application/json

Update Convai dashboard settings for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/dashboard/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/settings/dashboard:
    patch:
      operationId: update
      summary: Update Convai Dashboard Settings
      description: Update Convai dashboard settings for the workspace
      tags:
        - settings
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
                $ref: '#/components/schemas/GetConvAIDashboardSettingsResponseModel'
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
              $ref: '#/components/schemas/PatchConvAIDashboardSettingsRequest'
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
    PatchConvAiDashboardSettingsRequestChartsItems:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - call_success
              description: 'Discriminator value: call_success'
            name:
              type: string
          required:
            - type
            - name
          description: DashboardCallSuccessChartModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - criteria
              description: 'Discriminator value: criteria'
            name:
              type: string
            criteria_id:
              type: string
          required:
            - type
            - name
            - criteria_id
          description: DashboardCriteriaChartModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - data_collection
              description: 'Discriminator value: data_collection'
            name:
              type: string
            data_collection_id:
              type: string
          required:
            - type
            - name
            - data_collection_id
          description: DashboardDataCollectionChartModel variant
      discriminator:
        propertyName: type
      title: PatchConvAiDashboardSettingsRequestChartsItems
    PatchConvAIDashboardSettingsRequest:
      type: object
      properties:
        charts:
          type: array
          items:
            $ref: >-
              #/components/schemas/PatchConvAiDashboardSettingsRequestChartsItems
      title: PatchConvAIDashboardSettingsRequest
    GetConvAiDashboardSettingsResponseModelChartsItems:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - call_success
              description: 'Discriminator value: call_success'
            name:
              type: string
          required:
            - type
            - name
          description: DashboardCallSuccessChartModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - criteria
              description: 'Discriminator value: criteria'
            name:
              type: string
            criteria_id:
              type: string
          required:
            - type
            - name
            - criteria_id
          description: DashboardCriteriaChartModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - data_collection
              description: 'Discriminator value: data_collection'
            name:
              type: string
            data_collection_id:
              type: string
          required:
            - type
            - name
            - data_collection_id
          description: DashboardDataCollectionChartModel variant
      discriminator:
        propertyName: type
      title: GetConvAiDashboardSettingsResponseModelChartsItems
    GetConvAIDashboardSettingsResponseModel:
      type: object
      properties:
        charts:
          type: array
          items:
            $ref: >-
              #/components/schemas/GetConvAiDashboardSettingsResponseModelChartsItems
      title: GetConvAIDashboardSettingsResponseModel
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
  "charts": [
    {
      "type": "call_success",
      "name": "string"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.dashboard.settings.update({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.dashboard.settings.update()

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

	url := "https://api.elevenlabs.io/v1/convai/settings/dashboard"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/settings/dashboard")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/settings/dashboard")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/settings/dashboard', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings/dashboard");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings/dashboard")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
