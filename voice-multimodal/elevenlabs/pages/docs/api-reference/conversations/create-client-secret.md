---
title: "Create realtime client secret"
source: https://elevenlabs.io/docs/api-reference/conversations/create-client-secret.md
path: docs/api-reference/conversations/create-client-secret
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create realtime client secret

POST https://api.elevenlabs.io/v1/convai/realtime/client_secrets
Content-Type: application/json

Create an ephemeral client secret for authenticating browser-based Realtime API sessions.

Reference: https://elevenlabs.io/docs/api-reference/conversations/create-client-secret

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

This endpoint expects a CreateClientSecretRequest.

- `session` (OpenAISessionConfig-Input, optional, nullable)
- `expires_after` (ExpiresAfter, optional, nullable)

## Response

### 200

Successful Response

- `value` (string, required)
- `expires_at` (integer, required)
- `session` (OpenAISessionConfig-Output, optional, nullable)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### OpenAISessionConfig-Input

- `type` ("realtime", optional, default: realtime)
- `model` (enum, optional, default: eleven_realtime_v1_mini)
  - Allowed values: `eleven_realtime_v1_mini`, `eleven_realtime_v1_max`
- `instructions` (string, optional, default: )
- `output_modalities` (list of string, optional)
- `audio` (OpenAIAudioConfig-Input, optional)
- `tools` (list of OpenAiSessionConfigInputToolsItems, optional)
- `tool_choice` (OpenAiSessionConfigInputToolChoice, optional, default: auto)
- `temperature` (double, optional, default: 0.7)
- `max_response_output_tokens` (OpenAiSessionConfigInputMaxResponseOutputTokens, optional, default: 4096)
- `max_duration_seconds` (integer, optional, default: 600) — Maximum wall-clock duration of the session in seconds. The session is closed with code 1000 once it is exceeded.
- `turn_detection` (OpenAiSessionConfigInputTurnDetection, optional, nullable, default: __unset__)
- `tracing` (OpenAiSessionConfigInputTracing, optional, nullable)
- `include` (list of string, optional, nullable)
- `parallel_tool_calls` (boolean, optional, nullable)
- `reasoning` (map from string to any, optional, nullable)
- `truncation` (OpenAiSessionConfigInputTruncation, optional, nullable)
- `prompt` (map from string to any, optional, nullable)

### ExpiresAfter

- `seconds` (integer, required)
- `anchor` ("created_at", optional, default: created_at)

### OpenAISessionConfig-Output

- `type` ("realtime", optional, default: realtime)
- `model` (enum, optional, default: eleven_realtime_v1_mini)
  - Allowed values: `eleven_realtime_v1_mini`, `eleven_realtime_v1_max`
