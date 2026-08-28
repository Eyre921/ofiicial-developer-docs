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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `charts` (list of object, optional)
  - `type`: `call_success` (DashboardCallSuccessChartModel)
    - `name` (string, required)
  - `type`: `criteria` (DashboardCriteriaChartModel)
    - `criteria_id` (string, required)
    - `name` (string, required)
  - `type`: `data_collection` (DashboardDataCollectionChartModel)
    - `data_collection_id` (string, required)
    - `name` (string, required)

## Response

### 200

Successful Response

- `charts` (list of object, optional)
  - `type`: `call_success` (DashboardCallSuccessChartModel)
    - `name` (string, required)
  - `type`: `criteria` (DashboardCriteriaChartModel)
    - `criteria_id` (string, required)
    - `name` (string, required)
  - `type`: `data_collection` (DashboardDataCollectionChartModel)
    - `data_collection_id` (string, required)
    - `name` (string, required)

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
