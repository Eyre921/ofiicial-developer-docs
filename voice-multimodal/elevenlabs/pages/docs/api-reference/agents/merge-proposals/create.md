---
title: "Create A Merge Proposal"
source: https://elevenlabs.io/docs/api-reference/agents/merge-proposals/create.md
path: docs/api-reference/agents/merge-proposals/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create A Merge Proposal

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/merge-proposals
Content-Type: application/json

Record a request to merge a source branch into a target branch. Anyone with edit access can open one; merging it later is gated on write access to the target branch, so this is how a change reaches a protected branch the author cannot merge into themselves.

Reference: https://elevenlabs.io/docs/api-reference/agents/merge-proposals/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Body (application/json)

This endpoint expects a Body_Create_a_merge_proposal_v1_convai_agents__agent_id__merge_proposals_post.

- `source_branch_id` (string, required) — Branch whose changes should be merged.
- `target_branch_id` (string, required) — Branch that should receive the changes.
- `title` (string, required) — Short title for the merge_proposal.
- `description` (string, optional, default: ) — Optional longer description for reviewers.
- `requested_reviewer_user_ids` (list of string, optional, nullable) — User IDs to request a review from.
- `triage_ticket_id` (string, optional, nullable) — Triage ticket of this agent that the merge_proposal resolves. Merging it resolves the ticket if still open.

## Response

### 200

Successful Response

- `created_merge_proposal_id` (string, required) — ID of the created merge_proposal

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
{
  "source_branch_id": "string",
  "target_branch_id": "string",
  "title": "string"
}
```

**Response**

```json
{
  "created_merge_proposal_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.mergeProposals.create("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        sourceBranchId: "string",
        targetBranchId: "string",
        title: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.merge_proposals.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    source_branch_id="string",
    target_branch_id="string",
    title="string",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals"

	payload := strings.NewReader("{\n  \"source_branch_id\": \"string\",\n  \"target_branch_id\": \"string\",\n  \"title\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"source_branch_id\": \"string\",\n  \"target_branch_id\": \"string\",\n  \"title\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals")
  .header("Content-Type", "application/json")
  .body("{\n  \"source_branch_id\": \"string\",\n  \"target_branch_id\": \"string\",\n  \"title\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals', [
  'body' => '{
  "source_branch_id": "string",
  "target_branch_id": "string",
  "title": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"source_branch_id\": \"string\",\n  \"target_branch_id\": \"string\",\n  \"title\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "source_branch_id": "string",
  "target_branch_id": "string",
  "title": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals")! as URL,
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
