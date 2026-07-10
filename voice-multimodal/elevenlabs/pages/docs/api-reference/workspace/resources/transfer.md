---
title: "Transfer Workspace Resource Ownership"
source: https://elevenlabs.io/docs/api-reference/workspace/resources/transfer.md
path: docs/api-reference/workspace/resources/transfer
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Transfer Workspace Resource Ownership

POST https://api.elevenlabs.io/v1/workspace/resources/{resource_id}/transfer
Content-Type: application/json

Transfers ownership of a workspace resource from the current owner to another user in the same workspace. You must be the resource's current owner to transfer it. The previous owner keeps admin access to the resource.

Reference: https://elevenlabs.io/docs/api-reference/workspace/resources/transfer

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/resources/{resource_id}/transfer:
    post:
      operationId: transfer
      summary: Transfer Workspace Resource Ownership
      description: >-
        Transfers ownership of a workspace resource from the current owner to
        another user in the same workspace. You must be the resource's current
        owner to transfer it. The previous owner keeps admin access to the
        resource.
      tags:
        - resources
      parameters:
        - name: resource_id
          in: path
          description: The ID of the target resource.
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
                #/components/schemas/Body_Transfer_workspace_resource_ownership_v1_workspace_resources__resource_id__transfer_post
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
    WorkspaceResourceType:
      type: string
      enum:
        - voice
        - voice_collection
        - pronunciation_dictionary
        - dubbing
        - project
        - convai_agents
        - convai_knowledge_base_documents
        - convai_tools
        - convai_settings
        - convai_secrets
        - workspace_auth_connections
        - convai_phone_numbers
        - convai_mcp_servers
        - convai_api_integration_connections
        - convai_api_integration_trigger_connections
        - convai_batch_calls
        - convai_agent_response_tests
        - convai_test_suite_invocations
        - convai_crawl_jobs
        - convai_crawl_tasks
        - convai_kb_external_sync_jobs
        - convai_whatsapp_accounts
        - convai_agent_versions
        - convai_agent_branches
        - convai_agent_versions_deployments
        - convai_memory_entries
        - convai_coaching_proposals
        - convai_templates
        - dashboard
        - dashboard_configuration
        - convai_agent_drafts
        - resource_locators
        - assets
        - content_generations
        - content_templates
        - songs
        - transcription_tasks
        - avatars
        - avatar_video_generations
        - resource_collection
        - studio_projects
      description: >-
        Resource types that can be shared in the workspace. The name always need
        to match the collection names
      title: WorkspaceResourceType
    Body_Transfer_workspace_resource_ownership_v1_workspace_resources__resource_id__transfer_post:
      type: object
      properties:
        resource_type:
          $ref: '#/components/schemas/WorkspaceResourceType'
          description: Resource type of the target resource.
        target_user_id:
          type: string
          description: The ID of the user the resource should be transferred to.
      required:
        - resource_type
        - target_user_id
      title: >-
        Body_Transfer_workspace_resource_ownership_v1_workspace_resources__resource_id__transfer_post
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
  "resource_type": "voice_collection",
  "target_user_id": "user_8f3b2c9d7a4e"
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
    await client.workspace.resources.transfer("resource_id", {
        resourceType: "voice_collection",
        targetUserId: "user_8f3b2c9d7a4e",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.resources.transfer(
    resource_id="resource_id",
    resource_type="voice_collection",
    target_user_id="user_8f3b2c9d7a4e",
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

	url := "https://api.elevenlabs.io/v1/workspace/resources/resource_id/transfer"

	payload := strings.NewReader("{\n  \"resource_type\": \"voice_collection\",\n  \"target_user_id\": \"user_8f3b2c9d7a4e\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/resources/resource_id/transfer")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"resource_type\": \"voice_collection\",\n  \"target_user_id\": \"user_8f3b2c9d7a4e\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/resources/resource_id/transfer")
  .header("Content-Type", "application/json")
  .body("{\n  \"resource_type\": \"voice_collection\",\n  \"target_user_id\": \"user_8f3b2c9d7a4e\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/resources/resource_id/transfer', [
  'body' => '{
  "resource_type": "voice_collection",
  "target_user_id": "user_8f3b2c9d7a4e"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/resources/resource_id/transfer");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"resource_type\": \"voice_collection\",\n  \"target_user_id\": \"user_8f3b2c9d7a4e\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "resource_type": "voice_collection",
  "target_user_id": "user_8f3b2c9d7a4e"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/resources/resource_id/transfer")! as URL,
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
