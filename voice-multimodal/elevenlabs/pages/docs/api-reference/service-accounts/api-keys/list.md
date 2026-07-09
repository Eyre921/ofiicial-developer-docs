---
title: "Get API keys"
source: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/list.md
path: docs/api-reference/service-accounts/api-keys/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get API keys

GET https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys

Get all API keys for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/service-accounts/{service_account_user_id}/api-keys:
    get:
      operationId: list
      summary: Get API keys
      description: Get all API keys for a service account
      tags:
        - apiKeys
      parameters:
        - name: service_account_user_id
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
                $ref: '#/components/schemas/WorkspaceApiKeyListResponseModel'
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
    WorkspaceApiKeyListResponseModel:
      type: object
      properties:
        api-keys:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceApiKeyResponseModel'
      required:
        - api-keys
      title: WorkspaceApiKeyListResponseModel
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



**Response**

```json
{
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
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.serviceAccounts.apiKeys.list("service_account_user_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.api_keys.list(
    service_account_user_id="service_account_user_id",
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys"

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")! as URL,
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
