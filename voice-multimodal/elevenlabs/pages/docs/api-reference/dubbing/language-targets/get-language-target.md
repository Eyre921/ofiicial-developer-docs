---
title: "Get language target"
source: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/get-language-target.md
path: docs/api-reference/dubbing/language-targets/get-language-target
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get language target

GET https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}

Full language-target detail.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/get-language-target

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the parent dubbing project.
- `language_id` (string, required) — Identifier of the language target to fetch.

## Response

### 200

Successful Response

- `language_id` (string, required) — Unique identifier of the language target.
- `project_id` (string, required) — Identifier of the parent dubbing project.
- `target_language` (string, required) — BCP-47 language tag this target is dubbed into.
- `status` (enum, required) — Lifecycle status: 'queued' (waiting on the project), 'processing', 'completed', 'stale' (source/transcript changed), or 'failed'.
  - Allowed values: `queued`, `processing`, `completed`, `stale`, `failed`
- `revision` (integer, required) — Monotonic counter incremented whenever this target's transcript changes (a source edit affecting it, or an edit to its translation).
- `created_at` (string, required) — When the language target was created.
- `updated_at` (string, required) — When the language target was last updated.
- `model_id` (string, optional, nullable) — Effective dubbing model id (target override or project default).
- `voice_settings` (object, optional, nullable) — Voice settings applied to the whole language, or null if unset.
  - `cloning_strength` (integer, optional, default: 7) — How strongly the dubbed speakers clone the source voices, 0 to 10.
- `outputs` (object, optional, nullable) — Signed output URLs; null until the target has produced an output (present once 'completed', and kept while 'stale' -- compare `output_revision` against `revision` to tell whether the output is up to date).
  - `lossless_audio` (string, optional, nullable) — Signed URL of the dubbed lossless audio track.
- `output_revision` (integer, optional, nullable) — The `revision` the current dubbed output was generated from; equal to `revision` when up to date, less than it when 'stale'. Null until a generation has completed.
- `error` (object, optional, nullable) — Why this language failed; null unless `status` is 'failed', and also null for the few languages that failed before failure reporting was introduced. A code of 'project_failed' means the parent project failed, so read the project for the underlying cause.
  - `code` (string, required) — Stable identifier for the failure, safe to branch on. New codes are added over time, so treat an unrecognized value as 'internal_error'.
  - `message` (string, required) — Human-readable description of the failure, for display. The wording may change at any time; branch on `code` instead.
  - `retryable` (boolean, required) — Whether resubmitting the same input could succeed. False means the failure describes the input or the account, so an identical retry will fail the same way.
- `warnings` (list of object, optional) — Non-fatal conditions raised while dubbing this language, empty when there are none. Reflects the latest generation. Conditions raised while preparing the source are reported on the project instead.
  - `type` ("voices_not_permitted", required) — Identifies this warning; branch on it to read the fields below.
  - `speaker_ids` (list of string, required) — Speakers whose voices were not permitted for cloning. The dub used a replacement voice for each of them; the rest of the speakers are unaffected.
  - `message` (string, required) — Human-readable description of the warning, for display. The wording may change at any time; branch on `type` instead.

## Examples

**Response**

```json
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
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.get("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", "lang_1001kwkyxp0je6ktn4knsfrasx5s");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.get(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s")! as URL,
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
