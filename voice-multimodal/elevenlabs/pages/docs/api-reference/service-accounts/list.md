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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/service-accounts:
    get:
      operationId: list
      summary: Get service accounts
      description: List all service accounts in the workspace
      tags:
        - serviceAccounts
      parameters:
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
                $ref: '#/components/schemas/WorkspaceServiceAccountListResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
        - flows
        - templates
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
    LockReason:
      type: string
      enum:
        - trial_ended
        - subscription_downgrade
        - exposed_publicly
        - self_disabled
      title: LockReason
    WorkspaceApiKeyResponseModel:
      type: object
      properties:
        name:
          type: string
        hint:
          type: string
        key_id:
          type: string
        service_account_user_id:
          type: string
        created_at_unix:
          type:
            - integer
            - 'null'
        is_disabled:
          type: boolean
          default: false
        permissions:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/PermissionType'
        disable_reason:
          oneOf:
            - $ref: '#/components/schemas/LockReason'
            - type: 'null'
        character_limit:
          type:
            - integer
            - 'null'
          description: Maximum number of credits allowed in the current billing period.
        character_count:
          type:
            - integer
            - 'null'
          description: Credits already used in the current billing period.
        hashed_xi_api_key:
          type: string
        allowed_ips:
          type:
            - array
            - 'null'
          items:
            type: string
        third_party_disable_allowed:
          type:
            - boolean
            - 'null'
      required:
        - name
        - hint
        - key_id
        - service_account_user_id
        - hashed_xi_api_key
      title: WorkspaceApiKeyResponseModel
    WorkspaceGroupPermission:
      type: string
      enum:
        - text_to_speech
        - speech_to_speech
        - speech_to_text
        - voice_lab
        - sound_effects
        - projects
        - voiceover_studio
        - dubbing
        - audio_native
        - conversational_ai
        - conversational_ai_read
        - voice_isolator
        - ai_speech_classifier
        - synthid_detector
        - add_voice_from_voice_library
        - create_instant_voice_clone
        - create_professional_voice_clone
        - create_user_api_key
        - publish_studio_project
        - music
        - image_video_generation
        - flows
        - templates
        - share_voice_externally
        - publish_voice_to_voice_library
        - view_fiat_balance
        - workspace_analytics_full_read
        - service_accounts_manage
        - webhooks_manage
        - group_members_manage
        - workspace_members_invite
        - workspace_members_remove
        - terms_of_service_accept
        - audit_log_read
        - conversation_privacy_manage
        - copy_resources_cross_workspace
        - voice_design
      title: WorkspaceGroupPermission
    WorkspaceGroupResponseModelGroupUsageLimit:
      oneOf:
        - type: integer
        - type: string
          enum:
            - unlimited
      title: WorkspaceGroupResponseModelGroupUsageLimit
    WorkspaceGroupResponseModelGroupPvcLimit:
      oneOf:
        - type: integer
        - type: string
          enum:
            - unlimited
      title: WorkspaceGroupResponseModelGroupPvcLimit
    SeatType:
      type: string
      enum:
        - workspace_admin
        - workspace_member
        - workspace_lite_member
      description: Seat types for workspace members.
      title: SeatType
    ScimGroupResponseModel:
      type: object
      properties:
        scim_external_id:
          type:
            - string
            - 'null'
        display_name:
          type: string
        created_at_unix:
          type:
            - integer
            - 'null'
        updated_at_unix:
          type:
            - integer
            - 'null'
        seat_type:
          oneOf:
            - $ref: '#/components/schemas/SeatType'
            - type: 'null'
      required:
        - scim_external_id
        - display_name
      title: ScimGroupResponseModel
    WorkspaceGroupResponseModel:
      type: object
      properties:
        name:
          type: string
        id:
          type: string
        members:
          type: array
          items:
            type: string
        permissions:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/WorkspaceGroupPermission'
        group_usage_limit:
          oneOf:
            - $ref: '#/components/schemas/WorkspaceGroupResponseModelGroupUsageLimit'
            - type: 'null'
        group_pvc_limit:
          oneOf:
            - $ref: '#/components/schemas/WorkspaceGroupResponseModelGroupPvcLimit'
            - type: 'null'
        character_count:
          type:
            - integer
            - 'null'
        scim_external_id:
          type:
            - string
            - 'null'
        is_scim_synced:
          type: boolean
          default: false
        scim_group:
          oneOf:
            - $ref: '#/components/schemas/ScimGroupResponseModel'
            - type: 'null'
        scim_frozen:
          type: boolean
          default: false
      required:
        - name
        - id
        - members
        - permissions
      title: WorkspaceGroupResponseModel
    DefaultSharingGroupResponseModelPermissionLevel:
      type: string
      enum:
        - admin
        - editor
        - viewer
      description: The permission level to grant to the group
      title: DefaultSharingGroupResponseModelPermissionLevel
    DefaultSharingGroupResponseModel:
      type: object
      properties:
        group:
          $ref: '#/components/schemas/WorkspaceGroupResponseModel'
          description: The group to share with by default
        permission_level:
          $ref: '#/components/schemas/DefaultSharingGroupResponseModelPermissionLevel'
          description: The permission level to grant to the group
      required:
        - group
        - permission_level
      title: DefaultSharingGroupResponseModel
    WorkspaceServiceAccountResponseModel:
      type: object
      properties:
        service_account_user_id:
          type: string
        name:
          type: string
        created_at_unix:
          type:
            - integer
            - 'null'
        api-keys:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceApiKeyResponseModel'
        default_sharing_groups:
          type: array
          items:
            $ref: '#/components/schemas/DefaultSharingGroupResponseModel'
          default: []
      required:
        - service_account_user_id
        - name
        - api-keys
      title: WorkspaceServiceAccountResponseModel
    WorkspaceServiceAccountListResponseModel:
      type: object
      properties:
        service-accounts:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceServiceAccountResponseModel'
      required:
        - service-accounts
      title: WorkspaceServiceAccountListResponseModel
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

