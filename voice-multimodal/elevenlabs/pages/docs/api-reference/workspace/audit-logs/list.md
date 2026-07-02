---
title: "List audit logs"
source: https://elevenlabs.io/docs/api-reference/workspace/audit-logs/list.md
path: docs/api-reference/workspace/audit-logs/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List audit logs

GET https://api.elevenlabs.io/v1/workspace/audit-logs

Returns the audit log for the workspace. Requires enterprise tier and the audit_log_read permission.

Reference: https://elevenlabs.io/docs/api-reference/workspace/audit-logs/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/audit-logs:
    get:
      operationId: list
      summary: Get Workspace Audit Logs
      description: >-
        Returns the audit log for the workspace. Requires enterprise tier and
        the audit_log_read permission.
      tags:
        - subpackage_workspace/auditLogs
      parameters:
        - name: limit
          in: query
          description: Maximum number of entries per page
          required: false
          schema:
            type: integer
            default: 50
        - name: cursor
          in: query
          description: Cursor for the next page (from previous response)
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: time_from_unix_ms
          in: query
          description: Only include entries at or after this time (ms since epoch)
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: time_to_unix_ms
          in: query
          description: Only include entries at or before this time (ms since epoch)
          required: false
          schema:
            type:
              - integer
              - 'null'
        - name: actor_uid
          in: query
          description: Filter by actor user ID
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: class_name
          in: query
          description: Filter by OCSF event class name (e.g. Account Change)
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: activity_name
          in: query
          description: Filter by audit activity name (e.g. Subscription Creation)
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/WorkspaceAuditLogsPageResponse'
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
    AccountChangeActivityId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
        - '5'
        - '6'
        - '7'
        - '8'
        - '9'
        - '10'
        - '11'
        - '12'
        - '99'
      description: |-
        OCSF Activity IDs for Account Change [3001] events.

        Spec: https://schema.ocsf.io/1.6.0/classes/account_change
      title: AccountChangeActivityId
    AuthenticationActivityId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
        - '5'
        - '6'
        - '7'
        - '99'
      description: |-
        OCSF Activity IDs for Authentication [3002] events.

        Spec: https://schema.ocsf.io/1.6.0/classes/authentication
      title: AuthenticationActivityId
    EntityManagementActivityId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
        - '5'
        - '6'
        - '7'
        - '8'
        - '9'
        - '10'
        - '11'
        - '12'
        - '13'
        - '99'
      description: |-
        OCSF Activity IDs for Entity Management [3004] events.

        Spec: https://schema.ocsf.io/1.6.0/classes/entity_management
      title: EntityManagementActivityId
    UserAccessManagementActivityId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '99'
      description: |-
        OCSF Activity IDs for User Access Management [3005] events.

        Spec: https://schema.ocsf.io/1.6.0/classes/user_access_management
      title: UserAccessManagementActivityId
    GroupManagementActivityId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
        - '5'
        - '6'
        - '7'
        - '8'
        - '9'
        - '99'
      description: |-
        OCSF Activity IDs for Group Management [3006] events.

        Spec: https://schema.ocsf.io/1.6.0/classes/group_management
      title: GroupManagementActivityId
    WorkspaceAuditLogEntryResponseActivityId:
      oneOf:
        - $ref: '#/components/schemas/AccountChangeActivityId'
        - $ref: '#/components/schemas/AuthenticationActivityId'
        - $ref: '#/components/schemas/EntityManagementActivityId'
        - $ref: '#/components/schemas/UserAccessManagementActivityId'
        - $ref: '#/components/schemas/GroupManagementActivityId'
      description: Activity ID
      title: WorkspaceAuditLogEntryResponseActivityId
    SeverityId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
        - '5'
        - '6'
        - '99'
      description: |-
        OCSF Severity levels.

        Spec: https://schema.ocsf.io/1.6.0/objects/severity_id
      title: SeverityId
    StatusId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '99'
      description: |-
        OCSF Status levels.

        Spec: https://schema.ocsf.io/1.6.0/objects/status_id
      title: StatusId
    UserTypeId:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
        - '99'
      description: |-
        OCSF User type IDs.

        Spec: https://schema.ocsf.io/1.6.0/objects/user
      title: UserTypeId
    UserModel:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
          description: Username
        uid:
          type:
            - string
            - 'null'
          description: Unique user identifier
        type_id:
          $ref: '#/components/schemas/UserTypeId'
          description: Account type identifier
        type:
          type:
            - string
            - 'null'
          description: Account type description
        email_addr:
          type:
            - string
            - 'null'
          description: User email address
        full_name:
          type:
            - string
            - 'null'
          description: Full name of the user
        domain:
          type:
            - string
            - 'null'
          description: User's domain
      description: |-
        OCSF User object.

        Spec: https://schema.ocsf.io/1.6.0/objects/user
      title: UserModel
    ActorModel:
      type: object
      properties:
        user:
          $ref: '#/components/schemas/UserModel'
          description: User who performed the action
        app_name:
          type:
            - string
            - 'null'
          description: Client application or service name
        app_uid:
          type:
            - string
            - 'null'
          description: Client application unique identifier
        session:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: Session information
      required:
        - user
      description: |-
        OCSF Actor object - describes the entity that performed the action.

        Spec: https://schema.ocsf.io/1.6.0/objects/actor
      title: ActorModel
    DeviceModel:
      type: object
      properties:
        ip:
          type:
            - string
            - 'null'
          description: IP address
        hostname:
          type:
            - string
            - 'null'
          description: Device hostname
        type_id:
          type: integer
          default: 99
          description: Device type ID (99 = Unknown)
      description: |-
        Device information.

        Spec: https://schema.ocsf.io/1.6.0/objects/device
      title: DeviceModel
    UrlModel:
      type: object
      properties:
        url_string:
          type:
            - string
            - 'null'
          description: Full URL string
        scheme:
          type:
            - string
            - 'null'
          description: URL scheme (e.g., https)
        hostname:
          type:
            - string
            - 'null'
          description: URL hostname
        port:
          type:
            - integer
            - 'null'
          description: URL port
        path:
          type:
            - string
            - 'null'
          description: URL path
        query_string:
          type:
            - string
            - 'null'
          description: URL query string
      description: |-
        OCSF URL object.

        Spec: https://schema.ocsf.io/1.6.0/objects/url
      title: UrlModel
    HttpRequestModel:
      type: object
      properties:
        http_method:
          type: string
          description: HTTP method (GET, POST, etc.)
        url:
          $ref: '#/components/schemas/UrlModel'
          description: Request URL object
        user_agent:
          type:
            - string
            - 'null'
          description: User agent string
        x_forwarded_for:
          type:
            - array
            - 'null'
          items:
            type: string
          description: X-Forwarded-For header as a list
      required:
        - http_method
        - url
      description: |-
        HTTP request details.

        Spec: https://schema.ocsf.io/1.6.0/objects/http_request
      title: HttpRequestModel
    WorkspaceAuditLogEntryResponse:
      type: object
      properties:
        metadata:
          type: object
          additionalProperties:
            description: Any type
          description: Event metadata
        time:
          type: integer
          description: Event time in milliseconds since epoch
        activity_id:
          $ref: '#/components/schemas/WorkspaceAuditLogEntryResponseActivityId'
          description: Activity ID
        activity_name:
          type: string
          description: Activity name
        category_name:
          type: string
          default: Identity & Access Management
          description: Event category
        category_uid:
          type: integer
          default: 3
          description: Category UID for IAM
        class_name:
          type: string
          default: ''
          description: Event class name
        class_uid:
          type: integer
          default: 0
          description: Event class UID
        severity_id:
          $ref: '#/components/schemas/SeverityId'
          description: Severity level
        status_id:
          $ref: '#/components/schemas/StatusId'
          description: Status of the action
        actor:
          $ref: '#/components/schemas/ActorModel'
          description: Actor performing the action
        device:
          oneOf:
            - $ref: '#/components/schemas/DeviceModel'
            - type: 'null'
          description: Device information
        http_request:
          oneOf:
            - $ref: '#/components/schemas/HttpRequestModel'
            - type: 'null'
          description: HTTP request details
        message:
          type: string
          description: Human-readable event description
        unmapped:
          type: object
          additionalProperties:
            description: Any type
          description: Attributes not mapped to OCSF
        id:
          type: string
          description: Firestore document ID
        time_dt:
          type: string
          description: Event time in human-readable RFC 3339 format, derived from 'time'.
        type_uid:
          type: integer
          description: OCSF type_uid is class_uid * 100 + activity_id.
        type_name:
          type: string
          description: OCSF type_name combines class_name and activity_name.
      required:
        - activity_id
        - activity_name
        - status_id
        - actor
        - message
        - id
        - time_dt
        - type_uid
        - type_name
      description: Audit log entry with Firestore document ID for API responses.
      title: WorkspaceAuditLogEntryResponse
    WorkspaceAuditLogsPageResponse:
      type: object
      properties:
        entries:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceAuditLogEntryResponse'
        has_more:
          type: boolean
        next_cursor:
          type:
            - string
            - 'null'
      required:
        - entries
        - has_more
        - next_cursor
      description: Paginated workspace audit log response.
      title: WorkspaceAuditLogsPageResponse
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
  "entries": [
    {
      "activity_id": 1,
      "activity_name": "User Login",
      "status_id": 1,
      "actor": {
        "user": {
          "name": "jdoe",
          "uid": "user-1234",
          "type_id": 1,
          "type": "Standard User",
          "email_addr": "jdoe@example.com",
          "full_name": "John Doe",
          "domain": "example.com"
        },
        "app_name": "ElevenLabs Web Portal",
        "app_uid": "app-5678",
        "session": {
          "ip": "192.168.1.15",
          "session_id": "sess-7890"
        }
      },
      "message": "User jdoe successfully logged in.",
      "id": "auditlog-0001",
      "time_dt": "2023-06-15T12:00:00Z",
      "type_uid": 201,
      "type_name": "Authentication User Login",
      "metadata": {
        "ip_address": "192.168.1.15",
        "location": "New York, USA"
      },
      "time": 1686825600000,
      "category_name": "Identity & Access Management",
      "category_uid": 3,
      "class_name": "Authentication",
      "class_uid": 2,
      "severity_id": 1,
      "device": {
        "ip": "192.168.1.15",
        "hostname": "johns-laptop",
        "type_id": 3
      },
      "http_request": {
        "http_method": "POST",
        "url": {
          "url_string": "https://api.elevenlabs.io/v1/auth/login",
          "scheme": "https",
          "hostname": "api.elevenlabs.io",
          "port": 443,
          "path": "/v1/auth/login",
          "query_string": "redirect=/dashboard"
        },
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "x_forwarded_for": [
          "203.0.113.195"
        ]
      },
      "unmapped": {
        "custom_field": "custom_value"
      }
    }
  ],
  "has_more": true,
  "next_cursor": "cursor_abcdef123456"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.auditLogs.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.audit_logs.list()

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

	url := "https://api.elevenlabs.io/v1/workspace/audit-logs"

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

url = URI("https://api.elevenlabs.io/v1/workspace/audit-logs")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/audit-logs")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/audit-logs', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/audit-logs");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/audit-logs")! as URL,
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
