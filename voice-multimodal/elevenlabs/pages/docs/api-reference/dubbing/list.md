---
title: "List Dubs"
source: https://elevenlabs.io/docs/api-reference/dubbing/list.md
path: docs/api-reference/dubbing/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Dubs

GET https://api.elevenlabs.io/v1/dubbing

List the dubs you have access to.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing:
    get:
      operationId: list
      summary: List Dubs
      description: List the dubs you have access to.
      tags:
        - dubbing
      parameters:
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: >-
            How many dubs to return at maximum. Can not exceed 200, defaults to
            100.
          required: false
          schema:
            type: integer
            default: 100
        - name: dubbing_status
          in: query
          description: What state the dub is currently in.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersDubbingStatus'
        - name: dubbing_statuses
          in: query
          description: Filter by dubbing status.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              $ref: >-
                #/components/schemas/V1DubbingGetParametersDubbingStatusesSchemaItems
        - name: dubbing_models
          in: query
          description: Filter by dubbing model generation.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              $ref: >-
                #/components/schemas/V1DubbingGetParametersDubbingModelsSchemaItems
        - name: target_language_codes
          in: query
          description: Filter by target language code.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: creation_sources
          in: query
          description: Filter by dubbing creation source.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              $ref: >-
                #/components/schemas/V1DubbingGetParametersCreationSourcesSchemaItems
        - name: filter_by_creator
          in: query
          description: >-
            Filters who created the resources being listed, whether it was the
            user running the request or someone else that shared the resource
            with them.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersFilterByCreator'
            default: all
        - name: order_by
          in: query
          description: The field to use for ordering results from this query.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersOrderBy'
            default: created_at
        - name: order_direction
          in: query
          description: The order direction to use for results from this query.
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingGetParametersOrderDirection'
            default: DESCENDING
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DubbingMetadataPageResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    V1DubbingGetParametersDubbingStatus:
      type: string
      enum:
        - dubbing
        - dubbed
        - failed
      description: What state the dub is currently in.
      title: V1DubbingGetParametersDubbingStatus
    V1DubbingGetParametersDubbingStatusesSchemaItems:
      type: string
      enum:
        - queued
        - preparing
        - dubbing
        - dubbed
        - failed
      title: V1DubbingGetParametersDubbingStatusesSchemaItems
    V1DubbingGetParametersDubbingModelsSchemaItems:
      type: string
      enum:
        - dubbing_v1
        - dubbing_v2
      title: V1DubbingGetParametersDubbingModelsSchemaItems
    V1DubbingGetParametersCreationSourcesSchemaItems:
      type: string
      enum:
        - flow_node
        - dubbing_ui
        - dubbing_api
      title: V1DubbingGetParametersCreationSourcesSchemaItems
    V1DubbingGetParametersFilterByCreator:
      type: string
      enum:
        - personal
        - others
        - all
      default: all
      description: >-
        Filters who created the resources being listed, whether it was the user
        running the request or someone else that shared the resource with them.
      title: V1DubbingGetParametersFilterByCreator
    V1DubbingGetParametersOrderBy:
      type: string
      enum:
        - created_at
        - name
      default: created_at
      description: The field to use for ordering results from this query.
      title: V1DubbingGetParametersOrderBy
    V1DubbingGetParametersOrderDirection:
      type: string
      enum:
        - DESCENDING
        - ASCENDING
      default: DESCENDING
      description: The order direction to use for results from this query.
      title: V1DubbingGetParametersOrderDirection
    DubbingMediaMetadata:
      type: object
      properties:
        content_type:
          type: string
          description: The content type of the media.
        duration:
          type: number
          format: double
          description: The duration of the media in seconds.
      required:
        - content_type
        - duration
      title: DubbingMediaMetadata
    DubbingMetadataResponse:
      type: object
      properties:
        dubbing_id:
          type: string
          description: The ID of the dubbing project.
        name:
          type: string
          description: The name of the dubbing project.
        status:
          type: string
          description: The state this dub is in.
        source_language:
          type:
            - string
            - 'null'
          description: >-
            Once dubbing has completed, the ISO-639-1 code of the original
            media's source language.
        target_languages:
          type: array
          items:
            type: string
          description: The ISO-639-1 code of the languages this media has been dubbed into.
        editable:
          type: boolean
          default: false
          description: Whether this dubbing project is editable in Dubbing Studio.
        created_at:
          type: string
          format: date-time
          description: Timestamp this dub was created.
        media_metadata:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaMetadata'
            - type: 'null'
          description: >-
            Metadata, such as the length in seconds and content type, of the
            dubbed content.
        error:
          type:
            - string
            - 'null'
          description: Error message indicate, if this dub has failed, what happened.
      required:
        - dubbing_id
        - name
        - status
        - source_language
        - target_languages
        - created_at
      title: DubbingMetadataResponse
    DubbingMetadataPageResponseModel:
      type: object
      properties:
        dubs:
          type: array
          items:
            $ref: '#/components/schemas/DubbingMetadataResponse'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - dubs
        - next_cursor
        - has_more
      title: DubbingMetadataPageResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



**Response**

```json
{
  "dubs": [
    {
      "dubbing_id": "string",
      "name": "string",
      "status": "preparing",
      "source_language": "string",
      "target_languages": [
        "string"
      ],
      "created_at": "2024-01-15T09:30:00Z",
      "editable": false,
      "media_metadata": {
        "content_type": "string",
        "duration": 1.1
      },
      "error": "string"
    }
  ],
  "next_cursor": "string",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/dubbing"

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

url = URI("https://api.elevenlabs.io/v1/dubbing")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing")! as URL,
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
