---
title: "Get conversation token"
source: https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token.md
path: docs/api-reference/conversations/get-webrtc-token
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get conversation token

GET https://api.elevenlabs.io/v1/convai/conversation/token

Get a WebRTC session token for real-time communication.

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, required) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `participant_name` (string, optional, nullable) — Optional custom participant name. If not provided, user ID will be used
- `branch_id` (string, optional, nullable) — The ID of the branch to use
- `version_id` (string, optional, nullable) — The ID of the version to use
- `environment` (string, optional, nullable) — The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.
- `debug_events_request` (boolean, optional, default: false) — Whether to enable debug events. Only available for users with editor access to the agent.

## Response

### 200

Successful Response

- `token` (string, required)
- `conversation_id` (string, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb252YW5zYXRpb25fMTIzNDU2IiwiaWF0IjoxNjg3MjM0NTY3LCJleHAiOjE2ODcyMzgxNjd9.4f8e7d6c5b4a3e2f1d0c9b8a7d6c5b4a3e2f1d0c9b8a7d6c5b4a3e2f1d0c9b8a7",
  "conversation_id": "conv_9f8e7d6c5b4a3e2f1d0c9b8a7"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/conversation/token"

querystring = {"agent_id":"agent_3701k3ttaq12ewp8b7qv5rfyszkz","branch_id":"branch_9f8e7d6c5b4a3","debug_events_request":"false","environment":"production","participant_name":"jane_doe_92","version_id":"v1.3.0"}

payload = {}
headers = {
    "xi-api-key": "sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0';
const options = {
  method: 'GET',
  headers: {
    'xi-api-key': 'sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7',
    'Content-Type': 'application/json'
  },
  body: '{}'
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

	url := "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7")
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

url = URI("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0")
  .header("xi-api-key", "sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk_live_4f8e7d6c5b4a3e2f1d0c9b8a7",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_9f8e7d6c5b4a3&debug_events_request=false&environment=production&participant_name=jane_doe_92&version_id=v1.3.0")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
