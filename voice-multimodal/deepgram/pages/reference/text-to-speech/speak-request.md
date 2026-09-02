---
title: "Single Text Request"
source: https://developers.deepgram.com/reference/text-to-speech/speak-request.md
path: reference/text-to-speech/speak-request
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Single Text Request

POST https://api.deepgram.com/v1/speak
Content-Type: application/json

Convert text into natural-sounding speech using Deepgram's TTS REST API

Reference: https://developers.deepgram.com/reference/text-to-speech/speak-request

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
- `bit_rate` (enum or double or double, optional, default: 48000) — The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.
- `container` (enum or enum or enum or enum or enum, optional, default: wav) — Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.
- `encoding` (enum or enum or enum or enum or enum or enum or enum, optional, default: mp3) — Encoding allows you to specify the expected encoding of your audio output
- `model` (enum, optional, default: aura-asteria-en) — AI model used to process submitted text
  - Allowed values: `aura-angus-en`, `aura-arcas-en`, `aura-asteria-en`, `aura-athena-en`, `aura-helios-en`, `aura-hera-en`, `aura-luna-en`, `aura-orion-en`, `aura-orpheus-en`, `aura-perseus-en`, `aura-stella-en`, `aura-zeus-en`, `aura-2-amalthea-en`, `aura-2-andromeda-en`, `aura-2-apollo-en`, `aura-2-arcas-en`, `aura-2-aries-en`, `aura-2-asteria-en`, `aura-2-athena-en`, `aura-2-atlas-en`, `aura-2-aurora-en`, `aura-2-callista-en`, `aura-2-cora-en`, `aura-2-cordelia-en`, `aura-2-delia-en`, `aura-2-draco-en`, `aura-2-electra-en`, `aura-2-harmonia-en`, `aura-2-helena-en`, `aura-2-hera-en`, `aura-2-hermes-en`, `aura-2-hyperion-en`, `aura-2-iris-en`, `aura-2-janus-en`, `aura-2-juno-en`, `aura-2-jupiter-en`, `aura-2-luna-en`, `aura-2-mars-en`, `aura-2-minerva-en`, `aura-2-neptune-en`, `aura-2-odysseus-en`, `aura-2-ophelia-en`, `aura-2-orion-en`, `aura-2-orpheus-en`, `aura-2-pandora-en`, `aura-2-phoebe-en`, `aura-2-pluto-en`, `aura-2-saturn-en`, `aura-2-selene-en`, `aura-2-thalia-en`, `aura-2-theia-en`, `aura-2-vesta-en`, `aura-2-zeus-en`, `aura-2-agustina-es`, `aura-2-alvaro-es`, `aura-2-antonia-es`, `aura-2-aquila-es`, `aura-2-carina-es`, `aura-2-celeste-es`, `aura-2-diana-es`, `aura-2-estrella-es`, `aura-2-gloria-es`, `aura-2-javier-es`, `aura-2-luciano-es`, `aura-2-nestor-es`, `aura-2-olivia-es`, `aura-2-selena-es`, `aura-2-silvia-es`, `aura-2-sirio-es`, `aura-2-valerio-es`, `aura-2-aurelia-de`, `aura-2-elara-de`, `aura-2-fabian-de`, `aura-2-julius-de`, `aura-2-kara-de`, `aura-2-lara-de`, `aura-2-viktoria-de`, `aura-2-beatrix-nl`, `aura-2-cornelia-nl`, `aura-2-daphne-nl`, `aura-2-hestia-nl`, `aura-2-lars-nl`, `aura-2-leda-nl`, `aura-2-rhea-nl`, `aura-2-roman-nl`, `aura-2-sander-nl`, `aura-2-agathe-fr`, `aura-2-hector-fr`, `aura-2-cesare-it`, `aura-2-cinzia-it`, `aura-2-demetra-it`, `aura-2-dionisio-it`, `aura-2-elio-it`, `aura-2-flavio-it`, `aura-2-livia-it`, `aura-2-maia-it`, `aura-2-melia-it`, `aura-2-ama-ja`, `aura-2-ebisu-ja`, `aura-2-fujin-ja`, `aura-2-izanami-ja`, `aura-2-uzume-ja`
- `sample_rate` (enum or enum or enum or enum or enum, optional, default: 24000) — Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable
- `speed` (double, optional, default: 1) — Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody and voice quality. Not yet supported in all languages.

### Body (application/json)

- `text` (string, required) — The text content to be converted to speech

## Response

### 200

Successful text-to-speech transformation

## Examples

**Request**

```json
{
  "text": "Hello, welcome to Deepgram!"
}
```

**Response**

```json
{}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/speak"

querystring = {"model":"aura-2-thalia-en"}

payload = { "text": "Hello, welcome to Deepgram!" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/speak?model=aura-2-thalia-en';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"text":"Hello, welcome to Deepgram!"}'
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

	url := "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en"

	payload := strings.NewReader("{\n  \"text\": \"Hello, welcome to Deepgram!\"\n}")

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

url = URI("https://api.deepgram.com/v1/speak?model=aura-2-thalia-en")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Hello, welcome to Deepgram!\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/speak?model=aura-2-thalia-en")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Hello, welcome to Deepgram!\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/speak?model=aura-2-thalia-en', [
  'body' => '{
  "text": "Hello, welcome to Deepgram!"
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

var client = new RestClient("https://api.deepgram.com/v1/speak?model=aura-2-thalia-en");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Hello, welcome to Deepgram!\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["text": "Hello, welcome to Deepgram!"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en")! as URL,
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
