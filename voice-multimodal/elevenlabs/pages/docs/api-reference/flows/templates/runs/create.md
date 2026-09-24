---
title: "Create Template Run"
source: https://elevenlabs.io/docs/api-reference/flows/templates/runs/create.md
path: docs/api-reference/flows/templates/runs/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Template Run

POST https://api.elevenlabs.io/v1/flows/templates/{template_id}/runs
Content-Type: application/json

Start a run of a flows template. Pass `version_id` to pin a snapshot, or omit it / pass `latest` to run the latest published version. Set input values under `inputs`, keyed by input port id. The response is the run in its initial state, with every output already listed under its port id in `outputs`. Include `webhook` to receive a `flows_template_run` event carrying the finished run once its `status` is `completed` or `failed`; this is the recommended way to wait. Without one, fetch `GET /v1/flows/templates/{template_id}/runs/{run_id}` at a modest interval until the `status` is terminal.

Reference: https://elevenlabs.io/docs/api-reference/flows/templates/runs/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `template_id` (string, required) — The ID of the template, as shown in the ElevenLabs app or by `GET /v1/flows/templates`.

### Body (application/json)

This endpoint expects a TemplateRunCreateRequest.

- `inputs` (map from string to TemplateRunInput, required) — Input values keyed by input port id. Every input port of the version being run must be given; a missing or unknown id is rejected. Pass `{}` for a template with no inputs.
- `version_id` (string, optional, nullable) — The template snapshot to run. Pass a specific version id to pin that snapshot, or `latest` (the default when omitted) to run the template's most recently published version. Only published versions can be pinned, except by the template's owner, who may also pin an unpublished saved snapshot to try it out before publishing. The live draft is never run through this API.
- `webhook` (WebhookTarget, optional, nullable) — Include to send the run's result to the workspace's configured flows webhooks once the run's `status` reaches `completed` or `failed`. One event for the whole run: the `flows_template_run` event's `data` matches the terminal response of `GET /v1/flows/templates/{template_id}/runs/{run_id}`.

## Response

### 200

Successful Response

- `id` (string, required) — The unique identifier of the run.
- `template_id` (string, required) — The template this run executed, so a webhook consumer running several templates can tell their runs apart without keeping a run-to-template map.
- `version_id` (string, required) — The template version this run executed. Resolved when the run is created, so a run started with `latest` records the concrete version it ran.
- `status` (enum, required) — The run's status, rolled up from its outputs: `pending` until an output starts, `generating` while any output is unfinished, `completed` once every output has completed, and `failed` once every output has finished and at least one failed. `completed` and `failed` are terminal: the `flows_template_run` webhook fires once the run reaches either.
  - Allowed values: `pending`, `generating`, `completed`, `failed`
- `outputs` (map from string to TemplateOutput, required) — The run's outputs, keyed by output port id. Each is a `TemplateOutput` discriminated on `type`, the `type` of its port's `content_schema`.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### TemplateRunInput

One value bound to a template input port, in the form its `content_schema` calls for. A `string` port takes the text itself; `number`, `integer` and `boolean` ports take a JSON value of that type. Anything stored elsewhere is a reference discriminated on `type`: a prior `generation`, an uploaded `asset`, a `voice`, or media passed `inline_base64`. An `array` port takes a JSON array with one value per element, admissible for the schema's `items`. `object` ports cannot be bound through this API yet. No constraints beyond the wire shape live here: what a port accepts (an `enum`, a length) is stated by its `content_schema`, and the run path validates against that same schema.

### WebhookTarget

- `type`: `all` (WebhookTargetAll)
- `type`: `ids` (WebhookTargetIds)
  - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.

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

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{
  "inputs": {
    "prompt": "a corgi on a surfboard",
    "reference": {
      "asset_id": "5xM2KqOnZyce22SPZ9d4",
      "type": "asset"
    }
  },
  "version_id": "latest",
  "webhook": {
    "type": "all"
  }
}
```

**Response**

```json
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
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.templates.runs.create("template_id", {
        inputs: {
            prompt: "a corgi on a surfboard",
            reference: {
                type: "asset",
                assetId: "5xM2KqOnZyce22SPZ9d4",
            },
        },
        versionId: "latest",
        webhook: {
            type: "all",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, TemplateInputReference_Asset, WebhookTarget_All

client = ElevenLabs()

client.flows.templates.runs.create(
    template_id="template_id",
    inputs={
        "prompt": "a corgi on a surfboard",
        "reference": TemplateInputReference_Asset(
            asset_id="5xM2KqOnZyce22SPZ9d4",
        )
    },
    version_id="latest",
    webhook=WebhookTarget_All(),
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

	url := "https://api.elevenlabs.io/v1/flows/templates/template_id/runs"

	payload := strings.NewReader("{\n  \"inputs\": {\n    \"prompt\": \"a corgi on a surfboard\",\n    \"reference\": {\n      \"asset_id\": \"5xM2KqOnZyce22SPZ9d4\",\n      \"type\": \"asset\"\n    }\n  },\n  \"version_id\": \"latest\",\n  \"webhook\": {\n    \"type\": \"all\"\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/flows/templates/template_id/runs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": {\n    \"prompt\": \"a corgi on a surfboard\",\n    \"reference\": {\n      \"asset_id\": \"5xM2KqOnZyce22SPZ9d4\",\n      \"type\": \"asset\"\n    }\n  },\n  \"version_id\": \"latest\",\n  \"webhook\": {\n    \"type\": \"all\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/flows/templates/template_id/runs")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": {\n    \"prompt\": \"a corgi on a surfboard\",\n    \"reference\": {\n      \"asset_id\": \"5xM2KqOnZyce22SPZ9d4\",\n      \"type\": \"asset\"\n    }\n  },\n  \"version_id\": \"latest\",\n  \"webhook\": {\n    \"type\": \"all\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/flows/templates/template_id/runs', [
  'body' => '{
  "inputs": {
    "prompt": "a corgi on a surfboard",
    "reference": {
      "asset_id": "5xM2KqOnZyce22SPZ9d4",
      "type": "asset"
    }
  },
  "version_id": "latest",
  "webhook": {
    "type": "all"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/templates/template_id/runs");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": {\n    \"prompt\": \"a corgi on a surfboard\",\n    \"reference\": {\n      \"asset_id\": \"5xM2KqOnZyce22SPZ9d4\",\n      \"type\": \"asset\"\n    }\n  },\n  \"version_id\": \"latest\",\n  \"webhook\": {\n    \"type\": \"all\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "inputs": [
    "prompt": "a corgi on a surfboard",
    "reference": [
      "asset_id": "5xM2KqOnZyce22SPZ9d4",
      "type": "asset"
    ]
  ],
  "version_id": "latest",
  "webhook": ["type": "all"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/templates/template_id/runs")! as URL,
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
