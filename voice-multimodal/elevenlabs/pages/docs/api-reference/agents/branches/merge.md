---
title: "Merge agent branch"
source: https://elevenlabs.io/docs/api-reference/agents/branches/merge.md
path: docs/api-reference/agents/branches/merge
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Merge agent branch

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge
Content-Type: application/json

Merge a branch into a target branch

Reference: https://elevenlabs.io/docs/api-reference/agents/branches/merge

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
{
  "archive_source_branch": true,
  "force": false
}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.merge("agent_id", "source_branch_id", {
        targetBranchId: "target_branch_id",
        archiveSourceBranch: true,
        force: false,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.merge(
    agent_id="agent_id",
    source_branch_id="source_branch_id",
    target_branch_id="target_branch_id",
    archive_source_branch=True,
    force=False,
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/source_branch_id/merge?target_branch_id=target_branch_id"

	payload := strings.NewReader("{\n  \"archive_source_branch\": true,\n  \"force\": false\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/source_branch_id/merge?target_branch_id=target_branch_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"archive_source_branch\": true,\n  \"force\": false\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/source_branch_id/merge?target_branch_id=target_branch_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"archive_source_branch\": true,\n  \"force\": false\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/source_branch_id/merge?target_branch_id=target_branch_id', [
  'body' => '{
  "archive_source_branch": true,
  "force": false
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/source_branch_id/merge?target_branch_id=target_branch_id");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"archive_source_branch\": true,\n  \"force\": false\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "archive_source_branch": true,
  "force": false
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/source_branch_id/merge?target_branch_id=target_branch_id")! as URL,
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
