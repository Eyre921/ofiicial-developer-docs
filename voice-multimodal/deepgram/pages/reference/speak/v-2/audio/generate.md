---
title: "Flux Text to Speech (batch)"
source: https://developers.deepgram.com/reference/speak/v-2/audio/generate.md
path: reference/speak/v-2/audio/generate
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux Text to Speech (batch)

POST https://api.deepgram.com/v2/speak
Content-Type: application/json

Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API. Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up front and you don't need incremental playback or interruption.

Reference: https://developers.deepgram.com/reference/speak/v-2/audio/generate

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v2/speak:
    post:
      operationId: generate
      summary: Flux Text to Speech (batch)
      description: >-
        Synthesize a complete block of text into a single audio response using
        Deepgram's Flux TTS batch (REST) API. Use this for pre-rendering fixed
        audio (IVR prompts, notifications, narration) where the whole text is
        known up front and you don't need incremental playback or interruption.
      tags:
        - speak > v2 > audio
      parameters:
        - name: callback
          in: query
          description: URL to which we'll make the callback request
          required: false
          schema:
            type: string
        - name: callback_method
          in: query
          description: HTTP method by which the callback request will be made
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersCallbackMethod'
            default: POST
        - name: mip_opt_out
          in: query
          description: >-
            Opts out requests from the Deepgram Model Improvement Program. Refer
            to our Docs for pricing impacts before setting this to true.
            https://dpgr.am/deepgram-mip
          required: false
          schema:
            type: boolean
            default: false
        - name: tag
          in: query
          description: >-
            Label your requests for the purpose of identification during usage
            reporting
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersTag'
        - name: bit_rate
          in: query
          description: >-
            The bitrate of the audio in bits per second. Choose from predefined
            ranges or specific values based on the encoding type.
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersBitRate'
            default: 48000
        - name: container
          in: query
          description: >-
            Container specifies the file format wrapper for the output audio.
            The available options depend on the encoding type.
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersContainer'
            default: wav
        - name: encoding
          in: query
          description: >-
            Encoding allows you to specify the expected encoding of your audio
            output
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersEncoding'
            default: mp3
        - name: model
          in: query
          description: >-
            Flux TTS model used to synthesize the submitted text, in the form
            `flux-{voice}-{language}` (for example, `flux-alexis-en`). Required;
            unlike the v1 (Aura) endpoint there is no default and only flux
            models are accepted. English-only at launch.
          required: true
          schema:
            type: string
        - name: sample_rate
          in: query
          description: >-
            Sample Rate specifies the sample rate for the output audio. Based on
            the encoding, different sample rates are supported. For some
            encodings, the sample rate is not configurable
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersSampleRate'
            default: 24000
        - name: priority
          in: query
          description: >-
            Processing priority for asynchronous (callback) requests. The only
            supported value is low.
          required: false
          schema:
            $ref: '#/components/schemas/V2SpeakPostParametersPriority'
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
          description: >-
            Returns the synthesized audio in the requested encoding as a binary
            stream. When a `callback` URL is supplied, the request is processed
            asynchronously and the response body is instead a JSON
            acknowledgement (Content-Type `application/json`) of the form
            {"request_id": "..."}, with the audio delivered to the callback URL.
            Because this endpoint is typed as a binary audio stream, SDK callers
            that set `callback` receive this JSON acknowledgement through the
            audio byte iterator as raw bytes and must join the chunks and parse
            `request_id` themselves.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpeakV2AcceptedResponse'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        description: Transform text to speech
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SpeakV2Request'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    V2SpeakPostParametersCallbackMethod:
      type: string
      enum:
        - POST
        - PUT
      default: POST
      title: V2SpeakPostParametersCallbackMethod
    V2SpeakPostParametersTag:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V2SpeakPostParametersTag
    V2SpeakPostParametersBitRate0:
      type: string
      enum:
        - '8000'
        - '16000'
        - '24000'
        - '32000'
        - '40000'
        - '48000'
      description: >-
        Encoding - mp3(default). Supported bitrates - 8000, 16000, 24000, 32000,
        40000, 48000(default) bps.
      title: V2SpeakPostParametersBitRate0
    V2SpeakPostParametersBitRate:
      oneOf:
        - $ref: '#/components/schemas/V2SpeakPostParametersBitRate0'
        - type: integer
        - type: integer
      title: V2SpeakPostParametersBitRate
    V2SpeakPostParametersContainer0:
      type: string
      enum:
        - none
      description: No container.
      title: V2SpeakPostParametersContainer0
    V2SpeakPostParametersContainer1:
      type: string
      enum:
        - wav
      description: >-
        Encoding - linear16. Supported container - wav (default), or no
        container.
      title: V2SpeakPostParametersContainer1
    V2SpeakPostParametersContainer2:
      type: string
      enum:
        - wav
      description: Encoding - mulaw. Supported container - wav (default), or no container.
      title: V2SpeakPostParametersContainer2
    V2SpeakPostParametersContainer3:
      type: string
      enum:
        - wav
      description: Encoding - alaw. Supported container - wav (default), or no container.
      title: V2SpeakPostParametersContainer3
    V2SpeakPostParametersContainer4:
      type: string
      enum:
        - ogg
      description: Encoding - opus. Supported container - ogg (default).
      title: V2SpeakPostParametersContainer4
    V2SpeakPostParametersContainer:
      oneOf:
        - $ref: '#/components/schemas/V2SpeakPostParametersContainer0'
        - $ref: '#/components/schemas/V2SpeakPostParametersContainer1'
        - $ref: '#/components/schemas/V2SpeakPostParametersContainer2'
        - $ref: '#/components/schemas/V2SpeakPostParametersContainer3'
        - $ref: '#/components/schemas/V2SpeakPostParametersContainer4'
      title: V2SpeakPostParametersContainer
    V2SpeakPostParametersEncoding0:
      type: string
      enum:
        - linear16
      description: >-
        Encoding - linear16. Uncompressed, high-quality audio format often used
        for telephony or audio processing.
      title: V2SpeakPostParametersEncoding0
    V2SpeakPostParametersEncoding1:
      type: string
      enum:
        - flac
      description: Encoding - flac. Lossless audio format for high-quality compression.
      title: V2SpeakPostParametersEncoding1
    V2SpeakPostParametersEncoding2:
      type: string
      enum:
        - mulaw
      description: Encoding - mulaw. Compressed audio format commonly used in telephony.
      title: V2SpeakPostParametersEncoding2
    V2SpeakPostParametersEncoding3:
      type: string
      enum:
        - alaw
      description: Encoding - alaw. Similar to mulaw but used in international telephony.
      title: V2SpeakPostParametersEncoding3
    V2SpeakPostParametersEncoding4:
      type: string
      enum:
        - mp3
      description: Encoding - mp3. Popular compressed audio format for music and streaming.
      title: V2SpeakPostParametersEncoding4
    V2SpeakPostParametersEncoding5:
      type: string
      enum:
        - opus
      description: >-
        Encoding - opus. High-compression audio format optimized for real-time
        communications.
      title: V2SpeakPostParametersEncoding5
    V2SpeakPostParametersEncoding6:
      type: string
      enum:
        - aac
      description: >-
        Encoding - aac. Advanced audio format offering better quality at smaller
        file sizes than mp3.
      title: V2SpeakPostParametersEncoding6
    V2SpeakPostParametersEncoding:
      oneOf:
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding0'
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding1'
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding2'
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding3'
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding4'
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding5'
        - $ref: '#/components/schemas/V2SpeakPostParametersEncoding6'
      title: V2SpeakPostParametersEncoding
    V2SpeakPostParametersSampleRate0:
      type: string
      enum:
        - '8000'
        - '16000'
        - '24000'
        - '32000'
        - '44100'
        - '48000'
      description: >-
        Encoding - linear16. Supported sample rates - 8000, 16000, 24000, 32000,
        44100, 48000 Hz.
      title: V2SpeakPostParametersSampleRate0
    V2SpeakPostParametersSampleRate1:
      type: string
      enum:
        - '8000'
        - '16000'
      description: Encoding - mulaw. Supported sample rates - 8000, 16000 Hz.
      title: V2SpeakPostParametersSampleRate1
    V2SpeakPostParametersSampleRate2:
      type: string
      enum:
        - '8000'
        - '16000'
      description: Encoding - alaw. Supported sample rates - 8000, 16000 Hz.
      title: V2SpeakPostParametersSampleRate2
    V2SpeakPostParametersSampleRate3:
      type: string
      enum:
        - '8000'
        - '16000'
        - '22050'
        - '32000'
        - '48000'
      description: >-
        Encoding - flac. Supported sample rates - 8000, 16000, 22050, 32000,
        48000 Hz.
      title: V2SpeakPostParametersSampleRate3
    V2SpeakPostParametersSampleRate:
      oneOf:
        - $ref: '#/components/schemas/V2SpeakPostParametersSampleRate0'
        - $ref: '#/components/schemas/V2SpeakPostParametersSampleRate1'
        - $ref: '#/components/schemas/V2SpeakPostParametersSampleRate2'
        - $ref: '#/components/schemas/V2SpeakPostParametersSampleRate3'
      title: V2SpeakPostParametersSampleRate
    V2SpeakPostParametersPriority:
      type: string
      enum:
        - low
      title: V2SpeakPostParametersPriority
    SpeakV2Request:
      type: object
      properties:
        text:
          type: string
          description: >-
            The text content to be converted to speech. The server normalizes
            and preprocesses the text (e.g. stripping inline controls) before
            synthesis.
      required:
        - text
      description: >-
        Request body for Flux TTS batch (REST) text-to-speech conversion. The
        full block of text is synthesized in a single request and returned as
        one audio response.
      title: SpeakV2Request
    SpeakV2AcceptedResponse:
      type: object
      properties:
        request_id:
          type: string
          format: uuid
          description: Unique identifier for tracking the asynchronous request
      required:
        - request_id
      description: >-
        Accepted response returned when a callback URL is supplied; the audio is
        delivered asynchronously to that URL.
      title: SpeakV2AcceptedResponse
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
    JwtAuth:
      type: http
      scheme: bearer
      description: |
        Use `Authorization: Bearer <JWT>`
        Example: `Authorization: Bearer eyJhbGciOiJ...`

```

## Examples



**Request**

```json
{
  "text": "Your appointment is confirmed for 3pm tomorrow."
}
```

**Response**

```json
{
  "request_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v2/speak"

querystring = {"model":"flux-alexis-en"}

payload = { "text": "Your appointment is confirmed for 3pm tomorrow." }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v2/speak?model=flux-alexis-en';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"text":"Your appointment is confirmed for 3pm tomorrow."}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v2/speak?model=flux-alexis-en"

	payload := strings.NewReader("{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
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

url = URI("https://api.deepgram.com/v2/speak?model=flux-alexis-en")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v2/speak?model=flux-alexis-en")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v2/speak?model=flux-alexis-en', [
  'body' => '{
  "text": "Your appointment is confirmed for 3pm tomorrow."
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v2/speak?model=flux-alexis-en");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Your appointment is confirmed for 3pm tomorrow.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["text": "Your appointment is confirmed for 3pm tomorrow."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v2/speak?model=flux-alexis-en")! as URL,
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
