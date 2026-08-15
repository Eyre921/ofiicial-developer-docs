---
title: "Get target transcript"
source: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/get-target-transcript.md
path: docs/api-reference/dubbing/target-transcript/get-target-transcript
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get target transcript

GET https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}/transcript

A language target's transcript: source segments with their translations.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/get-target-transcript

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

### 200

Successful Response

- `target_language` (string, required) — BCP-47 language tag this target is translated into.
- `segments` (list of object, required) — The target segments, in playback order.
  - `id` (string, required) — Stable identifier of the segment (from the source).
  - `speaker_id` (string, required) — Identifier of the segment's speaker.
  - `start_s` (double, required) — Start time of the segment, in seconds.
  - `end_s` (double, required) — End time of the segment, in seconds.
  - `source_text` (string, required) — The source-language text of the segment.
  - `translation` (string, optional, nullable) — The translated text, or null if not translated yet (needs translation).
- `revision` (integer, required) — The target's revision at read time.
- `source_language` (string, optional, nullable) — BCP-47 language tag of the source transcript.

## Examples

**Response**

```json
{
  "target_language": "es",
  "segments": [
    {
      "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
      "speaker_id": "default_speaker",
      "start_s": 0,
      "end_s": 2.5,
      "source_text": "Welcome to our product demo.",
      "translation": "Bienvenido a la demostración de nuestro producto."
    }
  ],
  "revision": 3,
  "source_language": "en"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.transcript.get("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", "lang_1001kwkyxp0je6ktn4knsfrasx5s");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.transcript.get(
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript")! as URL,
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
