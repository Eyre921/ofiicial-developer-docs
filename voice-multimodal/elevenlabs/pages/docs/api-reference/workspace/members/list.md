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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `list of WorkspaceMemberResponseModel`

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### WorkspaceMemberResponseModel

Public workspace member fields exposed via GET /v1/workspace/members.

- `user_id` (string, required) — The user ID of the workspace member.
- `email` (string, required) — The email address of the workspace member.
- `first_name` (string, required, nullable) — The first name of the workspace member, if available.
- `seat_type` (enum, required, nullable) — The seat type (role) of the workspace member.
  - Allowed values: `workspace_admin`, `workspace_member`, `workspace_lite_member`
- `is_owner` (boolean, required) — Whether the member is the workspace owner.
- `is_locked` (boolean, required) — Whether the member's account is locked in this workspace.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

- string
- integer

## Examples

**Response**

```json
[
  {
    "user_id": "string",
    "email": "string",
    "first_name": "string",
    "seat_type": "workspace_admin",
    "is_owner": true,
    "is_locked": true
  }
]
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/workspace/members"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/workspace/members';
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

	url := "https://api.elevenlabs.io/v1/workspace/members"

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

url = URI("https://api.elevenlabs.io/v1/workspace/members")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/members")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/members');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/members");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/members")! as URL,
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
