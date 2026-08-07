---
title: "List environment variables"
source: https://elevenlabs.io/docs/api-reference/environment-variables/list.md
path: docs/api-reference/environment-variables/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List environment variables

GET https://api.elevenlabs.io/v1/convai/environment-variables

List all environment variables for the workspace with optional filtering

Reference: https://elevenlabs.io/docs/api-reference/environment-variables/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Pagination cursor from previous response
- `page_size` (integer, optional, default: 100) — Number of items to return (1-100)
- `label` (string, optional, nullable) — Filter by exact label match
- `environment` (string, optional, nullable) — Filter to only return variables that have this environment. When specified, the values dict in the response will only contain this environment.
- `type` (enum, optional, nullable) — Filter by variable type
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
  - `created_by_user_id` (string, optional, nullable)
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Examples

**Response**

```json
{
  "environment_variables": [
    {
      "label": "string",
      "created_at_unix_secs": 1,
      "updated_at_unix_secs": 1,
      "type": "string",
      "id": "string",
      "workspace_id": "string",
      "values": {},
      "created_by_user_id": "string"
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.environment_variables.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/environment-variables"

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables")! as URL,
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
