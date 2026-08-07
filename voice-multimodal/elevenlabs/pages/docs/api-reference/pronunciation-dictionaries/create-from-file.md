---
title: "Create a pronunciation dictionary from a file"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-file.md
path: docs/api-reference/pronunciation-dictionaries/create-from-file
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create a pronunciation dictionary from a file

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file
Content-Type: multipart/form-data

Creates a new pronunciation dictionary from a lexicon .PLS file

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-file

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `name` (string, required) — The name of the pronunciation dictionary, used for identification only.
- `file` (file, optional) — A lexicon .pls file which we will use to initialize the project with.
- `description` (string, optional) — A description of the pronunciation dictionary, used for identification only.
- `workspace_access` (enum, optional) — Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.

## Response

### 200

Successful Response

- `id` (string, required) — The ID of the created pronunciation dictionary.
- `name` (string, required) — The name of the created pronunciation dictionary.
- `created_by` (string, required) — The user ID of the creator of the pronunciation dictionary.
- `creation_time_unix` (integer, required) — The creation time of the pronunciation dictionary in Unix timestamp.
- `version_id` (string, required) — The ID of the created pronunciation dictionary version.
- `version_rules_num` (integer, required) — The number of rules in the version of the pronunciation dictionary.
- `permission_on_resource` (enum, required, nullable) — The permission on the resource of the pronunciation dictionary.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `description` (string, optional, nullable) — The description of the pronunciation dictionary.

## Examples

**Request**

```json
{
  "file": "<file: <file1>>",
  "name": "My Dictionary"
}
```

**Response**

```json
{
  "id": "5xM3yVvZQKV0EfqQpLrJ",
  "name": "My Dictionary",
  "created_by": "ar6633Es2kUjFXBdR1iVc9ztsXl1",
  "creation_time_unix": 1714156800,
  "version_id": "5xM3yVvZQKV0EfqQpLrJ",
  "version_rules_num": 5,
  "permission_on_resource": "admin",
  "description": "This is a test dictionary"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.createFromFile({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.create_from_file(
    file="example_file",
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'name',
        'contents' => 'My Dictionary'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nMy Dictionary\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"workspace_access\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "name",
    "value": "My Dictionary"
  ],
  [
    "name": "workspace_access",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file")! as URL,
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
