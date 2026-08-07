---
title: "Get Music Finetune"
source: https://elevenlabs.io/docs/api-reference/music/finetunes/get.md
path: docs/api-reference/music/finetunes/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Music Finetune

GET https://api.elevenlabs.io/v1/music/finetunes/{finetune_id}

Get a music finetune.

Reference: https://elevenlabs.io/docs/api-reference/music/finetunes/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `finetune_id` (string, required)

## Response

### 200

Successful Response

- `id` (string, required) — Unique identifier of the finetune.
- `name` (string, required) — Name of the finetune.
- `tags` (list of string, required) — Tags associated with the finetune.
- `model_id` (string, required) — The base music model the finetune was trained on.
- `created_at` (string, required) — When the finetune was created (UTC).
- `visibility` (enum, required) — Who can access this finetune: `private` (only you), `workspace` (members of your workspace), `public` (ElevenLabs-curated, available to everyone).
  - Allowed values: `private`, `workspace`, `public`
- `created_by` (enum, required) — Who created the finetune: `self`, `workspace`, or `elevenlabs`.
  - Allowed values: `self`, `workspace`, `elevenlabs`
- `status` (enum, required) — Training lifecycle status: pending, in_progress, completed, failed, and blocked.
  - Allowed values: `pending`, `in_progress`, `completed`, `failed`, `blocked`
- `training_progress` (double, required) — Training progress from 0.0 to 1.0.
- `primary_genre` (string, optional, nullable) — Primary musical genre of the finetune.
- `failure_reason` (enum, optional, nullable) — Reason the finetune failed or was blocked, if applicable.
  - Allowed values: `audio_processing_failed`, `copyright_violation`, `training_failed`

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "id": "finetune_8a7c3d2f9b4e4a1d9f6c7b8e",
  "name": "Chillwave Sunset Mix",
  "tags": [
    "chillwave",
    "electronic",
    "sunset vibes"
  ],
  "model_id": "music_v1",
  "created_at": "2024-01-15T09:30:00Z",
  "visibility": "private",
  "created_by": "self",
  "status": "in_progress",
  "training_progress": 0.45,
  "primary_genre": "electronic",
  "failure_reason": null
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.finetunes.get("finetune_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.finetunes.get(
    finetune_id="finetune_id",
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

	url := "https://api.elevenlabs.io/v1/music/finetunes/finetune_id"

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

url = URI("https://api.elevenlabs.io/v1/music/finetunes/finetune_id")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/music/finetunes/finetune_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/music/finetunes/finetune_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/finetunes/finetune_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/finetunes/finetune_id")! as URL,
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
