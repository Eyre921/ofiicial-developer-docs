---
title: "Update folder"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/update.md
path: docs/eleven-agents/api-reference/tests/test-folders/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update folder

PATCH https://api.elevenlabs.io/v1/convai/agent-testing/folders/{folder_id}
Content-Type: application/json

Updates an agent test folder. Currently only supports updating the folder name.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `folder_id` (string, required) — The folder ID.

### Body (application/json)

- `name` (string, required) — The new name for the folder

## Response

### 200

Folder successfully updated

- `id` (string, required)
- `name` (string, required)
- `folder_path` (list of object, optional) — The path from the root folder to the current folder.
  - `id` (string, required)
  - `name` (string, optional, default: )
- `children_count` (integer, optional, default: 0) — The number of direct children (tests and subfolders) in this folder

## Examples

**Request**

```json
{
  "name": "name"
}
```

**Response**

```json
{
  "id": "id",
  "name": "name",
  "folder_path": [
    {
      "id": "id",
      "name": "name"
    }
  ],
  "children_count": 1
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.folders.update("tfld_7301khxdkycse5f88fzjdtrterzm", {
        name: "name",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.folders.update(
    folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
    name="name",
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm"

	payload := strings.NewReader("{\n  \"name\": \"name\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"name\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"name\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm', [
  'body' => '{
  "name": "name"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"name\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "name"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
