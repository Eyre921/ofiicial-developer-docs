---
title: "Get default interruption ignore terms"
source: https://elevenlabs.io/docs/api-reference/agents/get-default-interruption-ignore-terms.md
path: docs/api-reference/agents/get-default-interruption-ignore-terms
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get default interruption ignore terms

GET https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms

Get the curated per-language default interruption ignore terms used to seed an agent's turn configuration.

Reference: https://elevenlabs.io/docs/api-reference/agents/get-default-interruption-ignore-terms

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
                  #/components/schemas/DefaultInterruptionIgnoreTermsResponseModel
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
    InterruptionIgnoreTermSetModel:
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
    DefaultInterruptionIgnoreTermsResponseModel:
      type: object
      properties:
        terms_by_language:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/InterruptionIgnoreTermSetModel'
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



**Request**

```json
{}
```

**Response**

```json
{
  "terms_by_language": {
    "en": {
      "acknowledgements": [
        "uh-huh",
        "mm-hmm",
        "okay"
      ],
      "openers": [
        "hello",
        "hi there",
        "good morning"
      ],
      "confirmations": [
        "yes",
        "no",
        "sure"
      ]
    },
    "es": {
      "acknowledgements": [
        "ajá",
        "mm-hmm",
        "vale"
      ],
      "openers": [
        "hola",
        "buenos días",
        "qué tal"
      ],
      "confirmations": [
        "sí",
        "no",
        "claro"
      ]
    },
    "fr": {
      "acknowledgements": [
        "d'accord",
        "mm-hmm",
        "bien"
      ],
      "openers": [
        "bonjour",
        "salut",
        "bonsoir"
      ],
      "confirmations": [
        "oui",
        "non",
        "bien sûr"
      ]
    }
  },
  "max_terms": 50
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/defaults/interruption-ignore-terms")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
