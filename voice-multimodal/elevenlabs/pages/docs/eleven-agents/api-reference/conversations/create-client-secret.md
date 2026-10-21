---
title: "Create realtime client secret"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/create-client-secret.md
path: docs/eleven-agents/api-reference/conversations/create-client-secret
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create realtime client secret

POST https://api.elevenlabs.io/v1/convai/realtime/client_secrets
Content-Type: application/json

Create an ephemeral client secret for authenticating browser-based Realtime API sessions.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/create-client-secret

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

This endpoint expects a CreateClientSecretRequest.

- `session` (OpenAiSessionConfigInput, optional)
- `expires_after` (ExpiresAfter, optional)

## Response

### 200

Successful Response

- `value` (string, required)
- `expires_at` (integer, required)
- `session` (OpenAiSessionConfigOutput, optional)

## Errors

### 422 Realtime Create Client Secret Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### OpenAiSessionConfigInput

- `type` ("realtime", optional)
- `model` (enum, optional, default: eleven_realtime_v1_mini)
  - Allowed values: `eleven_realtime_v1_mini`, `eleven_realtime_v1_max`
- `instructions` (string, optional, default: )
- `output_modalities` (list of string, optional)
- `audio` (OpenAiAudioConfigInput, optional)
- `tools` (list of OpenAiSessionConfigInputToolsItem, optional)
- `tool_choice` (OpenAiSessionConfigInputToolChoice, optional)
- `temperature` (double, optional, default: 0.7)
- `max_response_output_tokens` (OpenAiSessionConfigInputMaxResponseOutputTokens, optional)
- `max_duration_seconds` (integer, optional, default: 600) — Maximum wall-clock duration of the session in seconds. The session is closed with code 1000 once it is exceeded.
- `turn_detection` (OpenAiSessionConfigInputTurnDetection, optional)
- `tracing` (OpenAiSessionConfigInputTracing, optional)
- `include` (list of string, optional)
- `parallel_tool_calls` (boolean, optional)
- `reasoning` (map from string to any, optional)
- `truncation` (OpenAiSessionConfigInputTruncation, optional)
- `prompt` (map from string to any, optional)

### ExpiresAfter

- `seconds` (integer, required)
- `anchor` ("created_at", optional)

### OpenAiSessionConfigOutput

- `type` ("realtime", optional)
- `model` (enum, optional, default: eleven_realtime_v1_mini)
  - Allowed values: `eleven_realtime_v1_mini`, `eleven_realtime_v1_max`
