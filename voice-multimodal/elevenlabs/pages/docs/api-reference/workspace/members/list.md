---
title: "Get Workspace Members"
source: https://elevenlabs.io/docs/api-reference/workspace/members/list.md
path: docs/api-reference/workspace/members/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Workspace Members

GET https://api.elevenlabs.io/v1/workspace/members

Gets a list of all members of the workspace, including locked members. Service accounts are excluded. Requires the workspace_members_read permission.

Reference: https://elevenlabs.io/docs/api-reference/workspace/members/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/members:
    get:
      operationId: list
      summary: Get Workspace Members
      description: >-
        Gets a list of all members of the workspace, including locked members.
        Service accounts are excluded. Requires the workspace_members_read
        permission.
      tags:
        - members
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
                type: array
                items:
                  $ref: '#/components/schemas/WorkspaceMemberResponseModel'
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
    SeatType:
      type: string
      enum:
        - workspace_admin
        - workspace_member
        - workspace_lite_member
      description: Seat types for workspace members.
      title: SeatType
    WorkspaceMemberResponseModel:
      type: object
      properties:
        user_id:
          type: string
          description: The user ID of the workspace member.
        email:
          type: string
          description: The email address of the workspace member.
        first_name:
          type:
            - string
            - 'null'
          description: The first name of the workspace member, if available.
        seat_type:
          oneOf:
            - $ref: '#/components/schemas/SeatType'
            - type: 'null'
          description: The seat type (role) of the workspace member.
        is_owner:
          type: boolean
          description: Whether the member is the workspace owner.
        is_locked:
          type: boolean
          description: Whether the member's account is locked in this workspace.
      required:
        - user_id
        - email
        - first_name
        - seat_type
        - is_owner
        - is_locked
      description: Public workspace member fields exposed via GET /v1/workspace/members.
      title: WorkspaceMemberResponseModel
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
[
  {
    "user_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890",
    "email": "jane.doe@example.com",
    "first_name": "Jane",
    "seat_type": "workspace_admin",
    "is_owner": true,
    "is_locked": false
  },
  {
    "user_id": "f9e8d7c6-b5a4-3210-9876-5432fedcba10",
    "email": "john.smith@example.com",
    "first_name": "John",
    "seat_type": "workspace_member",
    "is_owner": false,
    "is_locked": false
  },
  {
    "user_id": "123e4567-e89b-12d3-a456-426614174000",
    "email": "alice.williams@example.com",
    "first_name": "Alice",
    "seat_type": "workspace_lite_member",
    "is_owner": false,
    "is_locked": true
  }
]
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.members.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.members.list()

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

	url := "https://api.elevenlabs.io/v1/workspace/members"

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

url = URI("https://api.elevenlabs.io/v1/workspace/members")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/members")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/members', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/members");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/members")! as URL,
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