- `instructions` (string, optional, default: )
- `output_modalities` (list of string, optional)
- `audio` (OpenAIAudioConfig-Output, optional)
- `tools` (list of OpenAiSessionConfigOutputToolsItems, optional)
- `tool_choice` (OpenAiSessionConfigOutputToolChoice, optional, default: auto)
- `temperature` (double, optional, default: 0.7)
- `max_response_output_tokens` (OpenAiSessionConfigOutputMaxResponseOutputTokens, optional, default: 4096)
- `max_duration_seconds` (integer, optional, default: 600) — Maximum wall-clock duration of the session in seconds. The session is closed with code 1000 once it is exceeded.
- `tracing` (OpenAiSessionConfigOutputTracing, optional, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### OpenAIAudioConfig-Input

- `input` (OpenAIAudioInputConfig-Input, optional)
- `output` (OpenAIAudioOutputConfig-Input, optional)

### OpenAiSessionConfigInputToolsItems

- `type`: `function` (OpenAIFunctionTool)
  - `name` (string, required)
  - `description` (string, optional, default: )
  - `parameters` (map from string to any, optional)
- `type`: `mcp` (OpenAIMCPTool)
  - `server_label` (string, required)
  - `server_url` (string, required)
  - `allowed_tools` (list of string, optional, nullable)
  - `authorization` (string, optional, nullable)
  - `require_approval` (enum, optional, default: never)
    - Allowed values: `never`, `always`

### OpenAiSessionConfigInputToolChoice

### OpenAiSessionConfigInputMaxResponseOutputTokens

### OpenAiSessionConfigInputTurnDetection

### OpenAiSessionConfigInputTracing

### OpenAiSessionConfigInputTruncation

### OpenAIAudioConfig-Output

- `input` (OpenAIAudioInputConfig-Output, optional)
- `output` (OpenAIAudioOutputConfig-Output, optional)

### OpenAiSessionConfigOutputToolsItems

- `type`: `function` (OpenAIFunctionTool)
  - `name` (string, required)
  - `description` (string, optional, default: )
  - `parameters` (map from string to any, optional)
- `type`: `mcp` (OpenAIMCPTool)
  - `server_label` (string, required)
  - `server_url` (string, required)
  - `allowed_tools` (list of string, optional, nullable)
  - `authorization` (string, optional, nullable)
  - `require_approval` (enum, optional, default: never)
    - Allowed values: `never`, `always`

### OpenAiSessionConfigOutputToolChoice

### OpenAiSessionConfigOutputMaxResponseOutputTokens

### OpenAiSessionConfigOutputTracing

### ValidationErrorLocItems

### OpenAIAudioInputConfig-Input

- `format` (OpenAIAudioInputFormat, optional)
- `transcription` (OpenAIAudioInputTranscription, optional, nullable)
- `turn_detection` (OpenAITurnDetection, optional, nullable)
- `pacing` (enum, optional, default: realtime) — ``BURSTY`` clients stream ahead of wall time, so decisions use the audio clock.
  - Allowed values: `realtime`, `bursty`

### OpenAIAudioOutputConfig-Input

- `format` (OpenAIAudioOutputFormat, optional)
- `voice` (string, optional, default: brian)

### OpenAIToolChoiceFunction

- `function` (OpenAIToolChoiceFunctionInner, required)
- `type` ("function", optional, default: function)

### OpenAITurnDetection

- `type` (enum, optional, default: semantic_vad)
  - Allowed values: `semantic_vad`, `server_vad`
- `eagerness` (enum, optional, default: medium)
  - Allowed values: `low`, `medium`, `high`
- `create_response` (boolean, optional, default: true)
- `interrupt_response` (boolean, optional, default: true)
- `threshold` (double, optional, nullable)
- `prefix_padding_ms` (integer, optional, nullable)
- `silence_duration_ms` (integer, optional, nullable)
- `turn_timeout` (double, optional, default: -1)

### OpenAITracingConfiguration

Only ``group_id`` is acted on; ``workflow_name`` and ``metadata`` are kept so the echoed session matches the request.

- `group_id` (string, optional, nullable) — Adds conversation to the group (case-insensitive, up to 64 chars).
- `workflow_name` (string, optional, nullable)
- `metadata` (map from string to any, optional, nullable)

### OpenAIAudioInputConfig-Output

- `format` (OpenAIAudioInputFormat, optional)
- `transcription` (OpenAIAudioInputTranscription, optional, nullable)
- `turn_detection` (OpenAITurnDetection, optional, nullable)
- `pacing` (enum, optional, default: realtime) — ``BURSTY`` clients stream ahead of wall time, so decisions use the audio clock.
  - Allowed values: `realtime`, `bursty`

### OpenAIAudioOutputConfig-Output

- `format` (OpenAIAudioOutputFormat, optional)
- `voice` (string, optional, default: brian)

### OpenAIAudioInputFormat

- `type` (enum, optional, default: audio/pcm)
  - Allowed values: `audio/pcm`, `audio/pcmu`, `audio/pcma`
- `rate` (integer, optional, default: 24000)

### OpenAIAudioInputTranscription

- `language` (string, optional, nullable) — Language code of the conversation (e.g. en, es, pt-br), used for transcription, speech and the model's reply language. Defaults to en.

### OpenAIAudioOutputFormat

- `type` (enum, optional, default: audio/pcm)
  - Allowed values: `audio/pcm`, `audio/pcmu`, `audio/pcma`

### OpenAIToolChoiceFunctionInner

- `name` (string, required)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "value": "ek_realtime_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
  "expires_at": 1735689600,
  "session": {
    "type": "realtime",
    "model": "eleven_realtime_v1_mini",
    "instructions": "You are a helpful customer support assistant. Be concise and friendly in your responses.",
    "output_modalities": [
      "audio",
      "text"
    ],
    "audio": {
      "input": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        },
        "transcription": {
          "language": "en"
        },
        "turn_detection": {
          "type": "semantic_vad",
          "eagerness": "medium",
          "create_response": true,
          "interrupt_response": true,
          "threshold": 0.5,
          "prefix_padding_ms": 300,
          "silence_duration_ms": 500,
          "turn_timeout": -1
        },
        "pacing": "realtime"
      },
      "output": {
        "format": {
          "type": "audio/pcm"
        },
        "voice": "brian"
      }
    },
    "tools": [
      {
        "type": "function",
        "name": "get_order_status",
        "description": "Retrieves the current status of a customer order by order ID.",
        "parameters": {}
      }
    ],
    "tool_choice": "auto",
    "temperature": 0.7,
    "max_response_output_tokens": "inf",
    "max_duration_seconds": 600,
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
