---
title: "Get dubbed transcript"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/get-transcript-for-dub.md
path: docs/api-reference/legacy/dubbing/get-transcript-for-dub
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dubbed transcript

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/transcript/{language_code}

Returns transcript for the dub as an SRT or WEBVTT file.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/get-transcript-for-dub

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `dubbing_id` (string, required) — ID of the dubbing project.
- `language_code` (string, required) — ISO-693 language code to retrieve the transcript for. Use 'source' to fetch the transcript of the original media.

### Query parameters

- `format_type` (enum, optional, default: srt) — Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.
  - Allowed values: `srt`, `webvtt`, `json`

## Response

### 200

Successful Response

- `object or string`
  - DubbingTranscriptResponseModel
    - `language` (string, required)
    - `utterances` (list of object, required)
      - `text` (string, optional, default: )
      - `speaker_id` (string, optional, default: unknown)
      - `start_s` (double, optional, default: 0)
      - `end_s` (double, optional, default: 0)
      - `words` (list of object, optional)
        - `text` (string, optional, default: )
        - `word_type` (string, optional, default: unknown)
        - `start_s` (double, optional, default: 0)
        - `end_s` (double, optional, default: 0)
        - `characters` (list of object, optional)
          - `text` (string, optional, default: )
          - `start_s` (double, optional, default: 0)
          - `end_s` (double, optional, default: 0)

## Examples

**Response**

```json
{
  "language": "string",
  "utterances": [
    {
      "end_s": 0,
      "speaker_id": "unknown",
      "start_s": 0,
      "text": "",
      "words": [
        {
          "characters": [
            {
              "end_s": 0,
              "start_s": 0,
              "text": ""
            }
          ],
          "end_s": 0,
          "start_s": 0,
          "text": "",
          "word_type": "unknown"
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
    await client.dubbing.transcript.getTranscriptForDub("dubbing_id", "language_code", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.transcript.get_transcript_for_dub(
    dubbing_id="dubbing_id",
    language_code="language_code",
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")! as URL,
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
