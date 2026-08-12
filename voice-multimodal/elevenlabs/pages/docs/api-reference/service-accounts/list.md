---
title: "Get service accounts"
source: https://elevenlabs.io/docs/api-reference/service-accounts/list.md
path: docs/api-reference/service-accounts/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get service accounts

GET https://api.elevenlabs.io/v1/service-accounts

List all service accounts in the workspace

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `service-accounts` (list of object, required)
  - `service_account_user_id` (string, required)
  - `name` (string, required)
  - `api-keys` (list of object, required)
    - `name` (string, required)
    - `hint` (string, required)
    - `key_id` (string, required)
    - `service_account_user_id` (string, required)
    - `hashed_xi_api_key` (string, required)
    - `created_at_unix` (integer, optional, nullable)
    - `is_disabled` (boolean, optional, default: false)
    - `permissions` (list of enum, optional, nullable)
      - Allowed values: `text_to_speech`, `speech_to_speech`, `speech_to_text`, `models_read`, `models_write`, `voices_read`, `voices_write`, `speech_history_read`, `speech_history_write`, `sound_generation`, `audio_isolation`, `voice_generation`, `dubbing_read`, `dubbing_write`, `pronunciation_dictionaries_read`, `pronunciation_dictionaries_write`, `user_read`, `user_write`, `projects_read`, `projects_write`, `audio_native_read`, `audio_native_write`, `workspace_read`, `workspace_write`, `forced_alignment`, `convai_read`, `convai_write`, `music_generation`, `image_video_generation`, `flows`, `templates`, `add_voice_from_voice_library`, `create_instant_voice_clone`, `create_professional_voice_clone`, `publish_voice_to_voice_library`, `share_voice_externally`, `create_user_api_key`, `workspace_analytics_full_read`, `webhooks_write`, `service_account_write`, `group_members_manage`, `workspace_members_read`, `workspace_members_invite`, `workspace_members_remove`, `terms_of_service_accept`, `audit_log_read`, `conversation_privacy_manage`, `copy_resources_cross_workspace`, `synthid_detector`
    - `disable_reason` (enum, optional, nullable)
      - Allowed values: `trial_ended`, `subscription_downgrade`, `exposed_publicly`, `self_disabled`
    - `character_limit` (integer, optional, nullable) — Maximum number of credits allowed in the current billing period.
    - `character_count` (integer, optional, nullable) — Credits already used in the current billing period.
    - `allowed_ips` (list of string, optional, nullable)
    - `third_party_disable_allowed` (boolean, optional, nullable)
  - `created_at_unix` (integer, optional, nullable)
  - `default_sharing_groups` (list of object, optional, default: [])
    - `group` (object, required) — The group to share with by default
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
    - `permission_level` (enum, required) — The permission level to grant to the group
      - Allowed values: `admin`, `editor`, `viewer`

## Examples

**Response**

```json
{
  "service-accounts": [
    {
      "service_account_user_id": "string",
      "name": "string",
      "api-keys": [
        {
          "name": "string",
          "hint": "string",
          "key_id": "string",
          "service_account_user_id": "string",
          "hashed_xi_api_key": "string",
          "created_at_unix": 1,
          "is_disabled": false,
          "permissions": [
            "text_to_speech"
          ],
          "disable_reason": "trial_ended",
          "character_limit": 1,
          "character_count": 1,
          "allowed_ips": [
            "string"
          ],
          "third_party_disable_allowed": true
        }
      ],
      "created_at_unix": 1,
      "default_sharing_groups": [
        {
          "group": {
            "name": "string",
            "id": "string",
            "members": [
              "string"
            ],
            "permissions": [
              "text_to_speech"
            ],
            "group_usage_limit": 1,
            "group_pvc_limit": 1,
            "character_count": 1,
            "is_scim_synced": false,
            "scim_group": {
              "scim_external_id": "string",
              "display_name": "string",
              "created_at_unix": 1,
              "updated_at_unix": 1,
              "seat_type": "workspace_admin"
            },
            "scim_frozen": false
          },
          "permission_level": "admin"
        }
      ]
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.serviceAccounts.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/service-accounts"

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

url = URI("https://api.elevenlabs.io/v1/service-accounts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/service-accounts")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/service-accounts');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts")! as URL,
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
