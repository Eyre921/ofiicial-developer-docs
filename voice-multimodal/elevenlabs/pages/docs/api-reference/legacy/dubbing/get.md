---
title: "Get dubbing"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/get.md
path: docs/api-reference/legacy/dubbing/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dubbing

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}

Returns metadata about a dubbing project, including whether it's still in progress or not

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `dubbing_id` (string, required) — ID of the dubbing project.

## Response

### 200

Successful Response

- `dubbing_id` (string, required) — The ID of the dubbing project.
- `name` (string, required) — The name of the dubbing project.
- `status` (string, required) — The state this dub is in.
- `source_language` (string, required, nullable) — Once dubbing has completed, the ISO-639-1 code of the original media's source language.
- `target_languages` (list of string, required) — The ISO-639-1 code of the languages this media has been dubbed into.
- `created_at` (string, required) — Timestamp this dub was created.
- `editable` (boolean, optional, default: false) — Whether this dubbing project is editable in Dubbing Studio.
- `media_metadata` (object, optional, nullable) — Metadata, such as the length in seconds and content type, of the dubbed content.
  - `content_type` (string, required) — The content type of the media.
  - `duration` (double, required) — The duration of the media in seconds.
- `error` (string, optional, nullable) — Error message indicate, if this dub has failed, what happened.

## Examples

**Response**

```json
{
  "dubbing_id": "21m00Tcm4TlvDq8ikWAM",
  "name": "My Dubbing Project",
  "status": "dubbed",
  "source_language": "en",
  "target_languages": [
    "es",
    "fr",
    "de"
  ],
  "created_at": "2025-07-15T14:49:41.149000",
  "editable": true,
  "media_metadata": {
    "content_type": "video/mp4",
    "duration": 127.5
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.get("dubbing_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.get(
    dubbing_id="dubbing_id",
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id")! as URL,
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
