---
title: "List dubs"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/list.md
path: docs/api-reference/legacy/dubbing/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List dubs

GET https://api.elevenlabs.io/v1/dubbing

List the dubs you have access to.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.
- `page_size` (integer, optional, default: 100) — How many dubs to return at maximum. Can not exceed 200, defaults to 100.
- `dubbing_status` (enum, optional) — What state the dub is currently in.
  - Allowed values: `dubbing`, `dubbed`, `failed`
- `dubbing_statuses` (list of enum, optional, nullable) — Filter by dubbing status.
  - Allowed values: `queued`, `preparing`, `dubbing`, `dubbed`, `failed`
- `dubbing_models` (list of enum, optional, nullable) — Filter by dubbing model generation.
  - Allowed values: `dubbing_v1`, `dubbing_v2`
- `target_language_codes` (list of string, optional, nullable) — Filter by target language code.
- `creation_sources` (list of enum, optional, nullable) — Filter by dubbing creation source.
  - Allowed values: `flow_node`, `dubbing_ui`, `dubbing_api`
- `filter_by_creator` (enum, optional, default: all) — Filters who created the resources being listed, whether it was the user running the request or someone else that shared the resource with them.
  - Allowed values: `personal`, `others`, `all`
- `order_by` (enum, optional, default: created_at) — The field to use for ordering results from this query.
  - Allowed values: `created_at`, `name`
- `order_direction` (enum, optional, default: DESCENDING) — The order direction to use for results from this query.
  - Allowed values: `DESCENDING`, `ASCENDING`

## Response

### 200

Successful Response

- `dubs` (list of object, required)
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
- `next_cursor` (string, required, nullable)
- `has_more` (boolean, required)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "dubs": [
    {
      "dubbing_id": "3f8a9b2c-7d4e-4f1a-9b2e-5c6d7e8f9a0b",
      "name": "Marketing Video Localization",
      "status": "dubbed",
      "source_language": "en",
      "target_languages": [
        "es",
        "fr",
        "de"
      ],
      "created_at": "2024-01-15T09:30:00Z",
      "editable": true,
      "media_metadata": {
        "content_type": "video/mp4",
        "duration": 125.7
      },
      "error": null
    }
  ],
  "next_cursor": "eyJwYWdlIjoxfQ==",
  "has_more": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.list()

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

	url := "https://api.elevenlabs.io/v1/dubbing"

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

url = URI("https://api.elevenlabs.io/v1/dubbing")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing")! as URL,
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
