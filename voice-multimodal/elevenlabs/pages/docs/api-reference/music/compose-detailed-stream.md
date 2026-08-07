---
title: "Stream music with details"
source: https://elevenlabs.io/docs/api-reference/music/compose-detailed-stream.md
path: docs/api-reference/music/compose-detailed-stream
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Stream music with details

POST https://api.elevenlabs.io/v1/music/detailed/stream
Content-Type: application/json

Stream a song and its detailed metadata using Server-Sent Events (SSE).

Reference: https://elevenlabs.io/docs/api-reference/music/compose-detailed-stream

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `output_format` (enum, optional, default: auto) — Output format of the generated audio. Formatted as codec_sample_rate_bitrate. Use "auto" (the default) to let the API pick the best format for the selected model: mp3_44100_128 for v1 models and mp3_48000_192 for v2 models.
  - Allowed values: `auto`, `mp3_48000_128`, `mp3_48000_192`, `mp3_48000_240`, `mp3_48000_320`, `mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_32000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`, `alaw_8000`, `opus_48000_32`, `opus_48000_64`, `opus_48000_96`, `opus_48000_128`, `opus_48000_192`

### Body (application/json)

- `prompt` (string, optional, nullable) — A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.
- `composition_plan` (object or object, optional, nullable) — A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.
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
- `music_length_ms` (integer, optional, nullable) — The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.
- `model_id` (enum, optional, default: music_v1) — The model to use for the generation.
  - Allowed values: `music_v1`, `music_v2`
- `seed` (integer, optional, nullable) — Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.
- `force_instrumental` (boolean, optional, default: false) — If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.
- `finetune_id` (string, optional, nullable) — The ID of the finetune to use for the generation
- `store_for_inpainting` (boolean, optional, default: false) — Whether to store the generated song for inpainting.
- `with_timestamps` (boolean, optional, default: false) — Whether to return the timestamps of the words in the generated song.

## Response

### 200

Server-Sent Events for composition plan, song metadata, audio chunks with optional word timestamps, and completion.

- Streaming response of `string`.

## Examples

**Request**

```json
{}
```

**Response**

```json
[
  "data: {\"event\":\"composition_plan\",\"data\":{\"plan\":\"Starting with a mellow intro, building up to an energetic chorus with layered synths and driving drums.\"}}\n",
  "data: {\"event\":\"song_metadata\",\"data\":{\"title\":\"Sunset Drive\",\"artist\":\"Neon Horizon\",\"genre\":\"Synthwave\",\"bpm\":110}}\n",
  "data: {\"event\":\"audio_chunk\",\"data\":\"UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=\"}\n",
  "data: {\"event\":\"audio_chunk\",\"data\":\"UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAE=\"}\n",
  "data: {\"event\":\"word_timestamps\",\"data\":{\"words\":[{\"word\":\"Sunset\",\"start\":0.0,\"end\":0.5},{\"word\":\"Drive\",\"start\":0.5,\"end\":1.0}]}}\n",
  "data: {\"event\":\"completion\",\"data\":{\"message\":\"Stream ended successfully.\"}}\n"
]
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.composeDetailedStream({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.compose_detailed_stream()

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

	url := "https://api.elevenlabs.io/v1/music/detailed/stream"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/music/detailed/stream")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/detailed/stream")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/detailed/stream', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/detailed/stream");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/detailed/stream")! as URL,
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
