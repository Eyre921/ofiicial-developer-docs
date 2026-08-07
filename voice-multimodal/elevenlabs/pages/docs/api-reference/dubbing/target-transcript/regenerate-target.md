---
title: "Regenerate target"
source: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/regenerate-target.md
path: docs/api-reference/dubbing/target-transcript/regenerate-target
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Regenerate target

POST https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}/transcript/regenerate

Enterprise only. Re-dub a target from its edited transcript, re-synthesizing only the edited regions (charged like a generation). Conflicts when the target has no edits to apply -- nothing is dispatched and nothing is charged.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/regenerate-target

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the dubbing project.
- `language_id` (string, required) — Identifier of the language target.

## Response

### 202

Successful Response

- `regenerated_segment_ids` (list of string, required) — The segments this re-dub re-synthesizes: those with edits to apply.
- `regenerated_seconds` (double, required) — Seconds of audio this re-dub covers -- the edited regions only, never the whole target. `charged_seconds` is the part of it that was billed.
- `charged_seconds` (double, required) — Seconds actually billed, after the free-regeneration allowance. Zero when the re-dub cost nothing -- the allowance covered all of it, or the project's included generation did.
- `free_regeneration_seconds_remaining` (double, required) — Free-regeneration seconds left for this language target after this re-dub. The allowance is the source's own duration.

## Examples

**Response**

```json
{
  "regenerated_segment_ids": [
    "0199a3f0-1c2d-7abc-8def-0123456789ab",
    "0199a3f0-3e4f-7abc-8def-0123456789cd"
  ],
  "regenerated_seconds": 4,
  "charged_seconds": 0,
  "free_regeneration_seconds_remaining": 38
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.transcript.regenerate("lang_1001kwkyxp0je6ktn4knsfrasx5s", "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.transcript.regenerate(
    language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

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
