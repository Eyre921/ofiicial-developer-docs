---
title: "Get Audio Isolation History"
source: https://elevenlabs.io/docs/api-reference/audio-isolation/list.md
path: docs/api-reference/audio-isolation/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Audio Isolation History

GET https://api.elevenlabs.io/v1/audio-isolation/history

Returns a list of all your audio isolation generations.

Reference: https://elevenlabs.io/docs/api-reference/audio-isolation/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 100) — How many history items to return at maximum. Defaults to 100.
- `page` (integer, optional, default: 1) — Page number for search pagination (1-based). Only used when search is provided.
- `search` (string, optional, nullable) — Optional search term used for filtering audio isolation history (title/text).

## Response

### 200

Successful Response

- `items` (list of object, required)
  - `id` (string, required)
  - `title` (string, required, nullable)
  - `created_at_unix` (integer, required)
  - `format` (string, required)
  - `duration_seconds` (double, required, nullable)
  - `download_url` (string, required, nullable)
  - `icon_url` (string, required, nullable)
  - `source_video_url` (string, required, nullable)
  - `supports_video` (boolean, required)
  - `processing` (boolean, required)
  - `video_processing_failed` (boolean, required)
  - `preview_b64` (string, required, nullable)
- `has_more` (boolean, required)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "items": [
    {
      "id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890",
      "title": "Interview with Dr. Smith - Noise Isolated",
      "created_at_unix": 1685000000,
      "format": "mp3",
      "duration_seconds": 245.7,
      "download_url": "https://cdn.elevenlabs.io/audio-isolation/a1b2c3d4-e5f6-7890-ab12-cd34ef567890.mp3",
      "icon_url": "https://cdn.elevenlabs.io/icons/audio-isolation-icon.png",
      "source_video_url": "https://videos.example.com/interview-dr-smith.mp4",
      "supports_video": true,
      "processing": false,
      "video_processing_failed": false,
      "preview_b64": "UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA="
    }
  ],
  "has_more": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.audioIsolation.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_isolation.list()

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

	url := "https://api.elevenlabs.io/v1/audio-isolation/history"

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

url = URI("https://api.elevenlabs.io/v1/audio-isolation/history")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/audio-isolation/history")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/audio-isolation/history', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-isolation/history");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-isolation/history")! as URL,
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
