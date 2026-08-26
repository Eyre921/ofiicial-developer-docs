---
title: "Update member"
source: https://elevenlabs.io/docs/api-reference/workspace/members/update.md
path: docs/api-reference/workspace/members/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update member

POST https://api.elevenlabs.io/v1/workspace/members
Content-Type: application/json

Updates attributes of a workspace member. Apart from the email identifier, all parameters will remain unchanged unless specified. This endpoint may only be called by workspace administrators.

Reference: https://elevenlabs.io/docs/api-reference/workspace/members/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `email` (string, required) — Email of the target user.
- `is_locked` (boolean, optional, nullable) — Whether to lock or unlock the user account.
- `workspace_seat_type` (enum, optional, nullable) — The workspace seat type
  - Allowed values: `workspace_admin`, `workspace_member`, `workspace_lite_member`
- `workspace_role` (enum, optional, nullable, deprecated) — The workspace role of the user. This is deprecated, use `workspace_seat_type` instead.
  - Allowed values: `workspace_admin`, `workspace_member`, `workspace_lite_member`

## Response

### 200

Successful Response

- `status` (string, required) — The status of the workspace member update request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

## Examples

**Request**

```json
{
  "email": "jane.doe@example.com"
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
    await client.workspace.members.update({
        email: "jane.doe@example.com",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.members.update(
    email="jane.doe@example.com",
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

	url := "https://api.elevenlabs.io/v1/workspace/members"

	payload := strings.NewReader("{\n  \"email\": \"jane.doe@example.com\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/members")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"jane.doe@example.com\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/members")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"jane.doe@example.com\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/members', [
  'body' => '{
  "email": "jane.doe@example.com"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/members");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"jane.doe@example.com\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["email": "jane.doe@example.com"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/members")! as URL,
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
