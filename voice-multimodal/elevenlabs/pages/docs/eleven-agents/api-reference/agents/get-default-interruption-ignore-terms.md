---
title: "Get default interruption ignore terms"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-default-interruption-ignore-terms.md
path: docs/eleven-agents/api-reference/agents/get-default-interruption-ignore-terms
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get default interruption ignore terms

GET https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms

Get the curated per-language default interruption ignore terms used to seed an agent's turn configuration.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-default-interruption-ignore-terms

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/defaults/interruption-ignore-terms:
    get:
      operationId: get_default_interruption_ignore_terms
      summary: Get default interruption ignore terms
      description: >-
        Get the curated per-language default interruption ignore terms used to
        seed an agent's turn configuration.
      tags:
        - agents
      parameters:
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
                  #/components/schemas/type_:DefaultInterruptionIgnoreTermsResponseModel
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:InterruptionIgnoreTermSetModel:
      type: object
      properties:
        acknowledgements:
          type: array
          items:
            type: string
          description: >-
            Acknowledgements: safe backchannels seeded when interruption ignore
            terms are turned on.
        openers:
          type: array
          items:
            type: string
          description: 'Openers: greetings and presence probes. Opt-in (off by default).'
        confirmations:
          type: array
          items:
            type: string
          description: >-
            Confirmations: affirmation/negation answer words. Opt-in (off by
            default).
      required:
        - acknowledgements
        - openers
        - confirmations
      title: InterruptionIgnoreTermSetModel
    type_:DefaultInterruptionIgnoreTermsResponseModel:
      type: object
      properties:
        terms_by_language:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:InterruptionIgnoreTermSetModel'
          description: >-
            Curated default interruption ignore terms keyed by language code,
            split into acknowledgements / openers / confirmations categories.
        max_terms:
          type: integer
          description: Maximum number of interruption ignore terms allowed on an agent.
      required:
        - terms_by_language
        - max_terms
      title: DefaultInterruptionIgnoreTermsResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Response**

```json
{
  "terms_by_language": {
    "key": {
      "acknowledgements": [
        "acknowledgements"
      ],
      "openers": [
        "openers"
      ],
      "confirmations": [
        "confirmations"
      ]
    }
  },
  "max_terms": 1
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.getDefaultInterruptionIgnoreTerms();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.get_default_interruption_ignore_terms()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms")! as URL,
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
