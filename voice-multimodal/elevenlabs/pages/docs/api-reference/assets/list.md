---
title: "List Assets"
source: https://elevenlabs.io/docs/api-reference/assets/list.md
path: docs/api-reference/assets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Assets

GET https://api.elevenlabs.io/v1/assets

List assets in the workspace, most recently created first.

Reference: https://elevenlabs.io/docs/api-reference/assets/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 30) — Number of assets to return.
- `cursor` (string, optional, nullable) — Token from a previous response's `next_cursor`. Omit to fetch the first page.
- `search` (string, optional, nullable) — Optional free-text search filter over asset names.

## Response

### 200

Successful Response

- `assets` (list of object, required) — List of Asset objects.
  - `asset_id` (string, required) — Unique identifier for the asset.
  - `name` (string, required) — Display name of the asset.
  - `mime_type` (string, required) — MIME type of the uploaded file (e.g. `audio/mpeg`).
  - `created_at_unix` (integer, required) — Unix timestamp (seconds) the asset was created.
  - `content_url` (string, required, nullable) — Signed URL to fetch the asset's content. May be `null` if the asset has not finished processing. Do not rely on it being valid for more than 1 hour; fetch the asset again for a fresh URL.
- `next_cursor` (string, required, nullable) — Pass as `cursor` to fetch the next page. `null` if there are no more results.
- `has_more` (boolean, required) — Whether there are more results to fetch.

## Examples

**Response**

```json
{
  "assets": [
    {
      "asset_id": "5xM2KqOnZyce22SPZ9d4",
      "name": "podcast-intro.mp3",
      "mime_type": "audio/mpeg",
      "created_at_unix": 1721520000,
      "content_url": "https://.../a1b2c3d4/content?..."
    }
  ],
  "next_cursor": "eyJvZmZzZXQiOjEwfQ",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.assets.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.assets.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/assets"

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

url = URI("https://api.elevenlabs.io/v1/assets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/assets")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/assets');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/assets");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/assets")! as URL,
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
