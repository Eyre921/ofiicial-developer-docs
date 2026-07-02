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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}:
    patch:
      operationId: update
      summary: Update API key
      description: Update an existing API key for a service account
      tags:
        - subpackage_serviceAccounts/apiKeys
      parameters:
        - name: service_account_user_id
          in: path
          required: true
          schema:
            type: string
        - name: api_key_id
          in: path
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
                #/components/schemas/Body_edit_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys__api_key_id__patch
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
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled:
      oneOf:
        - type: boolean
        - type: string
          enum:
            - no_update
      description: Whether to enable or disable the API key.
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
    PermissionType:
      type: string
      enum:
        - text_to_speech
        - speech_to_speech
        - speech_to_text
        - models_read
        - models_write
        - voices_read
        - voices_write
        - speech_history_read
        - speech_history_write
        - sound_generation
        - audio_isolation
        - voice_generation
        - dubbing_read
        - dubbing_write
        - pronunciation_dictionaries_read
        - pronunciation_dictionaries_write
        - user_read
        - user_write
        - projects_read
        - projects_write
        - audio_native_read
        - audio_native_write
        - workspace_read
        - workspace_write
        - forced_alignment
        - convai_read
        - convai_write
        - music_generation
        - image_video_generation
        - add_voice_from_voice_library
        - create_instant_voice_clone
        - create_professional_voice_clone
        - publish_voice_to_voice_library
        - share_voice_externally
        - create_user_api_key
        - workspace_analytics_full_read
        - webhooks_write
        - service_account_write
        - group_members_manage
        - workspace_members_read
        - workspace_members_invite
        - workspace_members_remove
        - terms_of_service_accept
        - audit_log_read
        - conversation_privacy_manage
        - copy_resources_cross_workspace
        - synthid_detector
      title: PermissionType
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions0:
      type: array
      items:
        $ref: '#/components/schemas/PermissionType'
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions0
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions1:
      type: string
      enum:
        - all
        - no_update
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions1
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions:
      oneOf:
        - $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions0
        - $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions1
      description: The permissions of the XI API.
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit:
      oneOf:
        - type: integer
        - type: string
          enum:
            - no_update
      description: >-
        The character limit of the XI API key. If provided this will limit the
        usage of this api key to n characters per month where n is the chosen
        value. Requests that incur charges will fail after reaching this monthly
        limit.
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps1:
      type: string
      enum:
        - clear
        - no_update
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps1
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps:
      oneOf:
        - type: array
          items:
            type: string
        - $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps1
      description: >-
        List of IP addresses or CIDR ranges allowed to use this API key. Each
        entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address
        (normalized to /32 or /128). On create, omit or pass null to allow all
        IPs. On update, omit to leave the allowlist unchanged, or pass "clear"
        to remove it.
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed1:
      type: string
      enum:
        - clear
        - no_update
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed1
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed:
      oneOf:
        - type: boolean
        - $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed1
      description: >-
        Whether the holder of this key may disable it via the self-disable
        endpoint. On create, omit or pass null to use the workspace's default
        (enabled for non-Enterprise plans, disabled for Enterprise plans). On
        update, omit to leave it unchanged, or pass "clear" to reset it to the
        workspace default. Only honored for workspaces with self-disable access
        enabled.
      title: >-
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed
    Body_edit_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys__api_key_id__patch:
      type: object
      properties:
        is_enabled:
          $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
          default: no_update
          description: Whether to enable or disable the API key.
        name:
          type:
            - string
            - 'null'
          description: >-
            The name of the XI API key to use (used for identification purposes
            only).
        permissions:
          $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
          default: no_update
          description: The permissions of the XI API.
        character_limit:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit
            - type: 'null'
          default: no_update
          description: >-
            The character limit of the XI API key. If provided this will limit
            the usage of this api key to n characters per month where n is the
            chosen value. Requests that incur charges will fail after reaching
            this monthly limit.
        allowed_ips:
          $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
          default: no_update
          description: >-
            List of IP addresses or CIDR ranges allowed to use this API key.
            Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP
            address (normalized to /32 or /128). On create, omit or pass null to
            allow all IPs. On update, omit to leave the allowlist unchanged, or
            pass "clear" to remove it.
        third_party_disable_allowed:
          $ref: >-
            #/components/schemas/BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisableAllowed
          default: no_update
          description: >-
            Whether the holder of this key may disable it via the self-disable
            endpoint. On create, omit or pass null to use the workspace's
            default (enabled for non-Enterprise plans, disabled for Enterprise
            plans). On update, omit to leave it unchanged, or pass "clear" to
            reset it to the workspace default. Only honored for workspaces with
            self-disable access enabled.
      title: >-
        Body_edit_service_account_api_key_v1_service_accounts__service_account_user_id__api_keys__api_key_id__patch
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
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.serviceAccounts.apiKeys.update("api_key_id", "service_account_user_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.api_keys.update(
    api_key_id="api_key_id",
    service_account_user_id="service_account_user_id",
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
