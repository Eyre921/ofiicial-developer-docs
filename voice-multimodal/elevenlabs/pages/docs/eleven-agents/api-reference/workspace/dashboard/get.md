---
title: "Get dashboard settings"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/dashboard/get.md
path: docs/eleven-agents/api-reference/workspace/dashboard/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dashboard settings

GET https://api.elevenlabs.io/v1/convai/settings/dashboard

Retrieve Convai dashboard settings for the workspace

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/dashboard/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/settings/dashboard:
    get:
      operationId: get
      summary: Get Convai Dashboard Settings
      description: Retrieve Convai dashboard settings for the workspace
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
                $ref: >-
                  #/components/schemas/type_:GetConvAiDashboardSettingsResponseModel
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:GetConvAiDashboardSettingsResponseModelChartsItem:
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
      discriminator:
        propertyName: type
      title: GetConvAiDashboardSettingsResponseModelChartsItem
    type_:GetConvAiDashboardSettingsResponseModel:
      type: object
      properties:
        charts:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:GetConvAiDashboardSettingsResponseModelChartsItem
      title: GetConvAiDashboardSettingsResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Response**

```json
{
  "charts": [
    {
      "type": "call_success",
      "name": "name"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.dashboard.settings.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.dashboard.settings.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/settings/dashboard"

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

url = URI("https://api.elevenlabs.io/v1/convai/settings/dashboard")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/settings/dashboard")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings/dashboard');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings/dashboard");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings/dashboard")! as URL,
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
