---
title: "Get Music Finetunes"
source: https://elevenlabs.io/docs/api-reference/music/finetunes/list.md
path: docs/api-reference/music/finetunes/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Music Finetunes

GET https://api.elevenlabs.io/v1/music/finetunes

List music finetunes accessible to you (your own, workspace-shared, and ElevenLabs-curated), with optional filtering, sorting, and cursor pagination.

Reference: https://elevenlabs.io/docs/api-reference/music/finetunes/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Used for fetching the next page. Cursor is returned in the response.
- `page_size` (integer, optional, default: 50) — How many finetunes to return. Max 100, default 50.
- `visibility` (enum, optional, nullable) — Filter by visibility. 'private' returns private finetunes; 'workspace' returns workspace-shared finetunes; 'public' returns public finetunes, which are currently ElevenLabs curated finetunes. Omit to return all accessible finetunes.
  - Allowed values: `private`, `workspace`, `public`
- `created_by` (enum, optional, nullable) — Filter by creator. 'self' returns finetunes you created; 'workspace' returns finetunes created by workspace teammates; 'elevenlabs' returns ElevenLabs curated finetunes. Omit to return finetunes from all creators.
  - Allowed values: `self`, `workspace`, `elevenlabs`
- `sort` (enum, optional, default: created_at) — Sort by field (created_at or name)
  - Allowed values: `created_at`, `name`
- `sort_direction` (enum, optional, default: desc) — Sort direction (asc or desc)
  - Allowed values: `asc`, `desc`

## Response

### 200

Successful Response

- `finetunes` (list of object, required) — The finetunes in this page.
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
- `next_cursor` (string, required, nullable) — Cursor to pass as `cursor` to fetch the next page; `null` when there are no more results.
- `has_more` (boolean, required) — Whether more finetunes are available beyond this page.

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "finetunes": [
    {
      "id": "ftn_9a8b7c6d5e4f3a2b1c0d",
      "name": "Chillwave Sunset",
      "tags": [
        "chillwave",
        "electronic",
        "ambient"
      ],
      "model_id": "music_v1",
      "created_at": "2024-01-15T09:30:00Z",
      "visibility": "private",
      "created_by": "self",
      "status": "completed",
      "training_progress": 1,
      "primary_genre": "Electronic",
      "failure_reason": null
    }
  ],
  "next_cursor": "eyJwYWdlIjoxLCJpZCI6ImZ0bl85YWJjNmQ1ZTRmM2EyYjFjMGQifQ==",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.finetunes.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.finetunes.list()

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

	url := "https://api.elevenlabs.io/v1/music/finetunes"

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

url = URI("https://api.elevenlabs.io/v1/music/finetunes")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/music/finetunes")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/music/finetunes', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/finetunes");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/finetunes")! as URL,
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
