---
title: "List WhatsApp accounts"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/accounts/list.md
path: docs/eleven-agents/api-reference/whats-app/accounts/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List WhatsApp accounts

GET https://api.elevenlabs.io/v1/convai/whatsapp-accounts

List all WhatsApp accounts

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/accounts/list

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
        - whatsappAccounts
      parameters:
        - name: agent_id
          in: query
          description: Filter by assigned agent ID
          required: false
          schema:
            type: string
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
                $ref: '#/components/schemas/type_:ListWhatsAppAccountsResponse'
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
    type_:GetWhatsAppAccountResponse:
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
          type: string
        enable_messaging:
          type: boolean
          default: true
        enable_audio_message_response:
          type: boolean
          default: true
        assigned_agent_name:
          type: string
        is_token_expired:
          type: boolean
          default: false
      required:
        - business_account_id
        - phone_number_id
        - business_account_name
        - phone_number_name
        - phone_number
      title: GetWhatsAppAccountResponse
    type_:ListWhatsAppAccountsResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/type_:GetWhatsAppAccountResponse'
      required:
        - items
      title: ListWhatsAppAccountsResponse
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
  "items": [
    {
      "business_account_id": "business_account_id",
      "phone_number_id": "phone_number_id",
      "business_account_name": "business_account_name",
      "phone_number_name": "phone_number_name",
      "phone_number": "phone_number",
      "assigned_agent_id": "assigned_agent_id",
      "enable_messaging": true,
      "enable_audio_message_response": true,
      "assigned_agent_name": "assigned_agent_name",
      "is_token_expired": true
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsappAccounts.list({
        agentId: "agent_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp_accounts.list(
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")! as URL,
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
