---
title: "Create Voice Collection"
source: https://elevenlabs.io/docs/api-reference/voices/collections/create.md
path: docs/api-reference/voices/collections/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Voice Collection

POST https://api.elevenlabs.io/v1/voices/collections
Content-Type: application/json

Creates a new voice collection. The caller becomes its admin.

Reference: https://elevenlabs.io/docs/api-reference/voices/collections/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

This endpoint expects a Body_Create_voice_collection_v1_voices_collections_post.

- `title` (string, required) — Title of the collection to create/update.
- `icon` (string, required) — Icon of the collection to create/update.

## Response

### 200

Successful Response

- `collection_id` (string, required) — The ID of the voice collection.
- `title` (string, required) — The title of the voice collection.
- `icon` (string, required) — The icon of the voice collection.
- `permission_on_resource` (enum, required) — The caller's access role on the voice collection.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{
  "title": "string",
  "icon": "string"
}
```

**Response**

```json
{
  "collection_id": "string",
  "title": "string",
  "icon": "string",
  "permission_on_resource": "admin"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/voices/collections"

payload = {
    "title": "string",
    "icon": "string"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/voices/collections';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"title":"string","icon":"string"}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/collections"

	payload := strings.NewReader("{\n  \"title\": \"string\",\n  \"icon\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/voices/collections")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"title\": \"string\",\n  \"icon\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/collections")
  .header("Content-Type", "application/json")
  .body("{\n  \"title\": \"string\",\n  \"icon\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/collections', [
  'body' => '{
  "title": "string",
  "icon": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/collections");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"title\": \"string\",\n  \"icon\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "title": "string",
  "icon": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/collections")! as URL,
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
