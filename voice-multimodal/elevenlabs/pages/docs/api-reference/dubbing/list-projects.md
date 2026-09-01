---
title: "List projects"
source: https://elevenlabs.io/docs/api-reference/dubbing/list-projects.md
path: docs/api-reference/dubbing/list-projects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List projects

GET https://api.elevenlabs.io/v1/dubbing/project

List the dubbing projects in your workspace that you can access, newest first, cursor-paginated. Listed projects carry no `language_ids`; fetch a project, or list its language targets, to see them.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/list-projects

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Pass the `next_cursor` from a previous response to fetch the page after it. Omit for the first page.
- `page_size` (integer, optional, default: 20) — Number of projects per page. Clamped to between 1 and 100 rather than rejected, so a larger value returns a full page.
- `status` (string, optional, nullable) — Filter to projects in this status: `queued`, `preparing`, `ready`, or `failed`. Omit to return every status.
- `sort_direction` (enum, optional, default: DESCENDING) — Sort by creation time; newest first by default.
  - Allowed values: `ASCENDING`, `DESCENDING`

## Response

### 200

Successful Response

- `projects` (list of object, required) — The page of dubbing projects the caller can access.
  - `project_id` (string, required) — Unique identifier of the dubbing project.
  - `status` (enum, required) — Lifecycle status of the project: `queued` before the source is picked up, `preparing` while it is transcribed, `ready` once transcription is done and language targets can start, or `failed`. A project is never reported as `processing` — that value belongs to language targets.
    - Allowed values: `queued`, `preparing`, `processing`, `ready`, `failed`
  - `revision` (integer, required) — Monotonic counter incremented whenever the source transcript is edited (segment add/edit/delete).
  - `created_at` (string, required) — When the project was created.
  - `updated_at` (string, required) — When the project was last updated.
  - `reference` (string, optional, nullable) — The free-form string you supplied as `reference` when creating the project, or null if you supplied none.
  - `source_language` (string, optional, nullable) — BCP-47 language tag of the source media (null if auto-detected).
  - `model_id` (string, optional, nullable) — Dubbing model every language target of this project is dubbed with. Fixed at create time and not selectable per language.
  - `media` (object, optional, nullable) — Source media metadata, populated once the source has been fetched and decoded (shortly after create, before the project is `ready`); null until then.
    - `filename` (string, optional, nullable) — Original filename of the uploaded source media (null for URL sources).
    - `duration_s` (double, optional, nullable) — Duration of the source media, in seconds.
    - `has_video` (boolean, optional, nullable) — Whether the source media contains a video stream.
    - `mime_type` (string, optional, nullable) — MIME type of the uploaded source media (null for URL sources).
  - `language_ids` (list of string, optional, default: []) — Identifiers of the language targets under this project. Populated when a single project is fetched, and on create when `target_language` creates one. Always empty in list responses — list the project's language targets instead.
  - `webhook_ids` (list of string, optional, default: []) — IDs of the workspace webhooks notified as this project and its languages reach `ready`, `completed`, or `failed`.
  - `error` (object, optional, nullable) — Why the project failed; null unless `status` is `failed`. Also null for the few projects that failed before failure reporting was introduced.
    - `message_type` ("error", required)
    - `error` (string, required)
  - `warnings` (list of object, optional) — Non-fatal conditions raised while preparing the source, empty when there are none. Reflects the latest preparation. Conditions raised while dubbing a particular language are reported on that language instead.
    - `type` ("voices_not_permitted", required) — Identifies this warning; branch on it to read the other fields.
    - `speaker_ids` (list of string, required) — Speakers whose voices were not permitted for cloning. The dub used a replacement voice for each of them; all other speakers are unaffected.
    - `message` (string, required) — Human-readable description of the warning, for display. The wording may change at any time, so we recommend branching on `type` instead.
- `next_cursor` (string, optional, nullable) — Opaque cursor to pass back as `cursor` for the next page, or null when there are no more results.

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
