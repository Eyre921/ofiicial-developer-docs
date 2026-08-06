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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/{dubbing_id}/transcripts/{language_code}/format/{format_type}:
    get:
      operationId: get
      summary: Retrieve A Transcript
      description: Fetch the transcript for one of the languages in a dub.
      tags:
        - transcripts
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: language_code
          in: path
          description: >-
            ISO-693 language code to retrieve the transcript for. Use 'source'
            to fetch the transcript of the original media.
          required: true
          schema:
            type: string
        - name: format_type
          in: path
          description: >-
            Format to return transcript in. For subtitles use either 'srt' or
            'webvtt', and for a full transcript use 'json'. The 'json' format is
            not yet supported for Dubbing Studio.
          required: true
          schema:
            $ref: >-
              #/components/schemas/V1DubbingDubbingIdTranscriptsLanguageCodeFormatFormatTypeGetParametersFormatType
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
                $ref: '#/components/schemas/DubbingTranscriptsResponseModel'
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
    V1DubbingDubbingIdTranscriptsLanguageCodeFormatFormatTypeGetParametersFormatType:
      type: string
      enum:
        - srt
        - webvtt
        - json
      description: >-
        Format to return transcript in. For subtitles use either 'srt' or
        'webvtt', and for a full transcript use 'json'. The 'json' format is not
        yet supported for Dubbing Studio.
      title: >-
        V1DubbingDubbingIdTranscriptsLanguageCodeFormatFormatTypeGetParametersFormatType
    DubbingTranscriptsResponseModelTranscriptFormat:
      type: string
      enum:
        - srt
        - webvtt
        - json
      title: DubbingTranscriptsResponseModelTranscriptFormat
    DubbingTranscriptCharacter:
      type: object
      properties:
        text:
          type: string
          default: ''
        start_s:
          type: number
          format: double
          default: 0
        end_s:
          type: number
          format: double
          default: 0
      title: DubbingTranscriptCharacter
    DubbingTranscriptWord:
      type: object
      properties:
        text:
          type: string
          default: ''
        word_type:
          type: string
          default: unknown
        start_s:
          type: number
          format: double
          default: 0
        end_s:
          type: number
          format: double
          default: 0
        characters:
          type: array
          items:
            $ref: '#/components/schemas/DubbingTranscriptCharacter'
      title: DubbingTranscriptWord
    DubbingTranscriptUtterance:
      type: object
      properties:
        text:
          type: string
          default: ''
        speaker_id:
          type: string
          default: unknown
        start_s:
          type: number
          format: double
          default: 0
        end_s:
          type: number
          format: double
          default: 0
        words:
          type: array
          items:
            $ref: '#/components/schemas/DubbingTranscriptWord'
      title: DubbingTranscriptUtterance
    DubbingTranscript:
      type: object
      properties:
        language:
          type: string
        utterances:
          type: array
          items:
            $ref: '#/components/schemas/DubbingTranscriptUtterance'
      required:
        - language
        - utterances
      title: DubbingTranscript
    DubbingTranscriptsResponseModel:
      type: object
      properties:
        transcript_format:
          $ref: '#/components/schemas/DubbingTranscriptsResponseModelTranscriptFormat'
        srt:
          type:
            - string
            - 'null'
        webvtt:
          type:
            - string
            - 'null'
        json:
          oneOf:
            - $ref: '#/components/schemas/DubbingTranscript'
            - type: 'null'
      required:
        - transcript_format
      title: DubbingTranscriptsResponseModel
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
