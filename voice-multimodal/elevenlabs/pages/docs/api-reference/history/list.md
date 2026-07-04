---
title: "Get generated items"
source: https://elevenlabs.io/docs/api-reference/history/list.md
path: docs/api-reference/history/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get generated items

GET https://api.elevenlabs.io/v1/history

Returns a list of your generated audio.

Reference: https://elevenlabs.io/docs/api-reference/history/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/history:
    get:
      operationId: list
      summary: Get generated items
      description: Returns a list of your generated audio.
      tags:
        - history
      parameters:
        - name: page_size
          in: query
          description: >-
            How many history items to return at maximum. Can not exceed 1000,
            defaults to 100.
          required: false
          schema:
            type: integer
            default: 100
        - name: start_after_history_item_id
          in: query
          description: >-
            After which ID to start fetching, use this parameter to paginate
            across a large collection of history items. In case this parameter
            is not provided history items will be fetched starting from the most
            recently created one ordered descending by their creation date.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: voice_id
          in: query
          description: >-
            ID of the voice to be filtered for. You can use the [Get
            voices](/docs/api-reference/voices/search) endpoint list all the
            available voices.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: model_id
          in: query
          description: >-
            Search term used for filtering history items. If provided, source
            becomes required.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: date_before_unix
          in: query
          description: Unix timestamp to filter history items before this date (exclusive).
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: date_after_unix
          in: query
          description: Unix timestamp to filter history items after this date (inclusive).
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: sort_direction
          in: query
          description: Sort direction for the results.
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/V1HistoryGetParametersSortDirectionSchema'
              - type: 'null'
            default: desc
        - name: search
          in: query
          description: search term used for filtering
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: source
          in: query
          description: Source of the generated history item
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/V1HistoryGetParametersSourceSchema'
              - type: 'null'
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
                $ref: '#/components/schemas/GetSpeechHistoryResponseModel'
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
    V1HistoryGetParametersSortDirectionSchema:
      type: string
      enum:
        - asc
        - desc
      default: desc
      description: Sort direction for the results.
      title: V1HistoryGetParametersSortDirectionSchema
    V1HistoryGetParametersSourceSchema:
      type: string
      enum:
        - TTS
        - STS
        - Flows
      description: Source of the generated history item
      title: V1HistoryGetParametersSourceSchema
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
    GetSpeechHistoryResponseModel:
      type: object
      properties:
        history:
          type: array
          items:
            $ref: '#/components/schemas/SpeechHistoryItemResponseModel'
          description: A list of speech history items.
        last_history_item_id:
          type:
            - string
            - 'null'
          description: The ID of the last history item.
        has_more:
          type: boolean
          description: Whether there are more history items to fetch.
        scanned_until:
          type:
            - integer
            - 'null'
          description: The timestamp of the last history item.
      required:
        - history
        - has_more
      title: GetSpeechHistoryResponseModel
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
  "history": [
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
  ],
  "has_more": true,
  "last_history_item_id": "ja9xsmfGhxYcymxGcOGB",
  "scanned_until": 1714650306
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.history.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.history.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/history"

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

url = URI("https://api.elevenlabs.io/v1/history")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/history")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/history');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/history");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/history")! as URL,
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