**Response**

```json
{
  "service-accounts": [
    {
      "service_account_user_id": "svcacc_9f8b7c6d5e4a3b2c1d0e",
      "name": "Audio Processing Service",
      "api-keys": [
        {
          "name": "Primary API Key",
          "hint": "Key for main audio processing",
          "key_id": "key_123abc456def789ghi",
          "service_account_user_id": "svcacc_9f8b7c6d5e4a3b2c1d0e",
          "hashed_xi_api_key": "a1b2c3d4e5f67890",
          "created_at_unix": 1688006400,
          "is_disabled": false,
          "permissions": [
            "text_to_speech",
            "voice_generation",
            "models_read"
          ],
          "disable_reason": null,
          "character_limit": 1000000,
          "character_count": 250000,
          "allowed_ips": [
            "192.168.1.100",
            "10.0.0.5"
          ],
          "third_party_disable_allowed": true
        }
      ],
      "created_at_unix": 1688006400,
      "default_sharing_groups": [
        {
          "group": {
            "name": "Audio Engineers",
            "id": "grp_456def789abc123ghi",
            "members": [
              "user_001",
              "user_002",
              "user_003"
            ],
            "permissions": [
              "text_to_speech",
              "voice_lab",
              "projects"
            ],
            "group_usage_limit": 5000000,
            "group_pvc_limit": 1000,
            "character_count": 1200000,
            "scim_external_id": "scim_group_789xyz",
            "is_scim_synced": true,
            "scim_group": {
              "scim_external_id": "scim_group_789xyz",
              "display_name": "Audio Engineers SCIM",
              "created_at_unix": 1672531200,
              "updated_at_unix": 1680393600,
              "seat_type": "workspace_member"
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/service-accounts"

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

url = URI("https://api.elevenlabs.io/v1/service-accounts")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/service-accounts")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/service-accounts', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts")! as URL,
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
