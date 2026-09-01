---
title: "List language targets"
source: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/list-language-targets.md
path: docs/api-reference/dubbing/language-targets/list-language-targets
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List language targets

GET https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language

List a project's language targets, cursor-paginated, each with signed output URLs once it has produced an output.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/list-language-targets

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the parent dubbing project.

### Query parameters

- `cursor` (string, optional, nullable) — Pass the `next_cursor` from a previous response to fetch the page after it. Omit for the first page.
- `page_size` (integer, optional, default: 20) — Number of language targets per page. Clamped to between 1 and 100 rather than rejected, so a larger value returns a full page.
- `status` (string, optional, nullable) — Filter to targets in this status: `queued`, `processing`, `completed`, `stale`, or `failed`. Omit to return every status.

## Response

### 200

Successful Response

- `languages` (list of object, required) — The page of language targets for the project.
  - `language_id` (string, required) — Unique identifier of the language target.
  - `project_id` (string, required) — Identifier of the parent dubbing project.
  - `target_language` (string, required) — BCP-47 language tag this target is dubbed into.
  - `status` (enum, required) — Lifecycle status: `queued` (waiting on the project to be ready, or on a worker), `processing` while it is being dubbed, `completed` once its output is available, `stale` when the transcript changed after the output was produced, or `failed`.
    - Allowed values: `queued`, `processing`, `completed`, `stale`, `failed`
  - `revision` (integer, required) — Monotonic counter incremented whenever this target's transcript changes (a source edit affecting it, or an edit to its translation).
  - `created_at` (string, required) — When the language target was created.
  - `updated_at` (string, required) — When the language target was last updated.
  - `model_id` (string, optional, nullable) — Dubbing model this target is dubbed with, inherited from the project and not selectable per language.
  - `voice_settings` (object, optional, nullable) — Voice settings applied to every speaker in this language, or null if the defaults apply.
    - `cloning_strength` (integer, optional, default: 7) — How strongly the dubbed speakers clone the source voices, 0 to 10.
  - `outputs` (object, optional, nullable) — Signed output URLs; null until the target has produced an output (present once `completed`, and kept while `stale` — compare `output_revision` against `revision` to tell whether the output is up to date).
    - `lossless_audio` (string, optional, nullable) — Signed URL for the dubbed lossless audio track, in FLAC. The link expires one hour after it is issued; re-read the language target for a fresh one.
  - `output_revision` (integer, optional, nullable) — The `revision` the current dubbed output was generated from; equal to `revision` when up to date, and lower when `stale`. This is null until a generation has completed.
  - `error` (object, optional, nullable) — Why this language failed; null unless `status` is `failed`, and also null for the few languages that failed before failure reporting was introduced. A code of `project_failed` means the parent project failed, so read the project for the underlying cause.
    - `message_type` ("error", required)
    - `error` (string, required)
  - `warnings` (list of object, optional) — Non-fatal conditions raised while dubbing this language, empty when there are none. Reflects the latest generation. Conditions raised while preparing the source are reported on the project instead.
    - `type` ("voices_not_permitted", required) — Identifies this warning; branch on it to read the other fields.
    - `speaker_ids` (list of string, required) — Speakers whose voices were not permitted for cloning. The dub used a replacement voice for each of them; all other speakers are unaffected.
    - `message` (string, required) — Human-readable description of the warning, for display. The wording may change at any time, so we recommend branching on `type` instead.
- `next_cursor` (string, optional, nullable) — Opaque cursor to pass back as `cursor` for the next page, or null when there are no more results.

## Examples

**Response**

```json
{
  "languages": [
    {
      "language_id": "lang_1001kwkyxp0je6ktn4knsfrasx5s",
      "project_id": "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
      "target_language": "es",
      "status": "completed",
      "revision": 3,
      "created_at": "2026-07-03T10:16:00Z",
      "updated_at": "2026-07-03T10:20:45Z",
      "model_id": "dubbing_v2",
      "outputs": {
        "lossless_audio": "https://storage.googleapis.com/eleven-dubbing/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/lang_1001kwkyxp0je6ktn4knsfrasx5s/output.flac?X-Goog-Signature=..."
      },
      "output_revision": 3,
      "warnings": []
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.list("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        pageSize: 20,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.list(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20")! as URL,
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
