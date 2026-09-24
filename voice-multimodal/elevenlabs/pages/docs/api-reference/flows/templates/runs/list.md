---
title: "List Template Runs"
source: https://elevenlabs.io/docs/api-reference/flows/templates/runs/list.md
path: docs/api-reference/flows/templates/runs/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Template Runs

GET https://api.elevenlabs.io/v1/flows/templates/{template_id}/runs

List this template's runs created through this API, newest first.

Reference: https://elevenlabs.io/docs/api-reference/flows/templates/runs/list

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

- `cursor` (string, optional, nullable) — Pagination cursor: the `next_cursor` value of the previous page's response. Omit it for the first page.
- `page_size` (integer, optional, default: 30) — How many runs to return per page.
- `version_id` (string, optional, nullable) — Only return runs of this template version id.

## Response

### 200

Successful Response

- `runs` (list of TemplateRunResponse, required) — The runs on this page, newest first. Each item has the same shape as `GET /v1/flows/templates/{template_id}/runs/{run_id}`.
- `next_cursor` (string, required, nullable) — Pass as `cursor` to fetch the next page. `null` when there is no further page.
- `has_more` (boolean, required) — Whether more runs exist beyond this page.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### TemplateRunResponse

A template run and its outputs. Every output exists from the moment the run is created and reports its own `status`; the run's `status` rolls them up, and the run is finished once it is `completed` or `failed`.

- `id` (string, required) — The unique identifier of the run.
- `template_id` (string, required) — The template this run executed, so a webhook consumer running several templates can tell their runs apart without keeping a run-to-template map.
- `version_id` (string, required) — The template version this run executed. Resolved when the run is created, so a run started with `latest` records the concrete version it ran.
- `status` (enum, required) — The run's status, rolled up from its outputs: `pending` until an output starts, `generating` while any output is unfinished, `completed` once every output has completed, and `failed` once every output has finished and at least one failed. `completed` and `failed` are terminal: the `flows_template_run` webhook fires once the run reaches either.
  - Allowed values: `pending`, `generating`, `completed`, `failed`
- `outputs` (map from string to TemplateOutput, required) — The run's outputs, keyed by output port id. Each is a `TemplateOutput` discriminated on `type`, the `type` of its port's `content_schema`.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### TemplateOutput

One output of a template run, discriminated on `type`: the `type` of the port's `content_schema`. Check `status` for where it is in its lifecycle.

- `type`: `array` (TemplateArrayOutput)
  - `has_more` (boolean, required) — Whether the list has elements beyond `content`.
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content` (list of TemplateOutput, optional, nullable) — The first elements of the list, in order, each following the shape of the schema's `items`. Present only when `status` is `completed`. When `has_more` is true this is not the whole list. Reserved: no template produces this kind of output yet; it is published so that templates which do can be run with the same client.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
  - `next_cursor` (string, optional, nullable) — Pass as `cursor` to a later endpoint to fetch the elements after `content`. `null` when `content` holds the whole list, or before the output completes. Reserved: no template produces this kind of output yet; it is published so that templates which do can be run with the same client.
- `type`: `audio` (TemplateAudioOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content_mime_type` (string, optional, nullable) — The MIME type of the generated media. Present only when `status` is `completed`.
  - `content_url` (string, optional, nullable) — A signed URL to download the generated media from. Present only when `status` is `completed`. It expires about an hour after this response is returned; fetch the run again for a fresh URL.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `boolean` (TemplateBooleanOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content` (boolean, optional, nullable) — The generated boolean. Present only when `status` is `completed`. Reserved: no template produces this kind of output yet; it is published so that templates which do can be run with the same client.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `image` (TemplateImageOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content_mime_type` (string, optional, nullable) — The MIME type of the generated media. Present only when `status` is `completed`.
  - `content_url` (string, optional, nullable) — A signed URL to download the generated media from. Present only when `status` is `completed`. It expires about an hour after this response is returned; fetch the run again for a fresh URL.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `integer` (TemplateIntegerOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content` (integer, optional, nullable) — The generated integer. Present only when `status` is `completed`. Reserved: no template produces this kind of output yet; it is published so that templates which do can be run with the same client.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `number` (TemplateNumberOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content` (double, optional, nullable) — The generated number. Present only when `status` is `completed`. Reserved: no template produces this kind of output yet; it is published so that templates which do can be run with the same client.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `object` (TemplateObjectOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content` (map from string to TemplateOutput, optional, nullable) — One output per field, keyed by field name, each following the shape of that field's schema. Present only when `status` is `completed`. Reserved: no template produces this kind of output yet; it is published so that templates which do can be run with the same client.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `string` (TemplateStringOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content` (string, optional, nullable) — The generated text. Present only when `status` is `completed`.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`
- `type`: `video` (TemplateVideoOutput)
  - `id` (string, required) — The id of the generation behind this output. Pass it as a `generation` reference to use the output as an input elsewhere.
  - `status` (enum, required) — The lifecycle status of the output. It ends at `completed`, when the output's content fields are set, or `failed`, when `failure_reason` and `error_message` are set.
    - Allowed values: `pending`, `generating`, `completed`, `failed`
  - `content_mime_type` (string, optional, nullable) — The MIME type of the generated media. Present only when `status` is `completed`.
  - `content_url` (string, optional, nullable) — A signed URL to download the generated media from. Present only when `status` is `completed`. It expires about an hour after this response is returned; fetch the run again for a fresh URL.
  - `error_message` (string, optional, nullable) — A human-readable description of the failure. Present only when `status` is `failed`. Failed generations are not charged.
  - `failure_reason` (enum, optional, nullable) — The category of failure. Present only when `status` is `failed`.
    - Allowed values: `timeout`, `model_error`, `moderated`, `invalid_parameters`, `dependency_failed`, `charging_failed`, `internal_error`

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "runs": [
    {
      "id": "sess_JWr5N6X9ZTqf8jD2LmQb",
      "template_id": "tmpl_abc123",
      "version_id": "ver_01hxyz",
      "status": "generating",
      "outputs": {
        "marketing_title": {
          "type": "string",
          "id": "Kx2mP7Y4WVrg9kE3NnRc",
          "status": "completed",
          "content": "Ride the wave."
        },
        "product_demo": {
          "type": "video",
          "id": "QWr5N6X9ZTqf8jD2La3B",
          "status": "generating"
        },
        "product_still": {
          "type": "image",
          "id": "JWr5N6X9ZTqf8jD2LmQb",
          "status": "completed",
          "content_mime_type": "image/png",
          "content_url": "https://storage.googleapis.com/generations/JWr5N6X9ZTqf8jD2LmQb"
        }
      }
    }
  ],
  "next_cursor": "MjAyNi0wNy0xN1QxMjowMDowMHxLeDJtUDdZNFdWcmc5a0UzTm5SYw",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.templates.runs.list("template_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.templates.runs.list(
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

	url := "https://api.elevenlabs.io/v1/flows/templates/template_id/runs"

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

url = URI("https://api.elevenlabs.io/v1/flows/templates/template_id/runs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/flows/templates/template_id/runs")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/flows/templates/template_id/runs');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/templates/template_id/runs");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/templates/template_id/runs")! as URL,
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
