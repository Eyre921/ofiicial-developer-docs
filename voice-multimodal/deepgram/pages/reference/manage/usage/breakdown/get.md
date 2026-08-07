---
title: "Get Project Usage Breakdown"
source: https://developers.deepgram.com/reference/manage/usage/breakdown/get.md
path: reference/manage/usage/breakdown/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get Project Usage Breakdown

GET https://api.deepgram.com/v1/projects/{project_id}/usage/breakdown

Retrieves the usage breakdown for a specific project, with various filter options by API feature or by groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND logic.

Reference: https://developers.deepgram.com/reference/manage/usage/breakdown/get

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Query parameters

- `start` (string, optional) — Start date of the requested date range. Format accepted is YYYY-MM-DD
- `end` (string, optional) — End date of the requested date range. Format accepted is YYYY-MM-DD
- `grouping` (enum, optional) — Common usage grouping parameters
  - Allowed values: `accessor`, `endpoint`, `feature_set`, `models`, `method`, `tags`, `deployment`
- `accessor` (string, optional) — Filter for requests where a specific accessor was used
- `alternatives` (boolean, optional) — Filter for requests where alternatives were used
- `callback_method` (boolean, optional) — Filter for requests where callback method was used
- `callback` (boolean, optional) — Filter for requests where callback was used
- `channels` (boolean, optional) — Filter for requests where channels were used
- `custom_intent_mode` (boolean, optional) — Filter for requests where custom intent mode was used
- `custom_intent` (boolean, optional) — Filter for requests where custom intent was used
- `custom_topic_mode` (boolean, optional) — Filter for requests where custom topic mode was used
- `custom_topic` (boolean, optional) — Filter for requests where custom topic was used
- `deployment` (enum, optional) — Filter for requests where a specific deployment was used
  - Allowed values: `hosted`, `beta`, `self-hosted`
- `detect_entities` (boolean, optional) — Filter for requests where detect entities was used
- `detect_language` (boolean, optional) — Filter for requests where detect language was used
- `diarize` (boolean, optional) — Filter for requests where diarize was used
- `dictation` (boolean, optional) — Filter for requests where dictation was used
- `encoding` (boolean, optional) — Filter for requests where encoding was used
- `endpoint` (enum, optional) — Filter for requests where a specific endpoint was used
  - Allowed values: `listen`, `read`, `speak`, `agent`
- `extra` (boolean, optional) — Filter for requests where extra was used
- `filler_words` (boolean, optional) — Filter for requests where filler words was used
- `intents` (boolean, optional) — Filter for requests where intents was used
- `keyterm` (boolean, optional) — Filter for requests where keyterm was used
- `keywords` (boolean, optional) — Filter for requests where keywords was used
- `language` (boolean, optional) — Filter for requests where language was used
- `measurements` (boolean, optional) — Filter for requests where measurements were used
- `method` (enum, optional) — Filter for requests where a specific method was used
  - Allowed values: `sync`, `async`, `streaming`
- `model` (string, optional) — Filter for requests where a specific model uuid was used
- `multichannel` (boolean, optional) — Filter for requests where multichannel was used
- `numerals` (boolean, optional) — Filter for requests where numerals were used
- `paragraphs` (boolean, optional) — Filter for requests where paragraphs were used
- `profanity_filter` (boolean, optional) — Filter for requests where profanity filter was used
- `punctuate` (boolean, optional) — Filter for requests where punctuate was used
- `redact` (boolean, optional) — Filter for requests where redact was used
- `replace` (boolean, optional) — Filter for requests where replace was used
- `sample_rate` (boolean, optional) — Filter for requests where sample rate was used
- `search` (boolean, optional) — Filter for requests where search was used
- `sentiment` (boolean, optional) — Filter for requests where sentiment was used
- `smart_format` (boolean, optional) — Filter for requests where smart format was used
- `summarize` (boolean, optional) — Filter for requests where summarize was used
- `tag` (string, optional) — Filter for requests where a specific tag was used
- `topics` (boolean, optional) — Filter for requests where topics was used
- `utt_split` (boolean, optional) — Filter for requests where utt split was used
- `utterances` (boolean, optional) — Filter for requests where utterances was used
- `version` (boolean, optional) — Filter for requests where version was used

