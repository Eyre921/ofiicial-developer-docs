---
title: "Delete draft"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/delete.md
path: docs/eleven-agents/api-reference/agents/drafts/delete
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Delete draft

DELETE https://api.elevenlabs.io/v1/convai/agents/{agent_id}/drafts

Delete a draft for an agent

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/delete

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Query parameters

- `branch_id` (string, required) — The ID of the agent branch to use

## Response

### 200

Successful Response

- `any`

## Examples

**Response**

```json
{
  "key": "value"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.drafts.delete("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        branchId: "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.drafts.delete(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj"

	req, _ := http.NewRequest("DELETE", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"

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
