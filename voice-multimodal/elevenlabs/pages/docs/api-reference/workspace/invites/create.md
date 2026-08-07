---
title: "Invite user"
source: https://elevenlabs.io/docs/api-reference/workspace/invites/create.md
path: docs/api-reference/workspace/invites/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Invite user

POST https://api.elevenlabs.io/v1/workspace/invites/add
Content-Type: application/json

Sends an email invitation to join your workspace to the provided email. If the user doesn't have an account they will be prompted to create one. If the user accepts this invite they will be added as a user to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission. If the user is already in the workspace a 400 error will be returned.

Reference: https://elevenlabs.io/docs/api-reference/workspace/invites/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `email` (string, required) — The email of the customer
- `seat_type` (enum, optional, nullable) — The seat type of the user
  - Allowed values: `workspace_admin`, `workspace_member`, `workspace_lite_member`
- `group_ids` (list of string, optional, nullable) — The group ids of the user
- `usage_limit` (integer, optional, nullable) — Monthly credit usage limit for the invitee. Omit or set to null for no custom cap.
- `workspace_permission` (string, optional, nullable, deprecated) — The workspace permission of the user. This is deprecated, use `seat_type` instead.

## Response

### 200

Successful Response

- `status` (string, required) — The status of the workspace invite request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

## Examples

**Request**

```json
{
  "email": "john.doe@testmail.com"
}
```

**Response**

```json
{
  "status": "ok"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.workspace.invites.create({
        email: "john.doe@testmail.com",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.invites.create(
    email="john.doe@testmail.com",
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

	url := "https://api.elevenlabs.io/v1/workspace/invites/add"

	payload := strings.NewReader("{\n  \"email\": \"john.doe@testmail.com\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/workspace/invites/add")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"john.doe@testmail.com\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/invites/add")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"john.doe@testmail.com\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/invites/add', [
  'body' => '{
  "email": "john.doe@testmail.com"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/invites/add");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"john.doe@testmail.com\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["email": "john.doe@testmail.com"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/invites/add")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
