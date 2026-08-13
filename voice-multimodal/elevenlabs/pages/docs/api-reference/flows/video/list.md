---
title: "List Video Generations"
source: https://elevenlabs.io/docs/api-reference/flows/video/list.md
path: docs/api-reference/flows/video/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Video Generations

GET https://api.elevenlabs.io/v1/flows/video

List the video generations created through this API, newest first.

Reference: https://elevenlabs.io/docs/api-reference/flows/video/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Pagination cursor: the `next_cursor` value of the previous page's response. Omit it for the first page.
- `page_size` (integer, optional, default: 30) — How many generations to return per page.
- `status` (enum, optional, nullable) — Only return generations with this lifecycle status.
  - Allowed values: `pending`, `generating`, `completed`, `failed`
- `model_id` (string, optional, nullable) — Only return generations of this model.

## Response

### 200

Successful Response

- `generations` (list of object, required) — The generations on this page, newest first. Each item has the same shape as the corresponding GET endpoint's response.
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
- `next_cursor` (string, required, nullable) — Pass as `cursor` to fetch the next page. `null` when there is no further page.
- `has_more` (boolean, required) — Whether more generations exist beyond this page.

## Examples

**Response**

```json
{
  "generations": [
    {
      "status": "completed",
      "content_mime_type": "video/mp4",
      "content_url": "https://storage.googleapis.com/generations/JWr5N6X9ZTqf8jD2LmQb",
      "id": "JWr5N6X9ZTqf8jD2LmQb"
    },
    {
      "status": "generating",
      "id": "Kx2mP7Y4WVrg9kE3NnRc"
    }
  ],
  "next_cursor": "MjAyNi0wNy0xN1QxMjowMDowMHxLeDJtUDdZNFdWcmc5a0UzTm5SYw",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.video.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.video.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/flows/video"

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

url = URI("https://api.elevenlabs.io/v1/flows/video")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/flows/video")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/flows/video');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/video");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/video")! as URL,
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
