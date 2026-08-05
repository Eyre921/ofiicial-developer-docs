---
title: "Delete a Project Self-Hosted Distribution Credential"
source: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/delete.md
path: reference/self-hosted/distribution-credentials/delete
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Delete a Project Self-Hosted Distribution Credential

DELETE https://api.deepgram.com/v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}

Deletes a set of distribution credentials for the specified project

Reference: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}:
    delete:
      operationId: delete
      summary: Delete a Project Self-Hosted Distribution Credential
      description: Deletes a set of distribution credentials for the specified project
      tags:
        - distributionCredentials
      parameters:
        - name: project_id
          in: path
          description: The unique identifier of the project
          required: true
          schema:
            type: string
        - name: distribution_credentials_id
          in: path
          description: The UUID of the distribution credentials
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: |
            Use `Authorization: Token <API_KEY>`
            Example: `Authorization: Token 12345abcdef`
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Single distribution credential
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetProjectDistributionCredentialsV1Response
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    GetProjectDistributionCredentialsV1ResponseMember:
      type: object
      properties:
        member_id:
          type: string
          format: uuid
          description: Unique identifier for the member
        email:
          type: string
          format: email
          description: Email address of the member
      required:
        - member_id
        - email
      title: GetProjectDistributionCredentialsV1ResponseMember
    GetProjectDistributionCredentialsV1ResponseDistributionCredentials:
      type: object
      properties:
        distribution_credentials_id:
          type: string
          format: uuid
          description: Unique identifier for the distribution credentials
        provider:
          type: string
          description: The provider of the distribution service
        comment:
          type: string
          description: Optional comment about the credentials
        scopes:
          type: array
          items:
            type: string
          description: List of permission scopes for the credentials
        created:
          type: string
          format: date-time
          description: Timestamp when the credentials were created
      required:
        - distribution_credentials_id
        - provider
        - scopes
        - created
      title: GetProjectDistributionCredentialsV1ResponseDistributionCredentials
    GetProjectDistributionCredentialsV1Response:
      type: object
      properties:
        member:
          $ref: >-
            #/components/schemas/GetProjectDistributionCredentialsV1ResponseMember
        distribution_credentials:
          $ref: >-
            #/components/schemas/GetProjectDistributionCredentialsV1ResponseDistributionCredentials
      required:
        - member
        - distribution_credentials
      title: GetProjectDistributionCredentialsV1Response
    ErrorResponseTextError:
      type: string
      title: ErrorResponseTextError
    ErrorResponseLegacyError:
      type: object
      properties:
        err_code:
          type: string
          description: The error code
        err_msg:
          type: string
          description: The error message
        request_id:
          type: string
          description: The request ID
      title: ErrorResponseLegacyError
    ErrorResponseModernError:
      type: object
      properties:
        category:
          type: string
          description: The category of the error
        message:
          type: string
          description: A message about the error
        details:
          type: string
          description: A description of the error
        request_id:
          type: string
          description: The unique identifier of the request
      title: ErrorResponseModernError
    ErrorResponse:
      oneOf:
        - $ref: '#/components/schemas/ErrorResponseTextError'
        - $ref: '#/components/schemas/ErrorResponseLegacyError'
        - $ref: '#/components/schemas/ErrorResponseModernError'
      title: ErrorResponse
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: |
        Use `Authorization: Token <API_KEY>`
        Example: `Authorization: Token 12345abcdef`

```

## Examples



**Response**

```json
{
  "member": {
    "member_id": "c7b9b131-73f3-11d9-8665-0b00d2e44b83",
    "email": "email@example.com"
  },
  "distribution_credentials": {
    "distribution_credentials_id": "82c32c10-53b2-4d23-993f-864b3d44502a",
    "provider": "quay",
    "scopes": [
      "self-hosted:product:api",
      "self-hosted:product:engine"
    ],
    "created": "2023-06-28T15:36:59.609841Z",
    "comment": "My Self-Hosted Distribution Credentials"
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3"

headers = {"Authorization": "Token <apiKey>"}

response = requests.delete(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3';
const options = {method: 'DELETE', headers: {Authorization: 'Token <apiKey>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Authorization", "Token <apiKey>")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Token <apiKey>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials/8b36cfd0-472f-4a21-833f-2d6343c3a2f3")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers

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
