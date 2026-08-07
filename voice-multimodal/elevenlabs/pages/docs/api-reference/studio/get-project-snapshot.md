---
title: "Get Project Snapshot"
source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot.md
path: docs/api-reference/studio/get-project-snapshot
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Project Snapshot

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}

Returns the project snapshot.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — The ID of the Studio project.
- `project_snapshot_id` (string, required) — The ID of the Studio project snapshot.

## Response

### 200

Successful Response

- `project_snapshot_id` (string, required) — The ID of the project snapshot.
- `project_id` (string, required) — The ID of the project.
- `created_at_unix` (integer, required) — The creation date of the project snapshot.
- `name` (string, required) — The name of the project snapshot.
- `character_alignments` (list of object, required)
  - `characters` (list of string, required)
  - `character_start_times_seconds` (list of double, required)
  - `character_end_times_seconds` (list of double, required)
- `audio_duration_secs` (double, required) — The total duration of the audio in seconds.
- `audio_upload` (map from string to any, optional, nullable) — (Deprecated)
- `zip_upload` (map from string to any, optional, nullable) — (Deprecated)

## Examples

**Response**

```json
{
  "project_snapshot_id": "aw1NgEzBg83R7vgmiJt6",
  "project_id": "aw1NgEzBg83R7vgmiJt6",
  "created_at_unix": 1714204800,
  "name": "My Project Snapshot",
  "character_alignments": [],
  "audio_duration_secs": 123.45
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.snapshots.get("project_id", "project_snapshot_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.snapshots.get(
    project_id="project_id",
    project_snapshot_id="project_snapshot_id",
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")! as URL,
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
