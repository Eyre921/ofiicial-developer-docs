---
title: "Get separated speaker audio"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-separated-speaker-audio.md
path: docs/api-reference/voices/pvc/samples/get-separated-speaker-audio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get separated speaker audio

GET https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio

Retrieve the separated audio for a specific speaker.

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-separated-speaker-audio

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio:
    get:
      operationId: get
      summary: Retrieve Separated Speaker Audio
      description: Retrieve the separated audio for a specific speaker.
      tags:
        - subpackage_voices/pvc/samples/speakers/audio
      parameters:
        - name: voice_id
          in: path
          description: >-
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices
            to list all the available voices.
          required: true
          schema:
            type: string
        - name: sample_id
          in: path
          description: Sample ID to be used
          required: true
          schema:
            type: string
        - name: speaker_id
          in: path
          description: >-
            Speaker ID to be used, you can use GET
            https://api.elevenlabs.io/v1/voices/{voice_id}/samples/{sample_id}/speakers
            to list all the available speakers for a sample.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/SpeakerAudioResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    SpeakerAudioResponseModel:
      type: object
      properties:
        audio_base_64:
          type: string
          description: The base64 encoded audio.
        media_type:
          type: string
          description: The media type of the audio.
        duration_secs:
          type: number
          format: double
          description: The duration of the audio in seconds.
      required:
        - audio_base_64
        - media_type
        - duration_secs
      title: SpeakerAudioResponseModel
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



**Response**

```json
{
  "audio_base_64": "audio_base_64",
  "media_type": "audio/mpeg",
  "duration_secs": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.speakers.audio.get("sample_id", "speaker_id", "voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.speakers.audio.get(
    sample_id="sample_id",
    speaker_id="speaker_id",
    voice_id="voice_id",
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

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio"

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

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio")! as URL,
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
