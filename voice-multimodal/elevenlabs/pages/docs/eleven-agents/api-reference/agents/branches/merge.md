---
title: "Merge agent branch"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/merge.md
path: docs/eleven-agents/api-reference/agents/branches/merge
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Merge agent branch

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge
Content-Type: application/json

Merge a branch into a target branch

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/merge

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.
- `source_branch_id` (string, required) — Unique identifier for the source branch to merge from.

### Query parameters

- `target_branch_id` (string, required) — The ID of the target branch to merge into.

### Body (application/json)

- `archive_source_branch` (boolean, optional, default: true) — Whether to archive the source branch after merging
- `force` (boolean, optional, default: false) — Force source branch changes onto the target, overriding timestamp-based conflict resolution

## Response

### 200

Successful Response

- `any`

## Examples

**Request**

```json
{}
```

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
    await client.conversationalAi.agents.branches.merge("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbrch_8901k4t9z5defmb8vh3e9361y7nj", {
        targetBranchId: "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.merge(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    target_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
)

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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/merge?target_branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/merge?target_branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/merge?target_branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/merge?target_branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/merge?target_branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/merge?target_branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")! as URL,
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
