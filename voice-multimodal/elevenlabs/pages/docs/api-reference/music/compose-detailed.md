---
title: "Compose music with details"
source: https://elevenlabs.io/docs/api-reference/music/compose-detailed.md
path: docs/api-reference/music/compose-detailed
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Compose music with details

POST https://api.elevenlabs.io/v1/music/detailed
Content-Type: application/json

Compose a song from a prompt or a composition plan.

Reference: https://elevenlabs.io/docs/api-reference/music/compose-detailed

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/detailed:
    post:
      operationId: compose_detailed
      summary: Compose Music With A Detailed Response
      description: Compose a song from a prompt or a composition plan.
      tags:
        - music
      parameters:
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. Use "auto" (the default) to let the API
            pick the best format for the selected model: mp3_44100_128 for v1
            models and mp3_48000_192 for v2 models. 
          required: false
          schema:
            $ref: '#/components/schemas/V1MusicDetailedPostParametersOutputFormat'
            default: auto
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Multipart/mixed response with JSON metadata and binary audio file
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/music_compose_detailed_Response_200'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Compose_Music_with_a_detailed_response_v1_music_detailed_post
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    V1MusicDetailedPostParametersOutputFormat:
      type: string
      enum:
        - auto
        - mp3_48000_128
        - mp3_48000_192
        - mp3_48000_240
        - mp3_48000_320
        - mp3_22050_32
        - mp3_24000_48
        - mp3_44100_32
        - mp3_44100_64
        - mp3_44100_96
        - mp3_44100_128
        - mp3_44100_192
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_32000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
        - alaw_8000
        - opus_48000_32
        - opus_48000_64
        - opus_48000_96
        - opus_48000_128
        - opus_48000_192
      default: auto
      title: V1MusicDetailedPostParametersOutputFormat
    TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
      title: TimeRange
    SectionSource:
      type: object
      properties:
        song_id:
          type: string
          description: >-
            The ID of the song to source the section from. You can find the song
            ID in the response headers when you generate a song.
        range:
          $ref: '#/components/schemas/TimeRange'
          description: The range to extract from the source song.
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/TimeRange'
          description: The ranges to exclude from the 'range'.
      required:
        - song_id
        - range
      title: SectionSource
    SongSection:
      type: object
      properties:
        section_name:
          type: string
          description: The name of the section. Must be between 1 and 100 characters.
        positive_local_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in this
            section. Use English language for best result.
        negative_local_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in this
            section. Use English language for best result.
        duration_ms:
          type: integer
          description: >-
            The duration of the section in milliseconds. Must be between 3000ms
            and 120000ms.
        lines:
          type: array
          items:
            type: string
          description: >-
            The lyrics of the section. Max 30 lines per section and max 200
            characters per line.
        source_from:
          oneOf:
            - $ref: '#/components/schemas/SectionSource'
            - type: 'null'
          description: Optional source to extract the section from. Used for inpainting.
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
      title: SongSection
    MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in the
            entire song. Use English language for best result.
        negative_global_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in the
            entire song. Use English language for best result.
        sections:
          type: array
          items:
            $ref: '#/components/schemas/SongSection'
          description: The sections of the song.
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
      description: >-
        Composition plan for the `music_v1` model. Using this field with any
        other model will result in an error.
      title: MusicPrompt
    GenerationChunkInputContextAdherence:
      type: string
      enum:
        - low
        - medium
        - high
      default: high
      description: >-
        How much the model adheres to the context of its surrounding chunks. Low
        adherence means the model can deviate from the context and be more
        creative. High adherence means the model will be more consistent with
        the context.
      title: GenerationChunkInputContextAdherence
    AudioRefChunk:
      type: object
      properties:
        song_id:
          type: string
          description: >-
            The ID of the song to source the chunk from. You can find the song
            ID in the response headers when you generate a song.
        range:
          $ref: '#/components/schemas/TimeRange'
          description: The time range to extract from the song.
      required:
        - song_id
        - range
      title: AudioRefChunk
    GenerationChunkInputConditionStrength:
      type: string
      enum:
        - low
        - medium
        - high
        - xhigh
      description: >-
        How strongly the model adheres to the conditioning reference. Low
        strength means the model will be more creative and deviate from the
        reference. High strength means the model will be more consistent with
        the reference.
      title: GenerationChunkInputConditionStrength
    GenerationChunk-Input:
      type: object
      properties:
        text:
          type: string
          description: >-
            The text config to be generated for this chunk. Can contain section
            name in square brackets, e.g. [Verse 1], lyrics lines, and inline
            directions in curly braces, e.g. {scratching}.
        duration_ms:
          type: integer
          description: >-
            The duration of the chunk in milliseconds. Must be between 3000ms
            and 120000ms.
        positive_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in this
            chunk. Use English language for best results. The styles for the
            first chunk are the most important as they set the overall tone and
            genre. Styles for subsequent chunks can be used to add nuance,
            progression, emphasis, or change the direction of the song. Aim to
            have at least 6-7 styles in early chunks until the direction is
            established. Generic styles like 'great production quality' are good
            default styles to append to the list.
        negative_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in this
            chunk. Use English language for best results. Leaving empty is a
            good default, only use this field if you want to explicitly avoid a
            particular style or direction.
        context_adherence:
          $ref: '#/components/schemas/GenerationChunkInputContextAdherence'
          default: high
          description: >-
            How much the model adheres to the context of its surrounding chunks.
            Low adherence means the model can deviate from the context and be
            more creative. High adherence means the model will be more
            consistent with the context.
        conditioning_ref:
          oneOf:
            - $ref: '#/components/schemas/AudioRefChunk'
            - type: 'null'
          description: >-
            The audio reference to condition the generation on. The first chunk
            is the most important as it will influence the generation of all
            subsequent chunks. Thus, if you want to apply conditioning to the
            entire song, start conditioning from the first chunk.
        condition_strength:
          oneOf:
            - $ref: '#/components/schemas/GenerationChunkInputConditionStrength'
            - type: 'null'
          description: >-
            How strongly the model adheres to the conditioning reference. Low
            strength means the model will be more creative and deviate from the
            reference. High strength means the model will be more consistent
            with the reference.
      required:
        - text
        - duration_ms
        - positive_styles
      title: GenerationChunk-Input
    CompositionPlanChunksItems:
      oneOf:
        - $ref: '#/components/schemas/GenerationChunk-Input'
        - $ref: '#/components/schemas/AudioRefChunk'
      title: CompositionPlanChunksItems
    CompositionPlan:
      type: object
      properties:
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/CompositionPlanChunksItems'
          description: The chunks that make up the generation.
      required:
        - chunks
      description: >-
        Composition plan for the `music_v2` model. Using this field with any
        other model will result in an error.
      title: CompositionPlan
    BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan:
      oneOf:
        - $ref: '#/components/schemas/MusicPrompt'
        - $ref: '#/components/schemas/CompositionPlan'
      description: >-
        A detailed composition plan to guide music generation. Cannot be used in
        conjunction with `prompt`.
      title: BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan
    BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId:
      type: string
      enum:
        - music_v1
        - music_v2
      default: music_v1
      description: The model to use for the generation.
      title: BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
    Body_Compose_Music_with_a_detailed_response_v1_music_detailed_post:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
          description: >-
            A simple text prompt to generate a song from. Cannot be used in
            conjunction with `composition_plan`.
        composition_plan:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan
            - type: 'null'
          description: >-
            A detailed composition plan to guide music generation. Cannot be
            used in conjunction with `prompt`.
        music_length_ms:
          type:
            - integer
            - 'null'
          description: >-
            The length of the song to generate in milliseconds. Used only in
            conjunction with `prompt`. Must be between 3000ms and 600000ms.
            Optional - if not provided, the model will choose a length based on
            the prompt.
        model_id:
          $ref: >-
            #/components/schemas/BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
          default: music_v1
          description: The model to use for the generation.
        seed:
          type:
            - integer
            - 'null'
          description: >-
            Random seed to initialize the music generation process. Providing
            the same seed with the same parameters can help achieve more
            consistent results, but exact reproducibility is not guaranteed and
            outputs may change across system updates. Cannot be used in
            conjunction with prompt.
        force_instrumental:
          type: boolean
          default: false
          description: >-
            If true, guarantees that the generated song will be instrumental. If
            false, the song may or may not be instrumental depending on the
            `prompt`. Can only be used with `prompt`.
        finetune_id:
          type:
            - string
            - 'null'
          description: The ID of the finetune to use for the generation
        finetune_strength:
          type: number
          format: double
          default: 1
          description: >-
            How strongly the finetune influences the generation. Defaults to 1.0
            (full strength). Lower values soften the influence of the finetune,
            leaving more room for prompt-level steering. Only meaningful when
            `finetune_id` is also provided.
        respect_sections_durations:
          type: boolean
          default: true
          description: >-
            Controls how strictly section durations in the `composition_plan`
            are enforced. Only used with `composition_plan` and only applies to
            `music_v1`; for `music_v2` section durations are always enforced and
            this is ignored. When false for `music_v1`, the model may adjust
            individual section durations for better quality and latency, while
            preserving the total song duration from the plan.
        store_for_inpainting:
          type: boolean
          default: false
          description: Whether to store the generated song for inpainting.
        with_timestamps:
          type: boolean
          default: false
          description: Whether to return the timestamps of the words in the generated song.
        sign_with_c2pa:
          type: boolean
          default: false
          description: >-
            Whether to sign the generated song with C2PA. Applicable only for
            mp3 files.
      title: Body_Compose_Music_with_a_detailed_response_v1_music_detailed_post
    music_compose_detailed_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: music_compose_detailed_Response_200
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



**Request**

```json
{
  "prompt": "A prompt for music generation",
  "music_length_ms": 10000
}
```

**Response**

```json
{
  "audio": "[binary audio data]",
  "composition_plan": {
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
  },
  "song_metadata": {
    "description": "My Song Description",
    "genres": [
      "pop",
      "rock",
      "jazz"
    ],
    "is_explicit": false,
    "languages": [
      "en",
      "fr"
    ],
    "title": "My Song"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "xi-api-key",
    });
    await client.music.composeDetailed({
        prompt: "A prompt for music generation",
        musicLengthMs: 10000,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="xi-api-key",
)

client.music.compose_detailed(
    prompt="A prompt for music generation",
    music_length_ms=10000,
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

	url := "https://api.elevenlabs.io/v1/music/detailed"

	payload := strings.NewReader("{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
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

url = URI("https://api.elevenlabs.io/v1/music/detailed")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/detailed")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/detailed', [
  'body' => '{
  "prompt": "A prompt for music generation",
  "music_length_ms": 10000
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/detailed");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"A prompt for music generation\",\n  \"music_length_ms\": 10000\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = [
  "prompt": "A prompt for music generation",
  "music_length_ms": 10000
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/detailed")! as URL,
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
