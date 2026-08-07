---
title: "Create composition plan"
source: https://elevenlabs.io/docs/api-reference/music/create-composition-plan.md
path: docs/api-reference/music/create-composition-plan
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create composition plan

POST https://api.elevenlabs.io/v1/music/plan
Content-Type: application/json

Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

Reference: https://elevenlabs.io/docs/api-reference/music/create-composition-plan

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `prompt` (string, required) — A simple text prompt to compose a plan from.
- `music_length_ms` (integer, optional, nullable) — The length of the composition plan to generate in milliseconds. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.
- `source_composition_plan` (object or object, optional, nullable) — An optional composition plan to use as a source for the new composition plan.
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
- `model_id` (enum, optional, default: music_v1) — The model to use for the generation.
  - Allowed values: `music_v1`, `music_v2`

## Response

### 200

Successful Response

- `object or object`
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

## Examples

**Request**

```json
{
  "prompt": "string"
}
```

**Response**

```json
{
  "negative_global_styles": [
    "metal",
    "hip-hop",
    "country"
  ],
  "positive_global_styles": [
    "pop",
    "rock",
    "jazz"
  ],
  "sections": [
    {
      "duration_ms": 10000,
      "lines": [
        "Verse 1 lyrics"
      ],
      "negative_local_styles": [
        "metal",
        "hip-hop",
        "country"
      ],
      "positive_local_styles": [
        "pop",
        "rock",
        "jazz"
      ],
      "section_name": "Verse 1"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.compositionPlan.create({
        prompt: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.composition_plan.create(
    prompt="string",
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

	url := "https://api.elevenlabs.io/v1/music/plan"

	payload := strings.NewReader("{\n  \"prompt\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/music/plan")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/plan")
  .header("Content-Type", "application/json")
  .body("{\n  \"prompt\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/plan', [
  'body' => '{
  "prompt": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/plan");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["prompt": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/plan")! as URL,
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
