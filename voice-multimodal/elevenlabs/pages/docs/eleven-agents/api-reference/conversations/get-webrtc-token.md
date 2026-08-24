---
title: "Get conversation token"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-webrtc-token.md
path: docs/eleven-agents/api-reference/conversations/get-webrtc-token
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get conversation token

GET https://api.elevenlabs.io/v1/convai/conversation/token

Get a WebRTC session token for real-time communication.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-webrtc-token

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, required) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `participant_name` (string, optional) — Optional custom participant name. If not provided, user ID will be used
- `branch_id` (string, optional) — The ID of the branch to use
- `environment` (string, optional) — The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.
- `debug_events_request` (boolean, optional, default: false) — Whether to enable debug events. Only available for users with editor access to the agent.

## Response

### 200

Successful Response

- `token` (string, required)
- `conversation_id` (string, required)

## Examples

**Response**

```json
{
  "token": "token",
  "conversation_id": "conversation_id"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.getWebrtcToken({
        agentId: "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        branchId: "branch_id",
        debugEventsRequest: true,
        environment: "environment",
        participantName: "participant_name",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.get_webrtc_token(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="branch_id",
    debug_events_request=True,
    environment="environment",
    participant_name="participant_name",
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

	url := "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_id&debug_events_request=true&environment=environment&participant_name=participant_name"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_id&debug_events_request=true&environment=environment&participant_name=participant_name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_id&debug_events_request=true&environment=environment&participant_name=participant_name")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_id&debug_events_request=true&environment=environment&participant_name=participant_name');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_id&debug_events_request=true&environment=environment&participant_name=participant_name");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_3701k3ttaq12ewp8b7qv5rfyszkz&branch_id=branch_id&debug_events_request=true&environment=environment&participant_name=participant_name")! as URL,
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
