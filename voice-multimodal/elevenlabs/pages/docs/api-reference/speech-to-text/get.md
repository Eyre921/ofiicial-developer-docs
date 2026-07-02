---
title: "Get transcript"
source: https://elevenlabs.io/docs/api-reference/speech-to-text/get.md
path: docs/api-reference/speech-to-text/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get transcript

GET https://api.elevenlabs.io/v1/speech-to-text/transcripts/{transcription_id}

Retrieve a previously generated transcript by its ID.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/speech-to-text/transcripts/{transcription_id}:
    get:
      operationId: get
      summary: Get Transcript By Id
      description: Retrieve a previously generated transcript by its ID.
      tags:
        - subpackage_speechToText/transcripts
      parameters:
        - name: transcription_id
          in: path
          description: The unique ID of the transcript to retrieve
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
          description: The transcript data
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/speech_to_text_transcripts_get_Response_200
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
    SpeechToTextWordResponseModelType:
      type: string
      enum:
        - word
        - spacing
        - audio_event
      description: >-
        The type of the word or sound. 'audio_event' is used for non-word sounds
        like laughter or footsteps.
      title: SpeechToTextWordResponseModelType
    SpeechToTextCharacterResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The character that was transcribed.
        start:
          type:
            - number
            - 'null'
          format: double
          description: The start time of the character in seconds.
        end:
          type:
            - number
            - 'null'
          format: double
          description: The end time of the character in seconds.
      required:
        - text
      title: SpeechToTextCharacterResponseModel
    SpeechToTextWordResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The word or sound that was transcribed.
        start:
          type:
            - number
            - 'null'
          format: double
          description: The start time of the word or sound in seconds.
        end:
          type:
            - number
            - 'null'
          format: double
          description: The end time of the word or sound in seconds.
        type:
          $ref: '#/components/schemas/SpeechToTextWordResponseModelType'
          description: >-
            The type of the word or sound. 'audio_event' is used for non-word
            sounds like laughter or footsteps.
        speaker_id:
          type:
            - string
            - 'null'
          description: Unique identifier for the speaker of this word.
        logprob:
          type: number
          format: double
          description: >-
            The log of the probability with which this word was predicted.
            Logprobs are in range [-infinity, 0], higher logprobs indicate a
            higher confidence the model has in its predictions.
        characters:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SpeechToTextCharacterResponseModel'
          description: The characters that make up the word and their timing information.
        channel_index:
          type:
            - integer
            - 'null'
          description: >-
            The channel this word was spoken on (for multichannel audio). Null
            for single-channel transcriptions.
      required:
        - text
        - type
        - logprob
      description: Word-level detail of the transcription with timing information.
      title: SpeechToTextWordResponseModel
    AdditionalFormatResponseModel:
      type: object
      properties:
        requested_format:
          type: string
          description: The requested format.
        file_extension:
          type: string
          description: The file extension of the additional format.
        content_type:
          type: string
          description: The content type of the additional format.
        is_base64_encoded:
          type: boolean
          description: Whether the content is base64 encoded.
        content:
          type: string
          description: The content of the additional format.
      required:
        - requested_format
        - file_extension
        - content_type
        - is_base64_encoded
        - content
      title: AdditionalFormatResponseModel
    DetectedEntity:
      type: object
      properties:
        text:
          type: string
          description: The text that was identified as an entity.
        entity_type:
          type: string
          description: >-
            The type of entity detected (e.g., 'credit_card', 'email_address',
            'person_name').
        start_char:
          type: integer
          description: Start character position in the transcript text.
        end_char:
          type: integer
          description: End character position in the transcript text.
      required:
        - text
        - entity_type
        - start_char
        - end_char
      title: DetectedEntity
    SpeechToTextChunkResponseModel:
      type: object
      properties:
        language_code:
          type: string
          description: The detected language code (e.g. 'eng' for English).
        language_probability:
          type: number
          format: double
          description: The confidence score of the language detection (0 to 1).
        text:
          type: string
          description: The raw text of the transcription.
        words:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextWordResponseModel'
          description: List of words with their timing information.
        channel_index:
          type:
            - integer
            - 'null'
          description: >-
            The channel index this transcript belongs to (for multichannel
            audio).
        additional_formats:
          type:
            - array
            - 'null'
          items:
            oneOf:
              - $ref: '#/components/schemas/AdditionalFormatResponseModel'
              - type: 'null'
          description: Requested additional formats of the transcript.
        transcription_id:
          type:
            - string
            - 'null'
          description: The transcription ID of the response.
        entities:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/DetectedEntity'
          description: >-
            List of detected entities with their text, type, and character
            positions in the transcript.
        audio_duration_secs:
          type:
            - number
            - 'null'
          format: double
          description: The duration of the audio that was transcribed in seconds.
      required:
        - language_code
        - language_probability
        - text
        - words
      description: Chunk-level detail of the transcription with timing information.
      title: SpeechToTextChunkResponseModel
    MultichannelSpeechToTextResponseModel:
      type: object
      properties:
        transcripts:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
          description: >-
            List of transcripts, one for each audio channel. Each transcript
            contains the text and word-level details for its respective channel.
        transcription_id:
          type:
            - string
            - 'null'
          description: The transcription ID of the response.
        audio_duration_secs:
          type:
            - number
            - 'null'
          format: double
          description: >-
            The duration of the audio that was transcribed across all channels
            in seconds.
      required:
        - transcripts
      description: Response model for multichannel speech-to-text transcription.
      title: MultichannelSpeechToTextResponseModel
    speech_to_text_transcripts_get_Response_200:
      oneOf:
        - $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/MultichannelSpeechToTextResponseModel'
        - $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/MultichannelSpeechToTextResponseModel'
      title: speech_to_text_transcripts_get_Response_200
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
  "language_code": "en",
  "language_probability": 0.98,
  "text": "Hello world!",
  "words": [
    {
      "end": 0.5,
      "logprob": -0.124,
      "speaker_id": "speaker_1",
      "start": 0,
      "text": "Hello",
      "type": "word"
    },
    {
      "end": 0.5,
      "logprob": 0,
      "speaker_id": "speaker_1",
      "start": 0.5,
      "text": " ",
      "type": "spacing"
    },
    {
      "end": 1.2,
      "logprob": -0.089,
      "speaker_id": "speaker_1",
      "start": 0.5,
      "text": "world!",
      "type": "word"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechToText.transcripts.get("transcription_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_to_text.transcripts.get(
    transcription_id="transcription_id",
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

	url := "https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id"

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

url = URI("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text/transcripts/transcription_id")! as URL,
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
