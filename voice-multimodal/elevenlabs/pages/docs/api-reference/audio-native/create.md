---
title: "Create audio native project"
source: https://elevenlabs.io/docs/api-reference/audio-native/create.md
path: docs/api-reference/audio-native/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create audio native project

POST https://api.elevenlabs.io/v1/audio-native
Content-Type: multipart/form-data

Creates Audio Native enabled project, optionally starts conversion and returns project ID and embeddable HTML snippet.

Reference: https://elevenlabs.io/docs/api-reference/audio-native/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `name` (string, required) — Project name.
- `image` (string, optional) — (Deprecated) Image URL used in the player. If not provided, default image set in the Player settings is used.
- `author` (string, optional) — Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.
- `title` (string, optional) — Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.
- `small` (boolean, optional) — (Deprecated) Whether to use small player or not. If not provided, default value set in the Player settings is used.
- `text_color` (string, optional) — Text color used in the player. If not provided, default text color set in the Player settings is used.
- `background_color` (string, optional) — Background color used in the player. If not provided, default background color set in the Player settings is used.
- `sessionization` (integer, optional) — (Deprecated) Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.
- `voice_id` (string, optional) — Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.
- `model_id` (string, optional) — TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.
- `file` (file, optional) — Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h3&gt;More of your content&lt;/h3&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'
- `auto_convert` (boolean, optional) — Whether to auto convert the project to audio or not.
- `apply_text_normalization` (enum, optional) — This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.
- `pronunciation_dictionary_locators` (list of string, optional) — A list of pronunciation dictionary locators (pronunciation\_dictionary\_id, version\_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation\_dictionary\_locators="\{"pronunciation\_dictionary\_id":"Vmd4Zor6fplcA7WrINey","version\_id":"hRPaxjlTdR7wFMhV4w0b"}"' --form 'pronunciation\_dictionary\_locators="\{"pronunciation\_dictionary\_id":"JzWtcGQMJ6bnlWwyMo7e","version\_id":"lbmwxiLu4q6txYxgdZqn"}"'.

## Response

### 200

Successful Response

- `project_id` (string, required) — The ID of the created Audio Native project.
- `converting` (boolean, required) — Whether the project is currently being converted.
- `html_snippet` (string, required) — The HTML snippet to embed the Audio Native player.

## Examples

**Request**

```json
{
  "file": "<file: <file1>>",
  "name": "string"
}
```

**Response**

```json
{
  "project_id": "JBFqnCBsd6RMkjVDRZzb",
  "converting": false,
  "html_snippet": "<div id='audio-native-player'></div>"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.audioNative.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_native.create(
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

	url := "https://api.elevenlabs.io/v1/audio-native"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/audio-native")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/audio-native")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/audio-native', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'name',
        'contents' => 'string'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-native");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"background_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nstring\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sessionization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"small\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text_color\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_id\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "apply_text_normalization",
    "value": 
  ],
  [
    "name": "author",
    "value": 
  ],
  [
    "name": "auto_convert",
    "value": 
  ],
  [
    "name": "background_color",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "image",
    "value": 
  ],
  [
    "name": "model_id",
    "value": 
  ],
  [
    "name": "name",
    "value": "string"
  ],
  [
    "name": "pronunciation_dictionary_locators",
    "value": 
  ],
  [
    "name": "sessionization",
    "value": 
  ],
  [
    "name": "small",
    "value": 
  ],
  [
    "name": "text_color",
    "value": 
  ],
  [
    "name": "title",
    "value": 
  ],
  [
    "name": "voice_id",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-native")! as URL,
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
