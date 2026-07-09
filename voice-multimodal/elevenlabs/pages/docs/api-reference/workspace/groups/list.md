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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/groups:
    get:
      operationId: list
      summary: List workspace groups
      description: Get all groups in the workspace
      tags:
        - groups
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
                type: object
                additionalProperties:
                  $ref: '#/components/schemas/WorkspaceGroupResponseModel'
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
