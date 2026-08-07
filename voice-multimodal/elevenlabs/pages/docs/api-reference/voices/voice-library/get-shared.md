---
title: "List shared voices"
source: https://elevenlabs.io/docs/api-reference/voices/voice-library/get-shared.md
path: docs/api-reference/voices/voice-library/get-shared
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List shared voices

GET https://api.elevenlabs.io/v1/shared-voices

Retrieves a list of shared voices.

Reference: https://elevenlabs.io/docs/api-reference/voices/voice-library/get-shared

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 30) — How many shared voices to return at maximum. Can not exceed 100, defaults to 30.
- `category` (enum, optional) — Voice category used for filtering
  - Allowed values: `professional`, `famous`, `high_quality`
- `gender` (string, optional, nullable) — Gender used for filtering
- `age` (string, optional, nullable) — Age used for filtering
- `accent` (string, optional, nullable) — Accent used for filtering
- `language` (string, optional, nullable) — Language used for filtering
- `locale` (string, optional, nullable) — Locale used for filtering
- `search` (string, optional, nullable) — Search term used for filtering
- `use_cases` (list of string, optional, nullable) — Use-case used for filtering
- `descriptives` (list of string, optional, nullable) — Search term used for filtering
- `featured` (boolean, optional, default: false) — Filter featured voices
- `min_notice_period_days` (integer, optional, nullable) — Filter voices with a minimum notice period of the given number of days.
- `include_custom_rates` (boolean, optional, nullable) — Include/exclude voices with custom rates
- `include_live_moderated` (boolean, optional, nullable) — Include/exclude voices that are live moderated
- `reader_app_enabled` (boolean, optional, default: false) — Filter voices that are enabled for the reader app
- `owner_id` (string, optional, nullable) — Filter voices by public owner ID
- `sort` (enum, optional, default: created_date) — Sort criteria. Must be one of: created_date, usage_character_count_1y, trending, cloned_by_count.
  - Allowed values: `created_date`, `usage_character_count_1y`, `trending`, `cloned_by_count`
- `page` (integer, optional, default: 0)

## Response

### 200

Successful Response

- `voices` (list of object, required) — The list of shared voices
  - `public_owner_id` (string, required) — The public owner id of the voice.
  - `voice_id` (string, required) — The id of the voice.
  - `date_unix` (integer, required) — The date the voice was added to the library in Unix time.
  - `name` (string, required) — The name of the voice.
  - `accent` (string, required) — The accent of the voice.
  - `gender` (string, required) — The gender of the voice.
  - `age` (string, required) — The age of the voice.
  - `descriptive` (string, required) — The descriptive of the voice.
  - `use_case` (string, required) — The use case of the voice.
  - `category` (enum, required) — The category of the voice.
    - Allowed values: `generated`, `cloned`, `premade`, `professional`, `famous`, `high_quality`
  - `usage_character_count_1y` (integer, required) — The usage character count of the voice in the last year.
  - `usage_character_count_7d` (integer, required) — The usage character count of the voice in the last 7 days.
  - `play_api_usage_character_count_1y` (integer, required) — The play API usage character count of the voice in the last year.
  - `cloned_by_count` (integer, required) — The number of times the voice has been cloned.
  - `free_users_allowed` (boolean, required) — Whether free users are allowed to use the voice.
  - `live_moderation_enabled` (boolean, required) — Whether live moderation is enabled for the voice.
  - `featured` (boolean, required) — Whether the voice is featured.
  - `language` (string, optional, nullable) — The language of the voice.
  - `locale` (string, optional, nullable) — The locale of the voice.
  - `description` (string, optional, nullable) — The description of the voice.
  - `preview_url` (string, optional, nullable) — The preview URL of the voice.
  - `rate` (double, optional, nullable) — The rate multiplier of the voice.
  - `fiat_rate` (double, optional, nullable) — The rate of the voice in USD per 1000 credits. null if default
  - `verified_languages` (list of object, optional, nullable) — The verified languages of the voice.
    - `language` (string, required) — The language of the voice.
    - `model_id` (string, required) — The voice's model ID.
    - `accent` (string, optional, nullable) — The voice's accent, if applicable.
    - `locale` (string, optional, nullable) — The voice's locale, if applicable.
    - `preview_url` (string, optional, nullable) — The voice's preview URL, if applicable.
  - `notice_period` (integer, optional, nullable) — The notice period of the voice.
  - `instagram_username` (string, optional, nullable) — The Instagram username of the voice.
  - `twitter_username` (string, optional, nullable) — The Twitter username of the voice.
  - `youtube_username` (string, optional, nullable) — The YouTube username of the voice.
  - `tiktok_username` (string, optional, nullable) — The TikTok username of the voice.
  - `image_url` (string, optional, nullable) — The image URL of the voice.
  - `is_added_by_user` (boolean, optional, nullable) — Whether the voice was added by the user.
  - `is_bookmarked` (boolean, optional, nullable) — Whether the voice is bookmarked by the current user. Only relevant when is_added_by_user is True.
- `has_more` (boolean, required) — Whether there are more shared voices in subsequent pages.
- `total_count` (integer, optional, default: 0) — The total number of shared voices matching the query.
- `last_sort_id` (string, optional, nullable)

## Examples

**Response**

```json
{
  "voices": [
    {
      "public_owner_id": "63e84100a6bf7874ba37a1bab9a31828a379ec94b891b401653b655c5110880f",
      "voice_id": "sB1b5zUrxQVAFl2PhZFp",
      "date_unix": 1714423232,
      "name": "Alita",
      "accent": "american",
      "gender": "Female",
      "age": "young",
      "descriptive": "calm",
      "use_case": "characters_animation",
      "category": "professional",
      "usage_character_count_1y": 12852,
      "usage_character_count_7d": 12852,
      "play_api_usage_character_count_1y": 12852,
      "cloned_by_count": 11,
      "free_users_allowed": true,
      "live_moderation_enabled": false,
      "featured": false,
      "language": "en",
      "description": "Perfectly calm, neutral and strong voice. Great for a young female protagonist.",
      "preview_url": "https://storage.googleapis.com/eleven-public-prod/wqkMCd9huxXHX1dy5mLJn4QEQHj1/voices/sB1b5zUrxQVAFl2PhZFp/55e71aac-5cb7-4b3d-8241-429388160509.mp3",
      "rate": 1,
      "verified_languages": [
        {
          "language": "en",
          "model_id": "eleven_multilingual_v2",
          "accent": "american",
          "locale": "en-US",
          "preview_url": "https://storage.googleapis.com/eleven-public-prod/wqkMCd9huxXHX1dy5mLJn4QEQHj1/voices/sB1b5zUrxQVAFl2PhZFp/55e71aac-5cb7-4b3d-8241-429388160509.mp3"
        }
      ]
    }
  ],
  "has_more": false,
  "total_count": 0
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.getShared({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.get_shared()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/shared-voices"

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

url = URI("https://api.elevenlabs.io/v1/shared-voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/shared-voices")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/shared-voices');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/shared-voices");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/shared-voices")! as URL,
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