## Response

### 200

Usage breakdown response

- `start` (string, required) — Start date of the usage period
- `end` (string, required) — End date of the usage period
- `resolution` (object, required)
  - `units` (string, required) — Time unit for the resolution
  - `amount` (double, required) — Amount of units
- `results` (list of object, required)
  - `hours` (double, required) — Audio hours processed
  - `total_hours` (double, required) — Total hours including all processing
  - `agent_hours` (double, required) — Agent hours used
  - `tokens_in` (double, required) — Number of input tokens
  - `tokens_out` (double, required) — Number of output tokens
  - `tts_characters` (double, required) — Number of text-to-speech characters processed
  - `requests` (double, required) — Number of requests
  - `grouping` (object, required)
    - `start` (string, optional) — Start date for this group
    - `end` (string, optional) — End date for this group
    - `accessor` (string, optional, nullable) — Optional accessor identifier
    - `endpoint` (string, optional, nullable) — Optional endpoint identifier
    - `feature_set` (string, optional, nullable) — Optional feature set identifier
    - `models` (list of string, optional)
    - `method` (string, optional, nullable) — Optional method identifier
    - `tags` (list of string, optional, nullable) — Optional list of tags, null unless grouped by tags.
    - `deployment` (string, optional, nullable) — Optional deployment identifier

## Examples

**Response**

```json
{
  "start": "2025-01-16",
  "end": "2025-01-23",
  "resolution": {
    "units": "day",
    "amount": 1
  },
  "results": [
    {
      "hours": 1619.7242069444444,
      "total_hours": 1621.7395791666668,
      "agent_hours": 41.33564388888889,
      "tokens_in": 0,
      "tokens_out": 0,
      "tts_characters": 9158866,
      "requests": 373381,
      "grouping": {
        "start": "2025-01-16",
        "end": "2025-01-16",
        "accessor": "123456789012345678901234",
        "endpoint": "listen",
        "feature_set": "punctuate",
        "models": [
          "Nova-2"
        ],
        "method": "async",
        "tags": [
          "tag1",
          "tag2"
        ],
        "deployment": "self-hosted"
      }
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown"

querystring = {"accessor":"12345678-1234-1234-1234-123456789012","alternatives":"true","callback_method":"true","callback":"true","channels":"true","custom_intent_mode":"true","custom_intent":"true","custom_topic_mode":"true","custom_topic":"true","deployment":"hosted","detect_entities":"true","detect_language":"true","diarize":"true","dictation":"true","encoding":"true","endpoint":"listen","extra":"true","filler_words":"true","intents":"true","keyterm":"true","keywords":"true","language":"true","measurements":"true","method":"async","model":"6f548761-c9c0-429a-9315-11a1d28499c8","multichannel":"true","numerals":"true","paragraphs":"true","profanity_filter":"true","punctuate":"true","redact":"true","replace":"true","search":"true","sentiment":"true","smart_format":"true","summarize":"true","tag":"tag1","topics":"true","utt_split":"true","utterances":"true","version":"true"}

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true';
const options = {method: 'GET', headers: {Authorization: 'Token <apiKey>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Token <apiKey>")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Token <apiKey>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/breakdown?accessor=12345678-1234-1234-1234-123456789012&alternatives=true&callback_method=true&callback=true&channels=true&custom_intent_mode=true&custom_intent=true&custom_topic_mode=true&custom_topic=true&deployment=hosted&detect_entities=true&detect_language=true&diarize=true&dictation=true&encoding=true&endpoint=listen&extra=true&filler_words=true&intents=true&keyterm=true&keywords=true&language=true&measurements=true&method=async&model=6f548761-c9c0-429a-9315-11a1d28499c8&multichannel=true&numerals=true&paragraphs=true&profanity_filter=true&punctuate=true&redact=true&replace=true&search=true&sentiment=true&smart_format=true&summarize=true&tag=tag1&topics=true&utt_split=true&utterances=true&version=true")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

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
