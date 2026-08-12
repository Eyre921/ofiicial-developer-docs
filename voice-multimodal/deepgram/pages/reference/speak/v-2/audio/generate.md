---
title: "Flux Text to Speech (batch)"
source: https://developers.deepgram.com/reference/speak/v-2/audio/generate.md
path: reference/speak/v-2/audio/generate
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux Text to Speech (batch)

POST https://api.deepgram.com/v2/speak
Content-Type: application/json

Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API. Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up front and you don't need incremental playback or interruption.

Reference: https://developers.deepgram.com/reference/speak/v-2/audio/generate

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`
- `Authorization` header (bearer token, required) — Use `Authorization: Bearer <JWT>` Example: `Authorization: Bearer eyJhbGciOiJ...`

## Request

### Query parameters

- `callback` (string, optional) — URL to which we'll make the callback request
- `callback_method` (enum, optional, default: POST) — HTTP method by which the callback request will be made
  - Allowed values: `POST`, `PUT`
- `mip_opt_out` (boolean, optional, default: false) — Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip
- `tag` (string or list of string, optional) — Label your requests for the purpose of identification during usage reporting
- `bit_rate` (enum or integer or integer, optional, default: 48000) — The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.
- `container` (enum or enum or enum or enum or enum, optional, default: wav) — Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.
- `encoding` (enum or enum or enum or enum or enum or enum or enum, optional, default: mp3) — Encoding allows you to specify the expected encoding of your audio output
- `expressivity` (enum, optional, default: 0) — Expressive range of the generated speech, on a calm-to-animated axis. Accepted values: `-2`, `-1`, `0`, `1`, `2`. `0` (the default) is the voice's tuned delivery and the production-validated setting; negative values are calmer and more measured, positive values more animated. Supported on all Flux voices; applies to the whole request. Beta: behavior may change in future model versions, and non-default values increase the risk of hallucinations and pronunciation errors; audition before shipping. An invalid value is rejected with a `400` — `EXPRESSIVITY_OUT_OF_RANGE` for a value outside the range, `EXPRESSIVITY_INCREMENT_INVALID` for a fractional value. See [Expressivity](/docs/tts-expressivity).
  - Allowed values: `-2`, `-1`, `0`, `1`, `2`
- `model` (string, required) — Flux TTS model used to synthesize the submitted text, in the form `flux-{voice}-{language}` (for example, `flux-alexis-en`). Required; unlike the v1 (Aura) endpoint there is no default and only flux models are accepted. English-only at launch.
- `sample_rate` (enum or enum or enum or enum, optional, default: 24000) — Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable
- `speed` (enum, optional, default: 1) — Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody and voice quality. Accepted values run `0.85` to `1.15` in `0.05` increments. Not yet supported in all languages.
  - Allowed values: `0.85`, `0.9`, `0.95`, `1`, `1.05`, `1.1`, `1.15`
- `priority` (enum, optional) — Processing priority for asynchronous (callback) requests. The only supported value is low.
  - Allowed values: `low`

### Body (application/json)

- `text` (string, required) — The text content to be converted to speech. The server normalizes and preprocesses the text before synthesis. Inline pause and pronunciation controls are not yet applied; they are stripped from the text before synthesis.

## Response

### 200

Returns the synthesized audio in the requested encoding as a binary stream. When a `callback` URL is supplied, the request is processed asynchronously and the response body is instead a JSON acknowledgement (Content-Type `application/json`) of the form \{"request\_id": "..."}, with the audio delivered to the callback URL. Because this endpoint is typed as a binary audio stream, SDK callers that set `callback` receive this JSON acknowledgement through the audio byte iterator as raw bytes and must join the chunks and parse `request_id` themselves.

- `request_id` (string, required) — Unique identifier for tracking the asynchronous request

## Examples

**Request**

```json
{
  "text": "Your appointment is confirmed for 3pm tomorrow."
}
```

**Response**

```json
{
  "request_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v2/speak"

querystring = {"expressivity":"1","model":"flux-alexis-en","speed":"1.05"}

payload = { "text": "Your appointment is confirmed for 3pm tomorrow." }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"text":"Your appointment is confirmed for 3pm tomorrow."}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05"

	payload := strings.NewReader("{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
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

url = URI("https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05', [
  'body' => '{
  "text": "Your appointment is confirmed for 3pm tomorrow."
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["text": "Your appointment is confirmed for 3pm tomorrow."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v2/speak?expressivity=1&model=flux-alexis-en&speed=1.05")! as URL,
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
