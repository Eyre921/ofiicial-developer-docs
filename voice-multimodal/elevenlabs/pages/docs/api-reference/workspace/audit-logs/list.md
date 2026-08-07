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
- `class_name` (string, optional, nullable) — Filter by OCSF event class name (e.g. Account Change)
- `activity_name` (string, optional, nullable) — Filter by audit activity name (e.g. Subscription Creation)

## Response

### 200

Successful Response

- `entries` (list of object, required)
  - `activity_id` (enum or enum or enum or enum or enum, required) — Activity ID
  - `activity_name` (string, required) — Activity name
  - `status_id` (enum, required) — Status of the action
    - Allowed values: `0`, `1`, `2`, `99`
  - `actor` (object, required) — Actor performing the action
    - `user` (object, required) — User who performed the action
      - `name` (string, optional, nullable) — Username
      - `uid` (string, optional, nullable) — Unique user identifier
      - `type_id` (enum, optional) — Account type identifier
        - Allowed values: `0`, `1`, `2`, `3`, `4`, `99`
      - `type` (string, optional, nullable) — Account type description
      - `email_addr` (string, optional, nullable) — User email address
      - `full_name` (string, optional, nullable) — Full name of the user
      - `domain` (string, optional, nullable) — User's domain
    - `app_name` (string, optional, nullable) — Client application or service name
    - `app_uid` (string, optional, nullable) — Client application unique identifier
    - `session` (map from string to any, optional, nullable) — Session information
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
  - `device` (object, optional, nullable) — Device information
    - `ip` (string, optional, nullable) — IP address
    - `hostname` (string, optional, nullable) — Device hostname
    - `type_id` (integer, optional, default: 99) — Device type ID (99 = Unknown)
  - `http_request` (object, optional, nullable) — HTTP request details
    - `http_method` (string, required) — HTTP method (GET, POST, etc.)
    - `url` (object, required) — Request URL object
      - `url_string` (string, optional, nullable) — Full URL string
      - `scheme` (string, optional, nullable) — URL scheme (e.g., https)
      - `hostname` (string, optional, nullable) — URL hostname
      - `port` (integer, optional, nullable) — URL port
      - `path` (string, optional, nullable) — URL path
      - `query_string` (string, optional, nullable) — URL query string
    - `user_agent` (string, optional, nullable) — User agent string
    - `x_forwarded_for` (list of string, optional, nullable) — X-Forwarded-For header as a list
  - `unmapped` (map from string to any, optional) — Attributes not mapped to OCSF
- `has_more` (boolean, required)
- `next_cursor` (string, required, nullable)

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
