---
title: "Create dialogue with timestamps"
source: https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps.md
path: docs/api-reference/text-to-dialogue/convert-with-timestamps
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create dialogue with timestamps

POST https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps
Content-Type: application/json

Generate dialogue from text with precise character-level timing information for audio-text synchronization.

Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/text-to-dialogue/with-timestamps:
    post:
      operationId: convert_with_timestamps
      summary: Text To Dialogue With Timestamps
      description: >-
        Generate dialogue from text with precise character-level timing
        information for audio-text synchronization.
      tags:
        - subpackage_textToDialogue
      parameters:
        - name: output_format
          in: query
          description: >-
            Output format of the generated audio. Formatted as
            codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at
            32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate
            requires you to be subscribed to Creator tier or above. PCM and WAV
            formats with 44.1kHz sample rate requires you to be subscribed to
            Pro tier or above. Note that the μ-law format (sometimes written
            mu-law, often approximated as u-law) is commonly used for Twilio
            audio inputs.
          required: false
          schema:
            $ref: >-
              #/components/schemas/V1TextToDialogueWithTimestampsPostParametersOutputFormat
            default: mp3_44100_128
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean history features are unavailable for
            this request, including request stitching. Zero retention mode may
            only be used by enterprise customers.
          required: false
          schema:
            type: boolean
            default: true
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
                $ref: >-
                  #/components/schemas/AudioWithTimestampsAndVoiceSegmentsResponseModel
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
              $ref: '#/components/schemas/Body_text_to_dialogue_full_with_timestamps'
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
    V1TextToDialogueWithTimestampsPostParametersOutputFormat:
      type: string
      enum:
        - alaw_8000
        - mp3_22050_32
        - mp3_24000_48
        - mp3_44100_128
        - mp3_44100_192
        - mp3_44100_32
        - mp3_44100_64
        - mp3_44100_96
        - opus_48000_128
        - opus_48000_192
        - opus_48000_32
        - opus_48000_64
        - opus_48000_96
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_32000
        - pcm_44100
        - pcm_48000
        - pcm_8000
        - ulaw_8000
        - wav_16000
        - wav_22050
        - wav_24000
        - wav_32000
        - wav_44100
        - wav_48000
        - wav_8000
      default: mp3_44100_128
      description: >-
        Output format of the generated audio. Formatted as
        codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs
        is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to
        be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz
        sample rate requires you to be subscribed to Pro tier or above. Note
        that the μ-law format (sometimes written mu-law, often approximated as
        u-law) is commonly used for Twilio audio inputs.
      title: V1TextToDialogueWithTimestampsPostParametersOutputFormat
    DialogueInput:
      type: object
      properties:
        text:
          type: string
          description: The text to be converted into speech.
        voice_id:
          type: string
          description: The ID of the voice to be used for the generation.
      required:
        - text
        - voice_id
      title: DialogueInput
    ModelSettingsResponseModel:
      type: object
      properties:
        stability:
          type:
            - number
            - 'null'
          format: double
          default: 0.5
          description: >-
            Determines how stable the voice is and the randomness between each
            generation. Lower values introduce broader emotional range for the
            voice. Higher values can result in a monotonous voice with limited
            emotion.
      title: ModelSettingsResponseModel
    PronunciationDictionaryVersionLocatorRequestModel:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
          description: The ID of the pronunciation dictionary.
        version_id:
          type:
            - string
            - 'null'
          description: >-
            The ID of the version of the pronunciation dictionary. If not
            provided, the latest version will be used.
      required:
        - pronunciation_dictionary_id
      title: PronunciationDictionaryVersionLocatorRequestModel
    BodyTextToDialogueFullWithTimestampsApplyTextNormalization:
      type: string
      enum:
        - auto
        - 'on'
        - 'off'
      default: auto
      description: >-
        This parameter controls text normalization with three modes: 'auto',
        'on', and 'off'. When set to 'auto', the system will automatically
        decide whether to apply text normalization (e.g., spelling out numbers).
        With 'on', text normalization will always be applied, while with 'off',
        it will be skipped.
      title: BodyTextToDialogueFullWithTimestampsApplyTextNormalization
    Body_text_to_dialogue_full_with_timestamps:
      type: object
      properties:
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/DialogueInput'
          description: >-
            A list of dialogue inputs, each containing text and a voice ID which
            will be converted into speech. The maximum number of unique voice
            IDs is 10. For reliable generation, keep the total character count
            across all `inputs[].text` values at or below 2,000 characters per
            request. Longer requests can terminate early in streaming responses
            or return a validation error.
        model_id:
          type: string
          default: eleven_v3
          description: >-
            Identifier of the model that will be used, you can query them using
            GET /v1/models. The model needs to have support for text to speech,
            you can check this using the can_do_text_to_speech property.
        language_code:
          type:
            - string
            - 'null'
          description: >-
            Language code (ISO 639-1) used to enforce a language for the model
            and text normalization. If the model does not support the provided
            language code, it will be ignored. This parameter is not supported
            for multilingual_v2 models.
        settings:
          oneOf:
            - $ref: '#/components/schemas/ModelSettingsResponseModel'
            - type: 'null'
          description: Settings controlling the dialogue generation.
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PronunciationDictionaryVersionLocatorRequestModel
          description: >-
            A list of pronunciation dictionary locators (id, version_id) to be
            applied to the text. They will be applied in order. You may have up
            to 3 locators per request
        seed:
          type:
            - integer
            - 'null'
          description: >-
            If specified, our system will make a best effort to sample
            deterministically, such that repeated requests with the same seed
            and parameters should return the same result. Determinism is not
            guaranteed. Must be integer between 0 and 4294967295.
        apply_text_normalization:
          $ref: >-
            #/components/schemas/BodyTextToDialogueFullWithTimestampsApplyTextNormalization
          default: auto
          description: >-
            This parameter controls text normalization with three modes: 'auto',
            'on', and 'off'. When set to 'auto', the system will automatically
            decide whether to apply text normalization (e.g., spelling out
            numbers). With 'on', text normalization will always be applied,
            while with 'off', it will be skipped.
      required:
        - inputs
      title: Body_text_to_dialogue_full_with_timestamps
    CharacterAlignmentResponseModel:
      type: object
      properties:
        characters:
          type: array
          items:
            type: string
        character_start_times_seconds:
          type: array
          items:
            type: number
            format: double
        character_end_times_seconds:
          type: array
          items:
            type: number
            format: double
      required:
        - characters
        - character_start_times_seconds
        - character_end_times_seconds
      title: CharacterAlignmentResponseModel
    VoiceSegment:
      type: object
      properties:
        voice_id:
          type: string
          description: The voice ID used for this segment
        start_time_seconds:
          type: number
          format: double
          description: Start time of this voice segment
        end_time_seconds:
          type: number
          format: double
          description: End time of this voice segment
        character_start_index:
          type: integer
          description: Start index in the characters array
        character_end_index:
          type: integer
          description: End index in the characters array (exclusive)
        dialogue_input_index:
          type: integer
          description: Line of the dialogue (script) that this segment is a part of.
      required:
        - voice_id
        - start_time_seconds
        - end_time_seconds
        - character_start_index
        - character_end_index
        - dialogue_input_index
      title: VoiceSegment
    AudioWithTimestampsAndVoiceSegmentsResponseModel:
      type: object
      properties:
        audio_base64:
          type: string
          description: Base64 encoded audio data
        alignment:
          oneOf:
            - $ref: '#/components/schemas/CharacterAlignmentResponseModel'
            - type: 'null'
          description: Timestamp information for each character in the original text
        normalized_alignment:
          oneOf:
            - $ref: '#/components/schemas/CharacterAlignmentResponseModel'
            - type: 'null'
          description: Timestamp information for each character in the normalized text
        voice_segments:
          type: array
          items:
            $ref: '#/components/schemas/VoiceSegment'
          description: Voice segments for the audio
      required:
        - audio_base64
        - voice_segments
      title: AudioWithTimestampsAndVoiceSegmentsResponseModel
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
  "inputs": [
    {
      "text": "Hello, how are you?",
      "voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    },
    {
      "text": "I'm doing well, thank you!",
      "voice_id": "6lCwbsX1yVjD49QmpkTR"
    }
  ]
}
```

**Response**

```json
{
  "audio_base64": "base64_encoded_audio_string",
  "voice_segments": [
    {
      "voice_id": "21m00Tcm4TlvDq8ikWAM",
      "start_time_seconds": 0,
      "end_time_seconds": 0.5,
      "character_start_index": 0,
      "character_end_index": 5,
      "dialogue_input_index": 0
    },
    {
      "voice_id": "VEDscrYI8uIMttlO2Ztu",
      "start_time_seconds": 0.5,
      "end_time_seconds": 0.7,
      "character_start_index": 5,
      "character_end_index": 7,
      "dialogue_input_index": 1
    }
  ],
  "alignment": {
    "characters": [
      "H",
      "e",
      "l",
      "l",
      "o",
      "H",
      "i"
    ],
    "character_start_times_seconds": [
      0,
      0.1,
      0.2,
      0.3,
      0.4,
      0.5,
      0.6
    ],
    "character_end_times_seconds": [
      0.1,
      0.2,
      0.3,
      0.4,
      0.5,
      0.6,
      0.7
    ]
  },
  "normalized_alignment": {
    "characters": [
      "H",
      "e",
      "l",
      "l",
      "o",
      "H",
      "i"
    ],
    "character_start_times_seconds": [
      0,
      0.1,
      0.2,
      0.3,
      0.4,
      0.5,
      0.6
    ],
    "character_end_times_seconds": [
      0.1,
      0.2,
      0.3,
      0.4,
      0.5,
      0.6,
      0.7
    ]
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.textToDialogue.convertWithTimestamps({
        inputs: [
            {
                text: "Hello, how are you?",
                voiceId: "bYTqZQo3Jz7LQtmGTgwi",
            },
            {
                text: "I'm doing well, thank you!",
                voiceId: "6lCwbsX1yVjD49QmpkTR",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DialogueInput

client = ElevenLabs()

client.text_to_dialogue.convert_with_timestamps(
    inputs=[
        DialogueInput(
            text="Hello, how are you?",
            voice_id="bYTqZQo3Jz7LQtmGTgwi",
        ),
        DialogueInput(
            text="I\'m doing well, thank you!",
            voice_id="6lCwbsX1yVjD49QmpkTR",
        )
    ],
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

	url := "https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps"

	payload := strings.NewReader("{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps', [
  'body' => '{
  "inputs": [
    {
      "text": "Hello, how are you?",
      "voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    },
    {
      "text": "I\'m doing well, thank you!",
      "voice_id": "6lCwbsX1yVjD49QmpkTR"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["inputs": [
    [
      "text": "Hello, how are you?",
      "voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    ],
    [
      "text": "I'm doing well, thank you!",
      "voice_id": "6lCwbsX1yVjD49QmpkTR"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-dialogue/with-timestamps")! as URL,
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
