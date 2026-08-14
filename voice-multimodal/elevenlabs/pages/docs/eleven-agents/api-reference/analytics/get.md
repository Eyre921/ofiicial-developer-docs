---
title: "Get live count"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/analytics/get.md
path: docs/eleven-agents/api-reference/analytics/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get live count

GET https://api.elevenlabs.io/v1/convai/analytics/live-count

Get the live count of the ongoing conversations.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/analytics/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, optional) — The id of an agent to restrict the analytics to.
- `agent_ids` (string, optional) — Restrict analytics to the union of the given agents. Takes precedence over `agent_id` when both are supplied.

## Response

### 200

Successful Response

- `count` (integer, required) — The number of active ongoing conversations.

## Examples

**Response**

```json
{
  "count": 42
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.analytics.liveCount.get({
        agentId: "agent_id",
        agentIds: [
            "agent_ids",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.analytics.live_count.get(
    agent_id="agent_id",
    agent_ids=[
        "agent_ids"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/analytics/live-count?agent_id=agent_id&agent_ids=%5B%22agent_ids%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/analytics/live-count?agent_id=agent_id&agent_ids=%5B%22agent_ids%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/analytics/live-count?agent_id=agent_id&agent_ids=%5B%22agent_ids%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/analytics/live-count?agent_id=agent_id&agent_ids=%5B%22agent_ids%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/analytics/live-count?agent_id=agent_id&agent_ids=%5B%22agent_ids%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/analytics/live-count?agent_id=agent_id&agent_ids=%5B%22agent_ids%22%5D")! as URL,
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
