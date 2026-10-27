---
title: "Update API key"
source: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update.md
path: docs/api-reference/service-accounts/api-keys/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update API key

PATCH https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}
Content-Type: application/json

Update an existing API key for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `service_account_user_id` (string, required)
- `api_key_id` (string, required)

### Body (application/json)

This endpoint expects a Body_edit_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys__api_key_id__patch.

- `is_enabled` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled, optional, default: no_update) — Whether to enable or disable the API key.
- `name` (string, optional, nullable) — The name of the XI API key to use (used for identification purposes only).
- `permissions` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions, optional, default: no_update) — The permissions of the XI API.
- `character_limit` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit, optional, nullable, default: no_update) — The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.
- `allowed_ips` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps, optional, default: no_update) — List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.
- `third_party_disable_allowed` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed, optional, default: no_update) — Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.
- `tts_concurrency_limit` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchTtsConcurrencyLimit, optional, nullable, default: no_update) — Maximum concurrent text-to-speech/speech-to-speech requests for this API key. Only available for enterprise customers.
- `dubbing_concurrency_limit` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchDubbingConcurrencyLimit, optional, nullable, default: no_update) — Maximum concurrent dubbing requests for this API key. Only available for enterprise customers.
- `music_concurrency_limit` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchMusicConcurrencyLimit, optional, nullable, default: no_update) — Maximum concurrent music generation requests for this API key. Only available for enterprise customers.
- `expires_at_unix` (BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchExpiresAtUnix, optional, default: no_update) — Unix timestamp (in seconds) after which this API key stops working. When set, it must be at least 15 minutes and at most 90 days in the future. On create, omit or pass null for a key that never expires. On update, omit to leave it unchanged, or pass "clear" to remove the expiry (never expires).

## Response

### 200

Successful Response

- `any`

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled

Whether to enable or disable the API key.

- boolean
- "no_update"

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions

The permissions of the XI API.

- list of enum
  - Allowed values: `text_to_speech`, `speech_to_speech`, `speech_to_text`, `models_read`, `models_write`, `voices_read`, `voices_write`, `voice_collections_read`, `voice_collections_write`, `speech_history_read`, `speech_history_write`, `sound_generation`, `audio_isolation`, `voice_generation`, `dubbing_read`, `dubbing_write`, `pronunciation_dictionaries_read`, `pronunciation_dictionaries_write`, `user_read`, `user_write`, `projects_read`, `projects_write`, `audio_native_read`, `audio_native_write`, `workspace_read`, `workspace_write`, `forced_alignment`, `convai_read`, `convai_write`, `music_generation`, `image_video_generation`, `flows`, `templates`, `add_voice_from_voice_library`, `create_instant_voice_clone`, `create_professional_voice_clone`, `publish_voice_to_voice_library`, `share_voice_externally`, `create_user_api_key`, `workspace_analytics_full_read`, `webhooks_write`, `service_account_write`, `group_members_manage`, `workspace_members_read`, `workspace_members_invite`, `workspace_members_remove`, `terms_of_service_accept`, `audit_log_read`, `conversation_privacy_manage`, `copy_resources_cross_workspace`, `synthid_detector`
- enum
  - Allowed values: `all`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit

The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.

- integer
- enum
  - Allowed values: `clear`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps

List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.

- list of string
- enum
  - Allowed values: `clear`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed

Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.

- boolean
- enum
  - Allowed values: `clear`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchTtsConcurrencyLimit

Maximum concurrent text-to-speech/speech-to-speech requests for this API key. Only available for enterprise customers.

- integer
- enum
  - Allowed values: `clear`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchDubbingConcurrencyLimit

Maximum concurrent dubbing requests for this API key. Only available for enterprise customers.

- integer
- enum
  - Allowed values: `clear`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchMusicConcurrencyLimit

Maximum concurrent music generation requests for this API key. Only available for enterprise customers.

- integer
- enum
  - Allowed values: `clear`, `no_update`

### BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchExpiresAtUnix

Unix timestamp (in seconds) after which this API key stops working. When set, it must be at least 15 minutes and at most 90 days in the future. On create, omit or pass null for a key that never expires. On update, omit to leave it unchanged, or pass "clear" to remove the expiry (never expires).

- integer
- enum
  - Allowed values: `clear`, `no_update`

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

- string
- integer

## Examples

**Request**

```json
{}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id';
const options = {method: 'PATCH', headers: {'Content-Type': 'application/json'}, body: '{}'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys/api_key_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
