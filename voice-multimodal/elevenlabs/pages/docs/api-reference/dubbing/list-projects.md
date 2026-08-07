---
title: "List projects"
source: https://elevenlabs.io/docs/api-reference/dubbing/list-projects.md
path: docs/api-reference/dubbing/list-projects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List projects

GET https://api.elevenlabs.io/v1/dubbing/project

List the workspace's dubbing projects (cursor-paginated).

Reference: https://elevenlabs.io/docs/api-reference/dubbing/list-projects

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Pagination cursor from a previous response's next_cursor.
- `page_size` (integer, optional, default: 20) — Number of projects per page (max 100).
- `status` (string, optional, nullable) — Filter to projects in this status (preparing, ready, failed).
- `sort_direction` (enum, optional, default: DESCENDING) — Sort by creation time (default 'DESCENDING').
  - Allowed values: `ASCENDING`, `DESCENDING`

## Response

### 200

Successful Response

- `projects` (list of object, required) — The page of dubbing projects the caller can access.
  - `project_id` (string, required) — Unique identifier of the dubbing project.
  - `status` (enum, required) — Lifecycle status of the project: 'preparing'/'processing' while it transcribes, 'ready' once transcription is done, or 'failed'.
    - Allowed values: `queued`, `preparing`, `processing`, `ready`, `failed`
  - `revision` (integer, required) — Monotonic counter incremented whenever the source transcript is edited (segment add/edit/delete).
  - `created_at` (string, required) — When the project was created.
  - `updated_at` (string, required) — When the project was last updated.
  - `reference` (string, optional, nullable) — Optional free-form string the customer can provide to identify the project on their end.
  - `source_language` (string, optional, nullable) — BCP-47 language tag of the source media (null if auto-detected).
  - `model_id` (string, optional, nullable) — Default dubbing model id applied to this project's language targets.
  - `media` (object, optional, nullable) — Source media metadata; null until the project is ready.
    - `filename` (string, optional, nullable) — Original filename of the uploaded source media (null for URL sources).
    - `duration_s` (double, optional, nullable) — Duration of the source media in seconds.
    - `has_video` (boolean, optional, nullable) — Whether the source media contains a video stream.
    - `mime_type` (string, optional, nullable) — MIME type of the uploaded source media.
  - `language_ids` (list of string, optional, default: []) — Identifiers of the language targets created under this project.
  - `webhook_ids` (list of string, optional, default: []) — Workspace webhooks notified when this project becomes ready or fails, and when any of its languages completes or fails.
  - `error` (object, optional, nullable) — Why the project failed; null unless `status` is 'failed'. Also null for the few projects that failed before failure reporting was introduced.
    - `code` (string, required) — Stable identifier for the failure, safe to branch on. New codes are added over time, so treat an unrecognized value as 'internal_error'.
    - `message` (string, required) — Human-readable description of the failure, for display. The wording may change at any time; branch on `code` instead.
    - `retryable` (boolean, required) — Whether resubmitting the same input could succeed. False means the failure describes the input or the account, so an identical retry will fail the same way.
  - `warnings` (list of object, optional) — Non-fatal conditions raised while preparing the source, empty when there are none. Reflects the latest preparation. Conditions raised while dubbing a particular language are reported on that language instead.
    - `type` ("voices_not_permitted", required) — Identifies this warning; branch on it to read the fields below.
    - `speaker_ids` (list of string, required) — Speakers whose voices were not permitted for cloning. The dub used a replacement voice for each of them; the rest of the speakers are unaffected.
    - `message` (string, required) — Human-readable description of the warning, for display. The wording may change at any time; branch on `type` instead.
- `next_cursor` (string, optional, nullable) — Cursor for the next page, or null when there are no more results.

## Examples

**Response**

```json
{
  "projects": [
    {
      "project_id": "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
      "status": "ready",
      "revision": 3,
      "created_at": "2026-07-03T10:15:30Z",
      "updated_at": "2026-07-03T10:17:12Z",
      "reference": "Q3 marketing video",
      "source_language": "en",
      "model_id": "dubbing_v2",
      "media": {
        "filename": "promo.mp4",
        "duration_s": 42.5,
        "has_video": true,
        "mime_type": "video/mp4"
      },
      "language_ids": [
        "lang_1001kwkyxp0je6ktn4knsfrasx5s"
      ],
      "webhook_ids": [],
      "warnings": [
        {
          "type": "voices_not_permitted",
          "speaker_ids": [
            "speaker_1"
          ],
          "message": "Voice cloning was not permitted for speaker speaker_1, so a replacement voice was used."
        }
      ]
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.list({
        pageSize: 20,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.list(
    page_size=20,
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

	url := "https://api.elevenlabs.io/v1/dubbing/project?page_size=20"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project?page_size=20")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project?page_size=20")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project?page_size=20');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project?page_size=20");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project?page_size=20")! as URL,
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
