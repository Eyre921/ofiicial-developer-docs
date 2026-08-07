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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `transcription_id` (string, required) — The unique ID of the transcript to retrieve

## Response

### 200

The transcript data

- `object or object or object or object`
  - SpeechToTextChunkResponseModel
    - `language_code` (string, required) — The detected language code (e.g. 'eng' for English).
    - `language_probability` (double, required) — The confidence score of the language detection (0 to 1).
    - `text` (string, required) — The raw text of the transcription.
    - `words` (list of object, required) — List of words with their timing information.
      - `text` (string, required) — The word or sound that was transcribed.
      - `type` (enum, required) — The type of the word or sound. 'audio_event' is used for non-word sounds like laughter or footsteps.
        - Allowed values: `word`, `spacing`, `audio_event`
      - `logprob` (double, required) — The log of the probability with which this word was predicted. Logprobs are in range [-infinity, 0], higher logprobs indicate a higher confidence the model has in its predictions.
      - `start` (double, optional, nullable) — The start time of the word or sound in seconds.
      - `end` (double, optional, nullable) — The end time of the word or sound in seconds.
      - `speaker_id` (string, optional, nullable) — Unique identifier for the speaker of this word.
      - `characters` (list of object, optional, nullable) — The characters that make up the word and their timing information.
        - `text` (string, required) — The character that was transcribed.
        - `start` (double, optional, nullable) — The start time of the character in seconds.
        - `end` (double, optional, nullable) — The end time of the character in seconds.
      - `channel_index` (integer, optional, nullable) — The channel this word was spoken on (for multichannel audio). Null for single-channel transcriptions.
    - `channel_index` (integer, optional, nullable) — The channel index this transcript belongs to (for multichannel audio).
    - `additional_formats` (list of object, optional, nullable) — Requested additional formats of the transcript.
      - `requested_format` (string, required) — The requested format.
      - `file_extension` (string, required) — The file extension of the additional format.
      - `content_type` (string, required) — The content type of the additional format.
      - `is_base64_encoded` (boolean, required) — Whether the content is base64 encoded.
      - `content` (string, required) — The content of the additional format.
    - `transcription_id` (string, optional, nullable) — The transcription ID of the response.
    - `entities` (list of object, optional, nullable) — List of detected entities with their text, type, and character positions in the transcript.
      - `text` (string, required) — The text that was identified as an entity.
      - `entity_type` (string, required) — The type of entity detected (e.g., 'credit_card', 'email_address', 'person_name').
      - `start_char` (integer, required) — Start character position in the transcript text.
      - `end_char` (integer, required) — End character position in the transcript text.
    - `audio_duration_secs` (double, optional, nullable) — The duration of the audio that was transcribed in seconds.
  - MultichannelSpeechToTextResponseModel
    - `transcripts` (list of object, required) — List of transcripts, one for each audio channel. Each transcript contains the text and word-level details for its respective channel.
      - `language_code` (string, required) — The detected language code (e.g. 'eng' for English).
      - `language_probability` (double, required) — The confidence score of the language detection (0 to 1).
      - `text` (string, required) — The raw text of the transcription.
      - `words` (list of object, required) — List of words with their timing information.
        - `text` (string, required) — The word or sound that was transcribed.
        - `type` (enum, required) — The type of the word or sound. 'audio_event' is used for non-word sounds like laughter or footsteps.
          - Allowed values: `word`, `spacing`, `audio_event`
        - `logprob` (double, required) — The log of the probability with which this word was predicted. Logprobs are in range [-infinity, 0], higher logprobs indicate a higher confidence the model has in its predictions.
        - `start` (double, optional, nullable) — The start time of the word or sound in seconds.
        - `end` (double, optional, nullable) — The end time of the word or sound in seconds.
        - `speaker_id` (string, optional, nullable) — Unique identifier for the speaker of this word.
        - `characters` (list of object, optional, nullable) — The characters that make up the word and their timing information.
          - `text` (string, required) — The character that was transcribed.
          - `start` (double, optional, nullable) — The start time of the character in seconds.
          - `end` (double, optional, nullable) — The end time of the character in seconds.
        - `channel_index` (integer, optional, nullable) — The channel this word was spoken on (for multichannel audio). Null for single-channel transcriptions.
      - `channel_index` (integer, optional, nullable) — The channel index this transcript belongs to (for multichannel audio).
      - `additional_formats` (list of object, optional, nullable) — Requested additional formats of the transcript.
        - `requested_format` (string, required) — The requested format.
        - `file_extension` (string, required) — The file extension of the additional format.
        - `content_type` (string, required) — The content type of the additional format.
        - `is_base64_encoded` (boolean, required) — Whether the content is base64 encoded.
        - `content` (string, required) — The content of the additional format.
      - `transcription_id` (string, optional, nullable) — The transcription ID of the response.
      - `entities` (list of object, optional, nullable) — List of detected entities with their text, type, and character positions in the transcript.
        - `text` (string, required) — The text that was identified as an entity.
        - `entity_type` (string, required) — The type of entity detected (e.g., 'credit_card', 'email_address', 'person_name').
        - `start_char` (integer, required) — Start character position in the transcript text.
        - `end_char` (integer, required) — End character position in the transcript text.
      - `audio_duration_secs` (double, optional, nullable) — The duration of the audio that was transcribed in seconds.
    - `transcription_id` (string, optional, nullable) — The transcription ID of the response.
    - `audio_duration_secs` (double, optional, nullable) — The duration of the audio that was transcribed across all channels in seconds.
  - SpeechToTextChunkResponseModel
    - `language_code` (string, required) — The detected language code (e.g. 'eng' for English).
    - `language_probability` (double, required) — The confidence score of the language detection (0 to 1).
    - `text` (string, required) — The raw text of the transcription.
    - `words` (list of object, required) — List of words with their timing information.
      - `text` (string, required) — The word or sound that was transcribed.
      - `type` (enum, required) — The type of the word or sound. 'audio_event' is used for non-word sounds like laughter or footsteps.
        - Allowed values: `word`, `spacing`, `audio_event`
      - `logprob` (double, required) — The log of the probability with which this word was predicted. Logprobs are in range [-infinity, 0], higher logprobs indicate a higher confidence the model has in its predictions.
      - `start` (double, optional, nullable) — The start time of the word or sound in seconds.
      - `end` (double, optional, nullable) — The end time of the word or sound in seconds.
      - `speaker_id` (string, optional, nullable) — Unique identifier for the speaker of this word.
      - `characters` (list of object, optional, nullable) — The characters that make up the word and their timing information.
        - `text` (string, required) — The character that was transcribed.
        - `start` (double, optional, nullable) — The start time of the character in seconds.
        - `end` (double, optional, nullable) — The end time of the character in seconds.
      - `channel_index` (integer, optional, nullable) — The channel this word was spoken on (for multichannel audio). Null for single-channel transcriptions.
    - `channel_index` (integer, optional, nullable) — The channel index this transcript belongs to (for multichannel audio).
    - `additional_formats` (list of object, optional, nullable) — Requested additional formats of the transcript.
      - `requested_format` (string, required) — The requested format.
      - `file_extension` (string, required) — The file extension of the additional format.
      - `content_type` (string, required) — The content type of the additional format.
      - `is_base64_encoded` (boolean, required) — Whether the content is base64 encoded.
      - `content` (string, required) — The content of the additional format.
    - `transcription_id` (string, optional, nullable) — The transcription ID of the response.
    - `entities` (list of object, optional, nullable) — List of detected entities with their text, type, and character positions in the transcript.
      - `text` (string, required) — The text that was identified as an entity.
      - `entity_type` (string, required) — The type of entity detected (e.g., 'credit_card', 'email_address', 'person_name').
      - `start_char` (integer, required) — Start character position in the transcript text.
      - `end_char` (integer, required) — End character position in the transcript text.
    - `audio_duration_secs` (double, optional, nullable) — The duration of the audio that was transcribed in seconds.
  - MultichannelSpeechToTextResponseModel
    - `transcripts` (list of object, required) — List of transcripts, one for each audio channel. Each transcript contains the text and word-level details for its respective channel.
      - `language_code` (string, required) — The detected language code (e.g. 'eng' for English).
      - `language_probability` (double, required) — The confidence score of the language detection (0 to 1).
      - `text` (string, required) — The raw text of the transcription.
      - `words` (list of object, required) — List of words with their timing information.
        - `text` (string, required) — The word or sound that was transcribed.
        - `type` (enum, required) — The type of the word or sound. 'audio_event' is used for non-word sounds like laughter or footsteps.
          - Allowed values: `word`, `spacing`, `audio_event`
        - `logprob` (double, required) — The log of the probability with which this word was predicted. Logprobs are in range [-infinity, 0], higher logprobs indicate a higher confidence the model has in its predictions.
        - `start` (double, optional, nullable) — The start time of the word or sound in seconds.
        - `end` (double, optional, nullable) — The end time of the word or sound in seconds.
        - `speaker_id` (string, optional, nullable) — Unique identifier for the speaker of this word.
        - `characters` (list of object, optional, nullable) — The characters that make up the word and their timing information.
          - `text` (string, required) — The character that was transcribed.
          - `start` (double, optional, nullable) — The start time of the character in seconds.
          - `end` (double, optional, nullable) — The end time of the character in seconds.
        - `channel_index` (integer, optional, nullable) — The channel this word was spoken on (for multichannel audio). Null for single-channel transcriptions.
      - `channel_index` (integer, optional, nullable) — The channel index this transcript belongs to (for multichannel audio).
      - `additional_formats` (list of object, optional, nullable) — Requested additional formats of the transcript.
        - `requested_format` (string, required) — The requested format.
        - `file_extension` (string, required) — The file extension of the additional format.
        - `content_type` (string, required) — The content type of the additional format.
        - `is_base64_encoded` (boolean, required) — Whether the content is base64 encoded.
        - `content` (string, required) — The content of the additional format.
      - `transcription_id` (string, optional, nullable) — The transcription ID of the response.
      - `entities` (list of object, optional, nullable) — List of detected entities with their text, type, and character positions in the transcript.
        - `text` (string, required) — The text that was identified as an entity.
        - `entity_type` (string, required) — The type of entity detected (e.g., 'credit_card', 'email_address', 'person_name').
        - `start_char` (integer, required) — Start character position in the transcript text.
        - `end_char` (integer, required) — End character position in the transcript text.
      - `audio_duration_secs` (double, optional, nullable) — The duration of the audio that was transcribed in seconds.
    - `transcription_id` (string, optional, nullable) — The transcription ID of the response.
    - `audio_duration_secs` (double, optional, nullable) — The duration of the audio that was transcribed across all channels in seconds.

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
