---
title: "Get Video Generation"
source: https://elevenlabs.io/docs/api-reference/flows/video/get.md
path: docs/api-reference/flows/video/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Video Generation

GET https://api.elevenlabs.io/v1/flows/video/{generation_id}

Retrieve the status of a video generation, and retrieve its output URL once completed.

Reference: https://elevenlabs.io/docs/api-reference/flows/video/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `generation_id` (string, required)

## Response

### 200

Successful Response

- `object`
  - `status`: `completed` (MediaGenerationCompletedResponse)
    - `content_mime_type` (string, required) — The MIME type of the generated media.
    - `content_url` (string, required) — A signed URL to download the generated media from. It expires about an hour after this response is returned; fetch the generation again for a fresh URL.
    - `id` (string, required) — The unique identifier of the generation.
  - `status`: `failed` (MediaGenerationFailedResponse)
    - `error_message` (string, required) — A human-readable description of the failure. Failed generations are not charged.
    - `failure_reason` (enum, required) — The category of failure.
      - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
    - `id` (string, required) — The unique identifier of the generation.
  - `status`: `generating` (MediaGenerationInProgressResponse)
    - `id` (string, required) — The unique identifier of the generation.
  - `status`: `pending` (MediaGenerationInProgressResponse)
    - `id` (string, required) — The unique identifier of the generation.

## Examples

**Response**

```json
{
  "status": "generating",
  "id": "JWr5N6X9ZTqf8jD2LmQb"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.video.get("generation_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.video.get(
    generation_id="generation_id",
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

	url := "https://api.elevenlabs.io/v1/flows/video/generation_id"

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

url = URI("https://api.elevenlabs.io/v1/flows/video/generation_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/flows/video/generation_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/flows/video/generation_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/video/generation_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/video/generation_id")! as URL,
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
