---
title: "Get history item"
source: https://elevenlabs.io/docs/api-reference/history/get.md
path: docs/api-reference/history/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get history item

GET https://api.elevenlabs.io/v1/history/{history_item_id}

Retrieves a history item.

Reference: https://elevenlabs.io/docs/api-reference/history/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/history/{history_item_id}:
    get:
      operationId: get
      summary: Get history item
      description: Retrieves a history item.
      tags:
        - subpackage_history
      parameters:
        - name: history_item_id
          in: path
          description: >-
            ID of the history item to be used. You can use the [Get generated
            items](/docs/api-reference/history/list) endpoint to retrieve a list
            of history items.
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
                $ref: '#/components/schemas/SpeechHistoryItemResponseModel'
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
    SpeechHistoryItemResponseModelVoiceCategory:
      type: string
      enum:
        - premade
        - cloned
        - generated
        - professional
      description: >-
        The category of the voice. Either 'premade', 'cloned', 'generated' or
        'professional'.
      title: SpeechHistoryItemResponseModelVoiceCategory
    FeedbackResponseModel:
      type: object
      properties:
        thumbs_up:
          type: boolean
          description: Whether the user liked the generated item.
        feedback:
          type: string
          description: The feedback text provided by the user.
        emotions:
          type: boolean
          description: Whether the user provided emotions.
        inaccurate_clone:
          type: boolean
          description: Whether the user thinks the clone is inaccurate.
        glitches:
          type: boolean
          description: Whether the user thinks there are glitches in the audio.
        audio_quality:
          type: boolean
          description: Whether the user thinks the audio quality is good.
        other:
          type: boolean
          description: Whether the user provided other feedback.
        review_status:
          type: string
          default: not_reviewed
          description: The review status of the item. Defaults to 'not_reviewed'.
      required:
        - thumbs_up
        - feedback
        - emotions
        - inaccurate_clone
        - glitches
        - audio_quality
        - other
      title: FeedbackResponseModel
    SpeechHistoryItemResponseModelSource:
      type: string
      enum:
        - TTS
        - STS
        - Projects
        - PD
        - AN
        - Dubbing
        - PlayAPI
        - ConvAI
        - VoiceGeneration
        - InVPC
        - Flows
      description: >-
        The source of the history item. Either TTS (text to speech), STS (speech
        to text), AN (audio native), Projects, Dubbing, PlayAPI, PD
        (pronunciation dictionary) or ConvAI (Agents Platform).
      title: SpeechHistoryItemResponseModelSource
    HistoryAlignmentResponseModel:
      type: object
      properties:
        characters:
          type: array
          items:
            type: string
          description: The characters in the alignment.
        character_start_times_seconds:
          type: array
          items:
            type: number
            format: double
          description: The start times of the characters in seconds.
        character_end_times_seconds:
          type: array
          items:
            type: number
            format: double
          description: The end times of the characters in seconds.
      required:
        - characters
        - character_start_times_seconds
        - character_end_times_seconds
      title: HistoryAlignmentResponseModel
    HistoryAlignmentsResponseModel:
      type: object
      properties:
        alignment:
          $ref: '#/components/schemas/HistoryAlignmentResponseModel'
          description: The alignment of the text.
        normalized_alignment:
          $ref: '#/components/schemas/HistoryAlignmentResponseModel'
          description: The normalized alignment of the text.
      required:
        - alignment
        - normalized_alignment
      title: HistoryAlignmentsResponseModel
    DialogueInputResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The text of the dialogue input line.
        voice_id:
          type: string
          description: The ID of the voice used for this dialogue input line.
        voice_name:
          type: string
          description: The name of the voice used for this dialogue input line.
      required:
        - text
        - voice_id
        - voice_name
      title: DialogueInputResponseModel
    SpeechHistoryItemResponseModel:
      type: object
      properties:
        history_item_id:
          type: string
          description: The ID of the history item.
        request_id:
          type:
            - string
            - 'null'
          description: The ID of the request.
        voice_id:
          type:
            - string
            - 'null'
          description: The ID of the voice used.
        model_id:
          type:
            - string
            - 'null'
          description: The ID of the model.
        voice_name:
          type:
            - string
            - 'null'
          description: The name of the voice.
        voice_category:
          oneOf:
            - $ref: '#/components/schemas/SpeechHistoryItemResponseModelVoiceCategory'
            - type: 'null'
          description: >-
            The category of the voice. Either 'premade', 'cloned', 'generated'
            or 'professional'.
        text:
          type:
            - string
            - 'null'
          description: The text used to generate the audio item.
        date_unix:
          type: integer
          description: Unix timestamp of when the item was created.
        character_count_change_from:
          type: integer
          description: The character count change from.
        character_count_change_to:
          type: integer
          description: The character count change to.
        content_type:
          type: string
          description: The content type of the generated item.
        state:
          description: Any type
        settings:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: The settings of the history item.
        feedback:
          oneOf:
            - $ref: '#/components/schemas/FeedbackResponseModel'
            - type: 'null'
          description: >-
            Feedback associated with the generated item. Returns null if no
            feedback has been provided.
        share_link_id:
          type:
            - string
            - 'null'
          description: The ID of the share link.
        source:
          oneOf:
            - $ref: '#/components/schemas/SpeechHistoryItemResponseModelSource'
            - type: 'null'
          description: >-
            The source of the history item. Either TTS (text to speech), STS
            (speech to text), AN (audio native), Projects, Dubbing, PlayAPI, PD
            (pronunciation dictionary) or ConvAI (Agents Platform).
        alignments:
          oneOf:
            - $ref: '#/components/schemas/HistoryAlignmentsResponseModel'
            - type: 'null'
          description: The alignments of the history item.
        dialogue:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/DialogueInputResponseModel'
          description: >-
            The dialogue (voice and text pairs) used to generate the audio item.
            If this is set then the top level `text` and `voice_id` fields will
            be empty.
        output_format:
          type:
            - string
            - 'null'
          description: The output format the audio was originally generated in.
      required:
        - history_item_id
        - date_unix
        - character_count_change_from
        - character_count_change_to
        - content_type
        - state
      title: SpeechHistoryItemResponseModel
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
  "history_item_id": "ja9xsmfGhxYcymxGcOGB",
  "date_unix": 1714650306,
  "character_count_change_from": 17189,
  "character_count_change_to": 17231,
  "content_type": "audio/mpeg",
  "state": null,
  "request_id": "BF0BZg4IwLGBlaVjv9Im",
  "voice_id": "21m00Tcm4TlvDq8ikWAM",
  "model_id": "eleven_multilingual_v2",
  "voice_name": "Rachel",
  "voice_category": "premade",
  "text": "Hello, world!",
  "settings": {
    "similarity_boost": 0.5,
    "stability": 0.71,
    "style": 0,
    "use_speaker_boost": true
  },
  "source": "TTS"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.history.get("history_item_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.history.get(
    history_item_id="history_item_id",
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

	url := "https://api.elevenlabs.io/v1/history/history_item_id"

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

url = URI("https://api.elevenlabs.io/v1/history/history_item_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/history/history_item_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/history/history_item_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/history/history_item_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history/history_item_id")! as URL,
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
