---
title: "List environment variables"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list.md
path: docs/eleven-agents/api-reference/environment-variables/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List environment variables

GET https://api.elevenlabs.io/v1/convai/environment-variables

List all environment variables for the workspace with optional filtering

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional) — Pagination cursor from previous response
- `page_size` (integer, optional, default: 100) — Number of items to return (1-100)
- `label` (string, optional) — Filter by exact label match
- `environment` (string, optional) — Filter to only return variables that have this environment. When specified, the values dict in the response will only contain this environment.
- `type` (enum, optional) — Filter by variable type
  - Allowed values: `string`, `secret`, `auth_connection`

## Response

### 200

Successful Response

- `environment_variables` (list of object, required)
  - `label` (string, required)
  - `created_at_unix_secs` (integer, required)
  - `updated_at_unix_secs` (integer, required)
  - `type` (enum, required)
    - Allowed values: `string`, `secret`, `auth_connection`
  - `id` (string, required)
  - `workspace_id` (string, required)
  - `values` (map from string to string or map from string to object or map from string to object, required)
  - `created_by_user_id` (string, optional)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "environment_variables": [
    {
      "label": "API_ENDPOINT",
      "created_at_unix_secs": 1685000000,
      "updated_at_unix_secs": 1687600000,
      "type": "string",
      "id": "envvar_123abc456def",
      "workspace_id": "workspace_789xyz123",
      "values": {
        "production": "https://api.production.example.com",
        "staging": "https://api.staging.example.com"
      },
      "created_by_user_id": "user_987654321"
    }
  ],
  "has_more": false,
  "next_cursor": "cursor_abcdef123456"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.list({
        cursor: "cursor",
        environment: "environment",
        label: "label",
        pageSize: 1,
        type: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.environment_variables.list(
    cursor="cursor",
    environment="environment",
    label="label",
    page_size=1,
    type="string",
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

	url := "https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
