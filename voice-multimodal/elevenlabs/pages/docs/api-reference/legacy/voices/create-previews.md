---
title: "Voice design"
source: https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews.md
path: docs/api-reference/legacy/voices/create-previews
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voice design

POST https://api.elevenlabs.io/v1/text-to-voice/create-previews
Content-Type: application/json

Create a voice from a text prompt.

Reference: https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/text-to-voice/create-previews:
    post:
      operationId: create_previews
      summary: Voice design
      description: Create a voice from a text prompt.
      tags:
        - subpackage_textToVoice
      parameters:
        - name: output_format
          in: query
          description: The output format of the generated audio.
          required: false
          schema:
            $ref: '#/components/schemas/AllowedOutputFormats'
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VoicePreviewsResponseModel'
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
              $ref: '#/components/schemas/VoicePreviewsRequestModel'
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
    AllowedOutputFormats:
      type: string
      enum:
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
      title: AllowedOutputFormats
    VoicePreviewsRequestModel:
      type: object
      properties:
        voice_description:
          type: string
          description: Description to use for the created voice.
        text:
          type:
            - string
            - 'null'
          description: Text to generate, text length has to be between 100 and 1000.
        auto_generate_text:
          type: boolean
          default: false
          description: >-
            Whether to automatically generate a text suitable for the voice
            description.
        loudness:
          type: number
          format: double
          default: 0.5
          description: >-
            Controls the volume level of the generated voice. -1 is quietest, 1
            is loudest, 0 corresponds to roughly -24 LUFS.
        quality:
          type: number
          format: double
          default: 0.9
          description: Higher quality results in better voice output but less variety.
        seed:
          type:
            - integer
            - 'null'
          description: >-
            Random number that controls the voice generation. Same seed with
            same inputs produces same voice.
        guidance_scale:
          type: number
          format: double
          default: 5
          description: >-
            Controls how closely the AI follows the prompt. Lower numbers give
            the AI more freedom to be creative, while higher numbers force it to
            stick more to the prompt. High numbers can cause voice to sound
            artificial or robotic. We recommend to use longer, more detailed
            prompts at lower Guidance Scale.
        should_enhance:
          type: boolean
          default: false
          description: >-
            Whether to enhance the voice description using AI to add more detail
            and improve voice generation quality. When enabled, the system will
            automatically expand simple prompts into more detailed voice
            descriptions. Defaults to False
      required:
        - voice_description
      title: VoicePreviewsRequestModel
    VoicePreviewResponseModel:
      type: object
      properties:
        audio_base_64:
          type: string
          description: The base64 encoded audio of the preview.
        generated_voice_id:
          type: string
          description: >-
            The ID of the generated voice. Use it to create a voice from the
            preview.
        media_type:
          type: string
          description: The media type of the preview.
        duration_secs:
          type: number
          format: double
          description: The duration of the preview in seconds.
        language:
          type:
            - string
            - 'null'
          description: The language of the preview.
      required:
        - audio_base_64
        - generated_voice_id
        - media_type
        - duration_secs
        - language
      title: VoicePreviewResponseModel
    VoicePreviewsResponseModel:
      type: object
      properties:
        previews:
          type: array
          items:
            $ref: '#/components/schemas/VoicePreviewResponseModel'
          description: The previews of the generated voices.
        text:
          type: string
          description: The text used to preview the voices.
      required:
        - previews
        - text
      title: VoicePreviewsResponseModel
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
  "voice_description": "A sassy squeaky mouse"
}
```

**Response**

```json
{
  "previews": [
    {
      "audio_base_64": "string",
      "generated_voice_id": "string",
      "media_type": "string",
      "duration_secs": 1.1,
      "language": "string"
    }
  ],
  "text": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.textToVoice.createPreviews({
        voiceDescription: "A sassy squeaky mouse",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.text_to_voice.create_previews(
    voice_description="A sassy squeaky mouse",
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/create-previews"

	payload := strings.NewReader("{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/create-previews")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/create-previews")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/create-previews', [
  'body' => '{
  "voice_description": "A sassy squeaky mouse"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/create-previews");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_description\": \"A sassy squeaky mouse\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["voice_description": "A sassy squeaky mouse"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/create-previews")! as URL,
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
