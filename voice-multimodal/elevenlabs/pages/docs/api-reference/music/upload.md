---
title: "Upload Music"
source: https://elevenlabs.io/docs/api-reference/music/upload.md
path: docs/api-reference/music/upload
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Upload Music

POST https://api.elevenlabs.io/v1/music/upload
Content-Type: multipart/form-data

Upload a music file to be later used for inpainting. Price for uploading is the same as the one for song generation. All uploaded content gets inspected for copyright infringement. If copyrighted content is detected, half of the request cost is still charged.

Reference: https://elevenlabs.io/docs/api-reference/music/upload

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `file` (file, required) — The audio file to upload.
- `extract_composition_plan` (boolean or enum, optional) — Whether to generate and return the composition plan for the uploaded song. Pass a model id (`music_v1` or `music_v2`) to control which composition plan format is returned. Passing `true`/`false` is deprecated; `true` defaults to the `music_v1` plan format. Enabling this will increase the latency.
- `with_timestamps` (boolean, optional) — Whether to transcribe the uploaded song and return word-level timestamps. If True, the response will include words_timestamps but will increase the latency.
- `with_waveform_visual` (boolean, optional) — Whether to return the visual waveform of the uploaded song.

## Response

### 200

Successfully uploaded music file with optional composition plan

- `song_id` (string, required) — Unique identifier for the uploaded song
- `composition_plan` (object or object, optional, nullable) — The composition plan extracted from the uploaded song. Only present if `extract_composition_plan` was provided in the request body.
  - MusicPrompt
    - `positive_global_styles` (list of string, required) — The styles and musical directions that should be present in the entire song. Use English language for best result.
    - `negative_global_styles` (list of string, required) — The styles and musical directions that should not be present in the entire song. Use English language for best result.
    - `sections` (list of object, required) — The sections of the song.
      - `section_name` (string, required) — The name of the section. Must be between 1 and 100 characters.
      - `positive_local_styles` (list of string, required) — The styles and musical directions that should be present in this section. Use English language for best result.
      - `negative_local_styles` (list of string, required) — The styles and musical directions that should not be present in this section. Use English language for best result.
      - `duration_ms` (integer, required) — The duration of the section in milliseconds. Must be between 3000ms and 120000ms.
      - `lines` (list of string, required) — The lyrics of the section. Max 30 lines per section and max 200 characters per line.
      - `source_from` (object, optional, nullable) — Optional source to extract the section from. Used for inpainting.
        - `song_id` (string, required) — The ID of the song to source the section from. You can find the song ID in the response headers when you generate a song.
        - `range` (object, required) — The range to extract from the source song.
          - `start_ms` (integer, required)
          - `end_ms` (integer, required)
        - `negative_ranges` (list of object, optional) — The ranges to exclude from the 'range'.
          - `start_ms` (integer, required)
          - `end_ms` (integer, required)
  - CompositionPlan
    - `chunks` (list of object or object, required) — The chunks that make up the generation.
      - GenerationChunk
        - `text` (string, required) — The text config to be generated for this chunk. Can contain section name in square brackets, e.g. \[Verse 1], lyrics lines, and inline directions in curly braces, e.g. \{scratching}.
        - `duration_ms` (integer, required) — The duration of the chunk in milliseconds. Must be between 3000ms and 120000ms.
        - `positive_styles` (list of string, required) — The styles and musical directions that should be present in this chunk. Use English language for best results. The styles for the first chunk are the most important as they set the overall tone and genre. Styles for subsequent chunks can be used to add nuance, progression, emphasis, or change the direction of the song. Aim to have at least 6-7 styles in early chunks until the direction is established. Generic styles like 'great production quality' are good default styles to append to the list.
        - `negative_styles` (list of string, optional) — The styles and musical directions that should not be present in this chunk. Use English language for best results. Leaving empty is a good default, only use this field if you want to explicitly avoid a particular style or direction.
        - `context_adherence` (enum, optional, default: high) — How much the model adheres to the context of its surrounding chunks. Low adherence means the model can deviate from the context and be more creative. High adherence means the model will be more consistent with the context.
          - Allowed values: `low`, `medium`, `high`
        - `conditioning_ref` (object, optional, nullable) — The audio reference to condition the generation on. The first chunk is the most important as it will influence the generation of all subsequent chunks. Thus, if you want to apply conditioning to the entire song, start conditioning from the first chunk.
          - `song_id` (string, required) — The ID of the song to source the chunk from. You can find the song ID in the response headers when you generate a song.
          - `range` (object, required) — The time range to extract from the song.
            - `start_ms` (integer, required)
            - `end_ms` (integer, required)
        - `condition_strength` (enum, optional, nullable) — How strongly the model adheres to the conditioning reference. Low strength means the model will be more creative and deviate from the reference. High strength means the model will be more consistent with the reference.
          - Allowed values: `low`, `medium`, `high`, `xhigh`
      - AudioRefChunk
        - `song_id` (string, required) — The ID of the song to source the chunk from. You can find the song ID in the response headers when you generate a song.
        - `range` (object, required) — The time range to extract from the song.
          - `start_ms` (integer, required)
          - `end_ms` (integer, required)
- `words_timestamps` (list of object, optional, nullable) — Word-level timestamps transcribed from the uploaded song. Only present if `with_timestamps` was True in the request body
  - `word` (string, required)
  - `start_ms` (integer, required)
  - `end_ms` (integer, required)
- `waveform_visual` (list of integer, optional, nullable) — A low-resolution waveform of the uploaded song, for showing a preview of it. Holds 4 values per second of audio, from -1000 to 1000. Stereo is mixed down to a single channel. Only present if `with_waveform_visual` was True in the request body.

## Examples

**Request**

```json
{
  "file": "<file: string>"
}
```

**Response**

```json
{
  "song_id": "jR4Xz8kL2mNpQ9wVtY1b"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.upload({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.upload(
    file="example_file",
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

	url := "https://api.elevenlabs.io/v1/music/upload"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_waveform_visual\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

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

url = URI("https://api.elevenlabs.io/v1/music/upload")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_waveform_visual\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/upload")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_waveform_visual\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/upload', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => 'string',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/upload");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_waveform_visual\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "extract_composition_plan",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "string"
  ],
  [
    "name": "with_timestamps",
    "value": 
  ],
  [
    "name": "with_waveform_visual",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/upload")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
