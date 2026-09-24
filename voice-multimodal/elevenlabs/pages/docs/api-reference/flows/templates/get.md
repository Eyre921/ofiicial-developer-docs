---
title: "Get Template"
source: https://elevenlabs.io/docs/api-reference/flows/templates/get.md
path: docs/api-reference/flows/templates/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Template

GET https://api.elevenlabs.io/v1/flows/templates/{template_id}

Retrieve one flows template, together with each runnable version's inputs and outputs. `versions` is empty when no published version is runnable through this API. Works for any template you can open, including templates shared with you by link or published to Explore from another workspace, which `GET /v1/flows/templates` does not list.

Reference: https://elevenlabs.io/docs/api-reference/flows/templates/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `template_id` (string, required) — The ID of the template, as shown in the ElevenLabs app or by `GET /v1/flows/templates`.

### Query parameters

- `versions_per_template` (integer, optional, default: 10) — How many of each template's published versions to return, newest first. `has_more_versions` tells you when a template has more.

## Response

### 200

Successful Response

- `id` (string, required) — Pass as `template_id` on `POST /v1/flows/templates/{template_id}/runs`.
- `name` (string, required) — The template's name.
- `versions` (list of TemplateVersion, required) — The published versions this caller can run, newest first. A version whose graph uses a model that is not available to you through the API is left out, as is one whose stored snapshot is gone; either way the list can be empty while the template still has versions the ElevenLabs app can run.
- `has_more_versions` (boolean, required) — Whether this template has further published versions beyond the `versions_per_template` returned here. Fetch `GET /v1/flows/templates/{template_id}` with a larger `versions_per_template` to see more of them.
- `description` (string, optional, nullable) — The template's description, if it has one.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### TemplateVersion

A published snapshot of a template, and the ports it runs with.

- `version_id` (string, required) — Pass as `version_id` on `POST /v1/flows/templates/{template_id}/runs` to pin a run to this snapshot.
- `published_at_unix` (integer, required) — When this version was published, as a Unix timestamp in seconds.
- `is_latest` (boolean, required) — Whether this is the version a run gets when `version_id` is omitted or set to `latest`.
- `inputs` (list of TemplatePort, required) — The inputs this version accepts, in canvas order. Every input is required on a run.
- `outputs` (list of TemplatePort, required) — The outputs this version produces, in canvas order.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### TemplatePort

One input or output port of a published template version.

- `id` (string, required) — The port id. Input ids are the keys of the `inputs` map on `POST /v1/flows/templates/{template_id}/runs`; output ids are the keys of the `outputs` map on the run response.
- `content_schema` (ContentSchema, required) — What this port accepts or produces, as a `ContentSchema`. Its `title` is the port's display name and its `description` is the help text the template author wrote. For an input, its `type` decides what value is accepted: `string` takes a bare string or a `generation` reference, `voice` takes a `voice` reference, and `image`/`video`/`audio` take an `asset`, `generation` or `inline_base64` reference. `number`, `integer` and `boolean` take a JSON value of that type. An `array` input takes a JSON array with one value per element, each admissible for its `items`. `object` inputs cannot be bound through this API yet. A `string` schema may carry an `enum` of the only values accepted. For an output, its `type` decides which `Template<Kind>Output` shape the run response holds under the port id.

### ValidationErrorLocItems

### ContentSchema

- `type`: `array` (ArraySchema)
  - `items` (ContentSchema, required)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `audio` (AudioSchema)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `boolean` (BooleanSchema)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `image` (ImageSchema)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `integer` (IntegerSchema)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `number` (NumberSchema)
  - `description` (string, optional, nullable)
  - `enum` (list of double, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `object` (ObjectSchema)
  - `description` (string, optional, nullable)
  - `properties` (map from string to ContentSchema, optional)
  - `required` (list of string, optional)
  - `title` (string, optional, nullable)
- `type`: `string` (StringSchema)
  - `description` (string, optional, nullable)
  - `enum` (list of string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `video` (VideoSchema)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)
- `type`: `voice` (VoiceSchema)
  - `description` (string, optional, nullable)
  - `title` (string, optional, nullable)

## Examples

**Response**

```json
{
  "id": "tmpl_abc123",
  "name": "Product shot",
  "versions": [
    {
      "version_id": "ver_01hxyz",
      "published_at_unix": 1,
      "is_latest": true,
      "inputs": [
        {
          "id": "prompt",
          "content_schema": {
            "type": "string",
            "description": "string",
            "enum": [
              "string"
            ],
            "title": "string"
          }
        }
      ],
      "outputs": [
        {
          "id": "prompt",
          "content_schema": {
            "type": "string",
            "description": "string",
            "enum": [
              "string"
            ],
            "title": "string"
          }
        }
      ]
    }
  ],
  "has_more_versions": true,
  "description": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.templates.get("template_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.templates.get(
    template_id="template_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/flows/templates/template_id"

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

url = URI("https://api.elevenlabs.io/v1/flows/templates/template_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/flows/templates/template_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/flows/templates/template_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/templates/template_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/templates/template_id")! as URL,
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
