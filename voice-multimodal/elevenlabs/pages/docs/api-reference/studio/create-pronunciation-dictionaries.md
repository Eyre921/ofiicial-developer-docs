---
title: "Create Pronunciation Dictionaries"
source: https://elevenlabs.io/docs/api-reference/studio/create-pronunciation-dictionaries.md
path: docs/api-reference/studio/create-pronunciation-dictionaries
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Pronunciation Dictionaries

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/pronunciation-dictionaries
Content-Type: application/json

Create a set of pronunciation dictionaries acting on a project. This will automatically mark text within this project as requiring reconverting where the new dictionary would apply or the old one no longer does.

Reference: https://elevenlabs.io/docs/api-reference/studio/create-pronunciation-dictionaries

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

### Body (application/json)

- `pronunciation_dictionary_locators` (list of object, required) — A list of pronunciation dictionary locators (pronunciation\_dictionary\_id, version\_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation\_dictionary\_locators="\{"pronunciation\_dictionary\_id":"Vmd4Zor6fplcA7WrINey","version\_id":"hRPaxjlTdR7wFMhV4w0b"}"' --form 'pronunciation\_dictionary\_locators="\{"pronunciation\_dictionary\_id":"JzWtcGQMJ6bnlWwyMo7e","version\_id":"lbmwxiLu4q6txYxgdZqn"}"'.
  - `pronunciation_dictionary_id` (string, required)
  - `version_id` (string, required, nullable)
- `invalidate_affected_text` (boolean, optional, default: true) — This will automatically mark text in this project for reconversion when the new dictionary applies or the old one no longer does.

## Response

### 200

Successful Response

- `status` (string, required) — The status of the create pronunciation dictionary request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

## Examples

**Request**

```json
{
  "pronunciation_dictionary_locators": [
    {
      "pronunciation_dictionary_id": "Vmd4Zor6fplcA7WrINey",
      "version_id": "hRPaxjlTdR7wFMhV4w0b"
    }
  ]
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
    await client.studio.projects.pronunciationDictionaries.create("project_id", {
        pronunciationDictionaryLocators: [
            {
                pronunciationDictionaryId: "Vmd4Zor6fplcA7WrINey",
                versionId: "hRPaxjlTdR7wFMhV4w0b",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, PronunciationDictionaryVersionLocator

client = ElevenLabs()

client.studio.projects.pronunciation_dictionaries.create(
    project_id="project_id",
    pronunciation_dictionary_locators=[
        PronunciationDictionaryVersionLocator(
            pronunciation_dictionary_id="Vmd4Zor6fplcA7WrINey",
            version_id="hRPaxjlTdR7wFMhV4w0b",
        )
    ],
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries"

	payload := strings.NewReader("{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"Vmd4Zor6fplcA7WrINey\",\n      \"version_id\": \"hRPaxjlTdR7wFMhV4w0b\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"Vmd4Zor6fplcA7WrINey\",\n      \"version_id\": \"hRPaxjlTdR7wFMhV4w0b\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")
  .header("Content-Type", "application/json")
  .body("{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"Vmd4Zor6fplcA7WrINey\",\n      \"version_id\": \"hRPaxjlTdR7wFMhV4w0b\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries', [
  'body' => '{
  "pronunciation_dictionary_locators": [
    {
      "pronunciation_dictionary_id": "Vmd4Zor6fplcA7WrINey",
      "version_id": "hRPaxjlTdR7wFMhV4w0b"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"Vmd4Zor6fplcA7WrINey\",\n      \"version_id\": \"hRPaxjlTdR7wFMhV4w0b\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["pronunciation_dictionary_locators": [
    [
      "pronunciation_dictionary_id": "Vmd4Zor6fplcA7WrINey",
      "version_id": "hRPaxjlTdR7wFMhV4w0b"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")! as URL,
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
