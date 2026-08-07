---
title: "Get Resource"
source: https://elevenlabs.io/docs/api-reference/workspace/resources/get.md
path: docs/api-reference/workspace/resources/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Resource

GET https://api.elevenlabs.io/v1/workspace/resources/{resource_id}

Gets the metadata of a resource by ID.

Reference: https://elevenlabs.io/docs/api-reference/workspace/resources/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `resource_id` (string, required) — The ID of the target resource.

### Query parameters

- `resource_type` (enum, required) — Resource type of the target resource.
  - Allowed values: `voice`, `voice_collection`, `pronunciation_dictionary`, `dubbing`, `project`, `convai_agents`, `convai_knowledge_base_documents`, `convai_tools`, `convai_settings`, `convai_secrets`, `workspace_auth_connections`, `convai_phone_numbers`, `convai_mcp_servers`, `convai_api_integration_connections`, `convai_api_integration_trigger_connections`, `convai_batch_calls`, `convai_agent_response_tests`, `convai_test_suite_invocations`, `convai_crawl_jobs`, `convai_crawl_tasks`, `convai_kb_external_sync_jobs`, `convai_whatsapp_accounts`, `convai_agent_versions`, `convai_agent_branches`, `convai_agent_versions_deployments`, `convai_memory_entries`, `convai_coaching_proposals`, `convai_templates`, `dashboard`, `dashboard_configuration`, `convai_agent_drafts`, `resource_locators`, `assets`, `content_generations`, `content_templates`, `songs`, `transcription_tasks`, `avatars`, `avatar_video_generations`, `resource_collection`, `studio_projects`, `convai_analysis_items`

## Response

### 200

Successful Response

- `resource_id` (string, required) — The ID of the resource.
- `resource_name` (string, required, nullable) — The name of the resource, if available.
- `resource_type` (enum, required) — The type of the resource.
  - Allowed values: `voice`, `voice_collection`, `pronunciation_dictionary`, `dubbing`, `project`, `convai_agents`, `convai_knowledge_base_documents`, `convai_tools`, `convai_settings`, `convai_secrets`, `workspace_auth_connections`, `convai_phone_numbers`, `convai_mcp_servers`, `convai_api_integration_connections`, `convai_api_integration_trigger_connections`, `convai_batch_calls`, `convai_agent_response_tests`, `convai_test_suite_invocations`, `convai_crawl_jobs`, `convai_crawl_tasks`, `convai_kb_external_sync_jobs`, `convai_whatsapp_accounts`, `convai_agent_versions`, `convai_agent_branches`, `convai_agent_versions_deployments`, `convai_memory_entries`, `convai_coaching_proposals`, `convai_templates`, `dashboard`, `dashboard_configuration`, `convai_agent_drafts`, `resource_locators`, `assets`, `content_generations`, `content_templates`, `songs`, `transcription_tasks`, `avatars`, `avatar_video_generations`, `resource_collection`, `studio_projects`, `convai_analysis_items`
- `creator_user_id` (string, required, nullable) — The ID of the user who created the resource.
- `anonymous_access_level_override` (enum, required, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `role_to_group_ids` (map from string to list of string, required) — A mapping of roles to group IDs. When the resource is shared with a user, the group id is the user's id.
- `share_options` (list of object, required) — List of options for sharing the resource further in the workspace. These are users who don't have access to the resource yet.
  - `name` (string, required) — The name of the principal.
  - `id` (string, required) — The ID of the principal.
  - `type` (enum, required) — The type of the principal: user, group, or service account (under 'key').
    - Allowed values: `user`, `group`, `key`

## Examples

**Response**

```json
{
  "resource_id": "4ZUqyldxf71HqUbcP2Lc",
  "resource_name": "My Custom Voice",
  "resource_type": "voice",
  "creator_user_id": "5zavrE1kZXv2lFw9BKgEkf0B5Wqo",
  "anonymous_access_level_override": "viewer",
  "role_to_group_ids": {
    "admin": [
      "5zavrE1kZXv2lFw9BKgEkf0B5Wqo"
    ],
    "editor": [
      "8ruQDGM2R4w1mFbHI5aROCUjIpJZ"
    ],
    "viewer": []
  },
  "share_options": [
    {
      "name": "user@example.com",
      "id": "i2YYI6huwBmcgYydAXARmQJc3pmX",
      "type": "user"
    },
    {
      "name": "mygroup",
      "id": "x1AfvYKAmiqxCnbvZeNXHqqthJaC",
      "type": "group"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.resources.get("resource_id", {
        resourceType: "voice",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.resources.get(
    resource_id="resource_id",
    resource_type="voice",
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

	url := "https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice"

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

url = URI("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/resources/resource_id?resource_type=voice")! as URL,
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
