---
title: "List WhatsApp accounts"
source: https://elevenlabs.io/docs/api-reference/whats-app/accounts/list.md
path: docs/api-reference/whats-app/accounts/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List WhatsApp accounts

GET https://api.elevenlabs.io/v1/convai/whatsapp-accounts

List all WhatsApp accounts

Reference: https://elevenlabs.io/docs/api-reference/whats-app/accounts/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/whatsapp-accounts:
    get:
      operationId: list
      summary: List Whatsapp Accounts
      description: List all WhatsApp accounts
      tags:
        - subpackage_conversationalAi/whatsappAccounts
      parameters:
        - name: agent_id
          in: query
          description: Filter by assigned agent ID
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/ListWhatsAppAccountsResponse'
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
    GetWhatsAppAccountResponse:
      type: object
      properties:
        business_account_id:
          type: string
        phone_number_id:
          type: string
        business_account_name:
          type: string
        phone_number_name:
          type: string
        phone_number:
          type: string
        assigned_agent_id:
          type:
            - string
            - 'null'
        enable_messaging:
          type: boolean
          default: true
        enable_audio_message_response:
          type: boolean
          default: true
        assigned_agent_name:
          type:
            - string
            - 'null'
        is_token_expired:
          type: boolean
          default: false
      required:
        - business_account_id
        - phone_number_id
        - business_account_name
        - phone_number_name
        - phone_number
        - assigned_agent_name
      title: GetWhatsAppAccountResponse
    ListWhatsAppAccountsResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/GetWhatsAppAccountResponse'
      required:
        - items
      title: ListWhatsAppAccountsResponse
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
  "items": [
    {
      "business_account_id": "string",
      "phone_number_id": "string",
      "business_account_name": "string",
      "phone_number_name": "string",
      "phone_number": "string",
      "assigned_agent_name": "string",
      "assigned_agent_id": "string",
      "enable_messaging": true,
      "enable_audio_message_response": true,
      "is_token_expired": false
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsappAccounts.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp_accounts.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/whatsapp-accounts"

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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp-accounts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/whatsapp-accounts")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp-accounts");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp-accounts")! as URL,
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
