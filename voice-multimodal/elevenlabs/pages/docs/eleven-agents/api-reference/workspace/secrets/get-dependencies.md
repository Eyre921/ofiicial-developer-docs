---
title: "Get secret dependencies"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get-dependencies.md
path: docs/eleven-agents/api-reference/workspace/secrets/get-dependencies
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secret dependencies

GET https://api.elevenlabs.io/v1/convai/secrets/{secret_id}/dependencies/{resource_type}

Get paginated list of resources that depend on a specific secret, filtered by resource type.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get-dependencies

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `secret_id` (string, required)
- `resource_type` (enum, required)
  - Allowed values: `tools`, `agents`, `phone_numbers`

### Query parameters

- `page_size` (integer, optional, default: 20) — How many dependency items to return per page.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `dependencies` (list of object or list of object or list of object, required)
- `next_cursor` (string, optional) — Cursor for fetching the next page of dependencies

## Examples

**Response**

```json
{
  "dependencies": [
    {
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "id",
      "name": "name",
      "type": "available"
    }
  ],
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.getDependencies("tools", "secret_id", {
        cursor: "cursor",
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.get_dependencies(
    resource_type="tools",
    secret_id="secret_id",
    cursor="cursor",
    page_size=1,
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools?cursor=cursor&page_size=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools?cursor=cursor&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools?cursor=cursor&page_size=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools?cursor=cursor&page_size=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools?cursor=cursor&page_size=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools?cursor=cursor&page_size=1")! as URL,
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