- `instructions` (string, optional, default: )
- `output_modalities` (list of string, optional)
- `audio` (OpenAiAudioConfigOutput, optional)
- `tools` (list of OpenAiSessionConfigOutputToolsItem, optional)
- `tool_choice` (OpenAiSessionConfigOutputToolChoice, optional)
- `temperature` (double, optional, default: 0.7)
- `max_response_output_tokens` (OpenAiSessionConfigOutputMaxResponseOutputTokens, optional)
- `max_duration_seconds` (integer, optional, default: 600) — Maximum wall-clock duration of the session in seconds. The session is closed with code 1000 once it is exceeded.
- `tracing` (OpenAiSessionConfigOutputTracing, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### OpenAiAudioConfigInput

- `input` (OpenAiAudioInputConfigInput, optional)
- `output` (OpenAiAudioOutputConfigInput, optional)

### OpenAiSessionConfigInputToolsItem

- `type`: `function`
  - `name` (string, required)
  - `description` (string, optional, default: )
  - `parameters` (map from string to any, optional)
- `type`: `mcp`
  - `server_label` (string, required)
  - `server_url` (string, required)
  - `allowed_tools` (list of string, optional)
  - `authorization` (string, optional)
  - `require_approval` (enum, optional, default: never)
    - Allowed values: `never`, `always`

### OpenAiSessionConfigInputToolChoice

- string
- Open AI Tool Choice Function: OpenAiToolChoiceFunction

### OpenAiSessionConfigInputMaxResponseOutputTokens

- integer
- "inf"

### OpenAiSessionConfigInputTurnDetection

- Open AI Turn Detection: OpenAiTurnDetection
- string

### OpenAiSessionConfigInputTracing

- "auto"
- Open AI Tracing Configuration: OpenAiTracingConfiguration

### OpenAiSessionConfigInputTruncation

- string
- map from string to any

### OpenAiAudioConfigOutput

- `input` (OpenAiAudioInputConfigOutput, optional)
- `output` (OpenAiAudioOutputConfigOutput, optional)

### OpenAiSessionConfigOutputToolsItem

- `type`: `function`
  - `name` (string, required)
  - `description` (string, optional, default: )
  - `parameters` (map from string to any, optional)
- `type`: `mcp`
  - `server_label` (string, required)
  - `server_url` (string, required)
  - `allowed_tools` (list of string, optional)
  - `authorization` (string, optional)
  - `require_approval` (enum, optional, default: never)
    - Allowed values: `never`, `always`

### OpenAiSessionConfigOutputToolChoice

- string
- Open AI Tool Choice Function: OpenAiToolChoiceFunction

### OpenAiSessionConfigOutputMaxResponseOutputTokens

- integer
- "inf"

### OpenAiSessionConfigOutputTracing

- "auto"
- Open AI Tracing Configuration: OpenAiTracingConfiguration

### ValidationErrorLocItem

- string
- integer

### OpenAiAudioInputConfigInput

- `format` (OpenAiAudioInputFormat, optional)
- `transcription` (OpenAiAudioInputTranscription, optional)
- `turn_detection` (OpenAiTurnDetection, optional)
- `pacing` (enum, optional, default: realtime) — ``BURSTY`` clients stream ahead of wall time, so decisions use the audio clock.
  - Allowed values: `realtime`, `bursty`

### OpenAiAudioOutputConfigInput

- `format` (OpenAiAudioOutputFormat, optional)
- `voice` (string, optional, default: brian)

### OpenAiToolChoiceFunction

- `function` (OpenAiToolChoiceFunctionInner, required)
- `type` ("function", optional)

### OpenAiTurnDetection

- `type` (enum, optional, default: semantic_vad)
  - Allowed values: `semantic_vad`, `server_vad`
- `eagerness` (enum, optional, default: medium)
  - Allowed values: `low`, `medium`, `high`
- `create_response` (boolean, optional, default: true)
- `interrupt_response` (boolean, optional, default: true)
- `threshold` (double, optional)
- `prefix_padding_ms` (integer, optional)
- `silence_duration_ms` (integer, optional)
- `turn_timeout` (double, optional, default: -1)

### OpenAiTracingConfiguration

Only ``group_id`` is acted on; ``workflow_name`` and ``metadata`` are kept so the echoed session matches the request.

- `group_id` (string, optional) — Adds conversation to the group (case-insensitive, up to 64 chars).
- `workflow_name` (string, optional)
- `metadata` (map from string to any, optional)

### OpenAiAudioInputConfigOutput

- `format` (OpenAiAudioInputFormat, optional)
- `transcription` (OpenAiAudioInputTranscription, optional)
- `turn_detection` (OpenAiTurnDetection, optional)
- `pacing` (enum, optional, default: realtime) — ``BURSTY`` clients stream ahead of wall time, so decisions use the audio clock.
  - Allowed values: `realtime`, `bursty`

### OpenAiAudioOutputConfigOutput

- `format` (OpenAiAudioOutputFormat, optional)
- `voice` (string, optional, default: brian)

### OpenAiAudioInputFormat

- `type` (enum, optional, default: audio/pcm)
  - Allowed values: `audio/pcm`, `audio/pcmu`, `audio/pcma`
- `rate` (integer, optional, default: 24000)

### OpenAiAudioInputTranscription

- `language` (string, optional) — Language code of the conversation (e.g. en, es, pt-br), used for transcription, speech and the model's reply language. Defaults to en.

### OpenAiAudioOutputFormat

- `type` (enum, optional, default: audio/pcm)
  - Allowed values: `audio/pcm`, `audio/pcmu`, `audio/pcma`

### OpenAiToolChoiceFunctionInner

- `name` (string, required)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "value": "value",
  "expires_at": 1,
  "session": {
    "type": "realtime",
    "model": "eleven_realtime_v1_mini",
    "instructions": "instructions",
    "output_modalities": [
      "output_modalities"
    ],
    "tools": [
      {
        "type": "function",
        "name": "name"
      }
    ],
    "tool_choice": "tool_choice",
    "temperature": 1.1,
    "max_response_output_tokens": "inf",
    "max_duration_seconds": 1,
    "tracing": "auto"
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/realtime/client_secrets"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/realtime/client_secrets';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "https://api.elevenlabs.io/v1/convai/realtime/client_secrets"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/convai/realtime/client_secrets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/realtime/client_secrets")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/realtime/client_secrets', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/realtime/client_secrets");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/realtime/client_secrets")! as URL,
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
