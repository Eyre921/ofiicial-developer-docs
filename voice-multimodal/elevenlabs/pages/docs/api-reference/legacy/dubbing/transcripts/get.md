---
title: "Retrieve a transcript"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/transcripts/get.md
path: docs/api-reference/legacy/dubbing/transcripts/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Retrieve a transcript

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/transcripts/{language_code}/format/{format_type}

Fetch the transcript for one of the languages in a dub.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/transcripts/get

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
- `format_type` (enum, required) — Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.
  - Allowed values: `srt`, `webvtt`, `json`

## Response

### 200

Successful Response

- `transcript_format` (enum, required)
  - Allowed values: `srt`, `webvtt`, `json`
- `srt` (string, optional, nullable)
- `webvtt` (string, optional, nullable)
- `json` (object, optional, nullable)
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
  "transcript_format": "srt",
  "srt": "string",
  "webvtt": "string",
  "json": {
    "language": "string",
    "utterances": [
      {
        "text": "",
        "speaker_id": "unknown",
        "start_s": 0,
        "end_s": 0,
        "words": [
          {
            "text": "",
            "word_type": "unknown",
            "start_s": 0,
            "end_s": 0,
            "characters": [
              {
                "text": "",
                "start_s": 0,
                "end_s": 0
              }
            ]
          }
        ]
      }
    ]
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.transcripts.get("dubbing_id", "srt", "language_code");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.transcripts.get(
    dubbing_id="dubbing_id",
    format_type="srt",
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt")! as URL,
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
