---
title: "List pronunciation dictionaries"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/list.md
path: docs/api-reference/pronunciation-dictionaries/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List pronunciation dictionaries

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries

Get a list of the pronunciation dictionaries you have access to and their metadata

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries:
    get:
      operationId: list
      summary: List pronunciation dictionaries
      description: >-
        Get a list of the pronunciation dictionaries you have access to and
        their metadata
      tags:
        - subpackage_pronunciationDictionaries
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
            How many pronunciation dictionaries to return at maximum. Can not
            exceed 100, defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: sort
          in: query
          description: Which field to sort by, one of 'created_at_unix' or 'name'.
          required: false
          schema:
            oneOf:
              - $ref: >-
                  #/components/schemas/V1PronunciationDictionariesGetParametersSortSchema
              - type: 'null'
            default: creation_time_unix
        - name: sort_direction
          in: query
          description: Which direction to sort the voices in. 'ascending' or 'descending'.
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: >-
                  #/components/schemas/GetPronunciationDictionariesMetadataResponseModel
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
    V1PronunciationDictionariesGetParametersSortSchema:
      type: string
      enum:
        - creation_time_unix
        - name
      default: creation_time_unix
      description: Which field to sort by, one of 'created_at_unix' or 'name'.
      title: V1PronunciationDictionariesGetParametersSortSchema
    GetPronunciationDictionaryMetadataResponseModelPermissionOnResource:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The permission on the resource of the pronunciation dictionary.
      title: GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
    GetPronunciationDictionaryMetadataResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the pronunciation dictionary.
        latest_version_id:
          type: string
          description: The ID of the latest version of the pronunciation dictionary.
        latest_version_rules_num:
          type: integer
          description: >-
            The number of rules in the latest version of the pronunciation
            dictionary.
        name:
          type: string
          description: The name of the pronunciation dictionary.
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
            - type: 'null'
          description: The permission on the resource of the pronunciation dictionary.
        created_by:
          type: string
          description: The user ID of the creator of the pronunciation dictionary.
        creation_time_unix:
          type: integer
          description: The creation time of the pronunciation dictionary in Unix timestamp.
        archived_time_unix:
          type:
            - integer
            - 'null'
          description: The archive time of the pronunciation dictionary in Unix timestamp.
        description:
          type:
            - string
            - 'null'
          description: The description of the pronunciation dictionary.
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - permission_on_resource
        - created_by
        - creation_time_unix
      title: GetPronunciationDictionaryMetadataResponseModel
    GetPronunciationDictionariesMetadataResponseModel:
      type: object
      properties:
        pronunciation_dictionaries:
          type: array
          items:
            $ref: >-
              #/components/schemas/GetPronunciationDictionaryMetadataResponseModel
          description: A list of pronunciation dictionaries and their metadata.
        next_cursor:
          type:
            - string
            - 'null'
          description: The next cursor to use for pagination.
        has_more:
          type: boolean
          description: Whether there are more pronunciation dictionaries to fetch.
      required:
        - pronunciation_dictionaries
        - has_more
      title: GetPronunciationDictionariesMetadataResponseModel
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
  "pronunciation_dictionaries": [
    {
      "id": "5xM3yVvZQKV0EfqQpLrJ",
      "latest_version_id": "5xM3yVvZQKV0EfqQpLr2",
      "latest_version_rules_num": 2,
      "name": "My Dictionary",
      "permission_on_resource": "admin",
      "created_by": "ar6633Es2kUjFXBdR1iVc9ztsXl1",
      "creation_time_unix": 1714156800,
      "description": "This is a test dictionary"
    }
  ],
  "has_more": false,
  "next_cursor": "5xM3yVvZQKV0EfqQpLr2"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries")! as URL,
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
