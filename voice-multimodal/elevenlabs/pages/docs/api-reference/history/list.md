---
title: "Get generated items"
source: https://elevenlabs.io/docs/api-reference/history/list.md
path: docs/api-reference/history/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get generated items

GET https://api.elevenlabs.io/v1/history

Returns a list of your generated audio (e.g. text to speech, speech to speech, Studio, dubbing). Music and SFX generations are not included and cannot currently be retrieved via the API.

Reference: https://elevenlabs.io/docs/api-reference/history/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 100) — How many history items to return at maximum. Can not exceed 1000, defaults to 100.
- `start_after_history_item_id` (string, optional, nullable) — After which ID to start fetching, use this parameter to paginate across a large collection of history items. In case this parameter is not provided history items will be fetched starting from the most recently created one ordered descending by their creation date.
- `voice_id` (string, optional, nullable) — ID of the voice to be filtered for. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.
- `model_id` (string, optional, nullable) — Search term used for filtering history items. If provided, source becomes required.
- `date_before_unix` (integer, optional, nullable) — Unix timestamp to filter history items before this date (exclusive).
- `date_after_unix` (integer, optional, nullable) — Unix timestamp to filter history items after this date (inclusive).
- `sort_direction` (enum, optional, nullable, default: desc) — Sort direction for the results.
  - Allowed values: `asc`, `desc`
- `search` (string, optional, nullable) — search term used for filtering
- `source` (enum, optional, nullable) — Source of the generated history item
  - Allowed values: `TTS`, `STS`, `Flows`

## Response

### 200

Successful Response

- `history` (list of object, required) — A list of speech history items.
  - `history_item_id` (string, required) — The ID of the history item.
  - `date_unix` (integer, required) — Unix timestamp of when the item was created.
  - `character_count_change_from` (integer, required) — The character count change from.
  - `character_count_change_to` (integer, required) — The character count change to.
  - `content_type` (string, required) — The content type of the generated item.
  - `state` (any, required)
  - `request_id` (string, optional, nullable) — The ID of the request.
  - `voice_id` (string, optional, nullable) — The ID of the voice used.
  - `model_id` (string, optional, nullable) — The ID of the model.
  - `voice_name` (string, optional, nullable) — The name of the voice.
  - `voice_category` (enum, optional, nullable) — The category of the voice. Either 'premade', 'cloned', 'generated' or 'professional'.
    - Allowed values: `premade`, `cloned`, `generated`, `professional`
  - `text` (string, optional, nullable) — The text used to generate the audio item.
  - `settings` (map from string to any, optional, nullable) — The settings of the history item.
  - `share_link_id` (string, optional, nullable) — The ID of the share link.
  - `source` (enum, optional, nullable) — The source of the history item. Either TTS (text to speech), STS (speech to text), AN (audio native), Projects, Dubbing, PlayAPI, PD (pronunciation dictionary) or ConvAI (Agents Platform).
    - Allowed values: `TTS`, `STS`, `Projects`, `PD`, `AN`, `Dubbing`, `PlayAPI`, `ConvAI`, `VoiceGeneration`, `InVPC`, `Flows`
  - `alignments` (object, optional, nullable) — The alignments of the history item.
    - `alignment` (object, required) — The alignment of the text.
      - `characters` (list of string, required) — The characters in the alignment.
      - `character_start_times_seconds` (list of double, required) — The start times of the characters in seconds.
      - `character_end_times_seconds` (list of double, required) — The end times of the characters in seconds.
    - `normalized_alignment` (object, required) — The normalized alignment of the text.
      - `characters` (list of string, required) — The characters in the alignment.
      - `character_start_times_seconds` (list of double, required) — The start times of the characters in seconds.
      - `character_end_times_seconds` (list of double, required) — The end times of the characters in seconds.
  - `dialogue` (list of object, optional, nullable) — The dialogue (voice and text pairs) used to generate the audio item. If this is set then the top level `text` and `voice_id` fields will be empty.
    - `text` (string, required) — The text of the dialogue input line.
    - `voice_id` (string, required) — The ID of the voice used for this dialogue input line.
    - `voice_name` (string, required) — The name of the voice used for this dialogue input line.
  - `output_format` (string, optional, nullable) — The output format the audio was originally generated in.
- `has_more` (boolean, required) — Whether there are more history items to fetch.
- `last_history_item_id` (string, optional, nullable) — The ID of the last history item.
- `scanned_until` (integer, optional, nullable) — The timestamp of the last history item.

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
