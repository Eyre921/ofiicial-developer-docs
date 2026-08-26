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

**Request**

```json
{}
```

**Response**

```json
{
  "language": "en",
  "utterances": [
    {
      "end_s": 3.5,
      "speaker_id": "speaker_1",
      "start_s": 0,
      "text": "Welcome to the ElevenLabs dubbing service.",
      "words": [
        {
          "characters": [
            {
              "end_s": 0.1,
              "start_s": 0,
              "text": "W"
            },
            {
              "end_s": 0.2,
              "start_s": 0.1,
              "text": "e"
            },
            {
              "end_s": 0.3,
              "start_s": 0.2,
              "text": "l"
            },
            {
              "end_s": 0.4,
              "start_s": 0.3,
              "text": "c"
            },
            {
              "end_s": 0.5,
              "start_s": 0.4,
              "text": "o"
            },
            {
              "end_s": 0.55,
              "start_s": 0.5,
              "text": "m"
            },
            {
              "end_s": 0.6,
              "start_s": 0.55,
              "text": "e"
            }
          ],
          "end_s": 0.6,
          "start_s": 0,
          "text": "Welcome",
          "word_type": "word"
        },
        {
          "characters": [
            {
              "end_s": 0.8,
              "start_s": 0.7,
              "text": "t"
            },
            {
              "end_s": 0.9,
              "start_s": 0.8,
              "text": "o"
            }
          ],
          "end_s": 0.9,
          "start_s": 0.7,
          "text": "to",
          "word_type": "word"
        },
        {
          "characters": [
            {
              "end_s": 1.05,
              "start_s": 1,
              "text": "t"
            },
            {
              "end_s": 1.1,
              "start_s": 1.05,
              "text": "h"
            },
            {
              "end_s": 1.2,
              "start_s": 1.1,
              "text": "e"
            }
          ],
          "end_s": 1.2,
          "start_s": 1,
          "text": "the",
          "word_type": "word"
        },
        {
          "characters": [
            {
              "end_s": 1.4,
              "start_s": 1.3,
              "text": "E"
            },
            {
              "end_s": 1.45,
              "start_s": 1.4,
              "text": "l"
            },
            {
              "end_s": 1.5,
              "start_s": 1.45,
              "text": "e"
            },
            {
              "end_s": 1.55,
              "start_s": 1.5,
              "text": "v"
            },
            {
              "end_s": 1.6,
              "start_s": 1.55,
              "text": "e"
            },
            {
              "end_s": 1.65,
              "start_s": 1.6,
              "text": "n"
            },
            {
              "end_s": 1.7,
              "start_s": 1.65,
              "text": "L"
            },
            {
              "end_s": 1.75,
              "start_s": 1.7,
              "text": "a"
            },
            {
              "end_s": 1.8,
              "start_s": 1.75,
              "text": "b"
            },
            {
              "end_s": 2,
              "start_s": 1.8,
              "text": "s"
            }
          ],
          "end_s": 2,
          "start_s": 1.3,
          "text": "ElevenLabs",
          "word_type": "word"
        },
        {
          "characters": [
            {
              "end_s": 2.15,
              "start_s": 2.1,
              "text": "d"
            },
            {
              "end_s": 2.2,
              "start_s": 2.15,
              "text": "u"
            },
            {
              "end_s": 2.25,
              "start_s": 2.2,
              "text": "b"
            },
            {
              "end_s": 2.3,
              "start_s": 2.25,
              "text": "b"
            },
            {
              "end_s": 2.35,
              "start_s": 2.3,
              "text": "i"
            },
            {
              "end_s": 2.4,
              "start_s": 2.35,
              "text": "n"
            },
            {
              "end_s": 2.6,
              "start_s": 2.4,
              "text": "g"
            }
          ],
          "end_s": 2.6,
          "start_s": 2.1,
          "text": "dubbing",
          "word_type": "word"
        },
        {
          "characters": [
            {
              "end_s": 2.75,
              "start_s": 2.7,
              "text": "s"
            },
            {
              "end_s": 2.8,
              "start_s": 2.75,
              "text": "e"
            },
            {
              "end_s": 2.85,
              "start_s": 2.8,
              "text": "r"
            },
            {
              "end_s": 2.9,
              "start_s": 2.85,
              "text": "v"
            },
            {
              "end_s": 2.95,
              "start_s": 2.9,
              "text": "i"
            },
            {
              "end_s": 3,
              "start_s": 2.95,
              "text": "c"
            },
            {
              "end_s": 3.1,
              "start_s": 3,
              "text": "e"
            },
            {
              "end_s": 3.5,
              "start_s": 3.1,
              "text": "."
            }
          ],
          "end_s": 3.5,
          "start_s": 2.7,
          "text": "service.",
          "word_type": "word"
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcript/language_code")! as URL,
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
