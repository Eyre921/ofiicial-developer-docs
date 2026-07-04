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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge:
    post:
      operationId: merge
      summary: Merge A Branch Into A Target Branch
      description: Merge a branch into a target branch
      tags:
        - branches
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: source_branch_id
          in: path
          description: Unique identifier for the source branch to merge from.
          required: true
          schema:
            type: string
        - name: target_branch_id
          in: query
          description: The ID of the target branch to merge into.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Merge_a_branch_into_a_target_branch_v1_convai_agents__agent_id__branches__source_branch_id__merge_post
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    Body_Merge_a_branch_into_a_target_branch_v1_convai_agents__agent_id__branches__source_branch_id__merge_post:
      type: object
      properties:
        archive_source_branch:
          type: boolean
          default: true
          description: Whether to archive the source branch after merging
        force:
          type: boolean
          default: false
          description: >-
            Force source branch changes onto the target, overriding
            timestamp-based conflict resolution
      title: >-
        Body_Merge_a_branch_into_a_target_branch_v1_convai_agents__agent_id__branches__source_branch_id__merge_post
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
