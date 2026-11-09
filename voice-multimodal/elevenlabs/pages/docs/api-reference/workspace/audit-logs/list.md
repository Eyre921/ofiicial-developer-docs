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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `limit` (integer, optional, default: 50) — Maximum number of entries per page
- `cursor` (string, optional, nullable) — Cursor for the next page (from previous response)
- `time_from_unix_ms` (integer, optional, nullable) — Only include entries at or after this time (ms since epoch)
- `time_to_unix_ms` (integer, optional, nullable) — Only include entries at or before this time (ms since epoch)
- `actor_uid` (string, optional, nullable) — Filter by actor user ID
- `class_name` (enum, optional, nullable) — Filter by OCSF event class name
  - Allowed values: `Account Change`, `Authentication`, `Entity Management`, `User Access Management`, `Group Management`
- `activity_name` (enum, optional, nullable) — Filter by audit activity name
  - Allowed values: `Account Security Change`, `Agents User Memory Entity Deleted`, `Agents User Memory Erased`, `Agents User Memory Exported`, `Agents User Memory Fact Deleted`, `Agents User Memory Viewed`, `Agents User Properties Reordered`, `Agents User Property Archived`, `Agents User Property Created`, `Agents User Property Unarchived`, `Agents User Property Updated`, `API Key Creation`, `API Key Deletion`, `API Key Management`, `API Key Update`, `Architect Member Spend Limits Update`, `Auth Connection Creation`, `Auth Connection Deletion`, `Auth Connection Management`, `Auth Connection Update`, `Billing Management`, `Child Workspace Resource Override`, `Content Generation Terms Update`, `Create workspace custom role`, `Custom Auth Token Created`, `Data Export Request`, `Delete Scribe meeting`, `Delete workspace custom role`, `Domain Verification Addition`, `Domain Verification Management`, `Domain Verification Removal`, `Domain Verification Status Update`, `Encryption Key Deleted`, `Encryption Key Paused`, `Encryption Key Registered`, `Encryption Key Unpaused`, `Enterprise Copying Toggle`, `Gift Credit Code Applied`, `Group Creation`, `Group Deletion`, `Group Management`, `Group Member Addition`, `Group Member Removal`, `Group to Billing Group Conversion`, `Group Update`, `Identity Provider Update`, `Influencer Code Applied`, `In-App Term Acceptance`, `Logon`, `MFA Factor Enrollment`, `MFA Factor Enrollment Reverted (unverified)`, `MFA Factor Removal`, `MFA Removal via Backup Code`, `Model Approvals Update`, `Notification Preference Creation`, `Notification Preference Deletion`, `Notification Preference Management`, `Notification Preference Update`, `Password Reset Email Request`, `Password Reset Link Generation`, `Reporting Workspace SSO Inheritance Update`, `Resource Access Granted`, `Resource Access Management`, `Resource Access Revoked`, `Resource Copied to Workspace`, `Resource Locator Creation`, `Resource Locator Deletion`, `Resource Locator Management`, `Resource Locator Update`, `Resource Ownership Transferred`, `SCIM Group Creation`, `SCIM Group Deletion`, `SCIM Group Management`, `SCIM Group Update`, `SCIM Provisioning Seat Type Updated`, `SCIM Token Deleted`, `SCIM Token Generated`, `SCIM Token Management`, `SCIM Token Rotated`, `SCIM User Creation`, `SCIM User Deletion`, `SCIM User Management`, `SCIM User Update`, `Sensitive Action Verification`, `Service Account Creation`, `Service Account Deletion`, `Service Account Management`, `Service Account Update`, `Shared SSO Sibling Workspaces Update`, `Sign-In Request Approval`, `Sign-In Request Decline`, `SMB Free Trial Activation`, `SMB Reseller Subscription Lifecycle`, `SMB Reseller Tier Assignment`, `SMB Reseller Tier Change`, `SSO Management`, `SSO Provider Configuration`, `SSO Provider Removal`, `Update workspace custom role`, `User API Key Creation`, `User API Key Deletion`, `User API Key Management`, `User API Key Update`, `User Auto-Provisioning Disabled`, `User Auto-Provisioning Enabled`, `User Creation`, `User Metadata Update`, `User Self-Deletion`, `User Sharing Preferences Update`, `User Sharing Preferences Update (Admin)`, `Webhook Creation`, `Webhook Deletion`, `Webhook Management`, `Webhook Update`, `Workspace Creation`, `Workspace Deletion`, `Workspace Deletion Cancellation`, `Workspace Invitation Accepted`, `Workspace Invitation Declined`, `Workspace Invitation Management`, `Workspace Invitation Reminder Sent`, `Workspace Invitation Revoked`, `Workspace Invitation Sent`, `Workspace Member Removal`, `Workspace Member Resource Transfer`, `Workspace Member Update`, `Workspace Member Usage Limit Update`, `Workspace Metadata Update`, `Workspace Ownership Transfer`, `Workspace Sign-In`

## Response

### 200

Successful Response

- `entries` (list of WorkspaceAuditLogEntryResponse, required)
- `has_more` (boolean, required)
- `next_cursor` (string, required, nullable)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### WorkspaceAuditLogEntryResponse

Audit log entry with Firestore document ID for API responses.

