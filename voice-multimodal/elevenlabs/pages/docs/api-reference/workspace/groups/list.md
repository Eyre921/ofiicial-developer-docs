---
title: "List workspace groups"
source: https://elevenlabs.io/docs/api-reference/workspace/groups/list.md
path: docs/api-reference/workspace/groups/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List workspace groups

GET https://api.elevenlabs.io/v1/workspace/groups

Get all groups in the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/groups/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `map from string to object`
  - `name` (string, required)
  - `id` (string, required)
  - `members` (list of string, required)
  - `permissions` (list of enum, required, nullable)
    - Allowed values: `text_to_speech`, `speech_to_speech`, `speech_to_text`, `voice_lab`, `sound_effects`, `projects`, `voiceover_studio`, `dubbing`, `audio_native`, `conversational_ai`, `conversational_ai_read`, `voice_isolator`, `ai_speech_classifier`, `synthid_detector`, `add_voice_from_voice_library`, `create_instant_voice_clone`, `create_professional_voice_clone`, `create_user_api_key`, `publish_studio_project`, `music`, `image_video_generation`, `flows`, `templates`, `share_voice_externally`, `publish_voice_to_voice_library`, `view_fiat_balance`, `workspace_analytics_full_read`, `service_accounts_manage`, `webhooks_manage`, `group_members_manage`, `workspace_members_invite`, `workspace_members_remove`, `terms_of_service_accept`, `audit_log_read`, `conversation_privacy_manage`, `copy_resources_cross_workspace`, `voice_design`
  - `group_usage_limit` (integer or "unlimited", optional, nullable)
  - `group_pvc_limit` (integer or "unlimited", optional, nullable)
  - `character_count` (integer, optional, nullable)
  - `scim_external_id` (string, optional, nullable)
  - `is_scim_synced` (boolean, optional, default: false)
  - `scim_group` (object, optional, nullable)
    - `scim_external_id` (string, required, nullable)
    - `display_name` (string, required)
    - `created_at_unix` (integer, optional, nullable)
    - `updated_at_unix` (integer, optional, nullable)
    - `seat_type` (enum, optional, nullable) — Seat types for workspace members.
      - Allowed values: `workspace_admin`, `workspace_member`, `workspace_lite_member`
  - `scim_frozen` (boolean, optional, default: false)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "engineering_group": {
    "name": "Engineering Group",
    "id": "grp-4b7e9f2a",
    "members": [
      "user_11223",
      "user_44556"
    ],
    "permissions": [
      "speech_to_text",
      "voice_isolator",
      "ai_speech_classifier",
      "workspace_analytics_full_read",
      "webhooks_manage"
    ],
    "group_usage_limit": "unlimited",
    "group_pvc_limit": 1000,
    "character_count": 1200000,
    "scim_external_id": null,
    "is_scim_synced": false,
    "scim_group": null,
    "scim_frozen": false
  },
  "marketing_team": {
    "name": "Marketing Team",
    "id": "grp-8f3a2c1d",
    "members": [
      "user_12345",
      "user_67890",
      "user_54321"
    ],
    "permissions": [
      "text_to_speech",
      "voice_lab",
      "projects",
      "workspace_members_invite",
      "group_members_manage"
    ],
    "group_usage_limit": 500000,
    "group_pvc_limit": "unlimited",
    "character_count": 350000,
    "scim_external_id": "scim-ext-001",
    "is_scim_synced": true,
    "scim_group": {
      "scim_external_id": "scim-ext-001",
      "display_name": "Marketing Team SCIM",
      "created_at_unix": 1672531200,
      "updated_at_unix": 1688208000,
      "seat_type": "workspace_member"
    },
    "scim_frozen": false
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.groups.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.groups.list()

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

	url := "https://api.elevenlabs.io/v1/workspace/groups"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/workspace/groups")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/groups")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/groups', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/groups");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/groups")! as URL,
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
