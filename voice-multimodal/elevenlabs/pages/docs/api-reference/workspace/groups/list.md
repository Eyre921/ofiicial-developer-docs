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

**Response**

```json
{}
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/groups"

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

url = URI("https://api.elevenlabs.io/v1/workspace/groups")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/groups")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/groups');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/groups");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/groups")! as URL,
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