- `activity_id` (WorkspaceAuditLogEntryResponseActivityId, required) — Activity ID
- `activity_name` (string, required) — Activity name
- `status_id` (enum, required) — Status of the action
  - Allowed values: `0`, `1`, `2`, `99`
- `actor` (ActorModel, required) — Actor performing the action
- `message` (string, required) — Human-readable event description
- `id` (string, required) — Firestore document ID
- `time_dt` (string, required) — Event time in human-readable RFC 3339 format, derived from 'time'.
- `type_uid` (integer, required) — OCSF type_uid is class_uid * 100 + activity_id.
- `type_name` (string, required) — OCSF type_name combines class_name and activity_name.
- `metadata` (map from string to any, optional) — Event metadata
- `time` (integer, optional) — Event time in milliseconds since epoch
- `category_name` (string, optional, default: Identity & Access Management) — Event category
- `category_uid` (integer, optional, default: 3) — Category UID for IAM
- `class_name` (string, optional, default: ) — Event class name
- `class_uid` (integer, optional, default: 0) — Event class UID
- `severity_id` (enum, optional) — Severity level
  - Allowed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `99`
- `device` (DeviceModel, optional, nullable) — Device information
- `http_request` (HttpRequestModel, optional, nullable) — HTTP request details
- `unmapped` (map from string to any, optional) — Attributes not mapped to OCSF

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### WorkspaceAuditLogEntryResponseActivityId

Activity ID

- AccountChangeActivityId: enum
  - Allowed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `99`
- AuthenticationActivityId: enum
  - Allowed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `99`
- EntityManagementActivityId: enum
  - Allowed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `99`
- UserAccessManagementActivityId: enum
  - Allowed values: `0`, `1`, `2`, `99`
- GroupManagementActivityId: enum
  - Allowed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `99`

### ActorModel

OCSF Actor object - describes the entity that performed the action. Spec: https://schema.ocsf.io/1.6.0/objects/actor

- `user` (UserModel, required) — User who performed the action
- `app_name` (string, optional, nullable) — Client application or service name
- `app_uid` (string, optional, nullable) — Client application unique identifier
- `session` (map from string to any, optional, nullable) — Session information

### DeviceModel

Device information. Spec: https://schema.ocsf.io/1.6.0/objects/device

- `ip` (string, optional, nullable) — IP address
- `hostname` (string, optional, nullable) — Device hostname
- `type_id` (integer, optional, default: 99) — Device type ID (99 = Unknown)

### HttpRequestModel

HTTP request details. Spec: https://schema.ocsf.io/1.6.0/objects/http_request

- `http_method` (string, required) — HTTP method (GET, POST, etc.)
- `url` (UrlModel, required) — Request URL object
- `user_agent` (string, optional, nullable) — User agent string
- `x_forwarded_for` (list of string, optional, nullable) — X-Forwarded-For header as a list

### ValidationErrorLocItems

- string
- integer

### UserModel

OCSF User object. Spec: https://schema.ocsf.io/1.6.0/objects/user

- `name` (string, optional, nullable) — Username
- `uid` (string, optional, nullable) — Unique user identifier
- `type_id` (enum, optional) — Account type identifier
  - Allowed values: `0`, `1`, `2`, `3`, `4`, `99`
- `type` (string, optional, nullable) — Account type description
- `email_addr` (string, optional, nullable) — User email address
- `full_name` (string, optional, nullable) — Full name of the user
- `domain` (string, optional, nullable) — User's domain

### UrlModel

OCSF URL object. Spec: https://schema.ocsf.io/1.6.0/objects/url

- `url_string` (string, optional, nullable) — Full URL string
- `scheme` (string, optional, nullable) — URL scheme (e.g., https)
- `hostname` (string, optional, nullable) — URL hostname
- `port` (integer, optional, nullable) — URL port
- `path` (string, optional, nullable) — URL path
- `query_string` (string, optional, nullable) — URL query string

## Examples

**Response**

```json
{
  "entries": [
    {
      "activity_id": 0,
      "activity_name": "string",
      "status_id": 0,
      "actor": {
        "user": {
          "name": "string",
          "uid": "string",
          "type_id": 0,
          "type": "string",
          "email_addr": "string",
          "full_name": "string",
          "domain": "string"
        },
        "app_name": "string",
        "app_uid": "string",
        "session": {}
      },
      "message": "string",
      "id": "string",
      "time_dt": "string",
      "type_uid": 1,
      "type_name": "string",
      "metadata": {},
      "time": 1,
      "category_name": "Identity & Access Management",
      "category_uid": 3,
      "class_name": "",
      "class_uid": 0,
      "severity_id": 0,
      "device": {
        "ip": "string",
        "hostname": "string",
        "type_id": 99
      },
      "http_request": {
        "http_method": "string",
        "url": {
          "url_string": "string",
          "scheme": "string",
          "hostname": "string",
          "port": 1,
          "path": "string",
          "query_string": "string"
        },
        "user_agent": "string",
        "x_forwarded_for": [
          "string"
        ]
      },
      "unmapped": {}
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/workspace/audit-logs"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/workspace/audit-logs';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/audit-logs"

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

url = URI("https://api.elevenlabs.io/v1/workspace/audit-logs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/audit-logs")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/audit-logs');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/audit-logs");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/audit-logs")! as URL,
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
