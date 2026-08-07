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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `history_item_id` (string, required) — ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

## Response

### 200

Successful Response

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
